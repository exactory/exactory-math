# enumeration-run-2: the whole 5-part box (enumerate-small-cases-to-locate-the-threshold)

Date: 2026-09-03. Entry: enumerate-small-cases-to-locate-the-threshold, actions 1, 2, 4, 5.
Step kind: enumeration run, exhaustive over the stratum "largest length 5" of the residue R
of move 1, every instance decided exactly.

## Encoder and parameter range

`scan.py --mode enumerate --parts 5 --sizes 5 .. 30` (four invocations covering sizes
5-26, 27-28, 29, 30; logs `scan-n5-*.log`, records `scan-n5-*.jsonl`). For every
partition lam of N <= 30 with at most 5 parts and every pair (mu, nu) with
|mu| + |nu| = N, mu, nu contained in lam, mu >= nu lexicographically, no common column at
length 5, and largest length exactly 5: c by lrcalc (classical rule); for c >= 3 the hive
dimension by Normaliz; for dim H >= 3 the Ehrhart quasi-polynomial by Normaliz from the
rhombus inequalities of `hivepoly.py` (validated against the published values and against
lrcalc in the workspace's `tools/`). The encoder is `scan.py` (about 200 lines) over
`hivepoly.py` (the hive model of Knutson-Tao / KTT 2006 Definition 3.1).

Trusted base: Normaliz 3.11 through PyNormaliz (exact arithmetic), lrcalc, Python integers
and Fractions, and the enumeration code.

## Counts

| | |
|---|---|
| canonical triples enumerated | 12,091,018 (per-size totals in `result.json`, e.g. 3,443,137 at size 30) |
| c <= 2 (positive by theorem) | 9,643,382 |
| c >= 3 with dim H <= 2 (positive by theorem) | 1,112,967 |
| Ehrhart polynomials computed | 1,334,669 (dimensions 3: 700,759; 4: 452,281; 5: 168,412; 6: 13,217) |
| period other than 1 | 0 |
| negative coefficient | 0 |
| largest vertex denominator | 2 (112,220 polytopes), else 1 |

Wall time: 54 + 166 + 200 + 207 s on 10 workers.

## The first value at which the answer changes

None: no triple with largest length 5 and size <= 30 has a negative coefficient. The
minimal linear coefficient in each dimension: 11/6 (dim 3), 2 (dim 4, the empty volume-2
simplices such as (5,4,3,2,1; 4,3,2,1; 2,2,1)), 137/60 (dim 5), 157/60 (dim 6, above the
simplex value 49/20). The minimal ratio of a coefficient to the unimodular-simplex value is
24/25, at the dimension-4 empty simplices; 304 empty non-unimodular simplices occur, none
of normalized volume above 2.

## Independent check (`check.sh` -> `check.py`, `result.json` status pass)

1. Completeness: the canonical triples for every size 5..30 were recounted by an
   independent partition generator, containment test, and canonical form written again in
   `check.py` (no code shared with `scan.py`): 0 mismatches against the scan's per-size
   totals (first run with sizes up to 18 on 2026-09-03; extended to every size on
   2026-09-04, `check.sh` now passes 30).
2. Recount: for 80 records (every negative one, none; the 20 with the smallest linear
   coefficient; the 20 with the smallest coefficient; 40 seeded random) the stretched
   coefficients for t = 0..min(deg + 2, 5) were recounted by the classical lattice-word
   rule (`lrtableaux.py`, no hive, no polytope, no Normaliz): every value agreed with the
   recorded polynomial (records of degree <= 3 pinned by deg + 2 points; the rest consistent
   at 6 points).

Every polynomial of the run was computed by Normaliz; this run's own checker covers the
enumeration's completeness for every size and a sample of the polynomials. The step
`certified-special-case-check-1` (2026-09-04) then pinned every one of the 1,334,669
polynomials by a second implementation (lrcalc counts at t = 0..6, exact interpolation,
0 mismatches), so the 5-part box is decided by two independent implementations that agree
on every certificate.

## What the run decided

With `certified-special-case-check-1`: a proof by computation that no counterexample to
King-Tollu-Toumazet positivity exists among triples with largest length 5 and size <= 30,
with lrcalc and Normaliz 3.11 as the trusted base; on its own, evidence.

## Correction (2026-09-04, from certified-special-case-check-4)

The polytopes this README calls "empty non-unimodular simplices" were named from their Ehrhart
polynomial (that of an empty lattice simplex of normalized volume 2, h* = (1, 0, 1, 0, ...),
c = D + 1). The vertex counts recorded by run 2 show that at 5 parts each of the 304 has 7 vertices, so at 5 parts they are not simplices (runs 3 and 4 recorded no vertex counts); read "polytopes with D + 1 lattice points, normalized
volume 2 and h* = (1, 0, 1, 0, ...)". The census of check 4 also shows that their minimal
coefficient ratio is 24/25 only in dimension 4 (44/45 in dimension 5, 799/812 in dimension 6).
