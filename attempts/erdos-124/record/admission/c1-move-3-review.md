# Independent finding on the two arithmetic repairs

Date: 2026-09-06.
Reviewed: `attack/erdos-124-central-prefix/moves/003-arithmetic-repairs-do-not-initialize.md`.
Reviewer: host session `01a078c1-781b-7580-9bcf-aaa4625cf458`.

The logical interpretation is correct. No mathematical error was found.

The first proposed implication, from divergent prefix surplus and every-tail
modular coverage to a central seed with the matching future surplus bound,
is refuted by the checked move-2 example. The second implication adds
irrational squared-norm divergence and raw label exponent greater than one;
the same example satisfies these premises and still has upper subset-sum
density at most q^(-k)<1. Finite residue witnesses and disjoint selections of
allowed labels produce only subset sums already present in that full set.
They cannot remove this obstruction.

Calling the second implication G is justified under its divergent-surplus
premise. A joint seed implies eventual central-prefix coverage by the append
lemma. Conversely, eventual central-prefix coverage supplies a fixed L;
divergent surplus then allows a sufficiently late m with every future surplus
at least 2L-1, while S_m>=2L and the represented interval also hold.
This conditional equivalence does not establish C1 implies C2 for pure-power
instances where surplus divergence has not been proved.

The append step remains valid: the integer intervals join, their cardinality
increases by a_(m+1), and restricting the future index set preserves its lower
bound. What fails is the universal initialization assertion from the specified
abstract premises. Neither repair's failure refutes pure-power C1/C2, excludes
other initialization methods, or invalidates the recorded finite-preamble
lemma and strict-mass conditional criterion.

This finding adds no counterexample or novelty claim, grants no controller
acceptance or budget credit, and does not adjudicate an unsubmitted successor.
No mathematical execution was performed and no harness file was edited.
