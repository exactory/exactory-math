import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace DittertScalar

/-- The strict quadratic criterion used after the Hall-cut bounds. -/
theorem positive_quadratic (a b c u : ℝ) (hc : 0 < c)
    (hdisc : 0 < 4 * c * a - b ^ 2) : 0 < c * u ^ 2 + b * u + a := by
  have hid : 4 * c * (c * u ^ 2 + b * u + a) =
      (2 * c * u + b) ^ 2 + (4 * c * a - b ^ 2) := by ring
  have hp : 0 < 4 * c * (c * u ^ 2 + b * u + a) := by
    rw [hid]
    exact add_pos_of_nonneg_of_pos (sq_nonneg _) hdisc
  exact pos_of_mul_pos_right hp (by linarith)

/-- All scalar values satisfying the permanent and deficit bounds are excluded. -/
theorem exclusion (gamma permanent deficit floor slope curvature u : ℝ)
    (hc : 0 < curvature)
    (hdisc : 0 < 4 * curvature * (floor - gamma) - slope ^ 2)
    (hper : floor - slope * u ≤ permanent)
    (hdef : curvature * u ^ 2 ≤ deficit)
    (hbudget : permanent + deficit = gamma) : False := by
  have hq := positive_quadratic (floor - gamma) (-slope) curvature u hc (by
    simpa using hdisc)
  nlinarith

#print axioms positive_quadratic
#print axioms exclusion

end DittertScalar
