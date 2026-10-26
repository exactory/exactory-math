# enumeration-run-3: the whole 6-part box (enumerate-small-cases-to-locate-the-threshold)

Date: 2026-09-03. Entry: enumerate-small-cases-to-locate-the-threshold, actions 1, 2, 4, 5.
Step kind: enumeration run, exhaustive over the stratum "largest length 6" of the residue R
of move 1, every instance decided exactly.

## Encoder and parameter range

`scan2.py --parts 6 --sizes 30 29 ... 6` with 10 workers and single-threaded Normaliz
(`OMP_NUM_THREADS=1`); log `scan-n6.log`, records `scan-n6.jsonl.gz`, totals
`scan-n6.summary.json`. One job per partition lam of N <= 30 with at most 6 parts; the
worker enumerates every pair (mu, nu) with |mu| + |nu| = N, mu, nu contained in lam,
mu >= nu lexicographically, no common column at length 6, largest length exactly 6, and
decides it: c by lrcalc; for c >= 3 the hive dimension by Normaliz; for dim H >= 3 the
Ehrhart quasi-polynomial by Normaliz from the rhombus inequalities of `hivepoly.py`
(same encoder as runs 1 and 2). Trusted base: Normaliz 3.11 (PyNormaliz, exact
arithmetic), lrcalc, Python integers and Fractions, the enumeration code.

## Counts

| | |
|---|---|
| canonical triples enumerated | 31,745,644 (10,254,687 at size 30; per size in `scan-n6.summary.json`) |
| c >= 3 | 6,564,885 |
| Ehrhart polynomials computed (dim H >= 3) | 4,217,762 (dimensions 3: 1,614,795; 4: 1,224,438; 5: 758,791; 6: 409,393; 7: 175,269; 8: 33,433; 9: 1,636; 10: 7) |
| period other than 1 | 0 |
| negative coefficient | 0 |
| largest vertex denominator | 1: 3,466,028; 2: 720,606; 3: 31,075; 4: 53 |

Wall time 1,883 s.

## The first value at which the answer changes

None. Minimal linear coefficient per dimension: 11/6 (3), 2 (4, the volume-2 empty
simplices, 3,088 of them), 67/30 (5, likewise, 1,098), 49/20 (6), 363/140 (7), 761/280 (8),
3827/1260 (9, above H_9), 2843/840 (10, above H_10); every other dimension's minimum is the
unimodular-simplex value H_D. The minimal coefficient ratio to the unimodular simplex is
24/25 (dimension 4). No empty non-unimodular simplex has normalized volume above 2.

## Independent check (`check.sh` -> `check.py`, `result.json` status pass)

1. Completeness: the canonical triples of every size 6..30 recounted by an independent
   generator, containment test and canonical form (no code shared with `scan2.py`):
   0 mismatches against the per-size totals.
2. Recount: 80 records (every negative one, none; the 20 with the smallest coefficient
   ratio; the 20 with the smallest linear coefficient; 40 seeded random) recounted by the
   classical lattice-word rule for t = 0..4: all 80 consistent at 5 points (no record of
   degree <= 2 exists in this run, so none is pinned by deg + 2 points).

The checker covers completeness for every size in the box and a sample of the polynomials, not each
certificate: on its own, evidence; `certified-special-case-check-2` pins every polynomial of this run by lrcalc.

## What the run decided

Evidence: no counterexample to King-Tollu-Toumazet positivity among triples with largest
length 6 and size <= 30, relative to the trusted base above.

## Correction (2026-09-04, from certified-special-case-check-4)

The polytopes this README calls "empty non-unimodular simplices" were named from their Ehrhart
polynomial (that of an empty lattice simplex of normalized volume 2, h* = (1, 0, 1, 0, ...),
c = D + 1). The vertex counts recorded by run 2 show that at 5 parts each of the 304 has 7 vertices, so at 5 parts they are not simplices (runs 3 and 4 recorded no vertex counts); read "polytopes with D + 1 lattice points, normalized
volume 2 and h* = (1, 0, 1, 0, ...)". The census of check 4 also shows that their minimal
coefficient ratio is 24/25 only in dimension 4 (44/45 in dimension 5, 799/812 in dimension 6).
