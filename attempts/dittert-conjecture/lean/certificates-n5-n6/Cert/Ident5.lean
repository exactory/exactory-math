import Cert.N5

/-!
# The polynomial identity of the n = 5 certificate, expanded over all degree-6 monomials

`Lcommon * (Q - lambda * D)` and `Lcommon * (sigma_0 + sum_p x_u x_v sigma_p)` are built as
integer coefficient vectors over the 593775 monomials of degree 6 in the 25 entries, and
`identOK` compares them.  With

  Q = n^n [ (2 - n!/n^n) (s/n)^(2D) - (prod r_i + prod c_j - per) (s/n)^eps ],
  D = (s/n)^(2D-2) (sum x_k^2 - s^2/n^2),          n = 5, D = 3, eps = 1,

this is, after multiplying by `Lcommon`,

  cS6 * s^6 - cPhi * (prod r + prod c - per) * s - cSq * s^4 * (sum x^2)
    = (Lcommon / mainDen) * sigma_0 + sum_p x_u x_v (Lcommon / multDen) * sigma_p.
-/

namespace Cert5
open Cert

def mon4 (_ : Unit) : Array (Array Nat) := multisets nv 4
def mon6 (_ : Unit) : Array (Array Nat) := multisets nv 6

/-- The stabiliser generators of the two pair representatives, matching `sdp_n.py`. -/
def stabGens (typ : Nat) : Array (Array Nat) :=
  let idp : Array Nat := #[0, 1, 2, 3, 4]
  let sw (i j : Nat) : Array Nat := (Array.range nn).map (fun t => if t == i then j else if t == j then i else t)
  let cyc (k lo : Nat) : Array Nat :=
    (Array.range nn).map (fun t => if lo ≤ t && t < lo + k then lo + (t - lo + 1) % k else t)
  let mk (rp cp : Array Nat) (tr : Bool) : Array Nat := Id.run do
    let mut g : Array Nat := Array.replicate nv 0
    for i in [0:nn] do
      for j in [0:nn] do
        let (a, b) := if tr then (j, i) else (i, j)
        g := g.set! (var i j) (var (rp[a]!) (cp[b]!))
    return g
  if typ == 0 then
    #[mk (sw 1 2) idp false, mk (cyc 4 1) idp false, mk idp (sw 2 3) false,
      mk idp (cyc 3 2) false, mk idp (sw 0 1) false]
  else
    #[mk (sw 2 3) idp false, mk (cyc 3 2) idp false, mk idp (sw 2 3) false,
      mk idp (cyc 3 2) false, mk (sw 0 1) (sw 0 1) false, mk idp idp true]

/-- Index in the degree-6 monomials of the product of two degree-3 monomials. -/
def prod33 (_ : Unit) : Array Nat := Id.run do
  let mut t : Array Nat := Array.replicate (dim3 * dim3) 0
  for a in [0:dim3] do
    let ma := mon3[a]!.toList
    for b in [0:dim3] do
      t := t.set! (a * dim3 + b) (rankMulti nv 6 ((sortNats (ma ++ mon3[b]!.toList)).toArray))
  return t

def prod22 (_ : Unit) : Array Nat := Id.run do
  let mut t : Array Nat := Array.replicate (dim2 * dim2) 0
  for a in [0:dim2] do
    let ma := mon2[a]!.toList
    for b in [0:dim2] do
      t := t.set! (a * dim2 + b) (rankMulti nv 4 ((sortNats (ma ++ mon2[b]!.toList)).toArray))
  return t

def prod42 (_ : Unit) : Array Nat := Id.run do
  let m4 := mon4 ()
  let mut t : Array Nat := Array.replicate (dim4 * dim2) 0
  for a in [0:dim4] do
    let ma := m4[a]!.toList
    for b in [0:dim2] do
      t := t.set! (a * dim2 + b) (rankMulti nv 6 ((sortNats (ma ++ mon2[b]!.toList)).toArray))
  return t

/-- Multinomial coefficient `k! / prod (multiplicities!)` of an ascending monomial. -/
def multinom (m : Array Nat) : Int := Id.run do
  let k := m.size
  let mut fact : Nat := 1
  for i in [1:k+1] do
    fact := fact * i
  let mut run : Nat := 1
  let mut den : Nat := 1
  for i in [1:k] do
    if m[i]! == m[i-1]! then
      run := run + 1
      den := den * run
    else
      run := 1
  return Int.ofNat (fact / den)

/-- The all-ones linear form to the sixth power. -/
def polyS6 (_ : Unit) : Array Int := (mon6 ()).map multinom

/-- `s^4 * (sum_k x_k^2)`. -/
def polyS4Sq (_ : Unit) : Array Int := Id.run do
  let m4 := mon4 ()
  let p42 := prod42 ()
  let sq := (Array.range nv).map (fun v => rankMulti nv 2 #[v, v])
  let mut c : Array Int := Array.replicate dim6 0
  for a in [0:dim4] do
    let coeff := multinom m4[a]!
    for v in [0:nv] do
      let idx := p42[a * dim2 + sq[v]!]!
      c := c.set! idx (c[idx]! + coeff)
  return c

/-- All permutations of `[0, n)`, as arrays. -/
partial def allPerms (k : Nat) : Array (Array Nat) := Id.run do
  let mut acc : Array (Array Nat) := #[#[]]
  for _ in [0:k] do
    let mut nxt : Array (Array Nat) := #[]
    for p in acc do
      for v in [0:k] do
        if !(p.toList.contains v) then
          nxt := nxt.push (p.push v)
    acc := nxt
  return acc

/-- `(prod_i r_i + prod_j c_j - per) * s`, as coefficients over the degree-6 monomials. -/
def polyPhiS (_ : Unit) : Array Int := Id.run do
  let mut c : Array Int := Array.replicate dim6 0
  -- one cell from each row: 5^5 choices, decoded base 5
  let mut pow : Nat := 1
  for _ in [0:nn] do
    pow := pow * nn
  for t in [0:pow] do
    let mut cells : List Nat := []
    let mut u := t
    for i in [0:nn] do
      cells := var i (u % nn) :: cells
      u := u / nn
    for v in [0:nv] do
      let idx := rankMulti nv 6 ((sortNats (v :: cells)).toArray)
      c := c.set! idx (c[idx]! + 1)
  -- one cell from each column
  for t in [0:pow] do
    let mut cells : List Nat := []
    let mut u := t
    for j in [0:nn] do
      cells := var (u % nn) j :: cells
      u := u / nn
    for v in [0:nv] do
      let idx := rankMulti nv 6 ((sortNats (v :: cells)).toArray)
      c := c.set! idx (c[idx]! + 1)
  -- minus the permanent
  for p in allPerms nn do
    let mut cells : List Nat := []
    for i in [0:nn] do
      cells := var i (p[i]!) :: cells
    for v in [0:nv] do
      let idx := rankMulti nv 6 ((sortNats (v :: cells)).toArray)
      c := c.set! idx (c[idx]! - 1)
  return c

/-- The 300 unordered pairs of distinct cells, each with its orbit type (0 = aligned,
1 = generic) and a cell permutation carrying the representative pair to it. -/
partial def transports (_ : Unit) : Array (Nat × Nat × Nat × Array Nat) := Id.run do
  let idp : Array Nat := Array.range nv
  let mut seen : Array Bool := Array.replicate (nv * nv) false
  let mut out : Array (Nat × Nat × Nat × Array Nat) := #[]
  let mut frontier : Array (Nat × Nat × Nat × Array Nat) := #[]
  let reps : Array (Nat × Nat × Nat) := #[(0, var 0 0, var 0 1), (1, var 0 0, var 1 1)]
  for r in reps do
    let (typ, u0, v0) := r
    let a := min u0 v0
    let b := max u0 v0
    if !seen[a * nv + b]! then
      seen := seen.set! (a * nv + b) true
      out := out.push (typ, a, b, idp)
      frontier := frontier.push (typ, a, b, idp)
  while frontier.size > 0 do
    let mut nxt : Array (Nat × Nat × Nat × Array Nat) := #[]
    for e in frontier do
      let (typ, u, v, perm) := e
      for g in gens do
        let a := min g[u]! g[v]!
        let b := max g[u]! g[v]!
        if !seen[a * nv + b]! then
          seen := seen.set! (a * nv + b) true
          let comp : Array Nat := perm.map (fun x => g[x]!)
          out := out.push (typ, a, b, comp)
          nxt := nxt.push (typ, a, b, comp)
    frontier := nxt
  return out

def lcmInt (a b : Int) : Int := a / (Int.gcd a b : Int) * b

/-- The full certificate check: the three Gram matrices are positive semidefinite and the
polynomial identity holds. -/
def certOK5Impl (_ : Unit) : Bool := Id.run do
  let n2D : Int := 15625            -- n ^ (2 D)
  let n2Dm2 : Int := 625            -- n ^ (2 D - 2)
  let qA : Int := 6130              -- 2 n^n - n!
  let qB : Int := 625               -- n^n / n^eps
  if lamDen != 1 then return false
  let L := lcmInt (lcmInt n2D mainDen) (lcmInt alignedDen genericDen)
  let cS6 := L * (qA + lamNum) / n2D
  let cPhi := L * qB
  let cSq := L * lamNum / n2Dm2
  if cS6 * n2D != L * (qA + lamNum) then return false
  if cSq * n2Dm2 != L * lamNum then return false
  if L % mainDen != 0 || L % alignedDen != 0 || L % genericDen != 0 then return false
  -- the Gram matrices
  let perms3 := gens.map (actIdx nv 3 mon3)
  let (idx3, cnt3) := pairOrbitIndex dim3 perms3
  if cnt3 != mainVals.size then return false
  let A3 := gram dim3 idx3 mainVals
  if !(isSymmetricZeroSum dim3 A3) then return false
  if !(choleskyCertifies dim3 A3 mainD mainF mainDelta) then return false
  let (idx2a, cnt2a) := pairOrbitIndex dim2 ((stabGens 0).map (actIdx nv 2 mon2))
  let (idx2g, cnt2g) := pairOrbitIndex dim2 ((stabGens 1).map (actIdx nv 2 mon2))
  if cnt2a != alignedVals.size || cnt2g != genericVals.size then return false
  let Aa := gram dim2 idx2a alignedVals
  let Ag := gram dim2 idx2g genericVals
  if !(isSymmetricZeroSum dim2 Aa) || !(isSymmetricZeroSum dim2 Ag) then return false
  if !(choleskyCertifies dim2 Aa alignedD alignedF alignedDelta) then return false
  if !(choleskyCertifies dim2 Ag genericD genericF genericDelta) then return false
  -- the identity
  let s6 := polyS6 ()
  let ps := polyPhiS ()
  let sq := polyS4Sq ()
  let mut acc : Array Int := Array.replicate dim6 0
  for i in [0:dim6] do
    acc := acc.set! i (cS6 * s6[i]! - cPhi * ps[i]! - cSq * sq[i]!)
  let scaleMain := L / mainDen
  let pr33 := prod33 ()
  for a in [0:dim3] do
    for b in [0:dim3] do
      let v := A3[a * dim3 + b]!
      if v != 0 then
        let idx := pr33[a * dim3 + b]!
        acc := acc.set! idx (acc[idx]! - scaleMain * v)
  let scaleAl := L / alignedDen
  let scaleGe := L / genericDen
  let pr22 := prod22 ()
  let pr42 := prod42 ()
  for e in transports () do
    let (typ, u, v, perm) := e
    let p2 := actIdx nv 2 mon2 (inverse perm)
    let A := if typ == 0 then Aa else Ag
    let sc := if typ == 0 then scaleAl else scaleGe
    let uv := rankMulti nv 2 #[u, v]
    for a in [0:dim2] do
      let pa := p2[a]!
      let base := pr22[uv * dim2 + a]!
      for b in [0:dim2] do
        let w := A[pa * dim2 + p2[b]!]!
        if w != 0 then
          let idx := pr42[base * dim2 + b]!
          acc := acc.set! idx (acc[idx]! - sc * w)
  let mut ok := true
  for i in [0:dim6] do
    if acc[i]! != 0 then ok := false
  return ok

end Cert5
