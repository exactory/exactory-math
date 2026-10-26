# checkpoint-000018: The accepted minimum-three theorem at eleven sixths

Written retrospectively on 2026-09-07 against controller revision 250.
This report was backfilled after the reporting gap was discovered, not written
at the checkpoint's original creation. Immutable evidence is unchanged.

Overall proof-completion estimate: 15% (subjective, low confidence).
This is a retrospective research judgment, not measured coverage, a success
probability or a time estimate. Balanced ternary and an independent reserve lower the minimum-three threshold from 13/4 to 11/6. This is a new mechanism and a proved range below mass two. The critical lower range is still open.

## Exact checkpoint claim

For every nonempty finite set D of distinct integers at least 3 with min D=3, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=11/6, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

Quantifiers: For every such finite D, every positive integer k and every finite labelled deletion F, there exists N(D,k,F), for every integer n>=N there is a finite subset of the remaining labels whose values sum to n.

Assumption IDs: []. Proof policy: reviewed.
In a counterexample report, the displayed universal claim is the claim being
refuted, not a theorem asserted to hold.

## Verification and evidence

Acceptance-000007: self-contained analytical reviewed proof with no mathematical dependencies outside its local argument.

- [Recorded argument](../attack/erdos-124-ternary-reserve/moves/001-ternary-reserve.md)
- [Native problem](../attack/erdos-124-ternary-reserve/problem.json)
- [Journal](../attack/erdos-124-ternary-reserve/journal.jsonl)
- [Independent result review](../admission/ternary-result-review.md)
- [Current research tree](../attack/SEARCH_TREE.md)

Stored checkpoint digest: `47dca12bc7966f05b1d183f2da943bf8bf28dbcc9f95f35d23c18ebeeff5072b`.
Evidence manifest digest: `5228299a26499d6d0c5e382ffc4c716571975c1d44f2114d1eb8ea2a15fc85bd`.
Origin: node-000012, journal move 1.
Accepted record: acceptance-000007; outcome proof; status accepted; progress eligible true.

The checkpoint's immutable verification_status remains pending even after
acceptance; a separate accepted record determines accepted status.
No mathematical computation, certificate verification or Lean build is claimed.

## Change and lineage

The exact minimum-three mass threshold is lowered from the accepted13/4 range to11/6 by a self-contained balanced-ternary tail unit construction, disjoint interval iteration and an untouched mass-one reserve. The full original objective is unchanged. This checkpoint records an analytical candidate pending independent result review.

Logical predecessor: node-000011.
Predecessor checkpoint: checkpoint-000017.
Native parent: none.
Logical lineage does not create unsupported native nesting.

## Branch decision, success criterion and failure signal

Success required fresh unit alternatives in every tail, disjoint iteration and a reserve gap fixed before the seed, including the equality boundary. These are proved. The binary-block successor investigates a family without base three.

Recorded next hypothesis: After independent acceptance, investigate whether a new reserve allocation can retain more of the two seed bases, or whether a distinct digit construction covers minimum bases above three. Any distinct claim or computation requires reviewed admission; do not infer a root theorem from thickness alone.

## Remaining objective and resources

The complete original all-D, all-positive-cutoff threshold-one objective is open.
This checkpoint records the following remaining obligation IDs:
obligation-000001, obligation-000023, obligation-000024.

Resources at the current backfill snapshot, not at the original checkpoint:
19 of 24 shared moves used, zero reserved moves, zero mathematical runs,
five moves left and no renewal. This report grants no proof acceptance,
new allowance or publication status.
