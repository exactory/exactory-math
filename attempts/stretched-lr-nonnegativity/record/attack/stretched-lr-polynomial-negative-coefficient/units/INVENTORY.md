# Inventory: stretched-lr-polynomial-negative-coefficient

Every journal move and what its output leaves in the record, grouped by
strategy. A move marked as a fired failure signal leaves what that
strategy's Failure signal names. Convert each into a unit under
CASHOUT.md or discard it.

Walk: reduce-to-a-finite-computation -> reduce-and-translate.

## reduce-and-translate

- move 9 (pass 2, change-the-ambient-space, failure signal fired): The failure signal fired (every candidate image lands at the origin's ceiling, or its pull-back leaves the box): the record gains the ceiling that no translation in print or listed here reaches the box, so a negative coefficient with length <= 7 and size <= 30 could only arise inside the hive family itself, where moves 3-8 found none. The strategy's use is outside the box only (larger lengths and sizes), handed to the unbounded attack under attack/stretched-lr-negative-coefficient-unbounded.

## reduce-to-a-finite-computation

- move 1 (pass 1, reduce-to-finite-witnesses): Residue R: the claim holds iff some triple in R has a negative coefficient; the claim fails iff every triple in R has nonnegative coefficients. R is finite and the polynomial of each member is one exact Ehrhart computation (Normaliz from the rhombus inequalities; tools/hivepoly.py, validated on the published values (12,8,4)^2 -> (18,14,10,6): 1 + 7t + 18t^2 + 24t^3 with c = 50, the half-integral (5,4,3,2,1; 2,2,1; 4,3,2,1): 1 + 2t + 17/12 t^2 + 1/2 t^3 + 1/12 t^4, and 300 random triples against lrcalc). Exhaustive coverage of R is beyond reach in the box's upper strata (of the order of 10^8 triples with c > 0 at 5 parts alone, more at 6 and 7 parts), so step 4 needs the ordering step 3 supplies; the settled exclusions above are what the known bounds remove from the box.
- move 2 (pass 1, predict-the-value-and-test-it-numerically): Evidence. No negative coefficient among 9,477 polynomials. P1 confirmed: every (n, dim) stratum's minimal a_1 is H_dim at unimodular simplices, except empty non-unimodular simplices of normalized volume 2 (h* = (1,0,1,0,...), c = dim+1, small third partition such as (2,2,1)) in dimensions 4 and 5 with a_1 = 2 and 67/30. P2 refuted: a_1 grows with the vertex denominator; no negative h* entry. P3 refuted in the sample: the high-dimensional hives (up to dim 12) are fat, h* unimodal, a_1 = 4..5; every coefficient stays within 4 percent of the simplex value. Corrected prediction: inside the box the only sub-simplex structure is the empty non-unimodular hive; a negative linear coefficient by that mechanism needs normalized volume above 1 + H_D D(D-1) (27 in dim 4, 47 in dim 5, 148 in dim 6) against the observed 2. Bounds for step 4: (i) the 5-part box is small enough to decide exhaustively (about 1.7 million canonical triples with c >= 3, a few milliseconds each); (ii) at 6 and 7 parts the search is restricted to few-lattice-point large-volume hives (small c, large c(2)/c(1), c(3)), the one negative-leaning shape the data show, plus the dimension >= 9 strata.
- move 3 (pass 1, enumerate-small-cases-to-locate-the-threshold): Evidence (the checker covers a sample of the 1,334,669 certificates, not each one): among the 12,091,018 canonical triples with largest length 5 and size <= 30, 9,643,382 have c <= 2 and 1,112,967 have dim H <= 2 (positive by theorem); the remaining 1,334,669 Ehrhart polynomials (dimensions 3..6, all of period 1) have no negative coefficient. No threshold: the answer does not change anywhere in the stratum. The minimal linear coefficients per dimension are 11/6, 2, 137/60, 157/60 (dimension 6 stays above the simplex value 49/20); the minimal coefficient ratio to the unimodular simplex is 24/25 at the 304 empty non-unimodular simplices, none of normalized volume above 2. Finite-range exclusion: no counterexample with largest length 5 and size <= 30, relative to the trusted base Normaliz 3.11, lrcalc, and the enumeration code.
- move 4 (pass 1, enumerate-small-cases-to-locate-the-threshold): Evidence (sampled checker): among the 31,745,644 canonical triples with largest length 6 and size <= 30, 6,564,885 have c >= 3 and 4,217,762 of those have dim H >= 3; all 4,217,762 Ehrhart polynomials (dimensions 3..10, period 1) have nonnegative coefficients. No threshold in the stratum. Minimal linear coefficients per dimension: 11/6, 2, 67/30, 49/20, 363/140, 761/280, 3827/1260, 2843/840 (the simplex value H_D except the volume-2 empty simplices in dimensions 4 and 5, 3,088 and 1,098 of them; dimensions 9 and 10 stay above H_D); minimal coefficient ratio 24/25; vertex denominators up to 4. Finite-range exclusion: no counterexample with largest length 6 and size <= 30, relative to the trusted base Normaliz 3.11, lrcalc, and the enumeration code.
- move 5 (pass 1, enumerate-small-cases-to-locate-the-threshold): Evidence (sampled checker for the polynomials): all 1,302,871 Ehrhart polynomials of primitive 7-part hives (dimensions 3..13, period 1, vertex denominators up to 7) have nonnegative coefficients, and every non-primitive 7-part triple factorises into box triples of fewer parts. With moves 3 and 4 and Ferudun's theorem for length <= 4, the residue R of move 1 is exhausted: no triple with length <= 7 and size <= 30 has a stretched Littlewood-Richardson polynomial with a negative coefficient, relative to the trusted base (Normaliz 3.11, lrcalc, the KTT factorisation theorem, the enumeration code). The claim of this attack is therefore false on the evidence: the box contains no counterexample. Minimal linear coefficients per dimension at 7 parts: 11/6, 2, 67/30, 29/12 (volume-2 empty simplices in dimensions 4, 5, 6), then exactly H_D for dimensions 7..11, above H_D at 12 and 13; the minimal coefficient ratio to the unimodular simplex in the whole box is 24/25. The first open instances lie outside the box: size 31 at 5, 6, or 7 parts, or 8 parts.
- move 6 (pass 1, certify-the-finite-residue-by-computation): The 5-part part of the residue is closed by two independent implementations that agree on every certificate: no partitions of length <= 5 and size <= 30 give a stretched Littlewood-Richardson polynomial with a negative coefficient, with lrcalc and Normaliz 3.11 as the trusted base (a proof by computation by the skill's standard, pending the extended completeness recount of run 2). The 6-part sub-residue's pinning is running (estimated hours); the 7-part sub-residue (1,302,871 primitive polynomials of degree up to 13, plus 9.2 million factorised triples) has no independent checker for every certificate within reach (pinning needs values up to t = 15, astronomically many tableaux for the fat hives), so it stays evidence.
- move 7 (pass 1, certify-the-finite-residue-by-computation): The 6-part part of the residue is closed by two independent implementations that agree on every certificate: no partitions of largest length 6 and size <= 30 give a stretched Littlewood-Richardson polynomial with a negative coefficient, with lrcalc and Normaliz 3.11 as the trusted base (a proof by computation by the skill's standard once the extended completeness recount finishes; the sizes above 14 currently rest on the enumeration code shared with run 2, whose completeness was recounted for every size). With move 6 this settles every triple of length <= 6 and size <= 30 by two implementations. The 7-part sub-residue (1,302,871 primitive polynomials of degree up to 13, plus 9,201,781 triples reduced by the KTT factorisation theorem to triples now certified) has no independent checker within reach for every certificate (pinning needs values up to t = 15), so it stays evidence.
- move 8 (pass 1, certify-the-finite-residue-by-computation, failure signal fired): Evidence, strengthened: every 7-part polynomial of the box is reproduced by two encodings and matched by lrcalc at t = 1 (and at t = 2 where feasible), and none has a negative coefficient; but the two encodings share Normaliz as the solver, so the trusted base of the 7-part part stays large (a Normaliz defect affecting both encodings identically at t >= 3 would not show) and the two-program certification of the 5- and 6-part parts is not reached. The strategy's failure signal fires on its third bullet, the trusted base cannot be made small within reach (no second Ehrhart solver is installed; lattice-word pinning needs t = 15). The record gains the settled range, the whole box (the 5- and 6-part parts proved by two independent programs, the 7-part part evidence with a second encoding), and the first open instances: size 31 at 5, 6 or 7 parts, or 8 parts.

## Candidate claims (declare-the-stall-and-inventory-what-stands, 2026-09-04)

Ledger: every one of the nine moves paid nothing (`costs_paid` empty throughout); the walk
gave up no component, so no unit carries `object`, `obligations`, or any other cost.

1. A special case proved by computation with two independent programs: for all partitions
   lam, mu, nu with at most 6 parts, |lam| = |mu| + |nu| <= 30, every coefficient of
   P(t) = c^{t lam}_{t mu, t nu} is nonnegative. Evidence: `enumeration-run-2` and
   `enumeration-run-3` (every canonical triple of largest length 5 and 6 decided; completeness
   recounted independently for every size), `certified-special-case-check-1` and
   `certified-special-case-check-2` (every polynomial pinned by lrcalc counts and exact
   interpolation, 0 mismatches), plus the theorems the reduction cites (length <= 4, c <= 2,
   dim H <= 2, the symmetry and column-removal identities). Self-check: one sentence; a claim;
   not in the literature (the unit-level queries in `novelty.md` find the length <= 4 theorem
   and unrecorded computations, no certified box); on the path to the target. Form:
   conditional-or-special-case. -> unit 1.
2. Computational evidence for the whole box: no partitions of length <= 7 and size <= 30 give
   a negative coefficient, so the FrontierMath open problem has no solution inside its box.
   Evidence: `enumeration-run-4` (every canonical triple of largest length 7; the non-primitive
   ones reduced by the King-Tollu-Toumazet factorisation theorem to triples of unit 1) with
   `certified-special-case-check-3` (every 7-part polynomial reproduced by a second encoding in
   the same solver and matched by lrcalc at t = 1 and 2), together with unit 1's steps. The
   7-part part rests on one solver, so the form is counterexample-or-computational-evidence.
   The structural findings with the same evidence belong to this unit, tabulated by the census
   `certified-special-case-check-4` (written at stage 8 after the reader's return): among the
   6,855,302 computed polynomials exactly 7,469 have a coefficient below the unimodular-simplex
   value, all polytopes with D + 1 lattice points, volume 2 and h* = (1, 0, 1, 0, ...) in
   dimensions 4, 5, 6 (minimal ratios 24/25, 44/45, 799/812); the minimal linear coefficient
   per stratum is H_D except at those polytopes; no computed polynomial with D + 1 lattice
   points has normalized volume above 2; vertex denominators reach 7. Self-check: a
   claim; not in print; on the path (it is the target's answer). -> unit 2, with the
   problem-paper content (the state of the attack, the ceilings, the open sub-questions) in its
   draft.
3. Discarded: the residue of move 1 (follows from the cited theorems in a few lines); the
   predictions of move 2 (heuristics, folded into unit 2's draft as the tested prediction); the
   translation ceiling of move 9 (not a theorem; content of unit 2's draft, not a barrier unit).

## The exact state of the attack (problem-paper content)

- Entries fired: reduce-to-finite-witnesses (the residue), predict-the-value-and-test-it-
  numerically (the corrected prediction: inside the box the only sub-simplex structure is the
  volume-2 empty simplex), enumerate-small-cases-to-locate-the-threshold three times (the box
  exhausted at 5, 6, 7 parts), certify-the-finite-residue-by-computation three times (the
  5- and 6-part parts closed by two programs; the 7-part part by two encodings in one solver),
  change-the-ambient-space (no translation in print reaches the box).
- Strategies failed: reduce-to-a-finite-computation on its trusted-base bullet (no second
  Ehrhart solver; lattice-word pinning at t <= 15 out of reach for 1.3 million 7-part hives);
  reduce-and-translate on its ceiling bullet (every image lands at the origin's ceiling or its
  pull-back leaves the box).
- Ceiling: a second Ehrhart solver (LattE, barvinok) or a pinning of every 7-part polynomial
  would turn unit 2's 7-part part into a proof by computation.
- First open instances: size 31 at 5, 6 or 7 parts; 8 parts. Handed to the unbounded attack
  (`attack/stretched-lr-negative-coefficient-unbounded`).
