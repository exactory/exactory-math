# Evaluation, unit 2 (author self-check against the evidence package, 2026-09-05)

Verdict: PASS, with the qualification that this pass was made by the author and not by an
independent reader (usage budget; see unit 1's evaluation).

## Statement

`draft.md` states the Proposition with the five conditions C1, C2, C3, C4, C6 exactly as
`unit.json` `statement` (checked clause by clause after the two rewordings of C6 on
2026-09-05: closed cone of a chamber, negative coefficient polynomial at the point, open
sub-cone when interior, counterexamples of every multiple of the size and of infinitely many
sizes). `form` conditional-or-special-case fits: the hypothesis is the negation of the
conjecture, and the ledger carries `obligations` from move 1 (the direction entered as an
assumption), which the statement names as its hypothesis.

## Evidence

`units/2/proof.md`: each condition derived from a cited theorem.

- C1: the factorisation theorem (KTT09, doi:10.1016/j.jcta.2008.06.005; CJM08,
  doi:10.46298/dmtcs.3592, Theorem 1.3, read for the box attack); the descent to a primitive
  counterexample terminates because the number of parts decreases. Sound.
- C2: c <= 2 (KTW04, Ik16, Sh17) and dim H <= 2 by reciprocity (Ma71), the same argument the
  box attack's unit 1 uses (checked there by three reader passes). Sound.
- C3: Fe26 Theorem 1 and the box result; the draft and `proof.md` say which part is a theorem
  and which is evidence, and what C3 reads without the evidence. Sound as stated.
- C4: Fe26 Theorem 3 (full-dimensional 5-part hives positive except the linear coefficient) and
  C2. Sound.
- C6: Rassart's piecewise polynomiality on closed chambers; the homogeneous-part identity
  P(t) = Q_Delta(t lam, t mu, t nu) holds because the ray stays in the closed cone; the open
  sub-cone argument needs the point interior to the chamber, which the statement assumes for
  that clause; the size claim is the ray (every multiple) plus infinitely many sizes (an open
  cone in the chamber's span contains integer points of unboundedly many sizes). Sound; the
  first version's "every size" was withdrawn as unproved.
- C5 of the journal (the h*-heuristic) is excluded from the statement, as the draft says.

## References

CJM08, DW02, Fe26, Ik16, KT99, KTW04, KTT09, Ma71, Ra04, Sh17: identifiers in `problem.json`
known (inherited and the entries copied on 2026-09-05) and the box attack's record. Every key
used has an entry and every entry is used.

## Self-check

- One sentence: yes (a conjunction under one hypothesis).
- A claim, not activity: yes ("A implies B").
- Follows from known literature in a few lines: the ingredients do; the conjunction and the
  chamber consequence are not stated in print (novelty V1-V2); the unit is modest and says so
  in `position.md` (a section of the problem paper, not a standalone paper).
- Novelty record cited: yes.
- On the path: yes.
- Every claim points to a proof: yes (`proof.md`).

## Findings requiring a change

None.
