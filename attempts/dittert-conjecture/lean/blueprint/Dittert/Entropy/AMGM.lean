/-
# The weighted AM–GM bounds of the entropy lemma

Built on the port `GurvitsPort` (DCPRevere/maths-pub, commit
0a1cb0a14fefe85668365d448f9bbaf4dd89d458, Apache-2.0; see `../../../maths-pub-port/PORT-NOTES.md`
and `AXIOMS.txt`).  No port file is modified.

For a `(k+1) × k` matrix `B ≥ 0` with row sums `1 - q i` and column sums `1`, weights `q ≥ 0`
summing to `1`, and positive `t`, the polynomial `Q(x) = ∑ᵢ (∏ᵣ L_{i.succAbove r}(x)) (qᵢ tᵢ)`
(with `Lᵢ(x) = ∑_c B i c x_c`) satisfies, at every positive `x`,

    (∏ᵢ tᵢ ^ qᵢ) (∏ᵢ (1 - qᵢ) ^ (1 - qᵢ)) ∏_c x_c ≤ Q(x) .

Two applications of `Real.geom_mean_le_arith_mean_weighted`: weights `q` over the rows
(`column_amgm`), then weights `B i c / (1 - q i)` inside each row form (`row_amgm`, where a row
with `1 - q i = 0` contributes `1 = 0 ^ 0` on both sides).  The column sums turn
`∏ᵢ ∏_c x_c ^ B i c` into `∏_c x_c`, so no normalisation of `x` is needed, and `Capacity.le_cap`
turns the pointwise bound into a lower bound for the capacity (`cap_lower_bound`).
-/
import Mathlib.Tactic
import Mathlib.Analysis.MeanInequalities
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import GurvitsPort.Capacity
import Dittert.Entropy.Algebra

open MvPolynomial Finset

namespace Dittert.Entropy

/-! ## §1  One row -/

/-- **Row AM–GM.**  For `b ≥ 0` with sum `s` and `x > 0`: `s ^ s ∏_c x_c ^ b_c ≤ (∑_c b_c x_c) ^ s`.
When `s = 0` every `b_c` vanishes and both sides are `1`. -/
theorem row_amgm {k : ℕ} (b : Fin k → ℝ) (hb : ∀ c, 0 ≤ b c) (x : Fin k → ℝ)
    (hx : ∀ c, 0 < x c) :
    (∑ c, b c) ^ (∑ c, b c) * ∏ c, x c ^ b c ≤ (∑ c, b c * x c) ^ (∑ c, b c) := by
  set s := ∑ c, b c with hs
  have hs0 : 0 ≤ s := Finset.sum_nonneg fun c _ => hb c
  rcases eq_or_lt_of_le hs0 with h0 | hpos
  · have hb0 : ∀ c, b c = 0 := fun c =>
      (Finset.sum_eq_zero_iff_of_nonneg fun c _ => hb c).mp h0.symm c (Finset.mem_univ c)
    rw [← h0]
    simp [hb0]
  · have hw : ∀ c ∈ (univ : Finset (Fin k)), 0 ≤ b c / s := fun c _ => div_nonneg (hb c) hs0
    have hw' : ∑ c, b c / s = 1 := by
      rw [← Finset.sum_div, div_self hpos.ne']
    have key := Real.geom_mean_le_arith_mean_weighted univ (fun c => b c / s) x hw hw'
      (fun c _ => (hx c).le)
    have hsum : ∑ c, b c / s * x c = (∑ c, b c * x c) / s := by
      rw [Finset.sum_div]
      exact Finset.sum_congr rfl fun c _ => by ring
    rw [hsum] at key
    have hL0 : 0 ≤ ∏ c, x c ^ (b c / s) :=
      Finset.prod_nonneg fun c _ => Real.rpow_nonneg (hx c).le _
    have key2 := Real.rpow_le_rpow hL0 key hs0
    have hLHS : (∏ c, x c ^ (b c / s)) ^ s = ∏ c, x c ^ b c := by
      rw [← Real.finsetProd_rpow _ _ (fun c _ => Real.rpow_nonneg (hx c).le _)]
      refine Finset.prod_congr rfl fun c _ => ?_
      rw [← Real.rpow_mul (hx c).le, div_mul_cancel₀ _ hpos.ne']
    have hsumnn : 0 ≤ ∑ c, b c * x c :=
      Finset.sum_nonneg fun c _ => mul_nonneg (hb c) (hx c).le
    rw [hLHS, Real.div_rpow hsumnn hs0, le_div_iff₀ (Real.rpow_pos_of_pos hpos s)] at key2
    linarith [key2]

/-- **All rows, with the column sums.**  `(∏ᵢ sᵢ ^ sᵢ) ∏_c x_c ≤ ∏ᵢ Lᵢ(x) ^ sᵢ` where
`sᵢ = ∑_c B i c` and every column of `B` sums to `1`. -/
theorem rows_amgm {k : ℕ} (B : Matrix (Fin (k + 1)) (Fin k) ℝ) (hB : ∀ i c, 0 ≤ B i c)
    (hcol : ∀ c, ∑ i, B i c = 1) (x : Fin k → ℝ) (hx : ∀ c, 0 < x c) :
    (∏ i, (∑ c, B i c) ^ (∑ c, B i c)) * ∏ c, x c
      ≤ ∏ i, (∑ c, B i c * x c) ^ (∑ c, B i c) := by
  have hprod : ∏ i, ∏ c, x c ^ B i c = ∏ c, x c := by
    rw [Finset.prod_comm]
    refine Finset.prod_congr rfl fun c _ => ?_
    rw [← Real.rpow_sum_of_nonneg (hx c).le (fun i _ => hB i c), hcol c, Real.rpow_one]
  rw [← hprod, ← Finset.prod_mul_distrib]
  refine Finset.prod_le_prod (fun i _ => ?_) (fun i _ => row_amgm (B i) (hB i) x hx)
  exact mul_nonneg (Real.rpow_nonneg (Finset.sum_nonneg fun c _ => hB i c) _)
    (Finset.prod_nonneg fun c _ => Real.rpow_nonneg (hx c).le _)

/-! ## §2  The rows, weighted by the column `q` -/

/-- A product over `i.succAbove` is a product over all indices with exponent `0` at `i`. -/
theorem prod_succAbove_eq_prod_rpow {k : ℕ} (f : Fin (k + 1) → ℝ) (i : Fin (k + 1)) :
    ∏ r : Fin k, f (i.succAbove r) = ∏ i', f i' ^ (if i' = i then (0 : ℝ) else 1) := by
  rw [Fin.prod_univ_succAbove (fun i' => f i' ^ (if i' = i then (0 : ℝ) else 1)) i,
    if_pos rfl, Real.rpow_zero, one_mul]
  refine Finset.prod_congr rfl fun r _ => ?_
  rw [if_neg (Fin.succAbove_ne i r), Real.rpow_one]

/-- `∑ᵢ (1 - [i = i']) qᵢ = 1 - q i'` when `∑ q = 1`. -/
theorem sum_weights {k : ℕ} (q : Fin (k + 1) → ℝ) (hq1 : ∑ i, q i = 1) (i' : Fin (k + 1)) :
    ∑ i, (if i' = i then (0 : ℝ) else 1) * q i = 1 - q i' := by
  have h : ∀ i, (if i' = i then (0 : ℝ) else 1) * q i = q i - (if i' = i then q i else 0) := by
    intro i
    split_ifs <;> ring
  simp only [h, Finset.sum_sub_distrib, hq1, Finset.sum_ite_eq, Finset.mem_univ, if_true]

/-- **Column AM–GM.**  With weights `q` (nonnegative, sum `1`) and positive `t`:
`(∏ᵢ tᵢ ^ qᵢ) ∏ᵢ' Lᵢ' ^ (1 - qᵢ') ≤ ∑ᵢ (∏ᵣ L_{i.succAbove r}) (qᵢ tᵢ)` for `L ≥ 0`. -/
theorem column_amgm {k : ℕ} (q t : Fin (k + 1) → ℝ) (hq : ∀ i, 0 ≤ q i) (hq1 : ∑ i, q i = 1)
    (ht : ∀ i, 0 < t i) (L : Fin (k + 1) → ℝ) (hL : ∀ i, 0 ≤ L i) :
    (∏ i, t i ^ q i) * ∏ i', L i' ^ (1 - q i')
      ≤ ∑ i, (∏ r : Fin k, L (i.succAbove r)) * (q i * t i) := by
  have hP : ∀ i : Fin (k + 1), 0 ≤ ∏ r : Fin k, L (i.succAbove r) :=
    fun i => Finset.prod_nonneg fun r _ => hL _
  have key := Real.geom_mean_le_arith_mean_weighted univ q
    (fun i : Fin (k + 1) => t i * ∏ r : Fin k, L (i.succAbove r)) (fun i _ => hq i) hq1
    (fun i _ => mul_nonneg (ht i).le (hP i))
  have hR : ∑ i : Fin (k + 1), q i * (t i * ∏ r : Fin k, L (i.succAbove r))
      = ∑ i : Fin (k + 1), (∏ r : Fin k, L (i.succAbove r)) * (q i * t i) :=
    Finset.sum_congr rfl fun i _ => by ring
  have h1 : ∀ i : Fin (k + 1), (t i * ∏ r : Fin k, L (i.succAbove r)) ^ q i
      = t i ^ q i * ∏ i', L i' ^ ((if i' = i then (0 : ℝ) else 1) * q i) := by
    intro i
    rw [Real.mul_rpow (ht i).le (hP i), prod_succAbove_eq_prod_rpow L i,
      ← Real.finsetProd_rpow _ _ (fun i' _ => Real.rpow_nonneg (hL i') _)]
    congr 1
    refine Finset.prod_congr rfl fun i' _ => ?_
    rw [← Real.rpow_mul (hL i')]
  have hLft : ∏ i : Fin (k + 1), (t i * ∏ r : Fin k, L (i.succAbove r)) ^ q i
      = (∏ i, t i ^ q i) * ∏ i', L i' ^ (1 - q i') := by
    rw [Finset.prod_congr rfl fun i _ => h1 i, Finset.prod_mul_distrib, Finset.prod_comm]
    congr 1
    refine Finset.prod_congr rfl fun i' _ => ?_
    rw [← Real.rpow_sum_of_nonneg (hL i')
      (fun i _ => mul_nonneg (by split_ifs <;> norm_num) (hq i)), sum_weights q hq1 i']
  calc (∏ i, t i ^ q i) * ∏ i', L i' ^ (1 - q i')
      = ∏ i : Fin (k + 1), (t i * ∏ r : Fin k, L (i.succAbove r)) ^ q i := hLft.symm
    _ ≤ ∑ i : Fin (k + 1), q i * (t i * ∏ r : Fin k, L (i.succAbove r)) := key
    _ = ∑ i : Fin (k + 1), (∏ r : Fin k, L (i.succAbove r)) * (q i * t i) := hR

/-! ## §3  The pointwise bound and the capacity bound -/

/-- **The pointwise entropy bound.**  For `B ≥ 0` with row sums `1 - q i` and column sums `1`,
weights `q ≥ 0` with sum `1`, positive `t`, and positive `x`:
`(∏ t ^ q) (∏ (1 - q) ^ (1 - q)) ∏_c x_c ≤ ∑ᵢ (∏ᵣ L_{i.succAbove r}(x)) (qᵢ tᵢ)`. -/
theorem pointwise_bound {k : ℕ} (B : Matrix (Fin (k + 1)) (Fin k) ℝ) (q t : Fin (k + 1) → ℝ)
    (hB : ∀ i c, 0 ≤ B i c) (hq : ∀ i, 0 ≤ q i) (hq1 : ∑ i, q i = 1)
    (hrow : ∀ i, ∑ c, B i c = 1 - q i) (hcol : ∀ c, ∑ i, B i c = 1)
    (ht : ∀ i, 0 < t i) (x : Fin k → ℝ) (hx : ∀ c, 0 < x c) :
    (∏ i, t i ^ q i) * (∏ i, (1 - q i) ^ (1 - q i)) * ∏ c, x c
      ≤ ∑ i, (∏ r : Fin k, ∑ c, B (i.succAbove r) c * x c) * (q i * t i) := by
  have hL : ∀ i, 0 ≤ ∑ c, B i c * x c :=
    fun i => Finset.sum_nonneg fun c _ => mul_nonneg (hB i c) (hx c).le
  have h1 := column_amgm q t hq hq1 ht (fun i => ∑ c, B i c * x c) hL
  have h2 := rows_amgm B hB hcol x hx
  simp only [hrow] at h2
  have htq : 0 ≤ ∏ i, t i ^ q i := Finset.prod_nonneg fun i _ => Real.rpow_nonneg (ht i).le _
  calc (∏ i, t i ^ q i) * (∏ i, (1 - q i) ^ (1 - q i)) * ∏ c, x c
      = (∏ i, t i ^ q i) * ((∏ i, (1 - q i) ^ (1 - q i)) * ∏ c, x c) := by ring
    _ ≤ (∏ i, t i ^ q i) * ∏ i', (∑ c, B i' c * x c) ^ (1 - q i') :=
        mul_le_mul_of_nonneg_left h2 htq
    _ ≤ _ := h1

/-- **The capacity bound.**  `(∏ t ^ q) (∏ (1 - q) ^ (1 - q)) ≤ cap Q` for
`Q = reduce (rowPoly (extend (q * t) B))`. -/
theorem cap_lower_bound {k : ℕ} (B : Matrix (Fin (k + 1)) (Fin k) ℝ) (q t : Fin (k + 1) → ℝ)
    (hB : ∀ i c, 0 ≤ B i c) (hq : ∀ i, 0 ≤ q i) (hq1 : ∑ i, q i = 1)
    (hrow : ∀ i, ∑ c, B i c = 1 - q i) (hcol : ∀ c, ∑ i, B i c = 1) (ht : ∀ i, 0 < t i) :
    (∏ i, t i ^ q i) * (∏ i, (1 - q i) ^ (1 - q i))
      ≤ Capacity.cap (fun _ => (1 : ℝ)) (fun x : Fin k → ℝ =>
          eval x (GurvitsInduction.reduce (FaceBounds.rowPoly (extend (fun i => q i * t i) B)))) := by
  refine Capacity.le_cap fun x hx => ?_
  show _ ≤ eval x (GurvitsInduction.reduce (FaceBounds.rowPoly (extend (fun i => q i * t i) B)))
    / Capacity.monom (fun _ => (1 : ℝ)) x
  rw [Capacity.monom_one_exp, le_div_iff₀ (Finset.prod_pos fun c _ => hx c),
    eval_reduce_rowPoly]
  simp only [extend_zero, extend_succ]
  exact pointwise_bound B q t hB hq hq1 hrow hcol ht x hx

end Dittert.Entropy
