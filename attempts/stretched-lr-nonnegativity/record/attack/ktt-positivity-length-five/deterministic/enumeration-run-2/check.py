#!/usr/bin/env python3
"""Independent check of the atlas-driven cell functionals.

1. The summary against `cells.jsonl`, every field recomputed, and each cell's recorded minimum
   and maximum against its own list of ray values.
2. Every extreme ray is a triple of partitions of equal size.
3. The identity the sweep rests on, at a point the run never evaluated: the sum of a cell's
   extreme rays lies in the relative interior of the cell, and the functional's value there is
   the sum of the ray values, so the linear Ehrhart coefficient at that triple must equal that
   sum. The checker computes it from the Ehrhart quasi-polynomial, which the run did not use for
   these cells at all, and for the smallest of them again from the depth-first hive enumerator
   through the counts at t = 0..6, which shares no code with either.
Exit 0 iff all three hold.
"""
import json
import os
import random
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chamber import _rref, a1_of, unpack  # noqa: E402
from hivepoly import count_hives  # noqa: E402

N = 5
bad = 0
cells = [json.loads(l) for l in open(os.path.join(HERE, "cells.jsonl"))]
summary = json.load(open(os.path.join(HERE, "cells.summary.json")))

mins = [Fraction(c["min"]) for c in cells]
recomputed = {
    "phase B cells": len(cells),
    "phase B cells that are full dimensional": sum(1 for c in cells if c["cell rank"] == 14),
    "phase B rays evaluated": sum(c["rays"] for c in cells),
    "phase B cells with a negative ray value": sum(1 for m in mins if m < 0),
    "phase B minimum ray value": str(min(mins, default=0)),
    "phase B maximum ray value": str(max((Fraction(c["max"]) for c in cells), default=0)),
    "phase B largest triple": max((c["size"] for c in cells), default=0),
}
for k, v in recomputed.items():
    if summary[k] != v:
        bad += 1
        print(f"SUMMARY MISMATCH {k}: summary {summary[k]}, recomputed {v}")
for c in cells:
    vals = [Fraction(x) for x in c["ell"]]
    if Fraction(c["min"]) != min(vals) or Fraction(c["max"]) != max(vals):
        bad += 1
        print(f"MIN/MAX MISMATCH {c['triple']}")
if summary["phase A cells whose ray values differ from certified-special-case-check-3"] or \
        summary["phase A cells whose value at the triple differs"]:
    bad += 1
    print("PHASE A MISMATCH recorded in the summary")
print(f"summary: {len(cells)} swept cells, {recomputed['phase B cells that are full dimensional']}"
      f" of them full dimensional, {recomputed['phase B rays evaluated']} rays, "
      f"{recomputed['phase B cells with a negative ray value']} with a negative ray value, "
      f"minimum {recomputed['phase B minimum ray value']}, largest triple "
      f"{recomputed['phase B largest triple']}; phase A compared "
      f"{summary['phase A rays compared']} rays with 0 mismatches")


def is_triple(v):
    lam, mu, nu = v[:N], v[N:2 * N], v[2 * N:]
    ok = all(all(p[i] >= p[i + 1] for i in range(N - 1)) and p[-1] >= 0 for p in (lam, mu, nu))
    return ok and sum(lam) == sum(mu) + sum(nu)


ray_bad = sum(1 for c in cells for r in c["ray_list"] if not is_triple(r))
bad += ray_bad
print(f"extreme rays: {sum(c['rays'] for c in cells)} checked, {ray_bad} are not triples of "
      f"partitions of equal size")


CAP = 4 * 10 ** 6


def a1_by_enumeration(b):
    """The linear coefficient from the depth-first hive enumerator, or None when the number of
    hives at t = 6 passes the cap the checker can afford."""
    lam, mu, nu = unpack(b, N)
    vals = []
    for t in range(7):
        try:
            v = count_hives(lam, mu, nu, t=t, cap=CAP)
        except OverflowError:
            return None
        if v < 0:
            return None
        vals.append(v)
    aug = [[Fraction(t ** k) for k in range(7)] + [Fraction(vals[t])] for t in range(7)]
    red, piv = _rref(aug)
    if piv != list(range(7)):
        raise ValueError("the fit is singular")
    return red[1][7]


rng = random.Random(20260906)
points = []
for c in cells:
    bs = [sum(r[i] for r in c["ray_list"]) for i in range(3 * N)]
    points.append((c, bs, sum(bs[:N])))
points.sort(key=lambda x: x[2])
ehr_checked = ehr_bad = 0
for c, bs, size in points[:10]:
    want = sum(Fraction(x) for x in c["ell"])
    got = a1_of(list(bs), N)
    ehr_checked += 1
    if got != want:
        ehr_bad += 1
        print(f"EHRHART MISMATCH at the ray sum of {c['triple']}: {got} against {want}")
bad += ehr_bad
print(f"the ray sum, by the Ehrhart quasi-polynomial the sweep never used: {ehr_checked} cells, "
      f"{ehr_bad} mismatches")

enum_checked = enum_bad = enum_skipped = 0
for c, bs, size in points[:12]:
    if enum_checked >= 3:
        break
    want = sum(Fraction(x) for x in c["ell"])
    got = a1_by_enumeration(bs)
    if got is None:
        enum_skipped += 1
        continue
    enum_checked += 1
    if got != want:
        enum_bad += 1
        print(f"ENUMERATION MISMATCH at the ray sum of {c['triple']}: {got} against {want}")
bad += enum_bad
print(f"the ray sum again, by the depth-first hive enumerator: {enum_checked} cells, "
      f"{enum_bad} mismatches, {enum_skipped} skipped for having more hives than the cap")
# 4. the weights this run computed on top of the atlas, against the closed formulas of
# Castillo-Liu wherever the transverse cone and its lattice split into unimodular blocks of
# dimension at most three. The sweep's new ingredient is these weights, so they get their own
# independent value, computed from a formula the recursion never touches.
from bvweight import _rref as bv_rref, det, saturated_basis  # noqa: E402
from transverse import transverse_cone  # noqa: E402

split_checked = split_bad = 0
if os.path.exists(os.path.join(HERE, "weights.jsonl")):
    computed = [json.loads(l) for l in open(os.path.join(HERE, "weights.jsonl"))]
    for r in computed:
        rays, gram = transverse_cone([list(v) for v in r["normals"]])
        if len(rays) != len(gram):
            continue                                   # not simplicial, no closed formula
        G = [[Fraction(x) for x in row] for row in gram]

        def ip(a, b):
            return sum(Fraction(a[i]) * G[i][j] * Fraction(b[j])
                       for i in range(len(G)) for j in range(len(G)))

        n = len(rays)
        par = list(range(n))

        def find(a):
            while par[a] != a:
                par[a] = par[par[a]]
                a = par[a]
            return a

        for i in range(n):
            for j in range(i + 1, n):
                if ip(rays[i], rays[j]) != 0:
                    a, b = find(i), find(j)
                    if a != b:
                        par[a] = b
        comp = {}
        for i in range(n):
            comp.setdefault(find(i), []).append(i)
        parts = list(comp.values())
        if len(parts) < 2 or max(len(p) for p in parts) > 3:
            continue
        dsum = []
        for p in parts:
            dsum += saturated_basis([list(rays[a]) for a in p], len(G))
        if len(dsum) != len(G) or abs(det([[Fraction(x) for x in v] for v in dsum])) != 1:
            continue
        unimodular = True
        for p in parts:
            sat = saturated_basis([list(rays[a]) for a in p], len(G))
            if len(sat) != len(p):
                unimodular = False
                break
            B = [[Fraction(sat[i][c]) for i in range(len(sat))] for c in range(len(G))]
            M = []
            for a in p:
                red, piv = bv_rref([B[c][:] + [Fraction(rays[a][c])] for c in range(len(G))])
                sol = [Fraction(0)] * len(sat)
                for i, q in enumerate(piv):
                    if q < len(sat):
                        sol[q] = red[i][len(sat)]
                M.append(sol)
            if abs(det([[M[i][j] for j in range(len(sat))] for i in range(len(p))])) != 1:
                unimodular = False
                break
        if not unimodular:
            continue
        prod = Fraction(1)
        for p in parts:
            M = [[ip(rays[a], rays[b]) for b in p] for a in p]
            if len(p) == 1:
                prod *= Fraction(1, 2)
            elif len(p) == 2:
                prod *= Fraction(1, 4) + Fraction(1, 12) * (M[0][1] / M[0][0] + M[0][1] / M[1][1])
            else:
                t = Fraction(1, 8)
                for i in range(3):
                    for j in range(i + 1, 3):
                        t += Fraction(1, 24) * M[i][j] * (Fraction(1) / M[i][i]
                                                          + Fraction(1) / M[j][j])
                prod *= t
        split_checked += 1
        if prod != Fraction(r["weight"]):
            split_bad += 1
            print(f"WEIGHT MISMATCH {r['normals']}: recursion {r['weight']}, product {prod}")
    bad += split_bad
    print(f"weights computed by this run: {len(computed)} held, {split_checked} whose cone and "
          f"lattice split into unimodular blocks checked against the products of the closed "
          f"formulas, {split_bad} mismatches")
sys.exit(1 if bad else 0)
