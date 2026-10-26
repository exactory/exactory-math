# certified-special-case-check-8: the zero-row shortcut is vacuous

Date: 2026-09-05. Entry: certify-the-finite-residue-by-computation, step 1. Run under amendment 2
of the fifth independent review of 2026-09-05, which required it before any solve.

## The shortcut that was proposed

Write the requirement that a local formula be nonnegative and reproduce every recorded linear
coefficient as `A w' = a1`, with `w' >= 0` the weights and `A` the matrix of lattice lengths, one
row per extreme ray of each cell. `A` is entrywise nonnegative because its entries are lengths, and
the right-hand side is nonnegative because the linear coefficients are certified nonnegative. A row
whose right-hand side is zero therefore forces `w'` to vanish on that row's whole support, and
7,109 of the recorded ray values are zero. If some row with a positive right-hand side had its
support inside the union of the zero rows' supports, the system would be infeasible outright, and
that would be a barrier proof with no solver.

## The premise it needs, tested on every cell

| | |
|---|---|
| cells | 2,199 |
| rows, one per extreme ray | 13,909 |
| rows whose value is zero | 7,973 |
| of those, rows with a non-empty support | **0** |
| rows whose value is positive | 5,936 |
| of those, rows with an empty support | 0 |
| edges of negative length at any row | 0 |

**Every zero row is identically zero.** At a ray where the linear coefficient vanishes the hive
polytope degenerates to a point, so every edge has length zero, the row imposes nothing, and the
containment check has nothing to contain. The shortcut is vacuous on this data and the forty-five
minutes it would have cost are not spent.

Two structural facts the linear program rests on are confirmed on the way: no edge has negative
length at any row, so the matrix is entrywise nonnegative, and no row with a positive value has an
empty support.

## What this leaves

Infeasibility, if reachable at all, must come from the equality relations rather than from the sign
pattern. Move 3 of this attack already measured that side: 2,000 polytopes gave 466 distinct
equations of rank 442 against 3,406 unknowns, with the class count growing faster than the equation
count. The record says so before the run rather than after it.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary recomputed from `rows.jsonl`: 0 mismatches.
2. The row counts against the ray counts recorded by the steps that built the cells: 2,199 cells,
   0 mismatches.
3. On 8 sampled cells and 38 rows, the lengths recomputed from the polytope: no zero row has a
   support, and every recorded ray value equals the sum over the edges of the weight times the
   length.

Trusted base: Normaliz 3.11 through PyNormaliz, the Berline-Vergne weights of `enumeration-run-1`
and `enumeration-run-2`, Python integers and Fractions.
