"""Theorem 1 and Theorem 2 at n = 7, 8, 9 with a vectorised Ryser permanent (2^n subsets).

Reports min over random doubly stochastic B of
    per(B) / (gamma_{n-1} max_j K(col_j))          [Theorem 1, must be >= 1]
    per(B) / (gamma_n exp(||E||^2/(2n)))            [Theorem 2, must be >= 1]
and the smallest ratio (per/gamma_n - 1)/||E||^2 seen, for scale.
"""
import math
import sys

import numpy as np


def permanent(A):
    n = A.shape[0]
    idx = np.arange(1 << n)
    S = np.zeros((1 << n, n))
    sizes = np.zeros(1 << n, dtype=np.int64)
    for b in range(n):
        has = (idx >> b) & 1 == 1
        S[has] += A[:, b]
        sizes[has] += 1
    sign = np.where((n - sizes) % 2 == 0, 1.0, -1.0)
    return float((sign * np.prod(S, axis=1))[1:].sum())


def sinkhorn(X, iters=20000, tol=1e-14):
    n = X.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = (X @ d2) * d1
        d1 = d1 / r
        c = (X.T @ d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return d1[:, None] * X * d2[None, :]


def K(w):
    return float(np.prod([(1 - t) ** (1 - t) if t < 1 else 1.0 for t in w]))


rng = np.random.default_rng(2026)
# sanity: Ryser against itertools at n = 4
import itertools
A = rng.uniform(size=(4, 4))
assert abs(permanent(A) - sum(math.prod(A[i, p[i]] for i in range(4)) for p in itertools.permutations(range(4)))) < 1e-12
for n in [int(a) for a in sys.argv[1:]] or [7, 8, 9]:
    gam = math.factorial(n) / n ** n
    gam1 = math.factorial(n - 1) / (n - 1) ** (n - 1)
    w1 = w2 = wq = math.inf
    for t in range(600):
        kind = t % 3
        if kind == 0:
            B = sinkhorn(np.exp([0.3, 1.0, 2.5, 5.0][(t // 3) % 4] * rng.standard_normal((n, n))))
        elif kind == 1:
            m = rng.integers(2, 6)
            wts = rng.dirichlet(np.ones(m))
            B = sum(wts[i] * np.eye(n)[rng.permutation(n)] for i in range(m))
        else:
            lam = rng.uniform(0, 1)
            B = (1 - lam) / n + lam * np.eye(n)[rng.permutation(n)]
        p = permanent(B)
        kmax = max(K(B[:, j]) for j in range(n))
        e2 = float(((B - 1 / n) ** 2).sum())
        w1 = min(w1, p / (gam1 * kmax))
        w2 = min(w2, p / (gam * math.exp(e2 / (2 * n))))
        if e2 > 1e-10:
            wq = min(wq, (p / gam - 1) / e2)
    print(f"n={n}: min per/(gamma_(n-1) max K) = {w1:.9f}, min per/(gamma_n e^(||E||^2/2n)) = {w2:.9f}, "
          f"min (per/gamma-1)/||E||^2 seen = {wq:.4f}, 1/(2n) = {1/(2*n):.4f}")
