import Cert.Sym
import Cert.Data5

/-!
# The n = 5 certificate check, as one computable Boolean

`certOK5` is true exactly when the certificate of `Cert/Data5.lean` passes every test:

* each Gram matrix `A` is symmetric with `A * 1 = 0`;
* `E := F^2 (A + d J) - N N^T` is diagonally dominant with nonnegative diagonal, for the
  integer Cholesky factor `N` of `F^2 (A + d J) - delta I` computed here;
* the polynomial identity `L * (Q - lambda D) = L * sigma_0 + L * sum_p x_u x_v sigma_p`
  holds coefficient by coefficient over all 593775 monomials of degree 6, `L` the common
  denominator.

Only the group generators and the orbit values are data; the monomial indexing, the orbit
structure, the Gram matrices and `N` are all recomputed here.  Every check is in `Cert.Sym`,
which `Cert/N6.lean` uses as well.
-/

namespace Cert5
open Cert

def nn : Nat := 5
def nv : Nat := 25
def dim3 : Nat := 2925
def dim2 : Nat := 325
def dim4 : Nat := 20475
def dim6 : Nat := 593775

def var (i j : Nat) : Nat := i * nn + j

/-- The five generators of `G_5 = (S_5 x S_5) semidirect Z_2`, as permutations of the cells. -/
def gens : Array (Array Nat) :=
  let rowSwap : Array Nat := #[1, 0, 2, 3, 4]
  let rowCyc  : Array Nat := #[1, 2, 3, 4, 0]
  let idp     : Array Nat := #[0, 1, 2, 3, 4]
  let mk (rp cp : Array Nat) (tr : Bool) : Array Nat := Id.run do
    let mut g : Array Nat := Array.replicate nv 0
    for i in [0:nn] do
      for j in [0:nn] do
        let (a, b) := if tr then (j, i) else (i, j)
        g := g.set! (var i j) (var (rp[a]!) (cp[b]!))
    return g
  #[mk rowSwap idp false, mk rowCyc idp false, mk idp rowSwap false, mk idp rowCyc false,
    mk idp idp true]

def mon2 : Array (Array Nat) := multisets nv 2
def mon3 : Array (Array Nat) := multisets nv 3

end Cert5
