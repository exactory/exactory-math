# certified-special-case-check-2: every 6-part polynomial pinned by a second implementation

Date: 2026-09-04. Entry: certify-the-finite-residue-by-computation, action 1 (two independent
implementations) applied to the 6-part sub-residue. Step kind: certified special-case check.

## Inputs

The 4,217,762 polynomial records of `enumeration-run-3` (every canonical triple with largest
length 6 and size <= 30 that has c >= 3 and dim H >= 3), each holding the Ehrhart polynomial
computed by Normaliz from the hive inequalities (first implementation).

## The second implementation (`verify6.py`)

For partitions with at most 6 parts the hive polytope lies in R^10 (ten interior hive entries),
so deg P <= 10 unconditionally and P is determined by P(0), ..., P(10). For every record,
lrcalc computed c^{t lam}_{t mu, t nu} for t = 1..10 by the classical Littlewood-Richardson
rule (lrcalc shares no code with Normaliz or with `hivepoly.py`); P(0) = 1; the eleven values
were interpolated exactly by Newton divided differences over Fractions and compared with the
recorded coefficients, largest dimensions first.

Result (`verify6.summary.json`): 4,217,762 records, 4,217,762 agree, 0 mismatches; the largest
value P(10) = 473,221,012 (a dimension-10 hive with c = 76); the slowest record took 405.5 s;
43,814.5 s in all on 11 workers at reduced priority on a machine shared with other jobs.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary's record count equals the number of polynomial records in `enumeration-run-3`
   and reports 0 mismatches.
2. A third implementation: for 30 seeded random records with P(10) <= 200,000, the values at
   t = 0..10 were recounted by the lattice-word counter `lrtableaux.py` (no lrcalc, no
   Normaliz, no hive code), interpolated by a Lagrange formula written in `check.py`, and
   compared with the recorded polynomial.

Trusted base: lrcalc, Normaliz 3.11, Python integers and Fractions, the degree bound
deg P <= 10 (the hive polytope of side 6 has 10 interior entries), and the enumeration of
run 3 (whose completeness `enumeration-run-3/check.sh` recounts independently for every
size 6..30, by a generator, containment test, and canonical form that share no code with
`scan2.py`; `result.json` of run 3 records the pass).

## What the step decided

The residue's 6-part part is closed: every Ehrhart polynomial of a 6-part hive in the box is
certified by two independent implementations that agree, and none has a negative coefficient.
With the theorems used by the reduction (c <= 2; dim H <= 2; the canonical form) this is a
proof by computation that no partitions of largest length 6 and size <= 30 give a negative
coefficient, with lrcalc, Normaliz, and the independent completeness recount of run 3 as the
trusted base.
