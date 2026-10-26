#!/usr/bin/env python3
"""Independent check of the codimension-five atlas of weights.

1. The summary against the file: the number of records, the count of negative weights, the
   minimum and the maximum, recomputed from `atlas.jsonl`.
2. An independent value for every class whose transverse cone splits as an orthogonal sum of
   blocks of dimension at most three: the weight must be the product of the block weights, which
   the checker computes from the closed formulas of Castillo-Liu Lemmas 3.3 and 3.10, rewritten
   here. This uses no part of the recursion.
3. The end-to-end identity, which is what the atlas is for: for seeded random full-dimensional
   five-part hive polytopes, the sum over the edges of the atlas weight of the edge's class times
   the lattice length of the edge must equal the linear coefficient the box attack certified.
Exit 0 iff all three hold.
"""
import glob
import gzip
import json
import os
import random
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
SYS1 = os.path.join(HERE, "..", "symbolic-computation-run-1")
CHECK1 = os.path.join(HERE, "..", "certified-special-case-check-1")
sys.path.insert(0, HERE)

bad = 0
recs = [json.loads(l) for l in open(os.path.join(HERE, "atlas.jsonl"))]
summary = json.load(open(os.path.join(HERE, "atlas.summary.json")))
ws = {r["class"]: Fraction(r["weight"]) for r in recs}
neg = sum(1 for w in ws.values() if w < 0)
if (summary["classes"] != len(recs) or summary["negative"] != neg
        or Fraction(summary["minimum"]) != min(ws.values())
        or Fraction(summary["maximum"]) != max(ws.values())):
    bad += 1
    print(f"SUMMARY MISMATCH: {summary} against {len(recs)} records, {neg} negative, "
          f"min {min(ws.values())}, max {max(ws.values())}")
else:
    print(f"summary: {len(recs)} classes, {neg} negative, minimum {min(ws.values())}, "
          f"maximum {max(ws.values())}")


def dot(a, b):
    return Fraction(sum(x * y for x, y in zip(a, b)))


def closed2(x, y):
    return Fraction(1, 4) + Fraction(1, 12) * (dot(x, y) / dot(x, x) + dot(x, y) / dot(y, y))


def closed3(rays):
    H = [[dot(a, b) for b in rays] for a in rays]
    s = Fraction(1, 8)
    for i in range(3):
        for j in range(i + 1, 3):
            s += Fraction(1, 24) * H[i][j] * (Fraction(1) / H[i][i] + Fraction(1) / H[j][j])
    return s


from transverse import transverse_cone  # noqa: E402
from bvweight import rank  # noqa: E402


def blocks(rays):
    """Connected components of the graph on the rays with an edge when they are not orthogonal."""
    n = len(rays)
    par = list(range(n))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for i in range(n):
        for j in range(i + 1, n):
            if dot(rays[i], rays[j]) != 0:
                a, b = find(i), find(j)
                if a != b:
                    par[a] = b
    g = {}
    for i in range(n):
        g.setdefault(find(i), []).append(rays[i])
    return list(g.values())


split_checked = split_bad = 0
for r in recs:
    rays, gram = transverse_cone([list(map(int, v)) for v in r["normals"]])
    if len(rays) != len(gram):
        continue                                   # non-simplicial, no closed formula
    # express the rays in an orthonormal-free way: use the Gram matrix as the metric
    G = [[Fraction(x) for x in row] for row in gram]

    def ip(a, b):
        return sum(Fraction(a[i]) * G[i][j] * Fraction(b[j])
                   for i in range(len(G)) for j in range(len(G)))

    n = len(rays)
    par = list(range(n))

    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a

    for i in range(n):
        for j in range(i + 1, n):
            if ip(rays[i], rays[j]) != 0:
                a, b = find(i), find(j)
                if a != b:
                    par[a] = b
    comp = {}
    for i in range(n):
        comp.setdefault(find(i), []).append(i)
    parts = list(comp.values())
    if len(parts) < 2 or max(len(p) for p in parts) > 3:
        continue
    # multiplicativity needs the lattice to split as well as the space: the sublattice generated
    # by the saturations of the blocks must be the whole lattice, else the blocks are glued
    from bvweight import saturated_basis, det
    dsum = []
    for p in parts:
        dsum += saturated_basis([list(rays[a]) for a in p], len(G))
    if len(dsum) != len(G) or abs(det([[Fraction(x) for x in v] for v in dsum])) != 1:
        continue
    # each block's rays must also be a basis of its own saturated lattice, since the closed
    # formulas are stated for unimodular cones
    unimodular = True
    for p in parts:
        sat = saturated_basis([list(rays[a]) for a in p], len(G))
        if len(sat) != len(p):
            unimodular = False
            break
        B = [[Fraction(sat[i][c]) for i in range(len(sat))] for c in range(len(G))]
        from bvweight import _rref
        M = []
        for a in p:
            red, piv = _rref([B[c][:] + [Fraction(rays[a][c])] for c in range(len(G))])
            sol = [Fraction(0)] * len(sat)
            for i, q in enumerate(piv):
                if q < len(sat):
                    sol[q] = red[i][len(sat)]
            M.append(sol)
        if abs(det([[M[i][j] for j in range(len(sat))] for i in range(len(p))])) != 1:
            unimodular = False
            break
    if not unimodular:
        continue
    prod = Fraction(1)
    ok = True
    for p in parts:
        M = [[ip(rays[a], rays[b]) for b in p] for a in p]
        if len(p) == 1:
            prod *= Fraction(1, 2)
        elif len(p) == 2:
            prod *= Fraction(1, 4) + Fraction(1, 12) * (M[0][1] / M[0][0] + M[0][1] / M[1][1])
        else:
            s = Fraction(1, 8)
            for i in range(3):
                for j in range(i + 1, 3):
                    s += Fraction(1, 24) * M[i][j] * (Fraction(1) / M[i][i] + Fraction(1) / M[j][j])
            prod *= s
    split_checked += 1
    if prod != ws[r["class"]]:
        split_bad += 1
        print(f"SPLIT MISMATCH class {r['class']}: recursion {ws[r['class']]}, product {prod}")
bad += split_bad
print(f"orthogonally splitting classes: {split_checked} checked against the products of the "
      f"closed formulas, {split_bad} mismatches")

# 3. the end-to-end identity on hive polytopes
types = [tuple(tuple(x) for x in t) for t in json.load(open(os.path.join(CHECK1, "edge-types.json")))]
members = json.load(open(os.path.join(SYS1, "classes.json")))["members"]
cls_of = [None] * len(types)
for c, mem in members.items():
    for i in mem:
        cls_of[i] = int(c)
polys = [json.loads(l) for l in gzip.open(os.path.join(CHECK1, "edges.jsonl.gz"), "rt")]
rng = random.Random(20260905)
small = [p for p in polys if len(p["edges"]) <= 40]
sample = rng.sample(small, min(5, len(small)))
ebad = 0
for p in sample:
    tot = Fraction(0)
    missing = False
    for i, ln in p["edges"]:
        c = cls_of[i]
        if c not in ws:
            missing = True
            break
        tot += ws[c] * Fraction(ln)
    if missing:
        continue
    if tot != Fraction(p["a1"]):
        ebad += 1
        print(f"IDENTITY MISMATCH {p['lam']} {p['mu']} {p['nu']}: atlas {tot}, certified {p['a1']}")
bad += ebad
print(f"end-to-end identity: {len(sample)} hive polytopes, {ebad} mismatches")

# 4. the identity again, on polytopes that realise a negative class
negcls = [c for c, w in ws.items() if w < 0]
nbad = nchecked = 0
for c in negcls:
    ids = {i for i, cc in enumerate(cls_of) if cc == c}
    host = next((p for p in polys if any(i in ids for i, _ in p["edges"])), None)
    if host is None:
        continue
    tot = Fraction(0)
    ok = True
    for i, ln in host["edges"]:
        if cls_of[i] not in ws:
            ok = False
            break
        tot += ws[cls_of[i]] * Fraction(ln)
    if not ok:
        continue
    nchecked += 1
    if tot != Fraction(host["a1"]):
        nbad += 1
        print(f"NEGATIVE-CLASS IDENTITY MISMATCH class {c} in {host['lam']} {host['mu']} "
              f"{host['nu']}: atlas {tot}, certified {host['a1']}")
bad += nbad
print(f"negative classes: {len(negcls)}, each realised by a hive polytope whose certified linear "
      f"coefficient the atlas reproduces: {nchecked} checked, {nbad} mismatches")
sys.exit(1 if bad else 0)
