# enumeration-run-5: the projected atlas of the non-full-dimensional five-part hives

Date: 2026-09-05. Entry: certify-the-finite-residue-by-computation. Approved with seven amendments
by the seventh independent review of 2026-09-05, recorded in ../../ADMISSION.md.

## Why this run

Move 11 reduced obligation O-B, the non-full-dimensional half of the rank-five rung, to the same
problem in the intrinsic lattice one dimension lower. Move 18 removed the shortcut that would have
closed the low dimensions by citation: the weight of a two-dimensional cone is already negative
when the cone is wide enough, so this project's positivity at codimensions two and three is about
cones spanned by the twenty-seven rank-five normals and not about all cones of those dimensions.
Each intrinsic dimension therefore needs its own atlas.

## The contraction, and why it needs checks the identity cannot give

contract.py translates the polytope by a lattice point of it, takes the lattice of the linear span
saturated in the ambient lattice, expresses the polytope and the hive rows in a basis of it, and
carries the induced Gram. The transverse cones are then built by transverse_q.py with that Gram in
place of the identity.

The end-to-end identity, that the local formula reproduces the certified linear coefficient, tests
validity and **cannot see the Gram**: moves 15 and 16 established that every positive-definite form
gives a valid local formula, so a wrong form would reproduce the coefficient exactly while changing
the sign census. The contraction is therefore checked directly: the intrinsic lattice is saturated,
the basis generates it rather than a sublattice, the Gram is recomputed from ambient inner products,
and it is positive definite. Carrying the induced form is a choice and not forced; a different form
would give a different sign census, as move 16 measured, twenty-one negatives against five.

## Result (projected.summary.json, types.jsonl, projected.jsonl, status pass)

| | |
|---|---|
| polytopes contracted | 444,175 |
| polytopes where the local formula reproduces the certified coefficient | 391,961 |
| identity mismatches | 0 |
| distinct types, by normal set together with the intrinsic Gram | 38,899 |
| types by intrinsic dimension | 3: 1,400; 4: 11,934; 5: 25,565 |
| types weighed, at intrinsic dimensions three and four | 13,334 |
| **types with a negative weight** | **0** |
| smallest weight | 1/120 |
| largest weight | 17/42 |
| seconds | 1,700 |

**No projected type at intrinsic dimension three or four has a negative weight**, and the smallest
is 1/120.

## What that discharges, exactly

By the nonnegative-class lemma, which root move 2 showed is rank-uniform and move 11 showed applies
verbatim in the intrinsic lattice, a polytope all of whose edge classes have nonnegative weight has
a nonnegative linear coefficient with no further computation.

- **Intrinsic dimension three is covered for the types seen**: a_3 is the volume, a_2 is half the
  sum of the facet volumes, a_1 is this atlas, and a_0 is one.
- **Intrinsic dimension four is covered except for a_2**: a_4 and a_3 are volume and facets, a_1 is
  this atlas, a_0 is one, and a_2 needs the codimension-two atlas of the two-faces, which this run
  did not build.
- **Intrinsic dimension five is enumerated and not weighed**: 25,565 types are recorded, and their
  weights are four-dimensional and are the next run.

## The completeness caveat, which is why this is not category two

The types are those that occur in the 444,175 contracted polytopes of the box, not a proof that no
other type occurs. The count was still growing when the allowance ended, from 33,252 at 624 seconds
to 38,899 at 1,700. A complete atlas is available in principle, because the intrinsic direction
space is the span of a face of the hive cone and there are finitely many, so projecting the
twenty-seven normals for each and taking subsets of size one less than the intrinsic dimension
would give one; its cost is not measured. Until then a dimension is not discharged, only covered
for the types seen.

## A bug the identity caught, recorded because it is the reason the check exists

The first version keyed a type by its normal set alone and reported 3,486 identity mismatches. The
weight depends on the intrinsic lattice as well, and two contracted polytopes can share a normal
set while carrying different lattices, so the cache returned a wrong weight for the second. Keying
by the normal set together with the Gram fixed it and the mismatches went to zero.

## Independent check (check.sh, check.py)

1. The summary recomputed from types.jsonl and projected.jsonl: 0 mismatches.
2. The identity recomputed from scratch with no cache on 8 sampled contracted polytopes, so that a
   wrong cache key cannot hide behind a right answer: 0 mismatches.
3. The contraction checks on those 8: 0 failures.
4. The seven two-dimensional weights of move 18, recomputed because a route decision rests on them,
   and the polygon identity on the unimodular triangle: 0 mismatches.

Trusted base: Normaliz 3.11 through PyNormaliz, tools/bvweight.py, the certified polynomial records
of the box attack, Python integers and Fractions, and the local Euler-Maclaurin formula for
rational hive polytopes.
