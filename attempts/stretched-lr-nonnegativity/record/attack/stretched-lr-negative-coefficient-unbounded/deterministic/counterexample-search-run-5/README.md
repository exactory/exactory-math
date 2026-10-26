# counterexample-search-run-5: class E, few-point hives beyond the box

Date: 2026-09-04. Entry: extract-structure-from-a-hypothetical-counterexample, actions 3-4 (the
structured class E of move 1 searched by computation). Step kind: counterexample search run
(seeded random sampling, structured by the number of lattice points).

## Encoder and ranges

`sample_search.py` (lrcalc for c; `horn.py` for primitivity with the essential Horn triples of
n = 5, 6, 7; Normaliz for the dimension and the Ehrhart quasi-polynomial from the hive
inequalities of `hivepoly.py`), with the filter `--cmax-excess 2`: a sampled triple is kept only
when it is primitive, c >= 3, dim H >= 3 and c <= dim H + 2, that is when the hive polytope has
at most D + 2 lattice points, the shape (few points against a large volume) that a negative
linear coefficient by the h*-mechanism needs. |lam| is uniform in the size range and |nu|
uniform in [|lam|/4, 3|lam|/4] (`run_all.sh`).

| file | parts | sizes | seed | recorded | tried | primitive with c >= 3 | with c = D + 1 | largest V with c = D + 1 | largest V with c <= D + 2 | records with ratio < 1 | negatives |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `e5` | 5 | 31..120 | 20260907 | 3,000 | 1,946,286 | 34,389 | 2,255 | 1 | 3 | 0 | 0 |
| `e6` | 6 | 31..80 | 20260908 | 2,000 | 2,234,537 | 24,087 | 1,390 | 1 | 4 | 0 | 0 |
| `e7` | 7 | 31..60 | 20260909 | 1,000 | 3,099,226 | 16,743 | 647 | 1 | 3 | 0 | 0 |

Dimensions reached: 3..6 (5 parts), 3..8 (6 parts), 3..11 (7 parts); vertex denominators up to
2, 3, 3. Wall times 100 s, 220 s and 7,154 s on 3 workers at the lowest priority.

## Ranges searched with no hit

No sampled polynomial has a negative coefficient, and none has a coefficient below the
unimodular-simplex value (minimal ratio exactly 1 in all three files). Every sampled polytope
with exactly D + 1 lattice points is unimodular (normalized volume 1); the volume-2 polytopes
with D + 1 points that the box contains (h* = (1, 0, 1, 0, ...), a small third partition) do not
appear when |nu| is drawn uniformly in [|lam|/4, 3|lam|/4], which is why run 6 samples the
small-nu corner separately. The largest normalized volume among polytopes with at most D + 2
lattice points is 3, 4 and 3 (5, 6, 7 parts), all with ratio >= 1.

## Independent check (`check.sh` -> `check.py`, `result.json`)

For every one of the 6,000 records: the tableau-polytope encoding (`tableau_polytope.py`, no
hive inequality) recomputed by Normaliz must give the same polynomial; lrcalc must give c at
t = 1 and the value at t = 2 when it is at most 1,000,000; when P(D_n) <= 2,000,000 (D_n the
degree bound (n-1)(n-2)/2), lrcalc counts at t = 0..D_n pin the polynomial by exact
interpolation; the summaries' counts equal the record counts and every record passes the
filter (c >= 3, dim >= 3, c <= dim + 2, primitive by `horn.py`). A third implementation (the
lattice-word counter) recounts 30 seeded random records with |lam| <= 40 at t = 0..4
(consistency, not a pinning; the counter's cost grows with the dilation, and a first run of the
checker spent hours on 7-part records at t up to 15). The check also reports the largest volume
among records with c = D + 1.

Trusted base: Normaliz 3.11 (two encodings), lrcalc, Python integers and Fractions, the
sampling code.

## What the run decided

Evidence for the claim on the class E beyond the box: among 6,000 sampled primitive hives with
at most D + 2 lattice points of sizes above 30 at 5, 6 and 7 parts, none has a negative
coefficient or a coefficient below the simplex value, and no few-point polytope of normalized
volume above 4 appears.

Result of the check (2026-09-04): `result.json` status pass; the tableau-polytope encoding agrees on all 6,000 records, lrcalc agrees at t = 1 and 2 on all, lrcalc pins 5,907 of the 5,907 records with P(D_n) <= 2,000,000, the third implementation agrees on 30 records; 4,292 records have c = D + 1, all of normalized volume 1; the largest volume among all records is 4.
