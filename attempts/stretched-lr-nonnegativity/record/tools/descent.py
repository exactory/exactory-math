#!/usr/bin/env python3
"""Local descent on the linear coefficient a_1 of the stretched LR polynomial.

Rassart (2004): on each chamber of the Littlewood-Richardson chamber complex the
coefficients of P(t) are polynomials in (lam, mu, nu), and a_k is homogeneous of degree
k; so a_1 is piecewise linear.  A chamber on which a_1 takes a negative value contains
integer points of every size, but its smallest integer point may be far from the
origin.  This tool starts from a random triple with n parts and walks along the
integer moves that keep |lam| = |mu| + |nu| (a unit transfer inside one partition, or
a unit added to lam and to mu or nu), accepting the move that lowers a_1 most, with
random restarts; every polynomial is computed exactly by Normaliz.  A move to a triple
with c <= 2 or dim H <= 2 is never taken (their polynomials are positive by theorem).

Output: the smallest a_1 found, the triple, its polynomial, and any negative coefficient.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hivepoly import hive_inequalities, normalize  # noqa: E402
from scan import lr_coef  # noqa: E402

_CACHE = {}


def poly(lam, mu, nu):
    """(dim, coeffs) or None when c <= 2 or dim <= 2; cached."""
    from PyNormaliz import Cone  # type: ignore

    key = (tuple(lam), tuple(mu), tuple(nu))
    if key in _CACHE:
        return _CACHE[key]
    res = None
    c = lr_coef(*key)
    if c >= 3:
        D, rows = hive_inequalities(*key)
        C = Cone(inhom_inequalities=rows)
        dim = C.AffineDim()
        if dim >= 3:
            q = C.EhrhartQuasiPolynomial()
            den = q[-1]
            if len(q) - 1 == 1:
                coeffs = [Fraction(x, den) for x in q[0]]
                while len(coeffs) > 1 and coeffs[-1] == 0:
                    coeffs.pop()
                res = (dim, c, coeffs)
    _CACHE[key] = res
    return res


def is_partition(p):
    return all(p[i] >= p[i + 1] for i in range(len(p) - 1)) and all(x >= 0 for x in p)


def neighbours(lam, mu, nu, n):
    """Integer moves keeping |lam| = |mu| + |nu| and at most n parts each."""
    lam, mu, nu = list(lam) + [0] * (n - len(lam)), list(mu) + [0] * (n - len(mu)), list(nu) + [0] * (n - len(nu))
    out = []
    for p_idx, p in enumerate((lam, mu, nu)):
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                q = list(p)
                q[i] += 1
                q[j] -= 1
                if is_partition(q):
                    trip = [list(lam), list(mu), list(nu)]
                    trip[p_idx] = q
                    out.append(tuple(tuple(x for x in t if x) for t in trip))
    for i in range(n):
        for j in range(n):
            for other in (1, 2):
                trip = [list(lam), list(mu), list(nu)]
                trip[0][i] += 1
                trip[other][j] += 1
                if is_partition(trip[0]) and is_partition(trip[other]):
                    out.append(tuple(tuple(x for x in t if x) for t in trip))
                trip = [list(lam), list(mu), list(nu)]
                trip[0][i] -= 1
                trip[other][j] -= 1
                if is_partition(trip[0]) and is_partition(trip[other]) and sum(trip[0]) > 0:
                    out.append(tuple(tuple(x for x in t if x) for t in trip))
    for i in range(n):
        for j in range(n):
            trip = [list(lam), list(mu), list(nu)]
            trip[1][i] += 1
            trip[2][j] -= 1
            if is_partition(trip[1]) and is_partition(trip[2]):
                out.append(tuple(tuple(x for x in t if x) for t in trip))
    return list(dict.fromkeys(out))


def random_triple(rng, n, size):
    """A random triple with n parts and |lam| = size, mu and nu about half each."""
    while True:
        m = rng.randint(size // 3, 2 * size // 3)
        def rp(total):
            cuts = sorted(rng.sample(range(1, total + n), n - 1))
            parts = sorted([b - a - 1 for a, b in zip([0] + cuts, cuts + [total + n])], reverse=True)
            return tuple(x for x in parts if x > 0)
        lam, mu, nu = rp(size), rp(m), rp(size - m)
        if len(lam) <= n and len(mu) <= n and len(nu) <= n and poly(lam, mu, nu):
            return lam, mu, nu


def descend(start, n, max_steps, rng, log):
    cur = start
    dim, c, coeffs = poly(*cur)
    best = (coeffs[1], cur, coeffs)
    for step in range(max_steps):
        cands = []
        for nb in neighbours(*cur, n):
            r = poly(*nb)
            if r is None:
                continue
            d, cc, co = r
            cands.append((co[1], nb, co, d, cc))
        if not cands:
            break
        cands.sort(key=lambda x: x[0])
        a1, nb, co, d, cc = cands[0]
        if any(x < 0 for x in co):
            log(f"NEGATIVE COEFFICIENT {nb} c={cc} dim={d} coeffs={[str(x) for x in co]}")
            return (a1, nb, co), True
        if a1 >= best[0]:
            # local minimum in a_1: take a random sideways move with probability 1/2
            if rng.random() < 0.5 and len(cands) > 1:
                a1, nb, co, d, cc = cands[rng.randint(1, min(5, len(cands) - 1))]
            else:
                break
        cur = nb
        if a1 < best[0]:
            best = (a1, cur, co)
    return best, False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parts", type=int, default=5)
    ap.add_argument("--size", type=int, default=60)
    ap.add_argument("--restarts", type=int, default=20)
    ap.add_argument("--steps", type=int, default=60)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    logf = open(args.out, "a") if args.out else None

    def log(msg):
        print(msg, flush=True)
        if logf:
            logf.write(msg + "\n")
            logf.flush()

    overall = None
    t0 = time.time()
    for r in range(args.restarts):
        start = random_triple(rng, args.parts, args.size)
        best, neg = descend(start, args.parts, args.steps, rng, log)
        a1, trip, co = best
        log(f"restart {r}: start {start} -> min a_1 {a1} ({float(a1):.4f}) at {trip} dim {len(co)-1} c {poly(*trip)[1]} coeffs {[str(x) for x in co]} [{time.time()-t0:.0f}s, cache {len(_CACHE)}]")
        if overall is None or a1 < overall[0]:
            overall = best
        if neg:
            break
    log(f"OVERALL min a_1 {overall[0]} at {overall[1]} coeffs {[str(x) for x in overall[2]]}")


if __name__ == "__main__":
    main()
