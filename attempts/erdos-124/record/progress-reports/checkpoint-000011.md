# checkpoint-000011: Exact coefficients still do not give a central seed

Written retrospectively on 2026-09-07 against controller revision 250.
This report was backfilled after the reporting gap was discovered, not written
at the checkpoint's original creation. Immutable evidence is unchanged.

Overall proof-completion estimate: 6% (subjective, low confidence).
This is a retrospective research judgment, not measured coverage, a success
probability or a time estimate. Exact coefficient and tilt reformulations give no positivity estimate. The fourth-moment argument is recorded but not independently accepted.

## Exact checkpoint claim

For every admissible finite D, every positive cutoff k and finite deletion F as in the all-future prefix-surplus claim, there is an integer L>=0 such that for every integer M>=1 there is m>=M with S_m>=2L and every integer in [L,S_m-L] a subset sum of the first m remaining labelled occurrences.

Quantifiers: For every admissible D,k,F there exists one integer L>=0, for every M>=1 there exists m>=M with the stated nonempty represented central interval; L is fixed while m is unbounded.

Assumption IDs: []. Proof policy: reviewed.
In a counterexample report, the displayed universal claim is the claim being
refuted, not a theorem asserted to hold.

## Verification and evidence

Hypothesis only; no accepted result.

- [Recorded argument](../attack/erdos-124-pure-power-seed/moves/01-exact-coefficients.md)
- [Native problem](../attack/erdos-124-pure-power-seed/problem.json)
- [Journal](../attack/erdos-124-pure-power-seed/journal.jsonl)
- [Current research tree](../attack/SEARCH_TREE.md)

Stored checkpoint digest: `66a5826cea0f51fbe5428ccd6341ec09d4278b6f79ffdaf0e606dbf59b209bcf`.
Evidence manifest digest: `7d4a9be01980a3e99f3030a44d0f1e7cfdc9fa8afc21350def2096cf87ce66d3`.
Origin: node-000007, journal move 1.
No acceptance is directly bound to this checkpoint at this report snapshot.

The checkpoint's immutable verification_status remains pending even after
acceptance; a separate accepted record determines accepted status.
No mathematical computation, certificate verification or Lean build is claimed.

## Change and lineage

The seed remains open. Exact coefficient and exponential-tilt pull-backs preserve all labels and quantifiers, but establish no positivity estimate. A complete elementary argument in the saved move gives a fixed-finite-base fourth-moment obstruction to a standard Gaussian prefix limit, pending independent review and without a novelty or root-progress claim. The exact per-base dilation identity does not close a common scalar recurrence; the valid prefix recurrence retains the old seed obligation.

Logical predecessor: node-000005.
Predecessor checkpoint: checkpoint-000009.
Native parent: none.
Logical lineage does not create unsupported native nesting.

## Branch decision, success criterion and failure signal

The branch was retreated. A successor needs a new lattice-scale positivity theorem, with fixed-loss seeds at arbitrarily large prefixes. A real interval or a Gaussian approximation alone is not success.

Recorded next hypothesis: Develop a separately scoped strict-mass coefficient-band approach only if a new lattice-scale positivity input can be identified. The strict forward-surplus certificate is inherited from node-000001 move 3, not a new discovery. One possible new question concerns non-Gaussian local estimates at aligned prefixes; the fixed-cutoff lattice bridge must be proved, not replaced by a real-interval or dimension statement. Keep the equality case and full root open.

## Remaining objective and resources

The complete original all-D, all-positive-cutoff threshold-one objective is open.
This checkpoint records the following remaining obligation IDs:
obligation-000001, obligation-000002, obligation-000003, obligation-000008, obligation-000009.

Resources at the current backfill snapshot, not at the original checkpoint:
19 of 24 shared moves used, zero reserved moves, zero mathematical runs,
five moves left and no renewal. This report grants no proof acceptance,
new allowance or publication status.
