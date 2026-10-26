# Novelty record for the exact statement

Statement searched: a Lean 4 proof, with only propext, Classical.choice and Quot.sound, that for
every integer 5 <= n <= 15 and every nonnegative n by n real matrix of total sum n,
prod r_i + prod c_j - per(A) <= 2 - n!/n^n with equality only at the uniform matrix.

Queries, all on 2026-09-06 (details and raw responses in study/problem.md and
scratch/study-2026-09-06): arXiv API, Crossref, zbMATH Open, Semantic Scholar (partly rate
limited), GitHub code search, the google-deepmind/formal-conjectures tree, and web search.

Findings:
- The mathematical theorem for 5 <= n <= 15 is claimed by the assembled computer-assisted chain of
  pedromnasc/dittert-conjecture-proof (revision 894066bb) with Lu's n = 6, 7 argument, reconstructed
  and audited locally (attack/dittert-branch-complete-audit/PROOF.md). It is not refereed.
- Formal proofs in print: n = 4 (arXiv:2607.29191, Lean 4, native_decide) and n = 5
  (arthurborgesdev/dittert-conjecture-n5, Lean 4, native_decide). The DCPRevere/maths-pub paper
  says it settles n = 4 and n = 5 "by exact certificates" inside a development that is kernel-checked
  "with two exceptions"; which declarations are the exceptions is recorded in the maths-pub report.
- No kernel-only Lean proof of Dittert's inequality for any n >= 5 was found, and no formal proof
  of any kind for 6 <= n <= 15.

Consequence: this attack claims no mathematical novelty. Its unit form is a formalisation of a
known (unrefereed) computer-assisted theorem, with attribution to the sources above and to the
ported Apache-2.0 Lean sources.
