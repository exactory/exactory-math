"""Measure K = sup ( -log cap(A) ) / ( |u|^2 + |v|^2 ) over near-doubly-stochastic matrices.

`H(n, K)` closes Dittert's conjecture at `n` as soon as `K < K_max(n)` (see conditional-K.py:
1.00 at n = 7, 1.94 at n = 8, 8.09 at n = 10, 417 at n = 15).  This script estimates the
supremum two ways:

  * over random near-doubly-stochastic matrices with a zero, at several entry spreads and
    margin sizes;
  * by direct maximisation of the ratio (multi-start Nelder-Mead).

`-log cap(A)` is computed as `sum log d1 + sum log d2` for the Sinkhorn factors, which is
exact up to the Sinkhorn tolerance.  The ratio is scale invariant in the margins only to
leading order, so the small-margin limit is reported separately: that limit is the constant
the theorem needs.
"""
import math
import sys

import numpy as np
from scipy.optimize import minimize


def sinkhorn_factors(A, iters=200000, tol=1e-15):
    n = A.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = np.einsum("ij,j->i", A, d2) * d1
        d1 = d1 / r
        c = np.einsum("ij,i->j", A, d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return d1, d2


def ratio(A):
    r, c = A.sum(1), A.sum(0)
    u, v = 1 - r, 1 - c
    den = float(u @ u + v @ v)
    if den < 1e-30:
        return 0.0
    d1, d2 = sinkhorn_factors(A)
    negcap = float(np.log(d1).sum() + np.log(d2).sum())
    return negcap / den


rng = np.random.default_rng(20260904)
print(f"{'n':>3} {'eps':>7} {'random max K':>13} {'optimised K':>12} {'K_max(n)':>10} {'headroom':>9}")
for n in [int(a) for a in sys.argv[1:]] or [5, 7, 10, 12]:
    g = math.factorial(n) / n ** n
    m = math.factorial(n - 2) * ((n - 2) / (n - 1) ** 2) ** (n - 2)
    h = math.sqrt(2 * g)
    kap = 1 / ((1 - g) * (1 - 2 * h / 3))
    kmax = math.log(m / g) / (2 * g * kap)
    for eps in (1e-2, 1e-3):
        best = 0.0
        for _ in range(300):
            spread = rng.choice([0.3, 1.0, 2.0, 3.0])
            X = np.exp(spread * rng.standard_normal((n, n)))
            X[0, 0] = 0.0
            d1, d2 = sinkhorn_factors(X)
            B = np.einsum("i,ij,j->ij", d1, X, d2)
            A = np.einsum("i,ij,j->ij", 1 + eps * rng.standard_normal(n), B,
                          1 + eps * rng.standard_normal(n))
            A *= n / A.sum()
            best = max(best, ratio(A))

        def negobj(th):
            X = np.exp(th[:n * n].reshape(n, n))
            X[0, 0] = 0.0
            d1, d2 = sinkhorn_factors(X)
            B = np.einsum("i,ij,j->ij", d1, X, d2)
            A = np.einsum("i,ij,j->ij", np.exp(eps * th[n * n:n * n + n]), B,
                          np.exp(eps * th[n * n + n:]))
            A *= n / A.sum()
            return -ratio(A)

        opt = 0.0
        for s in range(12):
            th0 = np.concatenate([rng.standard_normal(n * n) * [0.5, 1.5, 3.0][s % 3],
                                  rng.standard_normal(2 * n)])
            res = minimize(negobj, th0, method="Nelder-Mead",
                           options={"maxiter": 3000, "xatol": 1e-7, "fatol": 1e-10})
            opt = max(opt, -res.fun)
        K = max(best, opt)
        print(f"{n:>3} {eps:>7.0e} {best:>13.4f} {opt:>12.4f} {kmax:>10.4g} "
              f"{'OK x%.2f' % (kmax / K) if K < kmax else 'FAILS':>9}")
