# checkpoint-000016: An accepted all-cutoff high-mass theorem

Written retrospectively on 2026-09-07 against controller revision 250.
This report was backfilled after the reporting gap was discovered, not written
at the checkpoint's original creation. Immutable evidence is unchanged.

Overall proof-completion estimate: 10% (subjective, low confidence).
This is a retrospective research judgment, not measured coverage, a success
probability or a time estimate. This first positive infinite parameter range gives eventual representation for every positive cutoff and finite deletion, not just an auxiliary lemma.

## Exact checkpoint claim

For every nonempty finite set D of distinct integers at least 3, with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=3+2/m, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

Quantifiers: For every such finite D, every positive integer k and every finite labelled deletion F, there exists N(D,k,F), for every integer n>=N there is a finite subset of the remaining labels whose values sum to n.

Assumption IDs: []. Proof policy: reviewed.
In a counterexample report, the displayed universal claim is the claim being
refuted, not a theorem asserted to hold.

## Verification and evidence

Acceptance-000005: analytical reviewed proof, with direct dependency acceptance-000001 and explicitly recorded published additive input.

- [Recorded argument](../attack/erdos-124-mass-partition/moves/001-high-mass-completeness.md)
- [Native problem](../attack/erdos-124-mass-partition/problem.json)
- [Journal](../attack/erdos-124-mass-partition/journal.jsonl)
- [Independent result review](../admission/mass-result-review.md)
- [Current research tree](../attack/SEARCH_TREE.md)

Stored checkpoint digest: `98e41c9d8ea57e5aa3cb51b634cf7008427846c39dc9325b26c4dee9098fc735`.
Evidence manifest digest: `49c309e171825be70b3a3c683d9154b0d2871e2e0c22c82a36fcf628ec706d53`.
Origin: node-000010, journal move 1.
Accepted record: acceptance-000005; outcome proof; status accepted; progress eligible true.

The checkpoint's immutable verification_status remains pending even after
acceptance; a separate accepted record determines accepted status.
No mathematical computation, certificate verification or Lean build is claimed.

## Change and lineage

The exact high-mass completeness claim now has an analytical proof candidate: a labelled finite-correction criterion, a three-way mass partition using accepted reciprocal-core selection, and all-cutoff/deletion deficit and multiplier checks. It includes coincident values and the inclusive threshold. The proof yields a terminating finite certificate search without executing one. Independent acceptance remains pending.

Logical predecessor: node-000004.
Predecessor checkpoint: checkpoint-000008.
Native parent: none.
Logical lineage does not create unsupported native nesting.

## Branch decision, success criterion and failure signal

Success required three disjoint supplies, their gap and phase properties, and finite correction without label reuse. The accepted proof supplies these. Lower mass and the separate root implication bridge remain open.

Recorded next hypothesis: After independent acceptance, investigate whether actual pure-power supplies permit a lower-mass substitute for the three disjoint syndetic components, retaining the full threshold-one objective and separately reviewed scope. Do not treat generic arithmetic-profile or signed-tail hypotheses already refuted as sufficient. The complementary mass range and mass-split bridge remain open.

## Remaining objective and resources

The complete original all-D, all-positive-cutoff threshold-one objective is open.
This checkpoint records the following remaining obligation IDs:
obligation-000001, obligation-000002, obligation-000003, obligation-000005, obligation-000006, obligation-000008, obligation-000009, obligation-000011, obligation-000012, obligation-000014, obligation-000015, obligation-000017, obligation-000018.

Resources at the current backfill snapshot, not at the original checkpoint:
19 of 24 shared moves used, zero reserved moves, zero mathematical runs,
five moves left and no renewal. This report grants no proof acceptance,
new allowance or publication status.
