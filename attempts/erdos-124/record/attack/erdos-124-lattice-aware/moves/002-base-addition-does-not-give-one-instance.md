# Move 2: the class step does not produce one generating instance

Node: node-000003. Strategy: reduce-and-translate.
Entry: reduce-to-one-generating-instance. Reserved at revision 67.
Status: closure diagnostic and failure of the stated class step, not a root proof.

## Applicable plan step and available operations

The universal quantifier selects strategy step 4. Step 3 does not apply:
the leading objects are base sets and cutoffs, not a class of solutions.
The selected map in move 1 had an exact pullback and did not fire its entry
failure signal, so the conditional second and third map attempts do not run.

Let P(D,k) mean eventual labelled pure-power coverage at cutoff k.
If E is a subset of D and P(E,k) holds, the same representations prove
P(D,k): choose no occurrence from every base in D outside E. Every pair
already used for E stays a distinct pair for D. Thus adjoining bases
preserves the property. Reducing the cutoff also preserves it by retaining
the same finite exponent selections.

Arbitrary removal of bases is not an established preservation operation.
A common dilation changes the gcd and the represented lattice, and is not
one of the available admissibility-preserving operations. No new operation
of this kind is assumed.

## Why finitely many fixed base sets do not generate the class

Fix any finite list of nonempty finite base sets G_1,...,G_s. If the list
is empty it generates nothing. Otherwise choose an integer M>=3 larger
than every base in their union. Define
D_M={M+1,M+2,...,4M}.

This set has gcd one because it contains two consecutive integers. Also
sigma(D_M)=sum_{t=M}^{4M-1}1/t. Splitting at 2M gives

sum_{t=M}^{2M-1}1/t > M/(2M)=1/2,
sum_{t=2M}^{4M-1}1/t > (2M)/(4M)=1/2.

Every inequality is strict because each denominator in its block is
strictly smaller than the displayed comparison denominator. Hence
sigma(D_M)>1, so D_M is admissible. Its bases are all greater than every
base in every G_i. Consequently no G_i is a subset of D_M.

Starting from a G_i, adjoining bases and decreasing a cutoff never removes
a base. Therefore these operations cannot reach D_M from any G_i. The
same argument works at each fixed positive cutoff.

There are in fact infinitely many independent minimal admissible generators
for this operation. Inside each D_M choose a subset minimal for the two
conditions gcd one and reciprocal mass at least one. Such a subset exists
because D_M is finite and admissible. Repeat with the next M larger than
the preceding chosen sets. These minimal sets have disjoint base supports.
None can be reached from another by adjoining bases. This is a statement
about the specified operation, not a structural classification of all
possible proofs.

## The separately admitted core question

Checkpoint-000006 led to the separately reviewed node
erdos-124-reciprocal-core. Its exact target is to select E containing
m=min D with gcd(E)=1 and 1<=sigma(E)<1+1/m.

That assertion remains unproved at this move. It is a useful candidate
restriction, but it is not a single concrete input. The restricted
representation assertion still quantifies over infinitely many E and all
positive cutoffs. Merely enumerating all such E by one integer does not
provide fixed construction data or a propagation theorem.

The proposed controller route keeps core selection, restricted coverage,
and their implication bridge as separate obligations. None is discharged
by the class diagnostic.

## Failure signal and limits

The required generating-instance premise of the entry is not established.
The available base-addition closure has infinitely many independent
generators, as proved above. Accordingly the planned class step is recorded
with failure_signal_fired=true. It has not produced the entry's requested
equivalence to one concrete construction problem or one useful parameter
value.

The failed statement is narrower than the original conjecture. This does
not rule out a genuinely new closure operation, a useful one-parameter
family with an additional transfer theorem, or the core-selection route.
It also does not turn the failure of one direct thickness test into a
failure of every continuous or lattice-aware argument.

The strategy ends on this failure. Its later import condition is false
(the missing input is not a vocabulary-free imported lemma). The abandoned
route is not revived after the strategy has ended. Those facts close the
conditional action items without claiming that an unexecuted import or
revival succeeded.

## Problem metadata corrections

Move 1 already recorded an exact real thickening equivalence. The earlier
sentences saying no exact continuous equivalence was known referred to the
pre-move model and are now qualified accordingly. T itself remains unproved.
The full original claim, direction, and mode are unchanged in this move.

The arithmetic above is a computer-free diagnostic under the reserved
entry. No finite search, experiment, or formal check was run. It is not a
standalone novelty claim or controller-accepted proof of any root obligation.
