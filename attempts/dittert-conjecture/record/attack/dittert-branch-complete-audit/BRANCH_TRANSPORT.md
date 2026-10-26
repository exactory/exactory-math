# Branch-complete transport and common inputs

This note addresses the missing-branch objection to the old local proof.
It does not assert that the old scalar fixed-point inequalities have only
one solution branch. They do not. The old large-cost scalar region remains
a valid obstruction to that method.

## 1. Exact logical claim

For each integer 7<=n<=15, suppose A is an arbitrary global maximizer of
Phi on the nonnegative matrices of total mass n. No assumption on a
Sinkhorn cost or spectral gap is made. We construct a dominated doubly
stochastic matrix B_H and a Hall parameter u_H, and show that A enters
one of the explicitly enumerated cases of the dimensional coverage proofs.

The old route used a generally different doubly stochastic matrix B_S
obtained by multiplicative Sinkhorn scaling and an associated cost K_S.
Nothing here identifies B_H with B_S or u_H with K_S. In particular there
is no step K_S<=K_1, no least-fixed-point choice and no spectral-gap bound.
If a hypothetical global maximizer happened to satisfy K_S>=K_2(n),
the same construction and the same cases below would apply to it unchanged.

The numerical interface in every case is
\[
0=P+\delta-\gamma_n\ge H_n>0.
\]
For n7 the strict lower contradiction can instead be the incompatible
upper and lower bounds on the same nonnegative product in the entropy
alternative. Each component must cover its entire feasible domain.

This is a proof that the old missing branch cannot contain an actual
global maximizer, once the dimensional interfaces are established. It is
not a proof of a new permanent bound for every abstract near-decomposable
doubly stochastic matrix, nor a refutation of the old scalar region.

## 2. Global maximality, deficits, and stationarity

Compactness gives a global maximizer. At the uniform matrix U_n,
Phi(U_n)=2-gamma_n, where gamma_n=n!/n^n. Put
R=prod r_i, C=prod c_j, P=per(A), rho=1-R, sigma=1-C,
delta=gamma_n-P. AM--GM and P>=0 give
\[
0\le\rho,\sigma,\quad \rho+\sigma\le\delta\le\gamma_n<1.
\]
Thus R,C>=1-gamma_n>0, so all row and column sums are positive.
This argument does not assume the conjectured upper bound.

All positive entries of A have the same partial derivative mu: one can
transfer sufficiently small mass in either direction between any two
positive cells. Euler homogeneity of degree n gives
n*mu=sum a_ij*dPhi/da_ij=n*Phi(A), so mu=Phi(A). Consequently
\[
R/r_i+C/c_j-\operatorname{per}A(i|j)=\Phi(A)
\quad\text{whenever }a_{ij}>0.
\]
No differentiation in an infeasible negative direction at a zero is used.

## 3. Positive maximizers, including uniqueness

Here is an elementary dimension-independent version of the interior
argument, so the assembly need not leave its positive branch to an
unread source theorem.

At a positive global maximizer, mix two columns by
((1-t)x+ty, tx+(1-t)y). Total mass and nonnegativity are preserved for
0<=t<=1, and feasibility also holds for sufficiently small negative t.
The functional is quadratic in t and symmetric under t->1-t.
It therefore equals Phi(A)+alpha*t*(1-t). Its derivative at0 vanishes
by interior stationarity, so alpha=0. Pair averaging preserves both
positivity and the global maximum. The same proof works for rows.

A cyclic finite schedule of all pairs of columns is a composition of
orthogonal averaging projections. On the subspace of column collections
with mean zero, its operator norm is strictly below1. Indeed, equality of
norm would force equality at every projection, hence all columns equal,
and zero mean would make the collection zero. Compactness of the finite
dimensional unit sphere gives a uniform strict contraction. Repetition
therefore converges to A' with entries r_i(A)/n. Positivity is preserved
also in the limit. Cyclic row averaging of A' converges to U_n.
Continuity proves that the global maximum value equals Phi(U_n).

To prove uniqueness rather than merely the value, let X be a nonzero
tangent matrix with sum X_ij=0. Direct differentiation at U_n gives
\[
D^2\Phi(U_n)[X,X]=
-(1-c_n)(\|X\mathbf1\|^2+\|X^T\mathbf1\|^2)
-c_n\|X\|_F^2,\qquad c_n=(n-2)!/n^{n-2}.
\]
For n>=2, 0<c_n<=1, so this is strictly negative. The first tangent
derivative is zero. Hence U_n is an isolated feasible matrix of its
value in a neighborhood of U_n.

Any sequence of global maximizers converging to U_n is eventually equal
to U_n. If one pair average first reaches U_n from a distinct positive
maximizer N, its mixing path has the form
U_n+(1-2t)(N-U_n). Flatness gives distinct same-value matrices arbitrarily
close to U_n as t approaches1/2, a contradiction. Backtracking the finite
row segment gives A'=U_n; then the column sequence converges to U_n,
and the same argument gives A=U_n. The proof works for every n>=2.
It does not claim arbitrary pair averaging reaches its limit finitely.

## 4. Hall positivity before division

For n7 the subset-sum proof in the n7 coverage component establishes,
before Hall scaling, that each nonempty proper subset of line sums has
excess e with |e|<7/47. For n>=8 the analogous elementary deficit
localization gives |e|<1/10. For empty or full subsets the excess is zero.

Fix arbitrary row and column subsets I,J with
p=|I|+|J|-n>0. Put a=n-|I|, b=n-|J| and
e=sum_(i in I^c) r_i-a, f=sum_(j in J^c) c_j-b,
z=s_A(I^c,J^c)>=0. Inclusion-exclusion gives
\[
s_A(I,J)=p-e-f+z.
\]
For n7 this is at least p-|e|-|f|>p-14/47>0,
and for n>=8 it is greater than p-1/5>0.
Thus the finite minimum
\[
\lambda=\min_{p>0}s_A(I,J)/p
\]
is strictly positive without an assumption about the old cost.
The full cut shows lambda<=1. Let u_H=1-lambda in [0,1).

The alternative published reason for positivity, full indecomposability
by Cheon--Wanless Theorem3.2, is consistent with this direct localization
proof but is not needed at this step.

## 5. An explicit max-flow construction

Use a finite network with arcs from the source to each row of capacity
lambda, row i to column j of capacity a_ij, and each column to the sink
of capacity lambda. A cut with rows I and columns J^c on the source side
has capacity
\[
\lambda(n-|I|)+s_A(I,J)+\lambda(n-|J|)
=n\lambda+s_A(I,J)-\lambda p.
\]
If p>0, this is at least n*lambda by the definition of lambda.
If p<=0, nonnegativity makes the same assertion immediate.
Finite max-flow/min-cut, valid for real capacities, therefore gives a
flow of value n*lambda. Since all n source arcs and all n sink arcs have
total capacity n*lambda, each is saturated.

Writing F for the row-to-column flow, B_H=F/lambda is doubly stochastic
and lambda*B_H<=A entrywise. This division is now justified.
Monotonicity and homogeneity of the permanent give
P>=lambda^n*per(B_H). Every zero of A is also a zero of B_H.

No uniqueness of the flow, B_H, or minimizing cut is needed. For every
minimizing cut, double stochasticity gives
s_B(I,J)=p+s_B(I^c,J^c)>=p, whereas domination gives s_B(I,J)<=p.
Thus s_B(I^c,J^c)=0 and B_H has the claimed a by b zero rectangle.
This uses equality in the tight cut, not an unjustified assertion that
all of A=lambda*B_H.

## 6. Exhaustive cuts, ties, and endpoints

The integer pair (a,b) satisfies a,b>=0 and a+b<=n-1. Exactly one of
the following occurs.

1. a=b=0: the minimizing cut has ratio1, so lambda=1 and u_H=0.
   Since A>=B_H and both have mass n, A=B_H. If A is boundary,
   van der Waerden's strict equality condition gives P>gamma_n,
   inconsistent with P<=gamma_n.
2. Exactly one of a,b is zero: the ratio is an average of row sums or
   of column sums. All singleton line cuts occur among the original
   choices, so lambda<=minimum line sum<=this average=lambda.
   Thus lambda equals a minimum line sum. Choose a singleton row after
   transposition. This replacement preserves lambda and u_H, and proves
   every marginal cut is represented, including ties.
3. a,b>=1 with a+b<=n-1: this is a proper cut, represented by its ordered
   pair or by its explicitly justified transpose. Every pair is included
   in the dimensional finite coverage.

If several cases tie for the minimum, any of them can be used: every one
is excluded by its assigned proof. We do not select one by an unproved
sign or optimality condition. Lambda=0 was excluded before max flow;
lambda=1 was handled above. All residual rational covers use closed
intervals or closed boxes, so their internal junctions are not omitted.

## 7. Permanent floors and the corrected source assumption

For proper cuts the zero-rectangle capacity proof gives
\[
M=\nu_{n,a,b}=\gamma_{n-a}\gamma_{n-b}/\gamma_{n-a-b}.
\]
It is proved in the predecessor audit-n7.md, Section3, by successively
extracting b variables with degrees at most n-a,...,n-a-b+1 from the
stable product of row forms. The starting capacity is1 by weighted
AM--GM and double stochasticity. Each extraction keeps positive capacity
by Gurvits's derivative-capacity inequality. The remaining degree
n-b polynomial contributes gamma_(n-b). All factors are positive.
The one-zero floor kappa_n is the special case a=b=1.

For dimensions8,9,10 the stronger floor
L_n=kappa_n*(1+1/(2*n^2)) is used as well. Cheon--Wanless Theorem3.7
excludes a maximizer whose entire nonempty zero set is one rectangle.
If a set of zeros has no two in distinct rows and columns, all its zeros
lie in one row or in one column: fixing one zero, a zero off its row and
a zero off its column would themselves be independent. Such a nonempty
zero set is one rectangle. Hence a boundary maximizer has two independent
zeros, and so does B_H.

After permutations their positions are (1,2),(2,1). A permanent minimizer
on this entire face may be chosen in repeated-support block form with
m=n-2 identical remaining rows and columns. Pula--Song--Wanless page3
explicitly uses this form and their Section2 assumption is m,k>=2,
where k is the number of exceptional parameters. It therefore includes
k=2. The original PDF was downloaded and visually checked. Earlier local
audits incorrectly wrote m,k>2 because text extraction lost the equality
stroke. This is corrected in SOURCE_CORRECTION.md.

The direct exceptional-parameter equalization in the pinned source remains
an independent elementary check. For s=alpha_1+alpha_2, q=alpha_1*alpha_2,
0<=s<=2/m and q<=s^2/4, its derivative is
2m(m-1)q+(m+1)s^2-ms-1. This is at most
T(s)=((m^2+m+2)s^2-2ms-2)/2.
The convex quadratic T has T(0)=-1 and
T(2/m)=-1+2/m+4/m^2<0 for m>=4. Equalization is feasible and decreases
the permanent. All n8..10 have m>=6, within this range.

Thus the minimum reduces to the stated one-variable polynomial over
the full closed interval [(m-2)/m^2,1/m]. The predecessor's independent
integer-permanent interpolation and exact root counts prove P_n-L_n>0
on that entire interval. No branch of an optimizer's equation is selected.

## 8. Dimensional coverage that must be returned

- n7: all marginal cuts; all proper p>=2 types; p=1 with a nonpositive
  excess; p=1 with both excesses positive, including both children of
  each entropy-box subdivision.
- n8,9: all proper cuts and the marginal intervals not covered by the
  quadratic test. Every allowed support size must be excluded.
- n10: all cuts, with u_H^2<=gamma_n/C derived from the global shared
  deficit rather than an assumed small-root choice.
- n11..15: the strict completed-square lower bound on every u_H in [0,1].
  There is no discarded large-u_H branch.

The child evidence and final recombination must discharge each item.
The preceding transport is independent of all child positivity decisions.
