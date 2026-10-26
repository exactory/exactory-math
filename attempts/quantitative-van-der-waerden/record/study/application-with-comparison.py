"""The deduction again, this time paying for the step it was skipping.

Theorem R's Lemma 2 bounds K by the energy of A's own weighted bipartite Laplacian, so the
spectral quantity it needs is lambda_2(A), while the capacity route bounds lambda_2(B) for the
Sinkhorn scaling B.  The two differ, and the difference is not small: K = KL(B || A) and both
matrices have total mass n, so Pinsker gives

    ||A - B||_1 <= sqrt(2 n K),        hence   ||A - B||_F <= sqrt(2 n K),

and Weyl gives  lambda_2(A) >= lambda_2(B) - ||L_A - L_B||_2 >= lambda_2(B) - c_L sqrt(2 n K),
with c_L a constant of order 1 from the Laplacian's dependence on the entries and the margins.
This runs the fixed point with

    lambda_2 >= 1 - sqrt(K / a) - c_L sqrt(2 n K),

for the proved a = 1/(2n) and for the values a a better lemma might give, and for c_L in
{0, 1, 2}.  c_L = 0 is the calculation that skips the comparison; it is what application.md
records as obligation 1 and what this script is here to price.
"""
from mpmath import mp, mpf, log, sqrt, factorial

mp.dps = 50


def constants(n):
    g = factorial(n) / mpf(n) ** n
    m = factorial(n - 2) * (mpf(n - 2) / mpf(n - 1) ** 2) ** (n - 2)
    th = 1 - 2 * sqrt(2 * g) / 3
    return g, m, th, 1 / ((1 - g) * th)


def fp(n, a, cL):
    g, m, th, kap = constants(n)
    rhs = g * kap / th
    K = rhs
    for _ in range(5000):
        lam = 1 - sqrt(K / a) - cL * sqrt(2 * n * K)
        if lam <= 0:
            return None
        Kn = rhs / lam
        if abs(Kn - K) < mpf(10) ** -40:
            return Kn
        K = Kn
    return None


for cL in (0, 0.03, 0.1, 0.25, 0.5):
    print(f"\n=== c_L = {cL} " + ("(comparison skipped)" if cL == 0 else "(measured worst case 0.030)"))
    print(f"{'n':>3} " + "".join(f"{lab:>16}" for lab in
                                 ("a=1/(2n) proved", "a=1/n", "a=2/n", "a=1/4")))
    for n in range(7, 16):
        g, m, th, kap = constants(n)
        need = log(m / g)
        cells = []
        for a in (mpf(1) / (2 * n), mpf(1) / n, mpf(2) / n, mpf(1) / 4):
            K = fp(n, a, cL)
            cells.append("no" if K is None or K >= need else mp.nstr(need / K, 4) + "x")
        print(f"{n:>3} " + "".join(f"{c:>16}" for c in cells))
print("\nA cell shows the margin (need/K) when the case closes, and 'no' when it does not.")
