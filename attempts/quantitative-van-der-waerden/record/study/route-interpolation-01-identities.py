"""Check the identities used by the interpolation route.

B = J/n + E doubly stochastic, F = nE (entries >= -1, zero row and column sums), and

    f(t) = per(J/n + tE) = gamma_n * sum_k r_k(F) t^k / (n)_k          (Taylor form)
         = gamma_n * sum_k C(n,k) q_k t^k (1-t)^(n-k)                    (Bernstein form)

with r_k the k-matching sum of F, (n)_k = n!/(n-k)!, and q_k = Sigma_k(B)/Sigma_k(J/n) the
normalised sum of k x k subpermanents.  Checked here:

  (1) the two expansions agree with a direct permanent evaluation;
  (2) r_3(F) = (2/3) sum_ij F_ij^3;
  (3) 24 r_4(F) = 36 p_4 - 18 (sum_i R_i^2 + sum_j C_j^2) + 3 ||F||^4 + 6 ||F F^T||_F^2,
      R_i, C_j the row and column sums of F o F (entrywise square);
  (4) q_2 - 1 = ||E||_F^2 / (n-1)^2;
  (5) the Bernstein step identity  (k+1) Sigma_{k+1}(B) = sum_{S,T} per(B[S,T]) (n - 2k + B(S,T)).
"""
import itertools
import math

import numpy as np

rng = np.random.default_rng(1)


def permanent(A):
    n = A.shape[0]
    if n == 0:
        return 1.0
    return sum(math.prod(A[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n)))


def sinkhorn(X, iters=50000, tol=1e-15):
    d1, d2 = np.ones(X.shape[0]), np.ones(X.shape[0])
    for _ in range(iters):
        d1 = 1.0 / (X @ d2)
        d2 = 1.0 / (X.T @ d1)
        B = d1[:, None] * X * d2[None, :]
        if abs(B.sum(0) - 1).max() < tol and abs(B.sum(1) - 1).max() < tol:
            break
    return B


def random_ds(n, kind):
    if kind == "sinkhorn":
        return sinkhorn(rng.random((n, n)) ** 3)
    if kind == "perm-mix":
        k = rng.integers(2, 4)
        B = np.zeros((n, n))
        w = rng.dirichlet(np.ones(k))
        for a in range(k):
            B[np.arange(n), rng.permutation(n)] += w[a]
        return B
    raise ValueError(kind)


def subperm_sum(B, k):
    n = B.shape[0]
    return sum(permanent(B[np.ix_(S, T)])
               for S in itertools.combinations(range(n), k)
               for T in itertools.combinations(range(n), k))


def matching_sum(F, k):
    n = F.shape[0]
    return sum(permanent(F[np.ix_(S, T)])
               for S in itertools.combinations(range(n), k)
               for T in itertools.combinations(range(n), k))


def falling(n, k):
    return math.perm(n, k)


worst = {}
for n in (3, 4, 5):
    gamma = math.factorial(n) / n ** n
    for kind in ("sinkhorn", "perm-mix"):
        for trial in range(4):
            B = random_ds(n, kind)
            E = B - 1.0 / n
            F = n * E
            r = [matching_sum(F, k) for k in range(n + 1)]
            Sig = [subperm_sum(B, k) for k in range(n + 1)]
            SigJ = [math.comb(n, k) ** 2 * math.factorial(k) / n ** k for k in range(n + 1)]
            q = [Sig[k] / SigJ[k] for k in range(n + 1)]
            for t in (0.3, 0.7, 1.0):
                direct = permanent(1.0 / n + t * E)
                taylor = gamma * sum(r[k] * t ** k / falling(n, k) for k in range(n + 1))
                bern = gamma * sum(math.comb(n, k) * q[k] * t ** k * (1 - t) ** (n - k)
                                   for k in range(n + 1))
                worst["(1) taylor"] = max(worst.get("(1) taylor", 0), abs(direct - taylor))
                worst["(1) bernstein"] = max(worst.get("(1) bernstein", 0), abs(direct - bern))
            p3 = (F ** 3).sum()
            worst["(2) r3"] = max(worst.get("(2) r3", 0), abs(r[3] - 2.0 / 3.0 * p3))
            if n >= 4:
                G = F ** 2
                p4 = (F ** 4).sum()
                R = G.sum(1)
                C = G.sum(0)
                rhs = (36 * p4 - 18 * ((R ** 2).sum() + (C ** 2).sum())
                       + 3 * G.sum() ** 2 + 6 * ((F @ F.T) ** 2).sum()) / 24
                worst["(3) r4"] = max(worst.get("(3) r4", 0), abs(r[4] - rhs))
            worst["(4) q2"] = max(worst.get("(4) q2", 0),
                                  abs(q[2] - 1 - (E ** 2).sum() / (n - 1) ** 2))
            for k in range(1, n):
                lhs = (k + 1) * Sig[k + 1]
                rhs = sum(permanent(B[np.ix_(S, T)]) * (n - 2 * k + B[np.ix_(S, T)].sum())
                          for S in itertools.combinations(range(n), k)
                          for T in itertools.combinations(range(n), k))
                worst["(5) step"] = max(worst.get("(5) step", 0), abs(lhs - rhs))

for key in sorted(worst):
    print(f"{key:15s} max abs discrepancy {worst[key]:.2e}")
