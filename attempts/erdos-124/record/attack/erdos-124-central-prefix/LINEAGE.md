# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000002
Attack: erdos-124-central-prefix
Claim: For every finite set D of distinct integers d >= 3 with gcd(D)=1 and sum_{d in D} 1/(d-1)>=1, every integer k>=1, and every finite set F of labelled occurrences (d,j) with d in D and j>=k, list the occurrences outside F by increasing value and then increasing base label as a_1,a_2,... and set S_m=sum_{i=1}^m a_i; there exist integers L>=0 and m_0>=1 such that, for every m>=m_0, every integer n in [L,S_m-L] is a subset sum of a_1,...,a_m, with each occurrence used at most once.
Status: retreated
Deferred from new research selection: no
Obligation: obligation-000002
Relationship: prerequisite
Logical predecessor: node-000001
Predecessor checkpoint: checkpoint-000001
Native parent: node-000001
Account: account-000001

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000003: C1 remains unproved. Move1 formulates C2 with a jointly chosen seed and loss and derives finite-preamble lifting: proving C1 or C2 for every uniform positive cutoff with F empty is equivalent to the all-finite-deletions version. The positive-integer local-finiteness condition is explicit. No theorem acceptance or renewal credit is claimed.
  Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003"]
  Next hypothesis: Test whether abstract all-future surplus and arithmetic non-obstruction conditions can supply C2's missing seed, while retaining pure-power structure and distinguishing formal label count from distinct subset-sum support.
- checkpoint-000004: C1 remains unproved. Move2 derives an explicit translated-power counterexample to the abstract G seed principle: divergent all-prefix surplus, complete modular coverage in every tail, irrational nonconcentration and excessive raw label count coexist with upper subset-sum density at most q^(-k). The argument is under independent review. Its terms are not admissible pure powers, so it is not a root or C1 counterexample.
  Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003"]
  Next hypothesis: Determine whether the two proposed abstract seed repairs, modular coverage and irrational nonconcentration with raw label growth, survive the recorded counterexample. A successor must retain additional pure-power structure rather than repeat G.
- checkpoint-000005: The conditional append induction stands, but its proposed abstract initialization from modular tail coverage fails, and its repair by irrational nonconcentration plus raw label growth also fails, by the independently reviewed translated-power example. The failed method is narrower than C1; C1, C2 and the root remain hypotheses.
  Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003"]
  Next hypothesis: Keep pure-power self-similarity in a new reduction-and-translation route and isolate the exact integer-lifting or arithmetic recurrence information missing from the failed abstract initialization. Do not restart either failed arithmetic repair.

## Strategy reassessment

Recorded context: 84ecaee231019aef53009c15d3009e1aaa1d7eb5a650d1271812bba668a23417
Reassessment required by recorded evidence: yes
Policy recorded as enabled: yes
Local plan freshness is checked by search strategy-context and at execution.

### Retained strategy failures

- strategy-failure:node-000002:strengthen-and-generalise: The native harness recorded this strategy as failed
