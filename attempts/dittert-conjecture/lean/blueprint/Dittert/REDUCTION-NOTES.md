# Reduction.lean: lemma structure

Target: `Dittert.reduction : Reduction`, where
`Reduction := ∀ n, 2 ≤ n → (∀ A, IsMaximizer A → ∀ i j, 0 < A i j) → Statement n`
(`Dittert/Obligations.lean`). Definitions `rowSum`, `colSum`, `totalSum`, `Phi`, `Feasible`,
`gamma`, `IsUniform`, `Statement`, `IsMaximizer` are in `Dittert/Basic.lean`; neither file was
changed.

Status (2026-09-06): `lake build +Dittert.Reduction` succeeds with no `sorry`;
`#print axioms Dittert.reduction` reports `[propext, Classical.choice, Quot.sound]`
(`AuditReduction.lean` at the project root). No `native_decide`, no added axiom.

Mathlib note: `Matrix.permanent_updateRow_add` does not exist in Mathlib v4.33.1 (only
`permanent_updateRow_smul` and `permanent_updateCol_smul` do); additivity is proved here.

## 1. Continuity and compactness

| Lemma | Statement |
|---|---|
| `continuous_Phi` | `Phi` is continuous in the entries |
| `entry_le_totalSum` | `0 ≤ A → A i j ≤ totalSum A` |
| `isCompact_feasible` | `{A ∣ Feasible A}` is compact (closed subset of the box `[0, n]^(n×n)`) |
| `uniform n` | the matrix `J_n / n` (definition) |
| `feasible_uniform` | `1 ≤ n → Feasible (uniform n)` |
| `exists_maximizer` | `1 ≤ n → ∃ A, IsMaximizer A` (`IsCompact.exists_isMaxOn`) |

## 2. The value at the uniform matrix

| Lemma | Statement |
|---|---|
| `permanent_uniform` | `per (uniform n) = gamma n` |
| `rowSum_uniform`, `colSum_uniform` | every row and column sum of `uniform n` is `1` |
| `phi_uniform` | `Phi (uniform n) = 2 - gamma n` |
| `isUniform_iff_eq_uniform` | `IsUniform A ↔ A = uniform n` |

## 3. Mixing two rows

`mixRows A i k t`: row `i` becomes `(1-t) A i + t A k`, row `k` becomes `t A i + (1-t) A k`,
other rows unchanged.

Entry lemmas and sums:

| Lemma | Statement |
|---|---|
| `mixRows_apply_self`, `mixRows_apply_other`, `mixRows_apply_of_ne` | the three kinds of entries |
| `sum_eq_add_add_sum_erase_erase`, `prod_eq_mul_mul_prod_erase_erase` | split a sum or product over `Fin n` at two distinct indices |
| `sum_erase_erase_mixRows` | away from rows `i`, `k` the entries are those of `A` |
| `colSum_mixRows` | column sums are preserved |
| `totalSum_mixRows` | the total is preserved |
| `rowSum_mixRows_self`, `rowSum_mixRows_other`, `rowSum_mixRows_of_ne` | the row sums |
| `mixRows_zero` | `mixRows A i k 0 = A` |
| `mixRows_symm` | `mixRows A i k (1 - t) = (mixRows A i k t).submatrix (Equiv.swap i k) id` (proved, not used downstream: `alpha` is computed explicitly instead) |

The permanent along the line (multilinearity in rows):

| Lemma | Statement |
|---|---|
| `permanent_updateCol_eq` | `per (updateCol M j w) = ∑ σ, w (σ j) * ∏ c ∈ univ.erase j, M (σ c) c` |
| `permanent_updateCol_add` | additivity of `per` in one column |
| `permanent_updateRow_add` | additivity of `per` in one row (by transposition) |
| `mixRows_eq_updateRow` | `mixRows A i k t = updateRow (updateRow A i ((1-t)•A i + t•A k)) k (t•A i + (1-t)•A k)` for `i ≠ k` |
| `updateRow_updateRow_eq_swap` | `updateRow (updateRow A k (A i)) i (A k) = A.submatrix (Equiv.swap i k) id` |
| `permanent_mixRows` | `per (mixRows A i k t) = per A + t (1-t) (per A_{k←i} + per A_{i←k} - 2 per A)` |

Here `A_{k←i} = updateRow A k (A i)`. The expansion uses `permanent_updateRow_add`,
`Matrix.permanent_updateRow_smul`, `Matrix.updateRow_comm`, `Matrix.updateRow_eq_self`, and
`Matrix.permanent_permute_cols (Equiv.swap i k)`.

The row and column products and the quadratic:

| Lemma | Statement |
|---|---|
| `prod_rowSum_mixRows` | `∏ rowSum (mix) = ∏ rowSum A + t (1-t) (r_i - r_k)^2 ∏_{r ≠ i,k} r_r` |
| `prod_colSum_mixRows` | the column product is constant in `t` |
| `phi_mixRows_quadratic` | `∃ α, ∀ t, Phi (mixRows A i k t) = Phi A + α t (1-t)`, with `α = (r_i - r_k)^2 ∏_{r≠i,k} r_r - (per A_{k←i} + per A_{i←k} - 2 per A)` |

Feasibility near `0` and the vanishing coefficient:

| Lemma | Statement |
|---|---|
| `continuous_mixRows_entry` | each entry is continuous in `t` |
| `feasible_mixRows_of_pos` | positive feasible `A`: `∃ ε > 0, ∀ t, ∣t∣ < ε → Feasible (mixRows A i k t)` (`Filter.eventually_all`, `Filter.Tendsto.eventually_const_lt`, `Metric.eventually_nhds_iff`) |
| `phi_mixRows_const` | positive maximizer: `Phi (mixRows A i k t) = Phi A` for every `t` (`α t (1-t) ≤ 0` at `t = ±min(ε/2, 1/2)` forces `α = 0`) |

Following the line to the boundary:

| Lemma | Statement |
|---|---|
| `mixRows_apply_eq_add_mul` | each entry is affine: `mixRows A i k t r c = A r c + t * (mixRows A i k 1 r c - A r c)` |
| `exists_boundary_mixRows` | positive `A`, rows `i ≠ k` differing somewhere: `∃ t`, the mixing is nonnegative with a zero entry (`t` = minimum over entries with negative slope `D` of `A r c / (-D r c)`, via `Finset.exists_min_image`) |

## 4. Transposition

| Lemma | Statement |
|---|---|
| `totalSum_transpose`, `feasible_transpose`, `phi_transpose`, `isMaximizer_transpose` | invariance under `Aᵀ` |

## 5. Assembly

| Lemma | Statement |
|---|---|
| `rows_eq_of_maximizer` | under the positivity hypothesis a maximizer has all rows equal (else `exists_boundary_mixRows` and `phi_mixRows_const` produce a maximizer with a zero entry) |
| `maximizer_uniform` | `2 ≤ n`, positivity hypothesis: every maximizer is uniform (rows equal, columns equal via `Aᵀ`, so all entries equal `v` with `n (n v) = n`) |
| `reduction` | the obligation: a maximizer `M` is `uniform n`, so `Phi A ≤ Phi M = 2 - gamma n`; equality makes `A` a maximizer, hence uniform; conversely `IsUniform A` gives `A = uniform n` |
