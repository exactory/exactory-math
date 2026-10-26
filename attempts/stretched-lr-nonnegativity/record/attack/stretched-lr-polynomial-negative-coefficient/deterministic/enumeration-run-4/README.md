# enumeration-run-4: the whole 7-part box (enumerate-small-cases-to-locate-the-threshold)

Date: 2026-09-04. Entry: enumerate-small-cases-to-locate-the-threshold, actions 1, 2, 4, 5.
Step kind: enumeration run, exhaustive over the stratum "largest length 7" of the residue R
of move 1, every instance decided exactly or reduced by a theorem to instances decided in
runs 2 and 3.

## Encoder and parameter range

`scan2.py --parts 7 --sizes 30 29 ... 7 --horn-filter` with 11 workers and single-threaded
Normaliz; log `scan-n7.log`, records `scan-n7.jsonl.gz`, totals `scan-n7.summary.json`.
One job per partition lam of N <= 30 with at most 7 parts; the worker enumerates every
pair (mu, nu) with |mu| + |nu| = N, mu, nu contained in lam, mu >= nu lexicographically,
no common column at length 7, largest length exactly 7, and decides it:

1. c by lrcalc (classical rule); c <= 2 is positive by theorem (P = 1 or t + 1).
2. The Horn filter (`horn.py`): the 2042 essential Horn triples (I, J, K) of n = 7 (the
   r-subsets with c^{pi(K)}_{pi(I) pi(J)} = 1, r = 1..6, computed with lrcalc; the counts
   12, 41, 142, 521, 2042 for n = 3..7, where 142 agrees with the count Ferudun 2026 reports
   for five parts). When some essential triple is saturated, sum_K lam = sum_I mu + sum_J nu,
   the King-Tollu-Toumazet factorisation theorem (J. Combin. Theory Ser. A 116 (2009), stated
   as Theorem 1.3 in Cho-Jung-Moon, DMTCS proc. AJ (2008), read in full) gives
   c = c_1 c_2 and P = P_1 P_2 for the two factor triples (lam_K, mu_I, nu_J) and
   (lam_{K^c}, mu_{I^c}, nu_{J^c}), of lengths r and 7 - r (both <= 6) and sizes <= |lam|;
   both factors are inside the box and their polynomials have nonnegative coefficients by
   Ferudun 2026 (length <= 4), by c <= 2, or by runs 2 and 3; the product therefore has
   nonnegative coefficients and the triple is skipped. Every 100th skipped triple is
   recorded with its saturated essential triple for the checker.
3. For the primitive triples: the hive dimension by Normaliz; dim H <= 2 is positive by
   theorem; otherwise the Ehrhart quasi-polynomial by Normaliz from the rhombus
   inequalities of `hivepoly.py` (same encoder as runs 1-3).

Validation of the filter before the run: the factorisation P = P_1 P_2 was checked against
Normaliz on 150 random saturated 6-part triples and, during the run, on 120 sampled skipped
7-part triples (0 failures; factor length <= 6, factor size <= 29). Trusted base: Normaliz
3.11 (PyNormaliz, exact arithmetic), lrcalc, numpy integer sums, Python integers and
Fractions, the enumeration code, and the KTT factorisation theorem.

## Counts

| | |
|---|---|
| canonical triples enumerated | 52,834,374 (18,585,439 at size 30; per size in `scan-n7.summary.json`) |
| c >= 3 | 10,516,904 |
| non-primitive (skipped by the Horn filter) | 9,201,781 |
| primitive with dim H <= 2 | 12,252 |
| Ehrhart polynomials computed (primitive, dim H >= 3) | 1,302,871 (dimensions 3: 37,726; 4: 95,556; 5: 187,745; 6: 273,415; 7: 317,104; 8: 239,177; 9: 115,385; 10: 32,360; 11: 4,195; 12: 206; 13: 2) |
| period other than 1 | 0 |
| negative coefficient | 0 |
| largest vertex denominator | 1: 545,314; 2: 604,128; 3: 139,223; 4: 13,843; 5: 297; 6: 65; 7: 1 |

Wall time 9,625 s.

## The first value at which the answer changes

None. Minimal linear coefficient per dimension: 11/6 (3), 2 (4), 67/30 (5), 29/12 (6): the
volume-2 empty simplices (h* = (1, 0, 1, 0, ...), 151, 1,632 and 1,196 of them in dimensions
4, 5, 6) sit below the simplex value H_D; from dimension 7 to 11 the minimum is exactly
H_D (unimodular simplices); dimensions 12 and 13 stay above it (92531/27720 and 124723/25740).
The minimal coefficient ratio to the unimodular simplex is 24/25 (dimension 4); no empty
non-unimodular simplex has normalized volume above 2.

## Independent check (`check.sh` -> `check.py`, `result.json` status pass)

1. Completeness: the canonical triples of every size 7..30 recounted by an independent
   generator, containment test and canonical form: 0 mismatches.
2. Horn filter: for all 93,567 recorded skipped triples, the saturation equality was
   re-evaluated from the partitions, the factor triples were rebuilt, and c = c_1 c_2 was
   confirmed by lrcalc (no hive, no Normaliz): 0 mismatches.
3. Recount: 80 records (the 20 with the smallest coefficient ratio, the 20 with the
   smallest linear coefficient, 40 seeded random) recounted by the classical lattice-word
   rule for t = 0..4: all consistent at 5 points.

The checker covers completeness for every size in the box, the skip rule on its recorded sample, and a
sample of the polynomials, not each certificate: evidence, not a proof by the skill's standard.

## What the run decided

Evidence: no counterexample to King-Tollu-Toumazet positivity among triples with largest
length 7 and size <= 30, relative to the trusted base above; with runs 2 and 3 and the
length <= 4 theorem, none in the whole box (length <= 7, size <= 30).

## Correction (2026-09-04, from certified-special-case-check-4)

The polytopes this README calls "empty non-unimodular simplices" were named from their Ehrhart
polynomial (that of an empty lattice simplex of normalized volume 2, h* = (1, 0, 1, 0, ...),
c = D + 1). The vertex counts recorded by run 2 show that at 5 parts each of the 304 has 7 vertices, so at 5 parts they are not simplices (runs 3 and 4 recorded no vertex counts); read "polytopes with D + 1 lattice points, normalized
volume 2 and h* = (1, 0, 1, 0, ...)". The census of check 4 also shows that their minimal
coefficient ratio is 24/25 only in dimension 4 (44/45 in dimension 5, 799/812 in dimension 6).
