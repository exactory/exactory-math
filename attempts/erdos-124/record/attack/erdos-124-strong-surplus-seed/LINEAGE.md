# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000006
Attack: erdos-124-strong-surplus-seed
Claim: For every nondecreasing locally finite infinite sequence (a_i) of positive integers with bounded numerical multiplicity, if every tail has gcd one and its finite subset sums meet every residue class modulo every positive integer, liminf_{X->infinity} (log 2)#{i:a_i<=X}/log X>1, sum_i ||alpha a_i||^2=infinity for every irrational real alpha (where ||x|| is distance to the nearest integer), and (S_m-a_{m+1})/a_{m+1}^beta tends to positive infinity for every real beta with 0<beta<1, where S_m=sum_{i=1}^m a_i, then there exist integers L>=0 and m_0>=1 such that for every m>=m_0, S_m>=2L and every integer in [L,S_m-L] is a subset sum of a_1,...,a_m using each labelled index at most once.
Status: finished
Deferred from new research selection: no
Obligation: obligation-000010
Relationship: prerequisite
Logical predecessor: node-000005
Predecessor checkpoint: checkpoint-000009
Native parent: None
Account: account-000001

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000010: The paired floor-perturbation construction is a complete computer-free counterexample candidate to the exact stronger abstract inference. It satisfies the all-prefix surplus limit against every fixed sublinear power, all arithmetic and norm hypotheses, and strict labelled counting, while numerical subset-sum support has upper density at most one ninth. The older logarithmic example did not meet this hypothesis. No pure-power counterexample or root closure is claimed.
  Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000005", "obligation-000006", "obligation-000008", "obligation-000009", "obligation-000011", "obligation-000012"]
  Next hypothesis: After independent acceptance, discard the generic strong-surplus route as a source of C1. Further progress must use additional structure of actual pure-power streams, such as exact multiplicative recurrences or a disjoint represented-interval mechanism; neither a larger surplus rate nor modular and norm non-obstruction alone supplies the seed.

## Strategy reassessment

Recorded context: 84ecaee231019aef53009c15d3009e1aaa1d7eb5a650d1271812bba668a23417
Reassessment required by recorded evidence: yes
Policy recorded as enabled: yes
Local plan freshness is checked by search strategy-context and at execution.
