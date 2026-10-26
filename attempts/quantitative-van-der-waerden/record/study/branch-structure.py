"""The two branches of the fixed-point inequality, and which one the argument excludes.

Theorem 2 gives lambda >= 1 - sqrt(2 n K) and Lemma 2' gives K <= Phi(lambda), decreasing in
lambda; together K <= Psi(K) := Phi(1 - sqrt(2nK)), with Psi increasing and Psi -> infinity as
K -> 1/(2n).  Psi(0) > 0, so the solution set of K <= Psi(K) is [0, K_1] union [K_2, infinity):
the first crossing K_1 excludes the branch of small scaling cost, but every K >= K_2 satisfies
the inequality trivially.  A counterexample needs K >= log(m_n/gamma_n); the argument closes only
if BOTH branches lie below that, i.e. if K_2 < log(m_n/gamma_n) as well, which never happens.
"""
from mpmath import mp, mpf, exp, log, sqrt, factorial

mp.dps = 30


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


def Phi(mu, lam):
    W = mpf(0)
    for _ in range(300):
        Wn = sqrt(2) * mu / (lam * chi(W))
        if Wn > 5:
            return None
        if abs(Wn - W) < mpf(10) ** -25:
            W = Wn
            break
        W = Wn
    return max(psi(W) / chi(W), psi(-W) / chi(-W)) * mu ** 2 / (lam * chi(W))


print(f"{'n':>3} {'need=log(m/g)':>14} {'K_1':>10} {'K_2':>10} {'pole 1/(2n)':>12} {'small-K branch':>15} {'large-K branch':>15}")
for n in range(7, 16):
    g, m, mu = consts(n)
    need = log(m / g)
    pole = mpf(1) / (2 * n)
    # scan K on (0, pole) for sign changes of Psi(K) - K
    grid = [pole * mpf(i) / 4000 for i in range(1, 4000)]
    vals = []
    for K in grid:
        lam = 1 - sqrt(2 * n * K)
        P = Phi(mu, lam)
        vals.append(None if P is None else P - K)
    cross = [grid[i] for i in range(1, len(grid)) if vals[i - 1] is not None and vals[i] is not None
             and (vals[i - 1] > 0) != (vals[i] > 0)]
    K1 = cross[0] if cross else None
    K2 = cross[1] if len(cross) > 1 else None
    s1 = "excluded" if (K1 is not None and K1 < need) else "not excluded"
    s2 = "excluded" if (K2 is not None and K2 < need) else "NOT excluded"
    print(f"{n:>3} {mp.nstr(need, 6):>14} {mp.nstr(K1, 6) if K1 else '-':>10} "
          f"{mp.nstr(K2, 6) if K2 else '-':>10} {mp.nstr(pole, 6):>12} {s1:>15} {s2:>15}")
print("\nThe large-K branch is the near-decomposable case: lambda_2(B) <= 1 - sqrt(2 n K_2).")
