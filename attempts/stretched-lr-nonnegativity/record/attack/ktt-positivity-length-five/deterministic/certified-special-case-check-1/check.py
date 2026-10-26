#!/usr/bin/env python3
"""Independent check of the local-formula extraction run.

1. The summary is consistent with the files: the number of polytope records in `edges.jsonl.gz`,
   the number of edge types in `edge-types.json`, the total edge count, and zero mismatches.
2. The right-hand sides are the certified ones: for 200 seeded random records the linear
   coefficient stored here equals the coefficient recorded by `enumeration-run-2` of the box
   attack for the same triple, whose polynomials were pinned independently by lrcalc.
3. The edge extraction is independent of the vertex-pair method the run used: for 20 seeded
   random polytopes the edges are recomputed from Normaliz's face lattice at codimension
   dim - 1, and each edge's lattice length from Normaliz's `Volume` of the one-dimensional face,
   then compared with the run's records as multisets of (normal set, length).
4. The weight formula passes its own self-test, written here: the four vertex cones of the unit
   square and the three of the unimodular triangle have weights summing to the Ehrhart constant
   term 1.
Exit 0 iff all four hold.
"""
import glob
import gzip
import json
import os
import random
import sys
from fractions import Fraction
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
RUN2 = os.path.join(HERE, "..", "..", "..", "stretched-lr-polynomial-negative-coefficient",
                    "deterministic", "enumeration-run-2")
sys.path.insert(0, HERE)

bad = 0
summary = json.load(open(os.path.join(HERE, "validation.summary.json")))
types = json.load(open(os.path.join(HERE, "edge-types.json")))
recs = [json.loads(l) for l in gzip.open(os.path.join(HERE, "edges.jsonl.gz"), "rt")]
mism = json.load(open(os.path.join(HERE, "validation.mismatches.json")))

if (summary["polytopes"] != len(recs) or summary["edge_types"] != len(types)
        or summary["edges_total"] != sum(len(r["edges"]) for r in recs)
        or summary["mismatches"] != 0 or len(mism) != 0
        or summary["agree_top_three"] != len(recs)):
    bad += 1
    print(f"SUMMARY MISMATCH: {summary}, records {len(recs)}, types {len(types)}, "
          f"edges {sum(len(r['edges']) for r in recs)}, mismatch entries {len(mism)}")
else:
    print(f"summary: {len(recs)} polytopes, all {summary['agree_top_three']} agree on the top "
          f"three coefficients, {len(types)} edge types, {summary['edges_total']} edges, "
          f"0 mismatches")

# 2. right-hand sides against the certified records
cert = {}
for fn in sorted(glob.glob(os.path.join(RUN2, "scan-n5-*.jsonl"))):
    with open(fn) as f:
        for line in f:
            r = json.loads(line)
            if r.get("dim") == 6:
                cert[(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))] = r["coeffs"][1]
rng = random.Random(20260905)
sample = rng.sample(recs, min(200, len(recs)))
rbad = 0
for r in sample:
    key = (tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))
    if key not in cert or Fraction(cert[key]) != Fraction(r["a1"]):
        rbad += 1
        print(f"RIGHT-HAND SIDE MISMATCH {key}: here {r['a1']}, run-2 {cert.get(key)}")
bad += rbad
print(f"right-hand sides: {len(sample)} records against the certified run-2 coefficients, "
      f"{rbad} mismatches")

# 3. edges from Normaliz's face lattice, independent of the vertex-pair method
from PyNormaliz import Cone  # noqa: E402
sys.path.insert(0, os.path.join(HERE))
from hivepoly import hive_inequalities  # noqa: E402


def primitive(v):
    g = 0
    for x in v:
        g = gcd(g, abs(int(x)))
    return tuple(int(x) // g for x in v) if g else tuple(int(x) for x in v)


def as_frac(v):
    return Fraction(v[0], v[1]) if isinstance(v, list) else Fraction(v)


ebad = 0
esample = rng.sample(recs, min(20, len(recs)))
for r in esample:
    D, rows = hive_inequalities(r["lam"], r["mu"], r["nu"])
    C = Cone(inhom_inequalities=rows)
    sh = C.SupportHyperplanes()
    normals = [primitive([-a for a in h[:D]]) for h in sh]
    C.SetFaceCodimBound(D - 1)
    mine = []
    for bits, codim in C.FaceLattice():
        if codim != D - 1:
            continue
        act = [i for i, b in enumerate(bits) if b]
        F = Cone(inhom_equations=[sh[i] for i in act], inhom_inequalities=sh)
        if F.AffineDim() != 1:
            continue
        mine.append((tuple(sorted(normals[i] for i in act)), as_frac(F.Volume())))
    theirs = [(tuple(tuple(x) for x in types[i]), Fraction(ln)) for i, ln in r["edges"]]
    if sorted(mine) != sorted(theirs):
        ebad += 1
        print(f"EDGE MISMATCH {r['lam']} {r['mu']} {r['nu']}: "
              f"{len(mine)} from the face lattice, {len(theirs)} from the run")
bad += ebad
print(f"edges from Normaliz's face lattice with its own volumes: {len(esample)} polytopes, "
      f"{ebad} mismatches")

# 4. the weight formula's self-test, written here
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def alpha2(x, y):
    """Weight of a unimodular two-dimensional cone with rays x, y (Castillo-Liu Lemma 3.3)."""
    return Fraction(1, 4) + Fraction(1, 12) * (Fraction(dot(x, y), dot(x, x))
                                               + Fraction(dot(x, y), dot(y, y)))


square = (alpha2((1, 0), (0, 1)) + alpha2((-1, 0), (0, 1))
          + alpha2((1, 0), (0, -1)) + alpha2((-1, 0), (0, -1)))
tri = (alpha2((1, 0), (0, 1)) + alpha2((-1, 0), (-1, 1)) + alpha2((0, -1), (1, -1)))
if square != 1 or tri != 1:
    bad += 1
    print(f"WEIGHT SELF-TEST FAILED: square {square}, triangle {tri}")
else:
    print("weight self-test: the vertex weights of the unit square and of the unimodular "
          "triangle each sum to 1")

sys.exit(1 if bad else 0)
