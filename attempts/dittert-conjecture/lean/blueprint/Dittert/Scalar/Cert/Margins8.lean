import Dittert.Scalar.Defs8
import Mathlib.Data.Fintype.Prod

/-!
# Kernel decisions of the (L) margins and the tail conditions, dimensions 8 to 10

Every ordered proper cut of `n = 8, 9, 10` and the marginal cut of `n = 10` satisfies the
completed-square certificate `GoodLow`; the two residual marginal rows `(8,7,0)` and `(9,8,0)`
are exactly the excluded cases, handled by the near-zero, support and tail certificates.
-/

namespace HallScalar

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem finite_low_8 : ∀ a b : Fin 10, Reduced 8 a.val b.val → b.val ≠ 0 → GoodLow 8 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem finite_low_9 : ∀ a b : Fin 10, Reduced 9 a.val b.val → b.val ≠ 0 → GoodLow 9 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem finite_low_10 : ∀ a b : Fin 10, Reduced 10 a.val b.val → GoodLow 10 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem tails_8 : TailConditions 8 (1/400) (1/20) := by decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
theorem tails_9 : TailConditions 9 (1/500) (3/100) := by decide +kernel

/-- The margins for every reduced cut of `8 ≤ n ≤ 10` other than the two residual rows. -/
theorem margins_low (n a b : ℕ) (hn : 8 ≤ n) (hn' : n ≤ 10) (h : Reduced n a b)
    (hres : ¬ ((n = 8 ∨ n = 9) ∧ b = 0)) : GoodLow n a b := by
  have ha : a < 10 := by
    rcases h with h | h
    · obtain ⟨_, _, hs⟩ := h
      omega
    · obtain ⟨rfl, rfl⟩ := h
      omega
  have hb : b < 10 := by
    rcases h with h | h
    · obtain ⟨_, _, hs⟩ := h
      omega
    · obtain ⟨rfl, rfl⟩ := h
      omega
  have hnCases : n = 8 ∨ n = 9 ∨ n = 10 := by omega
  rcases hnCases with rfl | rfl | rfl
  · exact finite_low_8 ⟨a, ha⟩ ⟨b, hb⟩ h (by simpa using fun hb0 => hres ⟨Or.inl rfl, hb0⟩)
  · exact finite_low_9 ⟨a, ha⟩ ⟨b, hb⟩ h (by simpa using fun hb0 => hres ⟨Or.inr rfl, hb0⟩)
  · exact finite_low_10 ⟨a, ha⟩ ⟨b, hb⟩ h

end HallScalar
