# Evaluation of unit 3

Read against the evidence package (`unit.json`, `study/vdw-hessian.py`, `journal-excerpt.md`)
under the self-check in CASHOUT.md.

## Statement matches `unit.json`

Yes. `unit.json` asserts the expansion with constant `n/(2(n-1))` for `E` with zero row and column
sums, and the consequence that the quadratic strengthening with that constant reproduces
Knopp-Sinkhorn. The draft's sections 1 and 3 carry exactly those two, with the same constant and
the same extremal.

## Every claim points to its evidence

| Claim | Evidence | Resolves |
|---|---|---|
| The expansion and the constant `n/(2(n-1))` | Proof in section 1, from multilinearity | yes |
| The five constant values at `n = 4` to 8 | `study/vdw-hessian.py`, printed column | yes |
| Relative error below 4e-6 | same script, `rel err` column | yes |
| `\|\|T_n - J_n/n\|\|_F^2 = 1/(n-1)^2` exactly | direct computation in the same script | yes |
| 1.62e-2 against 1.34e-2 at `n = 7` | same script, last two columns | yes |

## Every reference resolves

Egorychev 1981 and Falikman 1981 are in `known` of `problem.json` with journal, volume, and pages.
Knopp and Sinkhorn 1982 likewise. Gurvits and Leake resolves to arXiv:1804.04351.

## Findings

1. **The priority disclaimer is required and present.** The identity is a two-line consequence of
   multilinearity and the unit-level query of 2026-09-04 returned only Gurvits and Leake, which
   does not state it. A draft that claimed the identity as new would be overclaiming; section 6
   says the claim is the consequence. Correct as written.
2. **Section 2's method is exact where it matters.** The permanent is summed over all `n!`
   permutations rather than estimated, so the 4e-6 is the error of the quadratic model at
   `||E||_F = 1e-4`, not a numerical artefact. Checked in the script.
3. **Section 4 states a consequence for the whole attack and points to where it is treated.**
   It is a claim about the record, not about the literature, and it names unit 5. No evidence
   beyond the record is needed for it, and none is implied.

## Verdict

Passes. The statement is the unit's, every claim points to its evidence, and every reference
resolves.
