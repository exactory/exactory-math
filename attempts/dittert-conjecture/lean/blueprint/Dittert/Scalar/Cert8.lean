import Dittert.Scalar.Cert.Margins8
import Dittert.Scalar.Cert.NearZero8
import Dittert.Scalar.Cert.NearZero9
import Dittert.Scalar.Cert.Support8z1
import Dittert.Scalar.Cert.Support8z2
import Dittert.Scalar.Cert.Support8z3
import Dittert.Scalar.Cert.Support8z4
import Dittert.Scalar.Cert.Support8z5
import Dittert.Scalar.Cert.Support8z6
import Dittert.Scalar.Cert.Support9z7
import Mathlib.Tactic.IntervalCases

/-!
# Obligation `s8`: the finite certificates of dimensions 8, 9, 10, assembled
-/

namespace Dittert

theorem near_zero_8 (u : ℝ) (hu : 0 ≤ u) (hu1 : u ≤ 1/400) : 0 < NearZero.p 8 u := by
  have hx : 0 ≤ 400*u := by positivity
  have hx1 : 400*u ≤ 1 := by linarith
  have hp := NearZero.positive8 (400*u) hx hx1
  rw [← NearZero.identity8] at hp
  have hid : (400*u)/400 = u := by ring
  rw [hid] at hp
  exact hp

theorem near_zero_9 (u : ℝ) (hu : 0 ≤ u) (hu1 : u ≤ 1/500) : 0 < NearZero.p 9 u := by
  have hx : 0 ≤ 500*u := by positivity
  have hx1 : 500*u ≤ 1 := by linarith
  have hp := NearZero.positive9 (500*u) hx hx1
  rw [← NearZero.identity9] at hp
  have hid : (500*u)/500 = u := by ring
  rw [hid] at hp
  exact hp

theorem support_8 (z : ℕ) (hz : 1 ≤ z) (hz6 : z ≤ 6) (u : ℝ) (hu : 1/400 ≤ u) (hu1 : u ≤ 1/20) :
    0 < NearZero.support 8 z u := by
  interval_cases z
  · exact Support8z1.support_certificate u hu hu1
  · exact Support8z2.support_certificate u hu hu1
  · exact Support8z3.support_certificate u hu hu1
  · exact Support8z4.support_certificate u hu hu1
  · exact Support8z5.support_certificate u hu hu1
  · exact Support8z6.support_certificate u hu hu1

/-- Obligation `s8`, kernel-checked. -/
theorem scalar_certificates_8 : ScalarCertificates8 :=
  ⟨HallScalar.margins_low, near_zero_8, near_zero_9, support_8,
    Support9z7.support_certificate, HallScalar.tails_8, HallScalar.tails_9⟩

end Dittert
