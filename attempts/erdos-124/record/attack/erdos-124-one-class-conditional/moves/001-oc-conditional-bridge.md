# Move 1: the one-class conditional high-mass theorem

Node: node-000017. Strategy: work-conditionally-then-discharge.
Entry: condition-on-the-one-missing-input, Action 1.
Reservation: controller revision 310.
Status: analytical conditional proof candidate, not accepted evidence.
No mathematical program or formal checker was run.

## 1. Exact hypothesis and conclusion

Write sigma(A)=sum_{d in A}1/(d-1). A label is an ordered pair (d,j),
with value d^j. FS_0 denotes the numerical finite-subset-sum set of a
specified label supply, including zero. Every representation uses each
label at most once. Distinct labels of equal value remain available.

The standing hypothesis OC is:

For every nonempty finite set E of distinct integers at least 3 with sigma(E)=sum_{d in E}1/(d-1)>=1, every integer k>=1 and every finite deletion F of labels (d,j), d in E and j>=k, there exist an integer r>=1, theta in (R/Z)^r, an open set U in (R/Z)^r meeting K=closure{n*theta:n in Z}, and a set J of positive integers containing intervals of every finite length, such that every n in J with n*theta in U can be written as sum_{(d,j) in H}d^j for some nonempty finite set H of remaining labels.

The conditional conclusion is the admitted claim verbatim:

For every nonempty finite set D of distinct integers at least 3 with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=2+min{1/8,1/m}, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

This file proves OC implies that conclusion. It does not assert OC.
In particular the unconditional claim, obligation-000035, stays open.

## 2. Exact inherited core allocation

We use the following accepted local evidence, with paths relative to the
attack root:

- Core: acceptance-000001, checkpoint-000008,
  erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md.
- Mass: acceptance-000005, checkpoint-000016,
  erdos-124-mass-partition/moves/001-high-mass-completeness.md.
- Quarter: acceptance-000006, checkpoint-000017,
  erdos-124-quarter-mass/moves/001-quarter-mass-completeness.md.

These dependencies concern intermediate lemmas, not a substitution of the
old final mass threshold. Checkpoint-000022 is logical lineage only.

Fix an input D,k,F of the admitted conclusion, and put
delta=min{1/8,1/m}. There is a subset C of D containing m, with

    gcd(C)=1,        1 <= sigma(C) < 1+delta.                (1)

For m<=8 use Quarter, Section 2, which gives mass below 9/8.
Here delta=1/8. For m>=8 use Core, which gives mass below 1+1/m.
Here delta=1/m. Either argument works at m=8. This choice does not
require one core to satisfy two independently chosen constructions.

Put E=D minus C. Since the hypothesis includes sigma(D)>=2+delta,
the strict upper bound in (1) gives

    sigma(E)=sigma(D)-sigma(C) > (2+delta)-(1+delta)=1.      (2)

Thus E is nonempty. It consists of bases distinct from m, so every
base of E is at least m+1>=4. In this first application we only need
that its bases are at least three and its mass is at least one.
The strict inequality proves that equality at the target threshold
is included. No pairwise coprimality or multiplicative independence
has entered the allocation.

Let P_C and P_E be the labels of their respective base groups at
exponents j>=k after the deletion F. They are infinite, locally finite
by value, and disjoint by labels. They can have overlapping numerical
values without any identification of their occurrences.

## 3. What the accepted correction supply provides

Sections 2 and 5.1 of Mass imply that FS_0(P_C) has bounded gaps
and that the same holds after any additional finite label deletion.
More explicitly, set

    B_C = sum_{d in C} d^k/(d-1)
          + sum_{(d,j) in F, d in C} d^j.

At a value x, the sum of the surviving C labels with value strictly
below x is at least sigma(C)*x-B_C. This follows from

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1).

Hence a label of value a_i in the sorted supply has
a_i-S_{i-1}<=B_C. Ties only add possible earlier labels, so they do
not spoil this inequality. A finite prefix and its translate by the
next label have consecutive subset-sum gaps at most ceil(B_C);
induction and unbounded prefix sums imply syndeticity on N_0.
After deleting a finite label set L from P_C, the positive integer

    g_L = ceil(B_C + sum_{ell in L} value(ell))             (3)

is a valid gap bound. Thus every interval of g_L consecutive
nonnegative integers meets FS_0(P_C minus L).

Sections 3.2 and 5.2 of Mass also give the following fact for every
finite-dimensional torus and every theta in it:

    {u*theta : u in FS_0(P_C)} is dense in
    K=closure{n*theta:n in Z}.                             (4)

Here is the input audit. If ||beta*d^j|| tends to zero, nearest-integer
errors satisfy e_{j+1}=d*e_j eventually, because
d*e_j-e_{j+1} is an integer tending to zero. Therefore e_j is eventually
zero, and beta*d^J is an integer. If the norms tended to zero along
all of P_C for a nonzero beta, this would hold for every d in C.
Writing beta as a reduced rational shows every prime in its
denominator divides every d in C, contradicting gcd(C)=1. Thus

    sum_{ell in P_C} ||beta*value(ell)|| = infinity

for every nonzero beta in R/Z, unchanged by finite label deletions.
The compact-group tail-sum argument of Mass, Section 3.2, then gives
(4). It forms the intersection of the closures of all tail sum phases,
uses disjoint finite supports to prove closure under addition, and
separates a proper closed subgroup by an integer character. A divergent
positive or negative signed norm subseries supplies tail sums whose
character norms are at least 1/4, contradicting annihilation of that
intersection. This argument applies to an arbitrary orbit closure K,
not just to a dense orbit in the whole torus.

## 4. Apply OC once and fix the finite corrections

Apply OC to the base set E, the original positive cutoff k, and
F restricted to E. By (2) its hypotheses hold. Obtain r,theta,U,J with

    U intersect K nonempty,
    J intersect {n>=1:n*theta in U} contained in FS_0(P_E). (5)

The representing supports in (5) are nonempty, as in OC.
We do not assert that this Bohr intersection is thick.

By (4), for every x in K the nonempty relatively open set
x-(U intersect K) meets the phases of FS_0(P_C).
Consequently the open sets u*theta+U, for u in FS_0(P_C),
cover K. Compactness gives a nonempty finite set V of such sums
whose translates already cover K.

For each u in V choose one finite label support L_u in P_C
representing u, and let

    L = union_{u in V} L_u,        M = max V.

The supports L_u may overlap each other. Only one of them is used
in any one final representation. L is finite and M is a nonnegative
integer. This fixes all correction labels before the remaining reserve
gap is chosen.

Consider

    T={n in N : n>M and n-h in J for every integer 0<=h<=M}.

T is thick towards positive infinity. For any requested finite length,
take a sufficiently long interval in the positive thick set J, remove
M positions from its left edge, and, if needed, remove its bounded
initial portion at most M. The remaining interval has the requested
length when the original interval was sufficiently long.

For n in T, choose u in V such that n*theta belongs to u*theta+U.
Then n-u is positive, belongs to J, and has phase in U. By (5) it is
represented on P_E. The chosen representation of u uses L_u subset L.
The base groups are disjoint, so joining these supports is legal.
Therefore

    T contained in FS_0(P_E union L).                     (6)

## 5. Fix the reserve gap and amplify

Only now let g=g_L be the gap bound (3) for P_C minus L.
By (6) choose an interval [A,A+g-1], A>=1, all of whose integers
are represented on P_E union L.

For n>=A+g-1, the interval [n-A-g+1,n-A] has g nonnegative
integers and meets FS_0(P_C minus L). Choose such a represented r.
Then n-r belongs to [A,A+g-1]. Its representation uses P_E union L,
whereas r uses P_C minus L. Their supports are disjoint, so their
union represents n using only surviving labels of D at exponents j>=k.

This proves the exact conditional conclusion, with N=A+g-1.
The dependence of N on D,k,F and the existential OC witnesses is
allowed. No bound uniform over those inputs was claimed.

## 6. Accounting and remaining obligations

The selected entry's Action 1 has produced the implication at the
exact admitted threshold. Its conclusion is not weakened, so no
bound_quality cost is paid. The object cost records that the proved
statement is an implication, and the obligations cost records that
OC is a standing unresolved hypothesis. OC is a statement inside
ordinary classical mathematics, not an additional set-theoretic axiom.

No entry failure signal has fired: no equivalence with the target,
weaker conditional conclusion, or proved obstruction to the restricted
input has been established. The next admitted application must trace
which form of OC was actually used. The unconditional node and the
full original objective remain open. This candidate has not yet
received independent result acceptance.
