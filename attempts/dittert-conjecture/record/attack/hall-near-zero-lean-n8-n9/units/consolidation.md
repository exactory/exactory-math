# Proof consolidation

The external coefficient-positivity step was the part requiring a smaller trusted base. It is replaced by norm_num/ring proof terms for the literal identities and elementary order proofs for every positive basis term and both endpoints. The constants and intervals are unchanged.

The rewritten argument is in PROOF.md. A general Bernstein soundness theorem was unnecessary for these two fixed certificates: direct positive-basis proofs are short and keep all hypotheses visible. The inherited source's Sturm checks provide a mathematically different computational route, but no Lean Sturm proof was built here, so no independent second formal proof is claimed.

The exact generality obtained is the full closed interval for each of the two specified polynomials. No statement for additional dimensions or larger intervals is asserted. The computational identity could be replaced only by another algebraic derivation; removing it would not improve this bounded verification artifact enough to justify a new project.
