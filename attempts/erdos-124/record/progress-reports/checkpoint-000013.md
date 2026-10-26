# checkpoint-000013: The bounded carry-exchange attempt fails

Written retrospectively on 2026-09-07 against controller revision 250.
This report was backfilled after the reporting gap was discovered, not written
at the checkpoint's original creation. Immutable evidence is unchanged.

Overall proof-completion estimate: 6% (subjective, low confidence).
This is a retrospective research judgment, not measured coverage, a success
probability or a time estimate. The ESS-based bounded-support obstruction and gain estimate are recorded, but are not separate accepted proofs.

## Exact checkpoint claim

For every finite set D of distinct integers d >= 3 with gcd(D) = 1 and sum_{d in D} 1/(d-1) >= 1, and every integer k >= 1, there exists N(D,k) such that every integer n >= N(D,k) is a sum of finitely many labelled occurrences d^j with d in D and j >= k, each pair (d,j) used at most once; equal numerical values from different pairs remain separately available.

Quantifiers: For every admissible finite D, for every integer k >= 1, there exists an integer N, for every integer n >= N, there exist finite subsets S_d of {k,k+1,...} such that n = sum_{d in D} sum_{j in S_d} d^j.

Assumption IDs: []. Proof policy: reviewed.
In a counterexample report, the displayed universal claim is the claim being
refuted, not a theorem asserted to hold.

## Verification and evidence

Hypothesis recording a strategy failure; no accepted result.

- [Recorded argument](../attack/erdos-124-carry-seed/moves/02-exchange-size-obstruction.md)
- [Native problem](../attack/erdos-124-carry-seed/problem.json)
- [Journal](../attack/erdos-124-carry-seed/journal.jsonl)
- [Current research tree](../attack/SEARCH_TREE.md)

Stored checkpoint digest: `443fe28042a983356b4d469d83e2358620230d1e12e290b4f75b4dec82950def`.
Evidence manifest digest: `d9b38873a627d6bd941975307e06fb93031b3627055b3736d865ff733007de01`.
Origin: node-000008, journal move 2.
No acceptance is directly bound to this checkpoint at this report snapshot.

The checkpoint's immutable verification_status remains pending even after
acceptance; a separate accepted record determines accepted status.
No mathematical computation, certificate verification or Lean build is claimed.

## Change and lineage

The second constructive application records a corollary of ESS excluding uniformly bounded-support bounded-difference identities in all deep tails, and an elementary vanishing support-normalized gain for disjoint bounded-difference exchanges. No compatible growing-gap seed or residual cost bound was constructed. This records the declared strategy failure and preserves the full original claim as unproved, without acceptance or progress credit.

Logical predecessor: node-000005.
Predecessor checkpoint: checkpoint-000009.
Native parent: none.
Logical lineage does not create unsupported native nesting.

## Branch decision, success criterion and failure signal

The carry branch was retreated after failing to construct a growing seed with controlled residual cost. A genuinely new mechanism is required; the same unconstructed exchanges are not renewed.

Recorded next hypothesis: A different route would need a proved transfer from persistent tail signed structure to positive coverage with the original labels, together with a proof of that signed structure for all pure-power inputs. The abstract profile counterexample has not settled this stronger signed condition. No such implication is assumed, and the failed unconstructed carry family is not automatically renewed.

## Remaining objective and resources

The complete original all-D, all-positive-cutoff threshold-one objective is open.
This checkpoint records the following remaining obligation IDs:
obligation-000001, obligation-000002, obligation-000003, obligation-000005, obligation-000006, obligation-000008, obligation-000009, obligation-000010, obligation-000011, obligation-000012.

Resources at the current backfill snapshot, not at the original checkpoint:
19 of 24 shared moves used, zero reserved moves, zero mathematical runs,
five moves left and no renewal. This report grants no proof acceptance,
new allowance or publication status.
