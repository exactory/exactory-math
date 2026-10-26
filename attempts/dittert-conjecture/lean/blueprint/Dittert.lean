import Dittert.Basic
import Dittert.Obligations
import Dittert.Scalar.Defs11
import Dittert.Scalar.Defs8
import Dittert.Scalar.Defs7
import Dittert.Reduction
import Dittert.Hall
import Dittert.Floors
import Dittert.Bridges

/-!
# Dittert's conjecture in dimensions 5 to 15

The final theorem composes the bridges with the obligation theorems. Proved obligations are
imported from their modules (`Dittert.Reduction`, `Dittert.Hall`, `Dittert.Floors`, and the
bridge `bridge_11` in `Dittert.Bridges`); every obligation below is a `sorry` until its node
proves it, and `#print axioms dittert_5_15` reports `sorryAx` until then. The scalar certificate
modules `Dittert.Scalar.Cert11` and `Dittert.Scalar.Cert8` are built as separate roots and will be
imported here when the root step is assembled.
-/

namespace Dittert

theorem core_entropy : CoreEntropy := by sorry
theorem maximizer_zero_pattern : MaximizerZeroPattern := by sorry
theorem two_zero_floor : TwoZeroFloor := by sorry
theorem scalar_certificates_7 : ScalarCertificates7 := by sorry
theorem scalar_certificates_8 : ScalarCertificates8 := by sorry
theorem scalar_certificates_11 : ScalarCertificates11 := by sorry
theorem case_5_6 : Case 5 6 := by sorry

theorem case_7 : Case 7 7 :=
  bridge_7 reduction hall_domination gurvits_floors core_entropy scalar_certificates_7

theorem case_8_10 : Case 8 10 :=
  bridge_8 reduction hall_domination gurvits_floors maximizer_zero_pattern two_zero_floor
    scalar_certificates_8

theorem case_11_15 : Case 11 15 :=
  bridge_11 reduction hall_domination gurvits_floors scalar_certificates_11

/-- Dittert's conjecture with its equality case for every integer `5 ≤ n ≤ 15`. -/
theorem dittert_5_15 : Root := bridge_assembly case_5_6 case_7 case_8_10 case_11_15

end Dittert
