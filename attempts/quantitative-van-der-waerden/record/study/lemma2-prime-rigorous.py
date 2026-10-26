"""Lemma 2' with crude but rigorous constants: which n does it close?

Proved ingredients (scratch/lemma2-prime-identity.py checks each to rounding):
  (I)  K = sum b_ij w_ij^2 psi(w_ij),  psi decreasing, psi(0) = 1/2.
  (II) (u; v) = L_B l + e,  |e|_2 <= |e|_1 <= e^delta Q,  delta = max(0, -min w).
  (A)  Q >= lambda |l|^2   (l orthogonal to (1; -1)).
  (B)  Q <= |l| (mu + |e|).
  (E)  |w|_inf <= sqrt(2) |l|,  so delta <= sqrt(2) |l| <= sqrt(2 Q / lambda).

Chain: with y = sqrt(Q),  sqrt(lambda) y <= mu + e^delta y^2, so y is at most the smaller root
of  e^delta y^2 - sqrt(lambda) y + mu = 0  (which needs lambda >= 4 e^delta mu), and then
K <= psi(-delta) y^2.  delta itself depends on y through (E), so iterate.

The application then closes n when the joint fixed point (K from Lemma 2' with lambda from the
capacity route, lambda >= 1 - sqrt(K/a)) sits below log(m_n/gamma_n).  a = 1/(2n) is proved.
"""
from mpmath import mp, mpf, exp, log, sqrt, factorial

mp.dps = 40


def consts(n):
    g = factorial(n) / mpf(n) ** n
    m = factorial(n - 2) * (mpf(n - 2) / mpf(n - 1) ** 2) ** (n - 2)
    th = 1 - 2 * sqrt(2 * g) / 3
    kap = 1 / ((1 - g) * th)
    return g, m, sqrt(2 * g * kap)          # mu = |(u; v)| bound


def psi(w):
    return mpf(1) / 2 if abs(w) < mpf(10) ** -12 else (exp(-w) - 1 + w) / w ** 2


def lemma2prime(mu, lam):
    """Crude rigorous Lemma 2': the K bound at margin mu and gap lam, or None."""
    delta = mpf(0)
    for _ in range(200):
        ed = exp(delta)
        disc = lam - 4 * ed * mu
        if disc < 0:
            return None
        y = (sqrt(lam) - sqrt(disc)) / (2 * ed)
        d_new = sqrt(2) * y / sqrt(lam)          # (E): delta <= sqrt(2 Q / lambda)
        if abs(d_new - delta) < mpf(10) ** -30:
            delta = d_new
            break
        delta = d_new
    return psi(-delta) * y ** 2


print(f"{'n':>3} {'mu':>9} {'K (Lemma 2 crude)':>18} {'K target':>12} {'closes':>7} {'margin':>8}")
for n in range(7, 16):
    g, m, mu = consts(n)
    need = log(m / g)
    a = mpf(1) / (2 * n)
    K = need                                   # start from the worst allowed K
    ok = None
    for _ in range(500):
        if K / a >= 1:
            ok = False
            break
        lam = 1 - sqrt(K / a)
        Kb = lemma2prime(mu, lam)
        if Kb is None:
            ok = False
            break
        if abs(Kb - K) < mpf(10) ** -30:
            K = Kb
            break
        K = Kb
    if ok is False:
        print(f"{n:>3} {mp.nstr(mu, 4):>9} {'bootstrap fails':>18} {mp.nstr(need, 6):>12} {'no':>7}")
        continue
    print(f"{n:>3} {mp.nstr(mu, 4):>9} {mp.nstr(K, 8):>18} {mp.nstr(need, 6):>12} "
          f"{'yes' if K < need else 'no':>7} {mp.nstr(need / K, 5):>8}")
