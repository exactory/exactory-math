import Main
import Mathlib.Tactic.NormNum

namespace HallScalar

-- A wrong factorial normalization would fail this hand-derived fixture.
example : gamma 3 = (2 / 9 : ℚ) := by norm_num [gamma, Nat.factorial]
-- These boundaries catch omission of the largest proper cut and inclusion of p=0.
example : Proper 11 1 9 := by decide
example : ¬ Proper 11 1 10 := by decide
example : Reduced 11 10 0 := by decide
example : ¬ Reduced 11 0 0 := by decide
-- The formal theorem covers both endpoints and negative u, with no small-root assumption.
example : 0 < (curvature 11 1 9 : ℝ) * (0:ℝ)^2 +
    (floor 11 1 9 : ℝ) * (1-(0:ℝ))^11 - (gamma 11 : ℝ) :=
  scalar_positive 11 1 9 (by omega) (by omega) (by omega) (by omega) 0 (by norm_num)
example : 0 < (curvature 15 14 0 : ℝ) * (1:ℝ)^2 +
    (floor 15 14 0 : ℝ) * (1-(1:ℝ))^15 - (gamma 15 : ℝ) :=
  scalar_positive 15 14 0 (by omega) (by omega) (by omega) (by omega) 1 (by norm_num)
example : 0 < (curvature 12 0 8 : ℝ) * (-2:ℝ)^2 +
    (floor 12 0 8 : ℝ) * (1-(-2:ℝ))^12 - (gamma 12 : ℝ) :=
  scalar_positive 12 0 8 (by omega) (by omega) (by omega) (by omega) (-2) (by norm_num)

end HallScalar
