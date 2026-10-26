# Checkpoint 000009: all-future prefix surplus

Date: 2026-09-07. Snapshot: controller revision 103.
Subjective full-objective completion estimate: 6%, low confidence.

## Exact accepted result

For every admissible finite D of distinct integers at least 3, every
positive cutoff k and every finite labelled deletion F, list the remaining
powers in increasing order, breaking value ties by base label. If S_m is
the first m terms' sum, then S_m-a_{m+1} tends to positive infinity.

This is acceptance-000002 for obligation-000007, analytical reviewed.
Checkpoint-000009 retains immutable pending metadata, while its separate
acceptance records that the evidence passed review and audit.
No integer-coverage claim is included.

## Lineage and proof

Producer: node-000005, erdos-124-tail-surplus, move 1.
Logical predecessor: node-000001, checkpoint-000002.
Native parent: none. Original resource account inherited unchanged.

Checkpoint-000002 left the equality-mass all-future estimate open.
The new argument chooses a pair of bases distinguished by divisibility
by one prime. Their positive powers never coincide. For each fixed
nonzero difference, the pair equation is a nondegenerate incidence in
a rank-two multiplicative group. The published ESS theorem gives
finiteness. A finite union over bounded differences yields separation
along every sufficiently late prefix.

The exact geometric-sum identity then bounds the surplus below by this
pair difference divided by max(a,b)-1, minus one fixed deletion constant.
It applies to both strict and equality mass and handles tied labels
without merging them.

Primary engine: Evertse, Schlickewei and Schmidt, DOI
[10.2307/3062133](https://doi.org/10.2307/3062133),
[arXiv:math/0409604v1](https://arxiv.org/abs/math/0409604v1).
The source theorem is imported, not newly proved or formally verified.

## Evidence

- [Complete proof](../attack/erdos-124-tail-surplus/moves/001-sunit-tail-surplus.md)
- [Independent result review](../admission/surplus-result-review.md)
- [Stored checkpoint copy](../attack/checkpoints/surplus-001-checkpoint.json)
- [Evidence manifest](../attack/checkpoints/surplus-001-manifest.json)
- [Public acceptance request](../admission/surplus-accept-public.json)
- [Consolidation](../attack/erdos-124-tail-surplus/units/consolidation.md)
- [Inventory](../attack/erdos-124-tail-surplus/units/INVENTORY.md)

The stored checkpoint digest is
48a5683c8865c6a3346c8d9be03eb25a8e14ecaab1c988487bd3f530d4bbdb71.
The canonical manifest digest is
bf7dd7cc79ac1f3ff8e7ecb6e5970ab2fc5eaa478a5f0eeb5c0c1662b63c37ef.

## Review and local disposition

Independent review found no blocking mathematical or binding defect.
It checked the complete proof, source hypotheses, finite-union argument,
finite deletions, ties and every requested metadata hash.
The first acceptance request used the internal record envelope and was
rejected before mutation. The public request retained the review exactly
and passed. No finding was suppressed or mathematical authority inferred
from the failed call.

The local node closed in one reserved move and finished with zero
publication units. The result is a useful short corollary, not a claim
of independent publication novelty.

## Remaining obligations and next hypothesis

The full original objective, C1, fixed-loss unbounded-prefix seeds, and
their bridges remain open. The reciprocal-core alternative still needs
restricted integer coverage and its bridge.

For any chosen L the extension inequality now eventually holds. The next
strategy must construct a represented central seed with L fixed at a
compatible late prefix, retaining actual power digits and occurrence
uniqueness. Success is an accepted seed argument, or a substantially
sharper exact reduction. Failure is an unproved matching condition,
loss of pure-power structure, occurrence reuse, or recurrence of the
documented abstract counterexample. Such a failure must be preserved.

The estimate rises only from 5% to 6%: one precise extension obligation
has been removed, but the seed condition may carry essentially all of
the remaining difficulty. There is no measured finite family coverage.

## Resources

Ten shared moves used, zero reserved, zero mathematical runs, ceiling
24 moves. No account renewal or refund. No commit, push or submission.

