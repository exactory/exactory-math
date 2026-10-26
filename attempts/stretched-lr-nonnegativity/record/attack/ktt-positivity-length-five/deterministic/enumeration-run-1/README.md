# enumeration-run-1: the codimension-five atlas at rank five, and where the local weight goes negative

Date: 2026-09-05. Entry: enumerate-small-cases-to-locate-the-threshold, actions 1, 2 and 5. Step
kind: enumeration run, exhaustive over the finite list this rung reduces to.

## What was enumerated

The linear coefficient of a full-dimensional five-part hive polytope is, by the local
Euler-Maclaurin formula transferred to the rational polytope, the sum over its edges of the
lattice length of the edge times the weight of the edge's transverse cone. The edges of the 2,000
polytopes of `certified-special-case-check-1` fall into 3,406 isometry classes
(`symbolic-computation-run-1`). This run computes the Berline-Vergne weight of every class:
`transverse.py` converts a class, given by the outward normals of the facets through the edge,
to its transverse cone (the polar of the normal cone inside the span of the normals, carrying the
projection of Z^6 as its lattice) and `bvweight.py` evaluates the defining recursion, validated
in `certified-special-case-check-2`. The 1,898 classes whose transverse cone is not simplicial
are triangulated by Normaliz without new rays and summed with the inclusion-exclusion of the
valuation property.

## Result (`atlas.summary.json`, `atlas.jsonl`, `result.json` status pass)

| | |
|---|---|
| classes | 3,406 |
| simplicial transverse cones | 1,508 |
| negative weights | 5 |
| minimum | -347/109824 |
| maximum | 906853/3628800 |
| time | 7,592 s |

The five negative classes, each with a five-part hive polytope of the box that realises it:

| class | weight | classes' types | realised in | example triple | its a_1 |
|---|---|---|---|---|---|
| 308 | -19/12096 | 4 | 129 of 2,000 | (13,5,4,3,2), (8,3,2,1), (7,3,2,1) | 43/12 |
| 1393 | -347/109824 | 2 | 21 of 2,000 | (11,6,5,4,1), (7,4,3,1), (6,3,2,1) | 211/60 |
| 1935 | -311/604800 | 1 | 2 of 2,000 | (10,7,5,4,1), (7,3,2,1), (6,4,3,1) | 77/20 |
| 2014 | -163/230400 | 1 | 3 of 2,000 | (10,7,5,4,1), (7,4,3,1), (5,4,2,1) | 73/20 |
| 3042 | -79/76800 | 1 | 1 of 2,000 | (9,7,5,4,2), (6,4,3,1), (6,4,2,1) | 22/5 |

All five transverse cones are simplicial, with five rays. Every host polytope has a positive
linear coefficient: the negative weights are outweighed by the positive ones.

## What the run decided

Termwise positivity of the Berline-Vergne weight fails at codimension five for rank five, on
cones that genuinely occur. This is the exact analogue at the next codimension of what Ferudun
2026 records at codimension four, with one difference that matters: his negative four-normal
cells "cannot be the full normal cone of a codimension-four hive face" and are repaired by a
slack closure, whereas each of the five cones here is the full normal cone of an edge of an
explicit five-part hive polytope, as the table shows and as the checker confirms. The route that
proved the top four coefficients of every full-dimensional hive, and the coefficient of t^2 at
rank five, therefore cannot be continued to the linear coefficient by the same argument: at rank
five, no proof of the rung can proceed cell by cell with this local formula.

What survives is the statement Ferudun calls (HTE): the local formula is not unique, so some
other choice may be nonnegative on these cones. The rank-five instance of that question is now
a finite linear program with an explicit base point, the 3,406 weights recorded here, and its
unknowns are the freedom of the McMullen boundary map. That is the next move.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary against `atlas.jsonl`: the record count, the count of negatives, the minimum and
   the maximum.
2. An independent value for every class whose transverse cone splits as an orthogonal sum of
   unimodular blocks of dimension at most three, and whose lattice splits with it: the weight
   must be the product of the block weights computed from the closed formulas of Castillo-Liu
   Lemmas 3.3 and 3.10, rewritten in the checker. 135 classes qualify and all 135 agree. (The
   guard matters: multiplicativity needs the lattice to split and each block to be unimodular,
   and eleven classes that satisfy neither were wrongly flagged before the guard was added.)
3. The end-to-end identity, which is what the atlas is for: for five seeded random hive polytopes,
   the sum over the edges of the class weight times the lattice length equals the linear
   coefficient the box attack certified. 0 mismatches.
4. The same identity on a polytope realising each of the five negative classes: 5 checked, 0
   mismatches. So the negative weights are not an artefact of the conversion; they sit inside
   identities that reproduce certified coefficients exactly.

Trusted base: Normaliz 3.11 (extreme rays and triangulations), Python integers and Fractions,
Proposition 4.1 of Berline-Vergne as the definition of the weight, the two closed formulas of
Castillo-Liu for the independent values, and the certified coefficients of the box attack.

## Scope

The atlas is the set of classes seen in the 2,000 polytopes of `certified-special-case-check-1`,
not a proof that no other class occurs at rank five. For the negative result that does not
matter: exhibiting five classes that occur and have negative weight is enough to close the
termwise route. For a positive result the atlas would have to be shown complete.
