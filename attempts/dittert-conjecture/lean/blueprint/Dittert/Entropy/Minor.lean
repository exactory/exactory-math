/-
# Positivity of the complementary minors of a doubly stochastic matrix

For `M` doubly stochastic with `M i j > 0`, the permanent of the minor `M(i|j)` is positive.
Birkhoff–von Neumann (Mathlib `exists_eq_sum_perm_of_mem_doublyStochastic`) writes
`M = ∑_σ w_σ P_σ` with `w ≥ 0`; since `M i j > 0` some `σ` with `σ i = j` has `w_σ > 0`, and then
`M r (σ r) ≥ w_σ > 0` for every row `r`.  The map `c ↦ σ⁻¹ (j.succAbove c)` lands in the rows
`≠ i`, so it is `i.succAbove ∘ τ` for an injective, hence bijective, `τ : Fin k → Fin k`; the
`τ`-term of the permanent of the minor is `∏_c M (σ⁻¹ (j.succAbove c)) (j.succAbove c) > 0`, and
every term is nonnegative.
-/
import Mathlib.Tactic
import Mathlib.Analysis.Convex.Birkhoff
import Mathlib.LinearAlgebra.Matrix.Permanent

open Finset

namespace Dittert.Entropy

/-- The permanent of a nonnegative matrix is nonnegative. -/
theorem permanent_nonneg {n : Type*} [Fintype n] [DecidableEq n] {A : Matrix n n ℝ}
    (hA : ∀ i j, 0 ≤ A i j) : 0 ≤ A.permanent :=
  Finset.sum_nonneg fun _ _ => Finset.prod_nonneg fun _ _ => hA _ _

/-- The entry `(r, c)` of the permutation matrix of `σ`. -/
theorem permMatrix_apply' {n : Type*} [Fintype n] [DecidableEq n] (σ : Equiv.Perm n) (r c : n) :
    (σ.permMatrix ℝ) r c = if σ r = c then 1 else 0 := by
  show (σ.toPEquiv.toMatrix : Matrix n n ℝ) r c = _
  rw [PEquiv.toMatrix_apply, Equiv.toPEquiv_apply]
  simp only [Option.mem_def, Option.some.injEq]

/-- Every entry of a doubly stochastic matrix is `∑_σ w_σ [σ r = c]` for the Birkhoff weights. -/
theorem entry_eq_sum_perm {n : Type*} [Fintype n] [DecidableEq n] {M : Matrix n n ℝ}
    {w : Equiv.Perm n → ℝ} (hwM : ∑ σ, w σ • σ.permMatrix ℝ = M) (r c : n) :
    M r c = ∑ σ, w σ * (if σ r = c then 1 else 0) := by
  conv_lhs => rw [← hwM]
  rw [Matrix.sum_apply]
  refine Finset.sum_congr rfl fun σ _ => ?_
  rw [Matrix.smul_apply, smul_eq_mul, permMatrix_apply']

/-- **Positivity of the complementary minor.**  `M` doubly stochastic and `M i j > 0` give
`per M(i|j) > 0`. -/
theorem permanent_minor_pos {k : ℕ} {M : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ}
    (hM : M ∈ doublyStochastic ℝ (Fin (k + 1))) {i j : Fin (k + 1)} (hij : 0 < M i j) :
    0 < (M.submatrix i.succAbove j.succAbove).permanent := by
  classical
  obtain ⟨w, hw0, -, hwM⟩ := exists_eq_sum_perm_of_mem_doublyStochastic hM
  have hentry := entry_eq_sum_perm hwM
  -- a permutation through `(i, j)` with positive weight
  obtain ⟨σ, hσ, hwσ⟩ : ∃ σ : Equiv.Perm (Fin (k + 1)), σ i = j ∧ 0 < w σ := by
    by_contra hcon
    push Not at hcon
    have hzero : M i j = 0 := by
      rw [hentry]
      refine Finset.sum_eq_zero fun σ _ => ?_
      by_cases h : σ i = j
      · rw [if_pos h, mul_one]
        exact le_antisymm (hcon σ h) (hw0 σ)
      · rw [if_neg h, mul_zero]
    linarith
  -- every entry on the graph of `σ` is positive
  have hMσ : ∀ r, 0 < M r (σ r) := by
    intro r
    rw [hentry]
    refine lt_of_lt_of_le hwσ ?_
    have h := Finset.single_le_sum (s := univ)
      (f := fun σ' : Equiv.Perm (Fin (k + 1)) => w σ' * (if σ' r = σ r then 1 else 0))
      (fun σ' _ => mul_nonneg (hw0 σ') (by split_ifs <;> norm_num)) (Finset.mem_univ σ)
    simpa using h
  -- `σ⁻¹` sends the columns `≠ j` to the rows `≠ i`
  have hne : ∀ c : Fin k, σ.symm (j.succAbove c) ≠ i := by
    intro c h
    have h' : j.succAbove c = j := by
      calc j.succAbove c = σ (σ.symm (j.succAbove c)) := (σ.apply_symm_apply _).symm
        _ = σ i := by rw [h]
        _ = j := hσ
    exact Fin.succAbove_ne j c h'
  choose τ₀ hτ₀ using fun c : Fin k => Fin.exists_succAbove_eq (hne c)
  have hinj : Function.Injective τ₀ := by
    intro c₁ c₂ h
    have h1 : σ.symm (j.succAbove c₁) = σ.symm (j.succAbove c₂) := by
      rw [← hτ₀, ← hτ₀, h]
    exact Fin.succAbove_right_injective (σ.symm.injective h1)
  have hbij : Function.Bijective τ₀ := Finite.injective_iff_bijective.mp hinj
  -- the `τ`-term of the permanent is positive, and every term is nonnegative
  rw [Matrix.permanent]
  refine Finset.sum_pos' (fun τ' _ => Finset.prod_nonneg fun c _ =>
    nonneg_of_mem_doublyStochastic hM) ⟨Equiv.ofBijective τ₀ hbij, Finset.mem_univ _, ?_⟩
  refine Finset.prod_pos fun c _ => ?_
  show 0 < M (i.succAbove (τ₀ c)) (j.succAbove c)
  rw [hτ₀ c]
  have h := hMσ (σ.symm (j.succAbove c))
  rwa [σ.apply_symm_apply] at h

end Dittert.Entropy
