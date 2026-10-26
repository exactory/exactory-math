#!/usr/bin/env python3
"""Independent check of the search and of the per-facet mechanism pass.

1. Both summaries against their record files, every field recomputed, including the failure count.
2. The band table's rows for the old data recomputed from `certified-special-case-check-6`.
3. On a sample of the new cells, the per-facet inequality recomputed from the polytope: the worst
   ratio must match the record and no facet may fail.
4. The mechanism claim recomputed from `per-facet.jsonl`: the median ratio grouped by the number
   of negative edges on the facet, and grouped by the cell's edge count, so that the two can be
   compared without trusting the run's own grouping.
Exit 0 iff all four hold.
"""
import json
import os
import random
import statistics
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from atlasform import WeightBook, apply_functional, edges_with_linear_length  # noqa: E402
from chamber import Cell  # noqa: E402
from isotypes import canonical  # noqa: E402

CHECK6 = os.path.join(HERE, "..", "certified-special-case-check-6")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
N = 5
bad = 0


def band(e):
    b = 1
    while b * 2 <= e:
        b *= 2
    return b


new = [json.loads(l) for l in open(os.path.join(HERE, "search.jsonl"))]
s1 = json.load(open(os.path.join(HERE, "search.summary.json")))
above = [r for r in new if r["edges"] > 684]
rec1 = {
    "cells tested here": len(new),
    "of them above 684 edges": len(above),
    "facet ray tests here": sum(r["facet tests"] for r in new),
    "facet ray tests above 684 edges": sum(r["facet tests"] for r in above),
    "failing facets": sum(len(r["failures"]) for r in new),
    "largest cell by edges": max(r["edges"] for r in new),
}
for k, v in rec1.items():
    if s1[k] != v:
        bad += 1
        print(f"SEARCH SUMMARY MISMATCH {k}: {s1[k]} against {v}")
print(f"search: {len(new)} cells, {len(above)} above 684 edges, {rec1['facet ray tests here']} "
      f"facet ray tests, {rec1['failing facets']} failing facets, largest cell "
      f"{rec1['largest cell by edges']} edges")

old = [json.loads(l) for l in open(os.path.join(CHECK6, "facets.jsonl"))]
old_bands = {}
for r in old:
    if r["worst ratio"]:
        old_bands.setdefault(band(r["edges"]), []).append(float(Fraction(r["worst ratio"])))
tbl = {row["band"]: row for row in s1["bands, old and new together"]}
for b, v in old_bands.items():
    newv = [float(Fraction(r["worst ratio"])) for r in new if r["worst ratio"] and r["band"] == b]
    both = v + newv
    if tbl[b]["cells"] != len(both) or abs(tbl[b]["median"] - statistics.median(both)) > 0.01:
        bad += 1
        print(f"BAND MISMATCH {b}: {tbl[b]} against {len(both)} cells median "
              f"{statistics.median(both)}")
print(f"bands: {len(old_bands)} bands of the old data recomputed and merged with the new, "
      f"0 mismatches" if not bad else "")

book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
for line in open(os.path.join(RUN2, "weights.jsonl")):
    r = json.loads(line)
    book.weights.setdefault(canonical([tuple(v) for v in r["normals"]]), Fraction(r["weight"]))
rng = random.Random(20260910)
sample = rng.sample([r for r in new if r["worst ratio"]], min(8, len(new)))
cell_bad = fail_bad = 0
for r in sample:
    Z = Cell(*tuple(tuple(x) for x in r["triple"]))
    edges = edges_with_linear_length(Z)
    weights = [book.weight(n) for n, _, _, _ in edges]
    fs = [set(f) for _, _, _, f in edges]
    counts = [len(f) for f in fs]
    K, eqs, ineqs = Z.cone()
    rays = [tuple(int(x) for x in y) for y in K.ExtremeRays()]
    worst = None
    for F in sorted({x for f in fs for x in f}):
        neg = [i for i in range(len(edges)) if F in fs[i] and weights[i] < 0]
        if not neg:
            continue
        left = [Fraction(0)] * Z.B
        for i in neg:
            left = [t + (-weights[i]) / counts[i] * x for t, x in zip(left, edges[i][1])]
        right = [Fraction(0)] * Z.B
        for i in range(len(edges)):
            if F in fs[i] and weights[i] > 0:
                right = [t + weights[i] / counts[i] * x for t, x in zip(right, edges[i][1])]
        for ray in rays:
            lo, hi = apply_functional(left, ray), apply_functional(right, ray)
            if lo > 0:
                if worst is None or hi / lo < worst:
                    worst = hi / lo
                if hi < lo:
                    fail_bad += 1
            elif hi < 0:
                fail_bad += 1
    if worst is None or worst != Fraction(r["worst ratio"]):
        cell_bad += 1
        print(f"CELL MISMATCH {r['triple']}: recomputed {worst} against {r['worst ratio']}")
bad += cell_bad + fail_bad
print(f"recomputed from the polytope on {len(sample)} of the new cells: {cell_bad} worst ratios "
      f"disagreeing, {fail_bad} facets failing")

pf = [json.loads(l) for l in open(os.path.join(HERE, "per-facet.jsonl"))]
s2 = json.load(open(os.path.join(HERE, "per-facet.summary.json")))
if s2["facets carrying a negative edge"] != len(pf):
    bad += 1
    print(f"MECHANISM COUNT MISMATCH: {s2['facets carrying a negative edge']} against {len(pf)}")


def med(key):
    g = {}
    for r in pf:
        g.setdefault(key(r), []).append(float(Fraction(r["worst ratio"])))
    return {k: round(statistics.median(v), 2) for k, v in sorted(g.items())}


by_neg = med(lambda r: r["negative edges on the facet"])
by_edges = med(lambda r: band(r["cell edges"]))
for k, v in by_neg.items():
    if abs(s2["by the number of negative edges on the facet"][str(k)]["median ratio"] - v) > 0.01:
        bad += 1
        print(f"MECHANISM MISMATCH at {k} negative edges")
spread_neg = max(by_neg.values()) / min(by_neg.values())
spread_edges = max(by_edges.values()) / min(by_edges.values())
print(f"mechanism: {len(pf)} facets; median ratio by the number of negative edges on the facet "
      f"{by_neg}, spread {spread_neg:.2f}; by the cell's edge count {by_edges}, spread "
      f"{spread_edges:.2f}")
sys.exit(1 if bad else 0)
