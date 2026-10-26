# Implementation attempts

The initial skeleton and final theorem have the same mathematical hypotheses. No mathematical failure or weakened replacement theorem occurred in the first milestone.

- Harness input correction: ranking.json initially used a top-level list, while the installed validator requires an object with order. Corrected the input, and rank passed. No harness validator was changed or suppressed.
- Package setup: explicitly list every module root in Lake. The initial Audit-only root did not make top-level Tests discoverable. The corrected build elaborated the theorem and domain fixtures.
- Fixture proof: unfold Nat.factorial in the gamma3=2/9 example. The expected rational value was unchanged.
- Audit syntax: the final theorem requires an explicit type before its term. The complete scalar exclusion type was written out.
- Expected red gate: the skeleton built, but the final theorem depended on sorryAx. The harness correctly failed; the result is preserved separately.
- Finite pilot syntax: place the doc comment after the two scoped set_option commands. The n11 kernel calculation then passed. No native fallback was used.
- Finite count imports: add Mathlib.Data.Fintype.Prod and Mathlib.Data.Finset.Card. All five rational families, their counts and natural-size coverage compiled without changes to their statements.
- Real proof attempt1: the requested rewrite name add_neg_eq_sub is not present in the pinned library. Replace it with the standard sub_eq_add_neg and mul_neg identities. Attempt2 passed the complete build and axiom audit. No lemma reached the six-attempt or two-restatement limits.

The finite snapshot in formal-check-2 is independent of the original failed skeleton. Final proof evidence uses moves2 and3 once move3 is closed; the move1 obligation is discharged rather than a hypothesis of the resulting theorem.
