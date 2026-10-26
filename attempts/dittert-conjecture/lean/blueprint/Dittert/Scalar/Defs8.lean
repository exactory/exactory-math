import Dittert.Scalar.Defs11
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Nat.Sqrt

/-!
# Scalar certificates for dimensions 8, 9, 10

Transcribed from `attack/hall-n8-n15-branch-coverage/PROOF.md` (sections 5 and 6) and its
independent checker `deterministic/certified-witness-chain-1/independent_coverage.py`.
The near-zero polynomials follow `attack/hall-near-zero-lean-n8-n9/deterministic/formal-check-1/Definitions.lean`.
-/

namespace HallScalar

/-- The two-zero floor `L_n = κ_n (1 + 1/(2n²))`. -/
def twoZeros (n : ℕ) : ℚ := oneZero n * (1 + 1 / (2 * (n : ℚ) * n))

/-- The permanent floor of section 5 for `8 ≤ n ≤ 10`: `max(ν, L_n)` on proper cuts, `L_n`
on the marginal cut. -/
def floorLow (n a b : ℕ) : ℚ := max (floor n a b) (twoZeros n)

/-- The enclosing rational square root: the least positive multiple `k/10^6` with
`(k/10^6)^2 ≥ q`. -/
def sqrtScaled (q : ℚ) : ℕ := Nat.sqrt ((q.num.toNat * 10 ^ 12) / q.den)

def enclosingSqrt (q : ℚ) : ℚ :=
  if ((sqrtScaled q : ℚ) / 10 ^ 6) ^ 2 < q then ((sqrtScaled q + 1 : ℕ) : ℚ) / 10 ^ 6
  else (sqrtScaled q : ℚ) / 10 ^ 6

/-- `ū`, the rational enclosure of `sqrt(γ_n / C)`. -/
def upper (n a b : ℕ) : ℚ := enclosingSqrt (gamma n / curvature n a b)

/-- `β = ((1-ū)^n - 1 + n ū) / ū²`, written as the finite binomial sum. -/
def beta (n a b : ℕ) : ℚ :=
  ∑ k ∈ Finset.range (n + 1), if 2 ≤ k then (Nat.choose n k : ℚ) * (-upper n a b) ^ (k - 2) else 0

/-- The (L) margin `M - γ_n - n² M² / (4 (C + β M))`. -/
def marginLow (n a b : ℕ) : ℚ :=
  floorLow n a b - gamma n -
    (n : ℚ) ^ 2 * floorLow n a b ^ 2 / (4 * (curvature n a b + beta n a b * floorLow n a b))

/-- The complete (L) certificate of one cut in dimensions 8 to 10, including the enclosure
conditions `0 < ū < 1`, `ū² ≥ γ_n / C`, `β > 0`, and the positive denominators. -/
def GoodLow (n a b : ℕ) : Prop :=
  0 < curvature n a b ∧ 0 < upper n a b ∧ upper n a b < 1 ∧
    gamma n / curvature n a b ≤ upper n a b ^ 2 ∧ 0 < beta n a b ∧
    gamma n < floorLow n a b ∧ 0 < marginLow n a b
instance (n a b : ℕ) : Decidable (GoodLow n a b) := inferInstanceAs
  (Decidable (0 < curvature n a b ∧ 0 < upper n a b ∧ upper n a b < 1 ∧
    gamma n / curvature n a b ≤ upper n a b ^ 2 ∧ 0 < beta n a b ∧
    gamma n < floorLow n a b ∧ 0 < marginLow n a b))

/-! ### The marginal scalar functions of section 4 and 6 -/

/-- `E(u) = 1 - (2 - γ_n) u`. -/
def eFun (n : ℕ) (u : ℚ) : ℚ := 1 - (2 - gamma n) * u
/-- `H(u) = (1 - γ_n) u`. -/
def hFun (n : ℕ) (u : ℚ) : ℚ := (1 - gamma n) * u
/-- `h(u) = H(u) / E(u)`. -/
def hRatio (n : ℕ) (u : ℚ) : ℚ := hFun n u / eFun n u
/-- `f(u) = (1-u)(1 + u/(n-1))^(n-1)`. -/
def fFun (n : ℕ) (u : ℚ) : ℚ := (1 - u) * (1 + u / ((n : ℚ) - 1)) ^ (n - 1)
/-- `g(h) = (1+h)(1 - h/(n-1))^(n-1)`. -/
def gFun (n : ℕ) (h : ℚ) : ℚ := (1 + h) * (1 - h / ((n : ℚ) - 1)) ^ (n - 1)
/-- `q(u) = 2 - γ_n - (1 - h(u)/(n-1))^(n-1)`. -/
def qFun (n : ℕ) (u : ℚ) : ℚ := 2 - gamma n - (1 - hRatio n u / ((n : ℚ) - 1)) ^ (n - 1)

/-- The tail and left-endpoint conditions of section 6 at the split `s` and the stop `v`:
`E(v) > 0`, `0 ≤ h(v) < n-1`, `2 - f(v) - g(h(v)) > γ_n`, and `q(s) > 1`. -/
def TailConditions (n : ℕ) (s v : ℚ) : Prop :=
  0 < eFun n v ∧ 0 ≤ hRatio n v ∧ hRatio n v < (n : ℚ) - 1 ∧
    gamma n < 2 - fFun n v - gFun n (hRatio n v) ∧ 0 < eFun n s ∧ 1 < qFun n s
instance (n : ℕ) (s v : ℚ) : Decidable (TailConditions n s v) := inferInstanceAs
  (Decidable (0 < eFun n v ∧ 0 ≤ hRatio n v ∧ hRatio n v < (n : ℚ) - 1 ∧
    gamma n < 2 - fFun n v - gFun n (hRatio n v) ∧ 0 < eFun n s ∧ 1 < qFun n s))

end HallScalar

namespace NearZero

/-! The literal near-zero polynomials, as in the kernel-checked package. -/

noncomputable def gamma (n : ℕ) : ℝ := (n.factorial : ℝ) / (n : ℝ)^n
noncomputable def kappa (n : ℕ) : ℝ :=
  ((n-2).factorial : ℝ) * (((n : ℝ)-2) / ((n : ℝ)-1)^2)^(n-2)
noncomputable def lower (n : ℕ) : ℝ := kappa n * (1 + 1 / (2 * (n : ℝ)^2))
noncomputable def e (n : ℕ) (u : ℝ) : ℝ := 1 - (2 - gamma n) * u
noncomputable def h (n : ℕ) (u : ℝ) : ℝ := (1 - gamma n) * u
noncomputable def t (n : ℕ) (u : ℝ) : ℝ := e n u - h n u / ((n : ℝ)-1)
noncomputable def f (n : ℕ) (u : ℝ) : ℝ := (1-u) * (1 + u / ((n : ℝ)-1))^(n-1)
/-- `p_n(u) = (2 - γ_n + L_n (1-u)^n - f(u)) E^n - (E + H) T^(n-1)`. -/
noncomputable def p (n : ℕ) (u : ℝ) : ℝ :=
  (2 - gamma n + lower n * (1-u)^n - f n u) * (e n u)^n -
    (e n u + h n u) * (t n u)^(n-1)

/-- `Q = (2-γ) E^(n-1) - T^(n-1)`. -/
noncomputable def q (n : ℕ) (u : ℝ) : ℝ := (2 - gamma n) * (e n u)^(n-1) - (t n u)^(n-1)
/-- `W = (n-1+u) Q - m E^(n-1)` with `m = n-1-z`. -/
noncomputable def w (n z : ℕ) (u : ℝ) : ℝ :=
  ((n : ℝ) - 1 + u) * q n u - ((n - 1 - z : ℕ) : ℝ) * (e n u)^(n-1)
/-- The permanent floor of the support case: `max(L_n, γ_{n-z} γ_{n-1} / γ_{n-1-z})` at `n = 8`
and `L_9` at `n = 9`. -/
noncomputable def supportFloor (n z : ℕ) : ℝ :=
  if n = 8 then max (lower 8) (gamma (8 - z) * gamma 7 / gamma (7 - z)) else lower n
/-- `S = (2 - γ + M_z (1-u)^n) E^n - (E + H) T^(n-1)`. -/
noncomputable def s (n z : ℕ) (u : ℝ) : ℝ :=
  (2 - gamma n + supportFloor n z * (1-u)^n) * (e n u)^n - (e n u + h n u) * (t n u)^(n-1)
/-- The literal support polynomial `G_z = z^z Q^(n-1) S - (1-u) E^(n+(n-1)m) W^z`. -/
noncomputable def support (n z : ℕ) (u : ℝ) : ℝ :=
  (z : ℝ)^z * (q n u)^(n-1) * s n z u -
    (1 - u) * (e n u)^(n + (n-1) * (n-1-z)) * (w n z u)^z

end NearZero

namespace Dittert

/-- Obligation `s8`: the finite certificates of dimensions 8, 9, 10. -/
def ScalarCertificates8 : Prop :=
  -- (L) margins: every ordered proper cut for n = 8, 9, 10 and the marginal cut for n = 10;
  -- the two residual marginal rows (8,7,0) and (9,8,0) are the only omissions.
  (∀ n a b : ℕ, 8 ≤ n → n ≤ 10 → HallScalar.Reduced n a b →
      ¬ ((n = 8 ∨ n = 9) ∧ b = 0) → HallScalar.GoodLow n a b) ∧
  -- near-zero polynomials
  (∀ u : ℝ, 0 ≤ u → u ≤ 1/400 → 0 < NearZero.p 8 u) ∧
  (∀ u : ℝ, 0 ≤ u → u ≤ 1/500 → 0 < NearZero.p 9 u) ∧
  -- support polynomials
  (∀ z : ℕ, 1 ≤ z → z ≤ 6 → ∀ u : ℝ, 1/400 ≤ u → u ≤ 1/20 → 0 < NearZero.support 8 z u) ∧
  (∀ u : ℝ, 1/500 ≤ u → u ≤ 3/100 → 0 < NearZero.support 9 7 u) ∧
  -- tails and left endpoints
  HallScalar.TailConditions 8 (1/400) (1/20) ∧ HallScalar.TailConditions 9 (1/500) (3/100)

end Dittert
