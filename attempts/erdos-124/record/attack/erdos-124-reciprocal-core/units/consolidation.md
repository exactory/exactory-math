# Consolidation of the reciprocal-core proof

Date: 2026-09-07. Local claim: minimum-preserving reciprocal-core selection.
Source: moves/001-minimum-preserving-core.md, move 1.
This is a consolidation record, not an independent result review.

## Necessity of the steps

The only non-immediate seed step is the size bound for a gcd-descent set.
A general decreasing gcd chain could have been bounded too loosely by m
additions, which would not ensure reciprocal mass below one. The first
proper-divisor step supplies the needed improvement: g_1<=floor(m/2).
The remaining strict integer decreases give at most g_1-1 more additions.

The strict inequality in seed mass uses distinctness and the occurrence of
an element greater than m. Replacing it by a non-strict termwise bound
alone would lose the strict final endpoint.

The threshold-crossing step must come after the gcd-one seed. Crossing
the reciprocal threshold first would not ensure gcd one. Retaining m in
the seed makes every subsequently added weight at most 1/m.

## Standard-framework replacement

The study proposed a prime-witness analysis of a minimal gcd-one subset.
The written proof replaces it with the elementary descent of a positive
integer gcd. No factorization theorem, optimized minimal subset search,
or computational certificate is needed. The exact target constant survives.

The proof is now in four steps: augmentation from a seed; construction by
gcd descent; strict seed mass bound; application of augmentation. Each step's
purpose and all hypotheses are explicit in the source proof.

## Second route and general statement

A prime-witness proof for a minimal seed would offer a different description
of the seed's size, but shares the same finite gcd mechanism and augmentation
step. No independent second-proof claim is made or separate unit proposed.

The seed argument itself works for every finite D with min D>=3 and gcd one,
without the assumption sigma(D)>=1. The mass assumption is used only to
ensure the augmentation reaches its threshold. The augmentation argument
is the elementary general principle that positive increments bounded by
delta, added to an initial mass below one with total available mass at
least one, first cross one strictly below 1+delta.

No result at minimum two follows: D={2,3} has only one gcd-one subset
containing 2, namely D itself, whose mass is exactly three halves, not
strictly below one plus the reciprocal of its minimum. This is a boundary
check for the existing proof, not a new branch objective.

## Publication and verification limits

The argument is a short elementary auxiliary lemma for a root-connected
reduction. It is not being presented as an independently significant paper.
Its proof can be checkpointed and independently reviewed without claiming
that the original eventual-coverage conjecture is solved or that any Lean
kernel check was performed.
