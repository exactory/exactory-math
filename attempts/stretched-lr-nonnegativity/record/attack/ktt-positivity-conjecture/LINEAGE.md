# Lineage of ktt-positivity-conjecture

This attack has no harness parent: it is a logical successor to two finished attacks, and the
skill's native child mechanism (`init --from`) requires an unfinished parent. The links below are
logical, recorded here and in `attack/SEARCH_TREE.md`, and are not harness-owned parent records.

## Predecessor checkpoint

CP-23ba531cae2da172 (`attack/checkpoints/CP-23ba531cae2da172.md`, archive
`ktt-box-and-negative-side.tar`, SHA-256 23ba531c...7315), which snapshots the closing states of
`stretched-lr-polynomial-negative-coefficient` and `stretched-lr-negative-coefficient-unbounded`.

## Inherited results, and how each is used here

| Inherited statement | Source | Status | Use in this attack |
|---|---|---|---|
| Length <= 6, size <= 30: every coefficient nonnegative | box attack `units/1` | Proof by computation, two independent programs | A verified range; it bounds where a counterexample could be and is cited in `known`, not used as a step of a proof |
| Length <= 7, size <= 30: no negative coefficient | box attack `units/2` | Evidence (7 parts on one solver) | The same, with its weaker status stated wherever it is cited |
| The census: exactly 7,469 of 6,855,302 computed polynomials fall below the simplex value, all with D + 1 lattice points, volume 2, h* = (1, 0, 1, 0, ...) | box attack `certified-special-case-check-4` | Two implementations agree | Fixes the extremal candidates and the shape of the h*-route hypothesis |
| 453,799 sampled hives beyond the box, no negative coefficient; a volume-3 few-point hive at 8 parts | unbounded attack `units/1` | Evidence | Supports direction true; the volume-3 object bounds what an h*-route hypothesis may assume |
| Necessary conditions C1-C4, C6 on any counterexample | unbounded attack `units/2` | Conditional theorem | Read in reverse: the classes a proof may restrict to (primitive triples, c >= 3, dim >= 3) |

Inheritance is by reference. Every inherited statement is checked against this attack's claim
before it is used, and the box results are finite-range facts, not steps of a general proof.

## New hypothesis

The conjecture is true, and its proof is a ladder in the number of parts n. For fixed n the
statement is finite: by Rassart each coefficient is a polynomial homogeneous of its degree on
each chamber of the Littlewood-Richardson chamber complex, so a_1 is piecewise linear and its
nonnegativity is decided at the extreme rays of the chambers; and the normal cones of the faces
of hive polytopes of side n form a finite set, so the existence of a nonnegative McMullen local
formula for that set is a finite linear program, the restriction of Ferudun's (HTE) to rank n.

## Success criterion and failure signal

Success: a rung of the ladder proved unconditionally, that is the conjecture for every triple of
length at most 5 at every size, extending Ferudun's length <= 4; then the same method at 6.
Failure signal: the rung's finite problem is out of computational reach at n = 5 (the chamber
complex or the cone enumeration explodes), or the linear program is infeasible at n = 5, which
would be a barrier for the whole local-formula class and is itself a result.

## Descendants

| Attack | Relationship | Opened | Checkpoint |
|---|---|---|---|
| ktt-positivity-length-five | Special case: the rank-five rung, every size | native child, `init --from`, at this attack's move 1 | CP-c8649a4002111252 |

The native link is recorded by the harness in `attack/ktt-positivity-length-five/parent.json`;
this attack cannot finish while that child is open, which is the intended dependency, since the
rung is part of what the root owes.
