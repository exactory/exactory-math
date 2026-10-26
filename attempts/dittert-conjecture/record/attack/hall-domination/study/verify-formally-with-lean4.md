# Strategy study: verify-formally-with-lean4 (obligation `hall`)

Queries (2026-09-06): the root strategy study; Mathlib's `doublyStochastic` API
(`mem_doublyStochastic`, `mem_doublyStochastic_iff_sum`, `nonneg_of_mem_doublyStochastic`,
`sum_row_of_mem_doublyStochastic`, `sum_col_of_mem_doublyStochastic`), `IsCompact.exists_isMaxOn`,
`Metric.isCompact_of_isClosed_isBounded` and the `Matrix` normed space instances; the maths-pub
report section 6 for reusable set-level Hall material.

Settled before step 2:
1. Canonical statement: `Dittert.HallDomination` (Dittert/Obligations.lean), quantifying over n,
   A, lambda and the cut condition over all `Finset (Fin n)` pairs.
2. Defined in Mathlib: doubly stochastic matrices, finite sums over `Finset`, compactness in
   finite dimension, `Finset.card` arithmetic. Not defined: flows, residual reachability,
   augmentation; these are local definitions of this node.
3. No formal proof in print for the real-capacity statement.

Constraints on the plan:
- Encode the proof as a lemma chain in one module `Dittert/Hall.lean`: (a) the feasible set of
  flows is compact and nonempty; (b) the inductive reachability predicate; (c) augmentation along
  a derivation increases the total by a positive amount while keeping feasibility; (d) at a maximal
  flow every reachable column is saturated; (e) the cut identity for the reachable sets; (f) the cut
  condition forces total flow n lambda; (g) the scaled flow is doubly stochastic and dominated.
- Prove every lemma with the tactics of references/lean4.md section 6; no computation step is
  involved, so the finite residue is empty.
- The controlled check names `Dittert.hall_domination` with requested type
  `Dittert.HallDomination`.
