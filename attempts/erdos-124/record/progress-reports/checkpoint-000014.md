# checkpoint-000014: A signed-tail counterexample candidate

Written retrospectively on 2026-09-07 against controller revision 250.
This report was backfilled after the reporting gap was discovered, not written
at the checkpoint's original creation. Immutable evidence is unchanged.

Overall proof-completion estimate: 6% (subjective, low confidence).
This is a retrospective research judgment, not measured coverage, a success
probability or a time estimate. The subsequent correction changes only the remaining-obligation list. These two snapshots are one mathematical result, not two.

## Exact checkpoint claim

For every nondecreasing locally finite infinite sequence (a_i) of positive integers with bounded numerical multiplicity, if every tail has gcd one and its finite subset sums meet every residue class modulo every positive integer, liminf_{X->infinity} (log 2)#{i:a_i<=X}/log X>1, sum_i ||alpha a_i||^2=infinity for every irrational real alpha, (S_m-a_{m+1})/a_{m+1}^beta tends to positive infinity for every fixed real beta with 0<beta<1, where S_m=sum_{i=1}^m a_i, and for every integer K>=1 there exist disjoint finite subsets P,Q of {K,K+1,...} with sum_{i in Q}a_i-sum_{i in P}a_i=1, then there exist integers L>=0 and m_0>=1 such that for every m>=m_0, S_m>=2L and every integer in [L,S_m-L] is a subset sum of a_1,...,a_m using each labelled index at most once.

Quantifiers: For every such sequence, assume the full stated arithmetic and growth profile, including every fixed beta in (0,1), and a finite occurrence-respecting signed unit representation in every tail; then there exist fixed L and m_0 giving central-prefix coverage for all m>=m_0.

Assumption IDs: []. Proof policy: reviewed.
In a counterexample report, the displayed universal claim is the claim being
refuted, not a theorem asserted to hold.

## Verification and evidence

Candidate not directly accepted; checkpoint 000015 is the corrected snapshot used for acceptance.

- [Recorded argument](../attack/erdos-124-signed-tail-seed/moves/001-sparse-signed-blocks.md)
- [Native problem](../attack/erdos-124-signed-tail-seed/problem.json)
- [Journal](../attack/erdos-124-signed-tail-seed/journal.jsonl)
- [Current research tree](../attack/SEARCH_TREE.md)

Stored checkpoint digest: `5503b6debefa746091a841f1a975c6c438b7e5337af2e02f2cec3a3fe9bdeb15`.
Evidence manifest digest: `0b42c83546348c27ec19dc869518f46540ea445cfb9dd008acf8dd4690e5107f`.
Origin: node-000009, journal move 1.
No acceptance is directly bound to this checkpoint at this report snapshot.

The checkpoint's immutable verification_status remains pending even after
acceptance; a separate accepted record determines accepted status.
No mathematical computation, certificate verification or Lean build is claimed.

## Change and lineage

A self-contained analytical infinite counterexample candidate now satisfies the exact full profile and legal signed units in every tail, indeed all-tail signed integer coverage and long positive intervals, while numerical subset sums have upper density at most one ninth. This decides only the new abstract inference; it does not decide any original pure-power instance. Independent result acceptance is pending.

Logical predecessor: node-000008.
Predecessor checkpoint: checkpoint-000013.
Native parent: none.
Logical lineage does not create unsupported native nesting.

## Branch decision, success criterion and failure signal

The negative-side test requires all stated antecedents and failure of central-prefix coverage. Use checkpoint 000015 for the accepted result. This historical list incorrectly includes already accepted obligations 000004 and 000007.

Recorded next hypothesis: Once independently accepted, exclude the signed-tail strong-profile inference as a route to C1. The original problem would require additional pure-power structure or a separately justified support-cost mechanism, not another use of the same unproved generic implication.

## Remaining objective and resources

The complete original all-D, all-positive-cutoff threshold-one objective is open.
This checkpoint records the following remaining obligation IDs:
obligation-000001, obligation-000002, obligation-000003, obligation-000004, obligation-000005, obligation-000006, obligation-000007, obligation-000008, obligation-000009, obligation-000010, obligation-000011, obligation-000012, obligation-000014, obligation-000015.

Resources at the current backfill snapshot, not at the original checkpoint:
19 of 24 shared moves used, zero reserved moves, zero mathematical runs,
five moves left and no renewal. This report grants no proof acceptance,
new allowance or publication status.
