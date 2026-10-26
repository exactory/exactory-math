"""What the quantitative van der Waerden inequality would give Dittert's conjecture.

Write gamma_n = n!/n^n, m_n = (n-2)!((n-2)/(n-1)^2)^(n-2), h_n = sqrt(2 gamma_n),
theta_n = 1 - 2 h_n / 3 and kappa_n = 1/((1 - gamma_n) theta_n), the constants of Theorem R
(attack/dittert-conjecture-n5-to-n15/study/route-a-reduction-theorem.md).

Suppose A in K_n has a zero entry and phi(A) >= 2 - gamma_n.  Let B be its Sinkhorn scaling and
K = -log cap(A), so per(A) = e^{-K} per(B).  The record already gives four facts.

  (a) |u|^2 + |v|^2 <= 2 gamma_n kappa_n           (Theorem R, Lemma 3(a))
  (b) per(A) <= gamma_n                            (from phi(A) >= 2 - gamma_n and AM-GM)
  (c) per(B) >= m_n                                (Knopp-Sinkhorn: B has a zero)
  (d) K <= (|u|^2 + |v|^2) / (2 theta_n lambda_2)  (Theorem R, Lemma 2, given condition (N))

From (b) and (c), K >= log(m_n / gamma_n): the scaling has to be expensive.  The claim supplies
the opposite.  From (b), per(B) = e^K per(A) <= e^K gamma_n, and the claim gives

    ||B - J_n/n||_F^2 <= (e^K - 1) / c,      c = 1/4,

and since B = J_n/n + E with E 1 = 0 and E^T 1 = 0, the second singular value of B is at most
||E||_F, so lambda_2(B) >= 1 - sqrt((e^K - 1)/c).  Feeding that back into (d) gives a fixed point

    K = gamma_n kappa_n / (theta_n (1 - sqrt((e^K - 1)/c))),

whose least solution is an upper bound on K.  The case closes at n when that bound is below
log(m_n / gamma_n).

Two steps are approximations that a proof has to make exact and this script marks as such:
lambda_2(A) is used in (d) while the claim bounds lambda_2(B), and the fixed point needs a
continuity argument to select the least solution.  Both are recorded as obligations.

Condition (N) of Theorem R's Lemma 2 is the reason the old route needed a large lambda_2.  Here
it is free: the competitor is B'_ij = a_ij (1 + alpha_i + beta_j) and Lemma 3(c) bounds
|alpha_i + beta_j| by sqrt(2) |(u; v)| / (theta_n lambda_2), which the script prints; as long as
that stays below 1 the competitor is non-negative.
"""
import math
import sys


def constants(n):
    g = math.factorial(n) / n ** n
    m = math.factorial(n - 2) * ((n - 2) / (n - 1) ** 2) ** (n - 2)
    h = math.sqrt(2 * g)
    th = 1 - 2 * h / 3
    kap = 1 / ((1 - g) * th)
    return g, m, th, kap


def fixed_point(n, c, iters=400):
    g, m, th, kap = constants(n)
    K = g * kap / th
    for _ in range(iters):
        d2 = (math.exp(K) - 1) / c
        if d2 >= 1.0:
            return None, None            # the spectral bound is vacuous
        lam = 1 - math.sqrt(d2)
        K_new = g * kap / (th * lam)
        if abs(K_new - K) < 1e-15:
            K = K_new
            break
        K = K_new
    d2 = (math.exp(K) - 1) / c
    lam = 1 - math.sqrt(d2)
    return K, lam


c = float(sys.argv[1]) if len(sys.argv) > 1 else 0.25
print(f"c = {c}\n")
print(f"{'n':>3} {'K upper bound':>15} {'lambda_2 >=':>12} {'log(m_n/gamma_n)':>17} "
      f"{'closes':>8} {'margin':>8} {'|alpha+beta| <=':>16}")
for n in range(5, 21):
    g, m, th, kap = constants(n)
    need = math.log(m / g)
    K, lam = fixed_point(n, c)
    if K is None:
        print(f"{n:>3} {'no fixed point':>15} {'-':>12} {need:>17.6e} {'no':>8}")
        continue
    ab = math.sqrt(2) * math.sqrt(2 * g * kap) / (th * lam)
    ok = K < need
    print(f"{n:>3} {K:>15.6e} {lam:>12.6f} {need:>17.6e} {'yes' if ok else 'no':>8} "
          f"{need / K:>8.2f}x {ab:>16.4f}")
print("\nA row that closes needs K below log(m_n/gamma_n), and needs |alpha+beta| below 1 for")
print("condition (N).  n = 5 and n = 6 are already proved by exact sum-of-squares certificates.")
