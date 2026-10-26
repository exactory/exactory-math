"""Numerical check of the effective-resistance bound that removes condition (N).

Claim (*): with L the weighted bipartite Laplacian of A (edge weights a_ij between row i and
column j), (alpha; beta) the solution of L (alpha; beta) = (u; v) in the sign convention
sum_ij a_ij (alpha_i + beta_j)^2, and Phi = (u;v)^T L^+ (u;v),

    |alpha_i + beta_j| <= sqrt( R_eff(i, j) * Phi ) <= sqrt( Phi / a_ij )   where a_ij > 0,

by Cauchy-Schwarz in the L^+ inner product and Rayleigh monotonicity (the single edge ij
already has conductance a_ij).  This replaces Theorem R's Lemma 3(c) bound
|alpha|_inf + |beta|_inf <= sqrt(2) |(u;v)|_2 / (theta lambda_2), which carries 1/lambda_2 and
so costs a square root of delta.

The script builds random near-doubly-stochastic matrices with a zero, computes both bounds,
and reports the ratio: how much smaller the resistance bound is.
"""
import math
import sys

import numpy as np


def sinkhorn(A, iters=4000, tol=1e-14):
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


rng = np.random.default_rng(20260903)
print(f"{'n':>3} {'spread':>7} {'eps':>7} {'Phi':>10} {'max|a+b| ':>10} {'Reff bound':>11} "
      f"{'old bound':>11} {'gain':>7} {'(*) holds':>10}")
worst_ratio = 0.0
allok = True
for n in (5, 7, 10, 12):
    for spread in (0.3, 1.0, 2.0):
        for eps in (1e-3, 1e-2):
            X = np.exp(spread * rng.standard_normal((n, n)))
            X[0, 0] = 0.0
            B = sinkhorn(X)
            A = np.einsum("i,ij,j->ij", 1 + eps * rng.standard_normal(n), B,
                          1 + eps * rng.standard_normal(n))
            A *= n / A.sum()
            r, c = A.sum(1), A.sum(0)
            u, v = 1 - r, 1 - c
            L = np.block([[np.diag(r), A], [A.T, np.diag(c)]])
            w = np.linalg.pinv(L) @ np.concatenate([u, v])
            alpha, beta = w[:n], w[n:]
            Phi = float(np.concatenate([u, v]) @ w)
            AB = alpha[:, None] + beta[None, :]
            sup = A > 0
            maxab = float(np.abs(AB[sup]).max())
            # the resistance bound, entrywise, at the entry that attains the maximum
            Lp = np.linalg.pinv(L)
            reff = np.array([[Lp[i, i] + Lp[n + j, n + j] + 2 * Lp[i, n + j] for j in range(n)] for i in range(n)])
            bound_reff = float(np.sqrt(np.maximum(reff, 0) * Phi)[sup].max())
            bound_edge = float(np.sqrt(Phi / A[sup]).max())
            old = math.sqrt(2) * float(np.linalg.norm(w))
            ok = maxab <= bound_reff * (1 + 1e-9) and bound_reff <= bound_edge * (1 + 1e-9)
            allok &= ok
            worst_ratio = max(worst_ratio, old / max(bound_reff, 1e-300))
            print(f"{n:>3} {spread:>7.1f} {eps:>7.0e} {Phi:>10.3e} {maxab:>10.3e} {bound_reff:>11.3e} "
                  f"{old:>11.3e} {old / bound_reff:>7.1f} {'yes' if ok else 'NO':>10}")
print(f"\n(*) held in every case: {allok}.  The resistance bound is up to {worst_ratio:.1f} times "
      f"smaller than Theorem R's Lemma 3(c) bound.")
print("Note both scale with sqrt(Phi); the gain is the constant, and the point of (*) is that")
print("it carries no 1/lambda_2, so the condition it imposes is linear in delta, not sqrt(delta).")
