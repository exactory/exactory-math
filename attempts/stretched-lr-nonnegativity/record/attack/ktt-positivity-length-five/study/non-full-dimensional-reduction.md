# The non-full-dimensional five-part hives, reduced

Date: 2026-09-05. A derivation, with no computation in it. It settles what obligation O-B of
`ADMISSION.md` actually is, and what of the machinery built for O-A carries over to it.

## The reduction

Let `H = H(lam, mu, nu)` be the hive polytope in `R^D`, `D = 6`, and suppose `dim H = d < 6`. Let
`A = aff(H)`, let `L` be the linear subspace parallel to `A`, and let `Lambda = Z^D ∩ L`, a
lattice of rank `d` because `L` is rational.

Since `c^{lam}_{mu nu} > 0` there is a lattice point `x0 ∈ H ∩ Z^D`. For every positive integer
`t`, `t x0 ∈ Z^D` and `tH` lies in the affine subspace through `t x0` with direction `L`, so

    tH ∩ Z^D = t x0 + ( t (H - x0) ∩ Lambda ),

because a point `t x0 + z` with `z ∈ L` is in `Z^D` exactly when `z ∈ Z^D ∩ L`. Hence

    P(t) = | t (H - x0) ∩ Lambda |,

the Ehrhart function of the `d`-dimensional rational polytope `H - x0` in the rank-`d` lattice
`Lambda`. This is the intrinsic-lattice contraction the record has owed since move 2, written out.

## What carries over from moves 6 to 10, and what does not

Everything proved for O-A is a statement about a polytope and its lattice, and none of it uses the
ambient rank. So all of it holds verbatim for `(H - x0, Lambda)`:

- the coefficient is a linear functional on a cell of the chamber complex, and nonnegativity on
  the whole cell is decided at the cell's extreme rays;
- a cell all of whose edge classes have nonnegative weight needs no computation;
- the discharging rule and the per-facet identity, whose shares sum to the functional exactly.

What does not carry over is the atlas. The transverse cone of an edge of `H - x0` lives in a
quotient of `Lambda`, and its normals are the images of the rhombus normals under the projection
onto `L`, not elements of `N_5`. So the weights are not in the codimension-five atlas of
`enumeration-run-1` and have to be computed for the projected list.

## What is left, exactly

For a polytope of intrinsic dimension `d` the coefficients are `a_0` to `a_d`, and `a_0 = 1`. The
transverse cone of an edge has dimension `d - 1`. So the work divides by `d`:

| `d` | dimension of the transverse cone of an edge | tool available |
|---|---|---|
| at most 2 | at most 1 | already proved in the record, by reciprocity |
| 3 | 2 | the closed pair formula of Castillo-Liu |
| 4 | 3 | the closed formula of Castillo-Liu, Lemma 3.10 |
| 5 | 4 | the Berline-Vergne recursion of `tools/bvweight.py`, validated to dimension five |

So O-B is cheaper than O-A, not harder: its hardest case needs weights of four-dimensional cones,
one dimension below the five-dimensional cones O-A needed, and the code for them exists and is
validated. The missing input is the list itself: the transverse cone types of the projected
lattices, which nobody has enumerated here.

## The obligation this leaves

Enumerate the transverse cone types of edges of five-part hive polytopes of intrinsic dimension
3, 4 and 5, in the projected lattice, and decide the sign of their weights. That is a bounded
computational task and is therefore gated by section 2 of the interim directive; it is recorded
as a proposal in `ADMISSION.md` and is not started here.

Two things this derivation does not do. It does not prove that the weights are nonnegative on the
projected list, which is the whole question. And it does not touch O-A, whose residue is
unchanged.
