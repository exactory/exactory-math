# Checkpoint 000007: the available operations do not give one instance

Date: 2026-09-07. Overall completion estimate: 5%, subjective and low confidence.

## Exact diagnostic

At every fixed positive cutoff, base addition and cutoff decrease cannot
generate all admissible finite base sets from any finite fixed list. For M
larger than the list's bases, the consecutive set {M+1,...,4M} is disjoint
from that list, has gcd one, and has reciprocal mass greater than one.

Inclusion-minimal admissible subsets in successive disjoint blocks provide
infinitely many incomparable generators for those operations. This is not
logical independence of the coverage assertions and does not exclude a new
transfer operation or a useful infinite one-parameter family.

- [Move and proof](../attack/erdos-124-lattice-aware/moves/002-base-addition-does-not-give-one-instance.md)
- [Independent scope review](../admission/lattice-move-2-review.md)
- [Checkpoint specification](../admission/checkpoint-lattice-002.json)
- [Recorded retreat](../admission/retreat-lattice-class.json)

The generating-instance entry failed on its stated operation class. The
lattice-aware node retreated; the separately admitted reciprocal-core route
was not abandoned. Its selection lemma, restricted-coverage statement, and
bridge remain distinct claims. At this checkpoint none was accepted.

The next work is the exact core-selection construction from checkpoint-000006.
Revisit the failed finite-generator route only when a new proven transfer
operation addresses its obstruction. No budget was renewed or refunded.
