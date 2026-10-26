# Erdos 124: signed-tail investigation and current handoff

Date: 2026-09-07 UTC.
Objective: objective-000001.
Verified controller state: revision 183, proof status open, execution paused.

## Outcome

The original all-base-set, all-positive-cutoff assertion is not proved.
No pure-power counterexample has been established. The reciprocal equality
case has not been removed from the objective.

The new signed-tail auxiliary implication has a complete, independently
reviewed counterexample. This is a result about a larger abstract class of
integer sequences, not a disproof of Erdos 124.

## What is established

The sequence in node-000009 has two labelled copies at each level and:

- A legal signed representation of 1 in every tail.
- Arbitrarily long intervals of positive subset sums in every tail.
- Gcd one and full subset-sum coverage for every fixed modulus in every tail.
- Divergent squared distance sums for every noninteger multiplier.
- Raw labelled counting exponent greater than one.
- Prefix surplus exceeding every fixed sublinear power asymptotically.

Nevertheless, its positive subset sums up to every real X>=0 number at most
floor(X/9). In particular they are not cofinite and cannot satisfy fixed-loss
central-prefix coverage.

The exact proof is
[001-sparse-signed-blocks.md](attack/erdos-124-signed-tail-seed/moves/001-sparse-signed-blocks.md).
The independent mathematical review is
[signed-seed-result-review.md](admission/signed-seed-result-review.md).
The frozen record is checkpoint-000015 and controller acceptance-000004.
The finished local evidence package is under
attack/erdos-124-signed-tail-seed/units/1/.

Previously accepted root prerequisites remain intact: the reciprocal-core
selection lemma, acceptance-000001, and the all-future prefix-surplus theorem,
acceptance-000002. The earlier abstract counterexample, acceptance-000003,
also remains intact. Only the first two are qualifying positive root
progress. The two abstract counterexamples are not a percentage of a proof.

## Method findings, with their limits

Node-000008 records a conditional interval-amplification argument with an
exact account of used occurrence weights. Its independent checks found no
mathematical error within their stated scope. No support-compatible seed
was constructed for all pure-power inputs.

Its second move applies established finite-rank multiplicative-group
finiteness to show that a fixed number of sufficiently deep pure powers
cannot have a bounded nonzero signed sum. Consequently any tail unit
construction must use growing support. It does not rule out such growing
supports or supply a quantitative exponent threshold.

These remain method findings at hypothesis checkpoint-000013, not accepted
root evidence. See
[02-exchange-size-obstruction.md](attack/erdos-124-carry-seed/moves/02-exchange-size-obstruction.md)
and [carry-seed-move2-check.md](admission/carry-seed-move2-check.md).

The external response in outsourcing/04-universal-central-seed/results/
was read and separately assessed. It does not prove its target, and its
reported private computations were not imported as evidence.
The input was preserved unchanged. Corrections and reading limits are in
[external-04-run-01-triage.md](admission/external-04-run-01-triage.md).

## Remaining mathematical obligation

The selected positive route still lacks a represented central seed whose
fixed endpoint loss is compatible with all later prefixes. Growth estimates,
fixed-modulus coverage, norm divergence and signed-tail unit identities alone
do not supply that seed by the tested general argument.

A later investigation needs a genuinely new pure-power mechanism and an
exactly scoped independent admission. Growing-support carry identities with
a verified support cost, or a non-Gaussian integer-scale positivity estimate,
are possible questions, not established inputs.

The post-signed source follow-up did not identify such a mechanism.
The linear-margin observation was already available for strict reciprocal
mass; its applicability gap had been recorded in the previous strict-band
preflight. A more elaborate abstract rigidity question was saved but not
admitted merely to prolong activity. See
[post-signed-root-assessment.md](admission/post-signed-root-assessment.md)
for the sources, exact limitations and deferred question.

## Controller state and continuation boundary

The third replanning round without new qualifying progress committed at
revision 182 and returned the durable pause reason:

    Three replans without new verified progress

A subsequent controller audit completed at revision 183. All four existing
acceptances remain accepted. The bounded status view itself labels freshness
unchecked; that label is not a new mathematical review. There are no pending
moves or runs. Every admitted node is finished or retreated.

The shared account has used 15 of 24 moves and zero of 24 runs. No allowance
was renewed and nine moves remain. The pause is a replanning stop, not
move-budget exhaustion. An explicit new authorized resume is required to
clear it. Old resume instructions cannot clear a later pause.

Research remains local. Nothing was committed, pushed, submitted or published.
The generated cross-attack index is
[SEARCH_TREE.md](attack/SEARCH_TREE.md). Existing checkpoints and failed
branches are preserved, and the full original objective remains open.

