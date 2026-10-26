"""How good a constant does n = 7 need?

The capacity route gives per(B) >= gamma_n exp(a ||E||_F^2) with a = 1/(2n).  Then
||E||_F^2 <= K/a and lambda_2(B) >= 1 - sqrt(K/a), and Theorem R's Lemma 2 closes n when the
least solution of  K = gamma_n kappa_n / (theta_n (1 - sqrt(K/a)))  is below log(m_n/gamma_n).

At a = 1/(2n) the margin at n = 7 is 1.085, and only a factor 1.053 of slack is left for the two
obligations of study/application.md.  This measures what a better a buys.
"""
from mpmath import mp, mpf, log, sqrt, factorial

mp.dps = 50


def constants(n):
    g = factorial(n) / mpf(n) ** n
    m = factorial(n - 2) * (mpf(n - 2) / mpf(n - 1) ** 2) ** (n - 2)
    th = 1 - 2 * sqrt(2 * g) / 3
    return g, m, th, 1 / ((1 - g) * th)


def fp(n, a, slack=mpf(1)):
    g, m, th, kap = constants(n)
    rhs = slack * g * kap / th
    K = rhs
    for _ in range(3000):
        if K / a >= 1:
            return None
        Kn = rhs / (1 - sqrt(K / a))
        if abs(Kn - K) < mpf(10) ** -40:
            return Kn
        K = Kn
    return K if K / a < 1 else None


print(f"{'a (the constant in the exponent)':>34} {'n=7 margin':>12} {'slack tolerated':>16}")
for name, a in (("1/(2n) = 1/14, proved", mpf(1) / 14), ("1/n = 1/7", mpf(1) / 7),
                ("1.1/n", mpf('1.1') / 7), ("1.5/n", mpf('1.5') / 7),
                ("2/n = 2/7", mpf(2) / 7), ("1/4, the truth", mpf(1) / 4),
                ("1/2, the limit", mpf(1) / 2)):
    g, m, th, kap = constants(7)
    need = log(m / g)
    K = fp(7, a)
    if K is None or K >= need:
        print(f"{name:>34} {'does not close':>12}")
        continue
    lo, hi = mpf(1), mpf(100)
    for _ in range(200):
        mid = (lo + hi) / 2
        Km = fp(7, a, mid)
        lo, hi = (mid, hi) if (Km is not None and Km < need) else (lo, mid)
    print(f"{name:>34} {mp.nstr(need / K, 6):>12} {mp.nstr(lo, 6):>16}")
