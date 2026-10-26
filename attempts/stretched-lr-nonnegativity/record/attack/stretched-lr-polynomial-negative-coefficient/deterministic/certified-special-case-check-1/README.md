# certified-special-case-check-1: every 5-part polynomial pinned by a second implementation

Date: 2026-09-04. Entry: certify-the-finite-residue-by-computation, action 1 (two independent
implementations) applied to the 5-part sub-residue. Step kind: certified special-case check.

## Inputs

The 1,334,669 polynomial records of `enumeration-run-2` (every canonical triple with largest
length 5 and size <= 30 that has c >= 3 and dim H >= 3), each holding the Ehrhart polynomial
computed by Normaliz from the hive inequalities (first implementation).

## The second implementation (`verify5.py`)

For partitions with at most 5 parts the hive polytope lies in R^6 (six interior hive
entries), so deg P <= 6 unconditionally and P is determined by P(0), ..., P(6). For every
record, lrcalc computed c^{t lam}_{t mu, t nu} for t = 1..6 by the classical
Littlewood-Richardson rule (lrcalc shares no code with Normaliz or with `hivepoly.py`);
P(0) = 1 (the Ehrhart quasi-polynomial of a rational polytope takes the value 1 at t = 0, and it is a polynomial by Derksen-Weyman); the seven values were interpolated exactly by Newton divided
differences over Fractions and compared with the recorded coefficients.

Result (`verify5.summary.json`): 1,334,669 records, 1,334,669 agree, 0 mismatches; the
largest value P(6) = 125,062; 101.5 s on 11 workers.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The summary's record count equals the number of polynomial records in
   `enumeration-run-2` and reports 0 mismatches.
2. A third implementation: for 300 seeded random records and the 10 with the smallest
   linear coefficient, the values at t = 0..6 were recounted by the lattice-word counter
   `lrtableaux.py` (no lrcalc, no Normaliz, no hive code), interpolated by a Lagrange
   formula written in `check.py` (not the Newton code of `verify5.py`), and compared with
   the recorded polynomial.

Trusted base: lrcalc, Normaliz 3.11, Python integers and Fractions, the degree bound
deg P <= 6 (the hive polytope of side 5 has 6 interior entries), and the enumeration of
run 2 (whose completeness `enumeration-run-2/check.sh` recounts independently for every
size 5..30).

## What the step decided

The residue's 5-part part is closed: every Ehrhart polynomial of a 5-part hive in the box
is certified by two independent implementations that agree, and none has a negative
coefficient. Together with the theorems used by the reduction (c <= 2; dim H <= 2; the
canonical form) this is a proof by computation that no partitions of length <= 5 and size
<= 30 give a negative coefficient, with lrcalc and Normaliz as the trusted base.
