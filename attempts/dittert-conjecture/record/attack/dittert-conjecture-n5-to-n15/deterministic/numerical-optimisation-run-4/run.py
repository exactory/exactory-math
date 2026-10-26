"""Numerical optimisation run 4: the smallest spectral gap of a near-maximiser with a zero.

Hypothesis G(n, c) of study/route-a-reduction-theorem.md asks that every A in K_n with
phi(A) >= 2 - gamma_n and a zero entry has lambda_2(A) = 1 - sigma_2(D_r^{-1/2} A D_c^{-1/2})
>= c.  No such A is known (the conjecture says none exists), so this run minimises
lambda_2 over the relaxation "doubly stochastic with a zero entry and per(B) <= (1 + eta)
gamma_n": B = Sinkhorn(exp(theta)) with theta_11 = -infinity, objective
lambda_2(B) + penalty * max(0, per(B)/gamma_n - 1 - eta), multi-start Nelder-Mead
for n = 5..8, eta = 0.05.  Records the smallest lambda_2 found and the matrix attaining
it, against the required c_n.  Evidence only.
"""
import json
import math
import sys

import numpy as np
from scipy.optimize import minimize


def sinkhorn(A, iters=3000, tol=1e-12):
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
    idx = np.arange(1 << n)
    for b in range(n):
        has = (idx >> b) & 1 == 1
        S[has] += A[:, b]
        sizes[has] += 1
    return float((np.where((n - sizes) % 2 == 0, 1.0, -1.0) * np.prod(S, axis=1))[1:].sum())


def lambda2(B):
    return 1.0 - np.linalg.svd(B, compute_uv=False)[1]


def build(theta, n):
    X = np.exp(theta.reshape(n, n) - theta.max())
    X[0, 0] = 0.0
    return sinkhorn(X)


def c_n(n):
    g = math.factorial(n) / n ** n
    h = math.sqrt(2 * g)
    k = 1 / ((1 - g) * (1 - 2 * h / 3))
    return 2 * math.sqrt(g * k) / (1 - h)


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [5, 6, 7, 8]
    eta, penalty = 0.05, 50.0
    rng = np.random.default_rng(20260903)
    out = {}
    for n in ns:
        gamma = math.factorial(n) / n ** n

        def f(theta):
            B = build(theta, n)
            return lambda2(B) + penalty * max(0.0, permanent(B) / gamma - 1 - eta)

        best = None
        starts = {5: 60, 6: 40, 7: 25, 8: 12}.get(n, 8)
        for s in range(starts):
            spread = [0.3, 1.0, 2.0][s % 3]
            th0 = spread * rng.standard_normal(n * n)
            if s % 2 == 1:  # planted near-block structure
                k = rng.integers(1, n)
                th0.reshape(n, n)[:k, k:] -= 3
                th0.reshape(n, n)[k:, :k] -= 3
            res = minimize(f, th0, method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-6, "fatol": 1e-9})
            B = build(res.x, n)
            p = permanent(B) / gamma
            l2 = lambda2(B)
            if p <= 1 + eta + 1e-6 and (best is None or l2 < best[0]):
                best = (l2, p, B)
        l2, p, B = best
        out[n] = {"n": n, "eta": eta, "min_lambda2": l2, "per_over_gamma": p, "c_n": c_n(n), "starts": starts,
                  "matrix": B.tolist()}
        print(f"n={n}: min lambda_2 over feasible optima = {l2:.4f} (per/gamma = {p:.4f}), required c_n = {c_n(n):.4f}, ratio {l2 / c_n(n):.1f}", flush=True)
        json.dump(out, open("gap-minima.json", "w"), indent=1)
