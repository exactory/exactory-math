# Hall domination: proof notes

`Dittert/Hall.lean` proves `Dittert.hall_domination : HallDomination` (statement in
`Dittert/Obligations.lean`). Toolchain Lean v4.33.1, Mathlib rev
`0df444a360eaa60ab8c11dca51a86af692955474`.

Verification record (2026-09-06):

* `lake build +Dittert.Hall` succeeds; `lake env lean Dittert/Hall.lean` prints no warning.
* `lake env lean AuditHall.lean` prints
  `'Dittert.hall_domination' depends on axioms: [propext, Classical.choice, Quot.sound]`.
* No `sorry`, `axiom`, `native_decide`, `decide`, or `admit` in the file. 393 lines.

## Argument

Maximum flow with real capacities. A flow is a matrix `F` with `0 ≤ F ≤ A` entrywise and every
row sum and column sum at most `lam`. A maximal flow exists by compactness. Residual
reachability is an inductive predicate. For a maximal flow every reachable column is saturated,
since a residual walk into a column with slack gives a strictly better flow. Counting the total
over the reachable rows `I` and reachable columns `J`, and applying the cut condition to
`(I, Jᶜ)`, gives total `≥ lam * n`, hence every row and column sum equals `lam`. Then
`B = F / lam` is doubly stochastic and `lam * B = F ≤ A`.

## Lemma structure

Sums (algebra of `rowSum`, `colSum`, `totalSum` from `Basic.lean`):

* `totalSum_eq_sum_rowSum`, `totalSum_eq_sum_colSum` (the second is `Finset.sum_comm`).
* `rowSum_add`, `rowSum_sub`, `rowSum_smul`, `colSum_add`, `colSum_sub`, `colSum_smul`,
  `totalSum_add`, `totalSum_smul`.

Indicator and single-entry matrix:

* `ind i a := if a = i then 1 else 0`; `sum_ind : ∑ a, ind i a = 1`.
* `single i j` is the matrix with one entry `1` at `(i, j)`; `single_apply`, `rowSum_single`,
  `colSum_single`.

Flows and the maximizer:

* `FlowSet A lam : Set (Matrix (Fin n) (Fin n) ℝ)`, the flows.
* `zero_mem_flowSet`: the zero matrix is a flow (needs `0 ≤ A`, `0 ≤ lam`).
* `isClosed_flowSet`: each defining inequality is closed (`isClosed_le`, continuity by
  `fun_prop`), and the set is their intersection.
* `flowSet_subset_box`: flows lie in the product of the intervals `[0, A i j]`.
* `isCompact_flowSet`: closed subset of the compact box (`isCompact_univ_pi`, `isCompact_Icc`).
* `exists_max_flow`: `IsCompact.exists_isMaxOn` applied to the continuous `totalSum`.

Residual reachability and augmentation:

* `inductive Reach A F lam : Fin n ⊕ Fin n → Prop` with constructors `slack` (a row with
  `rowSum F i < lam`), `col` (from a reachable row `i` along `F i j < A i j`), `row` (from a
  reachable column `j` along `0 < F i j`).
* `AugSpec A F lam v`: there is a start row `s` with slack and a direction matrix `D` such that
  `0 < D a b → F a b < A a b`, `D a b < 0 → 0 < F a b`, row sums of `D` are
  `ind s - (ind i if v = inl i)`, column sums are `ind j if v = inr j`.
* `augSpec_of_reach`: induction on `Reach`. `slack` gives `D = 0`; `col i j` adds
  `single i j`; `row i j` subtracts `single i j`. Repeated vertices need no special treatment,
  because only the row and column sums of `D` matter.
* `exists_better_flow`: from `AugSpec (inr j)` and `colSum F j < lam`, the flow `F + eps • D`
  has total `totalSum F + eps` for a small `eps > 0`. The size condition on `eps` is expressed
  as finitely many `∀ᶠ eps in 𝓝[>] 0` statements (`eventually_lt_nhds`, `eventually_all`),
  and one `eps` is extracted with `Filter.Eventually.exists`. Entry bounds use
  `lt_div_iff₀` case by case on the sign of `D a b`.
* `le_colSum_of_reach`: for a maximal flow, a reachable column has `lam ≤ colSum F j`.

Counting and the theorem:

* `max_flow_saturated`: with `I`, `J` the reachable rows and columns, the four facts
  (reachable columns saturated, unreachable rows saturated, `F = A` on `I × Jᶜ`, `F = 0` on
  `Iᶜ × J`) give `totalSum F = |J| lam + cutSum A I Jᶜ + |Iᶜ| lam`. The cut condition at
  `(I, Jᶜ)` when `n < |I| + |Jᶜ|`, or `cutSum ≥ 0` otherwise, gives `lam * n ≤ totalSum F`,
  and `Finset.sum_eq_sum_iff_of_le` turns this into equality of every row and column sum.
* `hall_domination`: `B := Matrix.of fun i j => F i j / lam`, membership through
  `mem_doublyStochastic_iff_sum`, and `lam * B i j = F i j ≤ A i j`.

## Remarks

* The hypothesis `1 ≤ n` of `HallDomination` is not used.
* `Basic.lean` and `Obligations.lean` are unchanged. `Dittert.lean` still carries its own
  `theorem hall_domination : HallDomination := by sorry`; replacing that line with
  `import Dittert.Hall` is a separate decision that this module does not make.
