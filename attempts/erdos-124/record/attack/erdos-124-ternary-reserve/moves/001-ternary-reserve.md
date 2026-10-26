# Move 1: a ternary seed and a disjoint reserve

Node: node-000012. Strategy: make-the-proof-constructive.
Entry: seed-and-amplify. Reservation: controller revision 226.
Status: self-contained analytical proof candidate, pending independent review.
No mathematical program, finite enumeration, or formal checker was run.

## Exact admitted claim

For every nonempty finite set D of distinct integers at least 3 with
min D=3, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=11/6, every
integer k>=1 and every finite set F of labelled occurrences (d,j) with
d in D and j>=k, all sufficiently large integers are sums of finitely
many remaining occurrences d^j, each pair (d,j) used at most once;
coincident numerical values from different pairs remain separately
available.

A supply is a locally finite set of labels, each with a positive integer
value. FS_0 of a supply is the set of sums on its finite subsets,
including the empty sum. Disjointness always means disjoint LABELS.
For a positive integer g, a subset of the nonnegative integers is
g-syndetic if it meets every interval of g consecutive nonnegative
integers. It is thick if it contains intervals of every finite length.

## 1. Amplification with a fixed independent reserve

Let T and R be disjoint supplies. Suppose FS_0(R) is g-syndetic and
FS_0(T) contains [A,A+g-1] for some integer A>=0. Then FS_0(T union R)
contains every integer n>=A+g-1.

Indeed, [n-A-g+1,n-A] consists of g nonnegative integers, so it contains
an element r of FS_0(R). The integer n-r lies in [A,A+g-1]. A finite
representation of n-r on T and a finite representation of r on R have
disjoint labels, and their union represents n.

The finite seed required by this lemma has g consecutive sums. From
this gap information alone, g-1 sums would not suffice in general:
for g>=2, R-values having subset sums g*N_0 and the seed [0,g-2]
miss a residue class. No minimality for an individual power supply is
asserted. We fix g before constructing the seed, and never consume R
while constructing it.

## 2. Unit alternatives produce intervals

Suppose a supply T has the following tail property: for every finite
set H of forbidden labels, it contains finite disjoint sets P,Q outside
H with value(Q)-value(P)=1. Here value denotes the sum of label values.
Then FS_0(T) is thick. More precisely, for every integer r>=0 there
are pairwise disjoint supports P_i union Q_i, 1<=i<=r, whose choices
represent an interval of r+1 consecutive integers.

For r=0 the empty representation gives [0,0]. Otherwise apply the
property repeatedly, forbidding the union of BOTH alternatives from
every earlier pair. This is a finite forbidden set at each stage.
Write A=sum_i value(P_i). For each t in {0,...,r}, choose Q_i on
the first t pairs and P_i on all other pairs. Their union is a legal
finite support and its value is A+t. Thus [A,A+r] is represented.
Each additional pair increases the number of consecutive sums by
exactly one, irrespective of the size of its values or support.

The seed motif is one pair with unit difference. The constraints
preserved under iteration are finiteness and non-reuse of labels.
This argument does not assert that thickness alone gives completeness.
Section 1 requires an additional disjoint syndetic reserve.

## 3. The exact ternary tail unit

Fix an integer b>=4 with gcd(b,3)=1. For every integer K>=1 there
exist disjoint finite sets P,Q of labels with bases in {3,b} and
exponents at least K such that value(Q)-value(P)=1.

First, every nonnegative integer q has a finite balanced ternary
expansion q=sum_{i>=0} epsilon_i*3^i with epsilon_i in {-1,0,1}.
Here is a proof. For q=0 use no nonzero digits. For q>=1 choose the
unique epsilon in {-1,0,1} congruent to q modulo 3 and put
q'=(q-epsilon)/3. This is a nonnegative integer and q'<q: it is at
most (q+1)/3<q for q>=1. By strong induction expand q', shift its
digits up one place, and use epsilon at place zero. This gives the
required finite expansion. Uniqueness is not needed.

There are finitely many residue classes modulo 3^K. Two among the
powers b^0,b^1,... are equal modulo 3^K. Since b is invertible
modulo 3^K, cancellation gives an integer h>=1 with b^h=1 modulo
3^K. Choose any positive multiple J of h with J>=K. Then

    q=(b^J-1)/3^K

is a positive integer. Apply the preceding balanced ternary expansion
to q and multiply by 3^K. It gives

    b^J - sum_i epsilon_i*3^(K+i) = 1.

Let P contain the labels (3,K+i) with epsilon_i=1. Let Q contain
(b,J) and the labels (3,K+i) with epsilon_i=-1. The digit expansion
is finitely supported, so these sets are finite. Every exponent is
at least K. The ternary labels in P and Q are disjoint because their
digits have different signs, and the b label has a different base.
Both alternatives are nonempty: Q contains (b,J), and q>0 ensures
at least one positive digit, hence P is nonempty. The displayed
identity says exactly value(Q)-value(P)=1. Each coefficient in
each positive alternative is one; no occurrence is repeated.

Now fix any positive cutoff k and any finite forbidden label set H
on these bases. Choose K>=k larger than every exponent appearing
in H (with no additional constraint if H is empty). The construction
avoids H. Repeating it with K beyond the exponents in the union of
all earlier alternatives gives exactly the hypothesis and iteration
of Section 2. Consequently, the remaining supply on {3,b} is thick
after every positive cutoff and finite deletion.

## 4. A self-contained bounded-gap lemma

Let a_1,a_2,... be a nondecreasing infinite list of positive integer
label values, with ties kept and ordered in any fixed way. Put S_0=0
and S_i=sum_{j=1}^i a_j. Suppose a_i-S_{i-1}<=g for all i, where
g is a positive integer. Then FS_0 of this labelled supply is
g-syndetic.

To prove this, the finite-prefix subset-sum set has endpoints 0,S_i,
and consecutive numerical gaps at most g. Induct on i. The assertion
for i=1 follows from a_1<=g. At the induction step, the new set is
U union (a_i+U), where U is the preceding subset-sum set. Each copy
has gaps at most g inside its span. If the two spans are disjoint,
the intervening gap is a_i-S_{i-1}<=g. If they overlap, a gap in
the union either lies in the span of a copy, whose mesh bounds it,
or would contain a span endpoint belonging to the union and so would
not be a gap. The mesh bound follows. The initial empty-prefix case
can alternatively start the same induction with the singleton {0}.

The prefix endpoints tend to infinity. Given [u,u+g-1] with u>=0,
choose a prefix with endpoint at least u+g-1. If the interval missed
all subset sums, then either it contained endpoint 0, a contradiction,
or consecutive subset sums on either side would differ by at least
g+1, contradicting the mesh bound. This proves the lemma.

## 5. A geometric reserve at reciprocal mass one

Let B be a finite set of integer bases at least 3 with sigma(B)>=1.
Fix k>=1 and a finite deletion F_B of its labels with exponents at
least k. List the remaining values in increasing order, keeping ties.
This supply is infinite and locally finite. Define

    C_B = sum_{d in B} d^k/(d-1) + sum_{(d,j) in F_B} d^j,
    g = ceil(C_B).

The set B is nonempty, and C_B>0, so g is a positive integer. We show
that the ordered deficit at every remaining label is at most C_B.

For any real x>0 and d in B,

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1).

If x<=d^k this is immediate. Otherwise take the least r>=k with
d^r>=x. The sum is (d^r-d^k)/(d-1), which is at least the stated
quantity, also when x is exactly a power. Summing over B and
subtracting the total value of every deleted label gives

    sum_{remaining labels with value<x} value
        >= sigma(B)*x-C_B.

Every such strictly smaller label precedes a label of value a_i=x,
even in the presence of ties. Therefore

    a_i-S_{i-1} <= (1-sigma(B))*a_i+C_B <= C_B <= g.

Section 4 proves g-syndeticity. Equality sigma(B)=1 is permitted.
No gcd-one hypothesis on B is used. Deletions, coincident numerical
values, and every positive k were included explicitly. This g depends
only on B,k,F_B, not on any seed supported on different bases.

## 6. The admitted minimum-three theorem

Fix D,k,F as in the exact claim. Since 3 belongs to D and gcd(D)=1,
some b in D is not divisible by 3. Such b is at least 4 and coprime
to 3. Set B=D minus {3,b}. Its reciprocal mass satisfies

    sigma(B) = sigma(D)-1/2-1/(b-1)
             >= 11/6-1/2-1/3
             = 1.

Let R be the remaining supply on B, and T the remaining supply on
{3,b}, in each case with cutoff k and the corresponding part of F
deleted. The base sets are disjoint, so the supplies are disjoint
by label, whether or not values from distinct labels coincide.

Use Section 5 to fix g for R. Sections 2 and 3 provide an interval
[A,A+g-1] of sums on T by making g-1 fresh unit pairs. Their supports
are finite and avoid F. No label of R is used in constructing this
interval, so the previously fixed gap g is still valid. Section 1
now represents every n>=A+g-1 on the original remaining supply.
For a positive threshold one may take N=max{1,A+g-1}.

All choices depend only on D,k,F, and are made before n is chosen.
This proves the exact admitted claim, including its inclusive boundary.

## 7. Construction size, dependencies, and remaining scope

For a chosen b, the argument only requires sigma(D minus {3,b})>=1.
Choosing the largest b in D coprime to 3 maximizes that reserve mass.
For each unit pair one may use the first admissible multiple J of a
period h and the balanced-digit recursion above. The first g-1 pairs
suffice. Their values can be extremely large. No efficiency, uniform
bound on N, optimal threshold, or executed computation is claimed.

These observations perform the entry's seed-size and seed-class check:
zero pairs are sufficient only when g=1; each further pair supplies
one interval increment. This construction uses the digit alphabet
{-1,0,1} and hence does not extend verbatim to a larger minimum base.
When the independent reserve has mass below one, Section 5 supplies
no bounded deficit, so this proof gives no conclusion there. It does
not revive the refuted abstract inference from signed tail units alone.

Every mathematical ingredient used in Sections 1-6 was proved there.
The classical status of balanced ternary is recorded in study/problem.md
and novelty.md; no external result, accepted predecessor, formal build,
or mathematical execution is a proof dependency. Previous accepted
results serve as comparison and logical lineage only.

The original threshold-one objective remains open. This candidate
extends its minimum-three subrange only. It does not prove the region
1<=sigma(D)<11/6 at minimum three, nor any new region at larger minima.
The root's separate implication bridge and complementary obligations
remain unaccepted. The numerical change from 13/4 to 11/6 is not a
percentage of the complete original proof. Publication priority and
publication-unit novelty are not asserted.
