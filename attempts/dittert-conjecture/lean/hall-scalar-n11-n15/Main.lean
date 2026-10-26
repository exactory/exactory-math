import Finite

namespace HallScalar

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

/-- The scalar lower bounds contradict even the relaxed budget inequality. -/
theorem scalar_exclusion (n a b : ℕ) (hn : 11 ≤ n) (hn' : n ≤ 15)
    (hab : 0 < a+b) (hsum : a+b < n) (u P delta : ℝ) (hu : u ≤ 1)
    (hP : (floor n a b : ℝ)*(1-u)^n ≤ P)
    (hd : (curvature n a b : ℝ)*u^2 ≤ delta)
    (hb : P+delta ≤ (gamma n : ℝ)) : False := by
  have hp := scalar_positive n a b hn hn' hab hsum u hu
  linarith

end HallScalar
