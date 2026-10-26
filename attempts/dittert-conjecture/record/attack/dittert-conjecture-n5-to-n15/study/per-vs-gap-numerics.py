"""Does a small permanent force a spectral gap?  Evidence for the missing lemma of
route A (study/route-a-capacity-notes.md).

Sample doubly stochastic matrices B with b_11 = 0 (Sinkhorn scalings of random
positive matrices with one zero, at several entry spreads and with planted
near-block structure), compute per(B)/gamma_n (Ryser, vectorised) and
lambda_2(B) = 1 - second singular value, and print the smallest lambda_2 seen
among matrices with per(B) below given multiples of gamma_n.
"""
import math
import sys

import numpy as np


def sinkhorn(A, iters=3000, tol=1e-13):
    n = A.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = np.einsum("ij,j->i", A, d2) * d1
        d1 = d1 / r
        c = np.einsum("ij,i->j", A, d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return np.einsum("i,ij,j->ij", d1, A, d2)


def permanent(A):
    n = A.shape[0]
    S = np.zeros((1 << n, n))
    sizes = np.zeros(1 << n, dtype=np.int64)
    for b in range(n):
        idx = np.arange(1 << n)
        has = (idx >> b) & 1 == 1
        S[has] += A[:, b]
        sizes[has] += 1
    prods = np.prod(S, axis=1)
    signs = np.where((n - sizes) % 2 == 0, 1.0, -1.0)
    return float((signs * prods)[1:].sum())


rng = np.random.default_rng(11)
for n in [int(a) for a in sys.argv[1:]] or [5, 8, 12]:
    gamma = math.factorial(n) / n ** n
    rows = []
    for trial in range(400):
        kind = trial % 4
        spread = [0.2, 0.7, 1.5, 3.0][trial % 4]
        X = np.exp(spread * rng.standard_normal((n, n)))
        if trial % 8 >= 4:  # planted near-block structure with cross mass eps
            k = rng.integers(1, n)
            eps = 10 ** rng.uniform(-3, -0.3)
            X[:k, k:] *= eps
            X[k:, :k] *= eps
        X[0, 0] = 0.0
        B = sinkhorn(X)
        if abs(B.sum(1) - 1).max() > 1e-8:
            continue
        p = permanent(B) / gamma
        s = np.linalg.svd(B, compute_uv=False)
        rows.append((p, 1 - s[1]))
    rows = np.array(rows)
    print(f"\n== n = {n}: {len(rows)} doubly stochastic samples with b_11 = 0; per/gamma in [{rows[:,0].min():.3f}, {rows[:,0].max():.3g}]")
    for thr in [1.05, 1.1, 1.2, 1.5, 2.0, 5.0]:
        sel = rows[rows[:, 0] <= thr]
        if len(sel):
            print(f"   per/gamma <= {thr:4.2f}: {len(sel):3d} samples, min lambda_2 = {sel[:,1].min():.3f}, median {np.median(sel[:,1]):.3f}")
    sel = rows[rows[:, 1] <= 0.3]
    if len(sel):
        print(f"   lambda_2 <= 0.3: {len(sel)} samples, min per/gamma among them = {sel[:,0].min():.3f}")
