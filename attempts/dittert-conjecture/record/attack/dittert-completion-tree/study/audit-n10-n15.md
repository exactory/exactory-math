# Independent analytic audit for dimensions 10 through 15

Source argument: Pedro Paulo Marques do Nascimento, unified proof at
https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701.
This audit rederives its finite-dimensional implications and independently
checks the arithmetic. It is not a claim of a new proof or a Lean formalization.

## Statement and boundary reduction

Let n be any of 10,11,12,13,14,15, and let K_n contain all nonnegative n by n
real matrices with total entry sum n. Write gamma=n!/n^n and
Phi(A)=R+C-P for the row product R, column product C, and permanent P.
Compactness supplies a global maximizer. Hwang's positive-support theorem
identifies any positive maximizer as the uniform matrix. Cheon-Wanless
Theorems 3.2 and 3.7 exclude partly decomposable maximizers and maximizers
whose complete nonempty zero set is one proper rectangle. These exact
statements were checked in the locally stored primary paper
../dittert-conjecture-n5-to-n15/study/fetched/cheon-wanless-2012.txt.

Consequently a boundary maximizer is fully indecomposable and has two zeros
in different rows and columns: a zero set with no such pair lies entirely in
one row or column, and is a rectangle. At a hypothetical boundary maximizer,
R,C<=1 and Phi>=2-gamma imply P=gamma-delta, 0<=delta<=gamma, and
rho+sigma<=delta where rho=1-R, sigma=1-C. In particular R,C>=1-gamma>0.

## Scaling and exhaustive cut cases

Set lambda=min s_A(I,J)/p over p=|I|+|J|-n>0. Every numerator is positive:
a zero rectangle with |I|+|J|>n would contain a partly decomposable zero
rectangle. The whole cut gives lambda<=1. Li's criterion (Cheon-Wanless
Lemma 2.2) gives a doubly stochastic B with lambda B<=A. Thus
P>=lambda^n per(B). This B is a dominated matrix; it need not be the
Sinkhorn scaling in the older local attacks.

Choose a minimizing cut and write a=n-|I|, b=n-|J|, p=n-a-b,
u=1-lambda. Cases are exhaustive: a=b=0; exactly one of a,b is zero;
or a,b>=1 with a+b<=n-1. Whole cuts force A=B doubly stochastic, contradicting
the strict boundary permanent bound. In a marginal cut, the ratio is a line
average. Since singleton line cuts are available in the same minimum,
lambda equals a minimum line sum. After transpose this is a minimum row,
so all marginal cases reduce to (a,b)=(n-1,0). Every ordered proper cut is
explicitly enumerated by the independent checker; transpose is not needed
for computational completeness.

On a proper tight cut, doubly stochasticity gives
s_B(I,J)=p+s_B(I^c,J^c)>=p. Domination gives
lambda s_B(I,J)<=s_A(I,J)=lambda p. Since lambda>0, both are equalities,
and B[I^c,J^c]=0. The staircase-face permanent floor is therefore
nu=gamma_(n-a) gamma_(n-b)/gamma_p. Hwang's staircase theorem identifies
the barycenter as a minimizer. For this rectangle its nonzero block entries
are 1/(n-b), 1/(n-a), and p/((n-a)(n-b)); counting supported permutations
gives the displayed value. The theorem, not just the count, licenses the
lower bound. Source DOI: 10.1080/03081088508817694.

For the assembled proof, this external extremizer input is replaced by the
dimension-independent capacity proof in study/audit-n7.md, section 3.
Its successive degree bounds prove exactly the same sharp constant for
every n=a+b+p with a,b,p>=1. The one-zero floor below is also its special
case a=b=1. Thus the assembly does not rely on access to the full text of
the older extremizer paper, whose publisher abstract was all we obtained.

Every zero of A is a zero of B because lambda>0. The one-zero floor
kappa=(n-2)!((n-2)/(n-1)^2)^(n-2) always applies. At n=10 the stronger
two-independent-zero floor L=kappa(1+1/(2n^2)) applies. Minc's general
averaging theorem supplies the repeated-support block form. Its use was
checked against Pula-Song-Wanless Section 2, university preprint
https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1022.pdf.
Their later equalization theorem is not assumed for block size two.
Instead, the direct derivative in the source is negative on the full
parameter domain: with m=n-2, s in [0,2/m], q<=s^2/4, the derivative
is at most ((m^2+m+2)s^2-2ms-2)/2. This convex quadratic is negative
at both endpoints for m>=4, so exceptional parameters can be equalized.
The resulting permanent polynomial is verified by integer subset-DP at
n+1 distinct points and an independent exact Sturm root count.

## Deficits and stationarity

For positive line sums x_i of sum n, product X>=1-gamma, and subset excess
e on d lines, separate AM-GM gives X<=exp(-g(e)), where
g(e)=-d log(1+e/d)-(n-d)log(1-e/(n-d)). Binary Pinsker gives
e^2<=n gamma/(2(1-gamma))<1/100 for n>=8. On |e|<=1/10,
g''(0)=n/[d(n-d)] and |g'''(e)|<=2000g''(0)/729. Taylor's theorem gives
g(e)>=(1987/4374)g''(0)e^2. Since g(e)<1/400,
1-exp(-g)>=g/(1+g) and (1987/2187)(400/401)>7/8 show
1-X>=7n e^2/[16d(n-d)]. All endpoint constants are exact-checked.

If e,f are the omitted row and column excesses of a proper cut, then
pu<=e+f<=e_++f_+. Applying the subset estimate to both products and
Cauchy-Schwarz gives delta>=Ccut*u^2 with
Ccut=7np^2/[16(a(n-a)+b(n-b))]. Negative excesses can be discarded
because their squared deficits are nonnegative.

For the marginal cut, let r_i=1-u. Support stationarity is
R/r_i+C/c_j-per A(i|j)=Phi(A) whenever a_ij>0. This follows from
equal partial derivatives on the positive support and Euler homogeneity;
no differentiation across a forbidden negative entry is used.
Multiplying by a_ij and summing in row i gives
q_i=sum_j a_ij/c_j=1-(1+theta)u, theta=(R-P)/C>=1-gamma.
The sum q_i is positive. A column meeting that row has
c_j>=r_i/q_i>=1+h, h=(1-gamma)u/[1-(2-gamma)u]. Its denominator is
positive because q_i>0. In particular h>=(1-gamma)u.
The one-line subset estimate on both this column and the minimum row
therefore gives Ccut=7n(1+(1-gamma)^2)/[16(n-1)]. All hypotheses
(positive line sums, product lower bounds, localization) still hold.

## Exact scalar contradictions and equality

For n=11..15 set M=nu on proper cuts and M=kappa on marginal cuts.
The independent Fraction checker establishes, for every ordered cut,
M-gamma-n^2*M^2/(4*Ccut)>0. Then for every u in [0,1],
P-gamma+delta >= M(1-u)^n-gamma+Ccut*u^2
>=M-gamma-n*M*u+Ccut*u^2>0, contradicting P=gamma-delta.
There is no choice of a small or large fixed-point branch in this argument.

At n=10 set M=max(nu,L) on proper cuts and M=L on marginal cuts.
Feasibility gives u^2<=gamma/Ccut. Let ubar
be the least positive multiple of 10^-6 whose square is at least that
ratio. The exact checker verifies 0<ubar<1. The integral identity
((1-u)^n-1+n*u)/u^2=n(n-1) integral_0^1(1-t)(1-ut)^(n-2) dt
shows this remainder is decreasing. With beta equal to its value at ubar,
the scalar lower bound has positive minimum
M-gamma-n^2*M^2/[4(Ccut+beta*M)] on every cut. The independent
minimum is greater than 5.94e-7; this decimal is descriptive, not a
correctness decision.

Thus no boundary global maximizer exists in any dimension 10..15.
Hwang's theorem makes the uniform matrix the unique global maximizer.
Its value is exactly 2-gamma, proving both inequality and equality case
for every admissible matrix, not just stationary or nearly stochastic ones.

## Fresh evidence

deterministic/certified-special-case-check-1/result.json is pass.
The source's full unified checker and the newly written independent checker
both passed. The latter enumerated 37,46,56,67,79,92 ordered cut cases
for n=10,11,12,13,14,15 respectively. Integer arithmetic and SymPy rational
root counting are the computational trust base. This finite-range audit
does not rely on the source's separate infinite-range monotonicity argument.
