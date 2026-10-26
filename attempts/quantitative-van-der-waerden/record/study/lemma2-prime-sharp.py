"""Lemma 2' with the third-order error tracked exactly.

The crude chain bounded |e|_2 by e^delta Q and lost a factor of about three at n = 7.  The
quantity that actually enters is not |e| but the inner product l^T e, and that is exact:

    l^T e = sum_i l1_i e^r_i + sum_j l2_j e^c_j = sum_ij b_ij (l1_i + l2_j) eta(w_ij)
          = sum_ij b_ij w_ij eta(w_ij),        eta(w) = 1 - e^{-w} - w,

and w eta(w) = -w^3/2 + w^4/6 - ... is third order: |w eta(w)| <= e^{max(0,-w)} |w|^3 / 2.
So, with Q = sum b w^2, W = |w|_inf and delta = max(0, -min w) <= W,

    Q = l^T (u; v) - l^T e  <=  |l| mu + (e^delta W / 2) Q,
    Q (1 - e^delta W / 2)   <=  |l| mu  <=  sqrt(Q / lambda) mu,
    sqrt(Q)                 <=  mu / ( sqrt(lambda) (1 - e^delta W / 2) ),
    K                       <=  psi(-delta) Q,

with W <= sqrt(2) |l| <= sqrt(2 Q / lambda) closing the loop.  Every step is proved except the
numerical value; this prints the joint fixed point with the capacity route lambda >= 1 - sqrt(K/a).
"""
from mpmath import mp, mpf, exp, log, sqrt, factorial

mp.dps = 40


def consts(n):
    g = factorial(n) / mpf(n) ** n
    m = factorial(n - 2) * (mpf(n - 2) / mpf(n - 1) ** 2) ** (n - 2)
    th = 1 - 2 * sqrt(2 * g) / 3
    kap = 1 / ((1 - g) * th)
    return g, m, sqrt(2 * g * kap)


def psi(w):
    return mpf(1) / 2 if abs(w) < mpf(10) ** -12 else (exp(-w) - 1 + w) / w ** 2


def lemma2prime_sharp(mu, lam):
    W = mpf(0)
    for _ in range(500):
        f = 1 - exp(W) * W / 2
        if f <= 0:
            return None
        y = mu / (sqrt(lam) * f)
        W_new = sqrt(2) * y / sqrt(lam)
        if abs(W_new - W) < mpf(10) ** -30:
            W = W_new
            break
        if W_new > 5:
            return None
        W = W_new
    f = 1 - exp(W) * W / 2
    if f <= 0:
        return None
    y = mu / (sqrt(lam) * f)
    return psi(-W) * y ** 2, W


def joint(n, a):
    g, m, mu = consts(n)
    need = log(m / g)
    K = need
    for _ in range(500):
        if K / a >= 1:
            return None, need, None
        lam = 1 - sqrt(K / a)
        r = lemma2prime_sharp(mu, lam)
        if r is None:
            return None, need, None
        Kb, W = r
        if abs(Kb - K) < mpf(10) ** -30:
            return Kb, need, W
        K = Kb
    return K, need, W


print(f"{'n':>3} {'a':>8} {'K bound':>12} {'K target':>11} {'closes':>7} {'margin':>8} {'|w|_inf':>8}")
for n in (7, 8, 9):
    for name, a in (("1/(2n)", mpf(1) / (2 * n)), ("1/n", mpf(1) / n), ("0.3", mpf('0.3')),
                    ("1/2", mpf('0.5'))):
        K, need, W = joint(n, a)
        if K is None:
            print(f"{n:>3} {name:>8} {'fails':>12} {mp.nstr(need, 6):>11} {'no':>7}")
        else:
            print(f"{n:>3} {name:>8} {mp.nstr(K, 7):>12} {mp.nstr(need, 6):>11} "
                  f"{'yes' if K < need else 'no':>7} {mp.nstr(need / K, 5):>8} {mp.nstr(W, 4):>8}")
