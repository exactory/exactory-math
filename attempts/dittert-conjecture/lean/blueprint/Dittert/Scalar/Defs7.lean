import Dittert.Scalar.Defs11

/-!
# Scalar certificates for dimension 7

Transcribed from `attack/hall-n7-branch-coverage/COVERAGE_PROOF.md`.
Notation: `g = 7!/7^7`, `v_k = k!/k^k`, `G(k) = v_k / v_{k-1}`, `L(a,b) = v_{7-a} v_{7-b} / v_p`
with `p = 7 - a - b`.
-/

namespace Hall7

def g : ℚ := 720 / 117649
def v (k : ℕ) : ℚ := (k.factorial : ℚ) / (k : ℚ) ^ k
def L (a b : ℕ) : ℚ := v (7 - a) * v (7 - b) / v (7 - a - b)

/-- `α_k` of the ordinary and mixed exclusions. -/
def alpha (k : ℕ) : ℚ :=
  if k = 0 then 0
  else if k ≤ 3 then 14 * ((k : ℚ) / 7 + 1 / 47) * (1 - (k : ℚ) / 7 - 1 / 47)
  else 2 * (k : ℚ) * (7 - (k : ℚ)) / 7

/-- The margin `M(L, c, λ) = L - g - 49 L² / (4 (λ L + (1-g)/c))`. -/
def margin (Lv c lam : ℚ) : ℚ := Lv - g - 49 * Lv ^ 2 / (4 * (lam * Lv + (1 - g) / c))

/-- The ordinary cut constant `c = (α_a + α_b) / p²`. -/
def cOrdinary (a b : ℕ) : ℚ := (alpha a + alpha b) / ((7 - a - b : ℕ) : ℚ) ^ 2

/-- Ordinary proper cuts `(1,1),(1,2),(1,3),(1,4),(2,2),(2,3)` with `(T, λ) = (5/24, 329/24)`. -/
def OrdinaryMargins : Prop :=
  ∀ ab ∈ ([(1,1),(1,2),(1,3),(1,4),(2,2),(2,3)] : List (ℕ × ℕ)),
    0 < cOrdinary ab.1 ab.2 ∧ 0 < margin (L ab.1 ab.2) (cOrdinary ab.1 ab.2) (329/24)

/-- Mixed single-bridge cuts `(1,5),(2,4),(3,3)`: `c = α_b` when `e ≤ 0` and `c = α_a` when
`f ≤ 0`, with `(T, λ) = (3/20, 63/4)`. -/
def MixedMargins : Prop :=
  ∀ ab ∈ ([(1,5),(2,4),(3,3)] : List (ℕ × ℕ)),
    0 < alpha ab.1 ∧ 0 < alpha ab.2 ∧
    0 < margin (L ab.1 ab.2) (alpha ab.2) (63/4) ∧ 0 < margin (L ab.1 ab.2) (alpha ab.1) (63/4)

/-- `W(t) = (2/3)(1-g)^2 (1-t)^6 - g (7 - 21 t + 35 t^2)^2`. -/
noncomputable def W (t : ℝ) : ℝ :=
  (2/3) * (1 - (g : ℝ)) ^ 2 * (1 - t) ^ 6 - (g : ℝ) * (7 - 21 * t + 35 * t ^ 2) ^ 2

/-! ### The positive single-bridge certificates on the closed square `[0, 3/20]²` -/

/-- `Pa = (1 + e/a)^a (1 - e/m)^m`, `m = 7 - a`. -/
noncomputable def Pa (a : ℕ) (e : ℝ) : ℝ :=
  (1 + e / (a : ℝ)) ^ a * (1 - e / ((7 - a : ℕ) : ℝ)) ^ (7 - a)
/-- `Pb = (1 + f/b)^b (1 - f/ℓ)^ℓ`, `ℓ = 7 - b`. -/
noncomputable def Pb (b : ℕ) (f : ℝ) : ℝ :=
  (1 + f / (b : ℝ)) ^ b * (1 - f / ((7 - b : ℕ) : ℝ)) ^ (7 - b)
/-- `K = g - 2 + Pa + Pb`. -/
noncomputable def K (a b : ℕ) (e f : ℝ) : ℝ := (g : ℝ) - 2 + Pa a e + Pb b f
/-- `A0 = L(a,b) (1 - t)^7`, `t = e + f`. -/
noncomputable def A0 (a b : ℕ) (e f : ℝ) : ℝ := (L a b : ℝ) * (1 - (e + f)) ^ 7
/-- `Δ = (m - e)(ℓ - f)(1 - t)`. -/
noncomputable def Delta (a b : ℕ) (e f : ℝ) : ℝ :=
  (((7 - a : ℕ) : ℝ) - e) * (((7 - b : ℕ) : ℝ) - f) * (1 - (e + f))
/-- `Bcal = Pa E + Pb F - [(t + d) K - d A0] / (1 - t)` with `E = e/(m-e)`, `F = f/(ℓ-f)`,
`d = a`. -/
noncomputable def Bcal (a b : ℕ) (e f : ℝ) : ℝ :=
  Pa a e * (e / (((7 - a : ℕ) : ℝ) - e)) + Pb b f * (f / (((7 - b : ℕ) : ℝ) - f)) -
    (((e + f) + (a : ℝ)) * K a b e f - (a : ℝ) * A0 a b e f) / (1 - (e + f))
/-- `G = A0 - K`. -/
noncomputable def Gpoly (a b : ℕ) (e f : ℝ) : ℝ := A0 a b e f - K a b e f
/-- `N = Δ Bcal`. -/
noncomputable def Npoly (a b : ℕ) (e f : ℝ) : ℝ := Delta a b e f * Bcal a b e f
/-- `Fpoly = 2 A0 N² - 3 (K - A0)² Δ²`. -/
noncomputable def Fpoly (a b : ℕ) (e f : ℝ) : ℝ :=
  2 * A0 a b e f * Npoly a b e f ^ 2 - 3 * (K a b e f - A0 a b e f) ^ 2 * Delta a b e f ^ 2

/-- At every point of the closed square, `G > 0` or (`N > 0` and `Fpoly > 0`). -/
def BridgeCertificate (a b : ℕ) : Prop :=
  ∀ e f : ℝ, 0 ≤ e → e ≤ 3/20 → 0 ≤ f → f ≤ 3/20 →
    0 < Gpoly a b e f ∨ (0 < Npoly a b e f ∧ 0 < Fpoly a b e f)

end Hall7

namespace Dittert

/-- Obligation `s7`: the finite certificates of dimension 7. -/
def ScalarCertificates7 : Prop :=
  Hall7.OrdinaryMargins ∧ Hall7.MixedMargins ∧
  (∀ t : ℝ, 0 ≤ t → t ≤ 3/20 → 0 < Hall7.W t) ∧
  Hall7.BridgeCertificate 1 5 ∧ Hall7.BridgeCertificate 2 4 ∧ Hall7.BridgeCertificate 3 3

end Dittert
