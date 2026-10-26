import Certificate8
import Certificate9

theorem near_zero_certificate :
    (∀ u : ℝ, 0 ≤ u → u ≤ 1/400 → 0 < NearZero.p 8 u) ∧
    (∀ u : ℝ, 0 ≤ u → u ≤ 1/500 → 0 < NearZero.p 9 u) := by
  constructor
  · intro u hu hu1
    have hx : 0 ≤ 400*u := by positivity
    have hx1 : 400*u ≤ 1 := by linarith
    have hp := NearZero.positive8 (400*u) hx hx1
    rw [← NearZero.identity8] at hp
    have hid : (400*u)/400 = u := by ring
    rw [hid] at hp
    exact hp
  · intro u hu hu1
    have hx : 0 ≤ 500*u := by positivity
    have hx1 : 500*u ≤ 1 := by linarith
    have hp := NearZero.positive9 (500*u) hx hx1
    rw [← NearZero.identity9] at hp
    have hid : (500*u)/500 = u := by ring
    rw [hid] at hp
    exact hp
