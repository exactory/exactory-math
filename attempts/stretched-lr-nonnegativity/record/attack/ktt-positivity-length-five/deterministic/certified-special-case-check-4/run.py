#!/usr/bin/env python3
"""The sharper residue: only cells carrying a negative-weight edge can fail.

On a cell the functional is l(b) = sum over the edges e of w(class of e) times the lattice length
of e at b, and the lattice length is a nonnegative linear function of b on the whole cell, since
the edge exists with that length at every triple of the cell. So if every edge class of the cell
has a nonnegative weight, then l >= 0 on all of the cell with no computation at all. The residue
of the rung is the cells that carry an edge whose class has a negative weight.

This run classifies every cell already built, measures how rare the dangerous ones are and how
much room they have, and records the list of negative classes over every weight the project
holds rather than over the atlas alone.
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
ATLAS = os.path.join(RUN2, "..", "enumeration-run-1", "atlas.jsonl")
BUDGET = float(os.environ.get("BUDGET", "2400"))
N = 5


def main():
    book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
    for line in open(os.path.join(RUN2, "weights.jsonl")):
        r = json.loads(line)
        book.weights.setdefault(canonical([tuple(v) for v in r["normals"]]), Fraction(r["weight"]))
    negative_classes = {k: v for k, v in book.weights.items() if v < 0}
    json.dump({"classes held": len(book.weights),
               "negative classes": len(negative_classes),
               "most negative": str(min(negative_classes.values())),
               "the negative classes": [{"normals": [list(v) for v in k], "weight": str(w)}
                                        for k, w in sorted(negative_classes.items(),
                                                           key=lambda kv: kv[1])]},
              open(os.path.join(HERE, "negative-classes.json"), "w"), indent=2)

    cells = []
    for path, tag in ((os.path.join(CHECK3, "cells.jsonl"), "certified-special-case-check-3"),
                      (os.path.join(RUN2, "cells.jsonl"), "enumeration-run-2")):
        for line in open(path):
            c = json.loads(line)
            cells.append((tag, c))

    out = open(os.path.join(HERE, "classified.jsonl"), "w")
    t0 = time.time()
    done = dangerous = mismatched = 0
    worst_margin = None
    for tag, c in cells:
        if time.time() - t0 > BUDGET:
            break
        w = tuple(tuple(x) for x in c["triple"])
        Z = Cell(*w)
        edges = edges_with_linear_length(Z)
        weights = [book.weight(normals) for normals, _, _, _ in edges]
        neg = [i for i, x in enumerate(weights) if x < 0]
        rec = {"source": tag, "triple": c["triple"], "edges": len(edges),
               "negative edges": len(neg), "rays": c["rays"]}
        worst = None
        for r, recorded in zip(c["ray_list"], c["ell"]):
            pos = sum(weights[i] * apply_functional(row, r)
                      for i, (_, row, _, _) in enumerate(edges) if weights[i] > 0)
            bad = sum(-weights[i] * apply_functional(edges[i][1], r) for i in neg)
            if pos - bad != Fraction(recorded):
                mismatched += 1
            if bad > 0 and (worst is None or pos - bad < worst[0] - worst[1]):
                worst = (pos, bad)
        if neg:
            dangerous += 1
            rec["negative classes present"] = sorted({str(weights[i]) for i in neg})
        if worst is not None:
            rec["worst ray positive part"] = str(worst[0])
            rec["worst ray negative part"] = str(worst[1])
            rec["worst ray margin"] = str(worst[0] / worst[1]) if worst[1] else None
            m = worst[0] / worst[1]
            if worst_margin is None or m < worst_margin[0]:
                worst_margin = (m, c["triple"])
        out.write(json.dumps(rec) + "\n")
        out.flush()
        done += 1
        if done % 100 == 0:
            print(f"{done} cells, {dangerous} carry a negative class, {mismatched} ray mismatches,"
                  f" {round(time.time() - t0)} s", flush=True)
    out.close()

    recs = [json.loads(l) for l in open(os.path.join(HERE, "classified.jsonl"))]
    with_neg = [r for r in recs if r["negative edges"]]
    summary = {
        "cells classified": len(recs),
        "of them from certified-special-case-check-3":
            sum(1 for r in recs if r["source"] == "certified-special-case-check-3"),
        "of them from enumeration-run-2": sum(1 for r in recs if r["source"] == "enumeration-run-2"),
        "cells carrying an edge of a negative-weight class": len(with_neg),
        "cells the reduction settles with no computation": len(recs) - len(with_neg),
        "edges examined": sum(r["edges"] for r in recs),
        "edges of a negative-weight class": sum(r["negative edges"] for r in recs),
        "ray values that disagree with the recorded ones": mismatched,
        "smallest ratio of the positive part to the negative part at a ray":
            str(worst_margin[0]) if worst_margin else None,
        "where": worst_margin[1] if worst_margin else None,
        "classes held": len(book.weights),
        "negative classes": len(negative_classes),
        "most negative class weight": str(min(negative_classes.values())),
        "seconds": round(time.time() - t0),
    }
    json.dump(summary, open(os.path.join(HERE, "classified.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
