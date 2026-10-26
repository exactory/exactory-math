#!/usr/bin/env python3
"""Local domination: is a negative-weight edge outweighed by its neighbours, on the whole cell?

certified-special-case-check-4 cut the residue to the cells that carry an edge of a
negative-weight class. This run asks whether those cells can be settled locally, without
enumerating them. Give each positive-weight edge f an equal share of its weighted length to each
negative-weight edge adjacent to it, and let share(e) be the sum of what e receives. The shares
of distinct negative edges are disjoint parts of the positive sum, so

    share(e) >= |w(e)| * (lattice length of e)  for every negative edge e   =>   l >= 0,

on every cell at once. Both sides are linear on a cell, so the inequality is decided at the
cell's extreme rays. This run evaluates it there, on every cell known to carry a negative edge,
and reports the worst ratio.
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
CHECK4 = os.path.join(HERE, "..", "certified-special-case-check-4")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
BUDGET = float(os.environ.get("BUDGET", "2400"))
N = 5


def main():
    book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
    for line in open(os.path.join(RUN2, "weights.jsonl")):
        r = json.loads(line)
        book.weights.setdefault(canonical([tuple(v) for v in r["normals"]]), Fraction(r["weight"]))

    built = {}
    for path, tag in ((os.path.join(CHECK3, "cells.jsonl"), "certified-special-case-check-3"),
                      (os.path.join(RUN2, "cells.jsonl"), "enumeration-run-2")):
        for line in open(path):
            c = json.loads(line)
            built.setdefault((tag, tuple(tuple(x) for x in c["triple"])), c)
    todo = [r for r in (json.loads(l) for l in open(os.path.join(CHECK4, "classified.jsonl")))
            if r["negative edges"]]

    out = open(os.path.join(HERE, "domination.jsonl"), "w")
    t0 = time.time()
    done = failures = neg_edges = ray_tests = 0
    worst = None
    facet_failures = [0]
    facet_worst = [None]
    for r in todo:
        if time.time() - t0 > BUDGET:
            break
        key = (r["source"], tuple(tuple(x) for x in r["triple"]))
        c = built.get(key)
        if c is None:
            continue
        Z = Cell(*key[1])
        edges = edges_with_linear_length(Z)
        weights = [book.weight(n) for n, _, _, _ in edges]
        neg = [i for i, w in enumerate(weights) if w < 0]
        touch = [set(pair) for _, _, pair, _ in edges]
        facets = [set(fs) for _, _, _, fs in edges]
        def near_vertex(f, e):
            return bool(touch[f] & touch[e])

        def near_facet(f, e):
            return bool(facets[f] & facets[e])

        rec = {"source": r["source"], "triple": r["triple"], "edges": len(edges),
               "negative edges": len(neg), "rays": len(c["ray_list"]), "per edge": []}
        total = [Fraction(0)] * Z.B
        for i, (_, row, _, _) in enumerate(edges):
            total = [t + weights[i] * x for t, x in zip(total, row)]
        for e in neg:
            need = [-weights[e] * x for x in edges[e][1]]
            item = {"weight": str(weights[e])}
            for name, near in (("vertex", near_vertex), ("facet", near_facet)):
                count = [0] * len(edges)
                for f, wf in enumerate(weights):
                    if wf > 0:
                        count[f] = sum(1 for g in neg if near(f, g))
                share = [Fraction(0)] * Z.B
                neighbours = 0
                for f, wf in enumerate(weights):
                    if wf > 0 and count[f] and near(f, e):
                        neighbours += 1
                        share = [s + wf / count[f] * x for s, x in zip(share, edges[f][1])]
                ratios, fails = [], 0
                for ray in c["ray_list"]:
                    lhs = apply_functional(share, ray)
                    rhs = apply_functional(need, ray)
                    if name == "vertex":
                        ray_tests += 1
                    if rhs > 0:
                        ratios.append(lhs / rhs)
                        if lhs < rhs:
                            fails += 1
                    elif lhs < 0:
                        fails += 1
                item[name] = {"positive neighbours": neighbours,
                              "rays where the negative edge has positive length": len(ratios),
                              "failures": fails,
                              "smallest ratio": str(min(ratios)) if ratios else None}
                if name == "vertex":
                    failures += fails
                    if ratios and (worst is None or min(ratios) < worst[0]):
                        worst = (min(ratios), r["triple"], str(weights[e]))
                else:
                    facet_failures[0] += fails
                    if ratios and (facet_worst[0] is None or min(ratios) < facet_worst[0]):
                        facet_worst[0] = min(ratios)
            rec["per edge"].append(item)
            neg_edges += 1
        out.write(json.dumps(rec) + "\n")
        out.flush()
        done += 1
        if done % 25 == 0:
            print(f"{done} cells, {neg_edges} negative edges, {ray_tests} ray tests, "
                  f"vertex failures {failures}, facet failures {facet_failures[0]}, "
                  f"{round(time.time() - t0)} s", flush=True)
    out.close()

    recs = [json.loads(l) for l in open(os.path.join(HERE, "domination.jsonl"))]
    def ratios_of(name):
        return [Fraction(i[name]["smallest ratio"]) for r in recs for i in r["per edge"]
                if i[name]["smallest ratio"] is not None]

    rv, rf = ratios_of("vertex"), ratios_of("facet")
    summary = {
        "cells with a negative edge": len(recs),
        "negative edges": sum(r["negative edges"] for r in recs),
        "ray tests per neighbourhood": ray_tests,
        "vertex neighbourhood: tests where the share fails to dominate": failures,
        "vertex neighbourhood: smallest ratio": str(min(rv)) if rv else None,
        "vertex neighbourhood: largest ratio": str(max(rv)) if rv else None,
        "facet neighbourhood: tests where the share fails to dominate": facet_failures[0],
        "facet neighbourhood: smallest ratio": str(facet_worst[0]) if facet_worst[0] is not None
        else None,
        "facet neighbourhood: largest ratio": str(max(rf)) if rf else None,
        "where the vertex neighbourhood is worst": {"triple": worst[1], "edge weight": worst[2]}
        if worst else None,
        "negative edges with no positive vertex neighbour":
            sum(1 for r in recs for i in r["per edge"] if i["vertex"]["positive neighbours"] == 0),
        "seconds": round(time.time() - t0),
    }
    json.dump(summary, open(os.path.join(HERE, "domination.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
