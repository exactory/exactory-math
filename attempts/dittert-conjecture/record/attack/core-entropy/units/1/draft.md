# Formalisation unit: core-entropy

## Statement

For every integer m >= 2, every m by m doubly stochastic real matrix M and every column index j, with q_i = M_ij and d_i = per(M(i|j)) the permanent of M with row i and column j removed, prod_i d_i^(q_i) >= gamma(m-1) prod_i (1 - q_i)^(1 - q_i), where gamma(k) = k!/k^k, real powers, and 0^0 = 1 (the complementary-minor entropy lemma; it implies the column entropy floor per(M) >= gamma(m-1) prod_i (1 - q_i)^(1 - q_i) by weighted AM-GM since per(M) = sum_i q_i d_i). Lean theorem Dittert.core_entropy with requested type Dittert.CoreEntropy, checked with propext, Classical.choice and Quot.sound only.

## Claim, quantifier by quantifier

The controller obligation reads: For every integer m >= 2, every m by m doubly stochastic real matrix M and every column index j, with q_i = M_ij and d_i = per(M(i|j)) the permanent of M with row i and column j removed, prod_i d_i^(q_i) >= gamma(m-1) prod_i (1 - q_i)^(1 - q_i), where gamma(k) = k!/k^k, real powers, and 0^0 = 1 (the complementary-minor entropy lemma; it implies the column entropy floor per(M) >= gamma(m-1) prod_i (1 - q_i)^(1 - q_i) by weighted AM-GM since per(M) = sum_i q_i d_i).

Quantifiers: For every integer m >= 2, every m by m doubly stochastic real matrix M and every column index j.

The Lean declaration `Dittert.core_entropy` has the requested type `Dittert.CoreEntropy`, whose definitions are the blueprint's (Dittert/Basic.lean, Dittert/Obligations.lean, Dittert/Scalar/Defs*.lean in the frozen step directory).

## Evidence

- Controlled formal check: `deterministic/formal-check-1/result.json`, status `pass`, axioms ["propext", "Classical.choice", "Quot.sound"].
- Journal moves: [1].

## Moves

- Move 1 (verify-formally-with-lean4 / formalise-while-fresh): Formalized the complementary-minor entropy lemma in Dittert/Entropy.lean with the helper modules Dittert/Entropy/Algebra.lean, AMGM.lean and Minor.lean on top of the floors modules and the ported GurvitsPort development: the weighted row form of the matrix extended by one column of entries q_i t_i, whose reduction (derivative in the new variable at zero) is the sum over rows of q_i t_i times the row form of the minor M(i|j), with top coefficient the sum of q_i t_i per M(i|j) (the Laplace expansion along a column appears as a by-product); H-stability of that reduction from the floors module's closure lemmas; two weighted AM-GM steps (weights q_i over the rows, then the row entries divided by 1 - q_i) bounding the capacity below by prod t_i^(q_i) prod (1 - q_i)^(1 - q_i); positivity of the minor's permanent whenever q_i > 0 by Birkhoff's decomposition; the port's Gurvits bound for the reduced polynomial; and the choice t_i = 1/d_i when q_i > 0, t_i = 1 otherwise, which rearranges to the claim with the real-power convention 0^0 = 1; installed the frozen project and ran the controlled formal check of Dittert.core_entropy. Output: Dittert.core_entropy : Dittert.CoreEntropy is kernel-checked with propext, Classical.choice and Quot.sound only (581 new lines over the floors modules and the GurvitsPort library, no sorry).

## Provenance

See study/problem.md, study/verify-formally-with-lean4.md and novelty.md of this node; ported sources are attributed in their file headers.
