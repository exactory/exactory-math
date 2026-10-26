#!/usr/bin/env python3
"""Stretched Littlewood-Richardson polynomials through the Knutson-Tao hive polytope.

Notation (the problem's): c^{lam}_{mu,nu} with |lam| = |mu| + |nu|; the stretched
polynomial is P(t) = c^{t lam}_{t mu, t nu}.

Hive model (Knutson-Tao 1999). Side n = max length. Triangle {(x, y): x, y >= 0,
x + y <= n}. Boundary: h(0, 0) = 0; left edge h(0, y) = mu_1 + ... + mu_y;
right edge h(x, n - x) = |mu| + nu_1 + ... + nu_x; bottom edge h(x, 0) =
lam_1 + ... + lam_x.  The number of integer labellings of the (n-1)(n-2)/2 interior
vertices that satisfy the rhombus inequalities (obtuse-corner sum >= acute-corner
sum) equals c^{lam}_{mu,nu}.  The three rhombus families, with h a function on
the triangle:
  (A) h(x+1,y) + h(x,y+1) >= h(x,y)   + h(x+1,y+1)   x,y >= 0, x+y <= n-2
  (B) h(x,y)   + h(x+1,y) >= h(x,y+1) + h(x+1,y-1)   y >= 1,  x+y <= n-1
  (C) h(x,y)   + h(x,y+1) >= h(x+1,y) + h(x-1,y+1)   x >= 1,  x+y <= n-1
Every inequality is linear with integer coefficients in the interior entries and a
right-hand side linear in (lam, mu, nu), so H(t lam, t mu, t nu) = t H(lam, mu, nu)
and P(t) is the Ehrhart function of the rational polytope H = H(lam, mu, nu).
Derksen-Weyman (2002) proved that P(t) is a polynomial.

Two independent counting routes are provided:
  * `hive_inequalities` + Normaliz (`ehrhart_polynomial`): Ehrhart quasi-polynomial
    of H computed by PyNormaliz from the inequality description.
  * `count_hives`: direct depth-first enumeration of the integer hives of t H, with
    interval propagation, no Normaliz.
And a third, sharing no code with either, through the classical LR rule: `lrcalc`.
"""
from __future__ import annotations

import itertools
from fractions import Fraction
from functools import lru_cache
from typing import Dict, List, Sequence, Tuple

Partition = Tuple[int, ...]


def normalize(p: Sequence[int]) -> Partition:
    p = tuple(int(x) for x in p if int(x) != 0)
    if any(p[i] < p[i + 1] for i in range(len(p) - 1)) or any(x < 0 for x in p):
        raise ValueError(f"not a partition: {p}")
    return p


def hive_setup(lam, mu, nu):
    """Return (n, interior vertex list, index map, boundary dict) for the hive of side n."""
    lam, mu, nu = normalize(lam), normalize(mu), normalize(nu)
    if sum(lam) != sum(mu) + sum(nu):
        raise ValueError("|lam| must equal |mu| + |nu|")
    n = max(len(lam), len(mu), len(nu), 1)
    lam_p = list(lam) + [0] * (n - len(lam))
    mu_p = list(mu) + [0] * (n - len(mu))
    nu_p = list(nu) + [0] * (n - len(nu))
    boundary: Dict[Tuple[int, int], int] = {}
    for y in range(n + 1):
        boundary[(0, y)] = sum(mu_p[:y])
    for x in range(n + 1):
        boundary[(x, 0)] = sum(lam_p[:x])
    for x in range(n + 1):
        boundary[(x, n - x)] = sum(mu_p) + sum(nu_p[:x])
    interior = [(x, y) for x in range(1, n) for y in range(1, n) if x + y <= n - 1]
    index = {v: i for i, v in enumerate(interior)}
    return n, interior, index, boundary


def hive_inequalities(lam, mu, nu):
    """Inequalities a.x + b >= 0 on the interior entries x (Normaliz inhom_inequalities format)."""
    n, interior, index, boundary = hive_setup(lam, mu, nu)
    D = len(interior)
    rows: List[List[int]] = []

    def add(plus, minus):
        row = [0] * (D + 1)
        for v in plus:
            if v in index:
                row[index[v]] += 1
            else:
                row[D] += boundary[v]
        for v in minus:
            if v in index:
                row[index[v]] -= 1
            else:
                row[D] -= boundary[v]
        if any(row[:D]):
            rows.append(row)
        elif row[D] < 0:
            raise ValueError("boundary rhombus violated: the LR coefficient is 0")

    for x in range(n + 1):
        for y in range(n + 1):
            if x + y <= n - 2:
                add([(x + 1, y), (x, y + 1)], [(x, y), (x + 1, y + 1)])          # (A)
            if y >= 1 and x + y <= n - 1:
                add([(x, y), (x + 1, y)], [(x, y + 1), (x + 1, y - 1)])          # (B)
            if x >= 1 and x + y <= n - 1:
                add([(x, y), (x, y + 1)], [(x + 1, y), (x - 1, y + 1)])          # (C)
    return D, rows


def count_hives(lam, mu, nu, t: int = 1, cap: int | None = None) -> int:
    """Number of integer points of t*H(lam,mu,nu) by depth-first enumeration with bounds.

    Returns -1 when `cap` partial assignments are exceeded."""
    lam = tuple(t * x for x in normalize(lam))
    mu = tuple(t * x for x in normalize(mu))
    nu = tuple(t * x for x in normalize(nu))
    D, rows = hive_inequalities(lam, mu, nu)
    if D == 0:
        return 1
    # Order variables; for each variable collect the inequalities whose last variable it is.
    order = list(range(D))
    last_of: List[List[Tuple[List[int], int]]] = [[] for _ in range(D)]
    for row in rows:
        a, b = row[:D], row[D]
        support = [i for i in range(D) if a[i]]
        last = max(support)
        last_of[last].append((a, b))
    count = 0
    nodes = 0
    x = [0] * D

    def rec(i: int):
        nonlocal count, nodes
        nodes += 1
        if cap is not None and nodes > cap:
            raise OverflowError
        lo, hi = -10 ** 18, 10 ** 18
        for a, b in last_of[i]:
            s = b + sum(a[j] * x[j] for j in range(i))
            c = a[i]
            # c*x_i + s >= 0
            if c > 0:
                lo = max(lo, -(s // c))   # ceil(-s/c)
            else:
                hi = min(hi, s // (-c))   # floor(s/(-c))
        if lo > hi:
            return
        if i == D - 1:
            count += hi - lo + 1
            return
        for v in range(lo, hi + 1):
            x[i] = v
            rec(i + 1)

    try:
        rec(0)
    except OverflowError:
        return -1
    return count


def ehrhart_polynomial(lam, mu, nu):
    """Exact Ehrhart (quasi-)polynomial of H(lam,mu,nu) via Normaliz.

    Returns (dim, period, coeffs) where coeffs is a list of Fractions low->high
    when the period is 1; otherwise coeffs is a list of lists (one per residue)."""
    from PyNormaliz import Cone  # type: ignore

    D, rows = hive_inequalities(lam, mu, nu)
    if D == 0:
        return 0, 1, [Fraction(1)]
    C = Cone(inhom_inequalities=rows)
    dim = C.AffineDim()
    q = C.EhrhartQuasiPolynomial()
    # PyNormaliz format: [[coeffs of component 0 ...], ..., denominator]
    period = len(q) - 1
    den = q[-1]
    comps = [[Fraction(c, den) for c in comp] for comp in q[:-1]]
    if period == 1:
        return dim, 1, comps[0]
    return dim, period, comps


def lrcalc_coef(lam, mu, nu) -> int:
    import lrcalc  # type: ignore

    return int(lrcalc.lrcoef(list(normalize(lam)), list(normalize(mu)), list(normalize(nu))))


def has_negative(coeffs) -> bool:
    return any(c < 0 for c in coeffs)


if __name__ == "__main__":
    import sys, json

    lam, mu, nu = (json.loads(a) for a in sys.argv[1:4])
    dim, period, coeffs = ehrhart_polynomial(lam, mu, nu)
    print("dim", dim, "period", period)
    print("coeffs low->high", [str(c) for c in coeffs] if period == 1 else coeffs)
    print("negative", has_negative(coeffs) if period == 1 else None)
