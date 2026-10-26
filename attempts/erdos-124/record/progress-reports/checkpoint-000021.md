# Checkpoint 000021: scalar normalization fails to compress the residual

Recorded: September 8, 2026.
Controller checkpoint revision:282. Retreat revision:283.
Source: node-000015, erdos-124-half-tail-structure, journal move2.
Checkpoint digest: `d9ecdf5831f0b8d1cc3e8d306654f785e59e234a93374359eef9ee29655200c0`.
Manifest digest: `56c705cf03cdfc7f83bee7089196a7ec2cf299f84f6651cd9c03693ff6d45c31`.

## Judgment

The original all-base, all-positive-cutoff problem remains open. The rough
subjective progress estimate remains15%, with low confidence. This is not a
fraction of proved inputs or a probability. The present method restriction
does not justify increasing it.

The checkpoint is a hypothesis snapshot with pending verification, not an
accepted proof, a general impossibility theorem or renewal credit.

## Exact claim and assumptions

The preserved attack asks whether every nonempty finite gcd-one set E of
distinct integer bases at least3 with sum over E of1/(d-1)>=1/2 admits
disjoint finite remaining labelled sets P,Q with sum(Q)-sum(P)=1, after
every positive cutoff and every finite deletion. Labels have capacity one;
numerically equal occurrences from distinct labels remain separately available.

That complete assertion has not been proved or refuted. It does not replace
the original positive-sum objective at reciprocal mass at least1.

## What changed

For d>=4 let X_d consist of finite signed base-d sums with digits in
{-1,0,1}. The new hand-checked lemma states

```text
M X_d subset X_d  iff  M = 0 or M = epsilon d^t,
where epsilon is -1 or 1 and t is a nonnegative integer.
```

The lowest signed digit is fixed by the residue modulo d. Strip the first
nonzero digit of M. If a second nonzero digit occurs at position r, multiplying
by the matching two-digit signed value forces a coefficient congruent to
plus or minus2 at position r, which is not an allowed digit for d>=4.
This proves the classification, including negative scalars and d=4.

A common expanding scalar preserving every individual X_d would therefore
be a positive power of each base in E, up to sign. A prime divisor would
divide every base, contradicting gcd(E)=1.

This obstruction holds even for known positive configurations. It supplies
no additional necessary condition distinguishing a missing tail unit, no
finite reduction, no uniform control of delta(K), and no counterexample.
It does not exclude target-dependent supports, mixed-base constructions
or nonlinear operations. The common-radix positive construction at
checkpoint20 is unaffected because it combines capacities across base labels.

## Verification and lineage

The proof is analytical and author-checked. No mathematical process or independent
result review ran for this move. The native journal and checkpoint service
validated the reserved origin and supplied artifact bytes. That integrity
check does not independently verify the mathematics.

Checkpoint20 remains the predecessor containing the positive common-radix
construction and stable-tail restrictions. Checkpoint21 preserves the next
negative-side attempt and its precise failure, without rewriting checkpoint20.
Node16 remains the distinct positive successor of checkpoint20, not of21.

The second planned negative-side application reached the declared no-compression
signal. Native fail and public retreat recorded it. Node15 is retreated and its
full claim stays open. This is not a native cash-out or local finish.

## Branch choice and next question

For the noncommensurate residual, a future distinct hypothesis must use a
selected-support, genuinely mixed-base or nonlinear operation, or new evidence
against delta(K) tending to infinity. Its success criterion is an exact additional
condition or legal arbitrary-cutoff unit. Repeating a restriction already
satisfied by known positive inputs is a failure signal.

Node16's common-radix reserve theorem was independently admitted at revision276.
It generalizes the fixed binary alphabet to variable exponent families,
including4,8,32. The reviewer noted that the displayed B>=2 parameter is
nonvacuous only at B=2 or3 under the mass condition; collective correction
coprimality itself is not a separate advance. No full node16 proof has executed.

At revision283 the scheduler selects node14, whose operation-existence trigger
is unknown and whose native negative-side ranking has no admission there.
Nearest-ancestor priority prevents existing route ordering from selecting node16.
No failure has been invented for node14 and no new scheduler patch was made.
The diagnosis requests direction on a separate explicit-deferral design.

## Remaining obligations and resources

Obligations1,28,29,30,31,32,33,34 remain open. Accepted results are unchanged;
acceptance8 at checkpoint19 is still the latest proof acceptance.

The shared account has21 of24 moves used, zero reserved, and zero runs used
or reserved. Three moves remain. No allowance or progress counter was reset;
the nonprogress replan counter remains1. All research artifacts remain local.

## Evidence

- [Move2 proof](../attack/erdos-124-half-tail-structure/moves/002-scalar-normalization-obstruction.md)
- [Source supplement](../attack/erdos-124-half-tail-structure/study/SOURCE_UPDATE_2.md)
- [Native journal](../attack/erdos-124-half-tail-structure/journal.jsonl)
- [Checkpoint input](../attack/admission/half-tail-scalar-checkpoint.json)
- [Frozen manifest input](../attack/preflight/half-signed-unit/scalar-checkpoint-manifest.json)
- [Retreat input](../attack/admission/half-tail-scalar-retreat.json)
- [Current selection diagnosis](../attack/admission/common-radix-frontier-diagnosis.md)
- [Node16 admission review](../attack/admission/common-radix-proposal-review.md)

## Continuation addendum, September8,2026

The user authorized routine continuation toward approximately checkpoint50.
The explicit-deferral repair subsequently passed independent review and tests;
its sole minor fixture finding was fixed and independently rechecked. The
[repair record](../../common-radix-controller-repair-rRF9kI/REPAIR_LOG.md) preserves
the exact change. Public replan284 deferred the unstarted node14 and selected
route11; ordinary next now returns node16. No claim, obligation, evidence,
account, usage or retreat fact changed. The nonprogress count rose from1 to2.
This supersedes the earlier selection blocker, not the checkpoint's mathematics.
