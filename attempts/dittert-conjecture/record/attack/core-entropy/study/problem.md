# Problem study: the complementary-minor entropy lemma (obligation `core-entropy`)

Claim: for every m >= 2, every m by m doubly stochastic real M and every column j, with
q_i = M_ij and d_i = per(M(i|j)), prod_i d_i^(q_i) >= gamma(m-1) prod_i (1 - q_i)^(1 - q_i)
(real powers, 0^0 = 1). Formal reading: `Dittert.CoreEntropy` in the blueprint (m = k + 1).

## Queries (source, string, date)

- The root study's tier-one queries (attack/dittert-lean-5-15/study/problem.md, 2026-09-06) and
  the independent review of the root proposal (controller/review-root-findings.json, 2026-09-06),
  which identified this lemma as the missing premise of the n = 7 route.
- The mathematical source: attack/dittert-completion-tree/study/audit-n7.md section 3
  ("Complementary-minor entropy, including zero entries") and the pinned reconstruction
  attack/dittert-completion-tree/study/external-proof/n6-n7/dittert_n6_n7_reconstruction.tex
  lines 772-835 (Lemma "Complementary-minor entropy") and 837-866 (Proposition "Core entropy").
- Gurvits arXiv:0711.3496 (capacity theorem) and the ported kernel-checked development
  scratch/maths-pub-port (2026-09-06): `GurvitsUnconditional.gurvitsBound`, H-stability closure
  under partial derivatives and products of linear forms with nonnegative coefficients,
  `Capacity.cap` and `Capacity.rowProd`.

## What was learned, as constraints on the plan

1. Proof: for positive t_i, Q_t = sum_i q_i t_i prod_{k != i} L_k (L_k the row forms of M with
   column j deleted, in m - 1 variables) is the coefficient of z in prod_i (L_i + q_i t_i z), hence
   H-stable (derivative in z, then z -> 0: the same restriction-closure lemma the floors node
   proves), homogeneous of degree m - 1 with nonnegative coefficients, with top coefficient
   sum_i q_i t_i d_i. Weighted AM-GM gives cap(Q_t) >= prod_i t_i^(q_i) prod_i (1 - q_i)^(1 - q_i)
   (weights q_i on the terms, then the remaining row entries divided by 1 - q_i; every remaining
   variable has total exponent equal to its column sum, one). Gurvits gives
   gamma(m-1) cap(Q_t) <= sum_i q_i t_i d_i. With t_i = 1/d_i for the i with d_i > 0 (Birkhoff:
   a positive entry lies in a positive permutation, so q_i > 0 implies d_i > 0) the right side is
   sum_i q_i = 1, and the two capacity bounds give the claim. Entries with q_i = 0 contribute the
   factor 1 on both sides (0^0 = 1); the smoothing argument of the source is replaced by the direct
   choice t_i = 1 for those i, which the AM-GM bound tolerates.
2. Shared infrastructure with the floors node: the row-form polynomial, its H-stability, the
   restriction-closure lemma, and the top-coefficient identity; the node imports them from the
   floors module and its acceptance depends on the floors acceptance.
3. The weighted AM-GM for capacities is `Real.inner_le_nnorm_mul_nnorm`-free: it is
   `Real.geom_mean_le_arith_mean_weighted` applied twice, available in Mathlib.

## Stop reason

The queries ran dry: the lemma has one source and one proof route, both recorded above.
