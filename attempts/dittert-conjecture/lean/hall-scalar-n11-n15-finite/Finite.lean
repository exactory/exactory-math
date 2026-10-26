import Definitions
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Finset.Card

namespace HallScalar

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
/-- Pilot: all ordered proper cuts and the normalized marginal cut at n=11. -/
theorem finite_n11 : ∀ a b : Fin 15, Reduced 11 a.val b.val → Good 11 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
/-- Direct kernel verification of every reduced case at n=12. -/
theorem finite_n12 : ∀ a b : Fin 15, Reduced 12 a.val b.val → Good 12 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
/-- Direct kernel verification of every reduced case at n=13. -/
theorem finite_n13 : ∀ a b : Fin 15, Reduced 13 a.val b.val → Good 13 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
/-- Direct kernel verification of every reduced case at n=14. -/
theorem finite_n14 : ∀ a b : Fin 15, Reduced 14 a.val b.val → Good 14 a.val b.val := by
  decide +kernel

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
/-- Direct kernel verification of every reduced case at n=15. -/
theorem finite_n15 : ∀ a b : Fin 15, Reduced 15 a.val b.val → Good 15 a.val b.val := by
  decide +kernel

/-- No transpose quotient is used: all ordered proper pairs are present. -/
def reducedCases (n : ℕ) : Finset (Fin 15 × Fin 15) :=
  Finset.univ.filter fun p => Reduced n p.1.val p.2.val

set_option maxRecDepth 8192 in
set_option maxHeartbeats 2000000 in
theorem case_counts :
    (reducedCases 11).card = 46 ∧ (reducedCases 12).card = 56 ∧
    (reducedCases 13).card = 67 ∧ (reducedCases 14).card = 79 ∧
    (reducedCases 15).card = 92 := by
  decide +kernel

/-- The normalized family contains exactly 340 cases. -/
theorem total_case_count :
    (reducedCases 11).card + (reducedCases 12).card + (reducedCases 13).card +
      (reducedCases 14).card + (reducedCases 15).card = 340 := by
  obtain ⟨h11, h12, h13, h14, h15⟩ := case_counts
  omega

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

/-- The finite audit includes coverage and the documented family cardinality. -/
theorem finite_certificate :
    (∀ n a b : ℕ, 11 ≤ n → n ≤ 15 → 0 < a+b → a+b < n → Good n a b) ∧
    (reducedCases 11).card + (reducedCases 12).card + (reducedCases 13).card +
      (reducedCases 14).card + (reducedCases 15).card = 340 :=
  ⟨all_good, total_case_count⟩

end HallScalar
