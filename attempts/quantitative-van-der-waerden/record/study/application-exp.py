"""The Dittert deduction with the exponential form, at high precision.

The capacity route proves  per(B) >= gamma_n exp(||E||_F^2 / (2n)),  E = B - J_n/n.
Combined with per(B) <= e^K gamma_n (K = -log cap(A)) that gives  ||E||_F^2 <= 2 n K,
hence lambda_2(B) >= 1 - sqrt(2 n K), and Theorem R's Lemma 2 gives the fixed point

    K = gamma_n kappa_n / ( theta_n (1 - sqrt(2 n K)) ).

The case closes when the least solution is below log(m_n / gamma_n).  The margin at n = 7 is
thin, so everything here is done with 60-digit arithmetic and the sensitivity is reported: the
last column is the factor by which the right-hand side of Lemma 2 could grow before n = 7 stops
closing.  That is the room left for the two obligations of study/application.md, in particular
the comparison between lambda_2(A) and lambda_2(B).
"""
import sys

from mpmath import mp, mpf, exp, log, sqrt, factorial

mp.dps = 60


def constants(n):
    g = factorial(n) / mpf(n) ** n
    m = factorial(n - 2) * (mpf(n - 2) / mpf(n - 1) ** 2) ** (n - 2)
    th = 1 - 2 * sqrt(2 * g) / 3
    kap = 1 / ((1 - g) * th)
    return g, m, th, kap


def least_fixed_point(n, slack=mpf(1)):
    g, m, th, kap = constants(n)
    rhs = slack * g * kap / th          # the numerator of Lemma 2 after |u|^2+|v|^2 <= 2 g kappa
    K = rhs
    for _ in range(2000):
        arg = 2 * n * K
        if arg >= 1:
            return None
        lam = 1 - sqrt(arg)
        Kn = rhs / lam
        if abs(Kn - K) < mpf(10) ** -50:
            K = Kn
            break
        K = Kn
    if 2 * n * K >= 1:
        return None
    return K


print(f"{'n':>3} {'K least fixed point':>22} {'log(m_n/gamma_n)':>22} {'closes':>7} {'margin':>9} "
      f"{'slack tolerated':>16}")
for n in range(6, 16):
    g, m, th, kap = constants(n)
    need = log(m / g)
    K = least_fixed_point(n)
    if K is None:
        print(f"{n:>3} {'no fixed point':>22} {mp.nstr(need, 8):>22} {'no':>7}")
        continue
    ok = K < need
    # how much extra the Lemma 2 numerator could carry before this n stops closing
    lo, hi = mpf(1), mpf(50)
    for _ in range(200):
        mid = (lo + hi) / 2
        Km = least_fixed_point(n, mid)
        if Km is not None and Km < need:
            lo = mid
        else:
            hi = mid
    print(f"{n:>3} {mp.nstr(K, 10):>22} {mp.nstr(need, 10):>22} {'yes' if ok else 'no':>7} "
          f"{mp.nstr(need / K, 6):>9} {mp.nstr(lo, 6):>16}")
print("\nThe last column is the factor the Lemma 2 numerator may grow by and still close that n.")
