# counterexample-search-run-1: class S1, primitive 5-part hives beyond the box

Date: 2026-09-04. Entry: extract-structure-from-a-hypothetical-counterexample, action 3
(a condition derived by computation: no counterexample in the sampled part of S1). Step
kind: counterexample search run (random sampling with a seed, structured by dimension).

## Encoder and ranges

`sample_search.py` (lrcalc for c; `horn.py` for primitivity with the 142 essential Horn
triples of n = 5; Normaliz for the dimension and the Ehrhart quasi-polynomial from the
hive inequalities of `hivepoly.py`). Each worker draws triples with largest length 5 and
|lam| uniform in 31..200 (lam a random partition, mu and nu random partitions contained in
lam with |mu| + |nu| = |lam|), canonicalises them, and keeps a triple when c >= 3, it is
primitive, and its hive has the required dimension.

| file | seed | dimension | recorded | tried | primitive with c >= 3 | negatives | minimal coefficient ratio | minimal a_1 |
|---|---|---|---|---|---|---|---|---|
| `s1` | 20260904 | >= 3 | 300,000 | 17,822,128 | 351,854 | 0 | 1 | 11/6 |
| `s1full` | 20260905 | 6 (full-dimensional) | 100,000 | 40,655,864 | 801,056 | 0 | 157/147 | 157/60 |

(A triple with c >= 3 that is not primitive factorises into two smaller triples by the
KTT theorem; its polynomial is a product and is nonnegative whenever the factors' are.)

## Ranges searched with no hit

No sampled polynomial has a negative coefficient. In the full-dimensional stratum, where
only the linear coefficient is open (Ferudun 2026, Theorem 3), the minimal a_1 over the
100,000 samples is 157/60, the same value as the minimum over all 13,217 full-dimensional
5-part hives of the box (enumeration-run-2), attained again by many triples; every
coefficient stays at least 157/147 times the unimodular-simplex value. In the all-dimensions
stratum the minimal coefficient ratio is exactly 1 (unimodular simplices) and no empty
non-unimodular simplex appears; the largest normalized volume among hives with c <= dim + 2
is 3 (dimension 4, c = 6, at lam = (9,9,8,5,5), mu = (8,6,3,1), nu = (8,5,3,2), size 36).

## Independent check (`check.sh` -> `check.py`, `result.json`)

For every one of the 400,000 recorded polynomials:

1. a second polytope encoding, the tableau polytope of `tableau_polytope.py` (the
   lattice-word conditions on the multiplicity matrix of a Littlewood-Richardson tableau, no
   hive inequality), computed by Normaliz, must give the same polynomial (the encoding was
   validated against the hive results on 400 box records, 60 seven-part records and 50
   beyond-box records before the check);
2. lrcalc (the classical rule) must reproduce c at t = 1, and the polynomial's value at
   t = 2 when that value is at most 1,000,000 (lrcalc enumerates tableaux, and the
   size-200 hives have millions of them already at t = 2);
3. when the polynomial's value at t = 6 is at most 2,000,000, lrcalc counts at t = 0..6 pin
   the polynomial outright (deg P <= 6 for 5 parts; a full pinning of every record by
   enumeration is out of reach for the large-size hives, whose values at t = 6 reach the
   hundreds of millions);
4. the summaries' counts equal the record counts, and every record has c >= 3, is primitive
   (re-tested with `horn.py`), and has dim H >= 3.

A third implementation (the lattice-word counter with a Lagrange interpolation) recounts 30
seeded random records with P(6) <= 200,000 and |lam| <= 40 at t = 0..6 (the counter's cost grows with the size; a first run of the checker spent hours in this phase on size-200 records).

Trusted base: Normaliz 3.11 (two encodings), lrcalc, Python integers and Fractions, the
sampling code. The polynomials of the largest hives are certified by the agreement of two
encodings in one solver plus lrcalc at t = 1, 2: evidence, not a two-program proof.

## What the run decided

Evidence for the claim on the sampled chambers of the 5-part LR cone: 400,000 primitive
5-part hives of sizes 31..200 have nonnegative coefficients; the full-dimensional
minimum of a_1 does not fall below the box's value 157/60.

Result of the check (2026-09-05): `result.json` status pass (second run of the checker, with the third-implementation sample restricted to |lam| <= 40).
