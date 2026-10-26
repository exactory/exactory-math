# Consolidation of the paired-perturbation counterexample

This is the Closing consolidation for native move 1. The complete proof
is moves/001-paired-perturbation.md. It remains a candidate until its
independent result acceptance, and it concerns only obligation-000010.

## Marked steps and replacements

The potentially ad hoc choices are the paired affine recurrence, the
slowly varying floor perturbation, and the use of raw label counts.
The proof identifies each role explicitly. The recurrence with constant
one supplies every-tail gcd one and excludes irrational norm summability.
The floor perturbation creates an odd-step surplus increment of order
9^t divided by t squared. The two labels create a counting exponent
greater than one, but their coefficient vectors, not label subsets,
are what the base-three support count controls.

No computational input or unproved standard theorem needs replacement.
Telescoping the surplus into local increments replaces any heuristic
comparison of nearby geometric series. The all-prefix split replaces
an argument based only on favourable pair endpoints. Finite cyclic
group arithmetic proves all modular residue claims directly.

## Rewritten proof structure

1. Define the sequence and prove order, multiplicity and the exact
   extension identities before using a seed.
2. Check the first complete-pair seed by integer equalities.
3. Keep the last positive surplus increment and bound both endpoint
   parities; then include the prefixes within a repeated-value block.
4. Derive every-tail gcd and residues, and every irrational norm
   divergence, from the infinitely recurring affine pair relation.
5. Count labels logarithmically but numerical coefficient vectors by
   unique base-three expansion. The latter proves noncoverage.
6. Use positivity of all terms to show that central-prefix coverage
   would imply cofiniteness, obtaining the exact contradiction.

## Second-route assessment and actual scope

A modular exclusion cannot give this counterexample's noncoverage,
because all tail residue classes are represented. An irrational
norm-summability exclusion cannot give it either, because even every
noninteger multiplier has divergent squared norms. Rewriting the same
digit argument with generating functions would share its essential
coefficient encoding and would not be an independent second proof.
No second proof is claimed.

The proved candidate is slightly stronger than the admitted negation:
it has multiplicity exactly two, norm divergence for every noninteger
real multiplier, and at least X-floor(X/9) missing integers below each
positive integer X. These are consequences already proved in the move,
not new unmetered research claims. Neither actual pure-power structure
nor a global extremal optimum is asserted.

## Publication assessment

The construction is a rigorous potential exclusion of one locally
proposed sufficient inference. The novelty study did not establish a
recognized conjecture or standalone publication priority for this exact
conjunction. The argument should remain a local research note unless a
separate, substantive novelty and significance study supports a paper.
Correctness acceptance and publication readiness are separate judgments.

