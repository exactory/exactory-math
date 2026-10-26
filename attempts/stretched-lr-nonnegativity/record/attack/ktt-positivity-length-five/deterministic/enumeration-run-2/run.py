#!/usr/bin/env python3
"""The cell functional from the local formula, and a sweep of full-dimensional cells.

certified-special-case-check-3 reduced the rung to the sign of a linear functional at the extreme
rays of each cell of the chamber complex, and took the functional from finite differences of
certified Ehrhart coefficients. That ties the cost to the size of the triple and so keeps the
full-dimensional cells out of reach. The local Euler-Maclaurin formula gives the same functional
for nothing:

    l(b) = sum over the edges e of  w(class of e) * (lattice length of e)(b),

the class fixed on the cell and the length linear in b. Phase A checks the two routes against
each other on the cells that step certified. Phase B then sweeps full-dimensional cells at
generic points of the hive cone, of any size, for a negative value at an extreme ray.
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
from atlasform import WeightBook, apply_functional, cell_functional  # noqa: E402
from chamber import (Cell, a1_of, hive_cone_rays, pack,  # noqa: E402
                     triple_of_hive, unpack)

CHECK3 = os.path.join(HERE, "..", "certified-special-case-check-3")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
BUDGET_A = float(os.environ.get("BUDGET_A", "600"))
BUDGET_B = float(os.environ.get("BUDGET_B", "1800"))
MAX_VERTICES = int(os.environ.get("MAX_VERTICES", "320"))
N = 5


def rays_and_functional(w, book, require_generic=False):
    Z = Cell(*w)
    if Z.C.dim != Z.D:
        return None, None, None, "the hive polytope is not full dimensional"
    if len(Z.C.vertices) > MAX_VERTICES:
        return None, None, None, "too many vertices"
    if require_generic and Z.walls:
        return None, None, None, "the triple lies on a wall"
    K, eqs, ineqs = Z.cone()
    rays = [tuple(int(x) for x in r) for r in K.ExtremeRays()]
    if not rays:
        return None, None, None, "no extreme rays"
    return Z, rays, cell_functional(Z, book), (K.Rank(), len(eqs))


def main():
    book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
    rng = random.Random(20260906)
    out = open(os.path.join(HERE, "cells.jsonl"), "w")
    t0 = time.time()

    # Phase A: the two routes to the functional, against each other
    recorded = [json.loads(l) for l in open(os.path.join(CHECK3, "cells.jsonl"))]
    rng.shuffle(recorded)
    a_cells = a_rays = a_bad = a_value_bad = 0
    for c in recorded:
        if time.time() - t0 > BUDGET_A:
            break
        w = tuple(tuple(x) for x in c["triple"])
        Z, rays, ell, info = rays_and_functional(w, book)
        if Z is None:
            continue
        got = {tuple(r): apply_functional(ell, r) for r in rays}
        want = {tuple(r): Fraction(v) for r, v in zip(c["ray_list"], c["ell"])}
        a_cells += 1
        a_rays += len(rays)
        if set(got) != set(want) or any(got[k] != want[k] for k in got):
            a_bad += 1
            print(f"RAY VALUE MISMATCH {c['triple']}", flush=True)
        if apply_functional(ell, pack(w[0], w[1], w[2], N)) != Fraction(c["triple a1"]):
            a_value_bad += 1
            print(f"TRIPLE VALUE MISMATCH {c['triple']}", flush=True)
        if a_cells % 25 == 0:
            print(f"phase A: {a_cells} cells, {a_rays} rays, {a_bad + a_value_bad} mismatches, "
                  f"{round(time.time() - t0)} s", flush=True)

    # Phase B: full-dimensional cells at generic points, of any size
    pts, idx, hrays = hive_cone_rays(N)
    b_cells = 0
    negative = []
    skipped: dict = {}
    worst = None
    t1 = time.time()
    while time.time() - t1 < BUDGET_B:
        h = [0] * len(pts)
        for _ in range(rng.randint(6, 16)):
            r = rng.choice(hrays)
            c = rng.randint(1, rng.choice([20, 200, 2000, 20000]))
            h = [a + c * b for a, b in zip(h, r)]
        w = triple_of_hive(h, idx, N)
        if min(len(x) for x in w) < 3:
            skipped["a boundary partition is too short"] = \
                skipped.get("a boundary partition is too short", 0) + 1
            continue
        try:
            Z, rays, ell, info = rays_and_functional(w, book, require_generic=True)
        except Exception as exc:
            skipped[type(exc).__name__] = skipped.get(type(exc).__name__, 0) + 1
            continue
        if Z is None:
            skipped[info] = skipped.get(info, 0) + 1
            continue
        rank, neq = info
        if neq:
            skipped["the triple lies on a wall"] = skipped.get("the triple lies on a wall", 0) + 1
            continue
        vals = [apply_functional(ell, r) for r in rays]
        rec = {
            "kind": "a generic point of the cone",
            "triple": [list(x) for x in w], "size": sum(w[0]),
            "vertices": len(Z.C.vertices), "cell rank": rank, "rays": len(rays),
            "min": str(min(vals)), "max": str(max(vals)),
            "ray_list": [list(r) for r in rays], "ell": [str(v) for v in vals],
        }
        if sum(w[0]) <= 400:
            a = a1_of(pack(w[0], w[1], w[2], N), N)
            rec["certified a1"] = str(a)
            rec["functional at the triple"] = str(apply_functional(ell, pack(w[0], w[1], w[2], N)))
            rec["identity"] = a == apply_functional(ell, pack(w[0], w[1], w[2], N))
        out.write(json.dumps(rec) + "\n")
        out.flush()
        b_cells += 1
        m = min(vals)
        if worst is None or m < worst:
            worst = m
        if m < 0:
            negative.append(rec)
            print(f"NEGATIVE RAY VALUE {m} at {w}", flush=True)
        print(f"phase B: {b_cells} cells, size {sum(w[0])}, rank {rank}, {len(rays)} rays, "
              f"{len(Z.C.vertices)} vertices, minimum {m}, worst {worst}, "
              f"{round(time.time() - t1)} s", flush=True)
    out.close()

    cells = [json.loads(l) for l in open(os.path.join(HERE, "cells.jsonl"))]
    summary = {
        "phase A cells": a_cells,
        "phase A rays compared": a_rays,
        "phase A cells whose ray values differ from certified-special-case-check-3": a_bad,
        "phase A cells whose value at the triple differs": a_value_bad,
        "phase B cells": b_cells,
        "phase B cells that are full dimensional": sum(1 for c in cells if c["cell rank"] == 14),
        "phase B rays evaluated": sum(c["rays"] for c in cells),
        "phase B cells with a negative ray value": len(negative),
        "phase B minimum ray value": str(min((Fraction(c["min"]) for c in cells), default=0)),
        "phase B maximum ray value": str(max((Fraction(c["max"]) for c in cells), default=0)),
        "phase B largest triple": max((c["size"] for c in cells), default=0),
        "phase B cells checked against a certified Ehrhart value":
            sum(1 for c in cells if "identity" in c),
        "phase B of those that agree": sum(1 for c in cells if c.get("identity")),
        "phase B skipped": skipped,
        "class weights held": len(book),
        "class weights from the atlas": book.from_atlas,
        "class weights computed here": book.computed,
        "seconds": round(time.time() - t0),
    }
    json.dump(summary, open(os.path.join(HERE, "cells.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
