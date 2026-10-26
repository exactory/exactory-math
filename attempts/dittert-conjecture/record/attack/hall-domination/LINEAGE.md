# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000003
Attack: hall-domination
Claim: For every integer n >= 1, every n by n real matrix A with nonnegative entries, and every real lambda > 0 such that for all subsets I of the rows and J of the columns with |I| + |J| > n the sum of the entries of A over I x J is at least lambda (|I| + |J| - n), there exists an n by n doubly stochastic real matrix B with lambda B_ij <= A_ij for all i and j.
Status: finished
Obligation: obligation-000007
Relationship: prerequisite
Logical predecessor: None
Predecessor checkpoint: None
Native parent: node-000001
Account: account-000003

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000002: The hall obligation shared by routes r7, r8 and r11 is proved in Lean.
  Remaining obligations: []
  Next hypothesis: The reduction and floors obligations complete the shared prerequisites of route r11.
