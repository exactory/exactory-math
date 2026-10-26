# Strategy study: verify-formally-with-lean4 (obligation `core-entropy`)

Queries (2026-09-06): the ported project scratch/maths-pub-port (PORT-NOTES.md, AXIOMS.txt;
modules Capacity, Gurvits, GurvitsUnconditional, HStableDerivative, HStableOrbit, HStableClass,
FaceBounds for `hstable_rowPoly` and `coeff_topIdx_rowPoly`); Mathlib's
`Real.geom_mean_le_arith_mean_weighted`, `Real.rpow` lemmas, `Matrix.submatrix`,
`Fin.succAbove`; the floors node's study for the shared restriction lemma.

Settled before step 2:
1. Canonical statement: `Dittert.CoreEntropy` (Dittert/Obligations.lean), stated for orders
   `k + 1` with `Matrix.submatrix (Fin.succAbove i) (Fin.succAbove j)` as the minor and real powers.
2. Defined in the port and Mathlib: H-stability, capacity, Gurvits's bound, the row-form
   polynomial and its top coefficient, weighted AM-GM, real powers with `0^0 = 1`.
3. Formal proofs in print: none for the lemma; its ingredients are the ported theorems.

Constraints on the plan (lemma chain in `Dittert/CoreEntropy.lean`):
- `minorPoly M j t`: the polynomial `Q_t` as an `MvPolynomial (Fin k) ℝ`; its homogeneity,
  nonnegative coefficients, H-stability (from the floors module's restriction lemma and the
  derivative closure of the port, or directly as a sum of products of linear forms times the
  positive coefficients `q_i t_i`, if the port's closure lemmas cover sums of such products),
  and its top coefficient `∑ i, q_i * t_i * d_i` (permanent expansion along column `j`,
  `Matrix.permanent` multilinearity, or the ported `coeff_topIdx_rowPoly` applied to the bordered
  matrix).
- `cap_minorPoly_ge`: `cap (Q_t) ≥ ∏ t_i^(q_i) ∏ (1 - q_i)^(1 - q_i)` by two weighted AM-GM steps
  on the evaluation at every positive point.
- `minor_pos`: `q_i > 0 → d_i > 0` from Birkhoff's theorem in Mathlib
  (`exists_eq_sum_perm_of_mem_doublyStochastic`) or from a direct permutation argument.
- Assembly with `t_i = 1/d_i` (and `t_i = 1` when `q_i = 0`), `gurvitsBound`, and the real-power
  algebra; the controlled check names `Dittert.core_entropy` with requested type
  `Dittert.CoreEntropy`.
