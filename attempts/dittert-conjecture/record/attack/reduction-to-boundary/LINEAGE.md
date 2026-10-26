# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000004
Attack: reduction-to-boundary
Claim: For every integer n >= 2: if every n by n real matrix with nonnegative entries and total entry sum n that attains the maximum of Phi(A) = prod_i r_i(A) + prod_j c_j(A) - per(A) over that set has all entries positive, then Phi(A) <= 2 - n!/n^n for every such matrix A, with equality if and only if every entry of A equals 1/n.
Status: finished
Obligation: obligation-000006
Relationship: prerequisite
Logical predecessor: None
Predecessor checkpoint: None
Native parent: node-000001
Account: account-000004

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000001: The reduction obligation shared by routes r7, r8 and r11 is proved in Lean: for 2 <= n, if every maximizer of Phi is entrywise positive then Statement n holds.
  Remaining obligations: []
  Next hypothesis: The hall obligation is next on the execution frontier; its staged Lean proof is reviewed and its controlled check will accept it.
