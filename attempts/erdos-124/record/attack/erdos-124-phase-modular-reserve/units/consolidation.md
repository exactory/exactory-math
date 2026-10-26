# Consolidation of the phase-modular completeness proof

This is the closing consolidation for node21 move1, outside the move budget.
It is not an independently accepted result or a second proof.

## Steps requiring explanation and their replacements

The first possible gap is charging a finite signed support to a positive
reserve. The rewritten proof makes its accounting explicit: only one
selected V power per unit is charged to V, while both large signed
supports lie on R. The same W sums all selected V corrections across
all unit boundaries. Sections2--3 prove every scale before the seed exists.

A second possible gap is using the full CP26 theorem with an unassumed
gcd(V)=1. The rewrite proves its elementary three-scale prefix interface
in full on V and does not use any spectral conclusion. The crucial
integer geometric-sum inequality, cutoff charge and strict-prefix
endpoint conventions are visible in equations(5)--(12).

A third possible gap is combining modular periodicity with an unrelated
syndetic phase set. Section5 instead applies a compact torus argument
directly to the period-multiple generator. Arbitrarily late returns
near zero suffice here; CP26's stronger bounded-waiting conclusion is
not needed. The compact-cover proof also covers finite periodic orbits,
because it selects infinitely many indices, not distinct orbit points.

The purported case without an individually coprime correcting base
is absent: the existing common-radix mass restriction forces B=2 or3.
Section4 reproves this scope fact and then fixes one coprime c in V.
There is no new collective-coprimality theorem.

The seed-to-cofiniteness implication is not inferred from signed units
alone. Section1 fixes the exact length-g interval needed by the final
unchanged reserve, and Section6 checks disjoint labels and both interval
endpoints after all g-1 pairs. Finite deletions on R change only its
cutoff, never the V charge or gap.

## Consolidation outcome and second-route check

No computation or unproved external theorem needed replacement.
All required steps now have self-contained proofs using elementary
arithmetic, finite induction and compactness. The complete rewritten
argument follows below, with each interface separated.

A second presentation could keep CP22's general finite modular-correction
recipe, selecting its multiple V labels one at a time under the same
phase test. It would share the new prefix estimate and lattice, add
unnecessary labels on the actual B=2 or3 domain, and is not an independent
second proof. No second-proof unit is claimed.

The exact admitted structural theorem, for every positive cutoff and
finite labelled deletion, is the broad conclusion proved here.
Its prefix lemma does not require gcd(V)=1, while its signed lattice
requires the stated common-radix half-mass condition. The minimum-three
strict-mass-above-three-halves consequence and the two comparison examples
belong to this one unit. Equality, arbitrary mixed half-mass input and
the original mass-one objective are not conclusions of the argument.

## Complete rewritten proof

# Move 1: phase-restricted modular corrections with a fixed positive reserve

Node: node-000021. Strategy: make-the-proof-constructive, plan step 3.
Entry: seed-and-amplify. Reservation: revision396, move-node-000021-1.
Status: analytical proof candidate, pending independent result review.
No mathematical program, finite enumeration or formal checker was run.

## Exact claim and notation

For every nonempty finite set D of distinct integers at least 3 with gcd(D)=1 for which there exist an integer B>=2 and a nonempty finite set A of positive integers such that R={B^a:a in A} is contained in D, sigma(R)=sum_{d in R}1/(d-1)>=1/2, V=D minus R has min V>=4 and sigma(V)>1, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit an integer N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each pair (d,j) used at most once and coincident numerical values from different pairs retained separately.

Fix an input and witnessing B,A,R,V. A label is a pair (d,j), of value
d^j. Write value(E) for the sum of a finite label set E, and FS_0(T)
for finite positive subset sums of a supply T, including zero.
A signed representation assigns one coefficient in {-1,0,1} to each
of finitely many labels. Its positive and negative supports are disjoint.
Coincident values do not identify their labels.

Let F_V and F_R be the parts of F on V and R. Define the original
V supply P_V by d in V, j>=k and (d,j) outside F_V. Its cutoff is
never raised. The final unused reserve will be P_V minus a finite
list of individually selected correction labels.

The preservation estimate below develops the elementary prefix interface
of accepted CP26, node20 move1 Sections2--3, without a gcd assumption on V.
The lattice and final interval argument develop the elementary interfaces
of accepted CP22, node16 move1 Sections1--3 and5. All ingredients needed
for the present conclusion are proved here. Their spectral conclusions
and external sumset theorems are not used.

## 1. The amplification law and the constants fixed before any seed

Suppose finite disjoint pairs (P_i,Q_i), 1<=i<=r, use pairwise disjoint
labels across BOTH supports of all pairs and satisfy

    value(Q_i)-value(P_i)=1.

Then, with H_r=sum_i value(P_i), selecting Q_i instead of P_i for the
first t pairs represents H_r+t for every 0<=t<=r. Thus their union
positively represents the integer interval [H_r,H_r+r].
One new pair increases the interval length by exactly one.
For r=0 the represented interval is {0}.

Suppose the labels of all these pairs are disjoint from a supply U,
and FS_0(U) meets every interval of g consecutive nonnegative integers,
where the positive integer g was fixed before the pairs were chosen.
For r=g-1 and n>=H_r+g-1, the g nonnegative integers in

    [n-H_r-g+1, n-H_r]

include some v in FS_0(U). Then n-v is in [H_r,H_r+g-1].
Its seed support and a support for v are disjoint, so their union
represents n legally. This proves the amplification law. The remaining
preservation obligation is to retain that same g as the pairs are added.

Set, using ONLY the fixed original V,k,F_V,

    sigma = sum_{d in V}1/(d-1),        delta = sigma-1 > 0,
    M = max V,
    C0 = sum_{d in V}d^k/(d-1),
    C = C0 + value(F_V),               g = ceil(C),
    K0 = 2+2/delta,
    epsilon = delta/[4(sigma+2K0)],
    eta = delta/(2 sigma),
    Lambda = 2M+4 sigma/delta = 2M+2/eta.                (1)

All are positive rational numbers except the specified integers.
In particular,

    epsilon<1/4,  eta<1/2,
    Lambda>2M,  Lambda>2/eta>1.                         (2)

Before any unit is constructed, impose the following rule on its
V correction label q_i, whose base may be any member of V:

    q_i > Lambda(C+W_{i-1}),                             (3)
    W_{i-1} = sum_{j<i}q_j,
    for every d in V, a power a_d=d^{n_d} lies in
                [(1-epsilon)q_i,(1+epsilon)q_i].        (4)

The exponents in (4) may initially be tested among nonnegative integers.
The growth rule will force all a_d above d^k. The ledger W is global
across the entire construction. It is not restarted for a new pair.
We first prove the preservation law for ANY finite list satisfying
(3)--(4), before showing that the first label and later labels exist.

## 2. An integer margin and the all-scale deletion estimate

For z>1 let p_d(z) be the least nonnegative integer power of d at least z.
Writing m=ceil(z), each p_d(z)>=m, and

    (p_d(z)-1)/(d-1)

is a nonnegative integer. Their sum is an integer at least
sigma(m-1)>m-1. It is therefore at least m>=z. Consequently,

    sum_{d in V}p_d(z)/(d-1) >= z+sigma.                 (5)

Only strict sigma>1 is used here, not gcd(V)=1.

Also, for any x>0,

    sum_{j>=k, d^j<x}d^j >= (x-d^k)/(d-1).              (6)

When x<=d^k the right side is nonpositive. Otherwise the geometric
sum has numerator b_d(x)-d^k, where b_d(x) is the least d-power
at least x. This also handles x equal to a power, since the prefix
is strict.

Fix a finite list satisfying (3)--(4). At a scale x for which there is
a selected q_i<=x, take the latest such q=q_i, and put W=W_{i-1}.
The values q_i are strictly increasing by (3), so every later
selected value exceeds x. Let h be the base of q. In (4) take a_h=q.

From q>2MC and epsilon<1/4, for every d in V,

    a_d >= (1-epsilon)q > (3M/[2(d-1)])d^k > d^k.       (7)

Further, a_d/d<q. The original powers strictly below a_d are therefore
strictly below q. Subtracting value(F_V) and W from any chosen original
subcollection is a valid lower bound even if some of those removed
labels were not in that subcollection.

For q<=x<=(1+epsilon)q, take the powers below a_d from every base.
They exclude the current selected label because a_h=q. Their retained
total is at least

    (1-epsilon)sigma q-C-W
      >= x+[delta-epsilon(sigma+1)]q-C-W
      >= x+(3delta/4)q-C-W.                            (8)

Here epsilon(sigma+1)<=epsilon(sigma+2K0)=delta/4.

For (1+epsilon)q<x<=K0 q, put z=x/[(1+epsilon)q]>1.
Since x>a_d, write b_d(x)=a_d d^r with r>=1. The inequality
d^r>=x/a_d>=z gives d^r>=p_d(z), and hence
b_d(x)>=(1-epsilon)q p_d(z).
The complete original strict x-prefix has total
sum_d(b_d(x)-d^k)/(d-1).
After subtracting F_V, all earlier selections, and the current q,
equation (5) gives a retained total at least

    (1-epsilon)q(z+sigma)-C-W-q
      = x+[delta-epsilon sigma
                  -(2epsilon/(1+epsilon))(x/q)]q-C-W
      >= x+[delta-epsilon(sigma+2K0)]q-C-W
      = x+(3delta/4)q-C-W.                             (9)

For x>=K0 q, summing (6) and subtracting those same removed weights
gives the lower bound

    sigma x-C-W-q
      >= x+(delta K0-1)q-C-W
      = x+(2delta+1)q-C-W
      >= x+q-C-W.                                     (10)

The three ranges cover every x>=q, including their endpoints.
Since eta<min(3delta/4,1), equations (8)--(10) and (3) imply

    retained strict-prefix total
       >= x+eta q-C-W > x+(eta/2)q.                    (11)

If no selected q_i<=x exists, summing (6) and paying F_V gives at
least sigma x-C>=x-C. Thus, after EVERY finite prefix of eligible
selections, its actual retained supply U satisfies

    sum_{ell in U, value(ell)<x}value(ell) >= x-C
    for every x>0.                                    (12)

This is a simultaneous all-scale assertion with the SAME original C.
Only the latest removed selection at most x and the single cumulative W
were used. There is no arbitrary-block cost assumption and no reset
at a unit boundary. Numerical ties are harmless: the original geometric
sums count all base labels, and subtracting q removes just its one label.

Every selected label is legal. Equation (7), with h, implies q>h^k.
Also q>C exceeds every value in F_V. Rule (3) makes its value greater
than every previous selected value. Thus no correction label repeats.
The retained supply is infinite, because a finite total weight would
contradict (12) as x tends to infinity.

## 3. The fixed-gap consequence

List the retained supply U in nondecreasing value, retaining all labels
and breaking ties by base. Let a_i be its values and S_i their prefix sums,
with S_0=0. All values strictly below a_i precede it. Equation (12) gives

    a_i-S_{i-1} <= C <= g.                              (13)

For a finite prefix, its subset-sum set contains 0 and S_i.
Inductively, its consecutive gaps are at most g: adjoining a_i replaces
the preceding set E by E union (a_i+E). Each copy has gaps at most g.
If their spans are disjoint, the intervening gap is
a_i-S_{i-1}<=g. If their spans overlap, any gap inside their combined
span is bounded by the consecutive points of at least one copy.
A gap cannot pass through a span endpoint, since that endpoint is in
the union. The first nonempty prefix has gap a_1<=g.

Since S_i tends to infinity, this finite-prefix assertion implies that
FS_0(U) meets every interval of g consecutive nonnegative integers.
Indeed, an interval missing all subset sums and not containing zero
would, within a sufficiently large prefix span, lie between two
consecutive subset sums at distance at least g+1.

Therefore the reserve gap g in Section1 survives every eligible
correction, before any seed is chosen. The estimate neither assumes
gcd(V)=1 nor deduces a signed unit from bounded gaps.

## 4. Available radices and the fresh signed lattice

We record the already known scope restriction from CP22, with proof.
If B>=4, then

    sum_{a>=1}1/(B^a-1)
      <= sum_{a>=1}1/[(B-1)B^{a-1}]
       = B/(B-1)^2 <= 4/9 < 1/2.

The penultimate inequality follows from (B-4)(4B-1)>=0.
Thus the hypothesis on R forces B=2 or B=3. For B=3, if 1 is absent
from A, the same geometric bound from a=2 onward is at most1/4,
so 3 must belong to R. Since every R base is divisible by the prime B,
gcd(D)=1 implies some c in V is coprime to B. Fix the least such c.
This does not require gcd(V)=1.

For any integer K_R>=k, choose a positive common multiple L of all
a in A with L>=a K_R for every a, and set m=B^L.
Use the injectively indexed R labels

    (B^a,L/a+t),   a in A, t>=0.

Their values divided by m are the labelled weights B^{at}.
Every original exponent is at least K_R.

For positive labelled weights w_1,w_2,... in nondecreasing order,
if w_i<=2T_{i-1}+1, where T_0=0 and T_i=sum_{j<=i}w_j, then their signed
prefix sums fill [-T_i,T_i]. The induction adjoins the three intervals
[-T-w,T-w], [-T,T], and [w-T,w+T]. The inequality makes them overlap
or meet at adjacent integer endpoints, so their union has no gap.

For the normalized R weights, at every positive level r carrying B^r,
the sum of strictly smaller weights is

    sum_{a in A}(B^{a ceil(r/a)}-1)/(B^a-1)
       >= (B^r-1)sigma(R) >= (B^r-1)/2.

The initial weights are labelled copies of1, which satisfy the induction.
The first weight at level r satisfies B^r<=2T+1, and any tied later
weight has a larger preceding sum. The normalized endpoint sums tend
to infinity. Every integer therefore has a finite legal signed
representation on these weights.

Restoring m, the R supply at cutoff K_R represents every multiple of m
by a finite signed sum. Choosing K_R above every exponent in any finite
forbidden R set ensures that both signed supports avoid that set.
The label map is injective; equal values never consume one label twice.

## 5. Phase recurrence after imposing a modular period

Fix any m=B^L arising in Section4. Multiplication by c is a permutation
of the finite group of invertible residues modulo m.
Two powers of c coincide, and cancellation yields a positive t with
c^t congruent to1 modulo m. Let t be the least positive such integer.
A finite search for this t terminates, but no such search is run here.

We show that arbitrarily large exponents e divisible by t satisfy (4).
Put theta_d=t log(c)/log(d), considered modulo one, for d in V.
For every rho>0 and every lower bound J, there exists an integer u>=J
with all coordinate distances ||u theta_d||<rho.
To prove this, cover the compact torus by finitely many sets of diameter
less than rho in its translation-invariant maximum-coordinate metric.
One cover set contains the orbit points n theta for infinitely many
indices n>=0. Choose two such indices with difference u>=J.
Subtracting the points yields the required return near zero.
This works on the actual period-multiple orbit regardless of any rational
relations; no density in the full torus or intersection of syndetic
sets is assumed.

Choose rho>0 less than every number

    log(1+epsilon)/log(d),  -log(1-epsilon)/log(d),  1/2,
    d in V.

For a return u, choose an integer n_d with
|n_d-ut log(c)/log(d)|<rho. Writing e=ut and q=c^e gives

    1-epsilon < d^{n_d}/q < 1+epsilon.

Take u sufficiently large that q>Lambda(C+W), for any prescribed
finite current global ledger W. The powers d^{n_d} then exceed d^k
by (7); the exponents are nonnegative and legal. Thus q satisfies
(3)--(4) AND q congruent to1 modulo m.

There is an entirely integer/rational selection rule: test u=1,2,...
and take the first whose q=c^{tu} exceeds Lambda(C+W) and passes (4).
For each d, testing (4) means generating its powers until the lower
endpoint is reached and comparing with the upper endpoint.
The recurrence argument proves termination. Logarithms prove existence
but are not part of the selection test. No uniform bound over the
changing periods t or final support heights is claimed.

## 6. A one-label positive seed and its repeated extension

Sections1--3 established the amplification and the fixed-gap preservation
law before constructing a seed. The smallest possible positive integer
interval increment is one. We now obtain that increment with exactly
one selected V label.

At any stage, let E_R be the union of F_R and both R supports of all
previous pairs. It is finite. Choose K_R>=k above all its exponents,
then choose L,m as in Section4. Section5 selects one new eligible
V label q, using the CURRENT W, such that q is congruent to1 modulo m.
Section4 represents the integer 1-q on fresh R labels as a finite
signed sum, because m divides 1-q. Add the positive label q.
This gives an exact signed sum of1. Its positive support Q_i and
negative support P_i are finite, disjoint, avoid F, and satisfy

    value(Q_i)-value(P_i)=1.

Both R supports avoid all earlier R supports by construction.
The new V label avoids all earlier V labels by strict growth.
R and V are disjoint base sets, so every pair is disjoint from all
earlier pairs in BOTH signs. After the extension set W:=W+q;
never change V's original k,F_V,C,epsilon,Lambda or g.

The first application, with W=0 and E_R=F_R, is a computer-free
unit seed. The same argument extends every finite state by one pair.
Each extension gains one integer of interval length and keeps the
original reserve gap by Sections2--3. There is no dilution under
iteration and no unpaid support cost on V: only the single selected
q is removed there. R supports may be large, but they lie outside V.

Perform exactly r=g-1 extensions. Let T be the union of both supports
of all pairs, let H=sum_i value(P_i), and let U be P_V with precisely
the r selected correction labels removed. Then T and U are disjoint.
Section1 represents [H,H+g-1] on T, and Section3 supplies the unchanged
g-gap property on U. Therefore every n>=H+g-1 is represented on T union U.
Take

    N(D,k,F)=max(1,H+g-1).                               (14)

All supports are finite, all exponents are at least k, all labels avoid F,
and each label is used at most once. Equal numerical values across labels
remain separately available. This proves every quantifier of the claim.

The construction is a terminating procedure, not an executed computation.
Choose witnessing B,A by any fixed finite order among subsets of D;
the bounds B in {2,3} make this finite when a witness exists.
The stated period and correction rules terminate. A signed lattice
representation can be found by extending normalized prefixes until
their total reaches the absolute normalized target and then using
the proved three-interval induction backwards. There are finitely
many pairs. For a requested n>=N, extend reserve prefixes until their
endpoint exceeds n-H; finite subset enumeration then finds the
required reserve value, by the g-gap proof. These are descriptions
with termination proofs, not reported runs or efficiency bounds.

## 7. Scope improvement and the limits of this seed class

The operation uses just one V correction per pair. Within this lattice
recipe zero V corrections cannot produce a signed unit, because all R
values are divisible by B. Thus one is the smallest nonzero correction
count for this recipe. The least eligible q minimizes the correction
value for its fixed c,t and current ledger; global optimal support size
or a smallest possible final N is not claimed.

If min D=3 and sigma(D)>3/2, take R={3}. Then sigma(R)=1/2 and
V=D minus {3} has minimum at least4 and mass greater than1.
The theorem consequently proves eventual completeness with every
positive cutoff and finite labelled deletion on this entire range.
It does not include total mass exactly3/2 by this deduction.

For an explicit comparison, D={3,4,5,6,7,8} has

    sigma(V)=153/140>1,     sigma(D)=223/140<11/6.

It is below the earlier accepted ternary11/6 range. It also fails CP22's
whole-correction-base criterion: its only qualifying ternary R is {3};
removing a nonempty correction set costs at least1/7, leaving at most
153/140-1/7=19/20<1. Its available binary R is contained in {4,8},
whose mass10/21 is below one half. Larger radices cannot qualify.
Thus the present theorem has a concrete additional completeness input.

There are also additional nonternary inputs. Let

    D={4,5,6,7,8,9,10,11,12,32},   R={4,8,32}.
    sigma(R)=331/651>1/2,
    V={5,6,7,9,10,11,12},          sigma(V)=4133/3960>1.

The gcd is one. Among its binary bases only the full R reaches half
mass, because every proper subset has mass at most10/21.
There is no qualifying ternary R, since3 is absent.
Every nonempty correction set coprime to2 contains an odd base from
{5,7,9,11}, of reciprocal mass at least1/10. The mass outside R and
such a correction set is at most

    4133/3960-1/10=3737/3960<1.

Hence CP22's whole-base correction criterion fails here too.
This is an exact hand calculation within the analytical proof, not
a bounded search or an additional checkpoint.

Strict sigma(V)>1 is used in (5) and the positive constants.
At equality delta=0 these choices do not exist; a limit of the
parameters is not an equality proof. The common-radix half-mass
hypothesis supplies an actual signed lattice. No such lattice is
proved here for arbitrary mixed bases at half mass.
The global weight ledger and label disjointness are essential to
this operation; arbitrary finite block removal is not established.

The original reciprocal-mass-one objective, the new complementary
obligation53 and root bridge54, the general half-mass signed-unit
claim, and equality and nonqualifying structural cases remain open.
The minimum-three consequence is part of the same structural proof,
not a replacement of its full claim or a separately counted result.

## 8. Entry outcome and verification boundary

The entry order is explicit: Section1 proves the interval amplification
law; Sections2--3 prove preservation for every eligible finite state;
Sections4--5 establish the legal fresh extension; Section6 supplies
the smallest positive unit seed and iterates it; Section7 optimizes
the correction count within the recipe and tests its scope limits.
No amplification or preservation hypothesis is left unpaid.
No entry or strategy failure signal fires.

The admitted statement and stage are unchanged. This complete
analytical candidate justifies direction true and mode construction.
The closing cost ledger is empty: no part of the exact claim,
constructivity or a requested bound has been given up.

The mathematical proof is self-contained in elementary integer
arithmetic, finite induction and compactness of a finite-dimensional
torus. CP26 and CP22 identify the earlier local interfaces and the
source of the method, but their spectral and sumset conclusions
are not premises. No formal-kernel check, mathematical program,
exhaustive novelty, publication-priority or root-closure claim is made.
Independent exact-result review and immutable evidence acceptance
are still required.
