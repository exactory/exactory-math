# Move 1: high-mass labelled pure-power completeness

Node: node-000010. Strategy: make-the-proof-constructive.
Entry: seed-and-amplify. Reservation: controller revision 192.
Status: analytical proof candidate, pending independent result review.
No mathematical process, sample enumeration, or formal checker was run.

## Claim and notation

For every nonempty finite set D of distinct integers at least 3, with
m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=3+2/m, every integer
k>=1 and every finite set F of labelled occurrences (d,j) with d in D
and j>=k, all sufficiently large integers are sums of finitely many
remaining occurrences d^j, each pair (d,j) used at most once. Coincident
numerical values from different pairs remain separately available.

A supply is a countably infinite set of labels with a positive-integer
value on each label, locally finite by value. Its nondecreasing enumeration
is a_1,a_2,..., with ties broken by a fixed label order. Write
S_0=0, S_i=a_1+...+a_i, and FS_0 for finite sums of distinct labels,
including the empty sum. All set additions below concern the numerical
sets of attainable sums. Unions of representations require disjoint
LABEL supports, not different numerical values.

An integer set is g-syndetic on the nonnegative integers if every interval
of g consecutive nonnegative integers meets it. It is syndetic if this
holds for some g, and thick if it contains intervals of every finite
length. Removing or adding zero makes no difference to the use of the
published positive-integer syndetic-set theorem below.

## 1. The amplification lemma and its finite seed

Suppose an infinite reserve R has FS_0(R) g-syndetic, and a disjoint
supply P has all integers in [A,A+g-1] in FS_0(P), where A>=0.
Then every n>=A+g-1 belongs to FS_0(P union R).

Indeed, the interval [n-A-g+1,n-A] consists of g nonnegative integers,
so choose r in it from FS_0(R). Then n-r lies in [A,A+g-1].
The two finite representing supports are disjoint, so their union
represents n legally. This also gives a representation search once a
finite interval certificate and a procedure enumerating R are specified.

Thus a seed of g consecutive sums is sufficient for a g-syndetic
reserve. No smaller universal length follows from this gap information
alone: the reserve set g*N_0 and the seed [0,g-2] miss one residue for
g>=2. This does not claim minimality for a particular power supply.

## 2. A labelled bounded-gap lemma

For a supply a_i, suppose a_i-S_{i-1}<=g for every i, where g is a
positive integer. Then FS_0(a_i) is g-syndetic. In particular, this
conclusion is unchanged in kind by finitely many label deletions.

For completeness, each finite prefix has endpoints 0 and S_i and its
ordered subset sums have consecutive gaps at most g. This is induction.
The first prefix has the required gap a_1<=g. At the next step its
subset-sum set is T union (a_i+T), where T is the previous one.
Each copy has gaps at most g within its closed span. If the two spans
are disjoint, the gap between them is a_i-S_{i-1}<=g. If they overlap,
a gap in their union cannot exceed a gap in one of the copies: a gap
crossing a span endpoint would contain that endpoint. This proves the
induction. The total S_i tends to infinity because the values are positive.
Given an interval of g nonnegative integers, take a prefix whose upper
endpoint is at least the interval's upper endpoint. Its mesh property
and endpoint 0 imply that the interval meets its subset sums.

If finitely many labels of total value W are deleted, the sum of the
remaining preceding terms at any remaining label is at least its old
preceding sum minus W. Thus g+W is a valid bound for the remaining
supply. This argument counts occurrences, including ties.

## 3. The occurrence-preserving three-component criterion

We prove the following form of the finite-correction method.

Let B_1,B_2,C be three disjoint infinite label supplies. Suppose each
has a bounded ordered deficit as in section 2. Suppose also that

    sum_{c in C} ||beta value(c)|| = infinity

for every beta in R/Z other than zero. Then FS_0(B_1 union B_2 union C)
contains every sufficiently large integer.

Here ||x|| denotes distance to the nearest integer. This is the labelled
form of Fan's three-component strong-completeness mechanism. The proof
below establishes the extension, rather than deduplicating the values
and applying a numerical-set theorem.

### 3.1 The published additive input

We use the theorem that the sum of two syndetic subsets of N is
piecewise Bohr. In the form used here, for such numerical sets S_1,S_2,
there exist a finite-dimensional torus T^r, a point theta in it, an
open set U, and a thick set J of positive integers such that

    J intersect {n>=1 : n*theta in U} is nonempty
    and is contained in S_1+S_2.

This is Bergelson-Furstenberg-Weiss, Theorem I, cited and stated as
Lemma 2.12 in Bergelson-Simmons [BS]. We take S_i to be the positive
elements of FS_0(B_i). Section 2 gives their syndeticity (enlarging the
gap constant near zero if necessary). Therefore every number in the
displayed intersection has a representation on B_1 union B_2.
The numerical S_1 and S_2 need not be disjoint. Their representing
label supplies are disjoint, which is exactly what is required.

The remaining compact-group facts used below are the elementary fact
that a nonempty compact subsemigroup of a compact group is a subgroup,
and character separation for closed subgroups of a finite-dimensional
torus: if x is outside a closed subgroup G, some integer character
chi:T^r -> R/Z is zero on G and nonzero at x. The latter is the
closed-subgroup/character description also used in [BS, section 2.1].
These facts are used in ordinary classical mathematics.

### 3.2 Tail sums and the compact group

Enumerate C by labels c_1,c_2,... and put v_i=value(c_i). Let C_{>=t}
denote its tail starting at t, and set

    K = closure{n*theta : n in Z},
    G_t = closure{u*theta : u in FS_0(C_{>=t})},
    G = intersection_{t>=1} G_t.

The G_t are nonempty nested compact sets, so G is nonempty and compact.
They lie in K, hence G is contained in K. For x,y in G and any tail
start t, approximate x by a sum on a finite support beyond t. Then
approximate y by a sum whose support starts beyond that first finite
support. Their union is legal, and approximates x+y. Arbitrarily good
approximations show x+y in G_t for every t, so G is a semigroup.

Here is the compact-semigroup fact in this setting. For x in G,
compactness gives a convergent subsequence n_j*x with increasing
integers n_j separated by at least two. Consequently
(n_{j+1}-n_j-1)*x tends to -x. Each positive multiple belongs to G,
so -x belongs to G. Thus G is a subgroup.

We claim theta belongs to G. Otherwise choose an integer character chi
annihilating G with beta=chi(theta) nonzero in R/Z. Choose signed
representatives b_i in [-1/2,1/2] for beta*v_i. The hypothesis says
sum |b_i| diverges, so either the positive sum or the absolute negative
sum diverges. Fix one of these signs with divergent sum. In every tail
select finitely many terms of that sign, stopping the first time their
absolute sum reaches 1/4. Every summand is at most 1/2, so the resulting
absolute sum lies in [1/4,3/4]. For its corresponding numerical sum u_t,

    ||chi(u_t*theta)|| >= 1/4.

Choose these supports beyond t and take a convergent subsequence of
u_t*theta as t tends to infinity. Its limit lies in each G_t, hence in
G, while continuity gives character norm at least 1/4. This contradicts
chi being zero on G. The claim follows. Since G is a closed subgroup
containing theta, it contains K, and therefore G=K.

In particular, the phases of finite sums from C are dense in K, and
this remains true after any finite initial deletion. This argument
uses occurrence indices throughout. Repeated values cause no problem.

### 3.3 Finite correction support

The nonempty intersection in section 3.1 implies U intersects K.
For any x in K, the relatively open set x-(U intersect K) meets the
dense set of phases of FS_0(C). Hence the translates
u*theta+U, for u in FS_0(C), cover K. Compactness gives a finite
numerical set D_0 contained in FS_0(C) such that these translates for
u in D_0 already cover K.

For each u in D_0 choose one finite labelled representation on C.
Let E be the union of all these finitely many supports, and M=max D_0.
The supports for different u need not be disjoint: only one u is used
in any one representation. E is a finite LABEL set.

The set

    T = {n>M : n-h in J for every integer 0<=h<=M}

is thick. Indeed, sufficiently long intervals in J give arbitrarily
long intervals after trimming M places at their left edge and any
bounded initial portion. For n in T, its phase belongs to K, so some
u in D_0 satisfies (n-u)*theta in U. Also n-u is in J. Section 3.1
represents n-u on B_1 union B_2, and u is represented on E.
These supports are disjoint. Thus FS_0(B_1 union B_2 union E) contains
the thick set T.

Section 2 shows that FS_0(C minus E) is g_E-syndetic for a finite
integer g_E. The thick set just obtained supplies an interval of
g_E consecutive sums. Its representations use B_1,B_2,E, whereas the
reserve uses C minus E. Section 1 proves eventual completeness.
This proves the criterion with no numerical-disjointness assumption.

The finite-support extraction follows [Fan, Lemma 2.2]. The proof
has explicitly justified every place at which labels, tails, or
disjointness enter. The full nonzero-multiplier hypothesis let us use
G=K instead of the finite-coset/modular step of Fan's weaker criterion.

## 4. Partitioning the actual base set

Apply the already accepted minimum-preserving reciprocal-core lemma,
checkpoint-000008 and acceptance-000001, to D. It gives C_D subset D
with m in C_D, gcd(C_D)=1, and

    1 <= sigma(C_D) < 1+1/m.

The candidate's stronger mass hypothesis certainly implies the
lemma's sigma(D)>=1 hypothesis. No power-representation conclusion
is inherited from that lemma.

The mass left outside C_D is strictly greater than 2+1/m. Adjoin those
remaining bases in increasing order until their mass first reaches
one, and call the resulting set B_{1,D}. Such a first crossing exists.
Each added base is different from m and at least m+1, so its reciprocal
weight is at most 1/m. The preceding mass at the crossing is strictly
below one. Therefore

    1 <= sigma(B_{1,D}) < 1+1/m.

Let B_{2,D}=D minus (C_D union B_{1,D}). Then

    sigma(B_{2,D})
      = sigma(D)-sigma(C_D)-sigma(B_{1,D})
      > (3+2/m)-(1+1/m)-(1+1/m)
      = 1.

All three groups are nonempty and are disjoint sets of base LABELS.
Only C_D is required to have gcd one. Both strict upper bounds above
show that the proof includes equality sigma(D)=3+2/m. No pairwise
coprimality or multiplicative independence has been assumed.

## 5. Power supplies after arbitrary cutoff and finite deletion

Fix any k>=1 and finite F as in the claim. For each of the three
base groups A, let P_A be its remaining labels (d,j), j>=k, outside F.
The supplies are infinite, locally finite by value, and disjoint by
label. Coincident values, such as powers arising from dependent bases,
are not removed.

### 5.1 The ordered deficit

For every real x>0 and every d>=3,

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1).

If x<=d^k the left side is zero and the inequality is immediate.
Otherwise let r be the least integer at least k with d^r>=x.
The geometric sum on the left is (d^r-d^k)/(d-1), which gives the
inequality, including when x itself is a power.

Define the computable rational constant

    K_A = sum_{d in A} d^k/(d-1)
          + sum_{(d,j) in F, d in A} d^j.

Summing the geometric bound and subtracting all deleted values gives

    sum_{label in P_A, value(label)<x} value(label)
        >= sigma(A)*x-K_A.

If a_i=x is a label in the sorted supply, every label with value
strictly less than x precedes it. Consequently

    a_i-S_{i-1} <= (1-sigma(A))*a_i+K_A <= K_A,

because sigma(A)>=1. Section 2 applies with g_A=ceil(K_A), a positive
integer. The proof handles ties by a lower bound using the strict
numerical prefix, not by deduplicating equal values. If a further
finite label set E is removed from P_A, ceil(K_A+sum_E value) is a
valid gap constant.

### 5.2 Every nonzero multiplier on the correction supply

We show that no beta in R/Z other than zero can satisfy
||beta value(c_i)|| -> 0 along the correction supply P_{C_D}.
This implies the divergent-series hypothesis of section 3.

First, for an integer d>=2, suppose ||beta*d^j|| tends to zero.
Choose a real representative of beta, nearest integers z_j to
beta*d^j, and errors e_j=beta*d^j-z_j tending to zero. The integers

    z_{j+1}-d*z_j = d*e_j-e_{j+1}

tend to zero, so they are zero for all sufficiently large j. Thus
e_{j+1}=d*e_j eventually. The only such sequence tending to zero
has e_j=0 eventually. Hence beta*d^J is an integer for some J.

A finite deletion F removes only finitely many exponents of each base.
Therefore convergence along P_{C_D} would imply this conclusion for
every d in C_D. From one base, beta is rational. Write it as a/b in
lowest terms with b>=1. For every d in C_D, the conclusion implies
b divides a power of d. If b>1, any prime divisor of b would divide
every d in C_D, contrary to gcd(C_D)=1. Therefore b=1, meaning beta
is zero in R/Z. This contradiction proves the claim.

For beta nonzero the nonnegative norm terms do not even tend to
zero, so their sum is infinite. This supplies exactly the full
multiplier hypothesis used in section 3, for every k and F.

### 5.3 Modular audit

Although section 3 used the stronger full-multiplier condition in
place of a separate modular argument, the correction supply also
has the modular property required by the originally studied weaker
criterion.

Every tail has gcd one: a prime dividing all its values would
divide every base in C_D. Fix q>=1 and enumerate a tail as v_i.
The sets of subset sums of the first t labels in Z/qZ increase and
eventually stabilize to a set S containing zero. For all later i,
S+v_i=S, since S union (S+v_i)=S and translation preserves cardinality.
The stabilizer of S is a subgroup containing every residue in a
further tail. Those residues generate Z/qZ because their integer gcd
is one. Thus S is the entire group. Every residue has a finite
labelled representation; a nonempty zero-residue representation, if
required, follows from two equal partial sums among q+1 consecutive
partial sums. No bounded uniform tail index is asserted.

## 6. Applying amplification and making the search explicit

Sections 4 and 5 verify every hypothesis of section 3 on the
remaining labelled powers. That criterion, whose last step is
section 1's disjoint-support amplification, proves the exact claim
for this arbitrary D,k,F.

There is also a terminating search for a finite certificate and then
for every representation. This is a mathematical procedure, not a
program executed in this attack.

Enumerate the correction supply c_1,c_2,... and let E_t be its first
t labels, allowing t=0. Set

    g_t=ceil(K_{C_D}+sum_{i<=t}value(c_i)).

Dovetail all pairs (t,p). For each, list the finite subset sums on
E_t together with the first p labels of each of the other two
supplies, and test whether they contain g_t consecutive integers.
If they do, record one finite support for every integer in one such
interval [A,A+g_t-1].

This search terminates. Section 3 provides some finite correction
support E_* giving thickness when combined with the two infinite
other supplies. Choose t with E_* contained in E_t. Adding labels
preserves thickness, so an interval of length g_t exists. Its
finitely many representations use finitely many labels of the other
two supplies and are all included for some p. Dovetailing eventually
checks that pair.

The certificate supplies N=A+g_t-1. For any n>=N, enumerate finite
subsets of C minus E_t until finding a sum in
[n-A-g_t+1,n-A]. The proved gap bound guarantees termination, and the
stored seed representation completes n using disjoint labels.
Thus the mode is construction despite the nonquantitative compactness
input. No complexity bound or convenient numerical value of N is
claimed. Finite pruning of seed supports may remove redundant labels
while preserving the certified interval; optimality is not asserted.

The three-way partition is sufficient, not claimed necessary.
This argument does not produce a partition or a completeness proof
throughout the complementary mass range.

## 7. Entry, quantifier, cost, and source audit

The amplification and required seed length were established first.
The finite-correction lemma proves the seed's existence without a
bounded mathematical run; the base partition is constructed by
finite symbolic selection. The final procedure has proved termination.
The seed operation never reuses a label, and its covering gain is
not lost by iteration. The entry's failure signal does not fire.
The target is feasibility, so the strategy's extremal optimization
step and forcing branch do not apply.

Direction becomes true and mode becomes construction. The admitted
claim, stage, and all input quantifiers remain unchanged. All local
amplification obligations have been discharged, so the closing
move's ledger is empty under CASHOUT.md. This does not assert
independent acceptance or a formal proof.

The statement covers arbitrary finite D, every positive k, all finite
labelled F, and the inclusive high-mass endpoint. It is unconditional
relative to the cited established mathematical results in classical
mathematics. It promises only N(D,k,F), not a uniform bound.

The original threshold-one objective is not proved. In the proposed
root route, this result applies with F empty only to the high-mass
premise, obligation-000016. The complementary premise and implication
bridge remain separate obligations.

Primary mathematical sources and exact uses:

- [BS] V. Bergelson and D. Simmons, New examples of complete sets, with
  connections to a Diophantine theorem of Furstenberg,
  arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016. Lemma 2.12 supplies
  the piecewise-Bohr sumset theorem, attributed there to
  Bergelson-Furstenberg-Weiss, Theorem I. Section 2.1 records the
  compact-group method and the relevant closed-subgroup facts.
  Local text: sources/bergelson-simmons.txt at the research root.
- [Fan] Steve Fan, Strongly complete sets and a conjecture of Erdos,
  arXiv:2607.14071v3, https://arxiv.org/html/2607.14071v3.
  Lemma 2.2 supplies the finite-correction idea, and Corollaries 2.3
  and 2.5 its numerical-set applications. They are not cited as
  directly applicable to overlapping occurrence supplies.
- Inherited local lemma: checkpoint-000008, acceptance-000001,
  erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md.

The exact new quantitative application was studied before execution.
The general completeness engine is existing mathematics. This proof
does not claim publication-level novelty for its corollary.

