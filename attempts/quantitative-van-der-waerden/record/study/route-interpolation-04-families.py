"""Structured families: how far the ratio (per/gamma - 1)/||E||^2 sits above 1/4, and whether the
third-order remainder  rem3 = (per/gamma - 1 - (n/(2(n-1))) ||E||^2) / ||E||^3  stays bounded
uniformly in n.

Families (B = J/n + E):
  rank-one   B_M = J/n + (M/n) v v^T, v = (1, -1/(n-1), ..., -1/(n-1)), 0 < M <= n-1
             (M = n-1 is diag(1, J_{n-1}/(n-1)); the (1,1) entry is (1+M)/n);
  cycle      (I + C_n)/2;
  KS         T_n, the Knopp-Sinkhorn minimiser on the face B_11 = 0;
  block      diag(J_k/k, J_{n-k}/(n-k)).
"""
import math

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


def report(tag, B):
    n = B.shape[0]
    gamma = math.factorial(n) / n ** n
    E = B - 1.0 / n
    d2 = (E ** 2).sum()
    ratio = (permanent(B) / gamma - 1) / d2
    loc = n / (2 * (n - 1))
    rem3 = (permanent(B) / gamma - 1 - loc * d2) / d2 ** 1.5
    print(f"  {tag:28s} ||E||^2={d2:8.4f}  ratio={ratio:8.4f}  rem3={rem3:+8.4f}  "
          f"max|E|={abs(E).max():.3f}")


for n in (4, 6, 8, 10, 12):
    print(f"n = {n}")
    v = np.full(n, -1.0 / (n - 1))
    v[0] = 1.0
    for M in (0.1, 0.5, 1.0, 2.0, 4.0, n - 1):
        if M > n - 1:
            continue
        B = 1.0 / n + (M / n) * np.outer(v, v)
        assert B.min() >= -1e-12
        report(f"rank-one M={M:.1f}", B)
    C = np.roll(np.eye(n), 1, axis=1)
    report("cycle (I+C)/2", (np.eye(n) + C) / 2)
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1.0 / (n - 1)
    T[:, 0] = 1.0 / (n - 1)
    T[0, 0] = 0.0
    report("Knopp-Sinkhorn T_n", T)
    for k in (1, 2, n // 2):
        B = np.zeros((n, n))
        B[:k, :k] = 1.0 / k
        B[k:, k:] = 1.0 / (n - k)
        report(f"block diag k={k}", B)
