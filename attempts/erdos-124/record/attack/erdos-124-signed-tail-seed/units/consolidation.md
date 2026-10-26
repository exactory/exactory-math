# Consolidation of the signed-block counterexample

Producer: node-000009, closed local move1. This is the harness
consolidation entry, outside the move budget. Independent result
acceptance is still pending.

## Marked steps and replacements

The sparse endpoint choice, the baseline floor estimate and the
growing-support norm implication are the steps needing explanation.
The proof in moves/001-sparse-signed-blocks.md now separates their
roles before the seed: endpoint replacement forces the legal unit,
the convex reciprocal identity gives an elementary surplus lower
bound, and reciprocal support lengths allow Cauchy-Schwarz to prove
norm divergence. No computation or unproved asymptotic approximation
is needed.

The standard geometric and floor inequalities replace any potential
numerical seed search. Their initial checks are exact small integer
inequalities. The two prefix types are checked separately so a
gadget-endpoint estimate is not mistaken for an all-prefix proof.
The coefficient integer is an encoding of vectors, not an unjustified
injection of label subsets or numerical sums.

## Consolidated proof and scope

The complete rewritten proof is the single self-contained file
moves/001-sparse-signed-blocks.md. Its order is: extension laws, seed,
legal tail identities, gcd and modular coverage, squared norms,
all-prefix surplus, labelled counts, numerical support and the
central-coverage contradiction. No proof claim here depends on a
source absent from that file.

The independent-route check gives no second proof of the full
counterexample: the digit-weight support bound and sparse endpoint
modification remain its essential construction. Recasting the same
coefficient count as generating-function support would be an
exposition, not an independent second route.

The argument actually gives one exhibited sequence with legal signed
coverage of every integer in every tail, arbitrary long positive
intervals in every tail, norm divergence for every noninteger
multiplier, and numerical subset-sum upper density at most one ninth,
in addition to every hypothesis of the admitted inference. These are
features of this same example and belong to one narrative, not
separate publication units. The statement decided is the exact
abstract inference only. No pure-power result, route bridge, formal
verification or original objective closure follows.
