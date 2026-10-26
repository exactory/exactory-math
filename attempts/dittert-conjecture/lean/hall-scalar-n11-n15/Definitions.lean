import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Algebra.Order.Ring.Pow

namespace HallScalar

-- These direct definitions follow the explicit scalar claim, not an external result table.
def gamma (n : ℕ) : ℚ := (n.factorial : ℚ) / (n : ℚ) ^ n

def rectangle (n a b : ℕ) : ℚ := gamma (n-a) * gamma (n-b) / gamma (n-a-b)

def oneZero (n : ℕ) : ℚ := ((n-2).factorial : ℚ) *
  (((n-2 : ℕ) : ℚ) / ((n-1 : ℕ) : ℚ)^2)^(n-2)

def floor (n a b : ℕ) : ℚ := if a = 0 ∨ b = 0 then oneZero n else rectangle n a b

def curvature (n a b : ℕ) : ℚ :=
  if a = 0 ∨ b = 0 then
    (7*(n:ℚ) / (16*((n-1 : ℕ):ℚ))) * (1+(1-gamma n)^2)
  else (7*(n:ℚ)*((n-a-b : ℕ):ℚ)^2) /
    (16 * (((a*(n-a)+b*(n-b) : ℕ) : ℚ)))

def Proper (n a b : ℕ) : Prop := 0 < a ∧ 0 < b ∧ a+b < n
instance (n a b : ℕ) : Decidable (Proper n a b) := inferInstanceAs
  (Decidable (0 < a ∧ 0 < b ∧ a+b < n))

def Reduced (n a b : ℕ) : Prop := Proper n a b ∨ (a = n-1 ∧ b = 0)
instance (n a b : ℕ) : Decidable (Reduced n a b) := inferInstanceAs
  (Decidable (Proper n a b ∨ (a = n-1 ∧ b = 0)))


def Good (n a b : ℕ) : Prop :=
  0 < floor n a b ∧ 0 < curvature n a b ∧
    0 < 4*curvature n a b*(floor n a b-gamma n)-((n:ℚ)*floor n a b)^2
instance (n a b : ℕ) : Decidable (Good n a b) := inferInstanceAs
  (Decidable (0 < floor n a b ∧ 0 < curvature n a b ∧
    0 < 4*curvature n a b*(floor n a b-gamma n)-((n:ℚ)*floor n a b)^2))

end HallScalar
