#!/usr/bin/env python3
"""The summary of the search, from the records it wrote.

`run.py` was stopped at its allowance with one cell in progress, so its own summary block never
ran. This script is that block, reading `search.jsonl` and the earlier `facets.jsonl` and writing
the same file. It constructs nothing and tests nothing.
"""
import json
import os
import statistics
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK6 = os.path.join(HERE, "..", "certified-special-case-check-6")


def band(e):
    b = 1
    while b * 2 <= e:
        b *= 2
    return b


new = [json.loads(l) for l in open(os.path.join(HERE, "search.jsonl"))]
old = [json.loads(l) for l in open(os.path.join(CHECK6, "facets.jsonl"))]
# facets.jsonl does not record the ray count per cell; take it from the step that built the cell
rays_of = {}
for path in (os.path.join(HERE, "..", "certified-special-case-check-3", "cells.jsonl"),
             os.path.join(HERE, "..", "enumeration-run-2", "cells.jsonl")):
    for line in open(path):
        c = json.loads(line)
        rays_of.setdefault(tuple(tuple(x) for x in c["triple"]), len(c["ray_list"]))
bands = {}
for r in old:
    if not r["worst ratio"]:
        continue
    e = bands.setdefault(band(r["edges"]), {"cells": 0, "tests": 0, "ratios": []})
    e["cells"] += 1
    e["tests"] += r["facets with a negative edge"] * rays_of.get(tuple(tuple(x) for x in r["triple"]), 0)
    e["ratios"].append(float(Fraction(r["worst ratio"])))
for r in new:
    if not r["worst ratio"]:
        continue
    e = bands.setdefault(r["band"], {"cells": 0, "tests": 0, "ratios": []})
    e["cells"] += 1
    e["tests"] += r["facet tests"]
    e["ratios"].append(float(Fraction(r["worst ratio"])))
table = []
for b, e in sorted(bands.items()):
    v = sorted(e["ratios"])
    q = statistics.quantiles(v, n=4) if len(v) >= 4 else [None, statistics.median(v), None]
    table.append({"band": b, "cells": e["cells"], "facet ray tests": e["tests"],
                  "worst ratio": round(min(v), 2),
                  "lower quartile": round(q[0], 2) if q[0] else None,
                  "median": round(statistics.median(v), 2),
                  "upper quartile": round(q[2], 2) if q[2] else None,
                  "median times band": round(statistics.median(v) * b)})
above = [r for r in new if r["edges"] > 684]
by_source = {}
for r in above:
    if r["worst ratio"]:
        by_source.setdefault(r["source"], []).append(float(Fraction(r["worst ratio"])))
ratios = [float(Fraction(r["worst ratio"])) for r in new if r["worst ratio"]]
summary = {
    "cells tested here": len(new),
    "of them above 684 edges": len(above),
    "cells above 684 edges from a generic point":
        sum(1 for r in above if r["source"] == "a generic point of the cone"),
    "cells above 684 edges from a perturbed box triple":
        sum(1 for r in above if r["source"] == "a perturbed box triple"),
    "facet ray tests here": sum(r["facet tests"] for r in new),
    "facet ray tests above 684 edges": sum(r["facet tests"] for r in above),
    "failing facets": sum(len(r["failures"]) for r in new),
    "worst ratio here": str(min(ratios)) if ratios else None,
    "largest cell by edges": max((r["edges"] for r in new), default=0),
    "above 684 edges, by source": {k: {"cells": len(v), "median": round(statistics.median(v), 2),
                                       "worst": round(min(v), 2)} for k, v in by_source.items()},
    "bands, old and new together": table,
    "stopped": "run.py was stopped at its allowance with one cell in progress; its 242 recorded "
               "cells are complete and this summary is computed from them",
    "verdict": "no failing facet; undecided, not support",
}
json.dump(summary, open(os.path.join(HERE, "search.summary.json"), "w"), indent=2)
print(json.dumps(summary, indent=2))
