# Move 2: a two-supply reciprocal-mass rung

Node: node-000018. Strategy: ladder-the-parameter, plan step4.
Entry: prove-the-subcritical-or-asymptotic-version-first, Actions1-2.
Reservation: revision331, move-node-000018-2, account-000002.
Status: analytical proof candidate, pending independent result review.
No mathematical program, sample enumeration or formal checker was run.

## 1. Exact rung

For every nonempty finite set D of distinct integers at least 4 with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=b(m)=2+1/(m-1)+(floor(log_2(m))+1)/m, every integer k>=1 and every finite set F of labels (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N is a sum of finitely many remaining labelled occurrences d^j, each pair used at most once and coincident numerical values retained separately; moreover b(m)<=37/12 for every integer m>=4 and b(m) tends to 2 as m tends to infinity.

This is obligation-000041. It is not the admitted full threshold claim
T_4=1, and it does not cover every original input with reciprocal mass
at least one. The exact open passage is given in Section8.

For a base set A and fixed k,F, let P_A be the labels (d,j) with d in A,
j>=k, outside F. Let S_A be their numerical finite-subset-sum set,
including zero. A sum uses each label at most once. Independent labels
may have identical values. A base partition gives disjoint label supplies,
even when its numerical sumsets intersect.

## 2. Primary input and accepted dependencies

We use the pinned version of John T. Griesmer, Discrete sumsets with one
large summand, arXiv:2507.10512v1, https://arxiv.org/pdf/2507.10512v1.

The exact imported assertion, Corollary4.2(ii), is:

If X,Y are subsets of a discrete abelian group, nu is an extreme invariant
mean, eta is an FS-mean, and nu(X)+eta(Y)>1, then nu(X+Y)=1.
In particular X+Y is thick.

Here an FS-mean has the Fourier-Stieltjes meaning of Definition3.4:
it averages every unitary matrix coefficient to the invariant projection.
It does not mean merely a mean on a finite-sum set.

The proof below verifies this condition using Lemma10.3 and
Lemma9.5(ii). Observation1.3 supplies an extreme invariant mean attaining
upper Banach density. The source's Section1.2 supplies weak-star compactness
of means. We justify the elementary density and thickness steps explicitly.

The primary theorem is imported as a published mathematical result, not
reproved here. The full source's proof of Theorem3.17 has not been independently
verified in this investigation. The relevant reading boundaries, exact version
and proposal-bound text copy are in [PRIMARY_READS](../study/PRIMARY_READS.md).
The retained [source text](../../../sources/griesmer2507.10512v1.txt) and
[PDF](../../../sources/griesmer2507.10512v1.pdf) give the original context.

We also use accepted [Mass](../../erdos-124-mass-partition/moves/001-high-mass-completeness.md),
checkpoint16, acceptance5, for the labelled gap and amplification lemmas.
Its nonzero-multiplier argument is repeated below at the exact smaller-supply
scope. Its proof, not merely its old numerical threshold, is the dependency.
The gcd-descent construction follows accepted
[Core](../../erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md);
the logarithmic estimate needed here is proved in full in Section5.

## 3. An FS-mean supported on a gcd-one power supply

Let A be any nonempty finite base set with gcd(A)=1 and bases at least two.
There is no reciprocal-mass hypothesis in this section. Fix a positive k
and a finite deletion F. Enumerate the remaining labels of P_A as
ell_1,ell_2,..., with values v_i. For example, order by value and break ties
by a fixed base/exponent order. Every remaining label appears.

### 3.1 Nonconvergence at every nonzero character

For beta in R/Z, suppose ||beta v_i|| tends to zero. Each base d in A
retains all its sufficiently late powers, so ||beta d^j|| tends to zero.

Choose a real representative of beta, nearest integers z_j to beta d^j,
and errors e_j=beta d^j-z_j tending to zero. The integers

    z_{j+1}-d z_j = d e_j-e_{j+1}

tend to zero, so eventually z_{j+1}=d z_j and e_{j+1}=d e_j.
Since d>=2, convergence e_j->0 forces e_j=0 at every sufficiently large j.
Thus beta d^J is an integer for some J depending on d.

One base already makes beta rational. Write beta=a/b in lowest terms,
b>=1. For each d in A, b divides a power of d. A prime dividing b would
therefore divide every d in A, contradicting gcd(A)=1. Hence b=1 and
beta=0 in R/Z.

Consequently, for every beta!=0, there is epsilon in (0,1/2] such that
||beta v_i||>=epsilon for infinitely many i. This assertion persists after
the arbitrary fixed finite deletion. No common uniform epsilon over beta
or over A is asserted.

### 3.2 Sequential Bernoulli averages and their characters

For each positive integer n, define a finitely supported probability
measure on Z by

    mu_n = 2^{-n} sum_{epsilon in {0,1}^n}
                     delta_{sum_{i=1}^n epsilon_i v_i}.

This measure counts label choices. If different choices give the same
integer, their probabilities add. It never reuses a label. In particular
mu_n(S_A)=1.

For the character chi_beta(x)=exp(2 pi i beta x), independence gives

    integral chi_beta d mu_n
      = product_{i=1}^n (1+exp(2 pi i beta v_i))/2.

The absolute value of the i-th factor is |cos(pi beta v_i)|.
For beta!=0, Section3.1 gives infinitely many factors at most
cos(pi epsilon)<1, while every factor is at most one. The product therefore
tends to zero. If epsilon=1/2, one of those factors is already zero.
At beta=0 the product is one for every n.

Thus (mu_n) is one sequence of countably additive probability measures
whose integrals tend to zero for every nontrivial character. The sequence
is chosen once from P_A, not separately for each character. There is no
claim of uniform convergence over beta.

### 3.3 The full FS-mean property

Regard mu_n as a mean on ell-infinity(Z), and take a weak-star cluster
point eta along n->infinity. Such a point exists by compactness of the
space of means. Because mu_n(S_A)=1 for all n, eta(S_A)=1.

Let rho be any positive finite Radon measure on the character circle,
and define its Fourier-Stieltjes transform by

    rho_hat(x)=integral chi_beta(x) d rho(beta).

Finite support of mu_n allows the interchange

    integral rho_hat d mu_n
      = integral (integral chi_beta d mu_n) d rho(beta).

The inner integrands have absolute value at most one. The sequential
pointwise limits just proved are zero off beta=0 and one at beta=0.
The dominated convergence theorem gives

    lim_{n->infinity} integral rho_hat d mu_n = rho({0}).

This is exactly the argument and conclusion of Griesmer Lemma10.3.
Every weak-star cluster point eta inherits this already established scalar
limit, for every rho. Thus eta(rho_hat)=rho({0}) for every positive finite
Radon rho. Lemma9.5(ii) implies that eta is an FS-mean in Definition3.4.

The dominated convergence argument was applied to the original SEQUENCE
mu_n, before taking a cluster point. It was not applied to the subnet used
for compactness. We do not assume that an arbitrary finitely additive mean
annihilating characters is an FS-mean; that is the distinct Question10.5
in the source.

We have proved the required full FS-mean, with eta(S_A)=1, for every k,F
on any finite gcd-one base supply A. This fact alone does not prove
positive density or completeness of S_A.

## 4. Two mass-one supplies and a gcd-one averaging supply suffice

Suppose D has a partition into nonempty disjoint base sets A,B,R such that

    gcd(A)=1,    sigma(B)>=1,    sigma(R)>=1.

No lower bound on sigma(A) is required. We prove eventual representation
for every positive k and finite F using only the labels from these groups.

For C equal to B or R, define the finite positive rational

    K_C = sum_{d in C} d^k/(d-1)
          + sum_{(d,j) in F, d in C} d^j.

For every x>0, the geometric-series estimate gives

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1).

Subtracting all deleted values and summing over d shows that the total
available value strictly below x is at least sigma(C)x-K_C.
Thus, in the sorted label enumeration a_i of P_C,

    a_i-sum_{h<i}a_h <= (1-sigma(C))a_i+K_C <= K_C.

This remains valid at tied values because all strictly smaller labels
precede a_i. By the accepted labelled gap lemma, S_C meets every interval
of g_C=ceil(K_C) consecutive nonnegative integers. The lemma follows by
inducting on finite prefixes: their subset-sum sets have endpoints zero
and the prefix total, and adjoining a_i takes the union of that set with
its a_i-translate. The displayed deficit bounds every gap between the two
spans. Overlapping spans create no new larger gap. Prefix totals tend
to infinity, giving the stated infinite interval property.

Let X=S_B as a subset of Z. Uniform averages on {0,...,n-1} give X mass
at least floor(n/g_B)/n. A weak-star cluster point of these averages is
translation invariant, since a fixed translate changes at most2|h|
terms. It gives X mass at least1/g_B>0. Hence X has positive upper
Banach density. By Griesmer Observation1.3 there is an extreme invariant
mean nu with nu(X)>0.

Let Y=S_A. Section3 gives an FS-mean eta with eta(Y)=1. Therefore

    nu(X)+eta(Y)>1.

Corollary4.2(ii) yields nu(X+Y)=1 and thickness of X+Y.
For completeness, full mass of a set S under an invariant mean implies
that the intersection of S-h over any finite set of integer shifts h
has mass one: its complement is a finite union of measure-zero sets.
Taking h=0,...,L-1 gives an interval of L consecutive integers in S.
Here S=X+Y is contained in the nonnegative integers, so its interval
starts at a nonnegative integer.

Take L=g_R. There is an integer u>=0 with

    [u,u+g_R-1] contained in X+Y.

Every integer in this interval has a finite representation on P_A union P_B.
The representations are legal because these two base groups are disjoint.
For n>=u+g_R-1, the interval

    [n-u-g_R+1,n-u]

consists of g_R nonnegative integers and therefore contains some r in S_R.
Now n-r belongs to the represented interval. Its support on P_A union P_B
is disjoint from the finite support representing r on P_R. Their union
represents n, using each label at most once.

This is the accepted disjoint-reserve amplification lemma, with no
finite correction removed from R. It proves the criterion for every k,F.
Numerical coincidences across groups do not affect label disjointness.

## 5. A logarithmic gcd seed and the endpoint allocation

Let D satisfy the rung's hypotheses and put m=min D>=4.
Start A_0={m}, with current gcd g_0=m. While g_i>1, adjoin any element
of D not divisible by g_i, for definiteness the least such element.

It exists because gcd(D)=1. It is not already in A_i, since g_i divides
every element already selected. The new gcd g_{i+1} is a positive proper
divisor of g_i. Therefore g_{i+1}<=g_i/2. The procedure ends at gcd one
after a finite number q of additions. Since

    1=g_q <= m/2^q,

we have q<=floor(log_2(m)). All added bases exceed m, so each has reciprocal
weight at most1/m. Consequently the final set A satisfies

    m in A,   gcd(A)=1,
    sigma(A) <= a(m):=1/(m-1)+floor(log_2(m))/m.

This improves the cardinality estimate needed for this application by
using the divisibility at every descent. No coprime pair or multiplicative
independence is required.

Since b(m)=2+a(m)+1/m and sigma(D)>=b(m), the complement D minus A has mass
at least2+1/m. Add its bases in increasing order until their mass first
reaches one, obtaining B. Such a first crossing exists. Every base outside
A is at least m+1, so its last added weight is at most1/m; the mass before
the crossing is strictly below one. Thus

    1 <= sigma(B) < 1+1/m.

Let R=D minus (A union B). The sets A,B,R are disjoint and

    sigma(R) = sigma(D)-sigma(A)-sigma(B)
             > (2+a(m)+1/m)-a(m)-(1+1/m)
             = 1.

In particular R is nonempty. The strict first-crossing bound preserves
the endpoint sigma(D)=b(m), even if the bound for sigma(A) is attained.

Section4 now applies. This proves the representation assertion for every
D,k,F in the exact rung, including equality at its stated mass threshold.

## 6. Uniform bound and large-minimum limit

Let r=floor(log_2(m)), so r>=2 and 2^r<=m<2^{r+1}. Then

    b(m)-2 = 1/(m-1)+(r+1)/m
            <= c_r:=1/(2^r-1)+(r+1)/2^r.

Both summands of c_r strictly decrease with integer r>=2.
For the second, (r+2)/2^{r+1}<(r+1)/2^r is equivalent to r>0.
Thus c_r<=c_2=1/3+3/4=13/12, proving

    b(m) <= 37/12    for every integer m>=4.

Also c_r->0: the first term tends to zero, and the ratio of successive
second terms is (r+2)/(2(r+1))<=2/3 for r>=2. Since b(m)>2 and r tends
to infinity with m, b(m)->2.

These are exact analytical inequalities, with no finite numerical check.
They complete every assertion of obligation-000041.
In particular the candidate gives T_4<=37/12, conditionally on acceptance
of this analytical proof under the required review standard.

## 7. What improved, and what is not established

The accepted previous sufficient threshold is3+min{1/4,2/m}.
The new b(m) uniformly improves its global minimum-four bound from13/4
to37/12 and changes the leading sufficient mass for large m from3 to2.
It does not follow just by tightening the old three-bin partition: Section3
and Griesmer's FS-mean theorem replace the second density supply itself.

The present b(m) is not claimed optimal. No arbitrary density-to-FS-mean
implication, common-divisor WOC theorem, subunit reserve lemma or
all-input threshold-one assertion was proved. Section3 alone gives neither
syndeticity nor a legal way to add two sums that reuse labels.

There is an exact limitation of this particular base-partition criterion:
its disjoint B,R each have mass at least one, and its nonempty A has
strictly positive mass. Hence every input to that criterion has sigma(D)>2.
No refinement of the gcd seed or crossing overhead alone can make this
criterion apply at sigma(D)<=2. This is not an obstruction to completeness,
to overlapping finite-support methods, or to every use of FS-means.

The representation threshold N(D,k,F)=u+g_R-1 is existential. Its uniform
value, feasible running time and optimality were never required. The mass
bound b(m) and the minimum-base domain m>=4 are explicit, without an
unspecified sufficiently-large-m exception.

## 8. Exact passage to the local and original targets

The remaining local assertion is obligation-000042:

For every nonempty finite set D of distinct integers at least 4 with m=min D, gcd(D)=1 and 1<sigma(D)=sum_{d in D}1/(d-1)<2+1/(m-1)+(floor(log_2(m))+1)/m, every integer k>=1 and every finite set F of labels (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N has a finite representation by remaining labelled occurrences d^j, each pair used at most once and coincident numerical values retained separately.

Together with the proved rung, it implies the all-cutoff/deletion
representation statement for every finite gcd-one minimum-four D with
sigma(D)>1: split into sigma(D)>=b(min D) and sigma(D)<b(min D).

That strict-mass statement is equivalent to T_4=1. In one direction it
implies P_4(t) for every t>1, hence T_4=1 because the infimum is restricted
to t>=1. In the other direction, the set of valid thresholds is nonempty
(the rung already supplies37/12). If its infimum is1 and sigma(D)>1, there
exists a valid threshold t<sigma(D). Applying P_4(t) to this D and the
same k,F proves the required representation. Equality sigma(D)=1 is not
inferred from an infimum.

This proves the implication described by obligation-000043, but does not
prove its sub-rung premise. The controller may not mark either premise
accepted just because this deduction has been written.

For the full original objective, obligation-000044 still covers minimum
three or reciprocal equality. If it were known together with T_4=1,
an arbitrary original input would either satisfy that residual premise,
or have minimum at least four and reciprocal mass greater than one.
The preceding threshold argument, with F empty, would cover the latter.
This explains the root implication obligation-000045, not a proof of its
unresolved premises.

## 9. Walk, costs and evidence boundary

The attacked statement moves to the exact rung while the native claim
remains T_4=1. The rung and the explicitly stated sub-rung remainder give
the deduction back to that native claim. Direction remains true and mode
remains existence. The stage is unchanged.

The move pays object and obligations. It leaves the critical local value
and original minimum-three/equality cases open. It pays no bound_quality:
b(m),37/12 and the limit2 are proved analytically, not estimated numerically.
No effectivity newly required by the claim is surrendered; a uniform or
explicit N was not part of that claim.

All four verification questions from Move1 are answered by Sections3-6.
The entry's third failure signal now applies to the attempted passage:
the weakened theorem relies on two disjoint mass-one supplies, a reason
that cannot survive the target value one. The strategy's current
partition-based ladder therefore ends with this rung and its explicit
remaining obligation. Record native fail for ladder-the-parameter rather
than queue further crossing-constant refinements as a path to one.

The representation conclusion is a theorem candidate until independent
result review and controller acceptance. There is no native closing move:
T_4=1 is not proved or refuted. No local stall, finish, formal verification,
publication or resource renewal follows from this partial result.
