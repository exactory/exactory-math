/-
# The complementary-minor entropy lemma: `Dittert.core_entropy : CoreEntropy`

Provenance.  This module and its helpers `Dittert/Entropy/Algebra.lean`,
`Dittert/Entropy/AMGM.lean` and `Dittert/Entropy/Minor.lean` are built on the library
`GurvitsPort`, a port of the Gurvits / van der Waerden subset of D C P Revere's `maths-pub` Lean
development (https://github.com/DCPRevere/maths-pub, commit
0a1cb0a14fefe85668365d448f9bbaf4dd89d458, Apache-2.0, see `LICENSE` and `NOTICE` in this
project, and `../maths-pub-port/PORT-NOTES.md`, `../maths-pub-port/AXIOMS.txt` for the port
record).  No port file is modified.  The floors modules `Dittert/Floors/Analytic.lean`
(`hstable_reduce`, which is the port's derivative closure on the explicit
`nonDegenerate_of_natDegree_pos` followed by `restrict_zero_hstable`) and
`Dittert/Floors/Chain.lean` (`isHomogeneous_reduce`, `gamma_nonneg`) are reused as they stand.

Content.  For `M` doubly stochastic of order `k + 1` and a column `j`, with `q i = M i j` and
`d i = per M(i|j)`:

    gamma k * ∏ i, (1 - q i) ^ (1 - q i) ≤ ∏ i, d i ^ q i        (real powers, `0 ^ 0 = 1`).

Route.  `B` is `M` with column `j` deleted, `t i = (d i)⁻¹` when `q i > 0` and `1` otherwise.
`Q = reduce (rowPoly (extend (q * t) B))` is the coefficient of `x₀` in the product of the
nonzero nonnegative linear forms `(q i t i) x₀ + ⟨B i, x⟩`, hence H-stable when nonzero
(`Floors.Analytic.hstable_reduce`), homogeneous of degree `k`, with nonnegative coefficients and
top coefficient `∑ i, d i (q i t i) = ∑ i, q i = 1` (`Entropy.coeff_topIdx_reduce_rowPoly`).
Weighted AM–GM at every positive `x` gives `cap Q ≥ (∏ t ^ q) (∏ (1 - q) ^ (1 - q))`
(`Entropy.cap_lower_bound`), Gurvits gives `gamma k * cap Q ≤ 1`
(`GurvitsUnconditional.gurvitsBound`), and `∏ t ^ q = (∏ d ^ q)⁻¹` rearranges to the claim;
`d i > 0` when `q i > 0` is Birkhoff–von Neumann (`Entropy.permanent_minor_pos`).
-/
import Mathlib.Tactic
import Dittert.Obligations
import Dittert.Floors.Analytic
import Dittert.Floors.Chain
import Dittert.Entropy.Algebra
import Dittert.Entropy.AMGM
import Dittert.Entropy.Minor
import GurvitsPort.FaceBounds
import GurvitsPort.GurvitsUnconditional

open MvPolynomial Finset

namespace Dittert

namespace Entropy

/-! ## §1  H-stability and Gurvits for `Q = reduce (rowPoly (extend a B))` -/

/-- The row polynomial of the extended matrix is H-stable when every row has a positive entry. -/
theorem hstable_rowPoly_extend {k : ℕ} {a : Fin (k + 1) → ℝ} {B : Matrix (Fin (k + 1)) (Fin k) ℝ}
    (ha : ∀ i, 0 ≤ a i) (hB : ∀ i c, 0 ≤ B i c) (hpos : ∀ i, 0 < a i ∨ ∃ c, 0 < B i c) :
    Gurvits.HStable (FaceBounds.rowPoly (extend a B)) := by
  refine FaceBounds.hstable_rowPoly (extend_nonneg ha hB) fun i => ?_
  rcases hpos i with h | ⟨c, hc⟩
  · exact ⟨0, by simpa using h⟩
  · exact ⟨c.succ, by simpa using hc⟩

/-- **Gurvits for `Q`.**  `gamma k * cap Q ≤ ∑ i, per ((extend a B)(i|0)) * a i`.  When `Q = 0`
both sides vanish; otherwise `Q` is H-stable by the floors closure lemma `hstable_reduce`,
homogeneous of degree `k` with nonnegative coefficients, and the port's `gurvitsBound` applies. -/
theorem gurvits_reduce {k : ℕ} {a : Fin (k + 1) → ℝ} {B : Matrix (Fin (k + 1)) (Fin k) ℝ}
    (ha : ∀ i, 0 ≤ a i) (hB : ∀ i c, 0 ≤ B i c) (hpos : ∀ i, 0 < a i ∨ ∃ c, 0 < B i c) :
    gamma k * Capacity.cap (fun _ => (1 : ℝ)) (fun x : Fin k → ℝ =>
        eval x (GurvitsInduction.reduce (FaceBounds.rowPoly (extend a B))))
      ≤ ∑ i, ((extend a B).submatrix i.succAbove Fin.succ).permanent * a i := by
  have htop := coeff_topIdx_reduce_rowPoly (extend a B)
  simp only [extend_zero] at htop
  rw [← htop]
  have hhom : (GurvitsInduction.reduce (FaceBounds.rowPoly (extend a B))).IsHomogeneous k :=
    Floors.Chain.isHomogeneous_reduce (FaceBounds.rowPoly_isHomogeneous _)
  have hnn := coeff_reduce_rowPoly_nonneg (extend_nonneg ha hB)
  rcases eq_or_ne (GurvitsInduction.reduce (FaceBounds.rowPoly (extend a B))) 0 with h0 | hne
  · rw [h0]
    simp only [map_zero, Capacity.cap_zero, mul_zero, MvPolynomial.coeff_zero, le_refl]
  · have hst := Floors.Analytic.hstable_reduce (hstable_rowPoly_extend ha hB hpos) hne
    unfold gamma
    exact GurvitsUnconditional.gurvitsBound k _ hhom hnn hst

end Entropy

/-! ## §2  The obligation -/

/-- **The complementary-minor entropy lemma** (`Dittert.Obligations.CoreEntropy`): for `M`
doubly stochastic of order `k + 1` and a column `j`,
`gamma k * ∏ i, (1 - M i j) ^ (1 - M i j) ≤ ∏ i, per M(i|j) ^ (M i j)`. -/
theorem core_entropy : CoreEntropy := by
  intro k _ M hM j
  classical
  have hM0 : ∀ i c, 0 ≤ M i c := fun i c => nonneg_of_mem_doublyStochastic hM
  have hrow := sum_row_of_mem_doublyStochastic hM
  have hcol := sum_col_of_mem_doublyStochastic hM
  -- the data: the weights `q`, the minors `d`, and `M` with column `j` deleted
  set q : Fin (k + 1) → ℝ := fun i => M i j with hqdef
  set d : Fin (k + 1) → ℝ := fun i => (M.submatrix i.succAbove j.succAbove).permanent with hddef
  set B : Matrix (Fin (k + 1)) (Fin k) ℝ := fun i c => M i (j.succAbove c) with hBdef
  have hq0 : ∀ i, 0 ≤ q i := fun i => hM0 i j
  have hq1 : ∑ i, q i = 1 := hcol j
  have hB0 : ∀ i c, 0 ≤ B i c := fun i c => hM0 _ _
  have hBrow : ∀ i, ∑ c, B i c = 1 - q i := by
    intro i
    have h := hrow i
    rw [Fin.sum_univ_succAbove _ j] at h
    show ∑ c, M i (j.succAbove c) = 1 - M i j
    linarith
  have hBcol : ∀ c, ∑ i, B i c = 1 := fun c => hcol (j.succAbove c)
  have hd0 : ∀ i, 0 ≤ d i := fun i => Entropy.permanent_nonneg fun r c => hM0 _ _
  have hdpos : ∀ i, 0 < q i → 0 < d i := fun i hi => Entropy.permanent_minor_pos hM hi
  have hqz : ∀ i, ¬ 0 < q i → q i = 0 := fun i h => le_antisymm (not_lt.mp h) (hq0 i)
  -- the weights `t`
  set t : Fin (k + 1) → ℝ := fun i => if 0 < q i then (d i)⁻¹ else 1 with htdef
  have ht : ∀ i, 0 < t i := by
    intro i
    simp only [htdef]
    split_ifs with h
    · exact inv_pos.mpr (hdpos i h)
    · exact one_pos
  -- every row of `M` has a positive entry: either `q i > 0` or some `B i c > 0`
  have hpos : ∀ i, 0 < q i * t i ∨ ∃ c, 0 < B i c := by
    intro i
    by_cases hqi : 0 < q i
    · exact Or.inl (mul_pos hqi (ht i))
    · right
      by_contra hcon
      push Not at hcon
      have hz : ∑ c, B i c = 0 :=
        le_antisymm (Finset.sum_nonpos fun c _ => hcon c) (Finset.sum_nonneg fun c _ => hB0 i c)
      rw [hBrow i, hqz i hqi] at hz
      norm_num at hz
  -- the capacity bound (AM–GM) and Gurvits
  have hcap := Entropy.cap_lower_bound B q t hB0 hq0 hq1 hBrow hBcol ht
  have hgur := Entropy.gurvits_reduce (a := fun i => q i * t i) (B := B)
    (fun i => mul_nonneg (hq0 i) (ht i).le) hB0 hpos
  have hminor : ∀ i, ((Entropy.extend (fun i => q i * t i) B).submatrix
      i.succAbove Fin.succ).permanent = d i := fun i => rfl
  simp only [hminor] at hgur
  -- the choice of `t`: the right side of Gurvits is `∑ q = 1`
  have hsum : ∑ i, d i * (q i * t i) = 1 := by
    rw [← hq1]
    refine Finset.sum_congr rfl fun i _ => ?_
    simp only [htdef]
    split_ifs with h
    · rw [mul_comm (q i), ← mul_assoc, mul_inv_cancel₀ (hdpos i h).ne', one_mul]
    · rw [hqz i h]
      ring
  rw [hsum] at hgur
  -- and `∏ t ^ q = (∏ d ^ q)⁻¹`
  have hprod : ∏ i, t i ^ q i = (∏ i, d i ^ q i)⁻¹ := by
    rw [← Finset.prod_inv_distrib]
    refine Finset.prod_congr rfl fun i _ => ?_
    simp only [htdef]
    split_ifs with h
    · exact Real.inv_rpow (hd0 i) _
    · rw [hqz i h, Real.rpow_zero, Real.rpow_zero, inv_one]
  rw [hprod] at hcap
  have hdq : 0 < ∏ i, d i ^ q i := by
    refine Finset.prod_pos fun i _ => ?_
    by_cases h : 0 < q i
    · exact Real.rpow_pos_of_pos (hdpos i h) _
    · rw [hqz i h]
      exact Real.rpow_zero_pos _
  -- assemble
  have hmain : gamma k * ((∏ i, d i ^ q i)⁻¹ * ∏ i, (1 - q i) ^ (1 - q i)) ≤ 1 :=
    (mul_le_mul_of_nonneg_left hcap (Floors.Chain.gamma_nonneg k)).trans hgur
  have hmain' : (gamma k * ∏ i, (1 - q i) ^ (1 - q i)) / ∏ i, d i ^ q i ≤ 1 := by
    have heq : (gamma k * ∏ i, (1 - q i) ^ (1 - q i)) / ∏ i, d i ^ q i
        = gamma k * ((∏ i, d i ^ q i)⁻¹ * ∏ i, (1 - q i) ^ (1 - q i)) := by ring
    rw [heq]
    exact hmain
  show gamma k * ∏ i, (1 - q i) ^ (1 - q i) ≤ ∏ i, d i ^ q i
  exact (div_le_one hdq).mp hmain'

end Dittert
