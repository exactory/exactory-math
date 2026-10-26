# certified-special-case-check-3: every 7-part polynomial recomputed from a second encoding

Date: 2026-09-04. Entry: certify-the-finite-residue-by-computation, action 1 (two independent
implementations) applied to the 7-part sub-residue. Step kind: certified special-case check.

## Inputs

The 1,302,871 polynomial records of `enumeration-run-4`: every canonical primitive triple with
largest length 7 and size <= 30 that has c >= 3 and dim H >= 3, each holding the Ehrhart
polynomial computed by Normaliz from the hive inequalities of `hivepoly.py` (the first
implementation). The 9,201,781 non-primitive 7-part triples with c >= 3 are not records: by the
King-Tollu-Toumazet factorisation theorem their polynomials are products of polynomials of
triples of length <= 6 and size <= 30, all certified by checks 1 and 2.

## The second implementation (`verify7.py`)

A hive of side 7 has 15 interior entries, so deg P <= 15, and pinning P by lattice-word counts
needs the values up to t = 15; for the fat hives of the box these are astronomically many
tableaux (P(10) already exceeds 4 x 10^8 at 6 parts), so the lrcalc pinning of checks 1 and 2
is out of reach here. Instead every record was recomputed from a second polytope encoding: the
tableau polytope of `tableau_polytope.py`, whose variables are the entries of the multiplicity
matrix of a Littlewood-Richardson tableau and whose inequalities are the column-strictness and
lattice-word conditions (no hive entry and no rhombus inequality; the two encoders share no
code), with Normaliz computing its Ehrhart quasi-polynomial. In addition lrcalc (the classical
rule, no code shared with Normaliz or with either encoder) recomputed c^{lam}_{mu nu} for every
record, and c^{2 lam}_{2 mu, 2 nu} for every record (each of the 1,302,871 polynomials has P(2) <= 1,000,000, the bound below which the value at t = 2 was recounted).

Result (`verify7.summary.json`): 1,302,871 records; the tableau encoding agrees with the hive
encoding on all 1,302,871; lrcalc agrees on all 1,302,871 (t = 2 checked on all 1,302,871); 0
mismatches (`verify7.mismatches.jsonl` is empty); the slowest record took 175.4 s;
6,666.9 s in all on 8 workers at reduced priority on a machine shared with other jobs.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary's record count equals the number of polynomial records in `enumeration-run-4`,
   both agreement counts equal it, and the mismatch file is empty.
2. The second encoding is re-run inside the checker on 313 records (300 seeded random, the 10
   with the smallest coefficient ratio, the 3 of largest dimension) and compared with the
   recorded polynomials.
3. A third implementation: for 30 seeded random records with P(3) <= 300,000, the values at
   t = 0..3 are recounted by the lattice-word counter `lrtableaux.py` (no lrcalc, no Normaliz,
   no hive code) and compared with the recorded polynomial (consistency at four points, not a
   pinning).

Trusted base: Normaliz 3.11 (its Ehrhart-series computation is the one component both
encodings share), lrcalc, Python integers and Fractions, the two encoders (which agree on every
record), the King-Tollu-Toumazet factorisation theorem for the non-primitive triples, and the
enumeration of run 4 (completeness recounted independently for every size 7..30 by
`enumeration-run-4/check.sh`, `result.json` status pass).

## What the step decided

The 7-part part of the residue is closed relative to this trusted base: every Ehrhart
polynomial of a primitive 7-part hive in the box is reproduced by a second encoding and matched
by lrcalc at t = 1 (and at t = 2 where feasible), and none has a negative coefficient. By the
skill's standard this is not the two-program certification of checks 1 and 2: the two
encodings share the solver, so a Normaliz defect that affected both encodings identically at
t >= 3 would not show. The 7-part part therefore stays computational evidence, strengthened by
the second encoding. The settled range is the whole box; the first open instances lie at size
31 or at 8 parts.
