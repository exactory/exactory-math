"""Independent check of the two inequalities the capacity route claims.

Theorem 1 (one column).  For every doubly stochastic n x n matrix B and every column j,

    per(B) >= gamma_{n-1} * prod_i (1 - b_ij)^(1 - b_ij),      gamma_m = m!/m^m.

Theorem 2 (the consequence).  With E = B - J_n/n,

    per(B) >= gamma_n * exp( ||E||_F^2 / (2n) ).

Both are checked here by an implementation written from the statements alone, over random
doubly stochastic matrices at several spreads, over the structured families that are extremal
for the problem, and over the vertices.  A ratio below 1 at any point refutes the statement.
"""
import itertools
import math
import sys

import numpy as np


def permanent(A):
    n = A.shape[0]
    return float(sum(math.prod(A[i, p[i]] for i in range(n))
                     for p in itertools.permutations(range(n))))


def sinkhorn(X, iters=20000, tol=1e-15):
    n = X.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = np.einsum("ij,j->i", X, d2) * d1
        d1 = d1 / r
        c = np.einsum("ij,i->j", X, d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return np.einsum("i,ij,j->ij", d1, X, d2)


def gamma(m):
    return math.factorial(m) / m ** m if m >= 1 else 1.0


def thm1_rhs(B, j):
    n = B.shape[0]
    return gamma(n - 1) * math.prod((1 - B[i, j]) ** (1 - B[i, j]) if B[i, j] < 1 else 1.0
                                    for i in range(n))


def thm2_rhs(B):
    n = B.shape[0]
    e2 = float(((B - 1.0 / n) ** 2).sum())
    return gamma(n) * math.exp(e2 / (2 * n))


def families(n, rng, count):
    yield np.full((n, n), 1.0 / n)
    C = np.eye(n)[[(i + 1) % n for i in range(n)]]
    yield 0.5 * (np.eye(n) + C)
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1); T[:, 0] = 1 / (n - 1); T[0, 0] = 0.0
    yield T
    for k in range(1, n // 2 + 1):
        B = np.zeros((n, n)); B[:k, :k] = 1.0 / k; B[k:, k:] = 1.0 / (n - k)
        yield B
    for p in itertools.islice(itertools.permutations(range(n)), 6):
        yield np.eye(n)[list(p)]
    for _ in range(count):
        spread = rng.choice([0.2, 0.8, 2.0, 5.0])
        yield sinkhorn(np.exp(spread * rng.standard_normal((n, n))))
    for _ in range(count // 2):                     # sparse supports
        X = np.exp(2.0 * rng.standard_normal((n, n)))
        X[rng.random((n, n)) < 0.35] = 1e-12
        try:
            yield sinkhorn(X)
        except Exception:
            pass


rng = np.random.default_rng(31415)
print(f"{'n':>3} {'cases':>7} {'min ratio Thm1':>16} {'min ratio Thm2':>16} {'both hold':>10}")
allok = True
for n in [int(a) for a in sys.argv[1:]] or [2, 3, 4, 5, 6, 7, 8]:
    m1 = math.inf
    m2 = math.inf
    cnt = 0
    for B in families(n, rng, 400 if n <= 6 else 120):
        if not np.isfinite(B).all() or B.min() < -1e-12:
            continue
        if max(abs(B.sum(axis=1) - 1).max(), abs(B.sum(axis=0) - 1).max()) > 1e-12:
            continue                              # not doubly stochastic to working precision
        p = permanent(np.clip(B, 0, None))
        cnt += 1
        for j in range(n):
            r = thm1_rhs(B, j)
            if r > 0:
                m1 = min(m1, p / r)
        r2 = thm2_rhs(B)
        m2 = min(m2, p / r2)
    ok = m1 > 1 - 1e-9 and m2 > 1 - 1e-9
    allok &= ok
    print(f"{n:>3} {cnt:>7} {m1:>16.10f} {m2:>16.10f} {'yes' if ok else 'NO':>10}")
print(f"\nBoth statements held in every case: {allok}")
