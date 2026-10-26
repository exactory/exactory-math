# Move 1: phase-aware spectral thinning at every strict mass

Node: node-000020. Strategy: make-the-proof-constructive, plan step 3.
Entry: seed-and-amplify. Reservation: revision373, move-node-000020-1.
Status: analytical proof candidate, pending independent result review.
No mathematical program, finite enumeration or formal checker was run.

## 1. Exact claim and fixed parameters

For every nonempty finite set D of distinct integers at least 4 with gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>1, every integer k>=1 and every finite set F of labels (d,j) with d in D and j>=k admit an explicitly recursive infinite sequence Q of distinct remaining labels with strictly increasing numerical values q_i, such that its actual complement R has finite subset sums with all consecutive gaps at most g=ceil(sum_{d in D}d^k/(d-1)+sum_{(d,j) in F}d^j), every base d in D occurs infinitely often in Q with bounded gaps between its selected exponents, and sum_i ||beta q_i||^2=infinity for every nonzero beta in R/Z; moreover for every integer L>=1 the finite subset sums of all remaining labels contain L consecutive integers with a terminating witness procedure, each label used at most once and coincident values from distinct labels retained separately.

Fix an input D,k,F in the claim. Let P be the remaining labels (d,j)
with d in D and j>=k, outside F. The value of (d,j) is d^j.
Coincident numerical values never identify labels. Write FS_0(A) for
the numerical finite subset sums of a label supply A, including 0.
Different represented integers may use overlapping supports; each
individual representation must use every label at most once.

Set

    sigma = sum_{d in D} 1/(d-1),       delta = sigma-1 > 0,
    M = max D,                         s = |D|,
    C0 = sum_{d in D} d^k/(d-1),
    C = C0 + sum_{(d,j) in F} d^j,      g = ceil(C),
    K = 2 + 2/delta,
    epsilon = delta / (4(sigma+2K)),
    eta = delta / (2 sigma),
    Lambda = 2M + 4 sigma/delta = 2M + 2/eta.              (1)

All these numbers except the indicated integers are positive rational
numbers computable from D,k,F. In particular

    0 < epsilon < 1/4,  0 < eta < 1/2,
    Lambda > 2M,       Lambda > 2/eta > 1.               (2)

The operation parameters epsilon and Lambda depend only on D and are
fixed before iteration. No logarithmic comparison is part of the
procedure below.

Fix the increasing cyclic order h_1,...,h_s of D, repeated indefinitely.
Starting at W_0=0, select q_i=h_i^{e_i} to be the least power of h_i
satisfying both tests

    q_i > Lambda(C+W_{i-1}),                              (3)
    for every d in D, some d^{n_d} lies in
          [(1-epsilon)q_i,(1+epsilon)q_i].                (4)

Here e_i and n_d are nonnegative integers. Set W_i=W_{i-1}+q_i.
Testing (4) is finite: for each d, increase its powers until reaching
the lower endpoint, then compare with the upper endpoint. All
comparisons use integer powers and rational numbers. Section 4 proves
termination of each selection and bounded waiting, without assuming
full-torus equidistribution.

First we prove the amplification's preservation property for any
finite sequence satisfying (3)--(4), before constructing its seed.

## 2. An integer geometric-sum inequality

For d>=2 and z>1 let p_d(z) be the least power d^a, with a>=0,
such that p_d(z)>=z. Thus a>=1. Put m=ceil(z)>=2. Since p_d(z)
is an integer,

    p_d(z) >= m,
    (p_d(z)-1)/(d-1) = 1+d+...+d^{a-1} is an integer.

Consequently

    V(z) = sum_{d in D} (p_d(z)-1)/(d-1)

is an integer and

    V(z) >= sigma(m-1) > m-1.

It follows that V(z)>=m>=z. Therefore

    sum_{d in D} p_d(z)/(d-1) >= z+sigma
    for every real z>1.                                 (5)

This is the additional absolute margin at aligned power scales. Its
integer step uses strict sigma>1. There is no limiting density
argument and no generic independence assumption on the bases.

For later use, the ordinary strict-prefix bound is

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1),    x>0.       (6)

When x<=d^k its right side is nonpositive. Otherwise the numerator of
the geometric sum is the least d-power at least x, minus d^k.
Equality at a power value is included because the prefix is strict.

## 3. The all-scale preservation lemma

Suppose a finite selected prefix satisfies (3)--(4), and write q for
its latest selection, h for its base, and W for the total value of
all earlier selections. For each d choose a power a_d=d^{n_d} in
the interval in (4). For h take a_h=q. This is allowed because q
itself belongs to the interval. In fact the interval contains at most
one power of any d, since (1+epsilon)/(1-epsilon)<5/3<d.

By (2)--(3), q>2MC. For every d in D,

    (1-epsilon)q > (3/4)2M C
                >= (3M/(2(d-1))) d^k
                > d^k.                                 (7)

Thus a_d>d^k. Also a_d/d <= (1+epsilon)q/d < q. Every
power strictly below a_d is therefore strictly below q. These facts
justify every geometric identity used next, including the cutoff.

Consider a finite or infinite selection satisfying (3)--(4), and a
scale x>=q for which q is the latest removed selection with value
at most x. Later removed selections, if any, have value greater than x.
Subtracting C-C0 pays for all F, and subtracting W pays for all earlier
selected labels, whether or not they lie in the subcollection being
estimated. Such oversubtraction only weakens a lower bound.

### 3.1 Near scales: q<=x<=(1+epsilon)q

Use, for each d, all original powers with exponent at least k strictly
below a_d. These are
strictly below q and hence below x. They exclude the current selected
label (h,e), since a_h=q. Their total value before removals is

    sum_{d in D} (a_d-d^k)/(d-1)
       >= (1-epsilon)sigma q-C0.

The retained strict-prefix total is at least

    (1-epsilon)sigma q-C-W
      >= x + [delta-epsilon(sigma+1)]q-C-W
      >= x + (3delta/4)q-C-W.                            (8)

For the final inequality, K>2 and the definition of epsilon give
epsilon(sigma+1)<=epsilon(sigma+2K)=delta/4.

### 3.2 Intermediate scales: (1+epsilon)q<x<=Kq

Put z=x/((1+epsilon)q)>1. For each d, let b_d(x) be the least
d-power at least x. Since x>a_d, we can write b_d(x)=a_d d^r
for an integer r>=1. Moreover

    d^r >= x/a_d >= z,

so d^r>=p_d(z). It follows that

    b_d(x) >= (1-epsilon)q p_d(z).

The total original strict x-prefix, before F or any Q removal, is
exactly sum_d (b_d(x)-d^k)/(d-1). Applying (5) and subtracting
all removed weights, including the current q, gives the lower bound

    (1-epsilon)q(z+sigma)-C-W-q
      = x + [delta-epsilon sigma
                   - (2epsilon/(1+epsilon))(x/q)]q-C-W
      >= x + [delta-epsilon(sigma+2K)]q-C-W
      = x + (3delta/4)q-C-W.                            (9)

This covers every intermediate real scale, not only powers or
selection times. The least-power convention includes numerical ties.

### 3.3 Far scales: x>=Kq

Sum (6), then subtract the weights of F and every selection at most x.
There are no later selections below x by the choice of q. The retained
strict-prefix total is at least

    sigma x-C-W-q
      = x+delta x-q-C-W
      >= x+(delta K-1)q-C-W
      = x+(2delta+1)q-C-W
      >= x+q-C-W.                                      (10)

Subtracting q at x=q would still be a valid weaker bound, although
the near-scale estimate is the one used there.

### 3.4 One uniform margin, finite prefixes and the infinite complement

The ranges above cover every x>=q because K>2>1+epsilon. Since

    eta = delta/(2sigma) < min(3delta/4,1),

(8)--(10) imply

    retained strict-prefix total >= x+eta q-C-W
                                  > x+(eta/2)q.         (11)

The strict inequality follows from (3) and Lambda>2/eta:
C+W<q/Lambda<(eta/2)q. The absolute margin is positive and
cannot be diluted by iteration.

For completeness, (3) also gives q_i>W_{i-1} and q_i>C.
For i>1 it implies q_i>Lambda q_{i-1}, so the selected numerical
values strictly increase and tend to infinity. Each selected label
is legal: q_i>2MC>h_i^k by (7), and q_i>C is larger than every
value in F. No selected label or numerical selection value repeats.

Let R_t be P with the first t selected labels removed, and let R
be P with all selected labels removed. For a fixed x>0, if there is
no removed q_i<=x, (6) summed over D gives the lower bound
sigma x-C>=x-C. Otherwise choose the last such removed selection
and apply (11). This applies to every R_t, including t=0, and to R:

    sum_{ell in R_t, value(ell)<x} value(ell) >= x-C,
    sum_{ell in R,   value(ell)<x} value(ell) >= x-C.       (12)

There is no exchange of FS_0 with an infinite intersection. For each
fixed x, the increasing q_i have only finitely many terms at most x,
and later deletions leave that strict prefix unchanged. Equations
(8)--(11) directly estimate the actual infinite complement. Distinct
base labels at a numerical tie remain distinct throughout.

Equation (12) implies that each retained supply is infinite with
unbounded prefix totals. A finite total retained weight would
contradict (12) as x tends to infinity.

### 3.5 The prescribed subset-sum gap

List either retained supply in nondecreasing value as a_1,a_2,...,
breaking ties by base. Write S_0=0 and S_n=sum_{j<=n}a_j.
Every strictly smaller value precedes a_n, so (12) at x=a_n gives

    a_n-S_{n-1} <= C <= g.                               (13)

Here is the full labelled gap induction, also used in accepted Mass,
acceptance-000005. Let A_n be the finite subset sums of the first n
labels. It contains 0,S_n, and A_n=A_{n-1} union (a_n+A_{n-1}).
The two copies have internal gaps at most g by induction. When their
spans are disjoint, the intervening gap is a_n-S_{n-1}<=g. When
the spans overlap, a gap of the union larger than g cannot lie in a
single span, and a gap crossing a span endpoint would contain that
endpoint, which itself belongs to the union. The first gap a_1 is
at most g by (13). Thus every finite-prefix gap is at most g.

Since S_n tends to infinity, every interval of g consecutive
nonnegative integers is contained within some finite-prefix span
and meets its subset-sum set. It follows that all consecutive gaps
of FS_0(R_t) and FS_0(R) are at most the same g=ceil(C), fixed
before any selection. No growing substitute for g is used.

## 4. Bounded phase waiting on the actual orbit closure

We now show that the operation always finds a next label and has
enough quantitative control to preserve exponent spacing.

Fix a cyclic base h. Let alpha in (R/Z)^D have coordinates
alpha_d=log(h)/log(d) modulo one. Let

    G_h = closure{n alpha : n in Z}.

Equip the torus with its usual translation-invariant metric. G_h is
a compact subgroup. The forward orbit
{n alpha:n>=0} is dense in G_h. One elementary proof is as follows.
In a compact metric group, for every integer j>=1 a finite cover by
sets of diameter less than 1/j places infinitely many members of
the sequence n alpha in one cover element. Two such indices can be
chosen with difference p_j>=j. Hence p_j alpha tends to zero.
For each fixed r>=1, (p_j-r)alpha tends to -r alpha and its indices
are eventually nonnegative. The forward-orbit closure therefore
contains every negative orbit point, and hence all of G_h.

For every y in G_h, its forward orbit y+n alpha is also dense in
G_h, by translation. Given any relatively open neighborhood U of
zero in G_h, the sets

    U-n alpha,  n>=0,

cover G_h. A finite subcover exists. If N_h is the largest
index in this subcover, then for every integer a>=0 some
n in {0,...,N_h} satisfies (a+n)alpha in U. This proves bounded
forward waiting without assuming that G_h is the entire torus.
All rational dependencies between the logarithms are allowed.

Choose rho>0 with

    rho < min_{d in D}{ log(1+epsilon)/log(d),
                       -log(1-epsilon)/log(d), 1/2 },

and let U consist of points whose coordinate distances from zero
are less than rho, intersected with G_h. It contains zero.
If e alpha lies in U, choose an integer n_d such that

    |n_d-e log(h)/log(d)|<rho.

Then

    1-epsilon < d^{n_d}/h^e < 1+epsilon.                 (14)

For candidate h^e above (3), these n_d are positive, since their
powers exceed (1-epsilon)h^e>d^k by (7). Thus every such orbit
return satisfies the exact finite test (4). These logarithms
establish termination only; the selection rule never evaluates them.

Given W, let a be the least exponent with h^a>Lambda(C+W).
The threshold is larger than h^k, so a>=k+1 and

    h^a <= h Lambda(C+W).

Within at most N_h further exponents an eligible power occurs.
The least eligible q chosen by (3)--(4) therefore satisfies

    Lambda(C+W) < q
       <= h^{N_h+1} Lambda(C+W).                         (15)

This proves termination for every extension, using a fixed finite
N_h depending only on D,h and the fixed epsilon. A computable or
numerically optimized bound for N_h is not claimed or needed for
the recursive rule.

This proof gives the classical compact-return interface recorded
in the study, without importing a new Diophantine independence
premise. Its source leads are Bergelson--Simmons,
arXiv:1507.02208v2, Claim2.13 footnote10, and
Li--Oprocha--Ye--Zhang, arXiv:1504.08191v1, Lemma2.1(2).
The complete elementary argument required here is given above.

## 5. Positive seed, amplification and every-base exponent gaps

Section 3 established preservation before any seed was chosen.
The smallest nonempty selected prefix has one label. With W_0=0,
Section 4 produces its least eligible q_1. Equation (11) supplies
a positive margin at least (eta/2)q_1 for every x>=q_1.
This is a computer-free positive one-label seed, not an enumeration.

The same operation extends each prefix by one label. Its selected
count increases by one, every label stays legal, its absolute
strict-prefix margin stays positive, and g is unchanged. Thus it
constructs one infinite Q and its actual complement R.

Set

    A = max_{h in D} h^{N_h+1} Lambda,    B = 2A.

Equation (3) implies C+W_i<q_i/Lambda+q_i<2q_i.
Applying (15) to the next cyclic base gives

    q_{i+1} <= A(C+W_i) < B q_i.                         (16)

One cycle therefore has q_{i+s}/q_i<B^s. For each h in D let
E_h be the least positive integer with h^{E_h}>=B^s. Consecutive
selected exponents e<e' of h are s indices apart, whence

    h^{e'-e}=q_{i+s}/q_i<B^s<=h^{E_h},
    1<=e'-e<=E_h.                                       (17)

Every base is selected once per cycle, infinitely often. These
bounds even depend only on D, not on k,F. The procedure for Q
does not need to compute N_h, A, B or E_h.

Minimality of q_i optimizes the stated one-step finite test: a
smaller power of h_i either fails the threshold or the near-alignment
condition. We claim no global minimum for support size, interval
location or running time. Arbitrarily sparser choices would not
retain the upper bound (15).

## 6. Divergence for the same Q at every nonzero character

Write ||x|| for distance to the nearest integer. Suppose that
beta in R/Z satisfies ||beta q_i|| tending to zero.

Fix h in D. For every sufficiently large exponent j, choose the
largest selected exponent e<=j of h. By (17), 0<=j-e<=E_h,
and hence

    ||beta h^j|| <= h^{j-e}||beta h^e||
                 <= h^{E_h}||beta h^e|| -> 0.            (18)

The selected index used here tends to infinity with j. Thus the
limit holds for all powers of h, not only its selected subsequence.

For a real representative of beta choose nearest integers z_j to
beta h^j and put u_j=beta h^j-z_j. Then u_j tends to zero and
the integers

    z_{j+1}-h z_j = h u_j-u_{j+1}

tend to zero. They are eventually zero, so eventually u_{j+1}=h u_j.
Because h>1 and u_j tends to zero, those errors are eventually
identically zero. Thus beta h^J is an integer for some J, for
every h separately.

One base makes beta rational. Writing beta=a/b in lowest terms,
every prime dividing b would divide every h in D, since b divides
a power of every h. This contradicts gcd(D)=1 unless b=1.
Therefore beta is zero in R/Z.

For beta!=0, the nonnegative norms ||beta q_i|| do not tend to
zero. Some positive lower bound occurs infinitely often, and thus

    sum_i ||beta q_i||^2 = infinity.                     (19)

This treats rational and irrational beta and uses the same Q for
all of them. It does not claim a uniform rate over the characters.

## 7. The full Fourier-Stieltjes mean

This continuation follows accepted CP24, acceptance-000011, and
accepted CP25, acceptance-000012. We state the full interface and
argument because character cancellation by an arbitrary mean
would not suffice.

The primary source is John T. Griesmer, Discrete sumsets with one
large summand, arXiv:2507.10512v1,
https://arxiv.org/pdf/2507.10512v1. Definition3.4 calls a mean
Fourier-Stieltjes (FS) when it averages every unitary matrix
coefficient to the invariant projection. Lemma9.5(ii) gives the
equivalent spectral-measure condition used below.

Define a finitely supported probability measure on Z by

    mu_n = 2^{-n} sum_{v in {0,1}^n}
                   delta_{sum_{i<=n}v_i q_i}.

These are measures on numerical sums, counting all label choices.
If choices coincide numerically their masses add. In particular,
mu_n(FS_0(Q))=1. For chi_beta(x)=exp(2 pi i beta x),

    integral chi_beta d mu_n
      = product_{i<=n}(1+exp(2 pi i beta q_i))/2.

By (19), at each beta!=0 infinitely many factors have absolute
value bounded by a fixed constant less than one. The integral
therefore tends to zero for beta!=0 and equals one for beta=0.

For any positive finite Radon measure rho on R/Z, define
rho_hat(x)=integral chi_beta(x) d rho(beta). Finite support of
mu_n permits interchange of integrals. Sequential dominated
convergence, with absolute bound one, yields

    lim_n integral rho_hat d mu_n = rho({0}).             (20)

Take a weak-star cluster point eta_FS of the sequence of means
mu_n along n tending to infinity. Compactness of the space of
means supplies such a point. Equation (20), valid for every rho,
passes to this point, and eta_FS(FS_0(Q))=1.
Griesmer's Lemma9.5(ii) identifies eta_FS as a full FS-mean.

Dominated convergence was applied to the original sequence of
countably additive measures before taking a cluster point, as in
Lemma10.3 and Remark10.4. It was not applied to a net of finitely
additive means. We do not substitute the character-only property
of an arbitrary mean, which is the distinct Question10.5.

## 8. Legal finite intervals and terminating witness procedures

Put X=FS_0(R) and Y=FS_0(Q), as numerical subsets of Z.
Section 3 gives a point of X in every interval of g consecutive
nonnegative integers. The averaging means on {0,...,n-1} give
X mass at least floor(n/g)/n. A weak-star cluster point along
n tending to infinity is translation invariant: a fixed integer
translation changes at most twice its absolute value of the
averaged positions. It gives X mass at least 1/g>0.

Thus X has positive upper Banach density. Griesmer's Observation1.3
supplies an extreme invariant mean nu with nu(X)>0. The exact
trusted sumset theorem is Corollary4.2(ii):

For subsets X,Y of a discrete abelian group, an extreme invariant
mean nu and an FS-mean eta_FS satisfying nu(X)+eta_FS(Y)>1
imply nu(X+Y)=1.

Here eta_FS(Y)=1, so the theorem applies. For any integer L>=1,
the intersection of the sets (X+Y)-j for 0<=j<L has mean one.
Its complement is a finite union of sets of mean zero. The
intersection is nonempty. Since X+Y is nonnegative, some u>=0
satisfies

    {u,u+1,...,u+L-1} contained in X+Y.                   (21)

The label supplies Q and R are disjoint. Each X representation
and Y representation can therefore be united legally, including
at numerical coincidences. Conversely, every finite support
in P splits between these two supplies. Hence

    X+Y = FS_0(P).

Equation (21) is exactly the required full-supply interval claim.
It is not a claim that FS_0(Q) alone is thick or that FS_0(P)
is cofinite.

The recursive selection Q uses only the finite integer/rational
tests (3)--(4), with termination proved in Section 4. Membership
of a given legal label in Q is decidable by generating selections
until their values exceed its value. Strict growth makes this
finite. This also yields an enumeration of R.

For an interval witness of requested length L, enumerate P in
nondecreasing numerical order, breaking ties by base. For each
finite prefix enumerate its labelled subsets and their sums,
retaining one support for each numerical sum. If L consecutive
integers appear, return them with those finite supports.
Fixed orders make this deterministic.

This procedure is described, not executed. Every stage is finite.
Equation (21) gives finitely many finite supports for one such
interval; their union lies in some finite prefix. Thus the procedure
terminates for every input in the claim. No uniform running-time,
support-height, memory or computable recurrence-gap bound is asserted.

The cited sumset theorem, including its underlying Theorem3.17,
is a trusted primary input at the same boundary as accepted CP24
and CP25. Its upstream proof is not independently reproved here.
This is an analytical candidate, not a Lean-kernel proof.

## 9. Limits, entry outcome and remaining objective

The positive margin (5) depends on strict delta>0. As delta
decreases to zero, K and Lambda increase and epsilon decreases.
The formulas do not extend to equality by taking a limit.
No equality theorem or minimum-three extension is claimed.

The argument does not partition P into a proper thick supply
and a further unused bounded-gap reserve. R is already used
in X+Y, so it cannot be reused as a disjoint completeness reserve.
All-tail thickness does not by itself prove eventual completeness.

An interval of length two gives a signed unit by taking supports
for u+1 and u, cancelling their common labels, and subtracting
the remaining sums. This is the intended contribution to
obligation28 on the present strict-mass domain. Complement50,
bridge51, the subunit half-mass cores, the critical threshold
T_4=1 and the original mass-one completeness objective remain
unproved by this move. In particular, no new root acceptance
or claim replacement is made.

The entry's order was respected: Sections 2--3 prove amplification
and preservation; Section 4 proves next-step existence; Section 5
obtains the smallest nonempty positive seed and quantifies its
iteration, including selected exponent gaps. Sections 6--8 prove
every remaining clause of the admitted claim. Section 5 states
the one-step optimization and this section tests its strict-mass
boundary. No amplification hypothesis remains unpaid.

This is a closing analytical proof candidate for node20 only.
It justifies direction true and mode construction, with the
admitted claim, stage and all quantifiers unchanged. The closing
cost ledger is empty because the exact claim, prescribed bound,
and required constructivity have all been retained.

Independent exact-result review, immutable evidence audit and
controller acceptance are still required. No computation,
formal verification, exhaustive novelty, priority, publication
or budget-renewal claim is made.
