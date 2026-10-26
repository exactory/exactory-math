# symbolic-computation-run-1: the recorded data does not determine the codimension-five weights

Date: 2026-09-05. Entry: enumerate-small-cases-to-locate-the-threshold, actions 1 and 2, applied
to the linear system that the previous step's prediction proposed. Step kind: symbolic
computation run, an exact reduction over the rationals whose certificate is the reduced system
and whose independent check recomputes it modulo a prime.

## The question

A valid McMullen local formula gives one linear equation per polytope,

    a_1(P) = sum over the edges E of P of w(class(E)) * (lattice length of E),

with the unknowns indexed by the isometry classes of the transverse cone types, because the
weight is invariant under the isometries of (Z^6, standard inner product) whatever construction
produced it. Any class the system pins therefore carries the value of every valid local formula,
so its sign would settle the corresponding part of the rung without computing the Berline-Vergne
weight at all. The question of this run is whether the recorded data pins anything.

## What was computed

The 8,305 edge types of `certified-special-case-check-1` were merged into isometry classes by
`isotypes.canonical`, a backtracking search for the lexicographically least image under the
2^6 6! = 46,080 signed permutations, and the system of 2,000 equations was reduced exactly by
sparse Gauss-Jordan elimination over the rationals.

| | |
|---|---|
| edge types | 8,305 |
| isometry classes | 3,406 |
| equations | 2,000 |
| distinct equations | 466 |
| rank | 442 |
| pinned classes | 0 |
| inconsistent equations | 0 |
| time | 201 s |

The class sizes are heavily skewed: 1,508 classes hold a single type and the largest holds 31.

## What the run decided

The route fails, and the reason is structural rather than a shortage of data. Of the 2,000
polytopes only 466 give distinct equations: many canonical triples of the box carry the same hive
polytope up to lattice equivalence, so the record's size is not the number of independent
equations. The rank is 442 against 3,406 unknowns, and not one class is pinned. Enlarging the
sample does not help in the way the prediction assumed: each polytope contributes one equation
but touches hundreds of classes, and the classes grow with the sample (2,743 types at 400
polytopes, 8,305 at 2,000). A side experiment on generic polytopes with the same normals, 200
random integral right-hand sides for the 27 rhombus inequalities, makes this sharper: one of the
200 has an Ehrhart quasi-polynomial of period one and it alone has 351 edges in 351 distinct
classes, so a generic polytope is worse, not better, as a source of equations.

The one positive by-product is that the merge is consistent: no equation contradicts another
after the classes are identified, which is what a wrong identification would have produced.

The conclusion for the plan is that the codimension-five weights have to be computed, not fitted:
the defining local Euler-Maclaurin recursion has to be implemented, validated against the closed
formulas in dimensions two and three and against the coefficients this project has certified, and
evaluated on the rank-five atlas.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The rank and the pinned count recomputed modulo the prime 2^31 - 1 by an elimination written
   in the checker, sharing no code with the exact rational reduction.
2. The number of distinct equations, of classes and of occurring classes recomputed from the raw
   edge data with the class assignment read from `classes.json`.
3. The isometry merge verified where it merges: for 40 seeded random classes holding more than
   one type, an explicit signed permutation carrying one type to another is exhibited by a
   brute-force search over the group, written in the checker.

Trusted base: Python integers and Fractions; the edge data of `certified-special-case-check-1`,
whose extraction that step checked independently; the invariance of a local weight under lattice
isometries, which is the one mathematical input of the merge.
