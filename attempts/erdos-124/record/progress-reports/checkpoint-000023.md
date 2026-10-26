# Checkpoint 000023: a restricted one-class conditional bridge

Recorded: September 8, 2026, 04:21 UTC.
Controller checkpoint revision:316.
Source: node-000017, erdos-124-one-class-conditional, journal move2.
Checkpoint digest: `93cbb0ea5f738b14d8c36d261bf263866f2754429980ee7890d17bc10fdcbb59`.
Manifest digest: `80c38432c8004dcb8958fd7860f87d6b246fd9c2fc872034190f1901127ed856`.

## Judgment and exact status

The original all-base, all-positive-cutoff objective remains open.
The approximate subjective judgment remains15%, with low confidence.
No additional unconditional parameter range has been accepted here.

The checkpoint is a reduction snapshot whose candidate result is the
exact implication WOC implies the high-mass theorem below. Independent
result review is in progress. It is not a proof of WOC.

## Exact statements

WOC:

For every nonempty finite set E of distinct integers at least 4 with sigma(E)=sum_{d in E}1/(d-1)>1 and every integer k>=1, there exist an integer r>=1, theta in (R/Z)^r, an open set U in (R/Z)^r meeting K=closure{n*theta:n in Z}, and a set J of positive integers containing intervals of every finite length, such that every n in J with n*theta in U can be written as sum_{(d,j) in H}d^j for some nonempty finite set H of labels (d,j) with d in E and j>=k.

Conditional conclusion:

For every nonempty finite set D of distinct integers at least 3 with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=2+min{1/8,1/m}, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

The implication, including its entire antecedent, is obligation-000037.
Only that implication is offered for proof acceptance. WOC is separately
obligation-000036 and remains open.

## What changed and why the restriction matters

The accepted core bounds select C containing m with gcd(C)=1 and

    1<=sigma(C)<1+min{1/8,1/m}.

At the target's inclusive threshold the complement E has mass strictly
greater than one and minimum at least four. One Bohr supply on E can
therefore replace the two syndetic supplies used in the old mass proof.
The existing correction and reserve argument then yields the conclusion
conditionally. The finite correction support is chosen before the
remaining reserve gap and the represented interval.

The second move checks that finite deletion need not appear in WOC:
raise its positive cutoff beyond every deleted exponent, then use only
those still-legal labels. Coincident numerical powers remain distinct
occurrences throughout. No density or gap property is substituted for
the Bohr-input hypothesis.

This is one routine quantitative conditional corollary and input audit,
not two independent discoveries or a standalone publication claim.
The OC and WOC formulations are preserved in the same evidence package.

## Verification, lineage and resources

Logical predecessor: node-000016 and checkpoint-000022.
There is no native parent. The mathematical dependencies are the accepted
Core, Mass and Quarter intermediates, acceptance-000001,
acceptance-000005 and acceptance-000006. Checkpoint22 supplies lineage,
not a theorem for arbitrary-base Bohr inputs.

The public checkpoint command validated the frozen manifest and acknowledged
journal prefix. A fresh independent reviewer, Dirac, host agent
01a07f41-a636-7d32-b284-c631e3627747, is reading the exact candidate and
inherited evidence without prior reviews or the author's conversation.
Prose mathematics is not checked automatically by the checkpoint command.

The native attack used two analytical entries. The unchanged shared account
has24 of24 moves used, no reservations and no mathematical runs.
Native budget reports no stall: an exhausted shared account is a different
predicate. No cash-out, local full-proof unit or invented strategy failure
has been recorded. A truthful controller move-limit retreat and a separately
reviewed successor are the next lifecycle steps. No future allowance is implied.

The first journal command was denied because the hook treated slash-containing
JSON prose as a path. Read-only status confirmed no append or pending effect.
A concise journal with the exact proof basename and unchanged transition flags
then passed the same direct checks. The proof and admitted claim were not changed,
and no guard or code was disabled.

## Remaining obligations and next hypothesis

WOC, the unconditional high-mass theorem, its lower-mass complement, the
root bridge and the original objective remain open. Accepted structural
families are not weakened or removed.

Next complete independent result review and its immutable acceptance audit.
Then study a genuinely different route for the exact WOC input, with its own
precondition scan, reviewed admission and resource justification. A repeated
restatement cannot reset the exhausted account. A missing proof by itself
is not a recorded mathematical failure.

## Evidence

- [OC-conditional proof](../attack/erdos-124-one-class-conditional/moves/001-oc-conditional-bridge.md)
- [Exact WOC-conditional bridge](../attack/erdos-124-one-class-conditional/moves/002-woc-restricted-bridge.md)
- [Checkpoint input](../attack/admission/one-class-conditional-checkpoint.json)
- [Frozen manifest](../attack/preflight/one-class-conditional/evidence-manifest.json)
- [Restricted result-review context](../attack/admission/one-class-conditional-result-context.json)
- [Journal-input diagnosis](../attack/erdos-124-one-class-conditional/study/JOURNAL_INPUT_DIAGNOSIS.md)

All research output remains local. Nothing was committed, pushed or published.

## Acceptance and resource addendum, September8,2026,04:36 UTC

Fresh independent result review approved the exact implication after reading
both candidates, all three inherited proofs and their intermediate lemmas.
The main agent read the complete review and reread all eight frozen artifacts;
their digests matched the manifest. The service performed its immutable,
transitive dependency and policy audit and accepted obligation-000037 as
acceptance-000010 at revision317, analytical reviewed proof.

The bound route13 retains WOC, obligation-000036, as an undischarged shared
prerequisite. Its consequent obligation-000035 and the original objective are
still open. The checkpoint's pending field is immutable snapshot metadata,
not its current acceptance status. No native cash-out or full-root claim follows.

At revision318 the public controller recorded node17's truthful account
move-limit retreat. The shared usage is24 of24, zero reserved, zero runs.
The native record retains its two successful conditional moves, two completed
tasks, no entry failure and no stall. No route or assumption was abandoned,
no account was reset, and the reviewer has completed and been closed.
The successor literature discovery continues without mathematical execution;
any new method and renewal need separate independent admission.

- [Independent result review](../attack/admission/one-class-conditional-result-review.md)
- [Accepted public specification](../attack/admission/one-class-conditional-result-review.json)
- [Truthful account-limit retreat](../attack/admission/one-class-conditional-retreat.json)
