# checkpoint-000012: A support-aware switch criterion without the switches

Written retrospectively on 2026-09-07 against controller revision 250.
This report was backfilled after the reporting gap was discovered, not written
at the checkpoint's original creation. Immutable evidence is unchanged.

Overall proof-completion estimate: 6% (subjective, low confidence).
This is a retrospective research judgment, not measured coverage, a success
probability or a time estimate. A conditional support ledger identifies the missing construction but settles no original family.

## Exact checkpoint claim

For every finite set D of distinct integers d >= 3 with gcd(D) = 1 and sum_{d in D} 1/(d-1) >= 1, and every integer k >= 1, there exists N(D,k) such that every integer n >= N(D,k) is a sum of finitely many labelled occurrences d^j with d in D and j >= k, each pair (d,j) used at most once; equal numerical values from different pairs remain separately available.

Quantifiers: For every admissible finite D, for every integer k >= 1, there exists an integer N, for every integer n >= N, there exist finite subsets S_d of {k,k+1,...} such that n = sum_{d in D} sum_{j in S_d} d^j.

Assumption IDs: []. Proof policy: reviewed.
In a counterexample report, the displayed universal claim is the claim being
refuted, not a theorem asserted to hold.

## Verification and evidence

Hypothesis only; no accepted result.

- [Recorded argument](../attack/erdos-124-carry-seed/moves/01-support-ledger.md)
- [Native problem](../attack/erdos-124-carry-seed/problem.json)
- [Journal](../attack/erdos-124-carry-seed/journal.jsonl)
- [Current research tree](../attack/SEARCH_TREE.md)

Stored checkpoint digest: `890030db848680ab44fcdd3a2a7c06988cfac01ce7a6df2c79038d6f7df8e483`.
Evidence manifest digest: `3e82842ae534fc3415072a7056f8a8e2ade924d10df89c1287f5e3563d5cc94a`.
Origin: node-000008, journal move 1.
No acceptance is directly bound to this checkpoint at this report snapshot.

The checkpoint's immutable verification_status remains pending even after
acceptance; a separate accepted record determines accepted status.
No mathematical computation, certificate verification or Lean build is claimed.

## Change and lineage

Move 1 records a complete analytical proof of the support-aware conditional switch criterion and the exact residual subset-sum gap identity. The constant buffer rule is excluded by diameter. The sufficient condition is explicit, but the all-input variable-length switch family and its cost bound remain unproved, so no root acceptance or new progress credit is claimed.

Logical predecessor: node-000005.
Predecessor checkpoint: checkpoint-000009.
Native parent: none.
Logical lineage does not create unsupported native nesting.

## Branch decision, success criterion and failure signal

Success required compatible exact switches and a residual gap bound after consuming their supports. Failure is absence of that family or uncontrolled support cost. Checkpoint 000013 records the subsequent failure.

Recorded next hypothesis: Try variable-length exact power switches satisfying h_1=1, h_t<=1+sum previous h and the support ledger S_{i-1}-a_i+W-W_{i-1}>=2B-1 at every retained index. Establish compatibility and cost before any finite run. The ledger itself is not the missing construction.

## Remaining objective and resources

The complete original all-D, all-positive-cutoff threshold-one objective is open.
This checkpoint records the following remaining obligation IDs:
obligation-000001, obligation-000002, obligation-000003, obligation-000005, obligation-000006, obligation-000008, obligation-000009.

Resources at the current backfill snapshot, not at the original checkpoint:
19 of 24 shared moves used, zero reserved moves, zero mathematical runs,
five moves left and no renewal. This report grants no proof acceptance,
new allowance or publication status.
