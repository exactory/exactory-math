import Mathlib

/-- Schur's inequality of degree one in the ordered case `x >= y >= z >= 0`, by the identity
`x(x-y)(x-z) + y(y-x)(y-z) + z(z-x)(z-y) = (x-y)^2 (x+y-z) + z (x-z)(y-z)`, whose two terms are
products of non-negative factors. -/
theorem schur_ordered (x y z : ℝ) (hz : 0 ≤ z) (hxy : y ≤ x) (hyz : z ≤ y) :
    0 ≤ x * (x - y) * (x - z) + y * (y - x) * (y - z) + z * (z - x) * (z - y) := by
  have hxz : z ≤ x := le_trans hyz hxy
  have hy : 0 ≤ y := le_trans hz hyz
  nlinarith [mul_nonneg (mul_self_nonneg (x - y)) (add_nonneg (sub_nonneg.2 hxz) hy),
             mul_nonneg hz (mul_nonneg (sub_nonneg.2 hxz) (sub_nonneg.2 hyz))]

/-- Schur's inequality for non-negative reals: the expression is symmetric, so order the
variables and apply the ordered case to the right permutation. -/
theorem schur_three (x y z : ℝ) (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : 0 ≤ z) :
    0 ≤ x * (x - y) * (x - z) + y * (y - x) * (y - z) + z * (z - x) * (z - y) := by
  rcases le_total y x with h1 | h1 <;> rcases le_total z y with h2 | h2 <;>
    rcases le_total z x with h3 | h3
  all_goals
    first
    | nlinarith [schur_ordered x y z hz h1 h2]
    | nlinarith [schur_ordered x z y hy h3 h2]
    | nlinarith [schur_ordered z x y hy h3 h1]
    | nlinarith [schur_ordered y x z hz h1 h3]
    | nlinarith [schur_ordered y z x hx h2 h3]
    | nlinarith [schur_ordered z y x hx h2 h1]

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
