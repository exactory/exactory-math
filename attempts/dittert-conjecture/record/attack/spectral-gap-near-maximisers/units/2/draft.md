# Dittert's conjecture as a bound on the cost of Sinkhorn scaling

**Form.** Reduction or equivalence. **Venue.** On the path: it is the cleanest restatement the
problem took in either attack, and it removes the permanent, the spectrum and the simplex from
the hypothesis.

## 1. The reduction

Write `K_n` for the non-negative `n x n` matrices of total sum `n`, `gamma_n = n!/n^n`,
`m_n = (n-2)! ((n-2)/(n-1)^2)^{n-2}` for the Knopp-Sinkhorn minimum of the permanent over the
doubly stochastic matrices with a zero, and

    cap(A) = inf_{z > 0} prod_i (Az)_i / prod_j z_j

for the capacity. For `A in K_n` put `u = 1 - r` and `v = 1 - c` for the margin deviations.

**H(n, K).** *Every fully indecomposable `A in K_n` satisfies*
`-log cap(A) <= K (|u|^2 + |v|^2)`.

**Theorem.** `H(n, K)` implies Dittert's conjecture at `n` whenever

    K < K_max(n) := log(m_n / gamma_n) / (2 gamma_n kappa_n),
    kappa_n = 1 / ((1 - gamma_n)(1 - 2 sqrt(2 gamma_n) / 3)).

*Proof sketch.* Suppose `phi(A) = 2 - gamma_n + delta` with `delta > 0` at some `A in K_n` with a
zero entry. Lemma 3(a) of Theorem R gives `|u|^2 + |v|^2 <= 2 delta kappa_n`, and
`delta <= gamma_n`. The Sinkhorn scaling `B` of `A` is doubly stochastic with the same support,
so it has a zero and `per(B) >= m_n` by Knopp-Sinkhorn; and `per(A) = cap(A) per(B)`. The
hypothesis `phi(A) >= 2 - gamma_n` forces `per(A) <= gamma_n`, so
`-log cap(A) >= log(m_n / gamma_n)`. Against `H(n, K)` this needs
`log(m_n / gamma_n) <= 2 K gamma_n kappa_n`, which fails when `K < K_max(n)`. QED

Theorem R is the special case `K = 1 / (2 theta_n lambda_2(A))` with
`theta_n = 1 - 2 sqrt(2 gamma_n)/3`, so `H` is the spectral statement with the spectrum removed
from the wording.

## 2. The thresholds

`study/conditional-K.py` computes `K_max(n)` exactly.

| n | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `K_max(n)` | 0.179 | 0.301 | 0.536 | 1.00 | 1.94 | 3.91 | 8.09 | 17.2 | 37.2 | 82.0 | 184 | 417 | 2.9e4 |

So `K < 1` already settles every `n >= 7`, `K < 8` settles `n >= 10`, `K < 400` settles `n >= 15`.
Measured against the truth, the sibling attack's capacity samples give `K` about 0.5, so the
hypothesis has a factor of two of room at `n = 7`, the hardest open dimension, and orders of
magnitude above it.

## 3. Why a uniform K is false

**Proposition.** For no finite `K` does `H(n, K)` hold over all fully indecomposable `A in K_n`.

*Proof.* Let `B` be block diagonal with two doubly stochastic blocks of sizes `k` and `n - k`.
Scale the rows of the first block by `e^t` and its columns by `e^{-t}`. The result stays in
`K_n` to first order after renormalisation, and its margins vanish to first order in `t`: the
linear map from the perturbation to `(u; v)` has a kernel of dimension equal to the number of
blocks. On that kernel the second-order scaling cost is `sum_b k_b t_b^2 > 0`. So the ratio
`-log cap / (|u|^2 + |v|^2)` is unbounded, and `K = infinity` for a decomposable `A` and
arbitrarily large for a nearly decomposable one. QED

The proposition is not a defeat of the reduction: it names the restriction the hypothesis needs.
`H(n, K)` has to be asserted only for matrices that are not nearly decomposable, and what must
supply that restriction is the other hypothesis in play, `per(A) <= gamma_n`. Supplying it is the
barrier of unit 5.

## 4. The dichotomy this leaves

Either `cap(A) >= gamma_n / m_n`, in which case `per(A) >= cap(A) m_n >= gamma_n` contradicts
`per(A) = gamma_n - delta` with `delta > 0` and the case is closed; or

    -log cap(A) > log(m_n / gamma_n) ~ 1 / (2(n-1)^2),

which says `A` is a definite distance from doubly stochastic. In that branch a lower bound on
`per(A)` has to take over, and it must be strong exactly where `cap(A)` is small. Every bound in
the record degrades there.

## 5. References

- Knopp and Sinkhorn, *Minimum permanents of doubly stochastic matrices with at least one zero
  entry*, Linear and Multilinear Algebra 11 (1982) 351-355.
- Egorychev 1981 and Falikman 1981 for `per(B) >= gamma_n`.
- Gurvits and Leake, *Counting Matchings via Capacity Preserving Operators*, arXiv:1804.04351, for
  capacity as a tool for permanent lower bounds.
- Theorem R and its Lemma 3(a):
  `attack/dittert-conjecture-n5-to-n15/study/route-a-reduction-theorem.md`.

## 6. Ledger

Obligations: `H(n, K)` itself, in the restricted form section 3 forces. What its proof needs is
the second-order behaviour of the Sinkhorn fixed point without a spectral gap, or a convexity
argument on the scaling functional that avoids its Hessian.
