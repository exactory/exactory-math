"""Is the two-column form of the capacity theorem true?

Theorem 2 of route-capacity.md is per(B) >= gamma_n exp(d_j / 2) for every column j, with
d_j = ||col_j - 1/n||^2, and the factor n in a = 1/(2n) comes from ||E||_F^2 = sum_j d_j <= n max_j d_j.
The application at n = 7 needs a >= 1/n, which would follow from any of

    (V1)  per(B) >= gamma_n exp( (d_j + d_l) / 2 )      for every two distinct columns j, l,
    (V2)  per(B) >= gamma_n exp( (d_j + d'_i) / 2 )     for every column j and row i,
    (V3)  per(B) >= gamma_n exp( (d_j + d_l + d_m) / 2 ) for every three distinct columns,

since the best pair has d_j + d_l >= 2 ||E||^2 / n.  This tests each at n = 4..7 over random
doubly stochastic matrices at several spreads, sparse supports, and the structured families,
and reports the worst ratio per(B) / (gamma_n exp(...)).  A ratio below 1 refutes the form.
"""
import itertools
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


def sinkhorn(X, iters=30000, tol=1e-14):
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


def families(n, rng, count):
    yield np.full((n, n), 1.0 / n)
    C = np.eye(n)[[(i + 1) % n for i in range(n)]]
    yield 0.5 * (np.eye(n) + C)
    for t in (0.1, 0.3, 0.5, 0.7, 0.9):
        yield t * np.eye(n) + (1 - t) * C
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1); T[:, 0] = 1 / (n - 1); T[0, 0] = 0.0
    yield T
    for k in range(1, n // 2 + 1):
        B = np.zeros((n, n)); B[:k, :k] = 1.0 / k; B[k:, k:] = 1.0 / (n - k)
        for t in (0.0, 0.2, 0.5, 0.8):
            yield (1 - t) * B + t / n
    for p in itertools.islice(itertools.permutations(range(n)), 4):
        yield np.eye(n)[list(p)]
    for _ in range(count):
        spread = rng.choice([0.2, 0.8, 2.0, 5.0])
        yield sinkhorn(np.exp(spread * rng.standard_normal((n, n))))
    for _ in range(count // 2):
        X = np.exp(2.0 * rng.standard_normal((n, n)))
        X[rng.random((n, n)) < 0.4] = 1e-13
        B = sinkhorn(X)
        if max(abs(B.sum(1) - 1).max(), abs(B.sum(0) - 1).max()) < 1e-11:
            yield B


rng = np.random.default_rng(2718)
print(f"{'n':>3} {'cases':>6} {'V1 two cols':>12} {'V2 col+row':>12} {'V3 three cols':>14} "
      f"{'where V1 worst':>20}")
for n in [int(a) for a in sys.argv[1:]] or [4, 5, 6, 7]:
    g = math.factorial(n) / n ** n
    w1 = w2 = w3 = math.inf
    where = ""
    cnt = 0
    for idx, B in enumerate(families(n, rng, 500 if n <= 6 else 200)):
        p = permanent(B)
        d = ((B - 1.0 / n) ** 2).sum(0)
        dr = ((B - 1.0 / n) ** 2).sum(1)
        cnt += 1
        for j, l in itertools.combinations(range(n), 2):
            r = p / (g * math.exp((d[j] + d[l]) / 2))
            if r < w1:
                w1, where = r, f"case {idx}, cols {j},{l}"
        for j in range(n):
            for i in range(n):
                w2 = min(w2, p / (g * math.exp((d[j] + dr[i]) / 2)))
        for j, l, m in itertools.combinations(range(n), 3):
            w3 = min(w3, p / (g * math.exp((d[j] + d[l] + d[m]) / 2)))
    print(f"{n:>3} {cnt:>6} {w1:>12.6f} {w2:>12.6f} {w3:>14.6f} {where:>20}")
print("\nA value below 1 refutes that form; 1.000000 means an equality case was hit.")
