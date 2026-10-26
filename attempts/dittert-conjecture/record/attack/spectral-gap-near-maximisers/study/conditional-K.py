"""The cleanest conditional form: how expensive may Sinkhorn scaling be?

Every proof of Dittert's conjecture, and Theorem R, is an upper bound on the same scalar,
`-log cap(A)`, against the lower bound `log(m_n/(gamma_n - delta))` that Knopp-Sinkhorn
forces.  Write the hypothesis in its most ordinary form:

  H(n, K): for every fully indecomposable A in K_n with row and column margins
           u = 1 - r and v = 1 - c,      -log cap(A) <= K (|u|^2 + |v|^2).

That is: the cost of Sinkhorn scaling is at most `K` times the squared margins.  It is the
statement Theorem R proves with `K = 1/(2 theta_n lambda_2(A))`, so `H(n, K)` with a bounded
`K` is the spectral gap statement with the spectrum removed from the wording.

With `|u|^2 + |v|^2 <= 2 delta kappa_n` (Theorem R Lemma 3(a)) and `delta <= gamma_n`, the
contradiction closes at `n` as soon as

  2 K gamma_n kappa_n < log( m_n / gamma_n ),      i.e.   K < K_max(n).

This script prints `K_max(n)`.  It is the number a proof of H has to beat, and it says which
dimensions need a sharp constant and which only need a crude one.
"""
import math

print(f"{'n':>3} {'gamma_n':>11} {'log(m_n/gamma_n)':>17} {'K_max(n)':>12}")
for n in range(4, 21):
    g = math.factorial(n) / n ** n
    m = math.factorial(n - 2) * ((n - 2) / (n - 1) ** 2) ** (n - 2)
    h = math.sqrt(2 * g)
    kap = 1 / ((1 - g) * (1 - 2 * h / 3))
    lg = math.log(m / g)
    kmax = lg / (2 * g * kap)
    print(f"{n:>3} {g:>11.4e} {lg:>17.6e} {kmax:>12.4g}")
print("\nK_max is what a proof of H(n, K) must beat.  Theorem R proves H with")
print("K = 1/(2 theta_n lambda_2), so K = O(1) is the spectral gap statement.")
