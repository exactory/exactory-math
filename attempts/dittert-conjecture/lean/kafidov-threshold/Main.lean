import Mathlib

/-!
# Formal check 1 for the Dittert attack (2026-09-03)

Two parts.

1. The exact final inequality of the boundary-exclusion proof of Dittert's
   conjecture at `n = 16` (arXiv:2607.19439, inequality (4.3)), which is the
   only dimension-dependent step of that proof for `n > 3`:
   `K n = m_n - γ_n - n^3 m_n^2 / (4 (1 - γ_n))` with `γ_n = n!/n^n` and
   `m_n = (n-2)! ((n-2)/(n-1)^2)^(n-2)`.  `kafidov_inequality_16` shows `K 16 > 0`
   (the published argument closes `n = 16`); `kafidov_fails_15` shows `K 15 < 0`
   (it does not reach `n = 15`).  Both are kernel-checked rational arithmetic.

2. The statement of Dittert's conjecture at `n = 5`, in its quantitative form,
   as proved by the exact rational certificate `certified-special-case-check-1`
   of the attack record.  The proofs are `sorry`: the certificate has 4339
   rational orbit coordinates and a 2925 x 2925 positive semidefinite Gram
   matrix, and its formal verification is the open item recorded in
   `study/verify-formally-with-lean4.md`.
-/

/-- `γ_n = n! / n^n`. -/
def gammaN (n : ℕ) : ℚ := (Nat.factorial n : ℚ) / ((n : ℚ) ^ n)

/-- The Knopp-Sinkhorn boundary minimum `m_n = (n-2)! ((n-2)/(n-1)^2)^(n-2)`. -/
def mN (n : ℕ) : ℚ := (Nat.factorial (n - 2) : ℚ) * (((n : ℚ) - 2) / ((n : ℚ) - 1) ^ 2) ^ (n - 2)

/-- The final comparison of arXiv:2607.19439, inequality (4.3), at dimension `n`. -/
def kafidovK (n : ℕ) : ℚ := mN n - gammaN n - (n : ℚ) ^ 3 * (mN n) ^ 2 / (4 * (1 - gammaN n))

theorem factorial_16 : Nat.factorial 16 = 20922789888000 := by decide
theorem factorial_14 : Nat.factorial 14 = 87178291200 := by decide
theorem factorial_15 : Nat.factorial 15 = 1307674368000 := by decide
theorem factorial_13 : Nat.factorial 13 = 6227020800 := by decide

/-- The published boundary-exclusion argument closes `n = 16`. -/
theorem kafidov_inequality_16 : 0 < kafidovK 16 := by
  unfold kafidovK mN gammaN
  norm_num [factorial_16, factorial_14]

/-- The same argument does not reach `n = 15`: its final comparison fails. -/
theorem kafidov_fails_15 : kafidovK 15 < 0 := by
  unfold kafidovK mN gammaN
  norm_num [factorial_15, factorial_13]

open Matrix BigOperators Finset

/-- The permanent of a `5 x 5` real matrix. -/
def per5 (A : Matrix (Fin 5) (Fin 5) ℝ) : ℝ := ∑ σ : Equiv.Perm (Fin 5), ∏ i, A i (σ i)

/-- The Dittert functional `φ(A) = ∏ r_i + ∏ c_j - per A`. -/
def phi5 (A : Matrix (Fin 5) (Fin 5) ℝ) : ℝ :=
  (∏ i, ∑ j, A i j) + (∏ j, ∑ i, A i j) - per5 A

/-- Dittert's conjecture at `n = 5`, inequality part (`2 - 5!/5^5 = 2 - 120/3125`). -/
theorem dittert_five (A : Matrix (Fin 5) (Fin 5) ℝ) (hA : ∀ i j, 0 ≤ A i j)
    (hs : ∑ i, ∑ j, A i j = 5) : phi5 A ≤ 2 - 120 / 3125 := by
  sorry

/-- The quantitative form certified at `n = 5` with `c_1 = 32/3125`. -/
theorem dittert_five_stability (A : Matrix (Fin 5) (Fin 5) ℝ) (hA : ∀ i j, 0 ≤ A i j)
    (hs : ∑ i, ∑ j, A i j = 5) :
    (32 / 3125) * ∑ i, ∑ j, (A i j - 1 / 5) ^ 2 ≤ (2 - 120 / 3125) - phi5 A := by
  sorry
