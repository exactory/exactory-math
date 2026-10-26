import Mathlib

/-!
# The quantitative van der Waerden inequality at n = 3, sharp

For every doubly stochastic 3 x 3 real matrix B,

    per(B) >= (2/9) * (1 + ||B - J/3||_F^2 / 4),

which is the claim of the attack with its constant 1/4, at the one dimension where that constant
is attained. The proof is the exact identity (Fable, route-interpolation.md, Theorem 2)

    per(B)/gamma_3 - 1 - ||B - J/3||^2 / 4 = sum over the rows (x, y, z) of  1 - 4 e_2 + 9 e_3,

together with Schur's inequality e_1^3 - 4 e_1 e_2 + 9 e_3 >= 0 for non-negative x, y, z, which
at e_1 = 1 is exactly each summand. The statement is written on the nine entries with the six
margin equations as hypotheses, so that it reads as the claim does; the constraints are then
substituted and the inequality is a polynomial inequality in four free entries that `nlinarith`
closes from the three Schur instances.
-/

/-- Schur's inequality, degree one, for non-negative reals. -/
theorem schur_three (x y z : ℝ) (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) :
    0 ≤ x * (x - y) * (x - z) + y * (y - x) * (y - z) + z * (z - x) * (z - y) := by
  rcases le_total x y with hxy | hxy <;> rcases le_total y z with hyz | hyz <;>
    rcases le_total x z with hxz | hxz <;>
    nlinarith [mul_nonneg (mul_nonneg hx hy) hz,
               mul_nonneg hx (mul_nonneg (sub_nonneg.2 hxy) (sub_nonneg.2 hxz)),
               mul_nonneg hy (mul_nonneg (sub_nonneg.2 hxy) (sub_nonneg.2 hyz)),
               mul_nonneg hz (mul_nonneg (sub_nonneg.2 hxz) (sub_nonneg.2 hyz)),
               mul_nonneg hx (mul_nonneg (sub_nonneg.2 hyz) (sub_nonneg.2 hxz)),
               mul_nonneg hy (mul_nonneg (sub_nonneg.2 hxy) (sub_nonneg.2 hxz)),
               mul_nonneg hz (mul_nonneg (sub_nonneg.2 hxy) (sub_nonneg.2 hyz)),
               mul_nonneg (sub_nonneg.2 hxy) (mul_nonneg (sub_nonneg.2 hyz) (sub_nonneg.2 hxz)),
               mul_nonneg (mul_nonneg (sub_nonneg.2 hxy) (sub_nonneg.2 hxy)) (add_nonneg hx hy),
               mul_nonneg (mul_nonneg (sub_nonneg.2 hyz) (sub_nonneg.2 hyz)) (add_nonneg hy hz),
               mul_nonneg (mul_nonneg (sub_nonneg.2 hxz) (sub_nonneg.2 hxz)) (add_nonneg hx hz)]

/-- The claim at `n = 3`: `per(B) >= (2/9)(1 + ||B - J/3||_F^2 / 4)` on the nine entries. -/
theorem qvdw_three (a b c d e f g h i : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hc : 0 ≤ c) (hd : 0 ≤ d) (he : 0 ≤ e) (hf : 0 ≤ f)
    (hg : 0 ≤ g) (hh : 0 ≤ h) (hi : 0 ≤ i)
    (r1 : a + b + c = 1) (r2 : d + e + f = 1) (r3 : g + h + i = 1)
    (c1 : a + d + g = 1) (c2 : b + e + h = 1) (c3 : c + f + i = 1) :
    (2 / 9) * (1 + ((a - 1/3)^2 + (b - 1/3)^2 + (c - 1/3)^2 + (d - 1/3)^2 + (e - 1/3)^2
      + (f - 1/3)^2 + (g - 1/3)^2 + (h - 1/3)^2 + (i - 1/3)^2) / 4)
      ≤ a*e*i + b*f*g + c*d*h + a*f*h + b*d*i + c*e*g := by
  have s1 := schur_three a b c ha hb hc
  have s2 := schur_three d e f hd he hf
  have s3 := schur_three g h i hg hh hi
  have ec : c = 1 - a - b := by linarith
  have ef : f = 1 - d - e := by linarith
  have eg : g = 1 - a - d := by linarith
  have eh : h = 1 - b - e := by linarith
  have ei : i = a + b + d + e - 1 := by linarith
  subst ec ef eg eh ei
  nlinarith [s1, s2, s3]

#print axioms qvdw_three
