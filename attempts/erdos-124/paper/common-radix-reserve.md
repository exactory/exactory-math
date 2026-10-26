# Common-radix seeds and a disjoint positive reserve

## Exact claim and notation

For every nonempty finite set D of distinct integers at least 3 with gcd(D)=1
for which there exist an integer B>=2, a nonempty finite set A of positive
integers and a nonempty set C contained in D minus R, where
R={B^a:a in A} is contained in D, such that
sigma(R)=sum_{d in R}1/(d-1)>=1/2, gcd({B} union C)=1 and
sigma(D minus (R union C))>=1, every integer k>=1 and every finite set F of
labelled occurrences (d,j) with d in D and j>=k admit N(D,k,F) such that every
integer n>=N is a sum of finitely many remaining occurrences d^j, each pair
(d,j) used at most once; coincident numerical values from different pairs
remain separately available.

Write U=D minus (R union C). For a supply of labels T, let FS_0(T) be the
set of its finite subset sums, including zero. A signed representation uses
coefficients in {-1,0,1}, one coefficient for each label. Disjointness always
means disjoint labels, not different numerical values.

An integer set is g-syndetic on the nonnegative integers when it meets
every interval of g consecutive nonnegative integers. All intervals below
that describe representable integers include their integer endpoints.

## 1. Amplification with a reserve fixed in advance

Let T and V be disjoint supplies of positive integer labels. Suppose
FS_0(V) is g-syndetic for an integer g>=1, and that outside every finite
forbidden subset of T there are finite disjoint P,Q with

    value(Q)-value(P)=1.

Choose r such pairs successively, requiring each new pair to avoid BOTH
supports from all preceding pairs. Each forbidden set is finite. Put
H=sum_{i=1}^r value(P_i). Switching the first t pairs from P_i to Q_i
represents H+t for every integer 0<=t<=r. All representations are legal,
since the supports of different pairs are disjoint. The zero-pair case is
H=0 and the represented singleton {0}. Each additional pair increases
the represented interval length by one, without changing any reserve label.

Choose r=g-1. For every n>=H+g-1 the interval

    [n-H-g+1, n-H]

consists of g nonnegative integers. It contains some v in FS_0(V).
Then n-v belongs to [H,H+g-1] and is represented on T. The two supports
are disjoint, so their union represents n on T union V.

This proves the amplification and its preservation law first. Its smallest
positive seed increment is one unit pair. No search can produce a smaller
positive integer increment. The argument requires g to be fixed before
constructing the pairs. It does not infer completeness from signed units
alone, and does not consume any reserve labels to create the seed.

## 2. Signed-prefix interval induction

Let w_1,...,w_s be positive integer labelled weights, with
W_i=sum_{j=1}^i w_j and W_0=0. If

    w_i <= 2W_{i-1}+1

for every i, their signed sums fill [-W_s,W_s].
Indeed, from the preceding interval [-W,W], the next label of value w
gives the three integer intervals

    [-W-w,W-w], [-W,W], [w-W,w+W].

The inequality makes consecutive intervals overlap or meet at adjacent
integers. Their union is [-W-w,W+w]. The induction begins with {0};
each step uses its new label at most once. Equal numerical weights cause
no difficulty when their labels are distinct.

## 3. The aligned common-radix lattice

Fix a positive integer K. Choose a positive common multiple L of every
a in A large enough that L>=aK for all a. Such L exists because A is
finite. For every a in A and integer t>=0 use the original label

    (B^a, L/a+t),

whose value is B^L times the normalized weight B^(at), and whose exponent
is at least K. Different a give different bases. For a fixed a, different
t give different exponents. Thus this map from normalized to original
labels is injective.

Order all normalized weights by value, retaining every label. This is an
infinite locally finite list. At level zero there is one weight1 for each
a in A. At any integer level r>=1 having a weight B^r, the sum of the
weights strictly below it is

    W(r) = sum_{a in A} (B^(a ceil(r/a))-1)/(B^a-1)
         >= (B^r-1) sigma(R)
         >= (B^r-1)/2.

For each a the terms counted are t=0,...,ceil(r/a)-1; this proves the
equality also when a divides r. Since a ceil(r/a)>=r, the first inequality
holds term by term. The mass hypothesis gives the second.

The first weight1 satisfies Section2 with preceding sum0, and later copies
of1 also satisfy it. At a positive level, B^r<=2W(r)+1, so the first label
at that level satisfies the same condition. Each subsequent label of equal
value has a larger preceding sum. Section2 therefore proves that each
finite normalized prefix fills its complete signed interval. Its endpoint
sums tend to infinity, so every integer has a finite signed representation.

Restoring B^L, the R labels with original exponents at least K represent
every multiple of B^L by a finite legal signed sum. This is an exact
integer lattice statement, not an approximation, congruence statement,
or assertion about an infinite sum.

## 4. Collective modular correction on different labels

Let h=B^L. We prove that C labels with exponents at least K have a positive
finite subset sum z congruent to1 modulo h.

For any c in C, multiplication by c maps the finite set of residues
modulo h to itself. The orbit c^j modulo h is eventually periodic, with
its transient finished by index h. Choose J>=max(K,h). Then c^J modulo h
occurs at arbitrarily large exponents for each c.

The integers h and all c^J, c in C, have gcd one. A prime dividing h
divides B, and if it also divided every c^J it would divide every c,
contrary to gcd({B} union C)=1. Bezout's identity consequently gives an
integer combination of the c^J congruent to1 modulo h. Replace each
coefficient by its residue in {0,...,h-1}. For each resulting copy choose
a different sufficiently late exponent where that base has residue c^J.
There are infinitely many such exponents, so the finite choices exist.
Their positive sum z has the required residue. Different bases or
different chosen exponents mean different labels.

Now q=(1-z)/h is an integer. Section3 represents hq=1-z on R labels
above K by a finite signed sum. Add the positive C representation of z.
The base sets R and C are disjoint, so no label is used twice.
The combined signed sum is exactly1. Let Q be its positive labels
and P its negative labels. They are finite, disjoint, and satisfy

    value(Q)-value(P)=1.

For any prescribed finite forbidden label set, first choose K above
every exponent occurring in that set and at least the desired cutoff.
The entire construction avoids that set. In particular it supplies the
fresh pairs required in Section1. It uses only R union C and no U label.

## 5. A fixed-gap lemma for positive subset sums

Let a_1,a_2,... be the nondecreasing values of an infinite locally finite
labelled supply of positive integers, with S_i=sum_{j=1}^i a_j.
Suppose a_i-S_{i-1}<=g for all i, for a fixed integer g>=1.
Then its finite subset sums are g-syndetic on the nonnegative integers.

For each finite prefix its subset sums have endpoints0,S_i and every
gap between consecutive values is at most g. Prove this by induction.
The empty prefix has no gap. If the preceding subset set is V with span
[0,S], adjoining a gives V union (a+V). Within either translated span,
any gap of the union is bounded by a gap of the corresponding copy of V.
More explicitly, a gap whose interior meets one span cannot contain its
endpoints, since those endpoints belong to the union; consecutive points
of that copy surrounding an interior point bound the gap. If the two
spans are disjoint, the only additional gap is a-S<=g. If they overlap,
their union is the full span and there is no additional gap. The case
V={0} gives the first gap a<=g directly.

The endpoint sums tend to infinity. If an interval of g nonnegative
integers contained no finite subset sum, choose a prefix whose endpoint
exceeds its upper endpoint. The interval cannot contain0. It would lie
between two consecutive prefix sums separated by at least g+1, a
contradiction. This proves the assertion with the specified endpoint
convention.

## 6. The mass-one reserve gives a gap independent of all later gadgets

Use the labels on U with exponents at least k and remove F_U, the part
of F on those bases. This supply is infinite and locally finite because
sigma(U)>=1 implies U is nonempty. Define

    M = sum_{d in U} d^k/(d-1) + sum_{(d,j) in F_U} d^j,
    g = ceil(M).

These depend only on the chosen U,k,F_U. They are positive, with g>=1.

For x>0 and any d in U,

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1).

If x<=d^k, the left side is zero and the right side is nonpositive.
Otherwise let s>=k be the least index with d^s>=x. The sum on the
left is (d^s-d^k)/(d-1), proving the inequality, including exact-power
endpoints. Subtracting the values of all deleted labels only weakens
the resulting lower bound, so

    sum_{remaining U labels of value<x} value >= sigma(U)x-M.

In the ordered remaining supply, all strictly smaller values precede
a label of value a_i=x. Earlier equal values can only increase its
preceding sum. Hence

    a_i-S_{i-1} <= (1-sigma(U))a_i+M <= M <= g.

Section5 gives the required g-syndetic reserve. No gcd condition on U
is needed, and equality sigma(U)=1 is included. This fixed g is chosen
before any pairs are constructed and remains valid because those pairs
use different base labels.

## 7. Completion for the exact quantified input

Fix D,k,F in the claim and choose any witnessing B,A,C; set U as above.
These choices precede the represented integer n. Compute the fixed integer
g from Section6. The remaining labels on R union C have the fresh-unit
property of Section4 after every additional finite deletion. Section1
therefore constructs g-1 pairs using no reserve labels and an integer
H>=0 such that [H,H+g-1] is positively represented on R union C.

Section1, with the unchanged reserve on U, represents every
n>=H+g-1. Take N(D,k,F)=max{1,H+g-1}. All final supports are finite,
all original exponents are at least k, all labels avoid F, and every
label is used at most once. Numerical coincidences across the disjoint
base sets remain separately available, exactly as the claim requires.

This proves the complete admitted structural claim. It does not prove
the original all-D reciprocal-mass-one objective.

## 8. Scope, a genuinely additional range, and limits

For the binary family R={4,8,32},

    sigma(R)=1/3+1/7+1/31=331/651>1/2.

Thus any D containing these three bases and a disjoint correcting odd
base, with mass at least1 remaining after removing those four bases,
satisfies the theorem. In particular the theorem does not require16.

This gives inputs outside every earlier accepted positive range. To
see existence without a finite search, take the correction base5.
Let U_M be the integers from6 through M excluding8,16 and32.
Their reciprocal mass diverges as M grows, because removing finitely
many terms from the harmonic series preserves divergence. For
completeness, successive blocks of integers from2^t through2^(t+1)-1
each contribute at least1/2 to sum1/(d-1), which proves divergence.

Choose the least M with sigma(U_M)>=1. The preceding mass is less
than1, and each new term is at most1/5, so sigma(U_M)<6/5.
Set D={4,8,32,5} union U_M. Then min D=4, gcd(D)=1, 16 is absent, and

    1 < sigma(D) < 331/651+1/4+6/5
                 = 25499/13020 < 2.

The new theorem applies. The earlier minimum-three result does not,
the fixed4,8,16 theorem lacks16, and the minimum-four quarter-mass
threshold13/4 exceeds this input's mass. The theorem therefore has
an actual additional structural range, not just a different description
of an earlier accepted range.

There are no qualifying radix families at B>=4. Indeed

    sum_{a>=1} 1/(B^a-1)
      <= sum_{a>=1} 1/((B-1)B^(a-1))
       = B/(B-1)^2 <= 4/9 < 1/2.

For the penultimate inequality, (B-4)(4B-1)>=0. At B=3, omitting
the exponent1 leaves mass at most1/(3-1)^2=1/4, so3 must occur in R.
The substantive extension is consequently the variable binary exponent
family; no nonvacuous extension to every radix is asserted. Since the
viable radices2 and3 are prime, their collective correction condition
already supplies an individual base coprime to the radix. No separate
new collective-coprimality phenomenon is claimed.

The argument requires both a common-radix half-mass seed and a disjoint
mass-one reserve. It proves no necessity for either condition and makes
no assertion for an arbitrary half-mass gcd-one family lacking that seed.
Support sizes, modular periods and the final threshold need not be
uniformly small. The g-1 pair recipe uses the smallest positive increment;
no globally optimal support bound or algorithmic efficiency is claimed.

## 9. Dependencies and author checks

Every mathematical ingredient used in the conclusion is proved above
by finite arithmetic, finite-state periodicity and induction. The earlier
signed-weight source and local accepted examples are context and comparison,
not external theorem or accepted-result dependencies of this self-contained
proof. The inherited checkpoint20 lattice is rederived in Sections2-4;
its pending status is not promoted by citation.

The author checked the equality boundaries, exact-power prefix endpoints,
zero-pair case, arbitrary positive cutoffs and finite deletions, injectivity
of the normalized-label map, finite recurrence choices, both signs of the
lattice coefficient, the ordering of the fixed reserve gap before gadgets,
and the strict extra-range comparison. No failure signal fired.
Independent review is still required before acceptance. The root, the
arbitrary-base half-mass claim, complementary ranges and implication
bridges remain open.
