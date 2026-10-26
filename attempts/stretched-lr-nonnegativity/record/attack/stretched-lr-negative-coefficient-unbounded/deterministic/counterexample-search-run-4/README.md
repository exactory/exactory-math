# counterexample-search-run-4: class S3, primitive 8-part hives of dimension 3..12

Date: 2026-09-04. Entry: extract-structure-from-a-hypothetical-counterexample, actions 3-4 (the
structured class S3 of move 1, the first number of parts outside the box, searched by
computation). Step kind: counterexample search run (seeded random sampling, dimension capped).

## Encoder and ranges

`sample_search.py` (lrcalc for c; `horn.py` for primitivity with the 8,499 essential Horn
triples of n = 8, `horn-essential-8.json`, computed by the Knutson-Tao-Woodward criterion;
Normaliz for the dimension and the Ehrhart quasi-polynomial from the hive inequalities of
`hivepoly.py`), with `--dmax 12`: triples with largest length 8, |lam| uniform in 8..40, |nu|
uniform in [|lam|/4, 3|lam|/4], kept when primitive, c >= 3 and 3 <= dim H <= 12 (the hive
polytope of side 8 has dimension up to 21; dimensions above 12 were skipped for solver cost).

| file | seed | recorded | tried | dimensions 3..12 | negatives | minimal coefficient ratio | minimal a_1 |
|---|---|---|---|---|---|---|---|
| `s3` | 20260913 | 1,799 | at least 4,571,344 | 2, 15, 45, 75, 117, 237, 340, 363, 310, 295 | 0 | 393/406 | 11/6 |

The run was started with `--count 20000` and stopped after its first progress line (2,000
recorded, 4,571,344 tried, 20,129 s on 3 workers): at that rate the target would have taken
more than two days. The summary `s3.summary.json` was rebuilt from the 1,799 records readable
on disk (the records still in the writer's buffer at the stop were lost; `tried` is the log
line's value, a lower bound for the readable records), and `recorded` is the number of readable
records. The stopped writer left `s3.jsonl.gz` without its end-of-stream marker; that file is
kept as `raw-stopped-s3.jsonl.gz` (a name outside the checker's `s3*` glob), and `s3.jsonl.gz` is its 1,799 readable records rewritten as
a complete gzip file (the checker reads the rewritten file). Sizes 20..40 (no readable record below size 20), vertex denominators up to 6.

## Ranges searched with no hit

No sampled polynomial has a negative coefficient. Six records have a coefficient below the
unimodular-simplex value, all with D + 1 lattice points (h*_1 = 0):

- three of dimension 6 with normalized volume 2 (ratio 799/812, the box's type) and two of
  dimension 7 with volume 2 (ratio 927/938, the same h*-pattern (1, 0, 1, 0, ...) one dimension
  higher);
- one of dimension 6 with normalized volume 3: lam = (4,4,3,3,2,2,1,1), mu = (3,3,2,2,1,1),
  nu = (3,2,2,1), c = 7, P(t) = (240 + 572 t + 524 t^2 + 255 t^3 + 75 t^4 + 13 t^5 + t^6)/240,
  h*-vector (1, 0, 2, 0, 0, 0, 0) (P(1) = 7, P(2) = 30, so h*_1 = 0 and h*_2 = 2), linear
  coefficient 143/60 = H_6 - 2/30, minimal ratio 393/406 at the coefficient of t^2. This is the
  first few-point hive polytope of normalized volume above 2 in the record: the box (length
  <= 7) and every sample at 5, 6, 7 parts have none, so the bound "volume 2" is a property of
  length <= 7, not of hives in general. By the h*-mechanism a negative linear coefficient in
  dimension 6 needs h*-mass above 1 + H_6 30 = 74.5 at index 2; this polytope has 2.

The largest normalized volume among records with at most D + 2 lattice points is 6.

## Independent check (`check.sh` -> `check.py`, `result.json`)

The sampled checker of run 3 with `s3`, 8 parts, dim >= 3: every hit (negative coefficient)
re-verified from the definition (none); lrcalc at t = 1 on every record; the tableau-polytope
encoding (`tableau_polytope.py`, Normaliz) and lrcalc at t = 2 (when P(2) <= 1,000,000) on a
seeded sample of 1,500 records; the summary's count against the records and the filter
(c >= 3, dim >= 3, primitive by `horn.py` with the n = 8 triples) on every record; a third
implementation (the lattice-word counter) on 30 records at t = 0..3.

Trusted base: Normaliz 3.11, lrcalc, Python integers and Fractions, the sampling code; the
polynomials outside the sample rest on Normaliz and lrcalc at t = 1: evidence.

## What the run decided

Evidence for the claim on the sampled 8-part hives of dimension at most 12 and size at most
40: none has a negative coefficient. The record gains a few-point hive polytope of volume 3
(the class E object move 1 asked for, with h*-mass 2 at index 2), still far from the volume the
mechanism needs.

Result of the check (2026-09-04): `result.json` status pass; 0 hits; lrcalc agrees at t = 1 on all 1,799 records; the tableau-polytope encoding and lrcalc at t = 2 agree on all 1,500 sampled records; the third implementation agrees on 30 records.
