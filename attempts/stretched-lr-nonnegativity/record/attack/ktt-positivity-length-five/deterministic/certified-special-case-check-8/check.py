#!/usr/bin/env python3
"""Independent check of the row-support census.

1. The summary recomputed from `rows.jsonl`.
2. The row count against the ray counts recorded by the steps that built the cells.
3. On a sample of cells, the lengths recomputed from the polytope: every zero row must have every
   edge length exactly zero, and the recorded ray value must equal the sum over the edges of the
   weight times the length, which ties this census to the steps before it.
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

CHECK3 = os.path.join(HERE, "..", "certified-special-case-check-3")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
bad = 0
recs = [json.loads(l) for l in open(os.path.join(HERE, "rows.jsonl"))]
s = json.load(open(os.path.join(HERE, "rows.summary.json")))
rows = [r for c in recs for r in c["rows"]]
recomputed = {
    "cells": len(recs),
    "rows": len(rows),
    "rows whose value is zero": sum(1 for r in rows if Fraction(r["value"]) == 0),
    "of those, rows with a non-empty support":
        sum(1 for r in rows if Fraction(r["value"]) == 0 and r["edges of positive length"]),
    "rows whose value is positive": sum(1 for r in rows if Fraction(r["value"]) != 0),
    "of those, rows with an empty support":
        sum(1 for r in rows if Fraction(r["value"]) != 0 and not r["edges of positive length"]),
}
for k, v in recomputed.items():
    if s[k] != v:
        bad += 1
        print(f"SUMMARY MISMATCH {k}: {s[k]} against {v}")
print(f"summary: {len(recs)} cells, {len(rows)} rows, "
      f"{recomputed['rows whose value is zero']} of value zero, of which "
      f"{recomputed['of those, rows with a non-empty support']} have a support")

built = {}
for path in (os.path.join(CHECK3, "cells.jsonl"), os.path.join(RUN2, "cells.jsonl")):
    for line in open(path):
        c = json.loads(line)
        built.setdefault(tuple(tuple(x) for x in c["triple"]), c)
count_bad = 0
for r in recs:
    c = built.get(tuple(tuple(x) for x in r["triple"]))
    if c is None or len(c["ray_list"]) != len(r["rows"]):
        count_bad += 1
bad += count_bad
print(f"row counts against the steps that built the cells: {len(recs)} cells, {count_bad} "
      f"mismatches")

book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
for line in open(os.path.join(RUN2, "weights.jsonl")):
    x = json.loads(line)
    book.weights.setdefault(canonical([tuple(v) for v in x["normals"]]), Fraction(x["weight"]))
rng = random.Random(20260915)
zero_bad = val_bad = checked = 0
for r in rng.sample(recs, 8):
    key = tuple(tuple(x) for x in r["triple"])
    c = built[key]
    Z = Cell(*key)
    edges = edges_with_linear_length(Z)
    weights = [book.weight(n) for n, _, _, _ in edges]
    for ray, val in zip(c["ray_list"], c["ell"]):
        lens = [apply_functional(row, ray) for _, row, _, _ in edges]
        checked += 1
        if Fraction(val) == 0 and any(x != 0 for x in lens):
            zero_bad += 1
            print(f"ZERO ROW WITH A SUPPORT {r['triple']}")
        if sum(w * x for w, x in zip(weights, lens)) != Fraction(val):
            val_bad += 1
            print(f"VALUE MISMATCH {r['triple']}")
bad += zero_bad + val_bad
print(f"recomputed from the polytope on 8 cells and {checked} rows: {zero_bad} zero rows with a "
      f"support, {val_bad} ray values disagreeing with the step that built the cell")
sys.exit(1 if bad else 0)
