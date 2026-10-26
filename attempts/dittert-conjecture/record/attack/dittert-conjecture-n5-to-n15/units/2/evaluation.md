# Evaluation of units/2/draft.md (second reader, 2026-09-03)

Read against unit.json, deterministic/certified-special-case-check-2 (certificate6.json,
README.md, check_verified.py, result.json), numerical-optimisation-run-3 (sdp6.log,
recover6.log, result.json), the journal excerpt for moves 4 and 6.

1. **Statement.** Theorem 2 matches unit.json, including the qualification that the main
   matrix's positive definiteness is verified in floating point with a rigorous bound; the
   draft places that qualification in the statement section, not in a footnote. Match.
2. **Claims and evidence.** The identity, the exact checks, and the verified Cholesky numbers
   (alpha 7.51e-5 against 3.06e-5; multipliers 1.05e-3 and 1.09e-3 against 4.3e-7) are those of
   result.json and recover6.log. The numerical optimum 174.89 and the block sizes are in
   sdp6.log. The abandoned Bareiss run is reported as such.
3. **References.** The same as unit 1; Higham Thm 10.3 is now load-bearing for the main
   matrix and is named as the base theory the theorem is stated relative to (ledger: axioms).
4. **Ledger.** costs = [axioms] from move 6; the draft names the base (IEEE-754 arithmetic,
   LAPACK's Cholesky and its error analysis) as the ledger rule requires.
5. **Findings.** The draft is explicit that the exact isotypic check was not run at n = 6 and
   why (element enumeration of G_6). It passes, as a special-case result with a stated
   non-exact step.
