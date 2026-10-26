import Tests

/-- The harness checks this declaration and all dependencies transitively. -/
theorem hall_scalar_certificate (n a b : ℕ) (hn : 11 ≤ n) (hn' : n ≤ 15)
    (hab : 0 < a+b) (hsum : a+b < n) (u P delta : ℝ) (hu : u ≤ 1)
    (hP : (HallScalar.floor n a b : ℝ)*(1-u)^n ≤ P)
    (hd : (HallScalar.curvature n a b : ℝ)*u^2 ≤ delta)
    (hb : P+delta ≤ (HallScalar.gamma n : ℝ)) : False :=
  HallScalar.scalar_exclusion n a b hn hn' hab hsum u P delta hu hP hd hb
