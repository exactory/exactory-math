"""Lemma 2' at its sharpest: two exact weighted sums and one ratio.

Besides K = sum b w^2 psi(w) (identity I), the inner product of the potentials with the margins
is also an exact weighted sum, from identity II:

    l^T (u; v) = sum_ij b_ij w_ij (1 - e^{-w_ij}) = sum_ij b_ij w_ij^2 chi(w_ij),
    chi(w) = (1 - e^{-w}) / w,   chi(0) = 1,  chi decreasing.

So K / l^T(u; v) <= max rho(w) over the support, rho = psi / chi, and rho is nearly flat:
rho(w) = 1/2 + w/12 + O(w^2).  The chain becomes

    K   <= rho_max * l^T (u; v) <= rho_max |l| mu,
    Q   <= l^T (u; v) / chi(W+) <= |l| mu / chi(W+)          (W+ = max w on the support),
    |l| <= Q / (lambda |l|) <= mu / (lambda chi(W+)),
    K   <= rho_max mu^2 / (lambda chi(W+)),

with W <= sqrt(2) |l| <= sqrt(2) mu / (lambda chi(W)) closing the loop.  Compared with the
previous chain, the third-order loss enters once and linearly instead of squared.
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


def chi(w):
    return mpf(1) if abs(w) < mpf(10) ** -12 else (1 - exp(-w)) / w


def rho_max(W):
    """max of psi/chi on [-W, W]; rho is increasing so it is at +W (checked below)."""
    return max(psi(W) / chi(W), psi(-W) / chi(-W))


def lemma(mu, lam):
    W = mpf(0)
    for _ in range(500):
        c = chi(W)
        ell = mu / (lam * c)
        W_new = sqrt(2) * ell
        if abs(W_new - W) < mpf(10) ** -30:
            W = W_new
            break
        if W_new > 5:
            return None
        W = W_new
    ell = mu / (lam * chi(W))
    return rho_max(W) * ell * mu, W


def joint(n, a):
    g, m, mu = consts(n)
    need = log(m / g)
    K = need
    for _ in range(500):
        if K / a >= 1:
            return None, need, None
        lam = 1 - sqrt(K / a)
        r = lemma(mu, lam)
        if r is None:
            return None, need, None
        Kb, W = r
        if abs(Kb - K) < mpf(10) ** -30:
            return Kb, need, W
        K = Kb
    return K, need, W


# sanity: rho increasing on [-1, 1]?
vals = [psi(mpf(x) / 20) / chi(mpf(x) / 20) for x in range(-20, 21)]
print("rho(w) on [-1,1] increasing:", all(vals[i] <= vals[i + 1] for i in range(len(vals) - 1)),
      " rho(-0.25) =", mp.nstr(psi(mpf('-0.25')) / chi(mpf('-0.25')), 5),
      " rho(0.25) =", mp.nstr(psi(mpf('0.25')) / chi(mpf('0.25')), 5))
print(f"\n{'n':>3} {'a':>8} {'K bound':>12} {'K target':>11} {'closes':>7} {'margin':>8} {'W':>7}")
for n in (7, 8):
    for name, a in (("1/(2n)", mpf(1) / (2 * n)), ("1/n", mpf(1) / n), ("0.2", mpf('0.2')),
                    ("0.3", mpf('0.3')), ("1/2", mpf('0.5'))):
        K, need, W = joint(n, a)
        if K is None:
            print(f"{n:>3} {name:>8} {'fails':>12} {mp.nstr(need, 6):>11} {'no':>7}")
        else:
            print(f"{n:>3} {name:>8} {mp.nstr(K, 7):>12} {mp.nstr(need, 6):>11} "
                  f"{'yes' if K < need else 'no':>7} {mp.nstr(need / K, 5):>8} {mp.nstr(W, 4):>7}")
