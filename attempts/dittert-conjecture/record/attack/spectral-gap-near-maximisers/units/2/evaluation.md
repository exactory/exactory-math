# Evaluation of unit 2

Read against the evidence package (`unit.json`, `study/work-conditionally-then-discharge.md`,
`study/conditional-K.py`, `journal-excerpt.md`) under the self-check in CASHOUT.md.

## Statement matches `unit.json`

Yes. `unit.json` asserts two things: that `H(n, K)` implies Dittert's conjecture at `n` when
`K < K_max(n)`, with the twelve threshold values; and that `H(n, K)` with a uniform `K` is false,
by the block-diagonal kernel argument. The draft's sections 1 and 3 carry exactly those two, and
the threshold table in section 2 repeats the twelve values in the same order. Sections 4 and 5
add context and no new claim.

## Every claim points to its evidence

| Claim | Evidence | Resolves |
|---|---|---|
| The implication `H(n, K)` to Dittert at `n` | Proof sketch in section 1, resting on Lemma 3(a) of Theorem R and on Knopp-Sinkhorn | yes |
| The twelve `K_max(n)` values and the 2.9e4 at `n = 20` | `study/conditional-K.py` output, move 5 | yes |
| `K` about 0.5 from capacity samples | sibling attack, cited in move 5's output | yes, and the draft calls it a measurement, not a bound |
| The proposition that a uniform `K` fails | Argument in section 3, move 6 | yes |
| The dichotomy of section 4 | move 6 output | yes |

## Every reference resolves

Knopp and Sinkhorn 1982 and Egorychev / Falikman 1981 are in `known` of `problem.json` with
journal and pages. Gurvits and Leake resolves to arXiv:1804.04351, found by the unit-level query
of 2026-09-04. Theorem R is cited to a repository path, correctly, since it is unpublished.

## Findings

1. **Section 1 is a proof sketch, and the draft labels it one.** The steps it compresses are
   Lemma 3(a) of Theorem R and the identity `per(A) = cap(A) per(B)`, both of which are stated
   with their sources. No step is asserted without one.
2. **The claim `K` about 0.5 needs its qualifier and has it.** It is a measurement over samples,
   not a proved bound, and section 2 says "measured against the truth". A reader cannot mistake it
   for a theorem.
3. **The proposition in section 3 weakens the unit rather than the reverse, and the draft leads
   with that.** Section 3 ends by saying what the restriction has to be and where it is treated
   (unit 5). This is the correct ordering: the refutation is part of the claim, not an aside.

## Verdict

Passes. The statement is the unit's, every claim points to its evidence, and every reference
resolves.
