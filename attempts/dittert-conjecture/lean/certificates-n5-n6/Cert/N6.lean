import Cert.Sym
import Cert.Data6

/-!
# The n = 6 problem constants

Only the group generators, the monomial lists and the dimensions live here; every check is in
`Cert.Sym` and every number in `Cert.Data6`.  The generators follow `sdp_n.py`: `GENS` for the
main Gram and `STAB_GENS` for the two multiplier Grams, with `n = 6` substituted into the
parametric definitions there.
-/

namespace Cert6
open Cert

def nn : Nat := 6
def nv : Nat := 36
def dim3 : Nat := 8436          -- C(38, 3)
def dim2 : Nat := 666           -- C(37, 2)
def dim4 : Nat := 82251         -- C(39, 4)
def dim6 : Nat := 4496388       -- C(41, 6)

def var (i j : Nat) : Nat := i * nn + j

def idp6 : Array Nat := #[0, 1, 2, 3, 4, 5]

/-- The transposition of `i` and `j` in `[0, n)`. -/
def sw (i j : Nat) : Array Nat :=
  (Array.range nn).map (fun t => if t == i then j else if t == j then i else t)

/-- The `k`-cycle on `[lo, lo + k)`, matching `cyc` of `sdp_n.py`. -/
def cyc (k lo : Nat) : Array Nat :=
  (Array.range nn).map (fun t => if lo ≤ t && t < lo + k then lo + (t - lo + 1) % k else t)

/-- A cell permutation from a row permutation, a column permutation and a transpose flag. -/
def mkPerm (rp cp : Array Nat) (tr : Bool) : Array Nat := Id.run do
  let mut g : Array Nat := Array.replicate nv 0
  for i in [0:nn] do
    for j in [0:nn] do
      let (a, b) := if tr then (j, i) else (i, j)
      g := g.set! (var i j) (var (rp[a]!) (cp[b]!))
  return g

/-- The five generators of `G_6 = (S_6 x S_6) semidirect Z_2`, as permutations of the 36 cells. -/
def gens : Array (Array Nat) :=
  #[mkPerm (sw 0 1) idp6 false, mkPerm (cyc nn 0) idp6 false,
    mkPerm idp6 (sw 0 1) false, mkPerm idp6 (cyc nn 0) false,
    mkPerm idp6 idp6 true]

/-- The stabiliser generators of the two pair representatives, `STAB_GENS` of `sdp_n.py` at
`n = 6`: `cyc(n - 1, 1) = cyc(5, 1)` and `cyc(n - 2, 2) = cyc(4, 2)`. -/
def stabGens (typ : Nat) : Array (Array Nat) :=
  if typ == 0 then
    #[mkPerm (sw 1 2) idp6 false, mkPerm (cyc 5 1) idp6 false, mkPerm idp6 (sw 2 3) false,
      mkPerm idp6 (cyc 4 2) false, mkPerm idp6 (sw 0 1) false]
  else
    #[mkPerm (sw 2 3) idp6 false, mkPerm (cyc 4 2) idp6 false, mkPerm idp6 (sw 2 3) false,
      mkPerm idp6 (cyc 4 2) false, mkPerm (sw 0 1) (sw 0 1) false, mkPerm idp6 idp6 true]

def mon2 : Array (Array Nat) := multisets nv 2
def mon3 : Array (Array Nat) := multisets nv 3

end Cert6
