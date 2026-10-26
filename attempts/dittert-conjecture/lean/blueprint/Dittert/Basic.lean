import Mathlib.LinearAlgebra.Matrix.Permanent
import Mathlib.Analysis.Convex.DoublyStochasticMatrix
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Nat.Factorial.Basic

/-!
# Dittert's conjecture: basic definitions and the statement

For a real `n × n` matrix `A` with nonnegative entries and total entry sum `n`, with row sums
`r_i` and column sums `c_j`, Dittert's functional is `Φ(A) = ∏ r_i + ∏ c_j - per(A)`, and the
conjecture states `Φ(A) ≤ 2 - n!/n^n` with equality only at the uniform matrix `J_n/n`.
-/

namespace Dittert

open Matrix Finset BigOperators

variable {n : ℕ}

/-- The row sum `r_i(A)`. -/
def rowSum (A : Matrix (Fin n) (Fin n) ℝ) (i : Fin n) : ℝ := ∑ j, A i j

/-- The column sum `c_j(A)`. -/
def colSum (A : Matrix (Fin n) (Fin n) ℝ) (j : Fin n) : ℝ := ∑ i, A i j

/-- The total entry sum. -/
def totalSum (A : Matrix (Fin n) (Fin n) ℝ) : ℝ := ∑ i, ∑ j, A i j

/-- Dittert's functional `Φ(A) = ∏ r_i + ∏ c_j - per(A)`. -/
noncomputable def Phi (A : Matrix (Fin n) (Fin n) ℝ) : ℝ :=
  (∏ i, rowSum A i) + (∏ j, colSum A j) - A.permanent

/-- `K_n`: every entry nonnegative and total entry sum `n`. -/
def Feasible (A : Matrix (Fin n) (Fin n) ℝ) : Prop :=
  (∀ i j, 0 ≤ A i j) ∧ totalSum A = n

/-- `γ_n = n! / n^n`. -/
noncomputable def gamma (n : ℕ) : ℝ := (n.factorial : ℝ) / (n : ℝ) ^ n

/-- `κ_n = (n-2)! ((n-2)/(n-1)^2)^(n-2)`, the one-zero permanent floor. -/
noncomputable def kappa (n : ℕ) : ℝ :=
  ((n - 2).factorial : ℝ) * (((n : ℝ) - 2) / ((n : ℝ) - 1) ^ 2) ^ (n - 2)

/-- `A` is the uniform matrix `J_n / n`. -/
def IsUniform (A : Matrix (Fin n) (Fin n) ℝ) : Prop := ∀ i j, A i j = 1 / (n : ℝ)

/-- Dittert's inequality with its equality case in dimension `n`. -/
def Statement (n : ℕ) : Prop :=
  ∀ A : Matrix (Fin n) (Fin n) ℝ, Feasible A →
    Phi A ≤ 2 - gamma n ∧ (Phi A = 2 - gamma n ↔ IsUniform A)

/-- The statement for every dimension in a closed integer interval. -/
def Case (lo hi : ℕ) : Prop := ∀ n : ℕ, lo ≤ n → n ≤ hi → Statement n

/-- The original claim: every dimension `5 ≤ n ≤ 15`. -/
def Root : Prop := Case 5 15

/-- `A` attains the maximum of `Φ` over `K_n`. -/
def IsMaximizer (A : Matrix (Fin n) (Fin n) ℝ) : Prop :=
  Feasible A ∧ ∀ B : Matrix (Fin n) (Fin n) ℝ, Feasible B → Phi B ≤ Phi A

/-- The sum of the entries of `A` over the rows `I` and the columns `J`. -/
def cutSum (A : Matrix (Fin n) (Fin n) ℝ) (I J : Finset (Fin n)) : ℝ := ∑ i ∈ I, ∑ j ∈ J, A i j

/-- The rows `I` and the columns `J` of `A` form a zero block. -/
def HasZeroBlock (A : Matrix (Fin n) (Fin n) ℝ) (I J : Finset (Fin n)) : Prop :=
  ∀ i ∈ I, ∀ j ∈ J, A i j = 0

end Dittert
