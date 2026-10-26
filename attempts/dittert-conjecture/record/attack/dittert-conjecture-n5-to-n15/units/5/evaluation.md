# Evaluation of units/5/draft.md (second reader, 2026-09-03)

Read against unit.json, units/INVENTORY.md, deterministic/certified-special-case-check-3,
formal-check-1, numerical-optimisation-run-1, numerical-optimisation-run-4 (all with
result.json pass), study/capacity-numerics.py and per-vs-gap-numerics.py outputs recorded in
study/route-a-capacity-notes.md, and the journal.

1. **Statement.** The three parts of unit.json's statement (the exact threshold n >= 16 with
   ratio 0.98712 at n = 15; the loss located in the capacity step; the numerical support for
   G(n, c_n) with the numbers 0.697 against 0.612 and 0.733 against 0.108) appear in the draft
   with the same numbers. Match.
2. **Claims and evidence.** The threshold: check-3 (two exact implementations) and
   formal-check-1 (Lean kernel, standard axioms). The loss location: the ledger of move 8 and
   study/capacity-numerics.py (evidence, labelled as such). The face maximum: run 1 (pass).
   The gap minima: run 4 (pass). The reach of route 2: blocks-output.txt and
   sdp7-attempt.log. Every number in the draft has a source in the record.
3. **References.** The five prior results with their identifiers (Sinkhorn 1984, Hwang 1987,
   2607.29191, 2607.19439, 2606.01531) and Minc 1983 Conjecture 28; all resolved in
   novelty.md / study/problem.md.
4. **Ledger.** costs = [bound_quality, obligations] from moves 11, 12, 13; the draft names the
   owed statements (G(n, c_n), the Lean checks, the exact n = 6 step) in its open questions,
   and states the closed range as the type reached (n <= 6) against the type asked (n <= 15).
5. **Findings.** The conjecture G(n, c_n) is presented as a conjecture with evidence, not as
   a result; the open questions are one sentence each. The draft passes as a problem paper.
