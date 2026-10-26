# C1 move 3: the proposed arithmetic repairs do not initialize the induction

Status: exact interpretation of the independently reviewed move-2 obstruction.
This does not prove or refute C1, C2, or the original pure-power conjecture.
It closes the present abstract seed-initialization attempt, not the objective.

## The induction that survives

For a locally finite sequence of positive integers and integers m>=1, L>=0,
write T_m for its prefix subset-sum set and S_m for its total. The tracked state
consists of

    S_m >= 2L,
    [L,S_m-L] intersect Z subset T_m,
    inf_(r>=m) (S_r-a_(r+1)) >= 2L-1.

Appending a_(m+1) gives both [L,S_m-L] and its translate by a_(m+1).
The surplus condition makes these intervals overlap or be adjacent. Their
union is [L,S_(m+1)-L]. The same future bound holds at m+1 because its
index set is smaller. The represented interval gains a_(m+1) integers,
which is positive. Thus the step delivers a strictly larger covered interval
with the same endpoint loss and preserved future robustness.

This is the conditional append lemma already isolated in root move 3 and C1
move 1. Its missing input is a base state, with L and m chosen jointly.
Divergent surplus supplies the last inequality for every fixed L eventually;
it does not imply the middle condition at that eventual scale.

## Repair attempt 1: add full tail modular coverage

The proposed extra tracked object is the family of residue sets of finite
subset sums of each unused tail, one for each modulus h. Assume each such set
is all of Z/hZ. Given a chosen h, finitely many distinct labelled occurrences
can realize representatives of all residues. The attempted repair would use
such a finite block, together with divergent surplus, to create a nonempty
central seed at a sufficiently late scale.

That implication is false for the abstract sequence class. The sequence in
move 2 has precisely the stipulated all-tail modular coverage and divergent
all-prefix surplus, but its full subset-sum set has upper density below one.
It cannot have any seed paired with the future bound for the same L. Otherwise
the valid induction above would make its subset-sum set cofinite.

Using a finite block does not avoid this obstruction. Subset sums made by
combining disjoint selected blocks are still subset sums of the whole original
sequence. Moving terms into a separate supply changes bookkeeping, not the
set of possible full numerical sums. An arbitrary modular representative can
be large, and a list of residue witnesses does not give consecutive integers
at a controlled scale.

## Repair attempt 2: add irrational nonconcentration and raw label growth

The second proposed repair additionally tracks divergent squared distances
for every irrational alpha and a raw label exponent greater than one. These
properties survive deletion of any finite block. They might suggest that
modular representatives can be spread sufficiently well to initialize the
interval invariant.

This stronger abstract implication is exactly the G principle refuted in
move 2. The same example satisfies both extra requirements. Selecting or
rearranging finitely many allowed labels cannot defeat its exact identity
FS={q^k t+s_q(t):t>=0} or its upper density bound q^(-k). The information
added by this repair is therefore insufficient to prove existence of the base
state, at any scale, for the abstract class under consideration.

This conclusion does not require a uniform quantitative Fourier bound, and
does not assert that one would be sufficient. It also does not replace raw
label growth with the unknown distinct-support growth of a different sequence.

## Failure, preserved result, and successor boundary

The strengthened abstract induction has a correct step but a false universal
base-initialization assertion, even after the two stated arithmetic repairs.
This is the entry's false-ambient-statement/base-scale failure and the
strategy's failed strengthened-base signal. The present use of
strengthen-and-generalise ends here. The failed hypothesis is precisely
initialization from these abstract growth and arithmetic conditions, not
initialization for admissible pure powers.

No new counterexample is manufactured in this move: the proof source is the
infinite construction in move 2 and its independent review. This move supplies
the two exact repair implications and the deduction showing why neither can
close the induction. It is not a second novelty claim for the same example.

The conditional append lemma, finite-preamble lifting, and strict-mass surplus
bound remain available as recorded results pending exact controller acceptance.
The full root and C1 obligations are retained. A distinct successor should keep
the self-similar pure-power digit sets and identify the step from continuous or
bounded-gap coverage to an actual integer seed. It must not reuse G as a seed
theorem or discard occurrence multiplicities.
