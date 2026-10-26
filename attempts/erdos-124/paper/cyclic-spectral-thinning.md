# Cyclic spectral thinning of labelled power supplies

Date: 2026-09-08. Unit1, node-000019. Analytical draft.
Frozen result: checkpoint-000025; independent acceptance and evaluation pending.
The original Erdos124 objective remains open.

## Abstract

We construct an explicit cyclic subsequence of individual powers whose
complement retains a gap bound fixed before any removal. Bounded selected
exponent gaps exclude every nontrivial character. Sequential spectral
averaging and Griesmer's sumset theorem then give intervals of every finite
length in the legal subset sums after each cutoff and finite deletion,
under the removable-core gcd-one hypothesis. Eventual completeness is
not asserted.

## Evidence

The full argument below is Sections 1--8 of the closing proof artifact
296ffdccd5bc5bf4f872201a3f6150b60ed4f820c19b8c2acbb95f61982732ee,
bound by manifest
73f908145b8601b3f44dc351f0ac5330620a8e315aefc7e4eaba6484c336cb1e.
The local full-proof label refers only to the exact node claim.
No mathematical program, formal proof or runtime bound is supplied.

## 1. Exact claim and notation

For every nonempty finite set D of distinct integers at least 4, write sigma(D)=sum_{d in D}1/(d-1) and H={h in D:sigma(D minus {h})>=1}; if H is nonempty with gcd(H)=1, then for every integer k>=1 and finite set F of labels (d,j) with d in D and j>=k, there is an explicitly recursive infinite sequence Q of distinct remaining labels, strictly increasing in numerical value q_i, whose complement R has finite subset sums with all consecutive gaps at most g=ceil(sum_{d in D}d^k/(d-1)+sum_{(d,j) in F}d^j), such that every h in H occurs infinitely often in Q with bounded gaps between its selected exponents and sum_i ||beta q_i||^2=infinity for every beta in R/Z other than zero; moreover for every integer L>=1 the finite subset sums of all remaining labels contain L consecutive integers, with a terminating witness procedure and each label used at most once.

Let P be the set of all labels (d,j) with d in D and j>=k, outside F.
The value of a label is d^j. A numerical coincidence does not identify
two labels. For a label supply A, FS_0(A) denotes its numerical finite
subset sums, including the empty sum 0. Each individual representation
uses each label at most once; supports for different represented integers
need not be mutually disjoint.

Fix one input D,k,F satisfying the claim. Put

    C = sum_{d in D} d^k/(d-1) + sum_{(d,j) in F} d^j,
    g = ceil(C),    s = |H|,    M = max H,
    B = 2 M(M-1).

These constants are chosen before any label is removed into Q.
They are finite, C>0, and g is a positive integer. Fix an ordering
h_1,...,h_s of H and repeat it cyclically, so h_{i+s}=h_i.

The proof constructs Q directly. R is its complement in P. It does
not construct a finite unit-switch family and then increase the
complement gap to pay for that family's support.

## 2. The extension operation and its preservation lemma

Start with W_0=0. Given a selected prefix of total value W_{i-1},
let q_i=h_i^{e_i} be the least power of h_i strictly greater than

    (h_i-1)(C+W_{i-1}),                                    (1)

and set W_i=W_{i-1}+q_i. The selected label is (h_i,e_i).

A least such power exists by unbounded growth of the positive integer
powers of h_i. Since C>=h_i^k/(h_i-1), the threshold in (1) is at least
h_i^k. Thus e_i>=k+1. Also q_i>(h_i-1)C>=3C, so it exceeds every
value deleted in F. The selected label is legal.

Because h_i>=4, (1) gives

    q_i > 3(C+W_{i-1}) > W_{i-1}.                           (2)

For i>1 this is strictly greater than q_{i-1}. Thus selected labels
never repeat, their numerical values strictly increase, and q_i tends
to infinity. In particular, no infinite choice or membership oracle
is concealed in this recursion.

Define the positive buffer

    Delta_i = q_i/(h_i-1) - C - W_{i-1} > 0.                (3)

Let T be the least common multiple of the positive integers d-1 for
d in D. Each term in (3) belongs to (1/T)Z, so

    Delta_i >= 1/T.                                       (4)

The absolute buffer does not tend to zero under iteration. We make
no assertion about its ratio to the exponentially growing support weight.

We next prove that every finite prefix of this operation, and its
infinite limit, preserves the same gap bound g.

### 2.1 Geometric prefix estimate

For d>=2 and x>0,

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1).                 (5)

If x<=d^k, the sum is zero and the right side is nonpositive. Otherwise
let d^J be the largest power strictly below x. The sum is
(d^{J+1}-d^k)/(d-1), and d^{J+1}>=x. This includes equality when x itself
is a power. The estimate always counts strictly smaller values.

Let R_t be P with the first t selected labels removed, and let R be
P with every selected label removed. For either supply, consider its
total value at labels strictly below x.

If x<q_1, none of the selected labels has value below x. Summing (5)
and subtracting the total weight of F gives a lower bound

    sigma(D)x-C >= x-C,                                   (6)

since a nonempty H implies sigma(D)>1.

If x>=q_1, let i be the largest selected index with q_i<=x
among the labels removed from the supply being considered. For R_t
this index exists and is at most t when t>=1. For R it is finite
because q_i tends to infinity. Write h=h_i.

Use the following subcollection of original, not-yet-deleted labels:

- every label of a base d in D minus {h} whose value is strictly below x;
- every label of base h whose value is strictly below q_i.

The two parts are disjoint by base. The second part is contained in the
strict x-prefix even when x=q_i. Its total value before deletions is

    (q_i-h^k)/(h-1).

Estimate the first part by (5). Subtract the total weight of F and
the entire weight W_{i-1} of earlier selections. This may subtract
labels absent from the chosen subcollection, which only weakens a
lower bound. The current selected label (h,e_i) is not in that
subcollection. Any later removed selection has value greater than x;
selections beyond t are not removed from R_t.

The remaining strict-prefix value is therefore at least

    sigma(D minus {h}) x + q_i/(h-1) - C - W_{i-1}
      >= x + Delta_i
      > x,                                                (7)

because h belongs to H. The endpoint sigma(D minus {h})=1 is included.
Coincident values belonging to other bases are not removed merely
because their value equals q_i.

For t=0, (6) follows for every x directly from (5).
Equations (6)--(7) show for every finite t and for the infinite
complement that

    sum_{ell retained, value(ell)<x} value(ell) >= x-C
    for every x>0.                                        (8)

For clarity, the infinite-complement conclusion is not an exchange of
an intersection with FS_0. For each fixed x only finitely many selected
labels have value at most x, and every later selection leaves that
strict prefix unchanged. The same explicit lower-bound argument
therefore applies to the actual infinite complement.

Equation (8) also proves that the retained supply is infinite and its
prefix totals are unbounded. A finite retained supply would have bounded
total value, contradicting (8) as x tends to infinity.

### 2.2 From prefix deficits to a fixed subset-sum gap

List retained labels in nondecreasing numerical order as a_1,a_2,...
and write S_0=0, S_n=sum_{j<=n}a_j. Local finiteness follows from
finiteness of D. At x=a_n, every strictly smaller label precedes a_n,
so (8), including at numerical ties, implies

    a_n-S_{n-1} <= C <= g.                                (9)

The labelled gap lemma from accepted Mass, acceptance-000005, now
gives that FS_0 of the retained supply meets every interval of g
consecutive nonnegative integers. Here is its full elementary argument.

For a finite prefix, let A_n be its subset-sum set. It contains
0 and S_n, and

    A_n = A_{n-1} union (a_n+A_{n-1}).

Inductively the gaps within each copy are at most g. If their spans
[0,S_{n-1}] and [a_n,a_n+S_{n-1}] are disjoint, the gap between
them is a_n-S_{n-1}<=g. If the spans overlap, a gap in the union
cannot be larger than a gap in a copy: a gap crossing a span endpoint
would contain that endpoint of the union. The first prefix has
a_1<=g by (9). Thus every finite-prefix gap is at most g.

Since S_n tends to infinity, each interval of g nonnegative integers
is reached by some finite prefix and intersects its subset sums.
Consequently all consecutive gaps of FS_0(R_t) and FS_0(R) are
at most the original fixed g. In particular, no g depending on t
has been substituted into the claim.

## 3. Seed, quantitative iteration and selected exponent gaps

The preservation lemma in Section 2 holds for every length of a
selected prefix, including the empty prefix, before any seed search.
The smallest nonempty seed has one selected label. Its least eligible
power q_1 exists as above and has Delta_1>=1/T, so it already has
strictly positive buffer. No nonempty selected prefix has fewer than
one label. This is a computer-free seed construction, not an enumeration.

The operation extends each such prefix by one legal label. Its selected
count increases by one, its buffer remains at least 1/T, and the
complement gap stays bounded by g. We must also prevent spectral
degeneration from excessively sparse selection.

Minimality of q_i in (1), with the preceding power at or below the
threshold, gives

    q_i <= h_i(h_i-1)(C+W_{i-1}).                          (10)

By (1) at the preceding stage,

    C+W_i = C+W_{i-1}+q_i
           < q_i/(h_i-1)+q_i
           <= (4/3)q_i.

Applying (10) to i+1 yields

    q_{i+1} < (4/3) M(M-1)q_i <= B q_i.                   (11)

Thus one full cycle satisfies q_{i+s}/q_i <= B^s.
For each h in H, let E_h be the least positive integer with

    h^{E_h} >= B^s.

Successive selected powers of this same h are s indices apart.
If their exponents are e and e', then

    h^{e'-e} = q_{i+s}/q_i <= B^s <= h^{E_h},

hence 1<=e'-e<=E_h. Every h occurs once in each cycle, so it occurs
infinitely often and has the required bounded selected exponent gaps.
The bounds E_h even depend only on the fixed set H, not on k,F.
No uniform Fourier decay rate is inferred from this observation.

The least-power choice in (1) is optimal for the current one-step
buffer test: every smaller power fails its strict inequality. This
does not assert global minimality of the partition or of interval
witnesses. Larger choices may preserve the gap estimate but lose
(10); arbitrary sparse extraction is therefore not an equivalent method.

## 4. Every nontrivial character has divergent square mass

Write ||x|| for distance from a real number to the nearest integer.
Suppose beta in R/Z satisfies ||beta q_i|| -> 0.

Fix h in H. For each sufficiently large integer j, take the largest
selected exponent e<=j of base h. The next selected exponent is at
most E_h larger. Therefore

    ||beta h^j|| <= h^{j-e} ||beta h^e||
                 <= h^{E_h} ||beta h^e|| -> 0.             (12)

The selected index used in (12) tends to infinity with j. This
establishes convergence for all powers of h, not just for the selected
ones.

Choose a real representative of beta and nearest integers z_j to
beta h^j. Let epsilon_j=beta h^j-z_j, so epsilon_j tends to zero.
The integers

    z_{j+1}-h z_j = h epsilon_j-epsilon_{j+1}

tend to zero and are eventually zero. Hence eventually
epsilon_{j+1}=h epsilon_j. Since h>1 and these errors tend to zero,
epsilon_j must be zero for every sufficiently large j. Thus beta h^J
is an integer for some J, separately for every h in H.

One h makes beta rational. Write beta=a/b in lowest terms with b>=1.
The preceding conclusion says that b divides a power of every h in H.
Every prime factor of b would divide every h, contradicting gcd(H)=1.
Thus b=1 and beta is zero in R/Z.

We have proved that for every beta!=0, the norms ||beta q_i|| do not
tend to zero. Equivalently, some epsilon>0 is attained as a lower bound
at infinitely many indices. It follows immediately that

    sum_i ||beta q_i||^2 = infinity                        (13)

for every beta!=0, rational or irrational. The same single Q works
for all beta. We do not claim one positive epsilon for all characters.

## 5. The full Fourier-Stieltjes mean on FS_0(Q)

We use the mechanism proved in accepted CP24, acceptance-000011,
and repeat its exact adaptation to this sequence.

The primary reference is John T. Griesmer, Discrete sumsets with one
large summand, arXiv:2507.10512v1,
https://arxiv.org/pdf/2507.10512v1. Definition 3.4 uses FS-mean to
mean Fourier-Stieltjes averaging of unitary matrix coefficients to
the invariant projection. It does not mean finite-sum closure.
Lemmas 9.5(ii) and 10.3 supply the interface below.

For n>=1 define the finitely supported probability measure on Z

    mu_n = 2^{-n} sum_{epsilon in {0,1}^n}
                       delta_{sum_{i<=n}epsilon_i q_i}.

This counts label choices. If distinct choices have equal numerical
sums their probabilities add, rather than deleting choices. In
particular mu_n(FS_0(Q))=1.

For chi_beta(x)=exp(2 pi i beta x),

    integral chi_beta d mu_n
      = product_{i<=n}(1+exp(2 pi i beta q_i))/2.

Each factor has absolute value |cos(pi beta q_i)|<=1.
Section 4 gives infinitely many factors bounded above by a constant
strictly below one at each beta!=0. Thus these character integrals
tend to zero for beta!=0, and equal one at beta=0.

Let rho be any positive finite Radon measure on R/Z, and set
rho_hat(x)=integral chi_beta(x) d rho(beta). Finite support of mu_n
allows interchange of the integrals. Sequential dominated convergence,
with integrands bounded in absolute value by one, gives

    lim_n integral rho_hat d mu_n = rho({0}).              (14)

Now, and only now, take a weak-star cluster point eta of the sequence
of means mu_n along n tending to infinity. Compactness of the space
of means supplies it. Equation (14) passes to eta for every rho,
and eta(FS_0(Q))=1. Griesmer's Lemma 9.5(ii) identifies eta as a full
FS-mean.

Dominated convergence was used on the original sequence of countably
additive measures, not on a subnet of finitely additive means.
We do not assume that annihilating all nontrivial characters alone
makes an arbitrary mean an FS-mean; Griesmer's Question 10.5 concerns
that different assertion. Nor do we assert that eta is translation
invariant on every bounded function.

## 6. Legal intervals on the full remaining supply

Set X=FS_0(R) and Y=FS_0(Q), as numerical subsets of Z.
Section 2 shows that X is g-syndetic on the nonnegative integers.
Averages on {0,...,n-1} therefore give X mass at least
floor(n/g)/n. A weak-star cluster point of these averages is
translation invariant, because translation by any fixed integer
changes at most twice its absolute value of the averaged positions.
It assigns X mass at least 1/g. Thus X has positive upper Banach density.

Griesmer's Observation 1.3 supplies an extreme invariant mean nu
with nu(X)>0. The exact imported sumset theorem, Corollary 4.2(ii), is:

If X,Y are subsets of a discrete abelian group, nu is an extreme
invariant mean, eta is an FS-mean, and nu(X)+eta(Y)>1, then
nu(X+Y)=1.

Our eta satisfies eta(Y)=1, so this hypothesis holds. Hence
nu(X+Y)=1. For every positive integer L, the intersection of
(X+Y)-j for j=0,...,L-1 has mean one: its complement is a finite
union of sets of mean zero. The intersection is nonempty. Since
X+Y is nonnegative, this gives u>=0 with

    {u,u+1,...,u+L-1} contained in X+Y.                    (15)

Every representation from X uses labels of R and every representation
from Y uses labels of Q. Those supplies are disjoint by construction,
so their finite supports can be united legally even at numerical
coincidences. In fact X+Y=FS_0(P). Equation (15) proves the interval
assertion for every L.

The published sumset theorem is an explicit trusted literature input.
Its full underlying Theorem 3.17 proof has not been independently
reproved in this investigation. The exact version and targeted reading
boundaries are recorded in the inherited CP24 source packet. This is
an analytical proof candidate, not a claimed Lean-kernel verification.

## 7. Terminating procedures and exact scope

The recursive Q is computable from the finite input D,k,F by repeated
integer multiplication and rational comparisons in (1). To decide
whether a given legal label belongs to Q, generate selections until
their increasing values exceed that label's value and inspect the
finitely many earlier selected labels. This terminates by (2).
It also gives a procedure enumerating R.

For an interval witness of specified positive length L, enumerate
the original remaining labels P by numerical value, breaking ties
by a fixed base order. At each finite prefix, list all its labelled
subsets and their sums, keeping one explicit support for each sum.
Check whether they contain L consecutive integers; when they do,
return the interval and those finite supports. Fixed lexicographic
orders can make every choice deterministic.

This describes a procedure but does not execute one. Each stage is
finite. By (15), some interval has a finite support for each of its
finitely many integers. Their union is finite, so all those supports
occur in a sufficiently long prefix of P. The procedure therefore
terminates for every input in the claim. No bound on its running
time, exponent height, or memory usage is asserted.

The construction also clarifies its limitations. The prefix argument
(7) specifically uses sigma(D minus {h})>=1 for the base of the most
recent selection. It establishes nothing for an empty H. If all
active bases shared a prime p, all selected powers would be divisible
by p, so beta=1/p would make every selected norm zero. Collective
gcd one is necessary for this particular active-base spectral scheme.
These statements limit the scheme, not all possible representations
outside its hypotheses.

As an immediate sufficient condition, if m=min D>=4, gcd(D)=1 and

    sigma(D) >= 1 + 1/(m-1),

then for every h in D,

    sigma(D minus {h}) = sigma(D)-1/(h-1) >= 1.

Thus H=D and the theorem applies, including equality. It gives
all-tail thickness and the explicit partition, not eventual
completeness. This is a consequence of the admitted criterion,
not a separately counted checkpoint or an optimality claim.

An interval of length two also gives a legal signed unit: take supports
for u+1 and u, cancel their common labels, and subtract the remaining
sums. This explains the proposed contribution to obligation28.
Its complementary half-mass obligation47 and exact bridge48 still
require their own controller acceptance. In particular, arbitrary
half-mass signed units, T_4=1 and the original mass-one completeness
claim are not proved here.

## 8. Entry outcome, costs and verification boundary

The amplification lemma was established before the positive seed:
Section 2 proves the finite-prefix and infinite-complement invariant;
Section 3 constructs its smallest nonempty seed and quantifies growth
and exponent spacing. Minimality and limitations of the seed rule are
recorded there and in Section 7. Sections 4--7 establish every remaining
spectral, interval and procedural assertion of the admitted claim.

The extension increases the selected count without diluting its absolute
positive buffer or changing g. It never relies on a finite unit family's
normalized gain or on an eventually sufficient support charge.

This is a closing analytical candidate for node19 only. The original
claim, stage and quantifiers are unchanged. The argument justifies
direction true and mode construction. No local amplification hypothesis
remains unpaid, so the closing move has an empty cost ledger. No
constructivity, uniformity required by the claim, or extra axiom is lost.

Independent result review, frozen evidence audit and controller acceptance
are still required. The argument supplies no formal proof, exhaustive
novelty finding, priority claim, resource renewal or root closure.


## Reference identifiers

John T. Griesmer, Discrete sumsets with one large summand,
arXiv:2507.10512v1, https://arxiv.org/pdf/2507.10512v1.
The exact cited interfaces are named in Sections 5--6 above.
The full main sumset theorem remains a trusted literature input.

The local CP24 reference is acceptance-000011 and manifest
c34b753e9129af8fd6fc65f54ef85887cee309ab7dddb872749b1aaa9d8c574a.
The local Mass reference is acceptance-000005 and manifest
49c309e171825be70b3a3c683d9154b0d2871e2e0c22c82a36fcf628ec706d53.
These are local evidence identifiers, not external publication claims.
The elementary gap lemma is re-proved in full here.

The adjacent novelty.md records the repeated bounded query check and
position.md distinguishes this result from the full original objective.
