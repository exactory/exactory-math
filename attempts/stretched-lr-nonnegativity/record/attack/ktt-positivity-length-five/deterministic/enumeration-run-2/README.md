# enumeration-run-2: the cell functional from the local formula, and a sweep of full-dimensional cells

Date: 2026-09-05. Entry: certify-the-finite-residue-by-computation, steps 1 and 3. Step kind:
enumeration run over sampled cells of the chamber complex.

## What changed

`certified-special-case-check-3` reduced the rung to the sign of a linear functional at the
extreme rays of each cell of the chamber complex, and took that functional from finite differences
of certified Ehrhart coefficients. That ties the cost to the size of the triple: the Ehrhart
computation of a six-dimensional rational polytope grows with the boundary data, so the run
reached exactly one full-dimensional cell out of 24,571 attempts.

The local Euler-Maclaurin formula gives the same functional for nothing. On a cell each edge keeps
the set of facet normals through it, hence its transverse cone and its Berline-Vergne weight,
while its lattice length is a linear function of the boundary triple, so

    l(b) = sum over the edges e of  w(class of e) * (lattice length of e)(b).

The weights are read from the codimension-five atlas of `enumeration-run-1` and computed and
cached when a class is new. Nothing in this depends on the size of the triple.

## Phase A: the two routes against each other

The functional is recomputed from the atlas on the cells of `certified-special-case-check-3`, and
its value at every extreme ray is compared with the value that step obtained from certified
Ehrhart differences. This is a comparison of two computations that share no step: one counts
lattice points in dilates, the other sums weights of transverse cones.

## Phase B: the sweep

Full-dimensional cells at generic points of the hive cone, of any size, are built and their
functional evaluated at every extreme ray. A negative value would give a family of triples with a
negative linear coefficient, that is a counterexample to the conjecture at rank five.

## Result (`cells.summary.json`, `cells.jsonl`, `result.json` status pass)

Phase A, the two routes against each other:

| | |
|---|---|
| cells | 2,006 |
| extreme rays compared | 9,145 |
| cells whose ray values differ | 0 |
| cells whose value at the triple differs | 0 |

Every ray value the previous step obtained from certified Ehrhart differences is reproduced
exactly by the local formula, and so is the certified coefficient at each cell's own triple.

Phase B, the sweep of full-dimensional cells:

| | |
|---|---|
| cells | 193, all of rank 14 |
| extreme rays evaluated | 4,764 |
| cells with a negative ray value | 0 |
| minimum ray value | 0 |
| maximum ray value | 4067/60 |
| largest triple a cell was built at | 722,265 |
| class weights held at the end | 5,142, of which 3,406 from the atlas and 1,457 computed here |
| seconds | 2,242 |

The size wall is gone: the cells were built at triples of size up to 722,265, where the certified
Ehrhart computation of the previous step is far out of reach, and the cost per cell is the edge
enumeration and the new class weights, neither of which depends on the size. 193 full-dimensional
unbounded cones of the Littlewood-Richardson cone now carry the statement `a1 >= 0`, against one
in the previous step.

No negative value appeared. Had one appeared it would have been a counterexample to the
conjecture at rank five, since the interior points of the cell near that ray are triples with a
negative linear coefficient.

## Scope

The 193 cells are a sample. The number of full-dimensional cells of the rank-five chamber complex
is not known, so what fraction of the cone they cover is not known either. The sweep skipped
1,540 sampled triples: 731 lay on a wall, 676 gave a hive polytope that is not full dimensional,
130 had more vertices than the cap of 220, and 3 had a boundary partition shorter than three
parts.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary against `cells.jsonl`, every field recomputed, and each cell's recorded minimum and
   maximum against its own list of ray values.
2. Every extreme ray is a triple of partitions of equal size.
3. The identity the sweep rests on, at a point the run never evaluated. The sum of a cell's
   extreme rays lies in the relative interior of the cell, so the linear coefficient there must be
   the sum of the ray values. The checker computes it from the Ehrhart quasi-polynomial, which the
   sweep did not use for these cells at all, on the twenty cells whose ray sum is smallest, and
   for the smallest of those again from the depth-first hive enumerator through the counts at
   t = 0..6, which shares no code with either.

Trusted base: Normaliz 3.11 through PyNormaliz, the Berline-Vergne weights of `enumeration-run-1`
and of `tools/transverse.py`, the depth-first hive enumerator for the independent values, Python
integers and Fractions, and the local Euler-Maclaurin formula for rational hive polytopes.
