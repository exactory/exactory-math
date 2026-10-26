# Notes for `Dittert/Floors.lean` (the obligation `Dittert.gurvits_floors : GurvitsFloors`)

Status line: **complete** (2026-09-06). `Dittert.gurvits_floors : GurvitsFloors` is proved in
`Dittert/Floors.lean` with helpers `Dittert/Floors/Analytic.lean` and `Dittert/Floors/Chain.lean`;
`lake build +Dittert.Floors` succeeds and `#print axioms Dittert.gurvits_floors` reports
`[propext, Classical.choice, Quot.sound]` (see the build record at the end).

Provenance of the port used: DCPRevere/maths-pub, commit
`0a1cb0a14fefe85668365d448f9bbaf4dd89d458`, Apache-2.0, ported as the `GurvitsPort` library of
this project (see `../maths-pub-port/PORT-NOTES.md` and `../maths-pub-port/AXIOMS.txt`).

## Route (deviation from the brief, and why)

The brief plans: derivative closure through the port's `NonDegenerate` hypothesis, "which holds
because the capacity stays positive". That is not enough: `HStableOrbit.NonDegenerate p`
quantifies over complex points of the open right half-space, and positive capacity only gives
positive `x₀`-degree of the line restriction at positive real points. The port's own
unconditional theorem sidesteps this with a perturbation `psub e` that makes every top coefficient
positive, but that perturbation destroys the zero block, so the degree-refined constants of the
rectangle floor would be lost.

Route taken instead (all homogeneous, `reduce = ∂₀ · |_{x₀ = 0}` as in `GurvitsInduction`):

1. One analytic core lemma (`hstable_of_limit`): if `g ≠ 0` is the pointwise limit, as a real
   parameter `s → 0⁺`, of a jointly continuous family `F s` of functions that are polynomials
   along every complex line, and every `F s` (`s > 0`) is nonvanishing on the open right
   half-space, then `g` is H-stable. Proof: minimum modulus principle
   (`Complex.eventually_eq_or_eq_zero_of_isLocalMin_norm`) on a small closed disc of a complex
   line through a hypothetical zero, uniform closeness from Heine–Cantor on a compact set.
2. `restrict_zero_hstable`: `f` H-stable and `f|_{x₀ = 0} ≠ 0` gives `f|_{x₀ = 0}` H-stable
   (family `F s w = f(s, w)`, `s` a positive real, so the right half-space convention is kept).
3. `leadingCoeff_hstable`: `q` H-stable, `q ≠ 0` gives the leading `x₀`-coefficient H-stable
   (family `F s w = s^D q(1/s, w)`, the reversed expansion). This yields
   `nonDegenerate_of_natDegree_pos`: H-stable with positive `x₀`-degree implies
   `HStableOrbit.NonDegenerate`, the explicit non-degeneracy lemma the reviewer asked for.
4. `hstable_reduce`: `q` H-stable, `reduce q ≠ 0` gives `reduce q` H-stable, by 3 (through the
   port's `hstable_pderiv_of_nonDegenerate`) and then 2 applied to `∂₀ q`.
5. `chain`: the `h`-fold extraction with the degree-refined constants, tracking the J-degree bound
   `JDegBd` (total exponent of the first `h` variables at most `N`), which is preserved by `reduce`
   with `N ↦ N - 1`; the final `n - b` variables are handled by the port's `gurvitsBound`.
6. `rect_floor`: column permutation putting `J` first, `rowPoly` of the permuted matrix, the
   J-degree bound from the zero block, capacity `1` (LemmaB6), telescoping of the constants.

## Lemma table

| lemma | statement in words | status |
|---|---|---|
| `Floors.Analytic.eval_aeval_poly` | evaluating a polynomial-valued `aeval` at `t` is `aeval` at the evaluated substitution | proved (`lake env lean` clean, 2026-09-06) |
| `Floors.Analytic.continuous_aeval` | `w ↦ aeval w p` is continuous on `Fin k → ℂ` | proved |
| `Floors.Analytic.aeval_ofReal` | `aeval` at a real point is the cast of `eval` | proved |
| `Floors.Analytic.hstable_of_limit` | the analytic core lemma (item 1 above) | proved |
| `Floors.Analytic.coeff_lineRestrict` | coefficients of the port's `lineRestrict` are `aeval z` of the `x₀`-coefficients | proved |
| `Floors.Analytic.natDegree_lineRestrict_le` | its degree is at most the `x₀`-degree | proved |
| `Floors.Analytic.aeval_cons_eq_sum` | expansion of `aeval (Fin.cons t w) q` in powers of `t` | proved |
| `Floors.Analytic.restrict_zero_hstable` | item 2 | proved |
| `Floors.Analytic.leadingCoeff_hstable` | item 3 | proved |
| `Floors.Analytic.nonDegenerate_of_natDegree_pos` | positive `x₀`-degree gives `NonDegenerate` | proved |
| `Floors.Analytic.reduce_eq_coeff_zero_pderiv` | `reduce q` is the `x₀ = 0` restriction of `∂₀ q` | proved |
| `Floors.Analytic.hstable_reduce` | item 4 | proved |
| `Floors.Chain.jdeg`, `jdeg_add`, `jdeg_cons`, `jdeg_le_degree`, `jdeg_single_of_le` | J-degree of a multi-index, additivity, `Fin.cons` splitting, bound by total degree, value on a non-J unit vector | proved (`lake env lean` clean, 2026-09-06) |
| `Floors.Chain.JDegBd` | the J-degree bound predicate | defined |
| `Floors.Chain.natDegree_finSuccEquiv_le_of_jDegBd` | the `x₀`-degree is at most the J-degree bound | proved |
| `Floors.Chain.jDegBd_reduce`, `isHomogeneous_reduce` | invariants under `reduce` | proved |
| `Floors.Chain.Gc`, `Gc_nonneg`, `Gc_antitone` | the port's constant `G(d,1)` cast to `ℝ`, nonnegative, non-increasing | proved |
| `Floors.Chain.gamma_nonneg`, `gamma_pos`, `gamma_eq_prod` | `γ` is positive and equals `∏_{k<m} G(k+1)` | proved |
| `Floors.Chain.prod_Gc_ratio` | `∏_{i<b} G(m - i) = γ(m) / γ(m - b)` | proved |
| `Floors.Chain.chain` | item 5 | proved |
| `Floors.exists_perm_front` | a permutation of `Fin n` sending `{j < b}` onto `J` | proved (`lake env lean` clean, 2026-09-06) |
| `Floors.AvoidsJ`, `avoidsJ_one`, `avoidsJ_mul`, `avoidsJ_prod`, `avoidsJ_linForm` | "involves none of the first `h` variables", closed under products, holds for the zero-block rows | proved |
| `Floors.jDegBd_rowPoly` | the zero block gives the J-degree bound `n - I.card` for `rowPoly` | proved |
| `Floors.rect_floor` | item 6 | proved |
| `Dittert.gurvits_floors` | the obligation | proved (elaborates; build and axiom audit recorded below) |

## Port lemmas used

`Gurvits.HStable`, `Gurvits.topIdx`, `Capacity.cap` and API (`cap_le`, `le_cap`, `cap_nonneg`,
`cap_zero`), `OneVarCapacity.stone12`, `BorderPayment.G`, `BorderPayment.G_nonneg`,
`GurvitsInduction.{reduce, coeff_reduce, coeff_topIdx_reduce, eval_nonneg, eval_reduce_of_fac,
capOne_eq_cap, capOne_nonpos_of_const, cons_pos, G_antitone, prod_G_one}`,
`HStableFac.classFac_hstable`, `HStableDerivative.{lineRestrict, eval_lineRestrict,
finSuccEquiv_pderiv_zero, cons_re_pos}`, `HStableOrbit.{NonDegenerate,
hstable_pderiv_of_nonDegenerate}`, `HStableClass.{subMap, reduceAt_eq_bind₁}`,
`SlicedTower.{reduceAt_zero, degree_cons}`, `FaceBounds.{rowPoly, eval_rowPoly,
rowPoly_isHomogeneous, rowPoly_coeff_nonneg, hstable_rowPoly, coeff_topIdx_rowPoly}`,
`LorentzianPoly.{linForm, linForm_isHomogeneous}`, `LemmaB6.cap_rowProd_eq_one_of_doublyStochastic`,
`GurvitsUnconditional.{gurvitsBound, egorychev_falikman}`.

No port file is modified.

## Project changes outside the new modules

`lakefile.toml`: the `Dittert` library now declares `roots = ["Dittert", "Dittert.Floors"]`
(the only edit). `Dittert.lean`, `Dittert/Basic.lean`, `Dittert/Obligations.lean`,
`lake-manifest.json`, `lean-toolchain` and every `GurvitsPort/*.lean` file are untouched
(`diff -rq` against `../maths-pub-port/GurvitsPort`: only the absent `Audit.lean` differs).
`Dittert.lean` still carries its own `sorry` placeholder for `gurvits_floors`; it does not import
`Dittert.Floors`, so nothing imports both.

## Build record (2026-09-06, Lean v4.33.1, Mathlib 0df444a360eaa60ab8c11dca51a86af692955474)

| command (from `scratch/floors-work`, `lake` = `~/.elan/bin/lake`) | result |
|---|---|
| `lake env lean Dittert/Floors/Analytic.lean` | no errors, no warnings (after fixes to three proof steps) |
| `lake build +Dittert.Floors.Analytic` | `Built Dittert.Floors.Analytic (6.9s)`, `Build completed successfully (3425 jobs)` |
| `lake env lean Dittert/Floors/Chain.lean` | no errors, no warnings |
| `lake build +Dittert.Floors.Chain` | `Built Dittert.Floors.Chain (7.6s)`, `Build completed successfully (3450 jobs)` |
| `lake env lean Dittert/Floors.lean` | no errors, no warnings |
| `lake build +Dittert.Floors` | `Built Dittert.Floors (5.6s)`, `Build completed successfully (3452 jobs)` |
| `lake env lean AuditFloors.lean` | `'Dittert.gurvits_floors' depends on axioms: [propext, Classical.choice, Quot.sound]` |

Line counts (`wc -l`): `Dittert/Floors.lean` 225, `Dittert/Floors/Analytic.lean` 441,
`Dittert/Floors/Chain.lean` 253, `AuditFloors.lean` 3; total 922.

A `grep` for `sorry`, `axiom`, `native_decide`, `decide +native`, `implemented_by`, `extern`
over the three new modules finds nothing.
