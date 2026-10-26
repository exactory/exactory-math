#!/usr/bin/env python3
"""A search for a facet where the per-facet inequality fails, at higher complexity.

`certified-special-case-check-6` found no failure in 46,501 tests, but the margin falls with the
complexity of the cell and the fall is confounded: every low-complexity cell came from a box
triple and every high-complexity one from a generic triple. This run does three things the
independent review of 2026-09-05 required.

  * It retests the eight tightest recorded cells and records, per facet, how many negative edges
    it carries and of which classes, which the earlier record does not hold.
  * It builds cells above the top band already measured, more than 684 edges, from both sources,
    so that edge count and construction route are separated.
  * It reports, per band, the median of the per-cell worst ratios beside the minimum, because the
    minimum falls with the number of tests in a band by construction.

A failing facet refutes the per-facet form of the sufficient condition. No number of passing
facets proves it.
"""
from __future__ import annotations

import gzip
import json
import os
import random
import statistics
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from atlasform import WeightBook, apply_functional, edges_with_linear_length  # noqa: E402
from chamber import (Cell, hive_cone_rays, triple_of_hive, wall_vertices)  # noqa: E402
from isotypes import canonical  # noqa: E402

CHECK1 = os.path.join(HERE, "..", "certified-special-case-check-1")
CHECK6 = os.path.join(HERE, "..", "certified-special-case-check-6")
CHECK3 = os.path.join(HERE, "..", "certified-special-case-check-3")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
BUDGET = float(os.environ.get("BUDGET", "2000"))
MAX_VERTICES = int(os.environ.get("MAX_VERTICES", "600"))
N = 5


def band(edges):
    b = 1
    while b * 2 <= edges:
        b *= 2
    return b


def test_cell(triple, rays, book, source):
    """Every facet of the cell that carries a negative edge, tested at every extreme ray."""
    Z = Cell(*triple)
    if Z.C.dim != Z.D or len(Z.C.vertices) > MAX_VERTICES:
        return None
    edges = edges_with_linear_length(Z)
    weights = [book.weight(n) for n, _, _, _ in edges]
    facets = [set(fs) for _, _, _, fs in edges]
    counts = [len(fs) for fs in facets]
    rec = {"source": source, "triple": [list(x) for x in triple], "edges": len(edges),
           "vertices": len(Z.C.vertices), "rays": len(rays), "band": band(len(edges)),
           "facets with a negative edge": 0, "facet tests": 0, "per facet": [],
           "worst ratio": None, "failures": []}
    worst = None
    for F in sorted({f for fs in facets for f in fs}):
        neg = [i for i in range(len(edges)) if F in facets[i] and weights[i] < 0]
        if not neg:
            continue
        rec["facets with a negative edge"] += 1
        left = [Fraction(0)] * Z.B
        for i in neg:
            left = [t + (-weights[i]) / counts[i] * x for t, x in zip(left, edges[i][1])]
        right = [Fraction(0)] * Z.B
        for i in range(len(edges)):
            if F in facets[i] and weights[i] > 0:
                right = [t + weights[i] / counts[i] * x for t, x in zip(right, edges[i][1])]
        ratios = []
        for k, ray in enumerate(rays):
            lo, hi = apply_functional(left, ray), apply_functional(right, ray)
            rec["facet tests"] += 1
            if lo > 0:
                ratios.append(hi / lo)
                if hi < lo:
                    rec["failures"].append({"facet": F, "ray": k, "left": str(lo),
                                            "right": str(hi)})
            elif hi < 0:
                rec["failures"].append({"facet": F, "ray": k, "left": str(lo), "right": str(hi)})
        item = {"facet": F, "negative edges": len(neg),
                "classes": sorted({str(weights[i]) for i in neg}),
                "positive edges on it": sum(1 for i in range(len(edges))
                                            if F in facets[i] and weights[i] > 0)}
        if ratios:
            item["smallest ratio"] = str(min(ratios))
            if worst is None or min(ratios) < worst:
                worst = min(ratios)
        rec["per facet"].append(item)
    if worst is not None:
        rec["worst ratio"] = str(worst)
    return rec


def cell_rays(triple):
    Z = Cell(*triple)
    if Z.C.dim != Z.D or len(Z.C.vertices) > MAX_VERTICES:
        return None, None
    K, eqs, ineqs = Z.cone()
    return [tuple(int(x) for x in r) for r in K.ExtremeRays()], Z


def main():
    book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
    for f in (os.path.join(RUN2, "weights.jsonl"),):
        for line in open(f):
            r = json.loads(line)
            book.weights.setdefault(canonical([tuple(v) for v in r["normals"]]),
                                    Fraction(r["weight"]))
    old = [json.loads(l) for l in open(os.path.join(CHECK6, "facets.jsonl"))]
    built = {}
    for path in (os.path.join(CHECK3, "cells.jsonl"), os.path.join(RUN2, "cells.jsonl")):
        for line in open(path):
            c = json.loads(line)
            built.setdefault(tuple(tuple(x) for x in c["triple"]), c)
    tight = sorted((r for r in old if r["worst ratio"]),
                   key=lambda r: Fraction(r["worst ratio"]))[:8]

    out = open(os.path.join(HERE, "search.jsonl"), "w")
    t0 = time.time()
    done = failures = 0
    worst = None

    def record(rec):
        nonlocal done, failures, worst
        out.write(json.dumps(rec) + "\n")
        out.flush()
        done += 1
        if rec["failures"]:
            failures += len(rec["failures"])
            print(f"FAILING FACET at {rec['triple']}: {rec['failures'][0]}", flush=True)
        if rec["worst ratio"] and (worst is None or Fraction(rec["worst ratio"]) < worst):
            worst = Fraction(rec["worst ratio"])
        print(f"{done} cells, {rec['source']}, {rec['edges']} edges, "
              f"{rec['facets with a negative edge']} facets, {rec['facet tests']} tests, "
              f"worst here {rec['worst ratio']}, worst overall {worst}, "
              f"{round(time.time() - t0)} s", flush=True)

    for r in tight:                       # the eight tightest, with per-facet detail
        if time.time() - t0 > BUDGET:
            break
        key = tuple(tuple(x) for x in r["triple"])
        c = built.get(key)
        if c is None:
            continue
        rec = test_cell(key, [tuple(x) for x in c["ray_list"]], book, "retest of a tightest cell")
        if rec:
            record(rec)

    rng = random.Random(20260909)
    pts, idx, hrays = hive_cone_rays(N)
    certified = [json.loads(l) for l in gzip.open(os.path.join(CHECK1, "edges.jsonl.gz"), "rt")]
    skipped: dict = {}
    turn = 0
    while time.time() - t0 < BUDGET:
        turn += 1
        if turn % 2:                      # generic points of the hive cone
            h = [0] * len(pts)
            for _ in range(rng.randint(10, 20)):
                r = rng.choice(hrays)
                cst = rng.randint(1, rng.choice([200, 2000, 20000]))
                h = [a + cst * b for a, b in zip(h, r)]
            t = triple_of_hive(h, idx, N)
            source = "a generic point of the cone"
        else:                             # perturbations of certified box triples
            w = rng.choice(certified)
            blocks = []
            for part in (w["lam"], w["mu"], w["nu"]):
                blocks.append(sorted((1000 * x + rng.randint(-50, 50) for x in part),
                                     reverse=True))
            L, M, V = blocks
            L[0] += sum(M) + sum(V) - sum(L)
            L = sorted(L, reverse=True)
            if min(L + M + V) < 0:
                continue
            t = (tuple(x for x in L if x), tuple(x for x in M if x), tuple(x for x in V if x))
            source = "a perturbed box triple"
        if min(len(x) for x in t) < 3:
            continue
        try:
            Z = Cell(*t)
            if Z.C.dim != Z.D:
                skipped["not full dimensional"] = skipped.get("not full dimensional", 0) + 1
                continue
            if len(Z.C.vertices) > MAX_VERTICES:
                skipped["too many vertices"] = skipped.get("too many vertices", 0) + 1
                continue
            if wall_vertices(Z.C) and source == "a generic point of the cone":
                skipped["on a wall"] = skipped.get("on a wall", 0) + 1
                continue
            K, eqs, ineqs = Z.cone()
            rays = [tuple(int(x) for x in r) for r in K.ExtremeRays()]
            rec = test_cell(t, rays, book, source)
        except Exception as exc:
            skipped[type(exc).__name__] = skipped.get(type(exc).__name__, 0) + 1
            continue
        if rec is None:
            continue
        if rec["edges"] <= 684 and rec["facets with a negative edge"] == 0:
            skipped["below the new band and no negative edge"] = \
                skipped.get("below the new band and no negative edge", 0) + 1
            continue
        record(rec)
    out.close()

    new = [json.loads(l) for l in open(os.path.join(HERE, "search.jsonl"))]
    bands: dict = {}
    for r in old:
        if not r["worst ratio"]:
            continue
        b = band(r["edges"])
        e = bands.setdefault(b, {"cells": 0, "tests": 0, "ratios": []})
        e["cells"] += 1
        e["tests"] += r["facets with a negative edge"] * r["rays"]
        e["ratios"].append(float(Fraction(r["worst ratio"])))
    for r in new:
        if not r["worst ratio"]:
            continue
        e = bands.setdefault(r["band"], {"cells": 0, "tests": 0, "ratios": []})
        e["cells"] += 1
        e["tests"] += r["facet tests"]
        e["ratios"].append(float(Fraction(r["worst ratio"])))
    table = [{"band": b, "cells": e["cells"], "facet ray tests": e["tests"],
              "worst ratio": round(min(e["ratios"]), 2),
              "median of the per-cell worst ratios": round(statistics.median(e["ratios"]), 2)}
             for b, e in sorted(bands.items())]
    above = [r for r in new if r["edges"] > 684]
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
        "worst ratio here": str(worst) if worst else None,
        "largest cell by edges": max((r["edges"] for r in new), default=0),
        "bands, old and new together": table,
        "skipped": skipped,
        "seconds": round(time.time() - t0),
        "verdict": ("a failing facet was found" if failures else
                    "no failing facet; this is undecided, not support"),
    }
    json.dump(summary, open(os.path.join(HERE, "search.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
