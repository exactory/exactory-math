# Exact proposed critical-complement extension

Date: 2026-09-08. Version 2 admission specification.
Status: conjectured operation and proof obligations only. No entry was reserved
or executed to establish this document. No new source query or mathematical
process was run. The original twelve-attempt preflight cap is unchanged.

## Fixed input and state

Use exactly the D,B,A,R,V,k,F hypotheses of the candidate claim in ../problem.md.
Write M=max V, F_V for the V-labelled part of F, and

    C = sum_{d in V} d^k/(d-1) + sum_{(d,j) in F_V} d^j,
    g = ceil(C),
    P_V = {(d,j): d in V, j>=k, (d,j) not in F_V}.

These are proposed original-state constants, not quantities reset at a unit
boundary. A partial state consists of a finite increasing list of correction
labels of values q_1,...,q_r, its entire weight W=sum_i q_i, and the union E_R
of F_R with BOTH R supports of every previous signed unit. Initially r=0,
W=0 and E_R=F_R. The V cutoff and C,g never change.

The construction is to establish a computable integer Q_0(V)>=16M depending
only on the finite set V. Its existence and the required bound are unproved
obligations of the proposed move. Q_0 is a single constant for the whole
construction. It must not depend on k,F,W,c,t or the final seed support.

## One fixed tolerance, not a menu of possible rules

For every integer q>=2 define the integers

    h(q) = max{h>=0: 2^h<=q},
    s(q) = max{s>=0: 2^(s^2)<=h(q)+2},
    epsilon(q) = 2^(-s(q)).

Thus this proposed tolerance is specified entirely by integer comparisons.
No logarithm evaluation or mathematical process is being executed here.

Let c be the least member of V coprime to the prime radix B. CP27's elementary
radix restriction supplies B in {2,3} and existence of such c in the present
common-radix scope. A new proof must also justify that this c has a
multiplicatively independent mate in V from the candidate's stated pair
assumption; that compatibility is not added as a new hypothesis.

Given the current finite E_R, take a fresh R cutoff and aligned lattice
modulus m=B^L as in the inherited signed-lattice construction. Let t be the
least positive integer with c^t congruent to 1 modulo m.

## Exact candidate predicate and operation

For a positive integer u and integers n_d>=k, d in V, put q=c^(tu) and
a_d=d^(n_d). The proposed eligibility predicate is the conjunction

    (c,tu) belongs to P_V,
    q > Q_0(V) + (C+W+1)^2,
    epsilon(q) <= 1/(100M),
    n_c = tu,
    (1-epsilon(q))q <= a_d <= (1+epsilon(q))q  for every d in V,
    a_d < q for at least one d in V other than c.          (E)

The last condition is fixed: at least one other anchor is strictly BELOW q.
There is no alternative unstated weighted condition in version 2.

Once the obligations below have been proved, the operation is to choose the
least positive u satisfying (E), using a fixed order on any anchor witnesses,
represent 1-q by the fresh signed R lattice, adjoin the one positive V label
q, and update W to W+q and E_R by BOTH new R supports. Only q is removed from
P_V. The operation is not asserted to terminate before those proofs.

## Precise preservation assertion to test

(P) For every finite V of distinct integers at least 4 with sigma(V)=1,
a multiplicatively independent pair, and H_V(x)>x for all real x>1, there
exists a computable integer Q_0(V)>=16M such that the following holds.
For every k>=1, finite F_V and every finite list of distinct corrections
generated with predicate (E), where the correction base can be any member
of V and no modular condition is needed for this assertion, the actual
remaining supply U satisfies

    sum_{ell in U, value(ell)<x} value(ell) >= x-C
    for every real x>0.                                  (P)

The sum is a strict prefix and counts coincident labels separately.
All corrections whose value is below x must be paid from the one cumulative
ledger; at a scale equal to a removed value, the strict-prefix convention
must be checked directly. The assertion requires one Q_0 and C for the
whole list. Its fixed-gap consequence and the legal g-1-unit amplification
are also required before any completeness conclusion.

The near-correction, normalized intermediate and remote-tail estimates are
parts of this precise assertion, not three extra assumptions. In particular,
the below-q anchor and the displayed epsilon must actually suffice at the
near scale. The proposed square growth is a hypothesis to test, not a bound
derived in this specification.

## Precise recurrence assertion to test

(R) For every finite V as in (P), every c in V having a multiplicatively
independent mate in V, every integer t>=1, every integer k>=1 and every
real T>0, there are a positive integer u and integers n_d>=k such that,
with q=c^(tu) and a_d=d^(n_d),

    q>T,
    epsilon(q)<=1/(100M),
    n_c=tu,
    (1-epsilon(q))q <= a_d <= (1+epsilon(q))q for every d in V,
    a_d<q for at least one d in V other than c.            (R)

This is recurrence on the ACTUAL exponent-multiple vector
(t log(c)/log(d))_{d in V}, with the exact height-dependent tolerance above
and a prescribed nonempty below-q sign. It is not full-torus density,
intersection of two syndetic sets, or Dirichlet's unsigned estimate alone.
Taking T above Q_0(V)+(C+W+1)^2 and the finitely excluded correction values
would yield the next legal candidate only AFTER (R) and (P) are proved.

The selected two-logarithm and simultaneous Dirichlet statements are
prospective inputs for (P) and (R). Their conversion and the sign condition
require original arguments inside a reserved move. No such argument is
claimed in this specification.

## Bounded entry order and stopping test

The proposed strategy has at most two computer-free step3 applications.
The first must establish the amplification and preservation law before
asserting a seed, then test (R), the coprime-c compatibility, the full global
ledger and the useful-domain requirement. If it returns only a precise
partial obligation, journal that result without a closing flag and obey
the controller's fresh reassessment before a possible second application.
A demonstrated failure of (E), (P) or (R) ends the strategy immediately.
If a required assertion remains unproved after the second application,
record exactly that unresolved assertion and end this route as inconclusive;
do not take a third application, assert a counterexample to completeness,
or silently change epsilon, sign, growth or claim to obtain a success.

This is an exact-operation revision of the same candidate claim. Altering
one of these substantive rules after admission requires the corresponding
updated studies, plans and review, and a separately reviewed claim when
the mathematical scope changes. A proof of an auxiliary assertion alone
does not receive a separate checkpoint or renew an account. A useful
effective H_V test or genuinely new explicit critical input remains part
of the proposal's substance requirement; the universal automatic-margin
question remains a distinct future research claim.
