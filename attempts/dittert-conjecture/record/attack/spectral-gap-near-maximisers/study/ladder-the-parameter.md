# Strategy study: ladder-the-parameter (opened for the R7 variational rung)

Written 2026-09-03. Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| arXiv, zbMATH, Crossref | the query set of `novelty.md` and of the sibling attack | 2026-09-03 | Hwang 1986 is the only paper that uses the first-order conditions on `K_n`; it proves the positive-maximiser case and the row-stochastic case with them |
| local | `study/r7-variational.py`, run here | 2026-09-03 | the first-order identities, verified exactly |

## 2. Hits worth reading

- Hwang, Linear Algebra Appl. 76 (1986) 31-44 (through the statements quoted by
  Cheon-Wanless 2012 and by the three 2026 preprints): the only positive maximiser is
  `J_n/n`; the only row-stochastic maximiser is `J_n/n`; `phi` has a strict local maximum at
  `J_n/n`; every row and column sum of a maximiser lies in an explicit interval. All four are
  first-order or second-order consequences, so this is the rung already climbed by the
  variational method.
- Cheon-Wanless 2012 Thm 3.2 and 3.7: the zero pattern results, also variational in spirit.

## 3. What was learned, as constraints on the plan

1. **The rung the variational method has already reached** is Hwang's: no positive maximiser
   other than `J_n/n`. What it has not reached is any statement forcing a contradiction at a
   maximiser with a zero, which is the whole open problem.
2. **The exact first-order identities.** Verified to machine precision on the
   Knopp-Sinkhorn extremal for `n = 5, 6, 7, 8` (`study/r7-variational.py`). With
   `R = prod r_i`, `C = prod c_j`, `P = per(A)`, `S_i = sum_j a_ij/c_j`,
   `T_j = sum_i a_ij/r_i`, a maximiser satisfies
   `mu = phi(A)`, `R + C S_i - P = phi r_i` and `R T_j + C - P = phi c_j`, and at a zero
   entry `per(A(i0|j0)) >= R/r_{i0} + C/c_{j0} - phi(A)`.
3. **The minor bound is real but weak.** Its right side is at least
   `gamma_n - delta - 2 sqrt(2 delta)`, which is positive only for `delta < gamma_n^2/8`, so
   it says nothing in the regime `delta ~ gamma_n` where the difficulty sits. The
   complementary upper bound `per(M) <= (s_M/(n-1))^{n-1} ~ e^{-1}` is far above `gamma_n`,
   so the two do not meet.
4. **A structural fact worth keeping.** The `(i0, j0)` minor of the Knopp-Sinkhorn extremal
   is exactly van der Waerden extremal: `per(T_n(0|0))` equals
   `((n-2)/(n-1))^{n-1} gamma_{n-1}` to every printed digit at `n = 5, 6, 7, 8`, because that
   minor is the uniform `(n-1) x (n-1)` matrix. So the extremal on the face is the matrix
   whose minor through the zero is itself extremal, one size down. This is the recursion the
   problem has, and no route in the record uses it yet.
5. **T_n is not a stationary point of `phi` on `K_n`.** Its gradient at the zero entry
   exceeds `mu` by `9.9e-3` at `n = 5` and `1.0e-3` at `n = 7`, so moving mass into the zero
   raises `phi`. That is the conjecture's content at the extremal, and it is checkable
   exactly; what is missing is the same statement at every other face point.

## 4. Stop reason

The queries ran dry: Hwang 1986 is the only variational source and its rungs are recorded.
