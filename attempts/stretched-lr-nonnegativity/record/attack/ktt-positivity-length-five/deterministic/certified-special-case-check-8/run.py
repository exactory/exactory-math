#!/usr/bin/env python3
"""Is the zero-row containment check vacuous? It is.

The fifth independent review proposed a barrier proof needing no solver. Write the requirement
that a local formula be nonnegative and reproduce every recorded linear coefficient as
`A w' = a1` with `A` entrywise nonnegative, its entries the lattice lengths, and `w' >= 0`. A row
whose right-hand side is zero then forces `w'` to vanish on that row's whole support, and 7,109 of
the 9,145 recorded ray values are zero. If some row with a positive right-hand side had its
support inside the union of the zero rows' supports, the system would be infeasible outright.

This run tests the premise the argument needs: that a zero row has a non-empty support. It does
not. At a ray where the linear coefficient vanishes the polytope degenerates to a point, so every
edge has length zero, the row is identically zero, and it constrains nothing.
"""
from __future__ import annotations

import json
import os
import random
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from atlasform import apply_functional, edges_with_linear_length  # noqa: E402
from chamber import Cell  # noqa: E402

CHECK3 = os.path.join(HERE, "..", "certified-special-case-check-3")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
BUDGET = float(os.environ.get("BUDGET", "900"))


def main():
    cells = []
    for path, tag in ((os.path.join(CHECK3, "cells.jsonl"), "check-3"),
                      (os.path.join(RUN2, "cells.jsonl"), "run-2")):
        for line in open(path):
            cells.append((tag, json.loads(line)))
    rng = random.Random(20260914)
    rng.shuffle(cells)
    out = open(os.path.join(HERE, "rows.jsonl"), "w")
    t0 = time.time()
    done = zero_rows = zero_with_support = pos_rows = pos_empty = 0
    for tag, c in cells:
        if time.time() - t0 > BUDGET:
            break
        Z = Cell(*tuple(tuple(x) for x in c["triple"]))
        edges = edges_with_linear_length(Z)
        rec = {"source": tag, "triple": c["triple"], "edges": len(edges), "rows": []}
        for ray, val in zip(c["ray_list"], c["ell"]):
            support = sum(1 for _, row, _, _ in edges if apply_functional(row, ray) > 0)
            neg = sum(1 for _, row, _, _ in edges if apply_functional(row, ray) < 0)
            rec["rows"].append({"value": val, "edges of positive length": support,
                                "edges of negative length": neg})
            if Fraction(val) == 0:
                zero_rows += 1
                if support:
                    zero_with_support += 1
            else:
                pos_rows += 1
                if not support:
                    pos_empty += 1
        out.write(json.dumps(rec) + "\n")
        out.flush()
        done += 1
        if done % 50 == 0:
            print(f"{done} cells, {zero_rows} zero rows of which {zero_with_support} have a "
                  f"support, {round(time.time() - t0)} s", flush=True)
    out.close()
    summary = {
        "cells": done,
        "rows": zero_rows + pos_rows,
        "rows whose value is zero": zero_rows,
        "of those, rows with a non-empty support": zero_with_support,
        "rows whose value is positive": pos_rows,
        "of those, rows with an empty support": pos_empty,
        "edges of negative length at any row":
            sum(1 for l in open(os.path.join(HERE, "rows.jsonl"))
                for r in json.loads(l)["rows"] if r["edges of negative length"]),
        "verdict": ("the containment check is vacuous: every zero row has an empty support"
                    if zero_with_support == 0 else
                    "some zero rows have a support and the containment check is worth running"),
        "seconds": round(time.time() - t0),
    }
    json.dump(summary, open(os.path.join(HERE, "rows.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
