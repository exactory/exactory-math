# The hive polytopes are not integrally closed, and the record already showed it

Date: 2026-09-05. A derivation on data already recorded, with no run.

## The argument

Let `H` be a hive polytope of intrinsic dimension `D`, let `S` be the semigroup of lattice points
in the cone over it graded by height, so that the degree-`t` part is `tH` intersected with the
lattice and has `P(t)` elements, and let `c = |H ∩ Z^D| = P(1)`. If `S` were generated in degree
one, every degree-`t` element would be a sum of `t` degree-one elements, so

    P(t)  <=  the number of multisets of size t from c generators  =  C(t + c - 1, c - 1).

Take `c = D + 1`, which is exactly the condition `h_1 = 0`, since `h_1 = P(1) - (D + 1)`. The bound
becomes `P(t) <= C(t + D, D)`, whose leading coefficient is `1/D!`, while the leading coefficient
of `P` is the normalized volume over `D!`. So a polytope with `h_1 = 0` and normalized volume at
least two has `P(t) > C(t + D, D)` for large `t` and its semigroup is **not** generated in degree
one.

## Such polytopes are in the record, in quantity

The sign census of move 5 carries the count of records with `h_1 = 0` broken down by dimension and
normalized volume. At five parts there are 518,644 records with `h_1 = 0`, of which 304 have
dimension four and normalized volume two. At six parts there are 3,088 such records in dimension
four and 1,098 in dimension five; at seven parts 151, 1,632 and 1,196 in dimensions four, five and
six. The maximum normalized volume among `h_1 = 0` records is two at every length.

An explicit one, from `census.below1.jsonl`: `lam = (17,4,3,2,1)`, `mu = (16,3,2,1)`,
`nu = (2,2,1)`, with `D = 4`, five lattice points, normalized volume two and
`h = (1,0,1,0,0)`.

## What this settles and what it opens

It settles the question root move 5 left as the one that decides this route's value: **no**, the
hive polytopes are not all integrally closed, so the sufficient condition of root move 4 is not
what is producing the nonnegativity the census found.

That makes the census result more interesting rather than less. Nonnegative `h` held in all
6,855,302 records although the family fails the property that would have explained it, so either
some weaker property is at work or the nonnegativity is a coincidence of the box. The record does
not decide between those, and neither does anything else in the attack.

It also removes an obligation cleanly: the integral-closure question does not need its own run, its
own allowance or its own review. It was answerable from data the project already had.
