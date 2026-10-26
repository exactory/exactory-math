# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000005
Attack: gurvits-floors
Claim: For every integer n >= 1 and every n by n doubly stochastic real matrix B: per(B) >= n!/n^n; and for all integers a, b >= 1 with a + b <= n - 1, if there are a rows and b columns of B whose a x b block of entries is zero, then per(B) >= gamma(n-a) gamma(n-b) / gamma(n-a-b), where gamma(k) = k!/k^k.
Status: finished
Obligation: obligation-000008
Relationship: prerequisite
Logical predecessor: None
Predecessor checkpoint: None
Native parent: node-000001
Account: account-000005

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000003: The floors obligation shared by routes r7, r8 and r11 is proved in Lean: van der Waerden and the rectangular zero-block floor for doubly stochastic matrices.
  Remaining obligations: []
  Next hypothesis: The complementary-minor entropy obligation is provable from the same row-form and closure infrastructure, and the n = 11..15 bridge closes route r11 once accepted.
