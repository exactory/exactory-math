import Dittert.Basic

/-!
# The shared obligations of the blueprint

Each obligation of the search controller is one `Prop`. The case bridges take these `Prop`s
as explicit hypotheses, so every bridge can be checked before its premises are proved.
-/

namespace Dittert

open Matrix Finset BigOperators

/-- Reduction to boundary maximizers: if every maximizer of `Φ` on `K_n` is entrywise
positive, then Dittert's inequality holds in dimension `n` with equality only at `J_n/n`. -/
def Reduction : Prop :=
  ∀ n : ℕ, 2 ≤ n →
    (∀ A : Matrix (Fin n) (Fin n) ℝ, IsMaximizer A → ∀ i j, 0 < A i j) → Statement n

/-- Hall domination: the cut condition with parameter `λ > 0` yields a doubly stochastic `B`
with `λ B ≤ A` entrywise. -/
def HallDomination : Prop :=
  ∀ n : ℕ, 1 ≤ n → ∀ A : Matrix (Fin n) (Fin n) ℝ, (∀ i j, 0 ≤ A i j) →
    ∀ lam : ℝ, 0 < lam →
      (∀ I J : Finset (Fin n), n < I.card + J.card →
        lam * ((I.card : ℝ) + (J.card : ℝ) - (n : ℝ)) ≤ cutSum A I J) →
      ∃ B ∈ doublyStochastic ℝ (Fin n), ∀ i j, lam * B i j ≤ A i j

/-- The Gurvits permanent floors for doubly stochastic matrices: van der Waerden, and the
rectangular zero-block floor `γ_{n-a} γ_{n-b} / γ_{n-a-b}`. -/
def GurvitsFloors : Prop :=
  ∀ n : ℕ, 1 ≤ n → ∀ B ∈ doublyStochastic ℝ (Fin n),
    gamma n ≤ B.permanent ∧
    ∀ a b : ℕ, 1 ≤ a → 1 ≤ b → a + b ≤ n - 1 →
      ∀ I J : Finset (Fin n), I.card = a → J.card = b → HasZeroBlock B I J →
        gamma (n - a) * gamma (n - b) / gamma (n - a - b) ≤ B.permanent

/-- The complementary-minor entropy lemma: for a column `j` of a doubly stochastic `M` of order
`k + 1`, with `q_i = M i j` and `d_i` the permanent of `M` with row `i` and column `j` removed,
`∏_i d_i^(q_i) ≥ γ_k ∏_i (1 - q_i)^(1 - q_i)` (real powers, with `0^0 = 1`). It implies the column
entropy floor `per(M) ≥ γ_k ∏_i (1 - q_i)^(1 - q_i)` by weighted AM-GM, since `per M = ∑ q_i d_i`. -/
def CoreEntropy : Prop :=
  ∀ k : ℕ, 1 ≤ k → ∀ M ∈ doublyStochastic ℝ (Fin (k + 1)), ∀ j : Fin (k + 1),
    gamma k * ∏ i, (1 - M i j) ^ (1 - M i j) ≤
      ∏ i, ((M.submatrix (Fin.succAbove i) (Fin.succAbove j)).permanent) ^ (M i j)

/-- The zero pattern of a boundary maximizer: fully indecomposable, and two zeros in distinct
rows and distinct columns. -/
def MaximizerZeroPattern : Prop :=
  ∀ n : ℕ, 3 ≤ n → ∀ A : Matrix (Fin n) (Fin n) ℝ, IsMaximizer A → (∃ i j, A i j = 0) →
    (∀ I J : Finset (Fin n), I.card + J.card = n → 1 ≤ I.card → I.card ≤ n - 1 →
      ¬ HasZeroBlock A I J) ∧
    ∃ i₁ j₁ i₂ j₂ : Fin n, i₁ ≠ i₂ ∧ j₁ ≠ j₂ ∧ A i₁ j₁ = 0 ∧ A i₂ j₂ = 0

/-- The two-zero permanent floor `κ_n (1 + 1/(2n²))` in dimensions `8 ≤ n ≤ 10`. -/
def TwoZeroFloor : Prop :=
  ∀ n : ℕ, 8 ≤ n → n ≤ 10 → ∀ B ∈ doublyStochastic ℝ (Fin n),
    ∀ i₁ j₁ i₂ j₂ : Fin n, i₁ ≠ i₂ → j₁ ≠ j₂ → B i₁ j₁ = 0 → B i₂ j₂ = 0 →
      kappa n * (1 + 1 / (2 * (n : ℝ) ^ 2)) ≤ B.permanent

end Dittert
