# Consolidation

Source moves: 1 and 2. Exact scope: every boundary global maximizer for each
integer n=8,...,15, using the explicitly listed structural/permanent inputs.

The following potentially unexplained steps were replaced by full deductions.

- The localization |e|<1/10 now follows directly by integrating
  g'(e)=n e/((d+e)(n-d-e)), before any local Taylor estimate.
- Proper-cut deficits use signed excesses and their exact inclusion-exclusion
  identity; no sign branch is dropped.
- The marginal denominator E is positive because E>=q_i>0, before division.
- Every marginal subset average is proved to reduce to one smallest line,
  with ties and both orientations included.
- The n=10 localization is derived from the global deficit budget, not
  assumed from a near-uniform branch.
- The n=8,9 tail is excluded across every feasible parameter by proved
  monotonicity and stationarity, including what happens beyond E's pole.
- The n=9 support compression is justified by inclusion of feasible product
  domains and uses a floor independent of z.
- Polynomial positivity has a second arithmetic route: direct Bernstein
  multiplication rather than power expansion plus conversion. All nine
  residual polynomials are certified without subdivision, including the two
  near-zero intervals for which the source uses Sturm root counts.

PROOF.md is the rewritten complete coverage argument. CODE_MAP.md connects
every source skip/compression to its mathematical reason and the independent
check. This is an attributed exposition and independent verification, not a
second proof of the full Dittert theorem; the structural and permanent inputs
are shared and explicitly named. No full Lean formalization was attempted.

The argument proves the parameter-cover statement for n=8,...,15 exactly.
It also exposes generic lemmas for signed deficit and capped products, but
no separate novelty claim or broader theorem is asserted for them.

