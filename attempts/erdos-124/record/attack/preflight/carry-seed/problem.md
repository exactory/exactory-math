# Problem study: eliminating a finite low-digit reservoir

Date: 2026-09-07. Proposed scope: the exact original obligation-000001.
Logical predecessor: accepted all-future surplus checkpoint-000009.
The newer coefficient attack's stopped record and checkpoint-000011 supply a
method exclusion, not an accepted proof of the desired representations.

## Queries and hits

See sources/queries.md for the complete problem and strategy sweeps, response
paths, identifiers, reading scope, and access failures. The primary sources
used here are BEGL96, DOI 10.4064/aa-77-2-133-138, and Bergelson-Simmons,
arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016. The canonical statement is
the study-root sources/124.lean, theorem Erdos124.erdos124.ne_zero.

## Exact statement comparison

The target is every finite set D of distinct integer bases at least 3, with
collective gcd one and reciprocal mass at least one, and every positive k.
Every sufficiently large integer must be a sum of labelled powers d^j,
j>=k, with each pair used at most once. Equal values from different base
labels remain distinct supplies. There is no bound on max D or k, no strict
reciprocal inequality, no pairwise-coprimality assumption, and no unit supply.
The solved zero-cutoff neighbour permits one occurrence (d,0) for every d.
It does not solve the target. The arbitrary-finite-deletion neighbour follows
from a proof for every k by increasing k past all deleted exponents.

## Constraints learned

The zero-cutoff Brown argument gives a complete initial digit system. Removing
finitely many low coordinates leaves a finite reservoir whose elimination is
exactly the issue this construction will attack. No claim that the reservoir
can be eliminated has been proved in this preflight.

BEGL96 creates many equal-step switches by finite differences across many
different bases. Its theorem chooses a cutoff-dependent finite subset from
an infinite positive-density supply. A fixed arbitrary D has no such
unbounded disjoint-base supply, so that construction cannot be copied here.

Bergelson-Simmons obtain complete sets by separately allocating syndetic
subset-sum components and an arithmetic component. The actual disjointness
hypotheses cannot be replaced by repeated use of the same occurrence.
Syndeticity alone is insufficient, as their examples show.

The accepted surplus result makes later interval propagation available once
a compatible seed is proved. The new route targets the original statement
directly through legal digit exchanges; it does not replace the root by the
seed conjecture, an unbounded numerical prefix, or a Gaussian approximation.
The intended new question is whether variable-length exchanges can remove
the low-digit reservoir while keeping exact labelled support legal.

## Stop reason

The fixed source sweep is complete. No solution of the exact statement was
located, and no novelty is claimed. The new construction is a hypothesis to
be attempted only after reviewed admission and a reserved move.

