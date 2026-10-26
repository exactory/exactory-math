# Strategy study: strengthen-and-generalise

Written 2026-09-04 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

The query set of `novelty.md` (five arXiv queries on stability of the van der Waerden
inequality, one zbMATH query), plus `study/vdw-hessian.py`, written and run here.

## 2. Hits worth reading

- Egorychev 1981, Falikman 1981: the inequality whose stability is the candidate
  strengthening; the equality case is `J_n/n` and is exactly characterised, but no
  quantitative form is in print (`novelty.md`).
- Knopp-Sinkhorn 1982: the sharp statement one size out, `per(B) >= m_n` for a doubly
  stochastic `B` with a zero. This is the value the candidate strengthening has to beat to
  be worth anything.

## 3. What was learned, as constraints on the plan

1. **The candidate strengthening** is `S(n, c)`: `per(B) >= gamma_n (1 + c ||B - J_n/n||_F^2)`
   for every `B` in `Omega_n`. It implies the claim through the capacity identity, and it is
   the statement every route in `study/routes-rubric.md` was reaching for.
2. **Its local constant is exact and computable.** The permanent is multilinear, so for
   `E` with zero row and column sums,
   `per(J_n/n + E) = gamma_n (1 + (n/(2(n-1))) ||E||_F^2) + O(E^3)`: the first-order term
   vanishes because `per(A(i|j))` is constant at `J_n/n`, and the second-order coefficient is
   `(1/2)(n-2)!/n^(n-2)` times `sum_{i != k, j != l} E_ij E_kl = ||E||_F^2`. Confirmed
   numerically to a relative error of 1e-6 at `n = 4` to `8` (`study/vdw-hessian.py`):
   0.6667, 0.6250, 0.6000, 0.5833, 0.5714 against the formula.
3. **The strengthening is therefore worth nothing here.** `||T_n - J_n/n||_F^2 = 1/(n-1)^2`,
   so `S(n, n/(2(n-1)))` predicts `per(T_n)/gamma_n - 1` of about `n/(2(n-1)^3)`, which is
   1.62e-2 at `n = 7` against the true `m_n/gamma_n - 1 = 1.34e-2`: the same quantity to
   leading order. The strengthening with its true constant says no more than Knopp-Sinkhorn,
   which the attack already uses.
4. **What that settles.** The bottleneck is not the permanent side at all. Both permanent
   inputs -- van der Waerden with its exact local stability, and Knopp-Sinkhorn -- are as
   strong as they can be, and the open interface is entirely the capacity bound of move 8.

## 4. Stop reason

The queries ran dry and the candidate was evaluated in closed form: it is not stronger than
what the record already has.
