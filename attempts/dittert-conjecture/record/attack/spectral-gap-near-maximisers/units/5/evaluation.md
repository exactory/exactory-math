# Evaluation of unit 5

Read against the evidence package (`unit.json`, `study/routes-rubric.md`,
`study/binding-constraint.py`, `study/r1-threshold.py`, `journal-excerpt.md`) under the self-check
in CASHOUT.md.

## Statement matches `unit.json`

Yes. `unit.json` asserts two things: that condition (N) is Theorem R's binding constraint by the
factor `1 / sqrt(gamma_n kappa_n)`, with the four values 12.1, 51.7, 576.8 and 6555; and that every
route reduces to one missing statement, a permanent lower bound strong when the capacity is small,
whose only candidate has threshold `n >= 35` crude and `n >= 23` refined. Sections 1 and 3 of the
draft carry those two, with the same numbers.

## Every claim points to its evidence

| Claim | Evidence | Resolves |
|---|---|---|
| Ratio 12.1 / 51.7 / 576.8 / 6555 | `study/binding-constraint.py` | yes |
| `lambda_2 >= 1/(2 n^4)` settles `n >= 15` against `bar c_C` | `study/r1-threshold.py`, move 1 | yes |
| `n >= 35` against `bar c_N` | same script, move 1 | yes |
| Spectral upper bounds 0.562 / 0.0635 / 1.2e-3 / 1.7e-5 | move 7 output | yes |
| Refined threshold about `n = 23` | move 7 output | yes |
| The circularity of the move-7 refinement | move 7 output, which records it | yes |
| The three interfaces and which are closed | move 8 output | yes |

## Every reference resolves

Gurvits and Leake resolves to arXiv:1804.04351. Knopp and Sinkhorn 1982 and Cheon and Wanless 2012
are in `known` of `problem.json` with journal, volume, and pages. Theorem R is cited to a
repository path, correctly, since it is unpublished.

## Findings

1. **The draft reports its own refinement as illusory, in section 2, in the same paragraph as the
   gain.** An earlier ordering would have let a reader take `n >= 23` as a standing result. Move 7
   records the circularity and the draft carries it forward. Correct as written.
2. **Section 4 makes an exhaustiveness claim, and it is checked.** The dichotomy is on
   `cap(A) >= gamma_n / m_n` or its negation, which is exhaustive by construction. The second half
   of the claim, that the permanent side is saturated, points to unit 3 rather than asserting
   itself, and unit 3 carries the evidence.
3. **`r1-threshold.py` once printed its usability flag inverted, and the journal records the
   correction.** The numbers used in section 2 are the corrected ones: R1 clears `bar c_N` only
   from about `n = 35`, so it is empty on 7 to 15. Re-checked against the script's current output.

## Verdict

Passes. The statement is the unit's, every claim points to its evidence, and every reference
resolves.
