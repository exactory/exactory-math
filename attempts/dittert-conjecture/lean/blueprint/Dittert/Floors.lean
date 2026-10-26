/-
# The Gurvits permanent floors: `Dittert.gurvits_floors : GurvitsFloors`

Provenance.  This module and its helpers `Dittert/Floors/Analytic.lean` and
`Dittert/Floors/Chain.lean` are built on the library `GurvitsPort`, a port of the Gurvits /
van der Waerden subset of D C P Revere's `maths-pub` Lean development
(https://github.com/DCPRevere/maths-pub, commit 0a1cb0a14fefe85668365d448f9bbaf4dd89d458,
Apache-2.0, see `LICENSE` and `NOTICE` in this project, and `../maths-pub-port/PORT-NOTES.md`,
`../maths-pub-port/AXIOMS.txt` for the port record).  No port file is modified.

Content.

1. `gamma n ≤ per B` for doubly stochastic `B` is the port's Egorychev–Falikman theorem
   (`GurvitsUnconditional.egorychev_falikman`).
2. The rectangle floor.  For a doubly stochastic `B` with an `a × b` zero block on rows `I` and
   columns `J` (`1 ≤ a`, `1 ≤ b`, `a + b ≤ n - 1`),

       gamma (n - a) * gamma (n - b) / gamma (n - a - b) ≤ per B .

   A column permutation moves `J` to the first `b` positions (`exists_perm_front`).  The row
   polynomial `p = ∏ᵢ ⟨Bᵢ, x⟩` of the permuted matrix is H-stable, homogeneous of degree `n`,
   has capacity `1` (LemmaB6), top coefficient `per B`, and, because the rows in `I` are free
   of the first `b` variables, the total exponent of those variables in every monomial is at most
   `n - a` (`jDegBd_rowPoly`).  `Chain.chain` extracts the `b` variables one at a time, paying
   `G(n - a - i)` at step `i`, and applies the port's `gurvitsBound` to the remaining `n - b`
   variables; the constants telescope to `gamma (n - a) / gamma (n - a - b)` (`prod_Gc_ratio`).
-/
import Mathlib.Tactic
import Dittert.Obligations
import Dittert.Floors.Chain
import GurvitsPort.FaceBounds
import GurvitsPort.LemmaB6
import GurvitsPort.GurvitsUnconditional

open MvPolynomial Finset

namespace Dittert

namespace Floors

/-! ## §1  A permutation moving `J` to the front -/

/-- For `J ⊆ Fin n` of cardinality `b` there is a permutation `σ` with `σ j ∈ J ↔ j < b`. -/
theorem exists_perm_front {n b : ℕ} {J : Finset (Fin n)} (hJ : J.card = b) (hbn : b ≤ n) :
    ∃ σ : Equiv.Perm (Fin n), ∀ j, σ j ∈ J ↔ j.val < b := by
  classical
  let e₀ : {j : Fin n // j.val < b} ≃ Fin b :=
    { toFun := fun j => ⟨j.1.val, j.2⟩
      invFun := fun i => ⟨⟨i.val, lt_of_lt_of_le i.2 hbn⟩, i.2⟩
      left_inv := fun j => by ext; rfl
      right_inv := fun i => by ext; rfl }
  have hcard₁ : Fintype.card {j : Fin n // j.val < b} = Fintype.card {j : Fin n // j ∈ J} := by
    rw [Fintype.card_congr e₀, Fintype.card_fin, Fintype.card_coe, hJ]
  have hcard₂ : Fintype.card {j : Fin n // ¬ j.val < b}
      = Fintype.card {j : Fin n // ¬ j ∈ J} := by
    rw [Fintype.card_subtype_compl, Fintype.card_subtype_compl, hcard₁]
  let e₁ : {j : Fin n // j.val < b} ≃ {j : Fin n // j ∈ J} := Fintype.equivOfCardEq hcard₁
  let e₂ : {j : Fin n // ¬ j.val < b} ≃ {j : Fin n // ¬ j ∈ J} := Fintype.equivOfCardEq hcard₂
  refine ⟨(Equiv.sumCompl (fun j : Fin n => j.val < b)).symm.trans
    ((Equiv.sumCongr e₁ e₂).trans (Equiv.sumCompl (fun j : Fin n => j ∈ J))), fun j => ?_⟩
  by_cases hj : j.val < b
  · have h1 : (Equiv.sumCompl (fun j : Fin n => j.val < b)).symm j = Sum.inl ⟨j, hj⟩ :=
      Equiv.sumCompl_symm_apply_of_pos (p := fun j : Fin n => j.val < b) hj
    simp only [Equiv.trans_apply, h1, Equiv.sumCongr_apply, Sum.map_inl,
      Equiv.sumCompl_apply_inl]
    exact ⟨fun _ => hj, fun _ => (e₁ ⟨j, hj⟩).2⟩
  · have h1 : (Equiv.sumCompl (fun j : Fin n => j.val < b)).symm j = Sum.inr ⟨j, hj⟩ :=
      Equiv.sumCompl_symm_apply_of_neg (p := fun j : Fin n => j.val < b) hj
    simp only [Equiv.trans_apply, h1, Equiv.sumCongr_apply, Sum.map_inr,
      Equiv.sumCompl_apply_inr]
    exact ⟨fun h => absurd h (e₂ ⟨j, hj⟩).2, fun h => absurd h hj⟩

/-! ## §2  The J-degree bound of the row polynomial of a zero-block matrix -/

/-- `p` involves none of the first `h` variables. -/
def AvoidsJ {k : ℕ} (h : ℕ) (p : MvPolynomial (Fin k) ℝ) : Prop :=
  ∀ μ : Fin k →₀ ℕ, 0 < Chain.jdeg h μ → coeff μ p = 0

theorem avoidsJ_one {k : ℕ} (h : ℕ) : AvoidsJ h (1 : MvPolynomial (Fin k) ℝ) := by
  intro μ hμ
  rw [MvPolynomial.coeff_one]
  split_ifs with h0
  · subst h0
    simp [Chain.jdeg] at hμ
  · rfl

theorem avoidsJ_mul {k : ℕ} {h : ℕ} {p q : MvPolynomial (Fin k) ℝ} (hp : AvoidsJ h p)
    (hq : AvoidsJ h q) : AvoidsJ h (p * q) := by
  intro μ hμ
  rw [MvPolynomial.coeff_mul]
  refine Finset.sum_eq_zero fun x hx => ?_
  rw [Finset.mem_antidiagonal] at hx
  have hadd : Chain.jdeg h x.1 + Chain.jdeg h x.2 = Chain.jdeg h μ := by
    rw [← Chain.jdeg_add, hx]
  rcases Nat.eq_zero_or_pos (Chain.jdeg h x.1) with h1 | h1
  · rw [hq x.2 (by omega), mul_zero]
  · rw [hp x.1 h1, zero_mul]

theorem avoidsJ_prod {k : ℕ} {h : ℕ} {ι : Type*} (s : Finset ι) (f : ι → MvPolynomial (Fin k) ℝ)
    (hf : ∀ i ∈ s, AvoidsJ h (f i)) : AvoidsJ h (∏ i ∈ s, f i) := by
  classical
  induction s using Finset.induction with
  | empty => simpa using avoidsJ_one h
  | insert a s ha ih =>
    rw [Finset.prod_insert ha]
    exact avoidsJ_mul (hf a (Finset.mem_insert_self _ _))
      (ih fun i hi => hf i (Finset.mem_insert_of_mem hi))

/-- A linear form whose coefficients on the first `h` variables vanish avoids them. -/
theorem avoidsJ_linForm {k : ℕ} {h : ℕ} {c : Fin k → ℝ} (hc : ∀ j : Fin k, j.val < h → c j = 0) :
    AvoidsJ h (LorentzianPoly.linForm c) := by
  intro μ hμ
  rw [LorentzianPoly.linForm, MvPolynomial.coeff_sum]
  refine Finset.sum_eq_zero fun j _ => ?_
  rw [MvPolynomial.C_mul_X_eq_monomial, MvPolynomial.coeff_monomial]
  split_ifs with hjμ
  · by_cases hj : j.val < h
    · exact hc j hj
    · exfalso
      rw [← hjμ, Chain.jdeg_single_of_le (not_lt.mp hj)] at hμ
      exact lt_irrefl 0 hμ
  · rfl

/-- **The J-degree bound from the zero block.**  If the rows in `I` vanish on the first `b`
columns, every monomial of `rowPoly M` has exponent at most `n - I.card` on the first `b`
variables: the factors indexed by `I` avoid those variables and the other factors have total
degree `n - I.card`. -/
theorem jDegBd_rowPoly {n : ℕ} (M : Matrix (Fin n) (Fin n) ℝ) (I : Finset (Fin n)) (b : ℕ)
    (hz : ∀ i ∈ I, ∀ j : Fin n, j.val < b → M i j = 0) :
    Chain.JDegBd b (n - I.card) (FaceBounds.rowPoly M) := by
  classical
  intro m hm
  have hsplit : FaceBounds.rowPoly M
      = (∏ i ∈ I, LorentzianPoly.linForm (M i)) * ∏ i ∈ Iᶜ, LorentzianPoly.linForm (M i) := by
    rw [FaceBounds.rowPoly, Finset.prod_mul_prod_compl]
  have hP : AvoidsJ b (∏ i ∈ I, LorentzianPoly.linForm (M i)) :=
    avoidsJ_prod I _ fun i hi => avoidsJ_linForm fun j hj => hz i hi j hj
  have hR : (∏ i ∈ Iᶜ, LorentzianPoly.linForm (M i)).IsHomogeneous (n - I.card) := by
    have h := MvPolynomial.IsHomogeneous.prod Iᶜ (fun i => LorentzianPoly.linForm (M i))
      (fun _ => 1) (fun i _ => LorentzianPoly.linForm_isHomogeneous (M i))
    have hcard : ∑ i ∈ Iᶜ, (1 : ℕ) = n - I.card := by
      rw [Finset.sum_const, smul_eq_mul, mul_one, Finset.card_compl, Fintype.card_fin]
    rwa [hcard] at h
  rw [hsplit, MvPolynomial.coeff_mul]
  refine Finset.sum_eq_zero fun x hx => ?_
  rw [Finset.mem_antidiagonal] at hx
  rcases Nat.eq_zero_or_pos (Chain.jdeg b x.1) with h1 | h1
  · have h2 : Chain.jdeg b x.2 = Chain.jdeg b m := by
      rw [← hx, Chain.jdeg_add, h1, zero_add]
    have h3 : x.2.degree ≠ n - I.card := by
      have := Chain.jdeg_le_degree b x.2
      omega
    rw [hR.coeff_eq_zero h3, mul_zero]
  · rw [hP x.1 h1, zero_mul]

/-! ## §3  The rectangle floor -/

/-- **The rectangle floor.**  For `B` with non-negative entries, row and column sums `1`, and a
zero block on the rows `I` (`I.card = a ≥ 1`) and the columns `J` (`J.card = b ≥ 1`) with
`a + b ≤ n - 1`:  `gamma (n - a) * gamma (n - b) / gamma (n - a - b) ≤ per B`. -/
theorem rect_floor {n : ℕ} {B : Matrix (Fin n) (Fin n) ℝ} (hB : ∀ i j, 0 ≤ B i j)
    (hrow : ∀ i, ∑ j, B i j = 1) (hcol : ∀ j, ∑ i, B i j = 1) {a b : ℕ} (ha : 1 ≤ a)
    (hb : 1 ≤ b) (hab : a + b ≤ n - 1) {I J : Finset (Fin n)} (hI : I.card = a) (hJ : J.card = b)
    (hz : HasZeroBlock B I J) :
    gamma (n - a) * gamma (n - b) / gamma (n - a - b) ≤ B.permanent := by
  classical
  have hbn : b ≤ n := by omega
  obtain ⟨σ, hσ⟩ := exists_perm_front hJ hbn
  -- the permuted matrix: columns `J` first
  set B' : Matrix (Fin n) (Fin n) ℝ := B.submatrix id σ with hB'def
  have hB' : ∀ i j, 0 ≤ B' i j := fun i j => hB i (σ j)
  have hrow' : ∀ i, ∑ j, B' i j = 1 := fun i =>
    (Equiv.sum_comp σ (fun j => B i j)).trans (hrow i)
  have hcol' : ∀ j, ∑ i, B' i j = 1 := fun j => hcol (σ j)
  have hper : B'.permanent = B.permanent := Matrix.permanent_permute_rows σ B
  have hz' : ∀ i ∈ I, ∀ j : Fin n, j.val < b → B' i j = 0 := fun i hi j hj =>
    hz i hi (σ j) ((hσ j).mpr hj)
  have hpos' : ∀ i, ∃ j, 0 < B' i j := by
    intro i
    by_contra hcon
    rw [not_exists] at hcon
    replace hcon : ∀ j, B' i j ≤ 0 := fun j => not_lt.mp (hcon j)
    have hz0 : (∑ j, B' i j) = 0 :=
      le_antisymm (Finset.sum_nonpos fun j _ => hcon j) (Finset.sum_nonneg fun j _ => hB' i j)
    rw [hrow' i] at hz0
    norm_num at hz0
  -- the row polynomial and its invariants
  set q := FaceBounds.rowPoly B' with hqdef
  have hst : Gurvits.HStable q := FaceBounds.hstable_rowPoly hB' hpos'
  have hhom : q.IsHomogeneous n := FaceBounds.rowPoly_isHomogeneous B'
  have hnn : ∀ m, 0 ≤ coeff m q := FaceBounds.rowPoly_coeff_nonneg hB'
  have hJq : Chain.JDegBd b (n - a) q := by
    have := jDegBd_rowPoly B' I b hz'
    rwa [hI] at this
  have hcap : Capacity.cap (fun _ => (1 : ℝ)) (fun x : Fin n → ℝ => eval x q) = 1 := by
    have heq : (fun x : Fin n → ℝ => eval x q) = Capacity.rowProd B' :=
      funext (FaceBounds.eval_rowPoly B')
    rw [heq]
    exact LemmaB6.cap_rowProd_eq_one_of_doublyStochastic B' hB' hrow' hcol'
  have htop : coeff (Gurvits.topIdx n) q = B.permanent := by
    rw [hqdef, FaceBounds.coeff_topIdx_rowPoly, hper]
  -- the chain, then the telescoping of the constants
  have hmain := Chain.chain b n (n - a) q hbn (by omega) (Or.inr hst) hhom hnn hJq
  rw [hcap, mul_one, htop, Chain.prod_Gc_ratio (by omega : b ≤ n - a)] at hmain
  calc gamma (n - a) * gamma (n - b) / gamma (n - a - b)
      = gamma (n - a) / gamma (n - a - b) * gamma (n - b) := by ring
    _ ≤ B.permanent := hmain

end Floors

/-- **The Gurvits permanent floors** (`Dittert.Obligations.GurvitsFloors`): van der Waerden's
bound `gamma n ≤ per B`, and the rectangular zero-block floor
`gamma (n - a) * gamma (n - b) / gamma (n - a - b) ≤ per B`, for doubly stochastic `B`. -/
theorem gurvits_floors : GurvitsFloors := by
  intro n _ B hB
  have hB0 : ∀ i j, 0 ≤ B i j := fun i j => nonneg_of_mem_doublyStochastic hB
  have hrow := sum_row_of_mem_doublyStochastic hB
  have hcol := sum_col_of_mem_doublyStochastic hB
  refine ⟨?_, ?_⟩
  · unfold gamma
    exact GurvitsUnconditional.egorychev_falikman hB0 hrow hcol
  · intro a b ha hb hab I J hI hJ hz
    exact Floors.rect_floor hB0 hrow hcol ha hb hab hI hJ hz

end Dittert
