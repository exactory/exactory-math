# Checkpoint 000010: the stronger abstract seed inference fails

Date: 2026-09-07. Overall estimate: 6%, unchanged and low-confidence.

## Exact result and verification

The exact universal claim of obligation-000010 is refuted by the sequence
defined in the [complete proof](../attack/erdos-124-strong-surplus-seed/moves/001-paired-perturbation.md):
two labelled copies of b_(2t)=9^t+floor(9^t/t) and
b_(2t+1)=3b_(2t)+1 for every t>=1.

It is locally finite, nondecreasing, positive, and has numerical multiplicity
two. Every tail has gcd one and every finite-subset-sum residue modulo every
positive integer. Its labelled counting exponent is log(4)/log(3)>1, and
the squared-norm sum diverges for every noninteger real multiplier.
For every fixed beta in (0,1), its all-prefix surplus divided by the beta
power of the next term tends to positive infinity. Yet its numerical
subset sums contain at most floor(X/9) positive integers up to X.

The [fresh-context GPT-6 Astra review](../admission/strong-seed-result-review.md)
checked every proof step and the exact claim and evidence hashes.
Acceptance-000003 accepted the counterexample at controller revision 119.
The complete stored checkpoint digest is
6014f5c37e695e93914f12781f56f8605753f78f1fbe4bf411105fe08735a410.
The analytical manifest digest is
cf16896e3550b80ae9bd7d644b819279cb606c4959b777d339507d7fbc7709ac.
Its single proof artifact is self-contained and has no imported theorem,
accepted-result dependency or mathematical process.

## Lineage and what changed

Node-000006 is a logical successor of finished node-000005 through
checkpoint-000009, with no native parent. It asked whether upgrading
qualitative surplus to every sublinear power could repair the abstract
seed route. The older constant-perturbation example had only logarithmic
surplus and did not decide this stronger claim.

The single reserved seed-and-amplify move proved extension invariants
before checking the first complete-pair seed, quantified all-prefix limits,
and gave a support deficit. Its exact counterexample closed this local
attack. Consolidation and the claim test retained a local research note,
with zero publication units because standalone novelty and significance
were not established.

## Boundaries and next hypothesis

This is not a counterexample to the original all-D, all-positive-cutoff
pure-power claim, which remains open. It is not a result for the endpoint
beta=1 and does not rule out every stronger surplus condition. It rejects
the proposed route that used the stated generic inference as a premise.

The accepted core and qualitative surplus lemmas remain intact. C1's
represented seed, the reciprocal-window coverage problem, the full
pure-power strong profile, and all their relevant bridges remain unproved.
The prospective next distinction is between genuinely linear relative
surplus (relevant to strict reciprocal mass) and the critical regime, or
an exact arithmetic mechanism specific to pure powers. Either needs its
own study and reviewed admission before execution.

A fixed-cutoff finite check was considered but not selected: without an
accepted finite reduction or a necessary bounded strategy decision it
would not support the original all-cutoff objective. No such process ran.

## Resources and reporting judgment

Eleven shared moves, zero mathematical runs, and no resource renewal.
The controller marks this auxiliary counterexample ineligible for progress
renewal; replanning used no progress acceptance and recorded one nonprogress
round at revision 122. The full objective was not closed or marked false.

The 6% estimate is unchanged. This checkpoint excludes an unjustified
inference but settles no new pure-power family. It improves the route
record rather than supplying the missing representation theorem.
