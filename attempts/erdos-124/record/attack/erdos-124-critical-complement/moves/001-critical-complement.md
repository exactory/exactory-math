# Move 1: exact critical-complement preservation and extension

Node: node-000022. Strategy: make-the-proof-constructive, plan step 3.
Entry: seed-and-amplify. Reservation: revision422, move-node-000022-1.
Status: complete analytical proof candidate, pending independent result review.
No mathematical process, finite enumeration or formal checker was run.

## Exact claim and notation

For every nonempty finite set D of distinct integers at least 3 with gcd(D)=1 for which there are an integer B>=2 and a nonempty finite set A of positive integers such that R={B^a:a in A} is contained in D, sigma(R)=sum_{d in R}1/(d-1)>=1/2, and V=D minus R has min V>=4, sigma(V)=1, contains multiplicatively independent integers a,b, and satisfies H_V(x)>x for every real x>1, where p_d(x) is the least nonnegative integer power of d at least x and H_V(x)=sum_{d in V}(p_d(x)-1)/(d-1), every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit an integer N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each labelled pair used at most once and coincident numerical values retained separately.

Use I for the witnessing radix exponent set in the proof, reserving A for
an integer estimate below. A label is a pair (d,j), of value d^j.
Write value(E) for the sum of a finite label set E, and F_V,F_R for the
parts of the original forbidden set on V and R. The original V supply is
P_V={(d,j):d in V,j>=k,(d,j) not in F_V}. Its cutoff never changes. Set

    C=sum_{d in V}d^k/(d-1)+value(F_V),  g=ceil(C),  M=max V.

The state W is the sum of ALL previously selected correction values;
initially W=0. The exact rule(E),
preservation assertion(P), recurrence assertion(R) and two-application limit are
those in study/OPERATION_SPEC.md. This file does not change that rule or add
a hypothesis to the claim. Symbols C, W, g, P_V, q, a_d, M and epsilon have
their specified meanings. Write v=|V| and sigma(V)=1.

## 1. Amplification before a seed

If r pairs of finite positive supports (P_i,Q_i) are mutually disjoint across
both signs and value(Q_i)-value(P_i)=1, their union represents every integer
in [H,H+r], where H=sum_i value(P_i). Choose Q_i for the first j pairs and
P_i for the others to obtain H+j. One extra disjoint pair increases r by one.

If a disjoint unused supply U has positive subset sums meeting every interval
of g consecutive nonnegative integers, r=g-1 suffices for completeness:
for n>=H+g-1 choose a subset sum u of U in [n-H-g+1,n-H]. Then n-u belongs
to [H,H+g-1], and the two supports are disjoint. The required preservation
law must keep the original g=ceil(C) before any such pair is selected.

## 2. A quantitative normalized margin

Fix the multiplicatively independent a,b in V provided by the hypothesis.
All logarithms in this proof are natural. Define integers and positive rationals

    A=40000 M^2,  K_1=2M+3,
    lambda=1/[(M-1) 4^(1000A) K_1^A].

For z>1, write p_a(z)=a^m and p_b(z)=b^n. Both m,n are positive and
p_d(z)<dz<=Mz. The logarithm form Lambda=m log(a)-n log(b) is nonzero.

The selected primary input is Gouillon2006, DOI10.5802/jtnb.537, Section2
setup and Corollary2.3 (study/sources/criticalGouillonReading2.json).
Here its field degree parameter is 1, its logarithmic heights are log(a)
and log(b), and its choices log(A_1)=log(a), log(A_2)=log(b) satisfy the
stated height and positivity requirements, since a,b>=4. Its positive
coefficient parameter is beta=m/log(b)+n/log(a)<=2 log(Mz). The numerical
coefficient 7200(3.409+1.705) log(a)log(b) is at most our A. Its h is at
most 1000+log(1+beta). Consequently

    |Lambda| >= exp(-1000A) [1+2 log(Mz)]^(-A)
              >= 4^(-1000A) K_1^(-A) (1+log z)^(-A).

The last inequality uses e<4 and 1+2 log(Mz)<=K_1(1+log z).
If p_a>=p_b then p_a-p_b=p_b(exp(Lambda)-1)>=z Lambda; reversing a,b
gives the same conclusion with absolute values. Therefore

    |p_a(z)-p_b(z)| >= (M-1)lambda z/(1+log z)^A.

Every p_d(z)>=z and sigma(V)=1, so

    H_V(z)-z = sum_d [p_d(z)-z]/(d-1)-1
              >= lambda z/(1+log z)^A-1.                 (1)

The strict H_V hypothesis provides a second, exact bound. For the integer
j=ceil(z), H_V(z)=H_V(j); all powers are integers and the least power
at least z is the least power at least j. H_V(j) is an integer, since
(p_d(j)-1)/(d-1) is a geometric sum. Thus H_V(j)>j implies

    H_V(z)-z >= 1.                                      (2)

These arguments use neither gcd(V)=1 nor a claim that the H_V hypothesis
holds automatically.

Choose an integer N>=2A with

    lambda 2^N >= 2(1+N)^A,

and put Z_0=2^N. This integer search terminates because an exponential
eventually exceeds a fixed polynomial. It is a description, not a run.
The function f(z)=z/(1+log z)^A is increasing when log z>=A-1.
Since log(2)>1/2, every z>=Z_0 has lambda f(z)>=2.
Set the positive rational

    kappa=min(lambda/2, 1/Z_0).

Combining (1) on z>=Z_0 with (2) on 1<z<=Z_0 gives the uniform estimate

    H_V(z)-z >= kappa z/(1+log z)^A   for every z>1.     (3)

All its constants are computable from V alone.

## 3. One constant for all correction lists

Set L=2A+2 and K=M+2. For q>1 define, for this proof's estimates only,

    y(q)=log(1+log q),
    Z(q)=(1+log q)^L,
    nu(q)=kappa/[1+L y(q)]^A.

These real-valued comparison functions do not replace the integer-defined
epsilon in rule(E). In fact h(q)+2>=1+log q and
s(q)>sqrt(log(h(q)+2)/log 2)-1 imply

    epsilon(q) <= 2 exp(-sqrt((log 2)y(q))).             (4)

There is an effectively selectable integer Y>=32A^2+2A+2 such that,
for every y>=Y,

    4K exp(-sqrt((log 2)y)) [1+Ly]^A < kappa,           (5)
    kappa exp((exp(y)-1)/2)/[1+Ly]^A > 2,              (6)
    kappa exp((L-A)y)/(L+1)^A > 2.                     (7)

Here is an effectivity justification, not merely a limiting assertion.
Each inequality eventually holds. The logarithm of the left-to-right
ratio favorable to (5) has derivative
sqrt(log 2)/(2 sqrt(y))-AL/(1+Ly)>0 on this range, since
y>=32A^2 and log 2>1/2. The favorable logarithm for (6) has derivative
exp(y)/2-AL/(1+Ly)>0; that for (7) has constant positive derivative L-A.
Enumerate integers Y in this range and dovetail certified rational
enclosures of the three strict inequalities. Some integer has a strict
certificate, so this is a terminating computable selection. Monotonicity
then certifies all larger y; no quantified real-number search is assumed.

Choose a computable integer Q_0(V)>=16M^2 large enough that y(Q_0)>=Y,
log Q_0>=A and Q_0>=16. For example, increase an integer J until
J>=2Y+2 and 2^(2^J)>=16M^2, and take Q_0=2^(2^J).
Then, for every integer q>Q_0, (4)--(7) imply

    K epsilon(q) < nu(q)/2,
    sqrt(q) nu(q) > 2,
    kappa(1+log q)^(L-A)/(L+1)^A > 2.                  (8)

This is the same Q_0 for every k,F_V,W,correction base and modular period.
The construction of Q_0 invokes no seed support.

## 4. Proof of the exact preservation assertion(P)

For each original base d and every x>0 its strict positive-cutoff prefix
has weight at least (x-d^k)/(d-1). If x>d^k the exact weight is
[p_d(x)-d^k]/(d-1); otherwise the claimed lower bound is nonpositive.
Summing and paying all forbidden V labels gives at least x-C.

Consider any finite list allowed in (P). The growth condition forces its
values to increase strictly. Fix x>0. If no selected q_i<=x exists, no
selected label has value below x, so the preceding estimate proves P.

Otherwise let q be the latest selected value with q<=x and let W be
the full sum of all earlier selected values. No later selection is below x.
Rule(E) gives

    C+W+1 < sqrt(q),  W<sqrt(q),  q>Q_0.

Every anchor a_d>q/2>MC>=d^k, using q>16M^2 and C<sqrt(q).
Also a_d/d<q since d>=4 and epsilon<=1/(100M).
All powers strictly below a_d therefore lie strictly below q.

For q<=x<=(1+epsilon)q, use the powers from exponent k strictly below
a_d for every d, and additionally the anchor a_e<q promised by (E).
These are all strictly below x and they omit the current correction
label: its own anchor is q. The extra anchor is not in the geometric
prefix already counted. Paying F_V and all W, even if some paid labels
are absent from this subcollection, gives retained weight at least

    (1-epsilon)q-C+(1-epsilon)q-W
       >= x-C+(1-3epsilon)q-W >= x-C.                  (9)

The last inequality follows from q>16 and epsilon<=1/(100M).
This directly handles x=q, where the current label is not in a strict
prefix, and handles numerical ties without identifying their labels.

For (1+epsilon)q<x<=q Z(q), put z=x/[(1+epsilon)q]>1.
The least d-power b_d at least x is a_d d^r with r>=1 and d^r>=z,
so b_d>=(1-epsilon)q p_d(z). All x exceed d^k.
Paying F_V, W and the current q bounds the retained weight below by

    (1-epsilon)q[H_V(z)+1]-C-W-q
     = x-C+q{H_V(z)-z-epsilon[H_V(z)+z+1]}-W.

Since p_d(z)<dz, H_V(z)+z+1<=(v+2)z<=Kz.
Also 1<z<=Z(q), so (3) gives H_V(z)-z>=nu(q)z.
Using (8) yields retained weight at least

    x-C+q z nu(q)/2-W >= x-C.                          (10)

Indeed sqrt(q)nu(q)>2 and W<sqrt(q).

Finally, for x>=qZ(q), equation (3) applied at x and the exact original
prefix formula give retained weight at least

    H_V(x)+1-C-W-q
       >= x-C+kappa f(x)+1-W-q.

The function f is increasing throughout this range, and

    1+log(qZ(q)) <= (L+1)(1+log q).
    kappa f(qZ(q))
       >= kappa q(1+log q)^(L-A)/(L+1)^A > 2q.

Since W<sqrt(q)<q, this retained weight is at least x-C.           (11)

The three ranges cover all x>=q. Equations (9)--(11), together with the
case with no selection at most x, prove (P) for every finite allowed list.
No constant, cutoff or removed-weight account was reset. The proof even
allows any correction base in V, as the quantified assertion requires.

## 5. Fixed-gap consequence

List the actual retained supply in nondecreasing value, keeping coincident
labels distinct. If its weights are u_i and S_i=sum_{j<=i}u_j, then P at
x=u_i gives u_i-S_{i-1}<=C<=g, since all labels of value less than u_i
precede this occurrence. The supply is infinite, since P excludes finite
total weight.

The positive subset sums of each finite prefix have gaps at most g.
Inductively adjoining u_i replaces E by E union (u_i+E). If their spans
are disjoint, the intervening gap is at most u_i-S_{i-1}<=g.
If their spans overlap, a gap within the union is controlled by one
copy; it cannot cross a span endpoint, which is a point in the union.
The first gap is u_1<=g. As the prefix total tends to infinity, every
interval of g consecutive nonnegative integers meets a positive subset
sum, including the empty sum zero where appropriate.

Thus the g used in Section1 is preserved before any seed construction.
The missing work is now the precise recurrence(R), its compatibility
with the coprime correction base, lawful seed extension, and the useful
critical-domain requirement. None is inferred from a bounded gap alone.

## 6. Exact signed recurrence on period multiples

Fix c in V with a multiplicatively independent mate e in V, and fix t>=1.
Put theta_d=t log(c)/log(d), for all d in V, and alpha=theta_e.
The number alpha is irrational. For every positive integer r,

    ||r alpha|| >= delta_t r^(-A),
    delta_t=1/[M 4^(1000A) (2t+2)^A].                 (12)

To verify this, take a nearest integer n to r alpha. If n>=1, apply
the same Gouillon corollary to (c,e) with coefficients tr,n. Its
beta=tr/log(e)+n/log(c)<=2tr/log(e)+1/log(c)<=(2t+1)r.
The logarithm estimate is at least
4^(-1000A)[(2t+2)r]^(-A); divide by log(e)<=M.
If n=0, the distance is r alpha>=1/M, which is larger than the
right side of (12). A nearest integer cannot be negative, since
r alpha>0. Irrationality excludes an exact zero distance.

Use the classical simultaneous Dirichlet theorem as stated in
Fishman-Simmons2017, DOI10.1007/s00605-016-0983-0, Section1
(study/sources/criticalPrimaryOpen4.json). In dimension v, for every
integer Q>=2 it supplies integers 1<=r<=Q^v and p_d with

    |r theta_d-p_d|<1/Q for every d.

Let eta_d=r theta_d-p_d. Equation (12) implies r>(delta_t Q)^(1/A);
thus these r tend to infinity with Q. The distinguished eta_e is
nonzero. If eta_e>0, take u=r and n_d=p_d.

If eta_e<0, define the integer K_t=2^(A+1)/delta_t and P=K_t r^A.
Apply simultaneous Dirichlet again, with parameter P, obtaining
1<=s<=P^v and integers z_d with |s theta_d-z_d|<1/P.
Write xi_d=s theta_d-z_d.
Equation (12) forces s>2r: otherwise its distinguished coordinate
has distance at least delta_t(2r)^(-A)>1/P.
Also 1/P<|eta_e|/2 by (12). Set u=s-r and n_d=z_d-p_d. Then

    u>r,
    |u theta_d-n_d|<2/Q for every d,
    u theta_e-n_e=xi_e-eta_e>|eta_e|/2>0.              (13)

The bound 1/P<1/Q follows directly from
r>(delta_t Q)^(1/A) and P=K_t r^A>2^(A+1)Q.
The error coordinates at c vanish exactly, since theta_c=t is an
integer and both Dirichlet errors are less than 1/2. Hence n_c=tu
in both cases.

In both sign cases we have u>=r, u tends to infinity, and

    u<=K_t^v Q^(Av^2).

Writing B_1=Av^2 and D_1=2 K_t^(v/B_1), the selected points therefore obey

    max_d |u theta_d-n_d| <= D_1 u^(-1/B_1),           (14)

with the e coordinate strictly positive. This argument uses differences
of two positive return times with a proved later-time bound, not a
symmetry assertion about a positive orbit or density in a full torus.

For q=c^(tu), its exact tolerance satisfies the lower bound

    epsilon(q) >= exp(-sqrt((log 2)log((2tM+2)(u+1)))).

Indeed h(q)+2<=tu log(c)/log(2)+2<=(2tM+2)(u+1), and the definition
gives s(q)<=sqrt(log(h(q)+2)/log 2).
Any fixed negative power of u tends to zero faster than this lower
bound: take logarithms and compare -(log u)/B_1 with a constant
multiple of sqrt(log u). Thus, for all sufficiently late selected u,

    (log M) D_1 u^(-1/B_1) <= epsilon(q)/2.

Equation (14) now gives |log(d^(n_d)/q)|<=epsilon(q)/2 for every d.
For 0<epsilon<=1, exp(epsilon/2)<=1+epsilon and
exp(-epsilon/2)>=1-epsilon. Hence every anchor lies in the exact
relative interval of (R). Equation (13), or its positive first-sign
case, gives d^(n_e)<q. Taking u later also makes all n_d>=k, q>T,
and epsilon(q)<=1/(100M), since epsilon(q) tends to zero.

This proves (R) with every stated quantifier, the original integer
tolerance, and the strictly below-q sign. The modulus t can be arbitrarily
large and changes between extensions; the proof fixes it only while
constructing that one extension. No uniform recurrence bound in t is
required or claimed.

## 7. The fresh signed radix supply

This section supplies the elementary inherited interface explicitly.
For any integer B>=4,

    sum_{a>=1}1/(B^a-1)
      <= sum_{a>=1}1/[(B-1)B^(a-1)]
       = B/(B-1)^2 <= 4/9 < 1/2.

The last nontrivial inequality is equivalent to (B-4)(4B-1)>=0.
Thus the common-radix hypothesis forces B=2 or 3, both prime.
As all R bases are divisible by B and gcd(D)=1, some c in V is
coprime to B; choose the least one as prescribed in (E).
This c has an independent mate: if it were dependent with both
members a,b of the given independent pair, both log(a)/log(c)
and log(b)/log(c) would be rational, contradicting the pair's
independence. This supplies Section6's hypothesis without changing
the admitted claim.

Let E_R be F_R together with BOTH R supports of every previous pair.
Choose K_R>=k strictly above every exponent in this finite set.
Choose a positive common multiple L_R of the exponents a in the
radix index set, large enough that L_R>=a K_R for every a.
Put m=B^(L_R). The R labels

    (B^a,L_R/a+j),  j>=0,

are all legal and outside E_R. Dividing their values by m gives
the labelled weights B^(aj), including a separate copy of 1 for each a.

For nondecreasing positive integer weights w_i, let T_i be their
prefix sums. If w_i<=2T_{i-1}+1, the signed prefix sums fill
[-T_i,T_i]. Inductively the shifts by -w_i,0,w_i of the previous
interval overlap or meet at consecutive integer endpoints.

At every positive level r carrying a weight B^r, the total weight
of strictly smaller normalized labels is

    sum_a [B^(a ceil(r/a))-1]/(B^a-1)
      >= (B^r-1)sigma(R) >= (B^r-1)/2.

The first label at that level therefore satisfies the induction
condition; tied labels have a larger preceding total. Initial
copies of 1 satisfy it too. Prefix totals tend to infinity.
Every integer has a finite legal signed representation on this
normalized supply. Restoring m, every multiple of m has a signed
representation on fresh R labels. Label injectivity is retained
even when two values agree.

## 8. The first seed, every extension, and the exact conclusion

The least positive t with c^t congruent to 1 modulo m exists because
c is invertible in the finite residue group. Section6, with T above
Q_0(V)+(C+W+1)^2 and all forbidden V values, provides a q=c^(tu)
satisfying every clause of (E). In particular the correction label
is legal, avoids F_V, and exceeds every earlier correction value.
It is congruent to 1 modulo m.

Represent 1-q on the fresh signed R supply in Section7 and add the
one positive V label q. The resulting signed sum is exactly 1.
Its negative and positive supports P_i,Q_i are finite and disjoint
and satisfy value(Q_i)-value(P_i)=1. The fresh R cutoff excludes
both earlier signs; strict correction growth excludes earlier V
labels; R and V have disjoint base labels. Thus BOTH supports of
all pairs remain mutually disjoint and avoid F.

Set W:=W+q and update E_R by both new R supports. Do not change
k,F_V,C,g or Q_0. Sections4--5 prove preservation for the entire
eligible list, so the unused reserve still has the original gap g.
This proves an extension of every finite partial state, including
the initial state W=0,E_R=F_R. One pair is a computer-free seed at
the smallest positive integer interval increment.

Repeat exactly g-1 times. Put H=sum_i value(P_i), let T be the
union of both supports of all pairs, and let U be P_V with only
the g-1 selected correction labels removed. Then T and U are
disjoint. Section1 represents [H,H+g-1] on T and combines it with
the unchanged gap on U to represent every integer n>=H+g-1.
Take N(D,k,F)=max(1,H+g-1).

Every support is finite, every exponent is at least the original k,
every forbidden label is absent, each labelled pair is used at most
once, and numerical coincidences retain their separate occurrences.
This proves the full admitted structural claim, not the original
all-admissible-D mass-one objective.

The construction is effective in the ordinary computability sense,
without an asserted useful running time. Q_0 has the terminating
selection in Section3. The choices of radix witness and cutoff
are finite; the period search terminates. Search u=1,2,... using
only integer powers and the exact dyadic epsilon, with a fixed
order on anchor witnesses. Section6 proves that this search terminates.
A signed lattice representation is obtained from a sufficiently
long normalized prefix and the three-interval induction backwards.
After the finite seed is built, finite reserve subset enumeration
finds the value used in Section1. These describe terminating
procedures with proofs, not executed mathematical processes.

Zero V corrections cannot supply a signed unit within this recipe,
since every R value is divisible by B. Thus its one-label correction
count is minimal within the recipe. The least eligible u minimizes
q for its fixed c,t and current state; no globally optimal N or
support size is claimed. Positive interval gain remains exactly
one per pair, and the same g survives every extension.

## 9. An effective domain test and a hand-verified critical input

The tail estimate (1), before importing the strict H_V hypothesis,
also gives an effective finite test of that hypothesis. For a finite
V of mass one with an independent pair, construct A,lambda,N,Z_0
as in Section2, using only V. For every real z>=Z_0, (1) gives
H_V(z)-z>=1. On (1,Z_0], integer powers give H_V(z)=H_V(ceil z).
Therefore the universal H_V hypothesis is equivalent to the finite
list of exact integer inequalities

    H_V(j)>j,  2<=j<=Z_0.

This bound is very large and is not claimed to be computationally
practical. It is a complete finite reduction, not a no-hit prefix.
No implementation or run of this test is made or authorized here.
A small hand certificate establishes that the theorem has additional
actual inputs, independently of the usefulness of this general bound.

Take

    D={3,4,5,6,7,21},  R={3},  V={4,5,6,7,21}.

Then gcd(D)=1, sigma(R)=1/2, and

    sigma(V)=1/3+1/4+1/5+1/6+1/20=1.

The pair 4,6 is multiplicatively independent. Suppose an integer j>=37
had H_V(j)<=j. Since sigma(V)=1, it would satisfy

    sum_d [p_d(j)-j]/(d-1)<=1,

so 0<=p_4(j)-j<=3 and 0<=p_6(j)-j<=5.
Their difference has absolute value at most 5.
But p_4(j)=4^r and p_6(j)=6^s have r,s>=3 and are both divisible by 8.
They must be equal. This is impossible for positive r,s, because
6^s is divisible by 3 and 4^r is not. Hence H_V(j)>j for j>=37.

For the remaining integers, direct geometric sums give the complete
table below. Within each displayed interval all least powers are
constant. In each row H_V exceeds the upper endpoint.

| Integer j | H_V(j) |
|---|---:|
| 2 through 4 | 5 |
| 5 | 9 |
| 6 | 14 |
| 7 | 20 |
| 8 through 16 | 27 |
| 17 through 21 | 43 |
| 22 through 25 | 64 |
| 26 through 36 | 89 |

Thus H_V(x)>x for every real x>1. This is a hand proof of the
required hypothesis, not a computer search or a separate checkpoint.

This D has total mass exactly 3/2 and is not in CP27's strict domain
under any alternative radix witness. B>=4 is excluded by Section7;
its binary R can only be {4}, of mass 1/3; its only qualifying
ternary R is {3}, whose complement has mass exactly one.
CP22's whole-base correction criterion also fails: removing any
nonempty correction base set from this mass-one complement leaves
mass strictly below one. The earlier accepted whole-set mass bounds
are larger than 3/2, and the minimum-four results do not apply to
this D. The minimum-four complement itself has mass one, not the
strict mass required by CP26 or a removable mass-one core for CP25.

The historical source boundary matters. BEGL1996,
DOI10.4064/aa-77-2-133-138, Section3 already gives cutoff-one
completeness of {3,4,5}, which is a subset of this D. No novelty is
claimed for this example at k=1,F empty. That printed small-set
result does not state every positive cutoff or finite deletion.
The added local coverage here is the all-k, finite-deletion
conclusion outside the earlier accepted structural criteria.
No exhaustive global novelty or publication-priority claim follows.

## 10. Entry outcome and remaining objective

The entry order is amplification, quantitative and exact all-scale
preservation, fixed gap, actual sign-controlled period recurrence,
fresh lattice, seed and repeated extension, and seed-class/domain
limits. Sections1--5 precede the seed in Section8. Both exact
assertions(P) and(R) are proved by the analytical candidate, including
the originally specified tolerance, growth and dependencies of Q_0.
No paid amplification or preservation assertion remains open in this
candidate, and no failure signal fires.

The admitted claim and stage are unchanged. The candidate supports
direction true and mode construction. Its cost ledger is empty:
no quantifier, scope, object, computability requirement or requested
bound has been given up. Only one step3 application has been used.

The original mass-one objective, the mixed-base half-mass signed-unit
question, the automatic H_V hypothesis beyond this criterion, and
the complement obligation56 and root bridge57 remain open. The
finite test and example are parts of this same structural result,
not additional CPs or budget-renewal claims.

Independent exact-result review, immutable evidence acceptance and
local cash-out remain required. This is an analytical proof candidate,
not a Lean-kernel check, executed certificate, accepted CP or root
closure. The only external theorem inputs are the precisely selected
Gouillon corollary and classical simultaneous Dirichlet statement.
The elementary CP27 lattice and interval interfaces are reproved here.
