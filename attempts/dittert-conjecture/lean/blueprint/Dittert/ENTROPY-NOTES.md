# Notes for `Dittert/Entropy.lean` (the obligation `Dittert.core_entropy : CoreEntropy`)

Status line: **complete** (2026-09-06). `Dittert.core_entropy : CoreEntropy` is proved in
`Dittert/Entropy.lean` with helpers `Dittert/Entropy/Algebra.lean`, `Dittert/Entropy/AMGM.lean`
and `Dittert/Entropy/Minor.lean`; `lake build +Dittert.Entropy` succeeds and
`#print axioms Dittert.core_entropy` reports `[propext, Classical.choice, Quot.sound]` (see the
build record at the end).

Provenance of the port used: DCPRevere/maths-pub, commit
`0a1cb0a14fefe85668365d448f9bbaf4dd89d458`, Apache-2.0, ported as the `GurvitsPort` library of
this project (see `../maths-pub-port/PORT-NOTES.md` and `../maths-pub-port/AXIOMS.txt`). The
floors modules `Dittert/Floors/Analytic.lean` and `Dittert/Floors/Chain.lean` are reused as they
stand (see `Dittert/FLOORS-NOTES.md`); no port file and no floors file is modified.

## Target

```
def CoreEntropy : Prop :=
  ∀ k : ℕ, 1 ≤ k → ∀ M ∈ doublyStochastic ℝ (Fin (k + 1)), ∀ j : Fin (k + 1),
    gamma k * ∏ i, (1 - M i j) ^ (1 - M i j) ≤
      ∏ i, ((M.submatrix (Fin.succAbove i) (Fin.succAbove j)).permanent) ^ (M i j)
```

## Route

Notation: `q i = M i j`, `d i = per (M.submatrix i.succAbove j.succAbove)`,
`B i c = M i (j.succAbove c)` (the `(k+1) × k` matrix with column `j` deleted), `t i > 0`.

1. `extend a B` is the `(k+1) × (k+1)` matrix with column `0` equal to `a` and columns
   `c.succ` equal to `B`. With `a i = q i * t i`, its row polynomial `rowPoly (extend a B)` is a
   product of nonzero nonnegative linear forms (each row of `M` has a positive entry), hence
   H-stable (`FaceBounds.hstable_rowPoly`), homogeneous of degree `k + 1`, with nonnegative
   coefficients.
2. `Q := GurvitsInduction.reduce (rowPoly (extend a B))`, the coefficient of `x₀` (this is
   `∂₀` followed by `x₀ := 0`). `Q` is H-stable when nonzero by the floors lemma
   `Floors.Analytic.hstable_reduce` (the port's derivative closure on the explicit
   `nonDegenerate_of_natDegree_pos`, then `restrict_zero_hstable`), homogeneous of degree `k`
   (`Floors.Chain.isHomogeneous_reduce`), with nonnegative coefficients
   (`GurvitsInduction.coeff_reduce`).
3. The identity `reduce (rowPoly A) = ∑ i, (∏ r, linForm (row i.succAbove r of A, column 0
   deleted)) * C (A i 0)`: `finSuccEquiv` sends each row form to `C L_i + C (a_i) X`, and the
   `X`-coefficient of a product of such linear polynomials is `∑ i, a_i ∏_{i' ≠ i} L_{i'}`
   (through `Polynomial.derivative_prod_finset` evaluated at `0`). Consequences: the top
   coefficient of `Q` is `∑ i, d i * (q i * t i)` (`FaceBounds.coeff_topIdx_rowPoly` on each
   minor), and the value `Q(x) = ∑ i, (∏ r, L_{i.succAbove r}(x)) * (q i * t i)`.
4. Weighted AM–GM (`Real.geom_mean_le_arith_mean_weighted`) at every positive `x`, twice:
   `Q(x) ≥ (∏ i, t i ^ q i) * ∏ i', L_{i'}(x) ^ (1 - q i')` (weights `q`, column sum `1`), and
   `L_{i'}(x) ^ (1 - q i') ≥ (1 - q i') ^ (1 - q i') * ∏ c, x c ^ B i' c` (weights
   `B i' c / (1 - q i')`; when `1 - q i' = 0` both sides are `1`). The column sums of `B` give
   `∏ i', ∏ c, x c ^ B i' c = ∏ c, x c`, so `Q(x) / ∏ c, x c ≥ (∏ t ^ q) (∏ (1 - q) ^ (1 - q))`
   and `Capacity.le_cap` bounds the capacity below. No normalisation `∏ x = 1` is needed.
5. Gurvits (`GurvitsUnconditional.gurvitsBound`): `gamma k * cap Q ≤ ∑ i, d i * (q i * t i)`.
6. `d i > 0` when `q i > 0` by Birkhoff–von Neumann
   (`exists_eq_sum_perm_of_mem_doublyStochastic`): a permutation `σ` with `σ i = j` and positive
   weight has `M r (σ r) > 0` for every `r`; `σ⁻¹` restricted to the minor is a permutation of
   its rows, so one term of the permanent is positive and all terms are nonnegative.
7. `t i = (d i)⁻¹` when `q i > 0`, `t i = 1` otherwise: the right side of 5 is `∑ q i = 1` and
   `∏ t ^ q = (∏ d ^ q)⁻¹`, which rearranges to the claim.

## Lemma table

| lemma | statement in words | status |
|---|---|---|
| `Entropy.prod_erase_eq_prod_succAbove` | a product over `univ.erase i` is a product over `i.succAbove` | proved (`lake build +Dittert.Entropy.Algebra` clean, 2026-09-06) |
| `Entropy.finSuccEquiv_C'` | `finSuccEquiv` of a constant is the constant | proved |
| `Entropy.finSuccEquiv_linForm` | `finSuccEquiv` of `∑ c, a c x_c` is `C (∑ c, a c.succ x_c) + C (a 0) X` | proved |
| `Entropy.coeff_one_prod_linear` | `[X] ∏ᵢ (bᵢ + aᵢ X) = ∑ᵢ (∏_{i' ≠ i} bᵢ') aᵢ` | proved |
| `Entropy.extend`, `extend_zero`, `extend_succ`, `extend_nonneg`, `extend_submatrix` | the extended matrix (column `0` = `a`, columns `c.succ` = `B`) and its entries, nonnegativity, minor | defined / proved |
| `Entropy.rowPoly_minor` | `rowPoly (A(i|0))` is `∏ r, linForm (row i.succAbove r, column 0 deleted)` | proved (`rfl`) |
| `Entropy.reduce_rowPoly` | `reduce (rowPoly A) = ∑ i, rowPoly (A(i|0)) * C (A i 0)` | proved |
| `Entropy.coeff_topIdx_reduce_rowPoly` | the top coefficient of `reduce (rowPoly A)` is `∑ i, per (A(i|0)) * A i 0` | proved |
| `Entropy.permanent_succ_column_zero` | Laplace expansion of the permanent along column `0` (by-product) | proved |
| `Entropy.eval_reduce_rowPoly` | `eval x (reduce (rowPoly A)) = ∑ i, (∏ r, ∑ c, A (i.succAbove r) c.succ * x c) * A i 0` | proved |
| `Entropy.coeff_reduce_rowPoly_nonneg` | nonnegative coefficients of `reduce (rowPoly A)` for `A ≥ 0` | proved |
| `Entropy.row_amgm` | `s ^ s ∏_c x_c ^ b_c ≤ (∑_c b_c x_c) ^ s` for `b ≥ 0`, `s = ∑ b`, `x > 0` (both sides `1` when `s = 0`) | proved (`lake env lean Dittert/Entropy/AMGM.lean` clean, 2026-09-06) |
| `Entropy.rows_amgm` | the product of the row bounds; the column sums `1` turn `∏ᵢ ∏_c x_c ^ B i c` into `∏_c x_c` | proved |
| `Entropy.prod_succAbove_eq_prod_rpow` | `∏ r, f (i.succAbove r) = ∏ i', f i' ^ [i' ≠ i]` (real exponents `0`/`1`) | proved |
| `Entropy.sum_weights` | `∑ i, [i ≠ i'] q i = 1 - q i'` when `∑ q = 1` | proved |
| `Entropy.column_amgm` | weights `q`: `(∏ t ^ q) ∏ i', L i' ^ (1 - q i') ≤ ∑ i, (∏ r, L (i.succAbove r)) (q i t i)` | proved |
| `Entropy.pointwise_bound` | `(∏ t ^ q)(∏ (1-q)^(1-q)) ∏ x ≤ Q(x)` at every positive `x` | proved |
| `Entropy.cap_lower_bound` | `(∏ t ^ q)(∏ (1-q)^(1-q)) ≤ cap Q` for `Q = reduce (rowPoly (extend (q * t) B))` | proved |
| `Entropy.permanent_nonneg` | the permanent of a nonnegative matrix is nonnegative | proved (`lake env lean Dittert/Entropy/Minor.lean` clean, 2026-09-06) |
| `Entropy.permMatrix_apply'` | entry `(r, c)` of a permutation matrix is `[σ r = c]` | proved |
| `Entropy.entry_eq_sum_perm` | `M r c = ∑ σ, w σ [σ r = c]` for the Birkhoff weights | proved |
| `Entropy.permanent_minor_pos` | `M` doubly stochastic, `M i j > 0` gives `per M(i|j) > 0` | proved |
| `Entropy.hstable_rowPoly_extend` | `rowPoly (extend a B)` is H-stable when every row has a positive entry | proved (`lake env lean Dittert/Entropy.lean` clean, 2026-09-06) |
| `Entropy.gurvits_reduce` | `gamma k * cap Q ≤ ∑ i, per ((extend a B)(i|0)) * a i` for `Q = reduce (rowPoly (extend a B))` (zero case by `cap_zero`; otherwise `hstable_reduce` + `gurvitsBound`) | proved |
| `Dittert.core_entropy` | the obligation `CoreEntropy` | proved (elaborates; build and axiom audit recorded below) |

## Port lemmas used

`Gurvits.HStable`, `Gurvits.topIdx`, `Capacity.{cap, le_cap, cap_zero, monom, monom_one_exp,
rowProd}`, `GurvitsInduction.{reduce, coeff_reduce, coeff_topIdx_reduce}`,
`FaceBounds.{rowPoly, eval_rowPoly, rowPoly_isHomogeneous, rowPoly_coeff_nonneg, hstable_rowPoly,
coeff_topIdx_rowPoly}`, `LorentzianPoly.linForm`, `GurvitsUnconditional.gurvitsBound`.

No port file is modified.

## Floors lemmas used

`Floors.Analytic.hstable_reduce` (this is the brief's "derivative in `z` through the port's
derivative closure with the explicit non-degeneracy lemma, then the restriction `z := 0` through
`restrict_zero_hstable`": `hstable_reduce` is proved in `Dittert/Floors/Analytic.lean` from
`HStableOrbit.hstable_pderiv_of_nonDegenerate` on `nonDegenerate_of_natDegree_pos` followed by
`restrict_zero_hstable`; it is imported and used as it stands, not re-proved),
`Floors.Chain.isHomogeneous_reduce`, `Floors.Chain.gamma_nonneg`.

No floors file is modified.

## Mathlib results used

`exists_eq_sum_perm_of_mem_doublyStochastic` (Birkhoff–von Neumann, checked in
`Mathlib/Analysis/Convex/Birkhoff.lean`: `∃ w, (∀ σ, 0 ≤ w σ) ∧ ∑ σ, w σ = 1 ∧ ∑ σ, w σ • σ.permMatrix R = M`),
`nonneg_of_mem_doublyStochastic`, `sum_row_of_mem_doublyStochastic`,
`sum_col_of_mem_doublyStochastic`, `Real.geom_mean_le_arith_mean_weighted`,
`Polynomial.derivative_prod_finset`, `Polynomial.coeff_derivative`,
`Polynomial.coeff_zero_eq_eval_zero`, `MvPolynomial.finSuccEquiv_{apply, X_zero, X_succ}`,
`Fin.univ_succAbove`, `Fin.prod_univ_succAbove`, `Fin.sum_univ_succAbove`,
`Fin.exists_succAbove_eq`, `Fin.succAbove_ne`, `Fin.succAbove_right_injective`,
`Real.{finsetProd_rpow, rpow_sum_of_nonneg, mul_rpow, inv_rpow, div_rpow, rpow_mul, rpow_le_rpow,
rpow_pos_of_pos, rpow_zero_pos}`, `PEquiv.toMatrix_apply`, `Equiv.toPEquiv_apply`.

## Deviations from the brief

1. `Q_t` is *defined* as `GurvitsInduction.reduce (rowPoly (extend (q * t) B))` (the coefficient
   of `x₀`), and the brief's expression `∑ᵢ qᵢ tᵢ ∏_{i' ≠ i} L_{i'}` is a proved lemma
   (`Entropy.reduce_rowPoly`, through `Polynomial.derivative_prod_finset`) rather than the
   definition. H-stability of `Q_t` is then exactly the brief's route (`hstable_reduce`).
2. The brief's top-coefficient argument ("`∏_{i' ≠ i} L_{i'}` is the row form of the minor") is
   realised through `reduce_rowPoly` plus the port's `coeff_topIdx_rowPoly` on each minor.
   Mathlib has no Laplace expansion of the permanent; the one along column `0` falls out as a
   by-product (`Entropy.permanent_succ_column_zero`) and is recorded but not needed.
3. The AM–GM step is taken at every positive `x`, without the normalisation `∏ x_c = 1`: the
   column sums give `∏ᵢ ∏_c x_c ^ B i c = ∏_c x_c` directly, so `Q_t(x) ≥ C · ∏_c x_c` and
   `Capacity.le_cap` applies with no scaling argument.
4. The case `Q_t = 0` is handled by `Capacity.cap_zero` (both sides of Gurvits vanish) instead
   of proving `Q_t ≠ 0` from the positive top coefficient; `hstable_reduce` is used only in the
   nonzero case, as its statement requires.
5. In the Birkhoff step the permutation of the minor is built from `σ⁻¹` on the columns `≠ j`
   (`c ↦ σ⁻¹ (j.succAbove c)` lands in the rows `≠ i`, so it is `i.succAbove ∘ τ₀` with `τ₀`
   injective, hence bijective), which is the same permutation as the brief's `σ` restricted to
   the minor, read in the direction Mathlib's `permanent` (`∑ σ, ∏ c, M (σ c) c`) uses.
6. As the review allows, there is no smoothing limit: `t i = 1` when `q i = 0`, `t i = (d i)⁻¹`
   when `q i > 0`; `Real.rpow` gives `1 ^ 0 = 1 = (d i ^ 0)⁻¹` in the first case.

## Project changes outside the new modules

`lakefile.toml`: the `Dittert` library now declares
`roots = ["Dittert", "Dittert.Floors", "Dittert.Entropy"]` (the only edit; `diff -rq` against
`../floors-work` outside the new files reports only this file). `Dittert.lean`,
`Dittert/Basic.lean`, `Dittert/Obligations.lean`, `Dittert/Scalar/Defs*.lean`,
`Dittert/Floors.lean`, `Dittert/Floors/*.lean`, `lake-manifest.json`, `lean-toolchain` and every
`GurvitsPort/*.lean` file are untouched. `Dittert.lean` still carries its own `sorry`
placeholder for `core_entropy`; it does not import `Dittert.Entropy`, so nothing imports both.
The project was created by copying `../floors-work` without its `.lake` directory, build logs,
`SmokePort.lean` and `AuditFloors.lean`; `lake update` was never run.

## Build record (2026-09-06, Lean v4.33.1, Mathlib 0df444a360eaa60ab8c11dca51a86af692955474)

| command (from `scratch/entropy-work`, `lake` = `~/.elan/bin/lake`) | result |
|---|---|
| `lake build +Dittert.Floors` (fresh `.lake`; compiles the port and the floors modules here) | `Built Dittert.Floors (5.7s)`, `Build completed successfully (3452 jobs)` |
| `lake env lean Dittert/Entropy/Algebra.lean` | no errors, no warnings (after two fixes: `map_add` added to the simp set of `finSuccEquiv_linForm`; `coeff_C_mul` with `mul_comm` in place of the nonexistent `coeff_mul_C`) |
| `lake build +Dittert.Entropy.Algebra` | `Built Dittert.Entropy.Algebra (5.1s)`, `Build completed successfully (3109 jobs)` |
| `lake env lean Dittert/Entropy/AMGM.lean` | no errors, no warnings (after two fixes: binder types `i : Fin (k + 1)` in `column_amgm`; `Real.finsetProd_rpow` in place of the deprecated `finset_prod_rpow`, used right-to-left) |
| `lake env lean Dittert/Entropy/Minor.lean` | no errors, no warnings (after `push Not` in place of the deprecated `push_neg`) |
| `lake build +Dittert.Entropy.AMGM +Dittert.Entropy.Minor` | `Built Dittert.Entropy.Minor (5.0s)`, `Built Dittert.Entropy.AMGM (5.3s)`, `Build completed successfully (3195 jobs)` |
| `lake env lean Dittert/Entropy.lean` | no errors, no warnings (after one fix: parentheses in the final `(gamma k * ∏ …) / ∏ …`) |
| `lake build +Dittert.Entropy` | `Built Dittert.Entropy (5.9s)`, `Build completed successfully (3464 jobs)` |
| `lake env lean AuditEntropy.lean` | `'Dittert.core_entropy' depends on axioms: [propext, Classical.choice, Quot.sound]` |

Line counts (`wc -l`): `Dittert/Entropy.lean` 171, `Dittert/Entropy/Algebra.lean` 141,
`Dittert/Entropy/AMGM.lean` 171, `Dittert/Entropy/Minor.lean` 95, `AuditEntropy.lean` 3;
total 581.

A `grep` for `sorry`, `axiom`, `native_decide`, `decide +native`, `implemented_by`, `extern`
over the four new modules and `AuditEntropy.lean` finds only the `#print axioms` line of
`AuditEntropy.lean`.
