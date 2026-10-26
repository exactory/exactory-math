# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000009
Attack: erdos-124-signed-tail-seed
Claim: For every nondecreasing locally finite infinite sequence (a_i) of positive integers with bounded numerical multiplicity, if every tail has gcd one and its finite subset sums meet every residue class modulo every positive integer, liminf_{X->infinity} (log 2)#{i:a_i<=X}/log X>1, sum_i ||alpha a_i||^2=infinity for every irrational real alpha, (S_m-a_{m+1})/a_{m+1}^beta tends to positive infinity for every fixed real beta with 0<beta<1, where S_m=sum_{i=1}^m a_i, and for every integer K>=1 there exist disjoint finite subsets P,Q of {K,K+1,...} with sum_{i in Q}a_i-sum_{i in P}a_i=1, then there exist integers L>=0 and m_0>=1 such that for every m>=m_0, S_m>=2L and every integer in [L,S_m-L] is a subset sum of a_1,...,a_m using each labelled index at most once.
Status: finished
Deferred from new research selection: no
Obligation: obligation-000013
Relationship: prerequisite
Logical predecessor: node-000008
Predecessor checkpoint: checkpoint-000013
Native parent: None
Account: account-000001

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000014: A self-contained analytical infinite counterexample candidate now satisfies the exact full profile and legal signed units in every tail, indeed all-tail signed integer coverage and long positive intervals, while numerical subset sums have upper density at most one ninth. This decides only the new abstract inference; it does not decide any original pure-power instance. Independent result acceptance is pending.
  Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000004", "obligation-000005", "obligation-000006", "obligation-000007", "obligation-000008", "obligation-000009", "obligation-000010", "obligation-000011", "obligation-000012", "obligation-000014", "obligation-000015"]
  Next hypothesis: Once independently accepted, exclude the signed-tail strong-profile inference as a route to C1. The original problem would require additional pure-power structure or a separately justified support-cost mechanism, not another use of the same unproved generic implication.
- checkpoint-000015: Corrects only the overinclusive remaining-obligation metadata in checkpoint-000014, which included already accepted obligations 000004 and 000007. The proof, claim, manifest and journal are unchanged. The complete analytical counterexample candidate satisfies the full signed-tail profile and has numerical subset-sum upper density at most one ninth; it decides only the auxiliary inference and remains pending independent acceptance. This metadata correction grants no new mathematical or budget progress.
  Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000005", "obligation-000006", "obligation-000008", "obligation-000009", "obligation-000010", "obligation-000011", "obligation-000012", "obligation-000014", "obligation-000015"]
  Next hypothesis: Once independently accepted, exclude the signed-tail strong-profile inference as a route to C1. The original problem would require additional pure-power structure or a separately justified support-cost mechanism, not another use of the same unproved generic implication.

## Strategy reassessment

Recorded context: 84ecaee231019aef53009c15d3009e1aaa1d7eb5a650d1271812bba668a23417
Reassessment required by recorded evidence: yes
Policy recorded as enabled: yes
Local plan freshness is checked by search strategy-context and at execution.
