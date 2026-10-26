# Checkpoint CP-b2f6b2b9b3ae485c

Date: 2026-09-05. Source: `ktt-positivity-length-five` after journal moves 17 and 18, the first two
of pass 3.
Predecessor checkpoint: CP-27216bd31dcaae53.
Archive: `ktt-five-pass3.tar`.
SHA-256: b2f6b2b9b3ae485c768657cd5a1bbe529fac0d388ea8192b4d624c25a0393d30.
Content-addressed immutable snapshot; do not modify. No Git commit and no external publication
were made. This checkpoint preserves research state; it grants no proof coverage and no fresh
budget.

## Exact statements added since the predecessor

1. **The zero-row shortcut is vacuous.** Status: `certified-special-case-check-8`, `result.json`
   pass. Over 2,199 cells and 13,909 rows, 7,973 rows have value zero and not one has a non-empty
   support: at a ray where the linear coefficient vanishes the polytope degenerates to a point and
   every edge length is zero. The other two structural facts hold: no edge has negative length at
   any row, so the length matrix is entrywise nonnegative, and every row of positive value has a
   non-empty support.
2. **The linear program is closed as a route**, with its obstruction written in Farkas form in the
   admission record. Infeasibility needs a nonnegative vector in the row space pairing negatively
   with the weight vector; the weight vector has twenty-one negative entries against roughly 5,121
   nonnegative ones, every row is spread over hundreds of co-occurring positive classes, and move 3
   measured the freedom at rank 442 against 3,406 unknowns. No mechanism for infeasibility is
   identified, so the run is not made.
3. **The weight is already negative in dimension two**, which removes the shortcut hoped for at
   obligation O-B. Under the standard form the cone with rays `(1,0)` and `(-5,1)` has weight
   `-19/104`, and `(20,1)` with `(-20,1)` has `-2279/802`, while thin cones go the other way. So
   this project's positivity at codimensions two and three is about cones spanned by the twenty-seven
   rank-five normals, not about all cones of those dimensions, and O-B needs its own atlas at each
   intrinsic dimension.
4. **A record defect, repaired.** Five of the thirteen steps had no README, because each was
   written in the same shell command as a harness call that the gate rejected. All five are now
   written from the results in each step's own files.

## Evidence paths

`attack/ktt-positivity-length-five/deterministic/certified-special-case-check-8/`;
`attack/ktt-positivity-length-five/study/low-dimensional-weights-can-be-negative.md`; the six
reviews and every amendment in `attack/ktt-positivity-length-five/ADMISSION.md`.

## Unresolved obligations

- O-A open. Its residue is the cells carrying a negative-weight edge, unenumerated; the per-facet
  inequality that would discharge it is unproved with 252,573 passing tests; the weight route's
  residue is five classes that survive every form tried.
- O-B open and now known to need its own atlas at intrinsic dimensions three, four and five.
- Every rung above five untouched. The root open.

## Next hypothesis

The projected transverse cone types of non-full-dimensional five-part hives, at intrinsic
dimensions three and four first, where the weights are two- and three-dimensional and the closed
formulas apply. Six moves remain in the final pass. The last is reserved for the honest close: what
is proved, what remains, and where each obligation stands.
