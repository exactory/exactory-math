# Evaluation of unit 6

Read against the evidence package (unit.json, study/verify-formally-with-lean4.md,
journal-excerpt.md) under the self-check in CASHOUT.md.

## Statement matches unit.json

Yes. unit.json lists the six missing pieces in order, says the sixth blocks the statement rather
than the proof, and lists the four things Mathlib does have. Sections 2, 3 and 4 of the draft
carry the same six and the same four, in the same order, with the same distinction.

## Every claim points to its evidence

| Claim | Evidence | Resolves |
|---|---|---|
| Toolchain v4.33.1, manifest of 2026-09-03 | the lean-toolchain and lake-manifest files of the sibling attack's Lean project | yes |
| Permanent.lean is 114 lines with fifteen algebraic declarations | declaration list in study/verify-formally-with-lean4.md | yes |
| DoublyStochasticMatrix.lean is 169 lines | same | yes |
| Birkhoff's theorem in three forms | same | yes |
| Each of the six is absent | the same file-index and declaration-list queries of 2026-09-04 | yes |
| The n = 5 check is decidable over the integers and takes about forty minutes | the sibling attack's Lean step, whose run printed that the check returned true | yes |

## Every reference resolves

Egorychev 1981, Falikman 1981, and Knopp and Sinkhorn 1982 are in the known field of problem.json
with journal, volume, and pages. Mathlib resolves to the repository and the recorded toolchain and
manifest date, which is the right identifier for a moving target.

## Findings

1. **The claims are absences, and an absence is the hardest kind of claim to source.** The draft
   handles it by naming what was read and how: file-index queries by name, then the declaration
   list of each module that matched. A reader can repeat both in one command. Section 1 says the
   claims were read rather than recalled, which is the honest framing for a library survey.
2. **The version is stated everywhere it matters.** Mathlib moves, so a survey of it is a
   snapshot. Section 1 fixes the toolchain and the manifest date and section 6 repeats them.
3. **Section 5 states the axiom cost of the one thing that is formalisable.** A draft that
   reported the check as true without naming the compiler-trusting axiom would be presenting a
   native evaluation as a kernel proof. It is stated in the same sentence as the result.

## Verdict

Passes. The statement is the unit's, every claim points to its evidence, and every reference
resolves.
