#!/usr/bin/env python3
"""Addendum: the cell's size acts on the margin through the per-facet negative-edge count.

Move 12 read the two groupings of `per-facet.jsonl` side by side and concluded that the driver is
the per-facet negative-edge count and not the cell's size. That is too strong. This script
regroups the same records, adding nothing, to separate the two: how the count itself grows with
the cell, and whether the count still moves the ratio once the cell's size is held fixed.
"""
import json
import os
import statistics
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
recs = [json.loads(l) for l in open(os.path.join(HERE, "per-facet.jsonl"))]


def band(e):
    b = 1
    while b * 2 <= e:
        b *= 2
    return b


by_band = {}
for r in recs:
    by_band.setdefault(band(r["cell edges"]), []).append(r["negative edges on the facet"])
counts = {b: {"facets": len(v), "maximum count": max(v), "mean count": round(sum(v) / len(v), 2),
              "share of facets with three or more": round(sum(1 for x in v if x >= 3) / len(v), 3)}
          for b, v in sorted(by_band.items())}

by_rank = {}
for r in recs:
    by_rank.setdefault(r["cell rank"], []).append(r["negative edges on the facet"])
ranks = {k: {"facets": len(v), "maximum count": max(v), "mean count": round(sum(v) / len(v), 2)}
         for k, v in sorted(by_rank.items())}

fixed = {}
for r in recs:
    if band(r["cell edges"]) == 512:
        fixed.setdefault(r["negative edges on the facet"], []).append(
            float(Fraction(r["worst ratio"])))
within = {k: {"facets": len(v), "median ratio": round(statistics.median(v), 2),
              "worst ratio": round(min(v), 2)} for k, v in sorted(fixed.items())}

out = {
    "the per-facet negative-edge count, by the cell's edge-count band": counts,
    "the same, by the cell's rank": ranks,
    "the margin against the count, inside the 512-edge band only": within,
    "maximum count observed": max(r["negative edges on the facet"] for r in recs),
    "reading": ("the count grows with the cell, from a maximum of 1 and a mean of 1.00 in the "
                "64-edge band to a maximum of 7 and a mean of 1.77 in the 256- and 512-edge "
                "bands, and the count still moves the margin with the cell's size held fixed, so "
                "the cell's size acts on the margin through the count rather than not at all"),
}
json.dump(out, open(os.path.join(HERE, "mediation.json"), "w"), indent=2)
print(json.dumps(out, indent=2))
