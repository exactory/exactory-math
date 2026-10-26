import Dittert.Obligations
import Dittert.Scalar.Defs7
import Dittert.Scalar.Defs8
import Dittert.Scalar.Defs11
import Dittert.Bridge.N11

/-!
# The bridges of the blueprint

Each bridge is a conditional theorem: its hypotheses are the obligation `Prop`s of the route,
its conclusion the case statement. The assembly bridge is the case split on `n`.
-/

namespace Dittert

/-- The assembly bridge: the four cases cover every `5 ≤ n ≤ 15`. -/
theorem bridge_assembly (h56 : Case 5 6) (h7 : Case 7 7) (h8 : Case 8 10) (h11 : Case 11 15) :
    Root := by
  intro n hlo hhi
  rcases Nat.lt_or_ge n 7 with h | h
  · exact h56 n hlo (by omega)
  rcases Nat.lt_or_ge n 8 with h' | h'
  · exact h7 n h (by omega)
  rcases Nat.lt_or_ge n 11 with h'' | h''
  · exact h8 n h' (by omega)
  exact h11 n h'' hhi

/-- Bridge for `n = 7`. -/
theorem bridge_7 (hR : Reduction) (hH : HallDomination) (hF : GurvitsFloors)
    (hE : CoreEntropy) (hS : ScalarCertificates7) : Case 7 7 := by
  sorry

/-- Bridge for `8 ≤ n ≤ 10`. -/
theorem bridge_8 (hR : Reduction) (hH : HallDomination) (hF : GurvitsFloors)
    (hZ : MaximizerZeroPattern) (hT : TwoZeroFloor) (hS : ScalarCertificates8) : Case 8 10 := by
  sorry

/-- Bridge for `11 ≤ n ≤ 15`: no maximizer has a zero entry (`Dittert.Bridge.N11`), so
`Reduction` gives the statement. -/
theorem bridge_11 (hR : Reduction) (hH : HallDomination) (hF : GurvitsFloors)
    (hS : ScalarCertificates11) : Case 11 15 := by
  intro n hlo hhi
  exact hR n (by omega) fun A hA i j => maximizer_pos hH hF hS hlo hhi A hA i j

end Dittert
