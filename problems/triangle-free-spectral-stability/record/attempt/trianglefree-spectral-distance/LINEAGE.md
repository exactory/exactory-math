# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000001
Attack: trianglefree-spectral-distance
Claim: For every finite simple triangle-free graph $G$, put $m=e(G)$ and let $\lambda(G)$ denote its adjacency spectral radius (with $\lambda(G)=0$ when $G$ has no vertices). Define $D(G)=\min_{A,B\subseteq V(G),\ A\cap B=\varnothing}|E(G)\mathbin{\triangle}E(K_{A,B})|$, where $K_{A,B}$ has all edges between $A$ and $B$ and no other edges on $V(G)$; empty parts are permitted. Then $D(G)\le 3\bigl(m-\lambda(G)^2\bigr)$.
Status: active
Deferred from new research selection: no
Obligation: obligation-000001
Relationship: main
Logical predecessor: None
Predecessor checkpoint: None
Native parent: None
Account: account-000001

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000001: The first analytical move produced an explicit weaker bound and an exact C5 obstruction to the separate cut-plus-bipartite estimate. Neither is claimed as an accepted root result.
  Remaining obligations: ["obligation-000001"]
  Next hypothesis: A joint Perron-weighted cut-and-target calculation can avoid the square-root perturbation term.
- checkpoint-000002: A signed least-eigenvector cut replaces the square-root perturbation loss. It yields proposed universal coefficient fifteen and asymptotic coefficient three, with exact calculations saved but independent acceptance pending. This is not proof of the root.
  Remaining obligations: ["obligation-000001"]
  Next hypothesis: Verify the weaker bounds as a separate branch, then test whether bipartite rounding slack absorbs the remaining signed spectral gap.

## Strategy reassessment

Recorded context: 3cd6addcf81cd317a3dee7023fd6df8fe3bdd6119e2a2e761800db50da5108c5
Reassessment required by recorded evidence: no
Policy recorded as enabled: yes
Local plan freshness is checked by search strategy-context and at execution.

### assessment-000001

Predecessor: None
Context: [snapshot](../.search/blobs/060f0f6863595991017b94e07e5df407c6b2125125ff2280e0d1b3993180e4ce.json)
Assessment: [record](../.search/blobs/2fb40c7caaa1f6eb190d55ed6e331c9d948e2d1bd0b4247929a4c15c851c78f3.json)
Independent review: [record](../.search/blobs/91e5283255283b99eaaffa75310be1a93b1dc0362287a7e10f2f7a863215c4e5.json)
What changed: Move 1 and checkpoint-000001 locate the perturbation loss and show that composing the two separate source bounds is insufficient even on C5. The root is unresolved.
Remaining obligations: ["obligation-000001"]

- node-000001 / ladder-the-parameter: continue. The initial ledger has identified a specific loss, but no joint auxiliary-object calculation has been attempted. The exact C5 obstruction concerns only separate use of the published inequalities.
  Next action: Derive a joint edit-cost functional for neighbourhood targets and test a Perron-weighted bound analytically, retaining any unproved remainder explicitly.
  Evidence: ["checkpoint:checkpoint-000001"]

Continuing order: [{"node_id": "node-000001", "strategy": "ladder-the-parameter"}]
Considered failures: []

- Hypothesis: A Perron-weighted average of joint neighbourhood-target edit costs admits a coefficient-three deficit bound without a separate spectral perturbation estimate.
  Success criterion: Establish a uniformly valid improved bound or an exact new implication with a distinct remaining inequality.
  Failure signal: The weighted inequality remains the full unresolved difficulty or loses an unbounded factor; no repeated producer or numeric search is authorized.

### assessment-000002

Predecessor: assessment-000001
Context: [snapshot](../.search/blobs/2491bdd710a4b213699eaf262f44b3ba3c811b1abdf32b15e1ff32339f2d420d.json)
Assessment: [record](../.search/blobs/bad5bdddf0543e1fd81f71ba9b630a75bfccaf80b1d5dc34677e9997bd16d283.json)
Independent review: [record](../.search/blobs/6fc40a61aefe8e27ab7c5ee1fdbf6e703de30fb89fec74207a64171ad9c0ea65.json)
What changed: The second root move produced a candidate uniform linear and asymptotic bound. An independently admitted standalone node now has an authorized two-move side interval in the same account to check the exact theorem before returning to the root. Two previous observed reviews declined this strategy subject because they treated it as proof acceptance of the root; their objections correctly preserve the unresolved root but do not identify a defect in this proposed verification step. The revised canonical protocol now distinguishes those subjects. This assessment still requests planning approval only, followed by a separately bound proof checkpoint and review.
Remaining obligations: ["obligation-000001"]

- node-000001 / ladder-the-parameter: defer. Temporarily validate the precise candidate rung from its own admission before relying on it in the sharp-constant argument.
  Next action: Resume after the separate proof is accepted or a defect is identified; the universal coefficient-three obligation remains open.
  Evidence: ["checkpoint:checkpoint-000002"]

Continuing order: [{"node_id": "node-000002", "strategy": "ladder-the-parameter"}]
Considered failures: []

- Hypothesis: The complete standalone linear and asymptotic theorem follows from the least-eigenvector sign cut, the published bipartite edit lemma, and exact finite spectral identities.
  Success criterion: A full analytical proof receives independent acceptance on its exact own claim.
  Failure signal: A defective inequality, unhandled graph case or incorrect C5 minimum prevents closing the admitted theorem.

### assessment-000003

Predecessor: assessment-000002
Context: [snapshot](../.search/blobs/3cd6addcf81cd317a3dee7023fd6df8fe3bdd6119e2a2e761800db50da5108c5.json)
Assessment: [record](../.search/blobs/47acb9b659e024212b4d06608a409269451ded36b47188b8db4765b83dd339b0.json)
Independent review: [record](../.search/blobs/2256ef3d1fd482b652a4ec88193e5bfa2d01cfbc97e1994af82e7c19921e81dd.json)
What changed: The complete standalone theorem received observed independent approval and native acceptance-000001. Its local unit is finished. Return to the unchanged root, retaining the exact remaining signed-cut and bipartite-rounding losses. The two-move side interval did not renew the shared account.
Remaining obligations: ["obligation-000001"]

- node-000001 / ladder-the-parameter: continue. The accepted rung now identifies a concrete dependent remainder. It has not yet been attacked jointly.
  Next action: Retain the deleted-edge saving, Rayleigh improvement and bipartite edit slack in one exact inequality; examine whether a valid averaging, asymptotic passage or subclass bootstrap removes their remaining loss. Preserve obstructions and use the native failure and cash-out rules if the ladder stops improving.
  Evidence: ["acceptance:acceptance-000001", "checkpoint:checkpoint-000002", "checkpoint:checkpoint-000003"]

Continuing order: [{"node_id": "node-000001", "strategy": "ladder-the-parameter"}]
Considered failures: []

- Hypothesis: The deletion saving and bipartite rounding slack of a least-eigenvector sign cut can absorb three times the remaining squared spectral gap.
  Success criterion: Prove a uniform cancellation inequality, a genuinely improved coefficient, or a precise restricted theorem with its remaining passage explicitly stated.
  Failure signal: The remainder stays equivalent to the original target for this certificate family, or the attempted relaxation supplies no passage back; preserve the exact obstruction and retire the method under its recorded rules.
