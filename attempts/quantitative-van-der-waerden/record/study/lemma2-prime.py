"""Can Theorem R's Lemma 2 be stated with the scaling's own spectral gap?

Lemma 2 bounds the scaling cost K = -log cap(A) by (|u|^2 + |v|^2) / (2 theta_n lambda_2(A)),
where lambda_2(A) is the gap of A's normalised bipartite Laplacian and theta_n absorbs the third
order.  The capacity route bounds lambda_2(B) for the Sinkhorn scaling B instead, so the
application has to compare the two gaps (obligation 1 of study/application.md).

The comparison disappears if Lemma 2 holds with lambda_2(B) in place of lambda_2(A).  There is
a reason to expect it to: with log-scalings (l1, l2), the exact identity K = sum l1 + sum l2 and
the margin equations expand to second order as (u; v) = L_B (l1; l2) + O(l^2), with L_B the
Laplacian of B, so K = (1/2)(u; v)^T L_B^+ (u; v) + O(l^3).  This script measures

    R(A) = 2 lambda_2(B) K / (|u|^2 + |v|^2),

over near-doubly-stochastic A with a zero entry, at the margin sizes of the application
(|(u; v)| <= sqrt(2 gamma_n kappa_n), which is 0.111 at n = 7) and also at larger margins, and
with B chosen to have a small spectral gap on purpose.  R <= 1 everywhere is Lemma 2' with
theta = 1; the worst R found is the theta the lemma would need.
"""
import math
import sys

import numpy as np


def sinkhorn_factors(X, iters=400000, tol=1e-15):
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


rng = np.random.default_rng(7)
print(f"{'n':>3} {'lam2(B) range':>16} {'|(u;v)| range':>16} {'cases':>6} {'worst R':>9} "
      f"{'worst R at small gap':>21}")
overall = 0.0
for n in [int(a) for a in sys.argv[1:]] or [5, 7, 8, 10]:
    g = math.factorial(n) / n ** n
    mmax = math.sqrt(2 * g / ((1 - g) * (1 - 2 * math.sqrt(2 * g) / 3)))
    worst, worst_small, cnt = 0.0, 0.0, 0
    lams, ms = [], []
    for trial in range(600):
        spread = rng.choice([0.3, 1.0, 2.0, 3.5])
        X = np.exp(spread * rng.standard_normal((n, n)))
        X[0, 0] = 0.0
        if trial % 3 == 2:                      # push B toward a block structure: small gap
            k = rng.integers(1, n // 2 + 1)
            t = rng.choice([0.02, 0.05, 0.1, 0.2])
            X[:k, k:] *= t
            X[k:, :k] *= t
        d1, d2 = sinkhorn_factors(X)
        B = np.einsum("i,ij,j->ij", d1, X, d2)
        lamB = 1.0 - float(np.linalg.svd(B, compute_uv=False)[1])
        eps = rng.choice([0.3, 1.0, 3.0]) * mmax / math.sqrt(2 * n)
        A = np.einsum("i,ij,j->ij", np.exp(eps * rng.standard_normal(n)), B,
                      np.exp(eps * rng.standard_normal(n)))
        A *= n / A.sum()
        u, v = 1 - A.sum(1), 1 - A.sum(0)
        m2 = float(u @ u + v @ v)
        e1, e2 = sinkhorn_factors(A)
        K = float(np.log(e1).sum() + np.log(e2).sum())
        if K <= 0 or m2 <= 0:
            continue
        Rv = 2 * lamB * K / m2
        cnt += 1
        worst = max(worst, Rv)
        if lamB < 0.3:
            worst_small = max(worst_small, Rv)
        lams.append(lamB); ms.append(math.sqrt(m2))
    overall = max(overall, worst)
    print(f"{n:>3} {min(lams):>7.3f}..{max(lams):<7.3f} {min(ms):>7.4f}..{max(ms):<7.4f} {cnt:>6} "
          f"{worst:>9.4f} {worst_small:>21.4f}")
print(f"\nworst R over everything: {overall:.4f}   (R <= 1 is Lemma 2' with theta = 1)")
