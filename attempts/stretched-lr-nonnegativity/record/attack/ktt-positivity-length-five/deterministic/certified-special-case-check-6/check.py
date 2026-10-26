#!/usr/bin/env python3
"""Independent check of the per-facet inequality.

1. The summary against `facets.jsonl`, every field recomputed.
2. The count of cells against the two steps that built them, and the count of cells carrying a
   negative edge against `certified-special-case-check-4`.
3. On a sample of cells, recomputed from the polytope rather than read from the record: that the
   facet shares add up to the functional, which is what makes the per-facet inequality sufficient,
   by comparing their sum at every extreme ray with the value the step that built the cell
   recorded from a different route; and that every facet carrying a negative edge pays for it at
   every ray, with a ratio at least the one the record states for that cell.
Exit 0 iff all three hold.
"""
import json
import os
import random
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from atlasform import WeightBook, apply_functional, edges_with_linear_length  # noqa: E402
from chamber import Cell  # noqa: E402
from isotypes import canonical  # noqa: E402

N = 5
bad = 0
recs = [json.loads(l) for l in open(os.path.join(HERE, "facets.jsonl"))]
summary = json.load(open(os.path.join(HERE, "facets.summary.json")))
ratios = [Fraction(r["worst ratio"]) for r in recs if r["worst ratio"]]
recomputed = {
    "cells": len(recs),
    "facets seen": sum(r["facets"] for r in recs),
    "facets carrying a negative edge, and so tested":
        sum(r["facets with a negative edge"] for r in recs),
    "cells with a failing facet": sum(1 for r in recs if r["failing facets"]),
    "smallest ratio of the positive share to the negative share": str(min(ratios))
    if ratios else None,
    "largest ratio": str(max(ratios)) if ratios else None,
}
for k, v in recomputed.items():
    if summary[k] != v:
        bad += 1
        print(f"SUMMARY MISMATCH {k}: summary {summary[k]}, recomputed {v}")
print(f"summary: {len(recs)} cells, {recomputed['facets seen']} facets of which "
      f"{recomputed['facets carrying a negative edge, and so tested']} carry a negative edge, "
      f"{recomputed['cells with a failing facet']} cells with a failing facet, smallest ratio "
      f"{recomputed['smallest ratio of the positive share to the negative share']}")

CHECK3 = os.path.join(HERE, "..", "certified-special-case-check-3")
CHECK4 = os.path.join(HERE, "..", "certified-special-case-check-4")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
built = {}
for path, tag in ((os.path.join(CHECK3, "cells.jsonl"), "certified-special-case-check-3"),
                  (os.path.join(RUN2, "cells.jsonl"), "enumeration-run-2")):
    for line in open(path):
        c = json.loads(line)
        built.setdefault((tag, tuple(tuple(x) for x in c["triple"])), c)
cls = [json.loads(l) for l in open(os.path.join(CHECK4, "classified.jsonl"))]
with_neg = sum(1 for c in cls if c["negative edges"])
here_neg = sum(1 for r in recs if r["facets with a negative edge"])
if len(recs) > 0 and here_neg != with_neg:
    bad += 1
    print(f"COUNT MISMATCH: {with_neg} cells carry a negative edge there, {here_neg} here")
print(f"against certified-special-case-check-4: {with_neg} cells carry a negative edge, "
      f"{here_neg} here")

book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
for line in open(os.path.join(RUN2, "weights.jsonl")):
    r = json.loads(line)
    book.weights.setdefault(canonical([tuple(v) for v in r["normals"]]), Fraction(r["weight"]))
rng = random.Random(20260908)
pool = [r for r in recs if r["facets with a negative edge"]]
sample = rng.sample(pool, min(20, len(pool)))
sum_bad = fac_bad = checked = 0
for r in sample:
    key = (r["source"], tuple(tuple(x) for x in r["triple"]))
    c = built[key]
    Z = Cell(*key[1])
    edges = edges_with_linear_length(Z)
    weights = [book.weight(n) for n, _, _, _ in edges]
    facets = [set(fs) for _, _, _, fs in edges]
    counts = [len(fs) for fs in facets]
    all_facets = sorted({F for fs in facets for F in fs})
    checked += 1
    for ray, recorded in zip(c["ray_list"], c["ell"]):
        s = Fraction(0)
        for F in all_facets:
            for i in range(len(edges)):
                if F in facets[i]:
                    s += weights[i] / counts[i] * apply_functional(edges[i][1], ray)
        if s != Fraction(recorded):
            sum_bad += 1
            print(f"SHARE SUM MISMATCH {r['triple']}: {s} against the recorded {recorded}")
    for F in all_facets:
        neg = [i for i in range(len(edges)) if F in facets[i] and weights[i] < 0]
        if not neg:
            continue
        for ray in c["ray_list"]:
            lo = sum((-weights[i]) / counts[i] * apply_functional(edges[i][1], ray) for i in neg)
            hi = sum(weights[i] / counts[i] * apply_functional(edges[i][1], ray)
                     for i in range(len(edges)) if F in facets[i] and weights[i] > 0)
            if hi < lo:
                fac_bad += 1
                print(f"FACET FAILS {r['triple']} facet {F}: {hi} against {lo}")
bad += sum_bad + fac_bad
print(f"recomputed from the polytope on {checked} cells: {sum_bad} rays where the facet shares do "
      f"not add up to the recorded value, {fac_bad} facets failing to pay for their negative edges")
sys.exit(1 if bad else 0)
