# certified-special-case-check-3: cells of the chamber complex, and a1 on all of a cell at once

Date: 2026-09-05. Entry: reduce-to-finite-witnesses, actions 1 to 4. Step kind: certified
special-case check, one certificate per cell.

## The reduction

A box search decides one triple at a time. A cell of the chamber complex is decided all at once,
and a cell is unbounded.

Write a triple as `b = (lam, mu, nu)` and the hive polytope as `H(b) = {x : A x + C b >= 0}`,
with `A` the fixed matrix of the thirty rhombus rows in the six interior entries and `C` their
fixed boundary parts. Fix `b0` with `H(b0)` full dimensional, let `V` be its vertices, and for a
vertex `v` let `T_v` be the rows tight at it and `x_v(b) = X_v b` the solution of those rows. The
**cell through `b0`** is

    Cell(b0) = { b : (A X_v + C)_i b = 0 for i in T_v, and >= 0 for i not in T_v, for every v }
               intersected with the dominance inequalities and |lam| = |mu| + |nu|.

It is a rational polyhedral cone with `b0` in its relative interior, and there are finitely many
cells, because a cell is determined by the finite datum "which rows are tight at which vertex".

On the relative interior of a cell the polytope keeps every incidence, so it keeps its face
lattice, every vertex is the same linear function of `b`, every edge keeps its direction and its
transverse cone, and every edge's lattice length is a linear function of `b`. The local
Euler-Maclaurin formula then reads

    a1(b) = sum over the edges e of alpha(transverse cone of e) * (lattice length of e)(b),

a fixed linear functional `l_C`. The same conclusion follows independently from Rassart
(arXiv:math/0308101), that the coefficient is a polynomial on each chamber, together with the
homogeneity `a_k(m b) = m^k a_k(b)`, which holds because the stretched polynomial of `m b` is the
stretched polynomial of `b` evaluated at `m t`. Hence

    a1 >= 0 on all of the cell   <=>   l_C(r) >= 0 at each extreme ray r of the cell.

That is the residue this step certifies: **the claim "a1 >= 0 for every five-part triple" holds
if and only if, for each of the finitely many cells, the functional is nonnegative at the cell's
finitely many extreme rays.** Nothing about the size of the triples survives into the residue.

## What was run

Two families of cells.

1. For each of the 2000 certified full-dimensional five-part hive polytopes of
   `certified-special-case-check-1` (the five hosts of a negative Berline-Vergne class first, then
   the 200 with the smallest linear coefficient for their size, then the rest shuffled): the cell
   through that triple, its extreme rays by the dual algorithm of Normaliz, and its functional by
   finite differences of certified Ehrhart coefficients at the sum of the rays, which lies in the
   relative interior. A certified triple of the box lies on walls, so its cell has rank below 14.
2. Cells at random points of the hive cone, where no vertex sits on a wall and the cell is full
   dimensional. There the rays are too many to take a difference along each, so the functional
   comes from fourteen differences, one per generator of the lattice of triples, and is then
   evaluated at every ray.

## Result (`cells.summary.json`, `cells.jsonl`, `result.json` status pass)

| | |
|---|---|
| cells | 2,006 |
| distinct cells | 1,347 |
| extreme rays evaluated | 9,145 |
| cells with a negative ray value | 0 |
| minimum ray value over all cells | 0 |
| maximum ray value over all cells | 143/15 |
| ray values that are exactly zero | 7,109 |
| cell ranks | 3 (213), 4 (777), 5 (742), 6 (240), 7 (32), 8 (1), 14 (1) |
| seconds | 720 |

All but the full-dimensional cell are simplicial. Every one of the 2,006 cells passes each
internal test: the functional is linear along the sampled rays at two successive steps, the ray
values reproduce the certified coefficient at the interior point, and the cell's own triple is a
nonnegative combination of the rays whose functional value is the coefficient the box certified
for it. All 6,018 spot checks at random interior lattice points agree.

So the linear coefficient is nonnegative not only at the 2,000 certified triples but on all of
1,347 distinct unbounded cones through them. The rank of a cell is the dimension of the family it
settles; rank one would be no gain, since homogeneity already gives the whole ray through a
certified triple.

One cell is full dimensional, of rank 14: the triple `(109,74,72,63,55)`, `(61,57,25,17,5)`,
`(77,52,42,23,14)`, whose hive polytope has 104 vertices, gives a cell with 321 facet
inequalities and 16 extreme rays, on which the functional takes the values 0 six times and then
1, 1, 1, 3/2, 239/60, 77/15, 28/5, 59/10, 371/60, 143/15. The linear coefficient is therefore
nonnegative on a fourteen-dimensional unbounded cone of the Littlewood-Richardson cone, and that
one certificate settles infinitely many triples of every size in an open region.

## Where the method stops

The sampler tried 24,571 further triples and reached only that one full-dimensional cell. The
reasons are recorded in `skipped`: 19,112 triples were too large for the certified Ehrhart run,
3,605 gave a hive polytope that is not full dimensional, 1,674 lay on a wall, and 178 had too
many vertices. The wall is the cost of the Ehrhart computation, which grows with the size of the
triple, while a generic triple small enough to be cheap is almost always on a wall. Taking the
functional from the local formula and the atlas of `enumeration-run-1` instead removes that wall,
since a class weight costs nothing per triple; that is the next step, not this one.

The cells built here are the ones these two sources reach, not the whole chamber complex, and the
number of cells of the complex is not known. The reduction is exact; the enumeration of its
instances is not attempted.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary against `cells.jsonl`, every field recomputed, and the recorded minimum and
   maximum of each cell against its own list of ray values.
2. The certified coefficient recorded with each cell against the value recorded independently by
   `certified-special-case-check-1` for the same triple.
3. Every extreme ray is checked to be a triple of partitions of equal size, and every cell's own
   triple to be a nonnegative combination of its rays.
4. The identity the certificate rests on, recomputed without Normaliz: for a sample of cells, the
   linear coefficient at the interior point and at that point plus an extreme ray is obtained
   from the depth-first hive enumerator of `tools/hivepoly.py` through the counts at t = 0..6 and
   an exact polynomial fit, and must reproduce the recorded ray value. This shares no code with
   the Ehrhart series algorithm the run used.

Trusted base: Normaliz 3.11 through PyNormaliz (vertices, extreme rays, Ehrhart quasi-polynomial),
the depth-first hive enumerator for the independent values, Python integers and Fractions, and the
local Euler-Maclaurin formula for rational hive polytopes as validated in `enumeration-run-1`.
