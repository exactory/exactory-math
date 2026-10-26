# Checkpoint 000008: an accepted reciprocal-core lemma

Date: 2026-09-07. Result accepted at controller revision 82.
Overall completion estimate: 5%, subjective and low confidence.

## Exact accepted statement

For every nonempty finite D of distinct integers at least 3, put m=min D
and sigma(D)=sum_{d in D}1/(d-1). If gcd(D)=1 and sigma(D)>=1, there exists
E subset D containing m with gcd(E)=1 and
1<=sigma(E)<1+1/m.

The proof constructs a gcd-one seed B containing m by decreasing its gcd.
There are at most floor(m/2) additions, so |B|<=m-1; distinctness gives
sigma(B)<1. Adding unused bases up to the first crossing of one adds a
last term at most 1/m, which gives the strict final bound.

- [Complete proof](../attack/erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md)
- [Independent result review](../admission/core-result-review.md)
- [Accepted-result specification](../admission/core-accept.json)
- [Stable checkpoint](../attack/checkpoints/core-001-checkpoint.json)
- [Evidence manifest](../attack/checkpoints/core-001-manifest.json)
- [Consolidation](../attack/erdos-124-reciprocal-core/units/consolidation.md)

The service records acceptance-000001 for obligation-000004, with analytical
reviewed standard. No Lean kernel check, numerical experiment, or finite
mathematical process was used. The proof is a short auxiliary note, not a
standalone publication claim. The local node finished with no publication units;
its accepted proof and immutable checkpoint remain available.

## Contribution and remaining obligations

The selected E has reciprocal mass below four thirds, and more precisely below
one plus the reciprocal of the unchanged minimum. This narrows the proposed
base-set reduction, but supplies no eventual integer representation.

The selected route still needs both:

1. Eventual labelled pure-power coverage for every E in that window at every
   positive cutoff, obligation-000005.
2. Its explicit implication to the original root using core selection,
   obligation-000006.

The full root and the earlier C1 route remain open. The estimate stays at 5%
because the selection lemma does not supply the missing pure-power seed or
a complete proof architecture.

## Lineage, resources, and next work

The logical chain is root, central-prefix method, lattice-aware method, and
reciprocal-core selection, with the last branch anchored at checkpoint-000006.
The native parent is the lattice-aware node; deeper links are logical, not
fabricated native nesting.

Nine of the original 24 shared moves have been used, no move is reserved, and
no mathematical run has occurred. The accepted lemma supplies real recorded
progress for replanning but no account renewal or additional allowance.

Next, develop a reviewed successor for the still-unproved reciprocal-window
coverage statement while retaining the separate bridge. It must use pure-power
structure and distinguish actual coefficient support from formal counts.
A method returning only bounded gaps, a continuous interval without exact
integer recovery, or an expanding no-hit prefix does not prove that statement.
