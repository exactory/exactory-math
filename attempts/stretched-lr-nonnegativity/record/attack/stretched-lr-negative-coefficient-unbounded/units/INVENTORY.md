# Inventory: stretched-lr-negative-coefficient-unbounded

Every journal move and what its output leaves in the record, grouped by
strategy. A move marked as a fired failure signal leaves what that
strategy's Failure signal names. Convert each into a unit under
CASHOUT.md or discard it.

Walk: attack-the-negative-side -> reduce-and-translate.

Costs paid across the attack: object, obligations.

## attack-the-negative-side

- move 1 (pass 1, extract-structure-from-a-hypothetical-counterexample, paid obligations): The direction false is a journalled assumption. Any counterexample satisfies C1-C6; the conditions leave the classes S1, S2, S3, E for search and S4 for translation; no finite range and no contradiction. Deduction back to the claim: a member of S1-S4 or E with a negative coefficient refutes the claim outright; searches that find none are evidence for the claim on the sampled chambers and nothing more.
- move 2 (pass 1, test-strengthenings-by-counterexample, paid object): No counterexample: every polytope in the six families has nonnegative Ehrhart coefficients; the minimal coefficient ratio to the unimodular simplex is at least 60/49 and the minima sit at the unit-margin members (Birkhoff-type polytopes: 3628625/2436559 at B_5). The boundary sharpened: the transportation image family, in the range 3 x N (N <= 6, total <= 16), 4 x 4, 4 x 5 and 5 x 5 with small totals, is Ehrhart positive like the 3 x 8 family of Ferudun 2026, so the strip transfer yields no counterexample from small margins; a negative member, if any, needs larger margins or more rows, beyond the reach of Normaliz here (a dimension-14 member took 40 minutes, dimension 16 about a minute each at total <= 8 but hours at total 9).
- move 3 (pass 1, extract-structure-from-a-hypothetical-counterexample, failure signal fired): Evidence, and the failure signal fired. No sampled polynomial (453,799 in all) has a negative coefficient. The conditions C1-C6 of move 1 yield no further condition: the near miss that passes every one of them, the polytopes with D + 1 lattice points, normalized volume 2 and h* = (1, 0, 1, 0, ...) (ratio 24/25 in dimension 4, 44/45 in dimension 5, 799/812 in dimension 6, the box's census), recurs beyond the box exactly as inside it (run-6: 112 of the 6,000 small-nu records at 5, 6 and 7 parts; run-4: three of dimension 6 and two of dimension 7, ratio 927/938, at 8 parts), and the per-dimension minima of the linear coefficient beyond the box equal the box's (157/60 in the full-dimensional 5-part stratum; 761/280, 3827/1260, 2843/840 in dimensions 8, 9, 10 at 6 parts). The one new object is a few-point hive polytope of normalized volume 3 at 8 parts (run-4: lam = (4,4,3,3,2,2,1,1), mu = (3,3,2,2,1,1), nu = (3,2,2,1), c = 7, dimension 6, h* = (1, 0, 2, 0, 0, 0, 0), minimal ratio 393/406): the volume-2 bound of the box is a property of length <= 7, not of hives, but the h*-mechanism needs mass above 1 + H_6 30 = 74.5 at index 2 for a negative linear coefficient in dimension 6, and no sampled few-point polytope at 5, 6, 7 parts exceeds volume 2. The range left (sizes above 200 at 5 parts, above 80 at 6 parts, dimensions above 12 and sizes above 40 at 8 parts, 9 parts and more) is beyond computational reach by sampling. The record gains the condition list of move 1 with the near miss as prove-the-barrier-first's input, and the answer no to the strategy's question 4 (no compression to a finite range).

## reduce-and-translate

- move 4 (pass 1, change-the-ambient-space, failure signal fired): The failure signal fired (every candidate image lands in a space whose theory has the same ceiling as the original: Ehrhart positivity is as open for 3 x N transportation polytopes as for hives, and the other images have no map). The record gains the ceiling: the one translation in print is one-way and lands on an open positivity question with only formulas on the far side; a negative 3 x N transportation polytope with integer margins would refute the conjecture, and its search (larger margins than the codegree-3 3 x 8 family and the small-total families of run 2) is the same kind of computation as the hive search, with the same reach. The statement stays the conjecture.

## Candidate claims (declare-the-stall-and-inventory-what-stands, 2026-09-05)

Ledger: move 1 paid obligations (the direction false as a journalled assumption), move 2 paid
object (the statement moved to the transportation image for that move), moves 3 and 4 paid
nothing.

1. Computational evidence beyond the box: the sampled classes S1, S2, S3, E (runs 1, 3, 4, 5, 6)
   and the transportation families (run 2) contain no negative coefficient; the near-miss
   structure of the box recurs; one few-point polytope of normalized volume 3 appears at 8 parts.
   Evidence: the six search runs (all result.json pass). Form: counterexample-or-computational-
   evidence, ledger object (move 2). -> unit 1, carrying the problem-paper content (the
   ceilings of moves 3 and 4, the barrier in print, the open questions).
2. The necessary conditions on a counterexample (move 1): a conditional reduction of the
   negation of the conjecture to the structured classes, with the chamber consequence.
   Evidence: a proof text citing the theorems. Form: conditional-or-special-case, ledger
   obligations (move 1). -> unit 2.
3. Discarded: the translation ceiling of move 4 and the barrier of prove-the-barrier-first
   (in print, Ferudun 2026): content of unit 1 draft, not units.

## The exact state of the attack (problem-paper content)

- Entries fired: extract-structure-from-a-hypothetical-counterexample (conditions C1-C6;
  the classes; six search runs, 453,799 polynomials, no hit), test-strengthenings-by-
  counterexample (transportation families), change-the-ambient-space (the one translation in
  print is one-way and lands on an open question).
- Strategies failed: attack-the-negative-side (the near miss passes every condition; the range
  left is beyond sampling reach), reduce-and-translate (same ceiling on the far side),
  prove-the-barrier-first (the barrier for termwise local formulas is in print: the
  codimension-4 cell of Ferudun 2026).
- Open: sizes above 200 at 5 parts, above 80 at 6 parts; dimensions above 12 at 8 parts; 9
  parts and more; the infimum of the coefficient ratio (24/25 so far); few-point hive polytopes
  of volume above 3; the (HTE) statement.
