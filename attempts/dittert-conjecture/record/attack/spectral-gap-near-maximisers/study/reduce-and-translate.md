# Strategy study: reduce-and-translate

Written 2026-09-03 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| arXiv | the five queries of `novelty.md` (stability of van der Waerden; permanent and spectral gap; capacity and singular values) | 2026-09-03 | only arXiv:1804.04351 (Gurvits-Leake) and the three 2026 Dittert preprints |
| zbMATH | `permanent doubly stochastic stability` | 2026-09-03 | one record, Egorychev 1981 |
| local | `study/route-a-reduction-theorem.md` of the sibling attack | 2026-09-03 | the translation already performed: spectral gap -> capacity -> entropy |
| local | `study/binding-constraint.py`, `study/r1-threshold.py` (written and run here) | 2026-09-03 | which bar each route must clear, below |

## 2. Hits worth reading

- arXiv:1804.04351 (Gurvits-Leake), abstract: the capacity method translates permanent
  inequalities into inequalities about real stable polynomials; that is the target language
  of the next translation, and its equality cases are the missing input.
- Cheon-Wanless 2012, Thms 2.1, 3.2 (full text, fetched by the sibling attack): the only
  quantitative facts about a near-maximiser that exist, both in the language of subset sums.
- Theorem R (`study/route-a-reduction-theorem.md`, sibling attack, full text): the
  translation chain that already worked, spectral gap -> capacity via Sinkhorn scaling ->
  entropy via the Jensen bound `cap(A) >= exp(sum b log(a/b))`.

## 3. What was learned, as constraints on the plan

1. **The languages available.** Four: the permanent itself; the capacity
   `cap(A) = inf prod (Az)_i / prod z_j`; the relative entropy, since
   `-log cap(A) = min over B in Omega_n with supp B contained in supp A of KL(B || A)`;
   and the spectrum of the normalised matrix. Theorem R is the chain
   spectrum -> entropy -> capacity -> permanent. A further translation has to leave the
   permanent language, and the only destination with a body of theory is real stable
   (or Lorentzian) polynomials.
2. **The one scalar everything reduces to.** With `B` the Sinkhorn scaling of `A`,
   `per(A) = cap(A) per(B)` and `per(B) >= m_n`, so the conjecture at `n` is exactly
   `-log cap(A) < log(m_n/(gamma_n - delta))` for every admissible `A`. Every published
   proof is an upper bound on `-log cap(A)`, and so is Theorem R. This is recorded in
   `study/routes-rubric.md` as the standing reduction.
3. **The binding constraint is technical, not mathematical** (`study/binding-constraint.py`,
   run 2026-09-03). Theorem R needs the gap to clear two bars: the nonnegativity condition
   (N) of its Lemma 2, which needs `lambda_2 >= c_N = 2 sqrt(gamma_n kappa_n)/theta_n`, and
   the final contradiction, which needs only `lambda_2 > c_C = 2 m_n kappa_n/theta_n`. The
   ratio `c_N/c_C = 1/sqrt(gamma_n kappa_n)` is 12 at `n = 7`, 52 at `n = 10`, 577 at
   `n = 15` and 6556 at `n = 20`. The reason is structural: the margins `u = 1 - r` have
   size `sqrt(delta)`, so the linear correction `alpha` has size `sqrt(delta)/lambda_2` and
   staying nonnegative costs a square root, while the contradiction is linear in `delta`.
4. **What that buys.** Against the contradiction bar alone, the crude Cheeger-and-blocks
   chain (`lambda_2 >= 1/(2n^4)`) settles `n >= 15`, and with a block capacity bound of the
   form `exp(-C eps)` instead of `(1 - eps)^n` it settles `n >= 10` (C = 2) or `n >= 12`
   (C = 4). Against the (N) bar it settles nothing below `n = 35`
   (`study/r1-threshold.py`). So the first thing to attack is (N), not the spectral estimate.
5. **Why (N) resists the obvious fixes.** The competitor must be nonnegative and doubly
   stochastic with support inside `supp A`. The linear competitor `A(1 + alpha_i + beta_j)`
   is the chi-square optimum but can go negative; the multiplicative competitor
   `a_ij e^{alpha_i + beta_j}` is nonnegative by construction but is doubly stochastic only
   at the exact Sinkhorn solution, whose entropy is `-log cap(A)` itself; and a convex
   combination with the Hall competitor of the published proofs loses the square root again.
   A competitor that is nonnegative by construction and doubly stochastic by construction is
   what the next move needs.

## 4. Stop reason

The queries ran dry: the literature offers no fifth language and no stability theorem, and
the two local computations settled the question step 1 asks, which bar each route must clear.
