# Strategy study: construct the reciprocal core

Date: 2026-09-07. Strategy: make-the-proof-constructive.

## Queries and primary reading

The eight source-by-source queries in problem.md explicitly include the
gcd-one seed, minimality, reciprocal constraint and greedy extension.
Their identifiers, reading status and results are part of this strategy
study. Pongsriiam arXiv:1306.4891 counts relatively prime subsets; it
does not provide the desired weighted seed theorem. The greedy
subset-sum-distinct-sequence paper returned by the secondary query
concerns a different infinite residue-avoidance problem.

## Constraints selecting the seed branch

The construction starts with a gcd-one seed containing the least base,
then adjoins unused bases until the reciprocal threshold is first met.
The operation and the stopping condition are finite for each input D,
but the theorem is universal over all finite inputs.

The amplification lemma must account for gcd, the distinguished minimum,
mass growth, and the final strict upper bound simultaneously. A candidate
seed is inclusion-minimal among gcd-one subsets containing the minimum.
A prime-witness argument is proposed to control its size relative to that
minimum. No proof of this seed bound has been performed in this study.

Step 2 is inapplicable: the requested output is a feasible object, not an
extremal value or an optimization claim. Step 3 dispatches seed-and-amplify.
Use a computer-free construction and proof of the seed for arbitrary D.
No finite mathematical process, compiler, search, or numerical experiment
is proposed. If a computer search appears necessary, stop this proof move
and seek the separate reviewed computation admission it would require.

The approximation/forcing branch does not apply to these finite sets.
Any failure of seed mass below one or of preservation under adjoining a
base must be recorded, not patched by deleting the gcd requirement.
The final object must be read against the exact original lemma claim.

## Stop reason

The fixed query list was completed. The count-theoretic hits do not supply
a proof. The exact seed and extension obligations suffice to test the
construction analytically under the original shared account.
