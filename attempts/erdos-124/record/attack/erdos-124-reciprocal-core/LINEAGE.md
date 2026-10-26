# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000004
Attack: erdos-124-reciprocal-core
Claim: For every nonempty finite set D of distinct integers at least 3, with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D} 1/(d-1)>=1, there exists a subset E of D containing m such that gcd(E)=1 and 1<=sigma(E)<1+1/m.
Status: finished
Deferred from new research selection: no
Obligation: obligation-000004
Relationship: prerequisite
Logical predecessor: node-000003
Predecessor checkpoint: checkpoint-000006
Native parent: node-000003
Account: account-000001

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000008: Move 1 supplies a self-contained analytical proof of minimum-preserving reciprocal-core selection. Strict gcd descent gives a small gcd-one seed of mass below one; a first-crossing argument gives the exact required window. No computational evidence or extra hypothesis is used. This snapshot awaits independent result acceptance.
  Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000005", "obligation-000006"]
  Next hypothesis: After independent acceptance, use the core only through the separate reciprocal-core bridge. The remaining substantial target is eventual labelled pure-power coverage for every base set in the minimum-dependent reciprocal window and every positive cutoff.

## Strategy reassessment

Recorded context: 84ecaee231019aef53009c15d3009e1aaa1d7eb5a650d1271812bba668a23417
Reassessment required by recorded evidence: yes
Policy recorded as enabled: yes
Local plan freshness is checked by search strategy-context and at execution.
