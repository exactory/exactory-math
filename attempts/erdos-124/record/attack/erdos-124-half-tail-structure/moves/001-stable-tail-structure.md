# Move 1: persistent signed-tail structure

Status: analytical move1 executed and journalled under reservation
move-node-000015-1, initially reserved at revision270. The lemmas below have
not received independent result review.
The admitted half-mass claim and the original Erdos 124 objective remain open.
No mathematical program has run.

## Definitions and the counterexample assumption

Fix a finite nonempty set E of distinct integers at least 3 with gcd(E)=1.
For K>=1, let T_K be the integers represented by finite signed sums of labels
(d,j), d in E, j>=K, with coefficients in {-1,0,1}. Labels with equal values
remain distinct. Write H=intersection_{K>=1} T_K.

A finite forbidden label set is avoided by increasing K beyond all of its
exponents. Thus the all-cutoff, finite-deletion unit assertion is equivalent
to 1 belonging to H. For the negative-side move, assume an admissible E
with sigma(E)>=1/2 fails that assertion. This is an assumption for analysis,
not a counterexample or a conclusion that the assertion is false.

## 1. Fresh supports make H a subgroup

Zero lies in H and negating a representation preserves its labels.
Given x,y in H and any K, represent x on a finite support above K.
Then represent y above every exponent in that support, also above K.
The supports are disjoint, so their union represents x+y legally above K.
Consequently H is an additive subgroup of Z.

If H is nonzero, let h be its least positive element. The division algorithm
shows H=hZ: for x in H, its remainder on division by h is in H and cannot
be strictly between 0 and h.

## 2. Every tail has positive subset representatives modulo every h>=1

For h=1 this is immediate. For general h, the residues d^j modulo h are
eventually periodic, since multiplication by d is a map of the finite residue
set. In particular, for a common J>=max(K,h), each residue d^J occurs at
arbitrarily high exponents. The gcd of h and all d^J, d in E, is one:
a prime dividing all of them would divide every member of E.

Bezout's identity gives integer coefficients whose combination of those
residues is 1 modulo h. Reduce each coefficient modulo h to a nonnegative
integer between 0 and h-1. Realize each copy using a distinct arbitrarily
late exponent of that base having the same recurring residue. This constructs
a finite positive subset sum z above K with z=1 modulo h. The same argument
works for any prescribed residue, and avoids any given finite label set.

## 3. The persistent subgroup is either zero or all of Z

Suppose H=hZ with h>=1. Fix K. Choose the preceding finite positive sum z
with z=1 modulo h. The integer 1-z belongs to hZ=H. Represent it beyond all
exponents used by z. Combining the disjoint supports represents 1 above K.
Since K was arbitrary, 1 belongs to H. Thus H=Z.

Therefore H is either {0} or Z. This argument uses gcd(E)=1 but no mass
hypothesis. It does not assert that either possibility is absent in the
half-mass family.

Let delta(K) be the least positive element of T_K; it exists because d^K
belongs to T_K. The sets T_K decrease, so delta(K) is nondecreasing.
If H={0}, then for any C there is a K excluding every nonzero integer in
[-C,C]: choose an excluding cutoff for each of the finitely many integers
and take their maximum. Hence delta(K) tends to infinity.
Conversely, bounded delta(K) gives a persistent nonzero integer by the
finite descending-set argument, and therefore H=Z by the dichotomy.

The half-mass unit claim is thus equivalent to excluding delta(K)->infinity
for every admissible E. A cutoff-independent finite bound on delta(K)
would suffice. A bound that grows with K does not.

## 4. What reciprocal mass one half gives directly

Here assume sigma(E)>=1/2. Order the labels above K by value, retaining
multiplicity, as a_1,a_2,..., and write S_i=sum_{r<=i}a_r.
Put C_K=sum_{d in E}d^K/(d-1).

For x=a_i, all labels of value strictly below x precede a_i. For each base,
the geometric sum of its powers in [d^K,x) is at least (x-d^K)/(d-1).
This remains true when the sum is empty. Thus
S_{i-1}>=sigma(E)x-C_K and a_i-2S_{i-1}<=2C_K.

For a finite signed-prefix set A with endpoints -S,S, adding a positive
weight a gives (A-a) union A union (A+a). If a>2S, the new between-hull
gaps are a-2S. If a<=2S, the three hulls overlap and the largest gap is
no larger than the old largest gap. To check the latter statement, take
a gap in the union and its midpoint. One hull contains the midpoint.
Its endpoints are in the union, so they cannot lie inside that gap;
the two neighboring points of its own translated set bound the whole gap.

Induction from {0} therefore bounds every signed-prefix gap by
G_K=ceil(2C_K). Prefix endpoints tend to both infinities. It follows that
every interval [u,u+G_K], u in Z, meets T_K. Each signed tail is syndetic,
but this bound depends on K and does not prove that H is nonzero.

## 5. A non-pure-power warning example

For the sequence b_j=3^j+2, j>=1, define signed tails in the same way.
If the largest used index is N and its sign is positive, then every nonzero
signed sum with indices at least K has value at least
(3^N+3^K)/2+2-2(N-K).
This lower bound increases with N, because its next increment is 3^N-2>0.
Flipping all signs covers the other case. Thus its least positive tail
difference is exactly 3^K+2, attained by the single term b_K.

Nevertheless gcd(b_K,b_{K+1})=gcd(3^K+2,4)=1. For any modulus h, choose
J>=max(K,h), so b_J and b_{J+1} both have recurring residues modulo h.
They too are coprime. Every tail therefore covers all residues by positive
subset sums, using repeated copies of these two recurring residues at
distinct later indices. Its signed tails have bounded gaps at each fixed K:
b_{N+1}-2 sum_{j=K}^N b_j=3^K+2-4(N-K+1), so the preceding mesh induction applies.

Hence tail gcd one, full modular subset coverage and signed-tail syndeticity
alone do not exclude delta(K)->infinity. This sequence is not a finite
union of unshifted pure-power streams. It is not a counterexample to the
admitted claim or the original problem.

## 6. An aligned common-radix family supplies a full signed lattice

Let B>=2 and let A be a nonempty finite set of positive integers. Suppose
R={B^a:a in A} is contained in E and sigma(R)>=1/2. This is an additional
hypothesis, not a consequence of the total mass condition on E.

Choose L divisible by every a in A, with L>=aK for each a. The label
(B^a,(L+at)/a), for t>=0, has value B^L B^(at) and exponent at least K.
After division by B^L the available labelled weights are B^(at), one for
each (a,t). There is a separate weight 1 for every a.

We show that their finite signed sums represent every integer. At a level
r>=1 with at least one label of value B^r, the sum W_r of weights strictly
below that level is

W_r = sum_{a in A} (B^(a ceil(r/a))-1)/(B^a-1)
    >= (B^r-1) sigma(R)
    >= (B^r-1)/2.

For a finite weight list whose signed sums fill [-W,W], adjoining a weight
w<=2W+1 preserves a full integer interval: the integer intervals
[-W-w,W-w], [-W,W], [w-W,w+W] overlap or are adjacent. The first weight 1
satisfies this criterion with W=0. Each later weight 1 does as well. At any
positive level r, the displayed inequality gives B^r<=2W_r+1, so the first
label at that level satisfies the criterion. Subsequent labels at the same
level only increase the preceding sum. Induction therefore gives the full
signed interval for every finite prefix. The endpoints tend to infinity,
so their union is Z.

Restoring B^L, the original R labels above cutoff K represent every integer
multiple of B^L, with coefficients in {-1,0,1} and no repeated label. The
map (a,t) to (B^a,L/a+t) is injective, so this conclusion preserves both
label capacities and the original exponent cutoff. No finite enumeration,
asymptotic rounding or balanced-digit termination claim is needed.

Now use gcd(E)=1. The set C=E\R is nonempty, and gcd(B,{c:c in C})=1:
any common prime divisor would divide all of E. For h=B^L, the modular
argument of section2, applied to C, provides a positive finite sum z of
C labels above K with z=1 modulo h. It needs only gcd(h,{c:c in C})=1,
which follows from the same prime-divisor argument. The integer (1-z)/h
has a finite signed representation in the normalized R weights. Combine
it with z. The two supports have different base labels, so they are disjoint,
and their signed total is exactly 1. Increasing K first avoids any prescribed
finite forbidden set.

Thus an E containing such an R has signed units after every cutoff and
finite deletion, regardless of the mass of E\R. This proves a special
case of the admitted assertion, not the assertion for arbitrary E.

For B=3, R={3} already has mass1/2. For B=2, one obtains every finite
power-of-two seed family of mass at least1/2, not just {4,8,16}. For example,
R={4,8,32} has mass 1/3+1/7+1/31=331/651>1/2, and it does not contain16.
These are exact hand calculations, not a computational search.

## 7. Counterexample restrictions and the remaining obligation

Any hypothetical counterexample to the admitted half-mass claim must have
H={0}, delta(K) tending to infinity, and a syndetic signed set at each fixed
K as above. It cannot contain a common-radix subset R with sigma(R)>=1/2.
In particular it cannot contain3, and the total reciprocal mass of all of
its power-of-two bases must be less than1/2. The new common-radix exclusion
is additional compression, not just a restatement of the unknown unit.

The shifted-power example in section5 passes the abstract gcd, modular and
fixed-cutoff gap tests. It is outside the pure-power domain and does not
satisfy every condition just derived. Accordingly it is an obstruction to
that abstract inference, not this move's strategy-failure signal and not
a counterexample to the admitted claim.

The case of total mass at least1/2 without a common-radix half-mass subset
remains open. No bounded range or process is produced. The direction false
records only the assumed counterexample used for this analysis. The move
pays object and obligations because its output is a necessary-condition list
and a special-case construction, rather than a proof of the full claim.
It does not close the native attack or justify cash-out.

An exact successor claim may combine the aligned lattice with a disjoint
positive reserve, or seek a new noncommensurate condition on delta(K).
The move has been journalled. Before such a successor, preserve its pending
hypothesis checkpoint. Any accepted auxiliary theorem requires separate reviewed
admission for its exact claim. No percentage of the original infinite
domain is certified by this reduction.

## Author verification

The proof was checked by hand against arbitrary K, finite deletions, label
coincidences, all common periods, the mass-equality boundary, and both signs
of the lattice coefficient. Eventual periodicity modulo h needs no coprimality
of each individual base: the finite-state orbit has entered its cycle by
index h, and only the collective gcd is used. In section5 the consecutive
terms are odd, their difference after subtracting three times the first is
-4, and hence they are coprime. Their recurring residues modulo any fixed
h provide the asserted modular coverage after a sufficiently late cutoff.
The signed largest-index bound there is positive and increasing, including
N=K, which verifies the exact least positive value. Section6's interval
induction is independent of section4's general maximum-gap argument.

This is author verification only. Independent result review has not run.
