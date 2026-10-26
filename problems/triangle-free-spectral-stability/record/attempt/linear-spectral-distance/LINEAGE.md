# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000002
Attack: linear-spectral-distance
Claim: For every finite simple triangle-free graph G, let m=e(G), let lambda be its adjacency spectral radius (zero for an empty vertex set), let xi=m-lambda^2, and let D(G) be the minimum of |E(G) symmetric-difference E(K_{A,B})| over disjoint vertex subsets A,B, allowing empty parts and leaving all other vertices isolated. Then D(G)<=15xi. If lambda>0, then D(G)<=3xi+18sqrt(6)xi^(3/2)/lambda. Consequently, for every sequence of such graphs with xi>0 and xi/m tending to zero, limsup D(G)/xi<=3. Moreover D(C5)=3 and e(C5)-lambda(C5)^2=1, so no universal coefficient smaller than 3 can bound D(G)/xi.
Status: finished
Deferred from new research selection: no
Obligation: None
Relationship: standalone
Logical predecessor: node-000001
Predecessor checkpoint: checkpoint-000002
Native parent: None
Account: account-000001

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000003: The complete admitted standalone theorem has an analytical proof with boundary cases, exact trace inequalities and exact C5 minimum, and a checked local draft/unit. This checkpoint requests independent acceptance and makes no priority claim.
  Remaining obligations: ["obligation-000001"]
  Next hypothesis: After independent acceptance, return to the original coefficient-three question and examine the combined sign-cut and bipartite-rounding slack.

## Strategy reassessment

Recorded context: 3cd6addcf81cd317a3dee7023fd6df8fe3bdd6119e2a2e761800db50da5108c5
Reassessment required by recorded evidence: no
Policy recorded as enabled: yes
Local plan freshness is checked by search strategy-context and at execution.

### assessment-000002

Predecessor: assessment-000001
Context: [snapshot](../.search/blobs/2491bdd710a4b213699eaf262f44b3ba3c811b1abdf32b15e1ff32339f2d420d.json)
Assessment: [record](../.search/blobs/bad5bdddf0543e1fd81f71ba9b630a75bfccaf80b1d5dc34677e9997bd16d283.json)
Independent review: [record](../.search/blobs/6fc40a61aefe8e27ab7c5ee1fdbf6e703de30fb89fec74207a64171ad9c0ea65.json)
What changed: The second root move produced a candidate uniform linear and asymptotic bound. An independently admitted standalone node now has an authorized two-move side interval in the same account to check the exact theorem before returning to the root. Two previous observed reviews declined this strategy subject because they treated it as proof acceptance of the root; their objections correctly preserve the unresolved root but do not identify a defect in this proposed verification step. The revised canonical protocol now distinguishes those subjects. This assessment still requests planning approval only, followed by a separately bound proof checkpoint and review.
Remaining obligations: ["obligation-000001"]

- node-000002 / ladder-the-parameter: continue. Both admission reviewers found the exact sign-cut, trace and five-cycle proof chain suitable for independent validation. No root credit or extra allowance is requested.
  Next action: Write and check the full analytical proof with all edge cases, close this local theorem if justified, and submit its immutable proof checkpoint to independent result review.
  Evidence: ["checkpoint:checkpoint-000002"]

Continuing order: [{"node_id": "node-000002", "strategy": "ladder-the-parameter"}]
Considered failures: []

- Hypothesis: The complete standalone linear and asymptotic theorem follows from the least-eigenvector sign cut, the published bipartite edit lemma, and exact finite spectral identities.
  Success criterion: A full analytical proof receives independent acceptance on its exact own claim.
  Failure signal: A defective inequality, unhandled graph case or incorrect C5 minimum prevents closing the admitted theorem.
