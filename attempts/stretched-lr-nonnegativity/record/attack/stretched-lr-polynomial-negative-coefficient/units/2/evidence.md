# Unit 2: no negative coefficient in the box (length <= 7, size <= 30)

## Statement

No integer partitions lam, mu, nu of length at most 7 and size at most 30 with
|lam| = |mu| + |nu| have a stretched Littlewood-Richardson polynomial
P(t) = c^{t lam}_{t mu, t nu} with a negative coefficient; in particular the FrontierMath open
problem "Stretched Littlewood-Richardson coefficients" (find such lam, mu, nu) has no solution
inside its box. Status: a proof by computation for at most 6 parts (unit 1, two independent
programs), and computational evidence for 7 parts (one solver, two encodings, lrcalc at t = 1
and 2).

## Evidence

**At most 6 parts.** Unit 1 (`units/1/proof.md`): enumeration runs 2 and 3, certified checks
1 and 2.

**Exactly 7 parts.** `deterministic/enumeration-run-4`: every canonical triple (mu >= nu
lexicographically, mu and nu contained in lam, neither with 7 parts) of largest length 7 and
|lam| <= 30: 52,834,374 triples; c by lrcalc; 10,516,904 have c >= 3. Of these,

- 9,201,781 are non-primitive: some essential Horn inequality (I, J, K) of rank r, 1 <= r <= 6
  (the 2042 essential triples of n = 7, `horn-essential-7.json`, computed by the
  Knutson-Tao-Woodward criterion c^{sigma_K}_{sigma_I sigma_J} = 1) holds with equality. By the
  King-Tollu-Toumazet factorisation theorem (King, Tollu, Toumazet, J. Combin. Theory Ser. A 116
  (2009); Cho, Jung, Moon 2008, Theorem 1.3) P is the product of the polynomials of the two
  sub-triples indexed by (I, J, K) and their complements, of lengths r and 7 - r and sizes at
  most 30, both nonnegative by unit 1; so P is nonnegative. The run records every hundredth
  skipped triple with its saturated inequality; the checker re-verifies the saturation, the
  factor triples and c = c1 c2 by lrcalc on all 93,567 recorded ones (0 mismatches), and the
  identity P = P1 P2 was verified against Normaliz on 150 saturated 6-part triples before the
  run and on 120 sampled skipped 7-part triples during it.
- 1,315,123 are primitive; 1,302,871 of them have dim H >= 3 (the rest have dim H <= 2 and
  nonnegative coefficients by reciprocity, unit 1, fact F6). Normaliz computed the Ehrhart
  quasi-polynomial of H for all 1,302,871: every one has period 1, dimensions 3..13, vertex
  denominators up to 7, and no negative coefficient (`scan-n7.summary.json`; `result.json`
  status pass).

**Certification of the 7-part polynomials.** `deterministic/certified-special-case-check-3`:
every one of the 1,302,871 polynomials was recomputed from a second encoding, the tableau
polytope (the column-strictness and lattice-word inequalities on the multiplicity matrix of a
Littlewood-Richardson tableau, `tableau_polytope.py`, sharing no code with the hive encoder),
with Normaliz: all agree. lrcalc recomputed c^{lam}_{mu nu} and c^{2 lam}_{2 mu, 2 nu} for
every record: all agree. The checker re-runs the second encoding on 313 records and a third
implementation (the lattice-word counter) on 30 records at t = 0..3 (`result.json` status
pass). Pinning by lattice-word counts is out of reach (deg P <= 15 needs values at t <= 15;
the fat hives have astronomically many tableaux there), and no second Ehrhart solver is
installed, so both encodings share Normaliz's Ehrhart-series computation: the 7-part part is
evidence, not a two-program proof.

**Completeness of run 4.** `check.sh` recounts the canonical triples of every size 7..30 by
the independent generator: 0 mismatches (`enumeration-run-4/result.json`, status pass).

## Structural findings with the same evidence

A census of all 6,855,302 computed polynomials (`deterministic/certified-special-case-check-4`,
two implementations that agree; `result.json` status pass) computes from the recorded
coefficients the ratios of every coefficient to the corresponding coefficient of the unimodular
simplex, the normalized volume and the h*-vector; the first and third findings below are its outputs, the others come from the READMEs of runs 2 to 4:

- Exactly 7,469 computed polynomials have a coefficient below the simplex value: 3,543 of
  dimension 4 (304, 3,088, 151 at 5, 6, 7 parts; h* = (1, 0, 1, 0, 0), volume 2, minimal ratio
  24/25), 2,730 of dimension 5 (1,098, 1,632 at 6, 7 parts; h* = (1, 0, 1, 0, 0, 0), volume 2,
  minimal ratio 44/45), and 1,196 of dimension 6 (7 parts; h* = (1, 0, 1, 0, 0, 0, 0), volume 2,
  minimal ratio 799/812). Every other computed polynomial has every coefficient at least the
  simplex value; the minimal ratio over all computed polynomials is 24/25. These polytopes have
  D + 1 lattice points and the Ehrhart polynomial of an empty lattice simplex of volume 2 and at 5 parts are not simplices (each of the 304 has 7 vertices); runs 3 and 4 recorded no vertex counts, but run 1's sample holds 12 six-part and 28 seven-part ones (dimensions 4 and 5, with 7 and 8 vertices, so not simplices), and the rest, including every dimension-6 one, are not known either way.
- The minimal linear coefficient per (n, D) stratum is the unimodular-simplex value
  H_D = 1 + 1/2 + ... + 1/D except at those polytopes (H_D - 1/(D(D-1)): 2, 67/30, 29/12) and in
  the strata where it lies above H_D (dimensions 9, 10 at 6 parts; 12, 13 at 7 parts; 6 at 5
  parts, the full-dimensional stratum, where only a_1 is open by Ferudun 2026, Theorem 3, with
  minimum 157/60 > H_6 = 49/20).
- No computed polynomial with D + 1 lattice points has normalized volume above 2; among those
  with at most D + 2 lattice points the largest normalized volume is 3 at 5 parts and 10 at 6
  and 7 parts. A negative linear coefficient by the few-point mechanism alone, with the
  h*-mass at index 2, would need normalized volume above 1 + H_D D(D-1) (27 in dimension 4, 47
  in dimension 5, 75 in dimension 6).
- Every polynomial in the box has period 1 (as Derksen-Weyman requires); the largest vertex denominator among the computed polynomials is 2 at 5 parts, 4 at 6 parts and 7 at 7 parts.
- Outside the census: the hive polytopes of dimension at most 2 (never computed) and the
  products of the non-primitive 7-part triples.

## Beyond the box (evidence from the sibling attack, `attack/stretched-lr-negative-coefficient-unbounded`)

5,170 transportation polytopes of the families 3 x 4, 3 x 5, 3 x 6, 4 x 4, 4 x 5, 5 x 5 with
small margins (`counterexample-search-run-2`, `result.json` status pass; the 3 x N ones images of Littlewood-Richardson polytopes under the strip construction of Ferudun 2026, which is stated for three strips; the k x N case for k >= 4 is not in print) have no negative coefficient.
(The sibling attack's `counterexample-search-run-1`, a seeded sampling of 400,000 primitive
5-part hives of sizes 31..200, is not cited here: its checker had not passed when this unit
was written.)

## Reproduction

`enumeration-run-4` takes 9,625 s on 11 single-threaded Normaliz workers;
`certified-special-case-check-3` takes 6,667 s on 8 workers; the census
`certified-special-case-check-4` takes 796 s on 6 workers. Each enumeration directory holds its
code and `input.json`, its records and logs (and summaries for runs 3 and 4), `README.md`, `check.sh` and
`result.json`; each certified-special-case-check directory holds its verification or census
script, its log and summary, `check.sh`, `README.md` and `result.json`, and reads the records
of the runs it certifies.
