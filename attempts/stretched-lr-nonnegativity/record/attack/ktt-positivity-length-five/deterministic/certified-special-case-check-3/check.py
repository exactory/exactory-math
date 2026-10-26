#!/usr/bin/env python3
"""Independent check of the cell certificates.

1. The summary against `cells.jsonl`, every field recomputed.
2. The certified linear coefficient recorded with each cell against the value recorded by
   certified-special-case-check-1 for the same triple.
3. Every extreme ray is a triple of partitions of equal size, and the cell's own triple is a
   nonnegative combination of the rays.
4. The claim itself, on a sample of cells, without Normaliz: the linear coefficient at the cell's
   interior point and at that point plus each of several extreme rays, computed by the
   depth-first hive enumerator of tools/hivepoly.py through the counts at t = 0..6 and a
   polynomial fit, must reproduce the recorded functional. This is the identity the certificate
   rests on: the recorded value at a ray is the increment of the linear coefficient along it.
Exit 0 iff all four hold.
"""
import itertools
import json
import os
import random
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chamber import _rref, solve_coeffs, unpack  # noqa: E402
from hivepoly import count_hives  # noqa: E402

N = 5
bad = 0
cells = [json.loads(l) for l in open(os.path.join(HERE, "cells.jsonl"))]
summary = json.load(open(os.path.join(HERE, "cells.summary.json")))

mins = [Fraction(c["min"]) for c in cells]
maxs = [Fraction(c["max"]) for c in cells]
recomputed = {
    "cells": len(cells),
    "simplicial cells": sum(1 for c in cells if c["simplicial"]),
    "cells with a negative ray value": sum(1 for m in mins if m < 0),
    "minimum ray value over all cells": str(min(mins)),
    "maximum ray value over all cells": str(max(maxs)),
    "rays checked": sum(c["rays"] for c in cells),
}
for k, v in recomputed.items():
    if summary[k] != v:
        bad += 1
        print(f"SUMMARY MISMATCH {k}: summary {summary[k]}, recomputed {v}")
for c in cells:                       # the recorded minimum is the minimum of the recorded values
    vals = [Fraction(x) for x in c["ell"]]
    if Fraction(c["min"]) != min(vals) or Fraction(c["max"]) != max(vals):
        bad += 1
        print(f"MIN/MAX MISMATCH {c['triple']}")
print(f"summary: {len(cells)} cells, {recomputed['cells with a negative ray value']} with a "
      f"negative ray value, minimum {recomputed['minimum ray value over all cells']}, "
      f"maximum {recomputed['maximum ray value over all cells']}, "
      f"{recomputed['rays checked']} rays")

import gzip  # noqa: E402
CHECK1 = os.path.join(HERE, "..", "certified-special-case-check-1")
rec1 = {(tuple(r["lam"]), tuple(r["mu"]), tuple(r["nu"])): r["a1"]
        for r in (json.loads(l) for l in gzip.open(os.path.join(CHECK1, "edges.jsonl.gz"), "rt"))}
n_cert = n_bad = 0
for c in cells:
    key = tuple(tuple(x) for x in c["triple"])
    if key not in rec1:
        continue
    n_cert += 1
    if Fraction(rec1[key]) != Fraction(c["triple a1"]) or Fraction(rec1[key]) != Fraction(c["certified a1"]):
        n_bad += 1
        print(f"CERTIFIED MISMATCH {c['triple']}: {rec1[key]} against {c['triple a1']}")
bad += n_bad
print(f"certified triples: {n_cert} carried by a cell, {n_bad} disagree with "
      f"certified-special-case-check-1")


def is_triple(v):
    lam, mu, nu = v[:N], v[N:2 * N], v[2 * N:]
    ok = all(all(p[i] >= p[i + 1] for i in range(N - 1)) and p[-1] >= 0 for p in (lam, mu, nu))
    return ok and sum(lam) == sum(mu) + sum(nu)


def in_cone(rays, rank, v):
    """Is v a nonnegative combination of the rays? By Caratheodory it is one exactly when some
    subset of `rank` rays gives it nonnegative coordinates, so subsets decide it outright."""
    if len(rays) == rank:
        co = solve_coeffs(rays, v)
        return co is not None and all(x >= 0 for x in co)
    for sub in itertools.combinations(range(len(rays)), rank):
        co = solve_coeffs([rays[i] for i in sub], v)
        if co is not None and all(x >= 0 for x in co):
            return True
    return False


ray_bad = comb_bad = comb_skipped = 0
for c in cells:
    for r in c["ray_list"]:
        if not is_triple(r):
            ray_bad += 1
    wb = []
    for x in c["triple"]:
        wb += list(x) + [0] * (N - len(x))
    rays = [tuple(r) for r in c["ray_list"]]
    from math import comb
    if comb(len(rays), c["cell rank"]) > 5000:
        comb_skipped += 1
        continue
    if not in_cone(rays, c["cell rank"], wb):
        comb_bad += 1
        print(f"NOT IN THE CONE: {c['triple']} against its {c['rays']} rays")
bad += ray_bad + comb_bad
print(f"extreme rays: {sum(c['rays'] for c in cells)} checked, {ray_bad} are not triples of "
      f"partitions of equal size; {len(cells) - comb_skipped} cells whose own triple was tested "
      f"for membership in the cone of its rays, {comb_bad} failures, {comb_skipped} with too many "
      f"subsets to decide")


def a1_by_enumeration(b):
    """The linear coefficient from the depth-first hive enumerator, through t = 0..6."""
    lam, mu, nu = unpack(b, N)
    vals = [count_hives(lam, mu, nu, t=t) for t in range(7)]
    aug = [[Fraction(t ** k) for k in range(7)] + [Fraction(vals[t])] for t in range(7)]
    red, piv = _rref(aug)
    if piv != list(range(7)):
        raise ValueError("the fit is singular")
    return red[1][7]


rng = random.Random(20260906)
small = [c for c in cells if sum(sum(x) for x in c["interior point"]) <= 260]
sample = rng.sample(small, min(12, len(small)))
ind_checked = ind_bad = 0
for c in sample:
    bs = []
    for x in c["interior point"]:
        bs += list(x) + [0] * (N - len(x))
    base = a1_by_enumeration(bs)
    if base != sum(Fraction(x) for x in c["ell"]):
        ind_bad += 1
        print(f"INDEPENDENT BASE MISMATCH {c['interior point']}: enumeration {base}, "
              f"sum of the ray values {sum(Fraction(x) for x in c['ell'])}")
    for k in rng.sample(range(c["rays"]), min(2, c["rays"])):
        r = c["ray_list"][k]
        got = a1_by_enumeration([bs[i] + r[i] for i in range(3 * N)]) - base
        ind_checked += 1
        if got != Fraction(c["ell"][k]):
            ind_bad += 1
            print(f"INDEPENDENT RAY MISMATCH {c['triple']} ray {k}: enumeration {got}, "
                  f"recorded {c['ell'][k]}")
bad += ind_bad
print(f"independent enumeration: {len(sample)} cells and {ind_checked} rays recomputed without "
      f"Normaliz, {ind_bad} mismatches")
sys.exit(1 if bad else 0)
