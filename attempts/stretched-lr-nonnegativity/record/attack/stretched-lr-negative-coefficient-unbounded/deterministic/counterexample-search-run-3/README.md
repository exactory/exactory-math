# counterexample-search-run-3: class S2, primitive 6-part hives of dimension >= 8 beyond the box

Date: 2026-09-04. Entry: extract-structure-from-a-hypothetical-counterexample, actions 3-4 (the
structured class S2 of move 1 searched by computation). Step kind: counterexample search run
(seeded random sampling, structured by dimension).

## Encoder and ranges

`sample_search.py` (lrcalc for c; `horn.py` for primitivity with the 521 essential Horn
triples of n = 6; Normaliz for the dimension and the Ehrhart quasi-polynomial from the hive
inequalities of `hivepoly.py`). Each worker draws triples with largest length 6 and |lam|
uniform in 31..80 (lam a random partition, mu and nu random partitions contained in lam with
|mu| + |nu| = |lam| and |nu| uniform in [|lam|/4, 3|lam|/4]), canonicalises them, and keeps a
triple when c >= 3, it is primitive, and dim H >= 8 (the hive polytope of side 6 has dimension
at most 10; the strata of dimension 8, 9, 10 are the ones where every coefficient below the top
four is open).

| file | seed | recorded | tried | primitive with c >= 3 | dimensions (8 / 9 / 10) | negatives | minimal coefficient ratio | minimal a_1 (dimension 8 / 9 / 10) |
|---|---|---|---|---|---|---|---|---|
| `s2` | 20260906 | 40,000 | 13,320,412 | 144,576 | 25,703 / 12,490 / 1,807 | 0 | 1 | 761/280 / 3827/1260 / 2843/840 |

Every polynomial has period 1; vertex denominators reach 4; sizes 31..80. Wall time 14,830 s
on 6 workers at reduced priority on a shared machine.

## Ranges searched with no hit

No sampled polynomial has a negative coefficient, and none has a coefficient below the
unimodular-simplex value: the minimal ratio is exactly 1. The minimal linear coefficient in
each dimension is the box's value again: H_8 = 761/280 in dimension 8 (attained at
lam = (15,14,13,12,9,4), mu = (14,12,9,8,1), nu = (11,10,1,1), c = 9), 3827/1260 in dimension
9 and 2843/840 in dimension 10 (the full-dimensional stratum), the same three minima as the
6-part box (`enumeration-run-3` of the box attack). The largest normalized volume among hives
with c <= D + 2 is 2.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. Every hit (a record with a negative coefficient) is re-verified against the full hypothesis:
   the tableau-polytope encoding (`tableau_polytope.py`, the lattice-word conditions, no hive
   inequality) recomputed by Normaliz must give the same polynomial and lrcalc must give c at
   t = 1 and 2. There are no hits; the check reports 0.
2. For every one of the 40,000 records, lrcalc (the classical rule) must give c at t = 1.
3. For a seeded sample of 1,500 records (seed 20260904), the tableau-polytope encoding must
   give the recorded polynomial and lrcalc the value at t = 2 when it is at most 1,000,000.
4. The summary's count equals the record count, and every record has c >= 3, is primitive
   (re-tested with `horn.py`) and has dim >= 8.

A third implementation (the lattice-word counter `lrtableaux.py`) recounts 30 seeded random
records with P(3) <= 300,000 at t = 0..3 (consistency, not a pinning: deg P <= 10 here).

Trusted base: Normaliz 3.11 (two encodings on the sample, one on the rest), lrcalc, Python
integers and Fractions, the sampling code. The polynomials outside the sample rest on Normaliz
and lrcalc at t = 1: evidence.

## What the run decided

Evidence for the claim on the sampled high-dimensional chambers of the 6-part cone beyond the
box: 40,000 primitive 6-part hives of dimension 8 to 10 and sizes 31..80 have nonnegative
coefficients, none below the simplex value, and the per-dimension minima of the linear
coefficient do not fall below the box's values.
