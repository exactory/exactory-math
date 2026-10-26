# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000007
Attack: core-entropy
Claim: For every integer m >= 2, every m by m doubly stochastic real matrix M and every column index j, with q_i = M_ij and d_i = per(M(i|j)) the permanent of M with row i and column j removed, prod_i d_i^(q_i) >= gamma(m-1) prod_i (1 - q_i)^(1 - q_i), where gamma(k) = k!/k^k, real powers, and 0^0 = 1 (the complementary-minor entropy lemma; it implies the column entropy floor per(M) >= gamma(m-1) prod_i (1 - q_i)^(1 - q_i) by weighted AM-GM since per(M) = sum_i q_i d_i).
Status: active
Obligation: obligation-000009
Relationship: prerequisite
Logical predecessor: None
Predecessor checkpoint: None
Native parent: node-000001
Account: account-000007

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000004: The complementary-minor entropy obligation of route r7 is proved in Lean.
  Remaining obligations: []
  Next hypothesis: The n = 8..10 and n = 11..15 scalar certificates and the n = 11..15 bridge, already kernel-checked, are accepted next on the frontier; the n = 7 bridge derives its column and core entropy floors from this obligation.
