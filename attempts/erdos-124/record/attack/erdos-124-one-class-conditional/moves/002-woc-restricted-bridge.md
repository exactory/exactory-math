# Move 2: the exact restricted one-class bridge

Node: node-000017. Strategy: work-conditionally-then-discharge.
Entry: condition-on-the-one-missing-input, Action 2.
Reservation: controller revision 313.
Status: analytical proof candidate of obligation-000037.
No mathematical program or formal checker was run.

## 1. Exact proposition

If the following one-class hypothesis WOC holds: For every nonempty finite set E of distinct integers at least 4 with sigma(E)=sum_{d in E}1/(d-1)>1 and every integer k>=1, there exist an integer r>=1, theta in (R/Z)^r, an open set U in (R/Z)^r meeting K=closure{n*theta:n in Z}, and a set J of positive integers containing intervals of every finite length, such that every n in J with n*theta in U can be written as sum_{(d,j) in H}d^j for some nonempty finite set H of labels (d,j) with d in E and j>=k. Then the following high-mass representation assertion holds: For every nonempty finite set D of distinct integers at least 3 with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=2+min{1/8,1/m}, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

WOC is the antecedent of this implication. It is not an established
assumption of the original objective. The empty assumption_ids of the
implication claim mean that the entire implication is to be proved in
ordinary classical mathematics; they do not remove its antecedent.

We use Core, Mass and Quarter with the exact accepted evidence references
specified in [Move 1](001-oc-conditional-bridge.md), Section 2. Their paths
are relative to the attack root, as stated there. The argument below imports
the unconditional intermediate lemmas and finite-support proof steps, not
the conclusion under OC.

## 2. Remove the explicit finite-deletion requirement by truncation

Assume WOC. Fix any D,k,F in the high-mass conclusion. Define a positive
integer q by

    q=k                         if F is empty,
    q=max{k,1+max{j:(d,j) in F}} otherwise.

Every label at exponent j>=q lies outside F. We may ignore all other
available labels: existence of a representation on this smaller supply
implies existence on the required surviving supply. This is a one-way
restriction of available labels, not a change of the target cutoff to one
or a demand for a threshold uniform in k or F.

Set m=min D and delta=min{1/8,1/m}. By the same unconditional core
selection proved in Move 1, Section 2, choose C subset D with

    m in C,    gcd(C)=1,    1<=sigma(C)<1+delta.

Specifically Quarter, Section 2, suffices when m<=8, and Core when m>=8.
Let E=D minus C. Then

    min E>=m+1>=4,       sigma(E)>1.                        (1)

The second inequality follows strictly even when sigma(D)=2+delta,
since the core mass has a strict upper bound. Thus E is nonempty.

Let Q_C and Q_E contain all labels of these base groups at exponents
j>=q, with no further deletion. Their base-label supports are disjoint.
All these labels are legal for the original input D,k,F.

## 3. Apply only WOC and repeat the unconditional correction

By (1), WOC applies to E and q. It supplies finite r,theta,U and
positive thick J with U intersect K nonempty, where
K=closure{n*theta:n in Z}, and

    J intersect {n>=1:n*theta in U} contained in FS_0(Q_E). (2)

These are the sole Bohr-input facts used in Move 1, Sections 4 and 5.
No statement for bases equal to three, reciprocal mass equal to one,
or a nonempty deletion on E has been invoked.

Here are the remaining steps explicitly, without assuming OC.
By the accepted Mass, Sections 3.2 and 5.2, the phases of FS_0(Q_C)
are dense in K, because gcd(C)=1. Compactness supplies a nonempty
finite V subset FS_0(Q_C) whose translates u*theta+U cover K.
Choose one finite labelled representation L_u for each u in V, let
L be their union, and let M=max V.

The positive thick set

    T={n>M:n-h in J for every integer h with 0<=h<=M}

is contained in FS_0(Q_E union L). Indeed, for n in T choose u in V
with (n-u)*theta in U. Then n-u is positive and in J, so (2)
represents n-u on Q_E. Adjoin the chosen representation of u on L_u.
The label supports are disjoint. Thickness follows by trimming long
positive intervals in J as in Move 1.

After L has been fixed, the accepted Mass, Sections 2 and 5.1, give
the finite positive integer gap bound

    g=ceil(sum_{d in C} d^q/(d-1)
           +sum_{ell in L} value(ell))

for FS_0(Q_C minus L). Choose an interval [A,A+g-1], A>=1,
inside T. For n>=A+g-1 choose a represented reserve value

    t in FS_0(Q_C minus L) intersect [n-A-g+1,n-A].

Such a t exists by the gap bound, and n-t is represented on
Q_E union L. Joining these two disjoint finite label supports
represents n. This uses only labels at exponents at least q, hence
at least k and outside F.

Taking N=A+g-1 proves the exact high-mass conclusion under WOC.
Neither the inclusive mass endpoint nor any input D,k,F is lost.

## 4. Exact input audit

The following comparison records the actual logical restrictions.
It does not assert strict logical inequivalence between the hypotheses.

| Input feature | OC | What the proof above uses |
|---|---|---|
| Bases | At least three | At least four, since C contains the minimum |
| Reciprocal mass | At least one | Strictly greater than one by the core upper bound |
| Cutoff | Every positive k | Every positive q, including q beyond a deletion |
| Finite deletion | Explicit arbitrary F | Empty deletion after raising the cutoff |
| Gcd of input group E | No condition | No condition |
| Bohr witnesses | Finite dimension, open U meeting K, positive thick J | Exactly these facts, without a uniform bound |

OC implies WOC by choosing E in the restricted domain and taking the
deletion empty. The converse is not proved, and no equivalence between
either hypothesis and the high-mass target is claimed.

The U intersects K clause is retained. It makes the input nonvacuous:
positive return times to U have bounded gaps. To see this, the closure
of the nonnegative orbit of theta is K, as a compact subsemigroup is a
subgroup. For each x in K, some nonnegative j has x+j*theta in U.
Compactness selects finitely many such j whose open preimages cover K.
Their maximum bounds the waiting time from any positive n. Consequently
every sufficiently long positive interval meets the Bohr return set.
Its intersection with the thick J is therefore unbounded. We have not
replaced that intersection by a thick set; thickness is obtained only
after the finite corrections.

Nothing requires U to contain zero, theta to be irrational, K to equal
the entire torus, or the bases to be pairwise coprime. Different
representations selected as alternatives may share labels; the two
supports joined in each final representation are disjoint.

## 5. Exact progress and successor obligation

The proved candidate is the whole implication obligation-000037.
A later acceptance may close that bridge, but cannot close WOC
(obligation-000036), the unconditional high-mass theorem
(obligation-000035), its lower-mass complement (obligation-000038),
the root implication bridge (obligation-000039), or the original
objective (obligation-000001).

The object cost remains because progress is an implication. The
obligations cost remains because WOC has not been discharged.
There is no bound_quality or additional-axiom cost. This is an
explicit routine conditional corollary and exact input audit of
the accepted core and correction lemmas, not an optimality or
standalone publication claim.

No entry failure is asserted. The two admitted entry applications
have been used, taking the inherited account to its declared
twenty-four-move limit. That is a controller resource predicate,
not a native stall or a proof that WOC is false or inaccessible.

Proposed successor: a separately reviewed direct investigation whose
exact claim is WOC as stated in Section 1. Its method must come from
its own study and admissibility scan. The successor may use this
checkpoint as logical lineage once recorded. Admission and any
renewal require their own exact reviewed justification. No native
child or additional move is created by this proof file.
