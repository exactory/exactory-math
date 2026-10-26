import Dittert.Scalar.Defs11
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Finset.Card
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

/-!
# The kernel certificates for dimensions 11 to 15

Ported from `attack/hall-scalar-lean-n11-n15/deterministic/formal-check-1` (Finite.lean and
Main.lean, kernel-checked on 2026-09-05), restated against `Dittert.ScalarCertificates11`.
-/

namespace HallScalar

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
/-- All ordered proper cuts and the normalized marginal cut at n=11. -/
theorem finite_n11 : ∀ a b : Fin 15, Reduced 11 a.val b.val → Good 11 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
theorem finite_n12 : ∀ a b : Fin 15, Reduced 12 a.val b.val → Good 12 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
theorem finite_n13 : ∀ a b : Fin 15, Reduced 13 a.val b.val → Good 13 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
theorem finite_n14 : ∀ a b : Fin 15, Reduced 14 a.val b.val → Good 14 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
theorem finite_n15 : ∀ a b : Fin 15, Reduced 15 a.val b.val → Good 15 a.val b.val := by
  decide +kernel

/-- Bounded natural sizes embed into the finite universe actually checked. -/
theorem reduced_good (n a b : ℕ) (hn : 11 ≤ n) (hn' : n ≤ 15)
    (h : Reduced n a b) : Good n a b := by
  have ha : a < 15 := by
    rcases h with h | h
    · obtain ⟨_, _, hs⟩ := h
      omega
    · obtain ⟨rfl, rfl⟩ := h
      omega
  have hb : b < 15 := by
    rcases h with h | h
    · obtain ⟨_, _, hs⟩ := h
      omega
    · obtain ⟨rfl, rfl⟩ := h
      omega
  have hnCases : n = 11 ∨ n = 12 ∨ n = 13 ∨ n = 14 ∨ n = 15 := by omega
  rcases hnCases with rfl | rfl | rfl | rfl | rfl
  · exact finite_n11 ⟨a, ha⟩ ⟨b, hb⟩ h
  · exact finite_n12 ⟨a, ha⟩ ⟨b, hb⟩ h
  · exact finite_n13 ⟨a, ha⟩ ⟨b, hb⟩ h
  · exact finite_n14 ⟨a, ha⟩ ⟨b, hb⟩ h
  · exact finite_n15 ⟨a, ha⟩ ⟨b, hb⟩ h

/-- Every nonfull ordered cut is covered, including both marginal orientations. -/
theorem all_good (n a b : ℕ) (hn : 11 ≤ n) (hn' : n ≤ 15)
    (hab : 0 < a+b) (hsum : a+b < n) : Good n a b := by
  by_cases hz : a = 0 ∨ b = 0
  · have hm : Reduced n (n-1) 0 := Or.inr ⟨rfl, rfl⟩
    have hg := reduced_good n (n-1) 0 hn hn' hm
    simpa only [Good, floor, curvature, hz, or_true, ite_true] using hg
  · have hp : Proper n a b := by
      dsimp [Proper]
      omega
    exact reduced_good n a b hn hn' (Or.inl hp)

/-- Completion of the square with a strict discriminant margin. -/
theorem quadratic_positive (C M g u : ℝ) (n : ℕ)
    (hC : 0 < C) (hdisc : 0 < 4*C*(M-g)-((n:ℝ)*M)^2) :
    0 < C*u^2-(n:ℝ)*M*u+M-g := by
  have hid : 4*C*(C*u^2-(n:ℝ)*M*u+M-g) =
      (2*C*u-(n:ℝ)*M)^2 + (4*C*(M-g)-((n:ℝ)*M)^2) := by ring
  have hp : 0 < 4*C*(C*u^2-(n:ℝ)*M*u+M-g) := by
    rw [hid]
    exact add_pos_of_nonneg_of_pos (sq_nonneg _) hdisc
  exact pos_of_mul_pos_right hp (by linarith)

/-- The finite scalar layer of the Hall argument, not its matrix reduction. -/
theorem scalar_positive (n a b : ℕ) (hn : 11 ≤ n) (hn' : n ≤ 15)
    (hab : 0 < a+b) (hsum : a+b < n) (u : ℝ) (hu : u ≤ 1) :
    0 < (curvature n a b : ℝ) * u^2 +
      (floor n a b : ℝ) * (1-u)^n - (gamma n : ℝ) := by
  obtain ⟨hMq, hCq, hDq⟩ := all_good n a b hn hn' hab hsum
  have hM : (0:ℝ) < (floor n a b : ℝ) := Rat.cast_pos.mpr hMq
  have hC : (0:ℝ) < (curvature n a b : ℝ) := Rat.cast_pos.mpr hCq
  have hD : (0:ℝ) < 4*(curvature n a b : ℝ)*
      ((floor n a b : ℝ)-(gamma n : ℝ))-((n:ℝ)*(floor n a b : ℝ))^2 := by
    exact_mod_cast hDq
  have hquad := quadratic_positive (curvature n a b) (floor n a b) (gamma n) u n hC hD
  have hbern : (1:ℝ)-(n:ℝ)*u ≤ (1-u)^n := by
    simpa only [mul_neg, sub_eq_add_neg] using
      (one_add_mul_le_pow (a := -u) (by linarith : (-2:ℝ) ≤ -u) n)
  have hscaled := mul_le_mul_of_nonneg_left hbern hM.le
  nlinarith

end HallScalar

namespace Dittert

/-- Obligation `s11`, kernel-checked. -/
theorem scalar_certificates_11 : ScalarCertificates11 := fun n a b hn hn' hab hsum u hu =>
  HallScalar.scalar_positive n a b hn hn' hab hsum u hu

end Dittert
