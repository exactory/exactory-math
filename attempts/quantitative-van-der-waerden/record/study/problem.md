# Problem-level study: the quantitative van der Waerden inequality

Written 2026-09-04. Contract: STUDY.md. The novelty half is in `novelty.md`.

## 1. Queries

The table in `novelty.md`: four arXiv queries by statement, two web queries, and two attempts at
Semantic Scholar that returned HTTP 429. Every neighbouring statement of `shape.neighbours` was
searched the same way.

## 2. Hits worth reading

- **Egorychev 1981 and Falikman 1981.** The inequality and its equality case. Falikman's proof is
  a variational argument on the polytope: at a minimiser, the permanent's partial derivatives
  satisfy a system that forces the matrix to be `J_n/n`. It produces the equality case but no
  rate.
- **Gurvits, arXiv:math/0510452 and arXiv:0711.3496.** The capacity proof. `per(B) >= cap(p_B)`
  times a combinatorial factor, and `cap` of a doubly stochastic matrix is 1. The method's
  documented ceiling for this problem is that capacity does not see the distance to `J_n/n`: it
  is defined by an infimum over positive scalings, and that infimum is 1 for every doubly
  stochastic matrix.
- **Gurvits and Leake, arXiv:1804.04351.** Capacity-preserving operators. Same absence, and the
  authors note their bounds are weakest exactly where the capacity is small.
- **Knopp and Sinkhorn 1982.** The minimum on the face with a zero entry, `m_n`. This is the one
  quantitative statement in print about how far above `gamma_n` the permanent sits on part of the
  polytope, and it is a statement about a face, not about distance.

## 3. What was learned, as constraints on the plan

1. **No route in print produces a deficiency term.** Both proof families (variational, capacity)
   give the value at the minimiser. So the plan cannot import a rate from the literature; it has
   to make one.
2. **The constant is pinned from above by an exact local computation.** The sibling attack proved
   `per(J_n/n + E) = gamma_n(1 + (n/(2(n-1)))||E||_F^2) + O(E^3)` for `E` with zero row and
   column sums, so no constant above `n/(2(n-1))` can hold, and that bound decreases to `1/2`.
3. **That local constant fails globally, and the failure was measured, not estimated.**
   `study/qvdw-test.py` finds a violating matrix at every `n` from 3 to 7, with slack `-5.6e-2`
   at `n = 3` falling to `-1.9e-4` at `n = 7`. So the plan must not assume the local constant.
4. **The sharp constant was measured and rises to `1/2`.** `study/qvdw-constant.py` gives
   `c*(n) = 0.250000, 0.333333, 0.418403, 0.460519, 0.486709, 0.497450` at `n = 3` to 8. The
   minimum over `n` in that range is at `n = 3`, which is why the claim fixes `1/4`.
5. **The extremal family is known at the bottom of the range and changes at `n = 6`.** At
   `n = 3, 4, 5` the minimiser is `(I + C_n)/2`, the average of two permutation matrices whose
   union is one `n`-cycle, and the ratio there is `1/4`, `1/3` and `0.418403`, each matching an
   exact hand computation: `per((I + C_n)/2) = 2^{1-n}` and
   `||(I + C_n)/2 - J_n/n||_F^2 = 2n(1/2 - 1/n)^2 + (n-2)/n`. At `n = 6` that family gives
   `0.5125`, above the measured `0.460519`, so a different matrix takes over; at `n = 7` and 8
   the measured minimiser has no zero entries at all.
6. **`n = 2` is an identity.** With `B = [[t, 1-t], [1-t, t]]`, both sides equal
   `1/2 + 2(t - 1/2)^2`. So the inequality is not merely true at `n = 2`, it is sharp everywhere
   there, and any proof must reproduce that.

## 4. Why this statement and not another

Two facts make it the right target rather than one more reformulation of Dittert's conjecture.

- It is a statement about the van der Waerden inequality alone. It mentions no capacity, no
  Sinkhorn scaling, no spectrum and no simplex, and it would stand on its own if true.
- It closes the application. With `c = 1/4`, `per(B) <= (1 + eta) gamma_n` gives
  `||B - J_n/n||_F^2 <= 4 eta`, hence `lambda_2(B) >= 1 - 2 sqrt(eta)`, and feeding that into
  Theorem R of the sibling attack closes Dittert's conjecture for every `n >= 7`; `n = 5` and
  `n = 6` are already proved there by exact sum-of-squares certificates. The arithmetic of that
  deduction is in `study/application.md`.

## 5. Stop reason

The queries ran dry: the inequality, its equality case and several proofs of it are in print, and
no deficiency term appears in any of them.
