# certified-special-case-check-1: the sign census of the h vectors

Date: 2026-09-05. Entry: replace-counting-by-an-algebraic-invariant, its test step. Approved with
eight amendments by the independent review of 2026-09-05 recorded in `../../ADMISSION.md`, which
cut the proposal from four tests to one.

## The one question this data can decide

Root move 4 proves that if the hive polytopes have the integer decomposition property then their
h vectors are nonnegative, and that nonnegative h does not give the conjecture. The question that
remains decidable on data already held is whether any h vector has a negative entry. A single
negative entry would refute nonnegativity for the family completely, and by the contrapositive of
move 4 it would also refute the integer decomposition property for that polytope.

The three tests that were dropped, and why: the asymmetry inequality of move 3 is equivalent to
the linear coefficient being nonnegative, which the box attack already certified on this data with
two independent programs, so testing it can only return a pass; monotonicity is a statement about
a nested pair and no pairs were named; Hibi's lower bound needs a lattice polytope with an
interior lattice point and no decision was stated to hang on it.

## Method

The box attack's `certified-special-case-check-4/census.py` already computes the h vector of every
polynomial by the alternating sum, and was independently checked, and never tested an entry for
negativity. `hsign.py` is that script with three additions and no other change: the smallest entry
of each h vector, the count of records with a negative entry by index, and the records that have
one.

## Result (`h-sign.summary.json`, `h-negative.jsonl`, `result.json` status pass)

| parts | polynomials | records with a negative entry | smallest entry seen |
|---|---|---|---|
| 5 | 1,334,669 | 0 | 0 |
| 6 | 4,217,762 | 0 | 0 |
| 7 | 1,302,871 | 0 | 0 |

6,855,302 polynomials, no negative entry anywhere, in 103 seconds. `h-negative.jsonl` is empty.

## What this does and does not mean

It does not make the classical inequalities available. Stanley's theorem gives nonnegative h
unconditionally for lattice polytopes, so every record whose hive polytope happens to be a lattice
polytope carries no information at all, and this census cannot separate those from the genuinely
rational ones without constructing the polytopes. What would earn the inequalities is a proof that
the hive polytopes are integrally closed, which move 4 shows is sufficient and which is registered
in the admission record as the question that decides this route's value.

It also does not touch the conjecture. Reeve's tetrahedron has nonnegative h and a negative linear
coefficient, so nonnegativity of h is a floor and the target remains the asymmetry inequality of
move 3.

What it does is remove the cheapest way the route could have died. Had one record carried a
negative entry, the route would have ended and the integer decomposition property would have been
refuted for that polytope.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary against the record files, and the emptiness of `h-negative.jsonl`.
2. An independent h vector on 590 sampled records, computed by solving the triangular system
   `P(t) = sum h_i C(t + D - i, D)` rather than by the alternating sum the run used. 0 mismatches,
   every sampled record has `h_0 = 1` and no negative entry.
3. A positive control on the detector itself, so that a census of zero is not the result of a test
   that never fires: the synthetic polynomial `1 - 2t + t^2` has `h = (1, -3, 4)` and the same code
   path flags it.

Trusted base: the box attack's certified polynomial records, its census script, Python integers and
Fractions. The seven-part records rest on one solver, so a negative entry there would have needed
re-certification; none appeared.
