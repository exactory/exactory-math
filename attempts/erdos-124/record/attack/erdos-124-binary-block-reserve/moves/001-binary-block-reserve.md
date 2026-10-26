# Move 1: a signed binary block and an independent reserve

Node: node-000013. Strategy: make-the-proof-constructive.
Entry: seed-and-amplify. Reservation: controller revision 243.
Status: self-contained analytical proof candidate, pending independent review.
No mathematical program, enumeration, or formal checker was run.

## Exact admitted claim and notation

For every nonempty finite set D of distinct integers at least 4 with
min D=4, {8,16} contained in D, gcd(D)=1 and
sigma(D)=sum_{d in D}1/(d-1)>=251/140, every integer k>=1 and every
finite set F of labelled occurrences (d,j) with d in D and j>=k, all
sufficiently large integers are sums of finitely many remaining
occurrences d^j, each pair (d,j) used at most once; coincident numerical
values from different pairs remain separately available.

A supply is a locally finite set of labels carrying positive integer
values. FS_0 denotes its finite subset sums, including zero. A signed
sum assigns each used label a coefficient in {-1,0,1}. Equal values
can belong to different labels. Disjointness concerns labels, never
merely numerical values. A set is g-syndetic on the nonnegative
integers if it meets every interval of g consecutive such integers.

## 1. The fixed-reserve amplification and its seed parameter

Let T and R be disjoint supplies, let FS_0(R) be g-syndetic, and
suppose FS_0(T) contains [A,A+g-1] with A>=0. For n>=A+g-1 the
interval [n-A-g+1,n-A] consists of g nonnegative integers. Choose
there a reserve sum r. Then n-r lies in [A,A+g-1], and its finite
representation on T combines with the representation of r on R.
Thus every such n is represented on T union R.

The required seed parameter is g consecutive sums, with g fixed from
the independent reserve before building the seed. The gap information
alone does not guarantee this conclusion from g-1 consecutive sums:
for g>=2, a reserve with values g,2g,4g,... has subset sums g*N_0,
and a seed [0,g-2] misses residue g-1 even after adding that reserve.
This is not an optimality assertion about a specific power supply.

Suppose that, outside every finite forbidden label set, T supplies
finite disjoint alternatives P,Q with value(Q)-value(P)=1. For each
integer r>=0 choose r such pairs, requiring each new pair to avoid
the union of BOTH alternatives of all preceding pairs. Every forbidden
set in this finite recursion is finite. Let A=sum_i value(P_i).
Switching the first t pairs to Q_i represents A+t for 0<=t<=r,
because the supports of different pairs are disjoint. For r=0 this
is the empty sum and interval [0,0]. Therefore g-1 pairs give the
seed required above. The smallest positive motif is one unit pair;
each pair increases the number of consecutive sums by exactly one.
No assertion that signed units or thickness alone imply completeness
has been used.

## 2. A finite signed-interval lemma

Let w_1,...,w_s be a finite list of positive integer labelled weights,
and S_i=sum_{j=1}^i w_j, with S_0=0. If

    w_i <= 2*S_{i-1}+1

for every i, then signed sums on these labels contain every integer
in [-S_s,S_s]. This permits repeated numerical weights with different
labels.

Induct on i. The empty prefix represents {0}. If the preceding
prefix represents [-S,S], adding the next label with coefficient
-1,0 or1 gives the three integer intervals

    [-S-w,S-w], [-S,S], [w-S,w+S].

The displayed inequality makes consecutive intervals overlap or
touch at consecutive integers. Their union is [-S-w,S+w]. Each
representation uses the new label at most once, so the induction
proves the assertion with the exact coefficient restriction.

## 3. The actual block on bases 4, 8 and 16

Use binary exponents and a half-open block of exponents [0,12).
The base4 occurrences correspond to offsets0,2,4,6,8,10; base8 to
offsets0,3,6,9; and base16 to offsets0,4,8. For now these are
normalized weights; the actual positive exponent labels are assigned
in Section 5. The normalized labelled list, ordered by weight, is

    1,1,1,4,8,16,16,64,64,256,256,512,1024.

The following exact table verifies the condition of Section 2. A row
with multiplicity greater than one checks the first copy; every later
copy has a larger preceding sum and so satisfies the same inequality.

| Weight | Multiplicity | Preceding sum | Twice preceding sum plus one | Sum after the row |
| --- | --- | --- | --- | --- |
| 1 | 3 | 0 | 1 | 3 |
| 4 | 1 | 3 | 7 | 7 |
| 8 | 1 | 7 | 15 | 15 |
| 16 | 2 | 15 | 31 | 47 |
| 64 | 2 | 47 | 95 | 175 |
| 256 | 2 | 175 | 351 | 687 |
| 512 | 1 | 687 | 1375 | 1199 |
| 1024 | 1 | 1199 | 2399 | 2223 |

Thus this exact labelled block represents every signed integer in
[-2223,2223]. In particular it represents every member of

    E={-2048,-2047,...,2047},

a set of 4096 consecutive integers, using each block label once at
most. No coefficient larger than one is assigned to an individual
label. The three copies of weight1 and the other multiplicities come
from different base labels, not from repeated use of a pair.

## 4. Finite repeated-block expansions

Every nonnegative integer q has a finite expansion

    q = sum_{t>=0} delta_t*4096^t,  delta_t in E.

For q=0 use all zero digits. For q>=1 choose the unique delta in E
congruent to q modulo4096, and let q'=(q-delta)/4096. This integer
is nonnegative. If q<=2047 then delta=q and q'=0. If q>=2048 then
q-delta>=q-2047>0. Also

    q' <= (q+2048)/4096 < q,

since 2048<4095*q for every q>=1. Strong induction on q now gives
the finite expansion, with delta in the units position and the
expansion of q' shifted one block. This proves termination and not
merely congruence coverage. Negating the digits gives the analogous
existence statement for negative integers if needed; the digit set
for that negated expansion remains within [-2223,2223]. The unit
construction below uses only positive q and the stated set E.

For each of the finitely many nonzero digits choose its signed
representation on the normalized block from Section 3, and multiply
that block by4096^t. Different t use different blocks. Section 5
supplies actual labels and checks that this repetition is legal at
any required depth.

## 5. Exact original exponents and the tail unit

Fix an integer K>=1 and an odd integer b>=5. Choose a positive
multiple L of12 with L>=4K. For t>=0, e in {2,3,4}, and an offset
r with 0<=r<12 and e dividing r, assign the normalized block weight
2^r at position t to the actual label

    (2^e, (L+12t+r)/e).

Its exponent is an integer because e divides L,12 and r. It is at
least L/e>=K. Its value is 2^L*4096^t*2^r, as required. Different
e mean different bases. For fixed e, two different pairs (t,r) cannot
give the same label: their binary exponents occupy disjoint half-open
blocks [L+12t,L+12(t+1)). This also accounts for every boundary
offset0 without overlap. Hence every signed expansion in Section 4
gives a finite legal signed representation of 2^L*q on bases4,8,16,
with all original exponents at least K.

Because b is odd, it is invertible modulo2^L. Repetition of its powers
in that finite residue system, followed by cancellation, gives a
positive h with b^h congruent to one modulo2^L. Choose a positive
multiple J of h with J>=K. Then

    q=(b^J-1)/2^L

is a positive integer. Sections 3-5 represent b^J-1 as a finite
signed sum of the permitted labels on4,8,16. Let P be the labels
with positive coefficient, and let Q consist of (b,J) together with
the labels with negative coefficient. We obtain

    value(Q)-value(P)=1.

Both P and Q are finite and disjoint. The odd base b is different
from4,8,16. Each underlying label has coefficient at most one in
absolute value, so signs split it into at most one alternative.
Since b^J-1>0, P is nonempty; Q contains (b,J). Every original
exponent on both sides is at least K.

Given any fixed positive cutoff k and any finite forbidden label set
H on {4,8,16,b}, choose K>=k larger than every original exponent
in H. The construction avoids H. Repeating this choice with H also
containing both alternatives from all preceding pairs supplies the
fresh unit property in Section 1 at every positive cutoff and after
every finite deletion. Each recursion is finite when a finite number
of pairs is requested. The sizes of L,J and the support need not
remain uniformly bounded.

## 6. A self-contained syndetic-reserve lemma

Let a_1,a_2,... be the nondecreasing values of an infinite locally
finite labelled supply of positive integers, retaining ties, and put
S_i=sum_{j=1}^i a_j. If a_i-S_{i-1}<=g for all i with integer g>=1,
its finite subset sums are g-syndetic on the nonnegative integers.

For a finite prefix, its subset sums have endpoints0,S_i and gaps
at most g. This follows by induction: from a preceding set U one
forms U union (a_i+U). Inside either closed span the preceding mesh
bound applies. If the spans are disjoint their intervening gap is
a_i-S_{i-1}<=g. If they overlap, any putative larger gap either
lies inside a span or contains a span endpoint belonging to the union,
both impossible. The first prefix has a_1<=g. The endpoints tend
to infinity. An interval of g nonnegative integers missing all sums
would either contain endpoint0 or force a finite-prefix gap of at
least g+1 once the prefix extends beyond that interval. This proves
the assertion, including the endpoints.

Now let B be a finite set of bases at least4 with sigma(B)>=1.
For any k>=1 and finite deletion F_B define

    C_B=sum_{d in B} d^k/(d-1)+sum_{(d,j) in F_B}d^j,
    g=ceil(C_B).

This is a positive integer g, since B is nonempty. For x>0 and
each d in B, the strict numerical prefix satisfies

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1).

When x<=d^k this is immediate. Otherwise the least r>=k with
d^r>=x gives the geometric sum (d^r-d^k)/(d-1), which proves the
bound, including exact-power endpoints. Subtracting all deleted
values and summing over B gives

    sum_{remaining labels with value<x}value >= sigma(B)*x-C_B.

All strictly smaller labels precede a label of value a_i=x. Earlier
equal values can only increase its preceding sum. Therefore

    a_i-S_{i-1} <= (1-sigma(B))*a_i+C_B <= C_B <= g.

The preceding mesh lemma applies to the remaining reserve. It is
infinite and locally finite, has g-syndetic subset sums, and requires
no gcd-one assumption. All numerical ties and finite deletions have
been retained. In particular the result holds at sigma(B)=1, and
g depends only on B,k,F_B.

## 7. The exact minimum-four structural range

Fix D,k,F from the claim. Since4 belongs to D and gcd(D)=1, D
contains an odd base b. It is at least5 and different from4,8,16.
For B=D minus {4,8,16,b}, the exact mass calculation is

    sigma({4,8,16}) = 1/3+1/7+1/15 = 19/35,
    sigma(B) >= 251/140-19/35-1/4 = 1.

Thus B is nonempty. Let R be its remaining labels with cutoff k
and its part of F removed. Fix the integer gap g from Section 6.
Let T be the remaining labels on {4,8,16,b}. By Section 5 and the
finite fresh-pair iteration in Section 1, T represents some interval
[A,A+g-1]. This uses only g-1 pairs, and never uses any R label.
Consequently the previously fixed g remains valid even though the
seed values may be large. Section 1 represents every n>=A+g-1.
Take N(D,k,F)=max{1,A+g-1} to make the threshold positive if desired.

The choice of b,B,g, the pairs and A depends only on D,k,F and
precedes the choice of n. Every final representation is a union of
two disjoint finite subsets of the remaining labels. This proves
the exact admitted claim, with equality at251/140 included.

## 8. Seed size, dependencies and limits

The fixed signed block uses exactly the listed13 labels, and its
radix digits are chosen from a smaller interval than its full signed
range. No search for a larger block is needed. Choosing the largest
odd b in D maximizes the remaining reciprocal mass. One can choose
the first multiple of12 at least4K and the first sufficiently high
multiple J of a modular period; the finite digit recursion and
finite signed-interval induction specify terminating choices. The
fresh-pair recipe uses exactly g-1 pairs; its zero-pair case represents
only the singleton seed and suffices in that recipe when g=1.
No efficient or uniform bound on witness size is claimed.

The proof would also work under the direct structural condition
sigma(D minus {4,8,16,b})>=1 for some odd b>=5 in D. This is a
corollary of the same argument, not a changed admitted claim. Omitting
one of the three fixed bases may change the signed alphabet, so no
conclusion for arbitrary minimum-four D follows. Removing numerical
duplicates would also change the alphabet and is not justified.
If the independent reserve has mass below one, this proof supplies
no bounded gap; it proves no impossibility result in that range.

All mathematical ingredients were proved in Sections1-7. The
classical signed-weight context and accepted predecessor are recorded
in the studies, but no external theorem, prior acceptance or
mathematical execution is a proof dependency. No formal proof or
publication-priority claim is made. The full original threshold-one
objective, the other base configurations and its separate implication
bridge remain open.
