import Cert.Check5
import Cert.Check6

/-!
# The n = 5 and n = 6 certificates, as one theorem

`certOK56` is the whole arithmetic residue of the `n = 5` and `n = 6` cases of Dittert's
conjecture.  For each of the two dimensions it

* rebuilds the symmetry-adapted monomial orbits from the group generators of `sdp_n.py`, and
  checks that their count is the number of values the certificate carries;
* assembles each Gram matrix from those orbits and the rational data of `Cert.Data5` and
  `Cert.Data6`, and checks that it is symmetric with zero row sums;
* checks positive semidefiniteness of every Gram matrix;
* expands the sum-of-squares identity against the Dittert polynomial over every monomial of
  degree 6 (593775 of them at `n = 5`, 4496388 at `n = 6`) and checks that the difference is
  zero coefficient by coefficient.

**This project depends on nothing but core Lean.**  There is no Mathlib here and no `Real`
anywhere in it: every step is a decidable computation over `Int`, `Nat` and `Float`.  That is a
claim about the residue itself, not about the tooling, and it is why the two checks can run at
all: the `n = 6` identity alone touches 4.5 million monomials with integers above `2^53`.

Two positive-semidefiniteness routes appear, and the difference matters when reading the result.

* At `n = 5`, and for the two 666 x 666 multiplier Grams at `n = 6`, the route is **exact**: an
  integer Cholesky factor whose residual is checked to be diagonally dominant with non-negative
  diagonal, so the conclusion follows by Gershgorin over the integers.
* For the 8436 x 8436 main Gram at `n = 6` the route is a **floating-point Cholesky with
  Higham's rigorous backward-error bound** (`Cert.Sym`).  It is rigorous given IEEE-754
  semantics, and it is not integer arithmetic.  The exact route at that dimension needs about
  3e11 big-integer operations and three 71-million-entry integer arrays.

The proof is `native_decide`: about 47 minutes of compiled code at `n = 5` and more at `n = 6`,
far beyond what the kernel's own reduction can do.  So the theorem rests on the axiom
`native_decide` introduces, which `#print axioms` names, in addition to Lean's standard three.
-/

/-- Both certificates verify. -/
def certOK56 (_ : Unit) : Bool := Cert5.certOK5 () && Cert6.certOK6 ()

theorem certOK56_true : certOK56 () = true := by native_decide

#print axioms certOK56_true
