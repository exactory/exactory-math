"""How far apart are lambda_2(A) and lambda_2(B) for A and its Sinkhorn scaling B?

Theorem R's Lemma 2 bounds the scaling cost K by the energy of A's own weighted bipartite
Laplacian, so the spectral quantity it needs is

    lambda_2(A) = 1 - sigma_2( D_r^{-1/2} A D_c^{-1/2} ),

while the capacity route bounds lambda_2(B) = 1 - sigma_2(B) for the doubly stochastic scaling.
Pinsker bounds ||A - B||_1 by sqrt(2 n K), which is large at the sizes that matter, so the crude
comparison lambda_2(A) >= lambda_2(B) - ||L_A - L_B|| loses too much.  This measures the truth:
over near-doubly-stochastic A with a zero entry, at several margin sizes and entry spreads, it
reports lambda_2(A) - lambda_2(B) against the margin size |(u; v)| and against sqrt(2 n K).

If the difference scales with the margin rather than with sqrt(K), the comparison costs
O(sqrt(gamma_n kappa_n)) and is free; if it scales with sqrt(2 n K), it is fatal at n = 7, 8.
"""
import math
import sys

import numpy as np


def sinkhorn_factors(X, iters=200000, tol=1e-15):
    n = X.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = np.einsum("ij,j->i", X, d2) * d1
        d1 = d1 / r
        c = np.einsum("ij,i->j", X, d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return d1, d2


def lam2_general(A):
    r, c = A.sum(1), A.sum(0)
    M = np.einsum("i,ij,j->ij", 1 / np.sqrt(r), A, 1 / np.sqrt(c))
    return 1.0 - float(np.linalg.svd(M, compute_uv=False)[1])


rng = np.random.default_rng(20260904)
print(f"{'n':>3} {'spread':>7} {'eps':>7} {'|(u;v)|':>10} {'K':>10} {'sqrt(2nK)':>11} "
      f"{'lam2(A)':>9} {'lam2(B)':>9} {'difference':>11} {'diff/|(u;v)|':>13}")
worst_ratio_margin = 0.0
worst_ratio_sqrtK = 0.0
for n in [int(a) for a in sys.argv[1:]] or [7, 8, 10, 12]:
    for spread in (0.3, 1.0, 2.0):
        for eps in (1e-3, 1e-2, 5e-2):
            X = np.exp(spread * rng.standard_normal((n, n)))
            X[0, 0] = 0.0
            d1, d2 = sinkhorn_factors(X)
            B = np.einsum("i,ij,j->ij", d1, X, d2)
            A = np.einsum("i,ij,j->ij", np.exp(eps * rng.standard_normal(n)), B,
                          np.exp(eps * rng.standard_normal(n)))
            A *= n / A.sum()
            u, v = 1 - A.sum(1), 1 - A.sum(0)
            mnorm = float(np.sqrt(u @ u + v @ v))
            e1, e2 = sinkhorn_factors(A)
            K = float(np.log(e1).sum() + np.log(e2).sum())
            Bs = np.einsum("i,ij,j->ij", e1, A, e2)
            la, lb = lam2_general(A), 1.0 - float(np.linalg.svd(Bs, compute_uv=False)[1])
            diff = lb - la
            worst_ratio_margin = max(worst_ratio_margin, abs(diff) / max(mnorm, 1e-300))
            if K > 0:
                worst_ratio_sqrtK = max(worst_ratio_sqrtK, abs(diff) / math.sqrt(2 * n * K))
            print(f"{n:>3} {spread:>7.1f} {eps:>7.0e} {mnorm:>10.3e} {K:>10.3e} "
                  f"{math.sqrt(2*n*max(K,0)):>11.3e} {la:>9.5f} {lb:>9.5f} {diff:>11.3e} "
                  f"{abs(diff)/max(mnorm,1e-300):>13.3f}")
print(f"\nworst |lambda_2(B) - lambda_2(A)| / |(u; v)|      = {worst_ratio_margin:.4f}")
print(f"worst |lambda_2(B) - lambda_2(A)| / sqrt(2 n K)  = {worst_ratio_sqrtK:.4f}")
print("The first ratio being bounded means the comparison costs the margin size, not sqrt(K).")
