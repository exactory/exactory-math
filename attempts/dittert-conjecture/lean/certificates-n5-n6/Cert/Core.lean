/-!
# The computational core of the Dittert certificate check

Everything here is `Bool`- or `Int`-valued and computable, so that a single
`native_decide` (or, where small enough, `decide`) settles it.  Nothing in this file is a
mathematical statement about the Dittert functional; `Cert/Bridge.lean` connects it.

The data a certificate consists of is tiny: the group generators, the orbit values of the
three Gram matrices, their denominators, and two integers `d`, `F` per matrix.  Everything
else -- the monomial indexing, the orbit structure, the Gram matrices themselves and the
Cholesky factor used to certify positive semidefiniteness -- is recomputed here.

The positive semidefiniteness argument, for an integer symmetric `A` with `A * 1 = 0`:
`E := F^2 * (A + d*J) - N N^T` diagonally dominant with nonnegative diagonal gives
`A + d*J >= 0` (Gershgorin on `E`, and `N N^T >= 0`), and then `A >= 0`, because for any
`y` the vector `z := y - mean y` satisfies `J z = 0` and `y^T A y = z^T A z` (as `A 1 = 0`).
`N` is produced here by a fixed-point Cholesky; it needs no accuracy guarantee at all,
since the diagonal-dominance test on the exact integer residual is what carries the proof.
-/

namespace Cert

/-- Sorted insert into a small ascending list of variable indices. -/
def insSorted (x : Nat) : List Nat → List Nat
  | [] => [x]
  | y :: ys => if x ≤ y then x :: y :: ys else y :: insSorted x ys

def sortNats (l : List Nat) : List Nat := l.foldr insSorted []

/-- Binomials up to 64. -/
def binom : Array (Array Nat) := Id.run do
  let mut rows : Array (Array Nat) := #[]
  let mut prev : Array Nat := #[1]
  rows := rows.push prev
  for _ in [0:64] do
    let mut cur : Array Nat := #[1]
    for j in [1:prev.size] do
      cur := cur.push (prev[j-1]! + prev[j]!)
    cur := cur.push 1
    rows := rows.push cur
    prev := cur
  return rows

def C (n k : Nat) : Nat := if k > n then 0 else (binom[n]!)[k]!

/-- Multisets of size `k` from `nv` symbols, in lexicographic order, as ascending lists. -/
partial def multisets (nv k : Nat) : Array (Array Nat) := Id.run do
  let mut acc : Array (Array Nat) := #[]
  let rec go (start : Nat) (left : Nat) (cur : Array Nat) : Array (Array Nat) → Array (Array Nat) :=
    fun out =>
      if left = 0 then out.push cur
      else Id.run do
        let mut o := out
        for v in [start:nv] do
          o := go v (left - 1) (cur.push v) o
        return o
  acc := go 0 k #[] acc
  return acc

/-- Rank of an ascending multiset of size `k` from `nv` symbols, in the same order as
`multisets nv k`.  Uses the strictly-increasing transform `b i = a i + i`. -/
def rankMulti (nv k : Nat) (a : Array Nat) : Nat := Id.run do
  let m := nv + k - 1                    -- b lives in [0, m)
  let mut r : Nat := 0
  let mut prev : Nat := 0
  for i in [0:k] do
    let b := a[i]! + i
    for j in [prev:b] do
      r := r + C (m - 1 - j) (k - 1 - i)
    prev := b + 1
  return r

/-- Apply a permutation of the variables to a monomial and rank the result. -/
def actRank (nv k : Nat) (p : Array Nat) (a : Array Nat) : Nat :=
  rankMulti nv k (((sortNats (a.toList.map (fun v => p[v]!))).toArray))

end Cert

namespace Cert

/-- Parse a run of comma-separated decimal integers.  Used so that certificate data can be
carried as a string literal: array literals of a few thousand entries exceed Lean's
elaboration budget, while a string literal costs nothing. -/
def parseInts (s : String) : Array Int := Id.run do
  let b := s.toUTF8
  let mut out : Array Int := #[]
  let mut cur : Int := 0
  let mut neg : Bool := false
  let mut any : Bool := false
  for i in [0:b.size] do
    let c := (b[i]!).toNat
    if c == 45 then
      neg := true
    else if c ≥ 48 && c ≤ 57 then
      cur := cur * 10 + Int.ofNat (c - 48)
      any := true
    else
      if any then out := out.push (if neg then -cur else cur)
      cur := 0
      neg := false
      any := false
  if any then out := out.push (if neg then -cur else cur)
  return out

end Cert
