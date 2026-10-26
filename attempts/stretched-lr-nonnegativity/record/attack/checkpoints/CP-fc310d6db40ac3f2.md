# Checkpoint CP-fc310d6db40ac3f2

Date: 2026-09-05. Source: `ktt-positivity-length-five` after journal move 15.
Predecessor checkpoint: CP-8dff598654f5dc84.
Archive: `ktt-five-form-gate.tar`.
SHA-256: fc310d6db40ac3f27cac30c4d73e76ffbcef1eb6c81023a3d8db7685dc0fb001.
Content-addressed immutable snapshot; do not modify. No Git commit and no external publication
were made. This checkpoint preserves research state; it grants no proof coverage and no fresh
budget.

## Exact statements added since the predecessor

1. The scalar product is a free parameter of the construction. Berline and Vergne build the local
   Euler-Maclaurin formula for polytopes in a rational euclidean space, so any rational
   positive-definite form is admissible, and `tools/bvweight.py` already takes the Gram matrix as
   an argument. Cited from the paper's abstract, arXiv:math/0507256, not from a numbered statement
   in it.
2. Measured, `enumeration-run-4`, `result.json` pass, with four independent checks. The vertex-sum
   identity, that the weights of the tangent cones at the vertices of a lattice polytope sum to
   one, holds for the standard form, for twice the standard form and for the `A_6` root-lattice
   form, on both the unimodular six-simplex with seven cones and the unit six-cube with sixty-four
   signed orthants. The fourth form tried was cut at sixteen of sixty-four by the allowance and is
   undecided.
3. So a form other than the standard one passes the test that is necessary for the whole
   programme, which is what had to be established before spending anything further on it.
4. Two by-products. The weight code is validated in dimension six, where it had been validated
   only to dimension five, since the standard form reproduces `2^-6` on the signed orthants and
   the identity closes to one over sixty-four of them. And scale invariance, which the
   classification argument in the admission record rests on, is confirmed on random
   three-dimensional cones rather than assumed.

## Assumptions and trusted base

Berline and Vergne's construction as cited from the abstract; `tools/bvweight.py`; Python integers
and rationals. The gate is necessary and not sufficient: passing it does not establish that a form
gives a valid local formula for every polytope.

## Evidence paths

`attack/ktt-positivity-length-five/deterministic/enumeration-run-4/`. The proposal, its two
reviews, the eleven amendments and the allowance accounting are in
`attack/ktt-positivity-length-five/ADMISSION.md`.

## Unresolved obligations

- Nothing here touches the twenty-one negative classes. Evaluating them under a non-standard form
  needs the transverse cone built in that form's own orthogonal complement, which
  `tools/transverse.py` does only for the standard form. That is the next phase and it needs its
  own admission and allowance.
- The reviewer's own preference is on record and not yet acted on: after this, the linear program
  over the whole affine space of local formulas, the project's superseded task 9, is what decides
  what this only probes.
- Unchanged: the per-facet inequality is unproved, move 8's residue is unenumerated, O-B awaits its
  own review, every rung above five is untouched.

## Next hypothesis

Extend `transverse.py` to build the transverse cone in the orthogonal complement of a given form,
then evaluate the twenty-one negative representative cones and a positive control drawn from the
smallest positive weights held, under `A_6` first. A form that lifts all twenty-one without pushing
the control negative would be the first evidence that the negativity is an artefact of the standard
scalar product. Successor: move 16, budget 7 of 8 in pass 2.
