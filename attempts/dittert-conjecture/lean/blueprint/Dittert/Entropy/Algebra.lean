/-
# Algebraic identities for the entropy lemma

Built on the port `GurvitsPort` (DCPRevere/maths-pub, commit
0a1cb0a14fefe85668365d448f9bbaf4dd89d458, Apache-2.0; see `../../../maths-pub-port/PORT-NOTES.md`
and `AXIOMS.txt`).  No port file is modified.

The entropy lemma works with the polynomial

    Q = ∑ᵢ aᵢ ∏_{i' ≠ i} Lᵢ'      (Lᵢ' the row forms of a `(k+1) × k` matrix `B`),

which is the coefficient of `x₀` in `∏ᵢ (aᵢ x₀ + Lᵢ')`, that is, `GurvitsInduction.reduce` of the
row polynomial of the `(k+1) × (k+1)` matrix `extend a B` (column `0` equal to `a`, the other
columns those of `B`).  This file proves that identity (`reduce_rowPoly`) and its two
consequences: the top coefficient of `Q` is `∑ᵢ per(A(i|0)) aᵢ`, and the value of `Q` at `x` is
`∑ᵢ (∏ᵣ L_{i.succAbove r}(x)) aᵢ`.  As a by-product, the Laplace expansion of the permanent along
column `0` (`permanent_succ_column_zero`).
-/
import Mathlib.Tactic
import GurvitsPort.FaceBounds
import GurvitsPort.GurvitsInduction

open MvPolynomial Finset

namespace Dittert.Entropy

/-! ## §1  Products over the complement of a point of `Fin (k + 1)` -/

/-- A product over `univ.erase i` is a product over `i.succAbove`. -/
theorem prod_erase_eq_prod_succAbove {M : Type*} [CommMonoid M] {k : ℕ} (f : Fin (k + 1) → M)
    (i : Fin (k + 1)) : ∏ i' ∈ univ.erase i, f i' = ∏ r : Fin k, f (i.succAbove r) := by
  rw [Fin.univ_succAbove k i, Finset.erase_cons, Finset.prod_map, Fin.coe_succAboveEmb]

/-! ## §2  `finSuccEquiv` of a linear form -/

theorem finSuccEquiv_C' {k : ℕ} (r : ℝ) :
    finSuccEquiv ℝ k (C r) = Polynomial.C (C r) := by
  rw [finSuccEquiv_apply, eval₂Hom_C]
  rfl

/-- Under `finSuccEquiv`, the linear form `∑ c, a c x_c` becomes `C (∑ c, a c.succ x_c) + C (a 0) X`. -/
theorem finSuccEquiv_linForm {k : ℕ} (a : Fin (k + 1) → ℝ) :
    finSuccEquiv ℝ k (LorentzianPoly.linForm a)
      = Polynomial.C (LorentzianPoly.linForm (fun c => a c.succ))
        + Polynomial.C (C (a 0)) * Polynomial.X := by
  simp only [LorentzianPoly.linForm, Fin.sum_univ_succ, map_add, map_sum, map_mul,
    finSuccEquiv_C', finSuccEquiv_X_zero, finSuccEquiv_X_succ]
  ring

/-! ## §3  The `X`-coefficient of a product of linear polynomials -/

/-- `[X] ∏ᵢ (bᵢ + aᵢ X) = ∑ᵢ aᵢ ∏_{i' ≠ i} bᵢ'`, through the derivative at `0`. -/
theorem coeff_one_prod_linear {R : Type*} [CommRing R] {ι : Type*} [DecidableEq ι]
    (s : Finset ι) (b a : ι → R) :
    (∏ i ∈ s, (Polynomial.C (b i) + Polynomial.C (a i) * Polynomial.X)).coeff 1
      = ∑ i ∈ s, (∏ i' ∈ s.erase i, b i') * a i := by
  have h1 : ∀ p : Polynomial R, p.coeff 1 = (Polynomial.derivative p).eval 0 := by
    intro p
    rw [← Polynomial.coeff_zero_eq_eval_zero, Polynomial.coeff_derivative]
    simp
  rw [h1, Polynomial.derivative_prod_finset, Polynomial.eval_finsetSum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [Polynomial.eval_mul, Polynomial.eval_prod]
  simp

/-! ## §4  The extended matrix -/

/-- The `(k+1) × (k+1)` matrix whose column `0` is `a` and whose columns `c.succ` are the
columns of `B`. -/
def extend {k : ℕ} (a : Fin (k + 1) → ℝ) (B : Matrix (Fin (k + 1)) (Fin k) ℝ) :
    Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ :=
  Matrix.of fun i c => Fin.cases (a i) (fun c' => B i c') c

@[simp] theorem extend_zero {k : ℕ} (a : Fin (k + 1) → ℝ) (B : Matrix (Fin (k + 1)) (Fin k) ℝ)
    (i : Fin (k + 1)) : extend a B i 0 = a i := rfl

@[simp] theorem extend_succ {k : ℕ} (a : Fin (k + 1) → ℝ) (B : Matrix (Fin (k + 1)) (Fin k) ℝ)
    (i : Fin (k + 1)) (c : Fin k) : extend a B i c.succ = B i c := rfl

theorem extend_nonneg {k : ℕ} {a : Fin (k + 1) → ℝ} {B : Matrix (Fin (k + 1)) (Fin k) ℝ}
    (ha : ∀ i, 0 ≤ a i) (hB : ∀ i c, 0 ≤ B i c) : ∀ i c, 0 ≤ extend a B i c := by
  intro i c
  refine Fin.cases ?_ (fun c' => ?_) c
  · exact ha i
  · exact hB i c'

/-- The minor `(extend a B)(i | 0)` is the minor `B(i | ·)`. -/
theorem extend_submatrix {k : ℕ} (a : Fin (k + 1) → ℝ) (B : Matrix (Fin (k + 1)) (Fin k) ℝ)
    (i : Fin (k + 1)) :
    (extend a B).submatrix i.succAbove Fin.succ = B.submatrix i.succAbove id := rfl

/-! ## §5  `reduce` of the row polynomial -/

/-- The row polynomial of the minor `A(i | 0)` is the product of the row forms of the rows
`i.succAbove r`, with column `0` deleted. -/
theorem rowPoly_minor {k : ℕ} (A : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ) (i : Fin (k + 1)) :
    FaceBounds.rowPoly (A.submatrix i.succAbove Fin.succ)
      = ∏ r : Fin k, LorentzianPoly.linForm (fun c => A (i.succAbove r) c.succ) := rfl

/-- **The coefficient of `x₀` in the row polynomial.**
`reduce (∏ᵢ ⟨Aᵢ, x⟩) = ∑ᵢ (∏_{r} ⟨A_{i.succAbove r}, x'⟩) · A i 0`, where `x'` omits `x₀`. -/
theorem reduce_rowPoly {k : ℕ} (A : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ) :
    GurvitsInduction.reduce (FaceBounds.rowPoly A)
      = ∑ i, FaceBounds.rowPoly (A.submatrix i.succAbove Fin.succ) * C (A i 0) := by
  rw [GurvitsInduction.reduce, FaceBounds.rowPoly, map_prod]
  simp only [finSuccEquiv_linForm]
  rw [coeff_one_prod_linear]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [prod_erase_eq_prod_succAbove, rowPoly_minor]

/-- The top coefficient of `reduce (rowPoly A)` is `∑ᵢ per(A(i|0)) · A i 0`. -/
theorem coeff_topIdx_reduce_rowPoly {k : ℕ} (A : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ) :
    coeff (Gurvits.topIdx k) (GurvitsInduction.reduce (FaceBounds.rowPoly A))
      = ∑ i, (A.submatrix i.succAbove Fin.succ).permanent * A i 0 := by
  rw [reduce_rowPoly, MvPolynomial.coeff_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [mul_comm, MvPolynomial.coeff_C_mul, FaceBounds.coeff_topIdx_rowPoly, mul_comm]

/-- **Laplace expansion of the permanent along column `0`.** -/
theorem permanent_succ_column_zero {k : ℕ} (A : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ) :
    A.permanent = ∑ i, (A.submatrix i.succAbove Fin.succ).permanent * A i 0 := by
  rw [← FaceBounds.coeff_topIdx_rowPoly, ← GurvitsInduction.coeff_topIdx_reduce,
    coeff_topIdx_reduce_rowPoly]

/-- The value of `reduce (rowPoly A)` at `x`. -/
theorem eval_reduce_rowPoly {k : ℕ} (A : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ) (x : Fin k → ℝ) :
    eval x (GurvitsInduction.reduce (FaceBounds.rowPoly A))
      = ∑ i, (∏ r : Fin k, ∑ c, A (i.succAbove r) c.succ * x c) * A i 0 := by
  rw [reduce_rowPoly, map_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [map_mul, eval_C, FaceBounds.eval_rowPoly, Capacity.rowProd]
  rfl

/-- Nonnegative coefficients of `reduce (rowPoly A)` for `A ≥ 0`. -/
theorem coeff_reduce_rowPoly_nonneg {k : ℕ} {A : Matrix (Fin (k + 1)) (Fin (k + 1)) ℝ}
    (hA : ∀ i c, 0 ≤ A i c) (m : Fin k →₀ ℕ) :
    0 ≤ coeff m (GurvitsInduction.reduce (FaceBounds.rowPoly A)) := by
  rw [GurvitsInduction.coeff_reduce]
  exact FaceBounds.rowPoly_coeff_nonneg hA _

end Dittert.Entropy
