# Unit 1: the negative side of the King-Tollu-Toumazet conjecture beyond the box, sampled

## Statement

See `unit.json`: in the sampled classes beyond the box no stretched Littlewood-Richardson
polynomial or transportation-polytope Ehrhart polynomial has a negative coefficient; the
polynomials with a coefficient below the unimodular-simplex value are exactly the few-point
polytopes of normalized volume 2 with h* = (1, 0, 1, 0, ...) in dimensions 4 to 7, plus one
polytope of normalized volume 3 with h* = (1, 0, 2, 0, 0, 0, 0) at 8 parts.

## Evidence: the six search runs (every `result.json` status pass)

| run | class | what was sampled | records | negatives | checker |
|---|---|---|---|---|---|
| `deterministic/counterexample-search-run-1` | S1 | primitive 5-part hives, sizes 31..200, dimension >= 3 (seed 20260904) and full-dimensional (seed 20260905) | 300,000 + 100,000 | 0 | every polynomial recomputed from the tableau-polytope encoding by Normaliz; lrcalc at t = 1 and 2; lrcalc pins 336,404 of the 336,404 records with P(6) <= 2,000,000; third implementation on 30 records |
| `counterexample-search-run-2` | S4 | transportation polytopes 3 x 4 (total <= 16), 3 x 5 (<= 14), 3 x 6 (<= 12), 4 x 4 (<= 14), 4 x 5 (<= 11), 5 x 5 (<= 8) | 5,170 | 0 | 78 pairs recounted from the definition of a contingency table at t = 1, 2 (and 3) |
| `counterexample-search-run-3` | S2 | primitive 6-part hives, dimension 8..10, sizes 31..80 (seed 20260906) | 40,000 | 0 | lrcalc at t = 1 on every record; the second encoding and lrcalc at t = 2 on 1,500 sampled records; third implementation on 30 |
| `counterexample-search-run-4` | S3 | primitive 8-part hives, dimension 3..12, sizes 20..40 (seed 20260913; stopped after 2,000, 1,799 readable) | 1,799 | 0 | as run 3 |
| `counterexample-search-run-5` | E | primitive hives with at most D + 2 lattice points, 5, 6, 7 parts, sizes 31..120, 31..80, 31..60 (seeds 20260907-9) | 3,000 + 2,000 + 1,000 | 0 | every polynomial recomputed from the second encoding; lrcalc pins 5,907 of the 5,907 records with P(D_n) <= 2,000,000; third implementation on 30 |
| `counterexample-search-run-6` | E, small nu | the same with the third partition of size at most 8 (seeds 20260910-2) | 3,000 + 2,000 + 1,000 | 0 | as run 5 (5,968 of 5,968 pinned) |

Trusted base: Normaliz 3.11 (two polytope encodings), lrcalc, Python integers and Fractions,
the sampling code (`sample_search.py`, `transport.py`) and the checkers recorded in the step
directories; the polynomials of runs 3 and 4 outside the checkers' samples rest on Normaliz and
lrcalc at t = 1.

## What the samples show

- Minimal linear coefficients per stratum equal the box's: 157/60 in the full-dimensional
  5-part stratum (run 1, 100,000 records, the same value as the 13,217 full-dimensional hives
  of the box); 761/280 = H_8, 3827/1260 and 2843/840 in dimensions 8, 9, 10 at 6 parts (run 3),
  the same three values as the 6-part box.
- The polynomials with a coefficient below the unimodular-simplex value: none in runs 1, 3, 5
  (minimal ratio 1 in each; the few-point polytopes with D + 1 lattice points sampled with |nu|
  uniform in [|lam|/4, 3|lam|/4] are all unimodular); in run 6 (|nu| <= 8) exactly 112 of 6,000,
  all with D + 1 lattice points and normalized volume 2 (13 of dimension 4 at 5 parts, ratio
  24/25; 13 of dimension 4 and 31 of dimension 5 at 6 parts, ratios 24/25 and 44/45; 23, 17 and
  15 of dimensions 4, 5, 6 at 7 parts, ratios 24/25, 44/45, 799/812); in run 4 (8 parts) six:
  three of dimension 6 with volume 2 (799/812), two of dimension 7 with volume 2 (927/938), and
  one of dimension 6 with normalized volume 3, lam = (4,4,3,3,2,2,1,1), mu = (3,3,2,2,1,1),
  nu = (3,2,2,1), c = 7, P(t) = (240 + 572 t + 524 t^2 + 255 t^3 + 75 t^4 + 13 t^5 + t^6)/240,
  h* = (1, 0, 2, 0, 0, 0, 0), minimal ratio 393/406.
- The largest normalized volume among polytopes with exactly D + 1 lattice points is 2 in runs
  1, 5, 6 (5, 6, 7 parts) and 3 in run 4 (8 parts); among those with at most D + 2 lattice points it is 3 (5 parts), 4 and 10 (6 parts, runs 5 and 6), 3 and 10 (7 parts) and 6 (8 parts).
- Transportation polytopes: every member of the six families is Ehrhart positive; the minimal
  ratio is 60/49 near the Birkhoff-type members; the tool reproduces the 3 x 8 example of
  Ferudun 2026 (1050 lattice points, linear coefficient 2157/280), the Ehrhart polynomial of
  B_3 and the volume of B_5.

## Reproduction

Each step directory holds the sampling code, `input.json` (or `run_all.sh`), the gzipped
records, the summaries and logs, `README.md`, `check.sh` and `result.json`; Normaliz runs
single-threaded (`OMP_NUM_THREADS=1`). Wall times: run 1, 817 s and 1,438 s on 6 workers;
run 3, 14,830 s on 6 workers; run 4, 20,129 s on 3 workers (stopped); runs 5 and 6, 7,474 s
and 9,126 s on 3 workers; the checkers from minutes (runs 2, 3, 4) to hours (runs 1, 5, 6).
