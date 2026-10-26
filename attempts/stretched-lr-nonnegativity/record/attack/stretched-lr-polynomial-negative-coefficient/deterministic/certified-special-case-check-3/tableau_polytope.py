#!/usr/bin/env python3
"""A second polytope encoding of the stretched LR polynomial: the tableau polytope.

Littlewood-Richardson tableaux of shape lam/mu and content nu are matrices m_{r,i} >= 0
(row r of the skew shape, letter i) with
  row sums   sum_i m_{r,i} = lam_r - mu_r,
  column sums sum_r m_{r,i} = nu_i,
  column strictness  mu_r + sum_{j<=i} m_{r,j} <= mu_{r-1} + sum_{j<=i-1} m_{r-1,j}  (r >= 2, i >= 1),
  lattice word       sum_{s<=r} m_{s,i+1} <= sum_{s<=r-1} m_{s,i}                     (r >= 1, i >= 1),
the same conditions as lrtableaux.py (validated against lrcalc).  The conditions are
linear with integer coefficients and right-hand sides linear in (lam, mu, nu), so the
polytope T(lam, mu, nu) dilates with t and its Ehrhart polynomial is P(t).  This encoding
shares no inequality with the hive model of hivepoly.py, so agreement of the two Normaliz
computations checks the hive encoder and the interpolation-free pipeline.
"""
from __future__ import annotations

from fractions import Fraction
from typing import List

from hivepoly import normalize


def tableau_inequalities(lam, mu, nu):
    lam, mu, nu = normalize(lam), normalize(mu), normalize(nu)
    n = len(lam)
    k = len(nu)
    mu_p = list(mu) + [0] * (n - len(mu))
    # variables m_{r,i} for 0 <= r < n, 0 <= i < k with i <= r (others are forced to 0)
    var = {}
    for r in range(n):
        for i in range(min(k, r + 1)):
            var[(r, i)] = len(var)
    D = len(var)
    eqs: List[List[int]] = []
    ineqs: List[List[int]] = []
    for r in range(n):
        row = [0] * (D + 1)
        for i in range(min(k, r + 1)):
            row[var[(r, i)]] = 1
        row[D] = -(lam[r] - mu_p[r])
        eqs.append(row)
    for i in range(k):
        row = [0] * (D + 1)
        for r in range(i, n):
            row[var[(r, i)]] = 1
        row[D] = -nu[i]
        eqs.append(row)
    # column strictness: mu_{r-1} + sum_{j<=i-1} m_{r-1,j} - mu_r - sum_{j<=i} m_{r,j} >= 0
    for r in range(1, n):
        for i in range(k):
            row = [0] * (D + 1)
            for j in range(min(i, r)):          # j <= i-1, j <= r-1
                row[var[(r - 1, j)]] += 1
            for j in range(min(i + 1, r + 1)):  # j <= i, j <= r
                row[var[(r, j)]] -= 1
            row[D] = mu_p[r - 1] - mu_p[r]
            ineqs.append(row)
    # lattice: sum_{s<=r-1} m_{s,i} - sum_{s<=r} m_{s,i+1} >= 0
    for r in range(n):
        for i in range(k - 1):
            row = [0] * (D + 1)
            for s in range(i, r):               # s <= r-1, s >= i
                row[var[(s, i)]] += 1
            for s in range(i + 1, r + 1):       # s <= r, s >= i+1
                row[var[(s, i + 1)]] -= 1
            ineqs.append(row)
    for v in range(D):
        row = [0] * (D + 1)
        row[v] = 1
        ineqs.append(row)
    return D, eqs, ineqs


def ehrhart_tableau(lam, mu, nu):
    from PyNormaliz import Cone  # type: ignore

    D, eqs, ineqs = tableau_inequalities(lam, mu, nu)
    C = Cone(inhom_equations=eqs, inhom_inequalities=ineqs)
    dim = C.AffineDim()
    q = C.EhrhartQuasiPolynomial()
    den = q[-1]
    if len(q) - 1 != 1:
        return dim, None
    coeffs = [Fraction(x, den) for x in q[0]]
    while len(coeffs) > 1 and coeffs[-1] == 0:
        coeffs.pop()
    return dim, coeffs


if __name__ == "__main__":
    import json
    import sys

    lam, mu, nu = (json.loads(a) for a in sys.argv[1:4])
    print(ehrhart_tableau(lam, mu, nu))
