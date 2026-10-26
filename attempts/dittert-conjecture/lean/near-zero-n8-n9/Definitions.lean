import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Factorial.Basic

noncomputable section
namespace NearZero

def gamma (n : ℕ) : ℝ := (n.factorial : ℝ) / (n : ℝ)^n
def kappa (n : ℕ) : ℝ :=
  ((n-2).factorial : ℝ) * (((n : ℝ)-2) / ((n : ℝ)-1)^2)^(n-2)
def lower (n : ℕ) : ℝ := kappa n * (1 + 1 / (2 * (n : ℝ)^2))
def e (n : ℕ) (u : ℝ) : ℝ := 1 - (2 - gamma n) * u
def h (n : ℕ) (u : ℝ) : ℝ := (1 - gamma n) * u
def t (n : ℕ) (u : ℝ) : ℝ := e n u - h n u / ((n : ℝ)-1)
def f (n : ℕ) (u : ℝ) : ℝ := (1-u) * (1 + u / ((n : ℝ)-1))^(n-1)
def p (n : ℕ) (u : ℝ) : ℝ :=
  (2 - gamma n + lower n * (1-u)^n - f n u) * (e n u)^n -
    (e n u + h n u) * (t n u)^(n-1)

end NearZero
