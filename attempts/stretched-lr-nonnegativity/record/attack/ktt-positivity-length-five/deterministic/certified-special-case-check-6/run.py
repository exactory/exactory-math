#!/usr/bin/env python3
"""The per-facet inequality: does each facet pay for its own negative edges?

Every edge f of a hive polytope lies on c(f) facets. Give each facet F containing f the amount
w(f) * (lattice length of f) / c(f). Summed over the facets, these shares are exactly

    l(b) = sum over the edges of w(f) * (lattice length of f)(b),

so l >= 0 follows as soon as every facet has

    sum over the negative edges e on F of |w(e)| * len(e) / c(e)
        <=  sum over the positive edges f on F of w(f) * len(f) / c(f).

That is a statement about one facet of a hive polytope and nothing else: no cell, no chamber
complex, no size. Both sides are linear on a cell, so the inequality on the whole cell is decided
at the cell's extreme rays. This run measures it there, on every cell the project has built.
"""
from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from atlasform import WeightBook, apply_functional, edges_with_linear_length  # noqa: E402
from chamber import Cell  # noqa: E402
from isotypes import canonical  # noqa: E402

CHECK3 = os.path.join(HERE, "..", "certified-special-case-check-3")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
BUDGET = float(os.environ.get("BUDGET", "2400"))
N = 5


def main():
    book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
    for line in open(os.path.join(RUN2, "weights.jsonl")):
        r = json.loads(line)
        book.weights.setdefault(canonical([tuple(v) for v in r["normals"]]), Fraction(r["weight"]))

    cells = []
    for path, tag in ((os.path.join(CHECK3, "cells.jsonl"), "certified-special-case-check-3"),
                      (os.path.join(RUN2, "cells.jsonl"), "enumeration-run-2")):
        for line in open(path):
            cells.append((tag, json.loads(line)))

    out = open(os.path.join(HERE, "facets.jsonl"), "w")
    t0 = time.time()
    done = facets_seen = facets_tested = failures = ray_tests = 0
    worst = None
    identity_bad = 0
    for tag, c in cells:
        if time.time() - t0 > BUDGET:
            break
        w = tuple(tuple(x) for x in c["triple"])
        Z = Cell(*w)
        edges = edges_with_linear_length(Z)
        weights = [book.weight(n) for n, _, _, _ in edges]
        facets = [set(fs) for _, _, _, fs in edges]
        counts = [len(fs) for fs in facets]
        all_facets = sorted({F for fs in facets for F in fs})
        # the shares add up to the functional: check it at every ray
        total = [Fraction(0)] * Z.B
        for i, (_, row, _, _) in enumerate(edges):
            total = [t + weights[i] * x for t, x in zip(total, row)]
        for ray, recorded in zip(c["ray_list"], c["ell"]):
            if apply_functional(total, ray) != Fraction(recorded):
                identity_bad += 1
        rec = {"source": tag, "triple": c["triple"], "edges": len(edges),
               "facets": len(all_facets), "facets with a negative edge": 0, "worst ratio": None,
               "failing facets": []}
        cell_worst = None
        for F in all_facets:
            facets_seen += 1
            neg = [i for i in range(len(edges)) if F in facets[i] and weights[i] < 0]
            if not neg:
                continue
            rec["facets with a negative edge"] += 1
            facets_tested += 1
            left = [Fraction(0)] * Z.B
            for i in neg:
                left = [t + (-weights[i]) / counts[i] * x for t, x in zip(left, edges[i][1])]
            right = [Fraction(0)] * Z.B
            for i in range(len(edges)):
                if F in facets[i] and weights[i] > 0:
                    right = [t + weights[i] / counts[i] * x for t, x in zip(right, edges[i][1])]
            for ray in c["ray_list"]:
                lo, hi = apply_functional(left, ray), apply_functional(right, ray)
                ray_tests += 1
                if lo > 0:
                    ratio = hi / lo
                    if cell_worst is None or ratio < cell_worst:
                        cell_worst = ratio
                    if worst is None or ratio < worst[0]:
                        worst = (ratio, c["triple"], F)
                    if hi < lo:
                        failures += 1
                        rec["failing facets"].append({"facet": F, "left": str(lo),
                                                      "right": str(hi)})
                elif hi < 0:
                    failures += 1
        if cell_worst is not None:
            rec["worst ratio"] = str(cell_worst)
        out.write(json.dumps(rec) + "\n")
        out.flush()
        done += 1
        if done % 100 == 0:
            print(f"{done} cells, {facets_tested} facets tested, {ray_tests} ray tests, "
                  f"{failures} failures, worst ratio {worst[0] if worst else None}, "
                  f"{round(time.time() - t0)} s", flush=True)
    out.close()

    recs = [json.loads(l) for l in open(os.path.join(HERE, "facets.jsonl"))]
    ratios = [Fraction(r["worst ratio"]) for r in recs if r["worst ratio"]]
    summary = {
        "cells": len(recs),
        "facets seen": facets_seen,
        "facets carrying a negative edge, and so tested": facets_tested,
        "ray tests": ray_tests,
        "tests where a facet fails to pay for its negative edges": failures,
        "cells with a failing facet": sum(1 for r in recs if r["failing facets"]),
        "smallest ratio of the positive share to the negative share": str(min(ratios))
        if ratios else None,
        "largest ratio": str(max(ratios)) if ratios else None,
        "where the smallest ratio is": {"triple": worst[1], "facet": worst[2]} if worst else None,
        "ray values that disagree with the step that built the cell": identity_bad,
        "seconds": round(time.time() - t0),
    }
    json.dump(summary, open(os.path.join(HERE, "facets.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
