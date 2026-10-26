# counterexample-search-run-6: class E in the small-third-partition corner beyond the box

Date: 2026-09-04. Entry: extract-structure-from-a-hypothetical-counterexample, actions 3-4 (the
structured class E of move 1, in the corner where the box's near-misses live). Step kind:
counterexample search run (seeded random sampling, structured by the number of lattice points
and by the size of the smaller partition).

## Encoder and ranges

As run 5 (`sample_search.py` with `--cmax-excess 2`: primitive, c >= 3, dim H >= 3, at most
D + 2 lattice points), with `--nu-max 8`: the smaller partition nu has |nu| uniform in 1..8,
the corner in which every volume-2 few-point polytope of the box lies (its third partition is
small, such as (2,2,1)); run 5's uniform |nu| in [|lam|/4, 3|lam|/4] never reaches it above
size 30. Commands in `run_all.sh`.

| file | parts | sizes | seed | recorded | tried | primitive with c >= 3 | with c = D + 1 | largest V with c = D + 1 | largest V with c <= D + 2 | records with ratio < 1 (D, V, ratio: count) | negatives |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `f5` | 5 | 31..120 | 20260910 | 3,000 | 44,985,542 | 6,674 | 2,215 | 2 | 3 | 13 (4, 2, 24/25) | 0 |
| `f6` | 6 | 31..80 | 20260911 | 2,000 | 127,896,155 | 7,542 | 1,639 | 2 | 10 | 13 (4, 2, 24/25); 31 (5, 2, 44/45) | 0 |
| `f7` | 7 | 31..60 | 20260912 | 1,000 | 344,002,969 | 5,147 | 748 | 2 | 10 | 23 (4, 2, 24/25); 17 (5, 2, 44/45); 15 (6, 2, 799/812) | 0 |

Dimensions reached: 3..5 (5 parts), 3..7 (6 parts), 3..8 (7 parts); vertex denominators up to
2, 3, 3; sizes up to 120, 79, 60. Wall times 910 s, 2,405 s and 5,811 s on 3 workers at the
lowest priority (the filter rejects almost every draw: 344 million draws for the 1,000
seven-part records).

## Ranges searched with no hit

No sampled polynomial has a negative coefficient. The near-miss structure of the box recurs
unchanged beyond it: the only polynomials with a coefficient below the unimodular-simplex value
are polytopes with D + 1 lattice points and normalized volume 2 in dimensions 4, 5 and 6, with
the same minimal ratios 24/25, 44/45 and 799/812 as in the box's census
(`attack/stretched-lr-polynomial-negative-coefficient/deterministic/certified-special-case-check-4`),
and no few-point polytope of larger volume appears: the largest normalized volume with exactly
D + 1 lattice points is 2 in all three files, and with at most D + 2 lattice points 3, 10 and 10.
The minimal ratio over the run is 24/25.

## Independent check (`check.sh` -> `check.py`, `result.json`)

The checker of run 5 on the files `f5`, `f6`, `f7`: for every one of the 6,000 records the
tableau-polytope encoding recomputed by Normaliz must give the recorded polynomial; lrcalc must
give c at t = 1 and the value at t = 2 when it is at most 1,000,000; when P(D_n) <= 2,000,000
lrcalc counts at t = 0..D_n pin the polynomial by exact interpolation; the summaries' counts
equal the record counts and every record passes the filter (c >= 3, dim >= 3, c <= dim + 2,
primitive by `horn.py`); a third implementation (the lattice-word counter with a Lagrange
interpolation) recounts 30 seeded random records at t = 0..D_n; the largest volume among records
with c = D + 1 is reported.

Trusted base: Normaliz 3.11 (two encodings), lrcalc, Python integers and Fractions, the
sampling code.

## What the run decided

Evidence for the claim on the small-nu corner of class E beyond the box: among 6,000 sampled
primitive hives with at most D + 2 lattice points and |nu| <= 8, of sizes 31..120 at 5 parts,
31..80 at 6 parts and 31..60 at 7 parts, none has a negative coefficient; the coefficients come
closest to zero exactly where they do in the box (volume-2 polytopes with D + 1 lattice points,
ratio 24/25 in dimension 4), and no few-point polytope of normalized volume above 2 appears.
