# Evaluation of units/1/draft.md (second reader, 2026-09-03)

Read against the evidence package: unit.json, deterministic/certified-special-case-check-1
(certificate5.json, README.md, check.py, result.json), the journal excerpt for moves 3 and 5,
and the novelty record.

1. **Statement.** The draft's Theorem 1 is unit.json's statement quantifier by quantifier
   (all nonnegative 5 x 5 real matrices with entry sum 5; the constant 32/3125; the equality
   clause). Match.
2. **Claims and evidence.** The identity (1), the positive semidefiniteness, and both
   verifications point to the step directory and its result.json (status pass, exit 0, output
   head recorded). The block list of the isotypic check matches recover5.log. The numerical
   optimum 40.1156 and the margin 0.343 are in numerical-optimisation-run-2 (result.json pass)
   and recover5.log. No claim without a pointer.
3. **References.** arXiv:2607.29191, arXiv:2607.19439, arXiv:2606.01531 (resolved in
   novelty.md, abstracts fetched); doi:10.1016/0024-3795(87)90032-2 (Crossref record in
   study/fetched/crossref-dittert.json); Minc 1983 and Sinkhorn 1984 as cited by the three
   preprints (bibliographies read); Higham Thm 10.3 is a textbook reference used for the
   floating-point bound of the second implementation only.
4. **Trusted base stated.** Yes: the first implementation exact (Python integers, flint), the
   second exact except one floating-point step; no Lean check, and the Lean statement file
   named.
5. **Ledger.** costs = [bound_quality], from move 3; the draft states the constant reached
   (32/3125) against the numerical optimum, as the ledger rule requires.
6. **Findings.** One slip corrected before this evaluation: an erroneous "61/32" fragment in
   the statement (that constant belongs to n = 4). The reproduction section names the scripts
   and the wall times. The draft passes.
