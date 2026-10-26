#!/usr/bin/env python3
"""Phase two: what the per-facet ratio actually tracks.

The trend reading says the ratio falls because the negative share grows with the number of
negative edges on a facet. `certified-special-case-check-6` recorded no per-facet detail for
passing facets, so that mechanism has never been tested and the extrapolation rests on the cell's
total edge count, a proxy. This pass re-runs the facet computation over the 2,199 cells already
built and records, for every facet that carries a negative edge, the number of negative edges on
it, the number of positive edges, the cell's edge count, the cell's rank and its source, beside
the worst ratio over the cell's extreme rays. Nothing new is constructed.
"""
from __future__ import annotations

import json
import os
import statistics
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
BUDGET = float(os.environ.get("BUDGET", "900"))
N = 5


def main():
    book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
    for line in open(os.path.join(RUN2, "weights.jsonl")):
        r = json.loads(line)
        book.weights.setdefault(canonical([tuple(v) for v in r["normals"]]), Fraction(r["weight"]))
    cells = []
    for path, tag in ((os.path.join(CHECK3, "cells.jsonl"), "check-3, box triple"),
                      (os.path.join(RUN2, "cells.jsonl"), "run-2, generic")):
        for line in open(path):
            cells.append((tag, json.loads(line)))

    out = open(os.path.join(HERE, "per-facet.jsonl"), "w")
    t0 = time.time()
    done = facets = 0
    for tag, c in cells:
        if time.time() - t0 > BUDGET:
            break
        Z = Cell(*tuple(tuple(x) for x in c["triple"]))
        edges = edges_with_linear_length(Z)
        weights = [book.weight(n) for n, _, _, _ in edges]
        fs = [set(f) for _, _, _, f in edges]
        counts = [len(f) for f in fs]
        for F in sorted({x for f in fs for x in f}):
            neg = [i for i in range(len(edges)) if F in fs[i] and weights[i] < 0]
            if not neg:
                continue
            pos = [i for i in range(len(edges)) if F in fs[i] and weights[i] > 0]
            left = [Fraction(0)] * Z.B
            for i in neg:
                left = [t + (-weights[i]) / counts[i] * x for t, x in zip(left, edges[i][1])]
            right = [Fraction(0)] * Z.B
            for i in pos:
                right = [t + weights[i] / counts[i] * x for t, x in zip(right, edges[i][1])]
            ratios = []
            for ray in c["ray_list"]:
                lo, hi = apply_functional(left, ray), apply_functional(right, ray)
                if lo > 0:
                    ratios.append(hi / lo)
            if not ratios:
                continue
            facets += 1
            out.write(json.dumps({
                "source": tag, "cell edges": len(edges), "cell rank": c["cell rank"],
                "facet": F, "negative edges on the facet": len(neg),
                "positive edges on the facet": len(pos),
                "negative weight sum": str(sum(-weights[i] for i in neg)),
                "worst ratio": str(min(ratios)), "rays": len(ratios)}) + "\n")
        done += 1
        if done % 200 == 0:
            print(f"{done} cells, {facets} facets recorded, {round(time.time() - t0)} s",
                  flush=True)
    out.close()

    recs = [json.loads(l) for l in open(os.path.join(HERE, "per-facet.jsonl"))]

    def group(key):
        g: dict = {}
        for r in recs:
            g.setdefault(key(r), []).append(float(Fraction(r["worst ratio"])))
        return {k: {"facets": len(v), "median ratio": round(statistics.median(v), 2),
                    "worst ratio": round(min(v), 2)} for k, v in sorted(g.items())}

    def band(e):
        b = 1
        while b * 2 <= e:
            b *= 2
        return b

    summary = {
        "cells re-run": done,
        "facets carrying a negative edge": len(recs),
        "by the number of negative edges on the facet": group(
            lambda r: r["negative edges on the facet"]),
        "by the cell's edge count, floor power of two": group(lambda r: band(r["cell edges"])),
        "by the cell's rank": group(lambda r: r["cell rank"]),
        "by source": group(lambda r: r["source"]),
        "seconds": round(time.time() - t0),
    }
    json.dump(summary, open(os.path.join(HERE, "per-facet.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
