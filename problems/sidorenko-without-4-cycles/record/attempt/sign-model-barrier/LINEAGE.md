# Investigation lineage

Generated from .search/tree.json; do not edit.

Node: node-000002
Attack: sign-model-barrier
Claim: Let $\mathcal{C}_2$ be the class of finite bipartite graphs $H$ with at least one edge and no cycle of length four that have a bipartition $(X,Y)$ in which every vertex of $X$ has degree at most two. For every finite bipartite graph $H$ with at least one edge and no cycle of length four that is not in $\mathcal{C}_2$, that is, each side of every bipartition of $H$ contains a vertex of degree at least three, and for every graphon $W$, $t(H,W)\ge t(K_2,W)^{e(H)}$, where $t$ is the homomorphism density.
Status: active
Deferred from new research selection: no
Obligation: obligation-000003
Relationship: prerequisite
Logical predecessor: None
Predecessor checkpoint: None
Native parent: None
Account: account-000002

Local finish does not imply objective completion.

## Checkpoints

- checkpoint-000002: Move 1 proved the barrier for the construction of the reported counterexample on girth-six patterns (Lemma O and Corollary O' of the proof file). For a bipartite pattern without 4-cycles, every set of active incidences and every choice of signs, the pairwise sign model of the construction equals 1, because a pair of points lying in two faces would be a 4-cycle, so every sign variable occurs in at most one factor and averages it to 1; on every pattern with a 4-cycle it takes the values 0 and 2. Hence, for every finite data of the construction and conditional on the analogue of its rank-layer limit for the pattern, the limit of t(H, V_q) equals (E V_q)^{e(H)}. This excludes the refutation strategy of transferring the construction to the premise outside C_2 at leading order; it neither proves nor refutes that premise and changes no obligation or route status.
  Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000004"]
  Next hypothesis: A girth-six pattern outside C_2 that violates the inequality would need a mechanism outside the admissible class of the reported construction at leading order: lower-order effects at a fixed field size, other kernels, or limits with terms beyond the pairwise sign model; the positive direction outside C_2 needs a method of its own.

## Strategy reassessment

Recorded context: d9a0bde2e1a137712f54151efa498dbc42e751bead2a0daab4272d21ff28ebaa
Reassessment required by recorded evidence: no
Policy recorded as enabled: yes
Local plan freshness is checked by search strategy-context and at execution.

### assessment-000002

Predecessor: assessment-000001
Context: [snapshot](../.search/blobs/17eb058adfd0945ae3fcad973bfec5018cf023687c5b034b822a28ff3450b19f.json)
Assessment: [record](../.search/blobs/8c886ef548b9874094a880c6c8d43928be6a41d95064cd127b2954c954d9fc32.json)
Independent review: [record](../.search/blobs/460656021e830113d83e9b3a07e91a3c7a1636e72842689854093501e9770c36.json)
What changed: Since assessment-000001: replan round 1 selected route-000001 for the root obligation with acceptance-000001 as its progress basis, which invalidated the assessment. The barrier node was revised after the local harness repair that adds the milestone kind verified_strategy_obstruction (the record now runs the local runtime candidate-5): proposal-000003 binds its obstruction milestone to its own target obligation-000003 instead of the positive route, states its hypothesis with exactly the scope of its success criterion (leading order, conditional on the analogue of the rank-layer limit of the reported counterexample for the pattern), and carries transcribed passages of the reported counterexample in its strategy study. It received an observed admission review that approves it with three non-blocking objections (the full text of the reported counterexample must be bound for the result review; the result must state the general pairwise sign model, the conditional assumption and the derivation of the limit; the objective-wide move total binds the node), and it was admitted as node-000002 with strategy prove-the-barrier-first. Its problem, preconditions, plan and ranking are recorded; no move has been made. The problem and novelty studies were revised to record that MathOverflow question 515955 was closed as not suitable for the site.
Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000004"]

- node-000002 / prove-the-barrier-first: continue. The hypothesis recorded by assessment-000001 is now an admitted node with a milestone that states what its result can be: the one published disproof mechanism is the natural first test of the premise outside C_2, its leading-order mechanism depends on pairs of points lying in two faces, and girth-six patterns have none, so the barrier strategy can decide whether the transfer works at all before any construction is tried. The node has no move and no failure.
  Next action: Reserve move 1 under prove-the-barrier-first with entry axiomatise-the-method-and-build-a-near-miss, write the proof of the barrier with the general pairwise sign model, the conditional rank-layer assumption and the derivation of the limit, and record the obstruction checkpoint with the full text of the reported counterexample in its evidence.
  Evidence: ["acceptance:acceptance-000001"]

Continuing order: [{"node_id": "node-000002", "strategy": "prove-the-barrier-first"}]
Considered failures: []

Existing hypotheses retained because: The hypothesis recorded by assessment-000001 for obligation-000003 is the one that node-000002 now tests, with the success criterion and failure signal of its admitted proposal; no new evidence has arrived since that would change it, and the other obligations have no admitted work in this bounded attempt.

### assessment-000003

Predecessor: assessment-000002
Context: [snapshot](../.search/blobs/d9a0bde2e1a137712f54151efa498dbc42e751bead2a0daab4272d21ff28ebaa.json)
Assessment: [record](../.search/blobs/87f1a26998321a30d3239175970040ce8ade8de4100d271b7a43653bd3a4b334.json)
Independent review: [record](../.search/blobs/2f31e97a7cfe995705b03226964ead297d6aac3699b25c613eb262669a7bad95.json)
What changed: Move 1 of node-000002 (strategy prove-the-barrier-first, entry axiomatise-the-method-and-build-a-near-miss) was journalled, and its obstruction checkpoint checkpoint-000002 was recorded under the milestone sign-model-barrier (kind verified_strategy_obstruction on obligation-000003) and accepted as acceptance-000002 after an observed result review that checked the proof against the full text of the reported counterexample: for every bipartite pattern of girth at least six the pairwise sign model of the reported construction is identically 1, so for every finite data of the construction, conditional on the rank-layer limit RL(H) for the pattern, the construction gives exactly the Sidorenko value at leading order; on every pattern with a 4-cycle the sign model takes the values 0 and 2. The node's problem moved to direction unreachable for this class. No obligation changed status; the root obligation, both premises of route-000001 and its bridge remain open.
Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000004"]

- node-000002 / prove-the-barrier-first: retire. The strategy's task is complete: its milestone sign-model-barrier is met by acceptance-000002, which excludes the one published refutation mechanism for the premise outside C_2 at leading order. Its next plan step would hand the record to another strategy; a construction outside the admissible class, or a proof of the premise, would be a new research programme beyond this bounded attempt.
  Next action: No further move; the accepted obstruction is delivered with the problem attempt.
  Evidence: ["acceptance:acceptance-000002", "checkpoint:checkpoint-000002", "journal:move-node-000002-1"]

Continuing order: []
Considered failures: []

- Hypothesis: Problem 1.5 of Conlon, Kim, Lee and Lee holds, so the premise on C_2 (obligation-000002) holds; a first test is a base graph outside the known classes (cliques, KNRS, regular-KNRS and Sidorenko graphs).
  Success criterion: A proof that the 1-subdivision of a new class of base graphs, or of every graph, is Sidorenko, accepted under the reviewed proof policy.
  Failure signal: A base graph whose 1-subdivision violates the inequality, which by acceptance-000001 refutes the premise on C_2 and the root statement.
- Hypothesis: A girth-six pattern outside C_2 that violates the inequality, if one exists, needs a mechanism outside the admissible class of the reported construction at leading order.
  Success criterion: A construction for a girth-six pattern outside C_2, such as the Heawood graph, with a strict deficit that does not come from the pairwise sign model at leading order, with a finite host.
  Failure signal: A proof of the premise outside C_2 for a class containing the natural transfer targets, or a further barrier that excludes the candidate mechanism.
