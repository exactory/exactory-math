# Dittert's inequality for every 5 <= n <= 15, with all branches covered

## Theorem

For every integer 5<=n<=15 and every nonnegative real n by n matrix A
whose entries sum to n, let r_i,c_j be its row and column sums. Then
\[
\prod_i r_i+\prod_j c_j-\operatorname{per}(A)\le2-\frac{n!}{n^n},
\]
with equality if and only if every entry of A equals1/n.

This is an attributed computer-assisted proof assembled from prior local
certificates and the public Hall argument of Hongyuan Lu and Pedro Paulo
Marques do Nascimento. It is not a new discovery claim, a journal referee
decision, or a full Lean formalization. This follow-up explicitly checks
the missing-branch objection to the earlier local Sinkhorn argument.

## Proof

Write gamma_n=n!/n^n and Phi for the displayed functional.

For n5,6, use the inherited SOS identities and PSD certificates at
[check1](../dittert-conjecture-n5-to-n15/deterministic/certified-special-case-check-1/README.md),
[check2](../dittert-conjecture-n5-to-n15/deterministic/certified-special-case-check-2/README.md),
and [check4](../dittert-conjecture-n5-to-n15/deterministic/certified-special-case-check-4/README.md).
Their original exact identities and verified bounds give the asserted
inequality and equality classification. The full n6 integer verification
log is preserved in the predecessor's study/inherited-n6-exact-psd.log.
Its positive exact residual slack is1691794048955. The large matrix checks
were not rerun in this follow-up; the prior complete evidence, not a
truncated output heading, is the inherited input.

Fix now any n with7<=n<=15. A global maximizer exists by compactness.
The uniform matrix has value2-gamma_n. At any global maximizer write
P=per(A)=gamma_n-delta, R=prod r_i=1-rho, C=prod c_j=1-sigma.
Then
\[
0\le\rho,\sigma,\qquad \rho+\sigma\le\delta\le\gamma_n<1.
\]
This uses only AM--GM and comparison with the uniform matrix, not the
conjectured upper bound. Thus every line sum is positive.

Every strictly positive global maximizer is uniform by the elementary
pair-averaging, contraction, and strict Hessian proof in
[BRANCH_TRANSPORT.md, Section3](BRANCH_TRANSPORT.md). This proof applies
to every n>=2. It remains to exclude a boundary global maximizer.

For such a maximizer define
\[
\lambda=\min_{|I|+|J|>n}\frac{s_A(I,J)}{|I|+|J|-n},\qquad u=1-\lambda.
\]
The subset excess bounds prove lambda>0 before any division, and the
full cut gives lambda<=1. Finite max-flow/min-cut constructs a doubly
stochastic B with lambda B<=A. Therefore P>=lambda^n per(B), and
every zero of A is a zero of B. If a minimizing cut has complementary
sizes a,b and p=n-a-b>=1, tightness forces B[I^c,J^c]=0.
These statements, including nonunique cuts and real capacities, are proved
in BRANCH_TRANSPORT.md, Sections4 and5.

Every minimizing cut is full, marginal, or proper. A full cut gives
lambda=1, A=B, and van der Waerden's strict boundary inequality gives
P>gamma_n, a contradiction. A marginal cut reduces to a minimum line sum
by the line-average argument, with either orientation allowed. A proper
cut has a,b>=1 and a+b<=n-1. This is an exhaustive partition, not a
choice of a branch of a scalar fixed-point equation.

The permanent inputs are the sharp rectangular-zero capacity bound
nu=gamma_(n-a)*gamma_(n-b)/gamma_p and, when needed, the two-independent-zero
floor L_n=kappa_n*(1+1/(2n^2)), with
kappa_n=(n-2)!*((n-2)/(n-1)^2)^(n-2). The exact source hypotheses and
polynomial floor certificates are discharged in BRANCH_TRANSPORT.md,
Section7. In particular the required two-parameter face is included in
the published source; [SOURCE_CORRECTION.md](SOURCE_CORRECTION.md)
records the visual correction of a prior text-extraction error.

For n7, [COVERAGE_PROOF.md](../hall-n7-branch-coverage/COVERAGE_PROOF.md)
gives a strict contradiction for every marginal cut, every proper cut
with p>=2, and every p=1 sign configuration. The three both-positive
p=1 cases are (a,b)=(1,5),(2,4),(3,3), covered by closed squares.
On every square point a direct lower bound is contradictory, or two
strict inequalities give incompatible bounds on the same nonnegative
product. The necessary sign is tested before squaring; zero-variable
endpoints and vanishing matrix entries are included.

The [new exact certificate](../hall-n7-branch-coverage/deterministic/certified-special-case-check-1/README.md)
enumerates all6476 actual subset-pair cuts and all28 ordered size types.
It independently rebuilds the polynomial formulas and certifies all62
terminal rectangles by direct restriction, without using the source's
subdivision implementation. A full binary-prefix condition and exact
rectangle union prove continuous coverage including junctions. All94
omission mutations are rejected. Its result.json is pass.
Consequently every n7 boundary global maximizer is excluded.

For each8<=n<=15, [the coverage proof](../hall-n8-n15-branch-coverage/PROOF.md)
derives delta>=C_cut*u^2 for every cut, including signed proper excesses
and both marginal orientations. Stationarity proves every denominator
positive before division. For n11..15, the exact inequality
\[
M-\gamma_n-\frac{n^2M^2}{4C_{\rm cut}}>0
\]
gives
\[
0=P+\delta-\gamma_n
\ge C_{\rm cut}\left(u-\frac{nM}{2C_{\rm cut}}\right)^2
 +M-\gamma_n-\frac{n^2M^2}{4C_{\rm cut}}>0
\]
on all u in[0,1]. There is no omitted high-u interval.

For n8..10, the global deficit gives
u^2<=gamma_n/C_cut, so the rational square-root enclosure is valid for
every hypothetical maximizer. The decreasing integral remainder of
(1-u)^n supplies a strict quadratic contradiction for every proper cut
and the n10 marginal cut. Only the n8 and n9 marginal rows remain.
They are not discarded.

For n8 the remaining domain is the union of [0,1/400] and
[1/400,1/20], with the entire feasible tail u>=1/20 excluded by a
monotone deficit exceeding gamma_8. For n9 it is [0,1/500] and
[1/500,3/100], with the analogous tail excluded. The near-zero intervals
use direct product bounds. The other intervals use incident-column
stationarity caps, every n8 support case z=1,...,6, and the largest
n9 zero count z=7. The latter covers all z=1,...,7 by a proved
monotonic relaxation with a constant permanent floor. Impossible column
zero counts0,n-1,n are excluded separately. All intervals are closed,
all cleared multipliers are strictly positive, and every tail endpoint
is covered.

The [new exact witness-chain check](../hall-n8-n15-branch-coverage/deterministic/certified-witness-chain-1/README.md)
validates all596 uncompressed omitted-size pairs, all428 ordered scalar
cases, and all9 residual interval polynomials. The independent program
constructs polynomials directly in the Bernstein basis, without importing
the source or its power-basis conversion. Each of the9 polynomials has
strictly positive coefficients on its entire interval, without subdivision.
The source's separate power/Sturm implementation also passes.
Its result.json is pass. Thus every n8..15 boundary global maximizer
is excluded.

There is therefore no boundary global maximizer for any7<=n<=15, and
every positive one is uniform. This proves the inequality throughout the
requested range. Any equality matrix is itself a global maximizer, so it
must be uniform; the uniform matrix attains the stated value. QED.

## Why the old missing branch is actually addressed

The old route's large-cost scalar branch still exists as a solution of
its relaxed inequalities. The proof above does not say otherwise.
It begins with an arbitrary global maximizer, without a restriction on
that old cost. It constructs a different dominated matrix and covers
every possible Hall case and every feasible value of its parameter.
A putative maximizer in the old large-cost branch therefore reaches one
of the same strict contradictions. BRANCH_TRANSPORT.md spells out this
transport without assuming the final theorem as a premise.

The following distinctions are essential: a near-maximizer is not
automatically stationary; a general near-decomposable doubly stochastic
matrix is not automatically the scaling of a global maximizer; the new
Hall parameter is not the old Sinkhorn cost. None is conflated here.

## Evidence and attribution

The prior source is pinned to
[Nascimento commit894066bbaa715138c98bf3cb7c6fdb4f39a37701](https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701);
the n7 method is attributed to
[Lu commit56397b70299278b338a286b90361180833dbf983](https://github.com/lueluelue2006/dittert-n7-extension/tree/56397b70299278b338a286b90361180833dbf983).
Classical inputs include Gurvits arXiv:0711.3496 and Cheon--Wanless
DOI10.1016/j.laa.2010.08.041. The original source and licenses remain
unchanged in ../dittert-completion-tree/study/external-proof.

All finite positivity decisions are exact integer/rational calculations,
not floating-point samples. Software arithmetic and the mathematical
reduction remain explicit trust boundaries. Independent review is recorded
separately in study/independent-review.md. No full real-matrix Lean proof
or journal peer review is claimed.
