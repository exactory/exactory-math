"""Numerical sanity check of the route-A notes (study/route-a-capacity-notes.md).

For random near-doubly-stochastic matrices A in K_n with a_11 = 0, compare
  -log cap(A)        (capacity via Sinkhorn scaling: cap = 1/(prod d1 prod d2))
  rho' + sigma'      (rho' = -log prod r_i, sigma' = -log prod c_j)
  n log(1/(1-t))     (Kafidov's loss, t = sqrt(n (rho+sigma)/(1-rho-sigma)))
  (|u|^2+|v|^2)/lambda_2   (the chi-square correction bound (3)-(4) of the notes)
and report the ratios.  Evidence only; no claim is proved here.
"""
import math
import sys

import numpy as np


def sinkhorn(A, iters=5000, tol=1e-14):
    n = A.shape[0]
    d1 = np.ones(n)
    d2 = np.ones(n)
    for _ in range(iters):
        r = np.einsum("ij,j->i", A, d2) * d1
        d1 = d1 / r
        c = np.einsum("ij,i->j", A, d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return d1, d2


def lambda2(A):
    r = A.sum(1)
    c = A.sum(0)
    Mn = np.einsum("i,ij,j->ij", 1 / np.sqrt(r), A, 1 / np.sqrt(c))
    s = np.linalg.svd(Mn, compute_uv=False)
    return 1 - s[1]


rng = np.random.default_rng(7)
for n in [int(a) for a in sys.argv[1:]] or [5, 8, 15]:
    gamma = math.factorial(n) / n ** n
    print(f"\n== n = {n}: gamma_n = {gamma:.4e}")
    for trial in range(6):
        # a doubly stochastic matrix with a zero (Sinkhorn of a random positive matrix with a_11 = 0),
        # then rows and columns rescaled by (1 + eps * noise) and renormalised to entry sum n
        spread = [0.3, 1.0, 3.0][trial % 3]
        X = np.exp(spread * rng.standard_normal((n, n)))
        X[0, 0] = 0.0
        d1, d2 = sinkhorn(X)
        B = np.einsum("i,ij,j->ij", d1, X, d2)
        eps = [1e-3, 1e-2][trial // 3]
        A = np.einsum("i,ij,j->ij", 1 + eps * rng.standard_normal(n), B, 1 + eps * rng.standard_normal(n))
        A *= n / A.sum()
        r, c = A.sum(1), A.sum(0)
        rho_p, sig_p = -np.log(r).sum(), -np.log(c).sum()
        delta_like = (1 - math.exp(-rho_p)) + (1 - math.exp(-sig_p))
        d1, d2 = sinkhorn(A)
        neglogcap = np.log(d1).sum() + np.log(d2).sum()
        t = math.sqrt(n * delta_like / (1 - delta_like))
        kaf = -n * math.log(1 - t) if t < 1 else float("inf")
        u, v = 1 - r, 1 - c
        l2 = lambda2(A)
        chi = (u @ u + v @ v) / l2
        print(f"  spread {spread:3.1f} eps {eps:.0e}: rho'+sigma' = {rho_p + sig_p:.3e}  -log cap = {neglogcap:.3e} "
              f"(ratio {neglogcap / (rho_p + sig_p):.3f})  Kafidov loss = {kaf:.3e} (ratio {kaf / (rho_p + sig_p):.1f})  "
              f"chi-bound = {chi:.3e} (ratio {chi / (rho_p + sig_p):.2f})  lambda_2 = {l2:.3f}")
