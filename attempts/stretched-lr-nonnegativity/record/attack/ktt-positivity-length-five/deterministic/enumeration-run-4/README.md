# enumeration-run-4: the first gate on a candidate scalar product

Date: 2026-09-05. Entry: certify-the-finite-residue-by-computation, step 1. Approved with eleven
amendments by the independent reviews of 2026-09-05 recorded in `../../ADMISSION.md`; this step
discharges amendments 3, 4 and 5 and part of 1.

## Why a scalar product is a free parameter

Every route since move 8 argues around the same twenty-one classes of negative Berline-Vergne
weight. The nonnegative-class lemma says that if no class is negative then the coefficient is
nonnegative on every cell with no computation, so the other move is to change the weight rather
than the argument. Berline and Vergne construct their formula for polytopes in a "rational
euclidean space" (arXiv:math/0507256, abstract), so the scalar product is a parameter and any
rational positive-definite form is admissible. `tools/bvweight.py` already takes the Gram matrix as
an argument.

## The gate

For a lattice polytope the local formula read at codimension equal to the dimension says that the
weights of the tangent cones at the vertices sum to the constant Ehrhart coefficient, which is 1.
The test is exact, needs no Ehrhart computation, and is necessary for a candidate form. It is not
sufficient.

Two polytopes: the unimodular six-simplex, seven tangent cones, and the unit six-cube, sixty-four
signed orthants. Four forms: the standard one; twice the standard one, as the control for scale
invariance; the `A_6` root-lattice form, chosen because its automorphism group is large so that a
usable collapse of edge types survives; and the form with unit diagonal and every off-diagonal
entry one quarter.

## Result (`gate.json`, `result.json` status pass)

| form | simplex, 7 cones | cube, 64 cones | passes |
|---|---|---|---|
| standard | 1 | 1 | yes |
| twice the standard | 1 | 1 | yes |
| `A_6` | 1 | 1 | yes |
| unit diagonal, off-diagonal 1/4 | 1 | cut at 16 of 64 by the allowance | undecided |

A six-dimensional weight costs about 6.3 seconds, so a form costs about seven and a half minutes.

The family is real: `A_6`, a form other than the standard one, passes the necessary test on both
polytopes. And the weight code is now validated in dimension six, where it had been validated only
to dimension five: the standard form reproduces `2^-6` on the signed orthants and the identity
closes to 1 over sixty-four of them.

Exactly one of the four is a usable non-standard form. The standard one is the baseline and twice
the standard could not have failed unless the implementation had a scale bug, so it is an
implementation control rather than a second data point.

## What this does not show

The gate is necessary and not sufficient, and it exercises full-dimensional tangent cones at
codimension six. The twenty-one negative classes are codimension-five transverse cones, so nothing
here bears on them, and nothing here validates the codimension-five module that
`certified-special-case-check-7` introduces.

## Independent check (`check.sh` -> `check.py`, `result.json`)

1. The recorded sums are exactly 1 where the record says the identity holds, and the vertex counts
   match: 4 forms recorded, 3 passing both.
2. A test the run did not do: the same identity on a second lattice simplex, not unimodular. Both
   the standard form and `A_6` give 1. 0 mismatches.
3. Scale invariance, which the classification argument in the admission record rests on, on random
   three-dimensional cones. 0 mismatches.
4. The closed value `2^-6` on three signed orthants under the standard form. 0 mismatches.

Trusted base: `tools/bvweight.py`, Python integers and Fractions, and Berline and Vergne's
construction as cited from the paper's abstract rather than from a numbered statement.
