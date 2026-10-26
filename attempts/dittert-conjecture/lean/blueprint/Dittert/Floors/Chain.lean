/-
# The extraction chain with degree-refined constants

Built on the port `GurvitsPort` (DCPRevere/maths-pub, commit
0a1cb0a14fefe85668365d448f9bbaf4dd89d458, Apache-2.0; see `../../../maths-pub-port/PORT-NOTES.md`
and `AXIOMS.txt`).

`chain` extracts the first `h` variables of a homogeneous H-stable polynomial in `k` variables
one at a time with `GurvitsInduction.reduce`, paying the one-variable constant
`G(d) = ((d-1)/d)^(d-1)` (`OneVarCapacity.stone12`) where `d` is bounded by a J-degree bound
`JDegBd h N` (the total exponent of the first `h` variables is at most `N`), and then applies the
port's `gurvitsBound` to the remaining `k - h` variables:

    (∏_{i<h} G(N - i)) · γ(k - h) · cap(q) ≤ [x₁ ⋯ x_k] q .

H-stability is carried through every step by `Analytic.hstable_reduce`.
-/
import Mathlib.Tactic
import GurvitsPort.GurvitsUnconditional
import Dittert.Basic
import Dittert.Floors.Analytic

open MvPolynomial Finset

namespace Dittert.Floors.Chain

/-! ## §1  The J-degree of a multi-index -/

/-- The total exponent of the first `h` variables in the multi-index `m`. -/
def jdeg {k : ℕ} (h : ℕ) (m : Fin k →₀ ℕ) : ℕ := ∑ j, if j.val < h then m j else 0

theorem jdeg_add {k : ℕ} (h : ℕ) (m₁ m₂ : Fin k →₀ ℕ) :
    jdeg h (m₁ + m₂) = jdeg h m₁ + jdeg h m₂ := by
  unfold jdeg
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun j _ => ?_
  rw [Finsupp.add_apply]
  split_ifs <;> simp

theorem jdeg_cons {k : ℕ} (h : ℕ) (m : Fin k →₀ ℕ) (i : ℕ) :
    jdeg (h + 1) (m.cons i) = i + jdeg h m := by
  unfold jdeg
  rw [Fin.sum_univ_succ]
  simp [Finsupp.cons_zero, Finsupp.cons_succ, Fin.val_succ]

theorem jdeg_le_degree {k : ℕ} (h : ℕ) (m : Fin k →₀ ℕ) : jdeg h m ≤ m.degree := by
  rw [Finsupp.degree_eq_sum]
  unfold jdeg
  refine Finset.sum_le_sum fun j _ => ?_
  split_ifs <;> simp

theorem jdeg_single_of_le {k : ℕ} {h : ℕ} {j : Fin k} (hj : h ≤ j.val) :
    jdeg h (Finsupp.single j 1) = 0 := by
  unfold jdeg
  refine Finset.sum_eq_zero fun j' _ => ?_
  by_cases hj' : j'.val < h
  · rw [if_pos hj', Finsupp.single_apply, if_neg]
    intro hjj
    rw [hjj] at hj
    omega
  · rw [if_neg hj']

/-- **The J-degree bound.**  Every monomial whose exponent on the first `h` variables exceeds
`N` has zero coefficient. -/
def JDegBd {k : ℕ} (h N : ℕ) (q : MvPolynomial (Fin k) ℝ) : Prop :=
  ∀ m : Fin k →₀ ℕ, N < jdeg h m → coeff m q = 0

/-- The `x₀`-degree is bounded by the J-degree bound when `x₀` is a J-variable. -/
theorem natDegree_finSuccEquiv_le_of_jDegBd {k h N : ℕ} {q : MvPolynomial (Fin (k + 1)) ℝ}
    (hq : JDegBd (h + 1) N q) : (finSuccEquiv ℝ k q).natDegree ≤ N := by
  refine Polynomial.natDegree_le_iff_coeff_eq_zero.mpr fun i hi => ?_
  ext m
  rw [finSuccEquiv_coeff_coeff, MvPolynomial.coeff_zero]
  exact hq _ (by rw [jdeg_cons]; omega)

/-- The J-degree bound survives one extraction, dropping by one. -/
theorem jDegBd_reduce {k h N : ℕ} {q : MvPolynomial (Fin (k + 1)) ℝ} (hq : JDegBd (h + 1) N q) :
    JDegBd h (N - 1) (GurvitsInduction.reduce q) := by
  intro m hm
  rw [GurvitsInduction.coeff_reduce]
  exact hq _ (by rw [jdeg_cons]; omega)

/-- `reduce` lowers the degree of a homogeneous polynomial by one. -/
theorem isHomogeneous_reduce {k N : ℕ} {q : MvPolynomial (Fin (k + 1)) ℝ}
    (hq : q.IsHomogeneous (N + 1)) : (GurvitsInduction.reduce q).IsHomogeneous N := by
  have h1 : GurvitsInduction.reduce q = bind₁ (HStableClass.subMap 0 k) (pderiv 0 q) := by
    rw [← SlicedTower.reduceAt_zero, HStableClass.reduceAt_eq_bind₁]
  have h2 : (pderiv (0 : Fin (k + 1)) q).IsHomogeneous N := by
    simpa using hq.pderiv (i := (0 : Fin (k + 1)))
  have h3 : ∀ i, (HStableClass.subMap 0 k i).IsHomogeneous 1 := by
    intro i
    induction i using Fin.cases with
    | zero =>
      rw [HStableClass.subMap_zero, map_zero]
      exact MvPolynomial.isHomogeneous_zero (σ := Fin k) (R := ℝ) 1
    | succ j =>
      rw [HStableClass.subMap_succ]
      exact MvPolynomial.isHomogeneous_X ℝ _
  rw [h1]
  simpa using h2.aeval (HStableClass.subMap 0 k) h3

/-! ## §2  The constants -/

/-- The port's one-variable constant `G(d,1) = ((d-1)/d)^(d-1)`, cast to `ℝ`. -/
noncomputable def Gc (d : ℕ) : ℝ := ((BorderPayment.G d 1 : ℚ) : ℝ)

theorem Gc_nonneg (d : ℕ) : 0 ≤ Gc d := by
  unfold Gc
  exact_mod_cast BorderPayment.G_nonneg d 1

theorem Gc_antitone {d D : ℕ} (hd : 1 ≤ d) (hdD : d ≤ D) : Gc D ≤ Gc d := by
  unfold Gc
  exact_mod_cast GurvitsInduction.G_antitone hd hdD

theorem gamma_nonneg (m : ℕ) : 0 ≤ gamma m := by
  unfold gamma
  positivity

theorem gamma_pos (m : ℕ) : 0 < gamma m := by
  unfold gamma
  have h : (0 : ℝ) < (m : ℝ) ^ m := by
    rcases Nat.eq_zero_or_pos m with rfl | hm
    · simp
    · exact pow_pos (by exact_mod_cast hm) m
  exact div_pos (by exact_mod_cast Nat.factorial_pos m) h

/-- `γ(m) = ∏_{k<m} G(k+1)`, the port's telescoping identity cast to `ℝ`. -/
theorem gamma_eq_prod (m : ℕ) : gamma m = ∏ k ∈ range m, Gc (k + 1) := by
  have h : ((∏ k ∈ range m, BorderPayment.G (k + 1) 1 : ℚ) : ℝ)
      = (((m.factorial : ℚ) / (m : ℚ) ^ m : ℚ) : ℝ) := by
    rw [GurvitsInduction.prod_G_one]
  push_cast at h
  unfold gamma Gc
  exact h.symm

/-- `∏_{i<b} G(m - i) = γ(m) / γ(m - b)` for `b ≤ m`. -/
theorem prod_Gc_ratio {m b : ℕ} (hb : b ≤ m) :
    ∏ i ∈ range b, Gc (m - i) = gamma m / gamma (m - b) := by
  have hsplit : gamma m = gamma (m - b) * ∏ i ∈ range b, Gc (m - i) := by
    rw [gamma_eq_prod, gamma_eq_prod]
    have hm : m = (m - b) + b := (Nat.sub_add_cancel hb).symm
    conv_lhs => rw [hm, Finset.prod_range_add]
    congr 1
    have hrefl := Finset.prod_range_reflect (fun i => Gc (m - i)) b
    rw [← hrefl]
    refine Finset.prod_congr rfl fun x hx => ?_
    rw [Finset.mem_range] at hx
    congr 1
    omega
  rw [hsplit, mul_div_cancel_left₀ _ (gamma_pos _).ne']

/-! ## §3  The chain -/

/-- **The extraction chain.**  For a homogeneous polynomial `q` of degree `k` in `k` variables,
H-stable (or zero), with non-negative coefficients and J-degree bound `N` on the first `h`
variables (`h ≤ k`, `h ≤ N`):

    (∏_{i<h} G(N - i)) · γ(k - h) · cap(q) ≤ [x₁ ⋯ x_k] q .

Each of the `h` steps pays `G(d)` for the actual `x₀`-degree `d ≤ N - i` (`G` is non-increasing),
H-stability is carried by `Analytic.hstable_reduce`, and the last `k - h` variables are handled by
the port's `gurvitsBound`. -/
theorem chain : ∀ (h k N : ℕ) (q : MvPolynomial (Fin k) ℝ), h ≤ k → h ≤ N →
    (q = 0 ∨ Gurvits.HStable q) → q.IsHomogeneous k → (∀ m, 0 ≤ coeff m q) → JDegBd h N q →
    (∏ i ∈ range h, Gc (N - i)) * gamma (k - h) *
        Capacity.cap (fun _ => (1 : ℝ)) (fun y => eval y q) ≤ coeff (Gurvits.topIdx k) q := by
  intro h
  induction h with
  | zero =>
    intro k N q _ _ hst hhom hnn _
    rw [Finset.prod_range_zero, one_mul, Nat.sub_zero]
    rcases hst with rfl | hst
    · simp
    · exact GurvitsUnconditional.gurvitsBound k q hhom hnn hst
  | succ h ih =>
    intro k N q hk hN hst hhom hnn hJ
    obtain ⟨k', rfl⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
    -- the constants of the step
    have hconst : (∏ i ∈ range (h + 1), Gc (N - i))
        = (∏ i ∈ range h, Gc (N - 1 - i)) * Gc N := by
      rw [Finset.prod_range_succ', Nat.sub_zero]
      congr 1
      refine Finset.prod_congr rfl fun i _ => ?_
      congr 1
      omega
    have hkh : k' + 1 - (h + 1) = k' - h := by omega
    rw [hconst, hkh]
    have hC0 : 0 ≤ (∏ i ∈ range h, Gc (N - 1 - i)) * gamma (k' - h) :=
      mul_nonneg (Finset.prod_nonneg fun i _ => Gc_nonneg _) (gamma_nonneg _)
    rcases hst with rfl | hst
    · simp
    -- basic facts about `q`
    have hNonneg : Capacity.NonnegOn (fun y : Fin (k' + 1) → ℝ => eval y q) :=
      fun y hy => GurvitsInduction.eval_nonneg hnn fun j => (hy j).le
    have hcapnn : 0 ≤ Capacity.cap (fun _ => (1 : ℝ)) (fun y : Fin (k' + 1) → ℝ => eval y q) :=
      Capacity.cap_nonneg hNonneg
    have hPnn : OneVarCapacity.NonnegOn₁
        (fun (x : Fin k' → ℝ) (t : ℝ) => eval (Fin.cons t x) q) :=
      fun x t hx ht => GurvitsInduction.eval_nonneg hnn fun j =>
        (GurvitsInduction.cons_pos ht hx j).le
    have hdN : (finSuccEquiv ℝ k' q).natDegree ≤ N := natDegree_finSuccEquiv_le_of_jDegBd hJ
    obtain ⟨d, hdle, hfx⟩ := HStableFac.classFac_hstable hst hhom hnn
    have htopnn : 0 ≤ coeff (Gurvits.topIdx (k' + 1)) q := hnn _
    rcases Nat.eq_zero_or_pos d with rfl | hd1
    · -- the distinguished variable does not appear: the capacity vanishes
      obtain ⟨c, a, hc, _, hval⟩ := hfx (fun _ => (1 : ℝ)) (fun _ => one_pos)
      have hconst' : ∀ t : ℝ, eval (Fin.cons t (fun _ => (1 : ℝ))) q = c := by
        intro t
        rw [hval t, LemmaU.fVal]
        simp
      have hzero := GurvitsInduction.capOne_nonpos_of_const (fun _ : Fin k' => (1 : ℝ)) hPnn
        (fun _ => one_pos) hc hconst'
      rw [GurvitsInduction.capOne_eq_cap hNonneg] at hzero
      have hcap0 : Capacity.cap (fun _ => (1 : ℝ)) (fun y : Fin (k' + 1) → ℝ => eval y q) = 0 :=
        le_antisymm hzero hcapnn
      rw [hcap0, mul_zero]
      exact htopnn
    · -- the one-variable capacity step, then the induction hypothesis on `reduce q`
      set r := GurvitsInduction.reduce q with hrdef
      have hstep := OneVarCapacity.stone12 (ι := Fin k') hd1 (fun _ => (1 : ℝ))
        (P := fun x t => eval (Fin.cons t x) q) (Q := fun x => eval x r)
        (fun x hx => by
          obtain ⟨c, a, hc, ha, hval⟩ := hfx x hx
          exact ⟨c, a, hc, ha, hval, GurvitsInduction.eval_reduce_of_fac hd1 hval⟩)
      rw [GurvitsInduction.capOne_eq_cap hNonneg] at hstep
      have hstep' : Gc d * Capacity.cap (fun _ => (1 : ℝ)) (fun y : Fin (k' + 1) → ℝ => eval y q)
          ≤ Capacity.cap (fun _ => (1 : ℝ)) (fun x : Fin k' → ℝ => eval x r) := hstep
      have hGle : Gc N ≤ Gc d := Gc_antitone hd1 (le_trans hdle hdN)
      have hrnn : ∀ m, 0 ≤ coeff m r := fun m => by
        rw [hrdef, GurvitsInduction.coeff_reduce]
        exact hnn _
      have hrhom : r.IsHomogeneous k' := isHomogeneous_reduce hhom
      have hrJ : JDegBd h (N - 1) r := jDegBd_reduce hJ
      have hrst : r = 0 ∨ Gurvits.HStable r := by
        rcases eq_or_ne r 0 with h0 | h0
        · exact Or.inl h0
        · exact Or.inr (Analytic.hstable_reduce hst h0)
      have hIH := ih k' (N - 1) r (by omega) (by omega) hrst hrhom hrnn hrJ
      calc (∏ i ∈ range h, Gc (N - 1 - i)) * Gc N * gamma (k' - h)
            * Capacity.cap (fun _ => (1 : ℝ)) (fun y : Fin (k' + 1) → ℝ => eval y q)
          = ((∏ i ∈ range h, Gc (N - 1 - i)) * gamma (k' - h))
              * (Gc N * Capacity.cap (fun _ => (1 : ℝ)) (fun y : Fin (k' + 1) → ℝ => eval y q)) := by
            ring
        _ ≤ ((∏ i ∈ range h, Gc (N - 1 - i)) * gamma (k' - h))
              * (Gc d * Capacity.cap (fun _ => (1 : ℝ)) (fun y : Fin (k' + 1) → ℝ => eval y q)) :=
            mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right hGle hcapnn) hC0
        _ ≤ ((∏ i ∈ range h, Gc (N - 1 - i)) * gamma (k' - h))
              * Capacity.cap (fun _ => (1 : ℝ)) (fun x : Fin k' → ℝ => eval x r) :=
            mul_le_mul_of_nonneg_left hstep' hC0
        _ ≤ coeff (Gurvits.topIdx k') r := hIH
        _ = coeff (Gurvits.topIdx (k' + 1)) q := GurvitsInduction.coeff_topIdx_reduce q

end Dittert.Floors.Chain
