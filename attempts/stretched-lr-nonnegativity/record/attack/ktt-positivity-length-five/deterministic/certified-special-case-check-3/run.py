#!/usr/bin/env python3
"""Cells of the rank-five chamber complex: extreme rays, the linear functional, its minimum.

The stretched polynomial of m*(lam,mu,nu) is the stretched polynomial of (lam,mu,nu) at m*t, so
its coefficient a_k is homogeneous of degree k in the boundary triple. On a cell of the chamber
complex, where the hive polytope keeps its incidence structure and every vertex is a fixed linear
function of the triple, the local Euler-Maclaurin formula writes a1 as a sum over the edges of a
fixed weight times the edge's lattice length, and the lattice lengths are linear in the triple.
So a1 restricted to a cell is a linear functional, and

    a1 >= 0 on the whole cell  <=>  the functional is nonnegative at the cell's extreme rays.

A cell is an unbounded cone: certifying one settles a1 >= 0 for infinitely many triples of
unbounded size, which no box search can do. This run builds the cell through each certified
triple of the box, computes its extreme rays and its functional by finite differences of
certified Ehrhart coefficients, and reports the minimum over the rays.
"""
from __future__ import annotations

import gzip
import json
import os
import random
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chamber import (Cell, a1_of, hive_cone_rays,  # noqa: E402
                     lattice_basis_of_size_hyperplane, pack, solve_coeffs, triple_of_hive, unpack)

CHECK1 = os.path.join(HERE, "..", "certified-special-case-check-1")
BUDGET = float(os.environ.get("BUDGET", "2400"))
GENERIC = float(os.environ.get("GENERIC", "1200"))
BASIS = lattice_basis_of_size_hyperplane(5)
N = 5
_a1: dict = {}


def a1(b):
    key = tuple(b)
    if key not in _a1:
        _a1[key] = a1_of(list(b), N)
    return _a1[key]


def study(w, rng, max_rays=10 ** 6, max_interior=3000):
    """The cell through the triple w: its extreme rays, its functional, and the checks."""
    Z = Cell(*w)
    if Z.C.dim != Z.D:
        return "the hive polytope is not full dimensional"
    K, eqs, ineqs = Z.cone()
    rays = [tuple(int(x) for x in r) for r in K.ExtremeRays()]
    if not rays:
        return "no extreme rays"
    bs = [sum(r[i] for r in rays) for i in range(Z.B)]
    if not Z.contains_cell(bs, eqs, ineqs):
        return "the sum of the rays is outside the cell"
    if len(rays) > max_rays:
        return "too many extreme rays for the certified Ehrhart run"
    if sum(unpack(bs, N)[0]) > max_interior:
        return "the smallest interior point is too large for the certified Ehrhart run"
    a_s = a1(bs)
    ell = [a1([bs[i] + r[i] for i in range(Z.B)]) - a_s for r in rays]
    linear = True
    for k in rng.sample(range(len(rays)), min(4, len(rays))):
        b1 = [bs[i] + rays[k][i] for i in range(Z.B)]
        b2 = [bs[i] + 2 * rays[k][i] for i in range(Z.B)]
        if a1(b2) - a1(b1) != ell[k]:
            linear = False
    wb = pack(w[0], w[1], w[2], N)
    c = solve_coeffs(rays, wb) if len(rays) == K.Rank() else None
    rec = {
        "triple": [list(x) for x in w],
        "vertices": len(Z.C.vertices),
        "cell rank": K.Rank(), "rays": len(rays), "simplicial": len(rays) == K.Rank(),
        "equations": len(eqs), "inequalities": len(ineqs),
        "ray_list": [list(r) for r in rays],
        "ell": [str(x) for x in ell],
        "min": str(min(ell)), "max": str(max(ell)),
        "linear along sampled rays": linear,
        "interior point": [list(x) for x in unpack(bs, N)],
        "interior a1": str(a_s),
        "interior from rays": str(sum(ell)),
        "interior identity": a_s == sum(ell),
        "triple a1": str(a1(wb)),
    }
    if c is not None and all(x >= 0 for x in c):
        e = sum(ci * li for ci, li in zip(c, ell))
        rec["triple from rays"] = str(e)
        rec["triple identity"] = a1(wb) == e
    spot = []
    for _ in range(3):
        m = [rng.randint(0, 3) for _ in rays]
        b = [bs[i] + sum(m[k] * rays[k][i] for k in range(len(rays))) for i in range(Z.B)]
        if Z.contains_cell(b, eqs, ineqs) and sum(unpack(b, N)[0]) <= 4000:
            spot.append(a1(b) == a_s + sum(m[k] * ell[k] for k in range(len(rays))))
    rec["spot checks"] = spot
    return rec


def study_generic(w, rng, max_size=400, max_vertices=200):
    """A full-dimensional cell at a generic triple.

    The cell has too many extreme rays to take a difference along each, so the functional is
    determined instead by fourteen differences, one per generator of the lattice of triples, and
    then evaluated at every ray. The sampled triple itself is the base point: it lies in the
    interior of the cell by construction.
    """
    if sum(w[0]) > max_size:
        return "the triple is too large for the certified Ehrhart run"
    Z = Cell(*w)
    if Z.C.dim != Z.D:
        return "the hive polytope is not full dimensional"
    if len(Z.C.vertices) > max_vertices:
        return "too many vertices"
    if Z.walls:
        return "the triple lies on a wall"
    K, eqs, ineqs = Z.cone()
    if eqs:
        return "the cell is not full dimensional"
    rays = [tuple(int(x) for x in r) for r in K.ExtremeRays()]
    b0 = list(Z.C.b0)
    m = 1
    while m <= 8 and not all(Z.contains_cell([m * b0[i] + f[i] for i in range(Z.B)], eqs, ineqs)
                             for f in BASIS):
        m *= 2
    base = [m * x for x in b0]
    if not all(Z.contains_cell([base[i] + f[i] for i in range(Z.B)], eqs, ineqs) for f in BASIS):
        return "no small dilate keeps the lattice generators inside the cell"
    a_base = a1(base)
    lf = [a1([base[i] + f[i] for i in range(Z.B)]) - a_base for f in BASIS]

    def ell(v):
        c = solve_coeffs(BASIS, list(v))
        return None if c is None else sum(ci * li for ci, li in zip(c, lf))

    vals = [ell(r) for r in rays]
    if any(v is None for v in vals):
        return "an extreme ray is outside the lattice of triples"
    rec = {
        "triple": [list(x) for x in w],
        "vertices": len(Z.C.vertices),
        "cell rank": K.Rank(), "rays": len(rays), "simplicial": len(rays) == K.Rank(),
        "equations": 0, "inequalities": len(ineqs),
        "ray_list": [list(r) for r in rays],
        "ell": [str(v) for v in vals],
        "min": str(min(vals)), "max": str(max(vals)),
        "linear along sampled rays": True,
        "dilate used for the differences": m,
        "interior point": [list(x) for x in unpack(base, N)],
        "interior a1": str(a_base),
        "interior from rays": str(ell(base)),
        "interior identity": ell(base) == a_base,
        "triple a1": str(a1(b0)),
        "triple from rays": str(ell(b0)),
        "triple identity": ell(b0) == a1(b0),
    }
    spot = []
    for _ in range(3):
        v = list(base)
        for k in rng.sample(range(len(rays)), min(3, len(rays))):
            c = rng.randint(1, 3)
            v = [v[i] + c * rays[k][i] for i in range(Z.B)]
        if Z.contains_cell(v, eqs, ineqs) and sum(unpack(v, N)[0]) <= 2 * max_size:
            spot.append(a1(v) == ell(v))
    rec["spot checks"] = spot
    return rec


def main():
    certified = [json.loads(l) for l in gzip.open(os.path.join(CHECK1, "edges.jsonl.gz"), "rt")]
    negative_hosts = [
        ((13, 5, 4, 3, 2), (8, 3, 2, 1), (7, 3, 2, 1)),
        ((11, 6, 5, 4, 1), (7, 4, 3, 1), (6, 3, 2, 1)),
        ((10, 7, 5, 4, 1), (7, 3, 2, 1), (6, 4, 3, 1)),
        ((10, 7, 5, 4, 1), (7, 4, 3, 1), (5, 4, 2, 1)),
        ((9, 7, 5, 4, 2), (6, 4, 3, 1), (6, 4, 2, 1)),
    ]
    by_risk = sorted(certified, key=lambda r: Fraction(r["a1"]) / sum(r["lam"]))
    rng = random.Random(20260905)
    order = ([("a hive polytope with a negative Berline-Vergne class", t) for t in negative_hosts]
             + [("the smallest linear coefficient for its size",
                 (tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))) for r in by_risk[:200]])
    rest = [r for r in certified if r not in by_risk[:200]]
    rng.shuffle(rest)
    order += [("a certified triple of the box",
               (tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"]))) for r in rest]
    a1_of_triple = {(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"])): r["a1"] for r in certified}

    out = open(os.path.join(HERE, "cells.jsonl"), "w")
    t0 = time.time()
    done = 0
    skipped: dict = {}
    worst = None
    for kind, w in order:
        if time.time() - t0 > BUDGET:
            break
        try:
            rec = study(w, rng)
        except Exception as exc:
            skipped[type(exc).__name__] = skipped.get(type(exc).__name__, 0) + 1
            continue
        if isinstance(rec, str):
            skipped[rec] = skipped.get(rec, 0) + 1
            continue
        rec["kind"] = kind
        if w in a1_of_triple:
            rec["certified a1"] = a1_of_triple[w]
        out.write(json.dumps(rec) + "\n")
        out.flush()
        done += 1
        v = Fraction(rec["min"])
        if worst is None or v < worst:
            worst = v
        if done % 25 == 0:
            print(f"{done} cells, {round(time.time() - t0)} s, worst ray value {worst}", flush=True)

    # cells at generic points of the cone: no vertex sits on a wall there, so the cell is
    # full dimensional and covers a fourteen-dimensional piece of the Littlewood-Richardson cone
    pts, idx, hrays = hive_cone_rays(N)
    while time.time() - t0 < BUDGET + GENERIC:
        h = [0] * len(pts)
        for _ in range(rng.randint(6, 16)):
            r = rng.choice(hrays)
            c = rng.randint(1, rng.choice([3, 8, 20, 50]))
            h = [a + c * b for a, b in zip(h, r)]
        w = triple_of_hive(h, idx, N)
        if min(len(x) for x in w) < 3:
            continue
        try:
            rec = study_generic(w, rng)
        except Exception as exc:
            skipped[type(exc).__name__] = skipped.get(type(exc).__name__, 0) + 1
            continue
        if isinstance(rec, str):
            skipped[rec] = skipped.get(rec, 0) + 1
            continue
        rec["kind"] = "a generic point of the cone"
        out.write(json.dumps(rec) + "\n")
        out.flush()
        done += 1
        v = Fraction(rec["min"])
        if worst is None or v < worst:
            worst = v
        print(f"{done} cells, {round(time.time() - t0)} s, rank {rec['cell rank']}, "
              f"minimum {rec['min']}, worst {worst}", flush=True)
    out.close()

    cells = [json.loads(l) for l in open(os.path.join(HERE, "cells.jsonl"))]
    ranks: dict = {}
    for c in cells:
        ranks[c["cell rank"]] = ranks.get(c["cell rank"], 0) + 1
    summary = {
        "cells": len(cells),
        "distinct cells": len({tuple(sorted(tuple(r) for r in c["ray_list"])) for c in cells}),
        "cell ranks": dict(sorted(ranks.items())),
        "skipped": skipped,
        "simplicial cells": sum(1 for c in cells if c["simplicial"]),
        "cells linear along every sampled ray": sum(1 for c in cells
                                                    if c["linear along sampled rays"]),
        "cells where the rays reproduce the interior point": sum(1 for c in cells
                                                                 if c["interior identity"]),
        "cells where the rays reproduce the certified triple": sum(1 for c in cells
                                                                   if c.get("triple identity")),
        "cells whose Ehrhart value matches the certified one":
            sum(1 for c in cells
                if "certified a1" in c and Fraction(c["triple a1"]) == Fraction(c["certified a1"])),
        "cells carrying a certified triple": sum(1 for c in cells if "certified a1" in c),
        "cells at a generic point": sum(1 for c in cells
                                        if c["kind"] == "a generic point of the cone"),
        "spot checks passed": sum(sum(1 for x in c["spot checks"] if x) for c in cells),
        "spot checks run": sum(len(c["spot checks"]) for c in cells),
        "cells with a negative ray value": sum(1 for c in cells if Fraction(c["min"]) < 0),
        "minimum ray value over all cells": str(min(Fraction(c["min"]) for c in cells)),
        "maximum ray value over all cells": str(max(Fraction(c["max"]) for c in cells)),
        "rays checked": sum(c["rays"] for c in cells),
        "seconds": round(time.time() - t0),
    }
    json.dump(summary, open(os.path.join(HERE, "cells.summary.json"), "w"), indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
