# Strategy study: verify-formally-with-lean4 (obligation `reduction`)

Queries (2026-09-06): the root strategy study; Mathlib's `Matrix.permanent` file (multilinearity
`permanent_updateRow_add`, `permanent_updateRow_smul`, permutation and transpose invariance),
`Matrix.updateRow`, `Equiv.swap`, `IsCompact.exists_isMaxOn`, `Metric.isCompact_of_isClosed_isBounded`,
`Finset.prod` and `Finset.sum` lemmas; the local proof record named in study/problem.md.

Settled before step 2:
1. Canonical statement: `Dittert.Reduction` (Dittert/Obligations.lean).
2. Defined in Mathlib: everything the mixing argument needs (row update, permanent
   multilinearity in one row, row-swap invariance, products over `Fin n`, compactness); the
   mixing line and the first-zero parameter are local definitions.
3. No formal proof in print.

Constraints on the plan, as a lemma chain in `Dittert/Reduction.lean`:
- `exists_maximizer (n) (hn : 1 ≤ n) : ∃ A, IsMaximizer A` by compactness and continuity of Phi.
- `phi_uniform : Phi (uniform n) = 2 - gamma n`, with `permanent` of the constant matrix
  `1/n` equal to `n! / n^n` (sum over `Equiv.Perm (Fin n)` of the constant product).
- `mix` of rows i and k with parameter t; its column sums, total and feasibility for t in [0,1]
  and for small negative t when A is positive; `Phi (mix A i k t) = Phi A + alpha * t * (1 - t)`
  (multilinearity in row i and row k, symmetry under `Equiv.swap i k`).
- At a positive maximizer `alpha = 0` (a quadratic bounded above at an interior point of an
  interval on both sides has zero derivative), so Phi is constant on the mixing line.
- `first_zero`: for a positive matrix and a mixing direction with a negative entry, the largest
  t keeping all entries nonnegative gives a feasible matrix with a zero entry.
- The row version and the column version (through `transpose`, `Phi` and `Feasible` being
  transpose-invariant).
- Assemble: every maximizer is uniform; deduce `Statement n`.
- The controlled check names `Dittert.reduction` with requested type `Dittert.Reduction`.
