# Bridge 11 (dimensions 11 to 15): lemma structure and status

Target: `Dittert.bridge_11 (hR : Reduction) (hH : HallDomination) (hF : GurvitsFloors)
(hS : ScalarCertificates11) : Case 11 15` in `Dittert/Bridges.lean`.

Project: `scratch/bridge11-work`, a copy of `scratch/reduction-work` without `.lake`
(Lean v4.33.1, Mathlib rev 0df444a360eaa60ab8c11dca51a86af692955474, shared `packagesDir`).
`Dittert/Basic.lean`, `Dittert/Obligations.lean`, `Dittert/Scalar/Defs*.lean` are unchanged
(frozen blueprint). `lake-manifest.json` and `lean-toolchain` are unchanged; no `lake update` was run.
Build tool: `~/.elan/bin/lake` (not on the default shell PATH).

## Status (2026-09-07)

- `Dittert.bridge_11` is fully proved. `bridge_7` and `bridge_8` keep their `sorry` as instructed.
- `lake build +Dittert.Bridges`: success. The only `sorry` warnings are `bridge_7` (line 29) and
  `bridge_8` (line 34).
- `lake env lean AuditBridge11.lean` prints
  `'Dittert.bridge_11' depends on axioms: [propext, Classical.choice, Quot.sound]`.
- No `native_decide`, no `decide +native`, no added `axiom`, no `implemented_by`, no `extern` on
  the import path (`Basic`, `Obligations`, `Scalar/Defs11`, `Reduction`, `Hall`, `Bridge/Common`,
  `Bridge/N11`, `Bridges`).
- Line counts: `Bridge/Common.lean` 795, `Bridge/N11.lean` 660, `Bridges.lean` 45,
  `AuditBridge11.lean` 3 (imported and unchanged: `Reduction.lean` 502, `Hall.lean` 393).

## Status log

- session 1: project copied, plan written, Mathlib lemma names checked.
- session 2: `Dittert/Bridge/Common.lean` complete (no `sorry`).
- session 3: `Dittert/Bridge/N11.lean` complete, `bridge_11` proved, audit run.

## Lemma table: `Dittert/Bridge/Common.lean`

Every blueprint statement is kept with its original name and statement; three unused hypotheses
were renamed with a leading underscore (`_hn` in `stationarity`, `_hA` in
`cut_condition_hallLambda` and `zero_block_of_min_cut`). Helpers added by this node are marked (+).

Section 1, permanent expansion:

| Lemma | Statement in words | Status |
|---|---|---|
| `minor` | `A.submatrix i.succAbove j.succAbove` | definition |
| (+) `permanent_succ_column_zero` | Laplace expansion along column 0 | proved (port, see below) |
| (+) `permanent_succ_column` | expansion along column `j` | proved (port) |
| (+) `permanent_succ_row` | expansion along row `i` | proved (port) |
| `permanent_expand_row` | `per A = ∑_j A i j per (minor A i j)` | proved |
| `permanent_expand_col` | `per A = ∑_i A i j per (minor A i j)` | proved |
| `permanent_nonneg` | nonnegative entries give `0 ≤ per A` | proved |
| `permanent_mono` | `0 ≤ B ≤ A` entrywise gives `per B ≤ per A` | proved |
| `permanent_smul'` | `per (c • B) = c^n per B` | proved |

Section 2, the budget:

| Lemma | Statement in words | Status |
|---|---|---|
| (+) `sum_log_le_card_mul_log_mean` | AM-GM in log form: `∑ log y ≤ |T| log (mean)` | proved |
| `prod_le_one_of_sum_eq` | nonnegative reals with sum `n` have product at most 1 | proved |
| `rowProd_le_one`, `colProd_le_one` | `R ≤ 1`, `C ≤ 1` for feasible `A` | proved |
| `phi_maximizer_ge` | `2 - γ_n ≤ Φ A` at a maximizer | proved |
| `permanent_le_gamma_of_maximizer` | `per A ≤ γ_n` at a maximizer | proved |
| `deficit_budget` | `(1 - R) + (1 - C) ≤ γ_n - per A` | proved |
| `rowProd_ge`, `colProd_ge` | `1 - γ_n ≤ R`, `1 - γ_n ≤ C` | proved |
| (+) `factorial_lt_pow_self` | `n! < n^n` for `n ≥ 2` | proved |
| `gamma_lt_one` | `γ_n < 1` for `n ≥ 2` | proved |
| `rowSum_pos_of_maximizer`, `colSum_pos_of_maximizer` | line sums of a maximizer are positive | proved |

Section 3, stationarity:

| Lemma | Statement in words | Status |
|---|---|---|
| (+) `rowSum_add_single`, `colSum_add_single`, `totalSum_add_single` | sums after adding `ε` at `(i, j)` | proved |
| (+) `prod_add_single_index` | `∏ (f r + [r = i] ε) = ∏ f + ε (∏ f) / f i` | proved |
| (+) `minor_add_single_row` | minors along row `i` ignore a change in row `i` | proved |
| (+) `permanent_add_single` | `per (A + ε E_ij) = per A + ε per (minor A i j)` | proved |
| `phi_add_single` | `Φ (A + ε E_ij) = Φ A + ε μ_ij` | proved |
| (+) `phi_smul` | `Φ (t • A) = t^n Φ A` | proved |
| `stationarity` | `μ_ij = Φ A` at a positive entry of a maximizer | proved |

Section 4, the Hall parameter:

| Lemma | Statement in words | Status |
|---|---|---|
| `cuts`, `cutRatio`, `hallLambda` | as in the blueprint | definitions |
| (+) `mem_cuts` | membership in `cuts n` | proved |
| `cuts_nonempty` | the full cut is a cut | proved |
| `hallLambda_le_cutRatio`, `exists_min_cut` | `inf'` facts | proved |
| (+) `cutRatio_univ` | the full cut has ratio 1 | proved |
| `hallLambda_le_one` | `λ ≤ 1` | proved |
| `cut_condition_hallLambda` | the cut condition with `λ` | proved |
| `permanent_ge_of_dominated` | `λ^n per B ≤ per A` | proved |
| `zero_of_dominated` | zeros persist | proved |
| `cutSum_doublyStochastic` | `s_B(I,J) = |I| + |J| - n + s_B(Iᶜ,Jᶜ)` | proved |
| `zero_block_of_min_cut` | a minimizing cut is tight for `B` | proved |

Section 5, the deficit bound:

| Lemma | Statement in words | Status |
|---|---|---|
| (+) `gfun` | `g a b e = -a log (1 + e/a) - b log (1 - e/b)` | definition |
| (+) `gfun_zero`, `hasDerivAt_gfun`, `hasDerivAt_gfun_sub` | `g 0 = 0`; `g' = -a/(a+e) + b/(b-e)`; `(g - 2e²/(a+b))' = e (a - b + 2e)² / ((a+b)(a+e)(b-e))` | proved |
| (+) `gfun_ge_global` | `2 e²/(a+b) ≤ g a b e` for `a, b > 0`, `-a < e < b` | proved |
| (+) `log_one_add_le_cubic` | `log (1+t) ≤ t - t²/2 + t³/3 + (10/9) t⁴` for `|t| ≤ 1/10` | proved |
| (+) `gfun_ge_local` | `(41/90)(e²/a + e²/b) ≤ g a b e` for `a, b ≥ 1`, `|e| ≤ 1/10` | proved |
| (+) `log_prod_le_neg_gfun` | grouped AM-GM: `log ∏ x ≤ -g d (n-d) e` | proved |
| (+) `neg_log_le_of_ge` | `1 - γ ≤ X`, `γ < 1` give `-log X ≤ γ/(1-γ)` | proved |
| (+) `gamma_budget` | `γ_n/(1-γ_n) < 1/400` and `n γ_n/(2(1-γ_n)) < 1/100`, `8 ≤ n ≤ 15` | proved (`interval_cases`, `norm_num`) |
| (+) `excess_bounds` | `-d < e < n - d` | proved |
| `localization` | `|e| < 1/10` | proved |
| `deficit_bound` | `(7n/(16 d (n-d))) e² ≤ 1 - ∏ x` | proved |

## Lemma table: `Dittert/Bridge/N11.lean`

| Lemma | Statement in words | Status |
|---|---|---|
| `hallScalar_gamma_cast`, `hallScalar_rectangle_cast` | the `ℚ` constants of `Defs11` as reals | proved |
| `hallScalar_oneZero_cast` | `oneZero n = γ_{n-1} γ_{n-1} / γ_{n-1-1}` for `11 ≤ n ≤ 15` | proved (per `n`, `norm_num`) |
| `hallScalar_floor_marginal`, `hallScalar_floor_proper` | the two branches of `floor` | proved |
| `hallScalar_curvature_marginal_cast`, `hallScalar_curvature_proper_cast` | the two branches of `curvature` as reals | proved |
| `sum_rowSum_compl`, `sum_colSum_compl`, `totalSum_eq_four_cuts`, `cutSum_eq_of_feasible` | inclusion-exclusion `s_A(I,J) = n - ∑_{Iᶜ} r - ∑_{Jᶜ} c + s_A(Iᶜ,Jᶜ)` | proved |
| `cutSum_nonneg`, `card_compl_cast` | small helpers | proved |
| `row_excess_small`, `col_excess_small` | `|e| ≤ 1/10` for any subset of at most `n-1` lines (empty subset included) | proved |
| `cutSum_pos_of_maximizer` | every cut sum of a maximizer is positive | proved |
| `hallLambda_pos` | `0 < λ` at a maximizer, `8 ≤ n ≤ 15` | proved |
| `cutRatio_row_cut`, `cutRatio_singleton_row`, `singleton_row_mem_cuts` | cuts with all columns | proved |
| `exists_row_eq_hallLambda` | a minimizing cut with all columns gives a row with `r_{i0} = λ` | proved |
| `cutRatio_transpose`, `swap_mem_cuts`, `hallLambda_transpose` | transposition of cuts and of `λ` | proved |
| `CaseData`, `CaseData.transpose` | the common data of a case and its transpose | definitions |
| `scalar_contradiction` | `M(1-u)^N ≤ P`, `C u² ≤ γ - P`, `0 < C u² + M (1-u)^N - γ` give `False` | proved |
| `permanent_B_ge_oneZero` | the persisting zero gives `per B ≥ oneZero (n+1)` | proved |
| `full_case` | `λ = 1` is impossible | proved |
| `row_stationarity_sum` | `R + C q - P = r_{i0} Φ` with `q = ∑_j a_{i0 j}/c_j` | proved |
| `marginal_case` | a row with `r_{i0} = λ` is impossible | proved |
| `sq_add_div_le` | weighted Cauchy-Schwarz `(e+f)²/(α+β) ≤ e²/α + f²/β` | proved |
| `proper_case` | a minimizing cut with `a, b ≥ 1` is impossible | proved |
| `marginal_case_of_cut` | a minimizing cut with all columns is impossible | proved |
| `no_zero_of_maximizer` | the case split; `a = 0` goes through `CaseData.transpose` | proved |
| `maximizer_pos` | every maximizer in dimension `11..15` is entrywise positive | proved |

## Deviations from the brief

1. Imports. `Common.lean` imports `Dittert.Reduction` (uniform matrix, `phi_uniform`,
   `entry_le_totalSum`, transposition lemmas) and `Dittert.Hall` (`rowSum_smul`, `totalSum_smul`,
   `totalSum_eq_sum_colSum`), and the Mathlib modules `SpecialFunctions.Log.Deriv`,
   `Calculus.Deriv.MeanValue`, `Calculus.LocalExtr.Basic`, `Calculus.Deriv.Pow`,
   `Calculus.Deriv.Inv`. Because `Dittert.Hall` defines `Dittert.single`, the basis matrix is
   always written `Matrix.single`.
2. Permanent expansion. Ported from `PermanentExpansion.lean` of DCPRevere/maths-pub
   (Apache-2.0; attribution in the docstring), stated on `Fin n.succ` as in the source; the
   blueprint statements on `Fin (n + 1)` follow by definitional unfolding.
3. Stationarity. Instead of a two-sided mass transfer plus Euler's identity, the proof rescales
   `A + ε E_ij` to total `n`: `Φ` is homogeneous of degree `n` (`phi_smul`), so
   `F ε = (n/(n+ε))^n (Φ A + ε μ_ij)` satisfies `F ε ≤ Φ A = F 0` for `|ε| < A i j`, and
   `IsLocalMax.hasDerivAt_eq_zero` with `F'(0) = μ_ij - Φ A` gives `μ_ij = Φ A`. The hypothesis
   `2 ≤ n + 1` of `stationarity` is not needed (kept in the signature as `_hn`).
4. Deficit bound, local part. The Taylor step uses Mathlib's
   `Real.abs_log_sub_add_sum_range_le` with three terms instead of the explicit third-derivative
   bound; the resulting constant is `41/90` (from `1/2 - 1/30 - 1/90`) instead of `1987/4374`,
   and `(400/401)(41/90) = 0.4544… > 7/16` closes the bound. The global part is the derivative
   route of the brief, with the closed form `(g - 2e²/(a+b))' = e (a - b + 2e)² / ((a+b)(a+e)(b-e))`
   and `monotoneOn_of_deriv_nonneg` / `antitoneOn_of_deriv_nonpos` on `[0, e]` and `[e, 0]`.
5. The one-zero floor. `kappa` of `Basic.lean` is not used; the identity
   `oneZero n = γ_{n-1}² / γ_{n-2}` is verified by `norm_num` for each `n = 11, …, 15`
   (`hallScalar_oneZero_cast`), which is what the full and marginal cases need.
6. The full case is handled as `λ = 1` directly: `per A ≥ per B ≥ oneZero n > γ_n ≥ per A`
   (certificate at `(a, b) = (1, 0)`, `u = 0`), without the `A = B` argument.
7. The marginal case with `a = 0` is reduced to the case `b = 0` for `Aᵀ` through
   `CaseData.transpose` and `hallLambda_transpose`, as the reviewer asked.
8. `Reduction` is used only as the hypothesis `hR` of `bridge_11`; the proved theorem
   `Dittert.reduction` is not referenced.

## The exact deficit bound and localization proved

`localization (hn : 8 ≤ n) (hn' : n ≤ 15) (x : Fin n → ℝ) (hx : ∀ i, 0 < x i)
(hsum : ∑ i, x i = n) (hX : 1 - gamma n ≤ ∏ i, x i) (S : Finset (Fin n)) (hS : 1 ≤ S.card)
(hS' : S.card ≤ n - 1) : |∑ i ∈ S, x i - S.card| < 1 / 10`

`deficit_bound` (same hypotheses) :
`7 * n / (16 * S.card * (n - S.card : ℝ)) * (∑ i ∈ S, x i - S.card) ^ 2 ≤ 1 - ∏ i, x i`

Both are the blueprint statements verbatim. The chain, with `d = |S|`, `e = ∑_S x - d`,
`g = gfun d (n-d) e`, `X = ∏ x`:

1. `excess_bounds`: `-d < e < n - d`.
2. `log_prod_le_neg_gfun`: `log X ≤ -g` (AM-GM through `log t ≤ t - 1` at `t = x_i / mean`).
3. `neg_log_le_of_ge`: `-log X ≤ γ_n / (1 - γ_n)`; `gamma_budget`: this is `< 1/400`, and
   `n γ_n / (2 (1 - γ_n)) < 1/100`.
4. `gfun_ge_global`: `2 e² / n ≤ g`, hence `e² < 1/100` and `|e| < 1/10` (localization).
5. `gfun_ge_local`: `(41/90) (e²/d + e²/(n-d)) ≤ g` on `|e| ≤ 1/10`.
6. `1 - X ≥ 1 - exp (-g) ≥ g / (1 + g) ≥ (400/401) g` and
   `(400/401)(41/90)(e²/d + e²/(n-d)) ≥ (7/16) n e² / (d (n-d))`.
