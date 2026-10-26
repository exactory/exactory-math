"""An independent test of the CONCLUSION of units 1 and 2, not of their certificates.

The theorems claim, for n = 5 and n = 6,

    phi(U_n) - phi(A) >= c_1(n) ||A - U_n||_F^2   for every A in K_n,

with c_1(5) = 32/3125 and c_1(6) = 128/46656.  This script minimises the ratio

    R(A) = (phi(U_n) - phi(A)) / ||A - U_n||_F^2

over K_n by multi-start local optimisation, from random starts, from points near U_n
(where the ratio is governed by the Hessian) and from the Knopp-Sinkhorn boundary
extremal T_n.  A minimum below c_1(n) would refute the theorem; a minimum above it is
independent support.  phi is computed from its definition (row products, column
products, permanent as a sum over permutations), sharing no code with the certificates.
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize


def phi(A, n):
    per = sum(math.prod(A[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n)))
    return float(np.prod(A.sum(1)) * 1.0 + np.prod(A.sum(0)) - per)


def unpack(theta, n):
    w = np.exp(theta - theta.max())
    return (n * w / w.sum()).reshape(n, n)


def ratio(theta, n, gap):
    A = unpack(theta, n)
    d = float(((A - 1 / n) ** 2).sum())
    if d < 1e-14:
        return 1e6
    return (gap - phi(A, n)) / d


for n, c1 in ((5, 32 / 3125), (6, 128 / 46656)):
    N = n * n
    gamma = math.factorial(n) / n ** n
    gap = 2 - gamma
    rng = np.random.default_rng(4242)
    best = (float("inf"), None, "")
    starts = []
    for s in range(400 if n == 5 else 200):
        spread = [0.05, 0.3, 1.0, 3.0][s % 4]
        starts.append((spread * rng.standard_normal(N), f"random spread {spread}"))
    for eps in (1e-1, 1e-2, 1e-3):          # near U_n: the Hessian regime
        for s in range(40):
            starts.append((eps * rng.standard_normal(N), f"near U eps={eps}"))
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)   # Knopp-Sinkhorn extremal (a boundary point)
    T[0, :] = 1 / (n - 1)
    T[:, 0] = 1 / (n - 1)
    T[0, 0] = 1e-14
    starts.append((np.log(T.flatten() / n), "Knopp-Sinkhorn T_n"))
    for th0, label in starts:
        res = minimize(ratio, th0, args=(n, gap), method="Nelder-Mead",
                       options={"maxiter": 4000, "xatol": 1e-9, "fatol": 1e-12})
        if res.fun < best[0]:
            best = (res.fun, unpack(res.x, n), label)
    r, A, label = best
    print(f"n={n}: min ratio found = {r:.8f}   claimed c_1 = {c1:.8f}   "
          f"{'HOLDS with margin x%.2f' % (r / c1) if r >= c1 else '*** VIOLATED ***'}   (from: {label})")
    print(f"      at the minimiser: min entry {A.min():.3e}, ||A-U||_F^2 = {((A - 1 / n) ** 2).sum():.4e}, "
          f"phi gap = {gap - phi(A, n):.4e}")
    sys.stdout.flush()
