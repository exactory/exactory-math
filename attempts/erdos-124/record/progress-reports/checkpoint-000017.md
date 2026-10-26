# checkpoint-000017: The accepted quarter-mass improvement

Written retrospectively on 2026-09-07 against controller revision 250.
This report was backfilled after the reporting gap was discovered, not written
at the checkpoint's original creation. Immutable evidence is unchanged.

Overall proof-completion estimate: 10% (subjective, low confidence).
This is a retrospective research judgment, not measured coverage, a success
probability or a time estimate. The sufficient bound becomes 3+min{1/4,2/min D}. This is a genuine quantitative improvement using the same mechanism, so the subjective estimate is unchanged.

## Exact checkpoint claim

For every nonempty finite set D of distinct integers at least 3, with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=3+min{1/4,2/m}, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

Quantifiers: For every such finite D, every positive integer k and every finite labelled deletion F, there exists N(D,k,F), for every integer n>=N there is a finite subset of the remaining labels whose values sum to n.

Assumption IDs: []. Proof policy: reviewed.
In a counterexample report, the displayed universal claim is the claim being
refuted, not a theorem asserted to hold.

## Verification and evidence

Acceptance-000006: analytical reviewed proof, with direct dependencies acceptance-000001 and acceptance-000005.

- [Recorded argument](../attack/erdos-124-quarter-mass/moves/001-quarter-mass-completeness.md)
- [Native problem](../attack/erdos-124-quarter-mass/problem.json)
- [Journal](../attack/erdos-124-quarter-mass/journal.jsonl)
- [Independent result review](../admission/quarter-result-review.md)
- [Current research tree](../attack/SEARCH_TREE.md)

Stored checkpoint digest: `32513300fcc14d53726380aa9cfd2a598fef719a0f1e4131c8517d709508d879`.
Evidence manifest digest: `ab59ab3fee5a4a4b9d8739030f497e216c4bbacb770525958dba5cda1ad0f884`.
Origin: node-000011, journal move 1.
Accepted record: acceptance-000006; outcome proof; status accepted; progress eligible true.

The checkpoint's immutable verification_status remains pending even after
acceptance; a separate accepted record determines accepted status.
No mathematical computation, certificate verification or Lean build is claimed.

## Change and lineage

A new analytical proof candidate lowers the high-mass sufficient threshold to3+min{1/4,2/minD}. It proves a uniform gcd-one minimum-preserving reciprocal core below9/8, a compatible second-bin bound below9/8, and retains the accepted occurrence-preserving amplification. The inclusive13/4 small-minimum range, every positive cutoff and finite labelled deletion are covered. Independent result acceptance is pending.

Logical predecessor: node-000010.
Predecessor checkpoint: checkpoint-000016.
Native parent: none.
Logical lineage does not create unsupported native nesting.

## Branch decision, success criterion and failure signal

Success required the strict 9/8 core and second-bin bounds, including all small-base cases, followed by the accepted labelled amplification. A three-component mass-one allocation cannot by itself go below total mass three; the next branch changes the seed construction.

Recorded next hypothesis: After independent acceptance, prioritize an analytically new mechanism below total reciprocal mass three, where merely tightening a three-group allocation cannot suffice. Preserve the exact complementary obligation and the full threshold-one objective; revisit the Cantor route only with new control of its positive-cutoff integer discrepancy.

## Remaining objective and resources

The complete original all-D, all-positive-cutoff threshold-one objective is open.
This checkpoint records the following remaining obligation IDs:
obligation-000001, obligation-000002, obligation-000003, obligation-000005, obligation-000006, obligation-000008, obligation-000009, obligation-000010, obligation-000011, obligation-000012, obligation-000013, obligation-000014, obligation-000015, obligation-000017, obligation-000018, obligation-000020, obligation-000021.

Resources at the current backfill snapshot, not at the original checkpoint:
19 of 24 shared moves used, zero reserved moves, zero mathematical runs,
five moves left and no renewal. This report grants no proof acceptance,
new allowance or publication status.
