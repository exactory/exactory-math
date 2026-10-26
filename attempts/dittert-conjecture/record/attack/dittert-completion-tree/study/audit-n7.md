# Independent analytic audit of the attributed n=7 reconstruction

Audit date: 2026-09-04.

Scope: the assertion that every nonnegative real \(7\times7\) matrix of total
entry sum seven satisfies

\[
\prod_i r_i+\prod_j c_j-\operatorname{per}(A)
\le 2-\frac{7!}{7^7},
\]

with equality precisely at \(U_7=J_7/7\). This is an independent review of
the analytic reduction in the supplied package, including its reduction to
the finite polynomial certificates. It is not a formal proof verification
and does not report a fresh execution of the full certificate programs.
The coordinating agent owns those executions and their result records.

The reviewed reconstruction is Pedro Paulo Marques do Nascimento's package
at commit `894066bbaa715138c98bf3cb7c6fdb4f39a37701`, in
`study/external-proof/n6-n7/dittert_n6_n7_reconstruction.tex`. Its
mathematical architecture, constants, and finite case families are attributed
to Hongyuan Lu's revision 2.0, at upstream commit
`56397b70299278b338a286b90361180833dbf983`. That attribution is retained here.
See the package's `ATTRIBUTION.md` and
[Lu's pinned source repository](https://github.com/lueluelue2006/dittert-n7-extension/tree/56397b70299278b338a286b90361180833dbf983).

## Verdict and remaining verification boundary

I found no invalid inequality, missing class of matrices, or unresolved
analytic hypothesis in the n=7 argument after supplying the elementary
details below. The n=7 analytic reduction is accepted within this review's
scope. There are two material exposition omissions, both repaired in this
audit: the explicit proof that the n=7 Hall dilation has positive denominator,
and the continuity/backtracking argument for the two averaging limits in
the interior classification.

The precise resulting statement is conditional on the finite arithmetic
obligations: if the six ordinary margins, six sign configurations, the
one-variable \(W\) certificate, and the three bivariate alternative trees
pass the stated exact checks, the supplemented argument proves the full
n=7 inequality and its unique equality case. There is no remaining analytic
assumption about arbitrary matrices, support patterns, or critical cuts.
I did not run the full finite checks because the machine was already heavily
loaded and the coordinating agent is running checks sequentially. Existing
package claims that programs pass were not used to establish any analytic
step. No counterexample was found or claimed.

## 1. From all matrices to positive or boundary global maximizers

The feasible set \(K_7\) is a compact simplex and \(\Phi\) is a polynomial,
so a global maximizer exists. Its value is at least \(\Phi(U_7)=2-\gamma\),
where \(\gamma=720/117649\). Put

\[
R=1-\rho=\prod_i r_i,\quad C=1-\sigma=\prod_j c_j,
\quad H=\operatorname{per}(A)=\gamma-\delta.
\]

AM--GM, nonnegativity of the permanent, and the comparison with \(U_7\) give

\[
0\le\rho,\sigma,\qquad \rho+\sigma\le\delta\le\gamma<1.
\]

Consequently every row and column sum is positive, and

\[
1-\gamma\le R,C\le1,\qquad 0\le H\le\gamma.
\]

This requires global maximality, and the later stationarity statements are
applied only to such a maximizer. They are not asserted for arbitrary matrices
having the same scalar deficits.

### Complete interior argument

TeX lines 109--182 give the right flatness and Hessian formulas. Here is a
complete version of the averaging passage, including its two limits.

For a positive global maximizer \(M\), mixing a pair of columns by the
parameter \(t\) is feasible for all \(t\in[0,1]\), and also in a neighborhood
of \(t=0\). The objective is a polynomial of degree at most two, invariant
under \(t\mapsto1-t\). Thus it has the form
\(\Phi(M)+\lambda t(1-t)\). Its derivative at zero vanishes by interior
stationarity, so \(\lambda=0\). In particular pair averaging preserves the
global maximum and positivity. The same holds for rows.

Fix a finite cyclic schedule that includes every pair of columns and repeat
it. Each pair averaging is an orthogonal projection on the vector space of
column collections. It preserves the common column mean, and decreases the
squared distance from that mean. On the subspace whose column sum is zero,
the product of the projections in a complete cycle has operator norm
strictly below one: if equality in norm held for a nonzero vector, every
projection in the cycle would preserve its norm and therefore leave it
unchanged, forcing every pair of columns to be equal. A zero-mean collection
with that property is zero, a contradiction. Compactness of the unit sphere
makes the strict bound uniform. Thus the iterates converge to a matrix

\[
B_{ij}=r_i(M)/7.
\]

Every entry of every iterate and of \(B\) is positive. Continuity of \(\Phi\)
makes \(B\) a positive global maximizer. Now run the corresponding cyclic
row averaging from \(B\). Its limit is \(U_7\), so continuity also shows
that the global maximum equals \(\Phi(U_7)\).

For a nonzero tangent matrix \(X\), the Hessian formula in the reconstruction is

\[
D^2\Phi(U_7)[X,X]
=-(1-c_7)(\|X\mathbf1\|^2+\|X^T\mathbf1\|^2)-c_7\|X\|_F^2<0,
\quad c_7=120/16807\in(0,1).
\]

The tangent first derivative is zero. Therefore there is a neighborhood of
\(U_7\) containing no other feasible matrix of value \(\Phi(U_7)\).
The row averaging sequence, whose value is always \(\Phi(U_7)\), must
reach \(U_7\) after finitely many steps.

No single pair averaging can carry a distinct positive global maximizer
\(N\) to \(U_7\): along the same pair mixing path,

\[
N(t)=U_7+(1-2t)(N-U_7),
\]

and flatness would give distinct feasible matrices of the same value
arbitrarily close to \(U_7\) as \(t\to1/2\). Backtracking the finite row
segment gives \(B=U_7\). The original column sequence now converges to
\(U_7\); the identical strict-locality and finite-backtracking argument gives
\(M=U_7\). This supplies the step that the original two-limit wording leaves
compressed. It does not assume that averaging reaches its limit in finite
time for arbitrary matrices.

## 2. Localization makes Hall domination valid

For a proper nonempty set of \(k\) rows of total \(k+e\), separate AM--GM
gives, for \(e>0\),

\[
7D(k/7\Vert(k+e)/7)
\le-\log(1-\rho)\le\frac{\rho}{1-\delta}.
\]

The last inequality follows from
\(-\log(1-\rho)\le\rho/(1-\rho)\) and \(\rho\le\delta\).
The integral formula for binary relative entropy and
\(u(1-u)\le1/4\) give

\[
\frac{2e^2}{7}\le\frac{\rho}{1-\delta}.
\]

For a negative excess, apply this to the complementary row set; column
excesses are treated with \(\sigma\). The reconstruction's checked rational
localization inequality

\[
\frac{1}{47^2}>\frac{\gamma}{14(1-\gamma)}
\]

therefore implies the useful explicit bound

\[
|e|<7/47<3/20
\]

for every proper nonempty row or column subset. In particular
\(r_i,c_j>40/47>17/20\). This proof does not use Hall dilation.

The finite definition of the maximal Hall deficit gives a critical pair
whenever \(\tau>0\). For that pair set

\[
a=|I^c|,\quad b=|J^c|,\quad p=7-a-b\ge1,
\quad x=s_A(I^c,J^c).
\]

Write \(e,f\) for the respective complementary row and column excesses,
with an empty complement assigned excess zero. Inclusion--exclusion gives

\[
p\tau=e+f-x\le e_++f_+<14/47<1.
\]

Thus \(\tau<1\) before any use of \(A/(1-\tau)\). If one complement is
empty, the sharper \(p\tau<7/47\) holds. This explicitly repairs the omitted
n=7 dilation precondition at TeX lines 237--244 and 330--351.

The Hall domination lemma is the usual unit-capacity bipartite max-flow
criterion: all cut capacities are at least seven exactly when
\(s_S(I,J)\ge |I|+|J|-7\). Hence \(S=A/(1-\tau)\) dominates a doubly
stochastic \(B\). For the critical pair,

\[
s_B(I,J)-s_B(I^c,J^c)=p,
\quad s_B(I,J)\le s_S(I,J)=p.
\]

It follows that \(B[I^c,J^c]=0\), and \(B[I,J]=A[I,J]/(1-\tau)\)
entry by entry. Every zero of \(A\) is a zero of \(B\). Neither uniqueness
of \(B\) nor uniqueness of the critical pair is required.

When \(\tau=0\), the dominated \(B\) has the same total mass as \(A\),
so \(A=B\). A boundary \(A\) then has a zero and
\(H\ge\kappa_7>\gamma\), a contradiction. Thus a boundary maximizer has
\(0<\tau<1\). This covers both endpoints of the dilation construction.

## 3. Permanent and entropy inputs

The needed derivative-capacity inequality and preservation of stability
under extraction are supported by [Gurvits, arXiv:0711.3496v2](https://arxiv.org/html/0711.3496v2),
Theorem 4.10 and Fact 4.9. The polynomials here are homogeneous, have
nonnegative coefficients, and are products of nonnegative linear forms or
their derivatives and zero specializations. Upper-half-plane real stability
and the half-plane convention in that source agree for these homogeneous
polynomials after a common rotation of all variables. Positive capacity
prevents an extraction used here from being the zero polynomial.

For clarity, the degree-one case omitted from the reconstruction's displayed
choice \(t=d/((d-1)\sum\lambda_h)\) is immediate: for
\(f(t)=a+bt\), \(\inf_{t>0}f(t)/t=b=f'(0)\), and \(G(1)=1\).
For \(d\ge2\) the displayed choice and AM--GM are valid. If \(f(0)=0\),
factoring its initial power of \(t\) proves the same inequality, including
the zero-capacity case.

### Dimension-independent rectangular zero-block lemma

Let \(n,a,b,p\) be integers with \(a,b,p\ge1\) and \(n=a+b+p\).
Every nonnegative doubly stochastic \(n\times n\) matrix \(B\) having an
\(a\times b\) zero block satisfies

\[
\operatorname{per}(B)\ge
L_{n,a,b}^{\sharp}:=\frac{v_{n-a}v_{n-b}}{v_p},
\qquad v_k=k!/k^k.
\]

This is a dimension-independent application of Gurvits's extraction
inequality to the forced zero block, as used in Lu's attributed architecture.
It requires no separate zero-block extremizer theorem.

To prove it, move the zero block to the first \(a\) rows and first \(b\)
columns, and write the row-form product
\(P_B(x)=\prod_{i=1}^n\sum_jb_{ij}x_j\). Weighted AM--GM gives
\(\operatorname{Cap}(P_B)=1\). None of the first \(a\) factors contains
\(x_1,\ldots,x_b\). After taking the square-free coefficient in the first
\(h\) of these variables, where \(0\le h<b\), the resulting polynomial is
a sum over assignments of those \(h\) variables to distinct rows outside
the first \(a\) rows. Each summand retains the first \(a\) row factors and
only \(n-a-h\) other row factors. Thus its degree in \(x_{h+1}\), and hence
the degree of the whole polynomial in that variable, is at most
\(n-a-h\). All coefficients are nonnegative.

Each successive derivative followed by specialization at zero remains
stable or is zero. Its capacity remains positive by Gurvits's inequality,
so the zero case cannot occur in this argument. The actual selected-variable
degree is at least one; a polynomial independent of that variable would
have zero capacity, by sending the unused variable to infinity.

The function \(G(d)=((d-1)/d)^{d-1}\), with \(G(1)=1\), decreases with
integer \(d\). For real \(x>1\), the logarithmic derivative is
\(\log(1-1/x)+1/x<0\), which also gives the needed integer monotonicity.
Consequently the first \(b\) extractions preserve a capacity factor at
least

\[
\prod_{h=0}^{b-1}G(n-a-h)
=G(n-a)\cdots G(p+1)=v_{n-a}/v_p.
\]

The remaining polynomial has degree \(n-b\) in \(n-b\) variables and
nonnegative coefficients. Full square-free extraction gives the further
factor \(v_{n-b}\). That coefficient is precisely \(\operatorname{per}(B)\),
which proves the displayed lower bound.

The constant is attained. Set \(m=n-a=b+p\) and \(\ell=n-b=a+p\), and take

\[
B_*=\begin{pmatrix}
0_{a\times b}&\ell^{-1}J_{a,\ell}\\
m^{-1}J_{m,b}&p(m\ell)^{-1}J_{m,\ell}
\end{pmatrix}.
\]

Its row and column sums are one. A perfect matching first assigns the
\(a\) top rows injectively to the \(\ell\) right columns and the \(b\) left
columns injectively to the \(m\) bottom rows; the remaining \(p\) rows and
columns are matched within the core. The resulting permanent is

\[
\frac{\ell!}{p!}\frac{m!}{p!}p!\,
\ell^{-a}m^{-b}\left(\frac{p}{m\ell}\right)^p
=\frac{v_m v_\ell}{v_p}.
\]

In dimension seven this gives exactly

\[
\operatorname{per}(B)\ge L_{7,a,b}^{\sharp}
=v_{7-a}v_{7-b}/v_p.
\]

In particular the \(a=b=1\) case gives
\(\operatorname{per}(B)\ge v_6G(6)=\kappa_7>v_6G(7)=\gamma\).
This establishes the boundary constant directly, independent of the
potentially ambiguous phrase about putting a column "last" in the extraction.

### Complementary-minor entropy, including zero entries

Let \(M\) be a positive doubly stochastic matrix of size \(m\), with selected
column \(q\), remaining row forms \(L_i\), and complementary permanents \(d_i\).
For arbitrary positive \(t_i\),

\[
Q_t=\sum_i q_i t_i\prod_{k\ne i}L_k
\]

is a stable homogeneous polynomial of degree \(m-1\) in \(m-1\) variables,
as it is the coefficient of \(z\) in
\(\prod_i(L_i+q_i t_i z)\). Weighted AM--GM gives

\[
\operatorname{Cap}(Q_t)
\ge\prod_i t_i^{q_i}\prod_i(1-q_i)^{1-q_i}.
\]

Indeed, the first application has weights \(q_i\); the second uses the
remaining entries of each row divided by \(1-q_i\). The exponent of each
remaining variable after the latter application is its column sum, one.
Extraction and \(t_i=1/d_i\) therefore yield

\[
\prod_i d_i^{q_i}
\ge v_{m-1}\prod_i(1-q_i)^{1-q_i}
=v_m\exp\Psi_m(q).
\]

For a nonnegative \(M\), the smoothing
\(M_\varepsilon=(1-\varepsilon)M+\varepsilon U_m\) is legitimate.
If \(q_i>0\), Birkhoff decomposition shows
that the selected positive entry belongs to a positive permutation, hence
\(d_i>0\). If \(q_i=0\), its smoothed exponent is \(\varepsilon/m\), and
the minor is bounded below by
\((m-1)!(\varepsilon/m)^{m-1}\) and above by a fixed constant. Its
logarithm times that exponent tends to zero. Consequently the stated
zero-exponent convention follows by a genuine limit. No positivity of all
original minors is being assumed.

For the entropy estimate, \(h(x)=(1-x)\log(1-x)\) has
\(h''(x)\ge1+x\). Taylor expansion at \(u=1/m\), followed by
\((q_i-u)^3\ge-u(q_i-u)^2\), gives

\[
\Psi_m(q)\ge(1/2+1/(3m))\sum_i(q_i-1/m)^2.
\]

Continuity covers coordinates equal to one. The column entropy inequality
is the same capacity calculation with every \(t_i=1\).

### Complete p=1 core-entropy deduction

Permute the zero block to the upper left and write

\[
B=\begin{pmatrix}0_{a\times b}&X\\Y&Z\end{pmatrix},
\qquad a+b+1=7.
\]

The core \(Z\) has mass one. Let its row and column marginals be \(\xi\)
and \(\zeta\), of lengths \(m=b+1\) and \(\ell=a+1\).
The matrices \([Y\mid\xi]\) and \([X^T\mid\zeta]\) are doubly
stochastic of orders \(m\) and \(\ell\). Their complementary permanents
are \(d_i=\operatorname{per}(Y\text{ with row }i\text{ removed})\)
and \(h_j=\operatorname{per}(X\text{ with column }j\text{ removed})\).

Every perfect matching of \(B\) uses precisely one core edge, so

\[
\operatorname{per}(B)=\sum_{i,j}Z_{ij}d_i h_j
\ge\prod_i d_i^{\xi_i}\prod_j h_j^{\zeta_j}
\ge v_m v_\ell\exp\{\Psi_m(\xi)+\Psi_\ell(\zeta)\}.
\]

The weights \(Z_{ij}\) sum to one. A positive weight has both positive
marginals, so both associated minors are positive by the preceding argument;
zero weights are omitted. Because \(v_1=1\), \(v_m v_\ell=L_{7,a,b}^{\sharp}\).
In particular this proves the exponential bound

\[
\operatorname{per}(B)\ge L_{7,a,b}^{\sharp}e^{s/2},
\quad s=s_m(\xi)+s_\ell(\zeta),
\]

which is needed at TeX lines 549--554, not merely the weaker displayed
linear bound in the statement of the core-entropy proposition.

## 4. Cut coverage and scalar exclusions

The following list covers every critical pair with \(\tau>0\), up to
transposition. Permuting row and column indices does not change the argument.

| Class | Complete parameters | Method |
| --- | --- | --- |
| One-sided | \(a=0, 1\le b\le6, p=7-b\) | Stationarity and column entropy |
| Two-sided, \(p\ge2\) | \((a,b)=(1,1),(1,2),(1,3),(1,4),(2,2),(2,3)\) | Six scalar margins |
| Two-sided, \(p=1\), a nonpositive excess | \((a,b)=(1,5),(2,4),(3,3)\), either \(e\le0\) or \(f\le0\) | Six sign configurations, five distinct margins |
| Two-sided, \(p=1\), both excesses positive | The same three pairs, \(e,f>0\) | Three bivariate alternatives |

The case \(a=b=0\) has \(\tau=0\) and is already excluded. Neither
complement can have size seven since \(|I|+|J|>7\). Both excesses cannot
be nonpositive when \(p\tau=e+f-x>0\). Zero excesses are included in the
sign-mixed class. No unlisted arrangement of individual zero entries needs
a separate case, since every bound holds for every dominated \(B\) with
the specified forced zero block.

The sharper subset bound is obtained by retaining the largest value of
\(u(1-u)\) on the localized interval. For \(k\le3\), that interval lies
strictly below \(1/2\), so the upper endpoint gives the reconstruction's
\(\alpha_{7,k}\). For \(k\ge4\), \(u(1-u)\) decreases along the positive
excess interval, so the initial endpoint gives \(2k(7-k)/7\). This justifies
both branches and their directions.

By Cauchy--Schwarz and the joint deficit budget,

\[
\tau^2\le\frac{\alpha_{7,a}+\alpha_{7,b}}{p^2}
\frac{\delta}{1-\delta}.
\]

For a sign-mixed \(p=1\) cut only the positive excess contributes, so the
coefficient is the corresponding single \(\alpha\). The bounds imply
the intervals stated in the note. In particular
\(\alpha_{7,k}<7/2\), and the certified comparison for \(T=5/24\) is
even weaker than the \(p\ge2\) bound requires.

On the relevant interval,
\((1-t)^7\ge1-7t+(21-35T)t^2\). The remaining binomial terms are
\(t^4(35-21t+7t^2-t^3)\ge0\) there. Taking

\[
\lambda=329/24\quad(T=5/24),\qquad
\lambda=63/4\quad(T=3/20)
\]

is therefore valid. If the Hall bound has coefficient \(c>0\), then
\(\delta\ge(1-\gamma)\tau^2/c\). Consequently

\[
H-L(1-\tau)^7
\le\gamma-L+7L\tau-
\{\lambda L+(1-\gamma)/c\}\tau^2
\le-M_7^{(2)}(L,c,\lambda).
\]

The last step maximizes a concave quadratic over all real \(\tau\),
so it remains a valid upper bound on the allowed interval. A positive
margin contradicts \(A\ge(1-\tau)B\). No reversal in the scalar squeeze
was found.

## 5. One-sided cuts

For \(a=0\), the \(p\) selected columns have total \(p\theta\), where
\(\theta=1-\tau\). Each has total at least \(\theta\) because it dominates
the corresponding column of \(\theta B\). Equality of the combined total
therefore forces every selected column sum to be \(\theta\), and every
one of those columns is saturated entry by entry.

Let \(\beta\) be the average of those probability columns of \(B\).
The selected entries of row \(i\) have mass \(p\theta\beta_i\), and each
permanent monomial uses exactly \(p\) selected entries. Substituting these
facts in the normalized block variation gives the exact identity

\[
D:=1-\sum_i\frac{\beta_i}{r_i}
=\frac{\tau(C-H)}{\theta R}
\ge\frac{(1-\gamma)\tau}{\theta}>0.
\]

Here \(C-H=\Phi(A)-R\ge1-\gamma\), and \(R\le1\). This verifies the
direction and all denominators in TeX equation `D7`.

With \(y_i=1-1/r_i\), the integral estimate using
\(r_i>17/20\), together with
\(\rho\ge(1-\gamma)(-\log R)\), gives

\[
\rho\ge\frac{(1-\gamma)(17/20)^2}{2}\sum_i y_i^2
>\frac13\sum_i y_i^2.
\]

The strict last inequality applies here because \(D>0\) implies \(y\ne0\).
The harmonic-mean inequality gives \(\sum_i y_i\le0\), whence

\[
D^2\le s\sum_i y_i^2,
\quad s=\sum_i(\beta_i-1/7)^2>0,
\quad \rho>\frac{D^2}{3s}.
\]

Convexity of squared distance shows that at least one of the selected
columns has squared distance from uniformity at least \(s\). Column entropy
and entrywise domination give
\(H\ge\gamma\theta^7 e^{s/2}\), whereas \(H\le\gamma-\rho\).

Put \(q=\theta^7\). For every \(s>0\), not just \(s\ge s_0\),

\[
\rho+\gamma q e^{s/2}-\gamma
>\frac{D^2}{3s}+\frac{\gamma qs}{2}+\gamma(q-1)
\ge D\sqrt{2\gamma q/3}+\gamma(q-1).
\]

The lower bound for \(D\) makes the last quantity positive if

\[
\frac23(1-\gamma)^2(1-\tau)^5
>\gamma\left(\frac{1-(1-\tau)^7}{\tau}\right)^2.
\]

Localization has already established \(0<\tau<3/20\). On that interval,

\[
0<\frac{1-(1-t)^7}{t}\le7-21t+35t^2,
\qquad (1-t)^5\ge(1-t)^6.
\]

Thus the exact positive Bernstein coefficients of the reconstruction's
\(W(t)\) suffice. Squaring the upper bound is legitimate because both sides
are positive. This proves the one-sided exclusion for all six values of
\(b\), and also shows that the preceding \(s\le s_0\) case in the note
is redundant. Its stated small-entropy scalar condition is consistent:
completing the square gives
\(\kappa-\gamma-49\kappa^2 s/(4a)\), with
\(a=(1-\gamma)^2/3\); using
\(s\le2\log(\kappa/\gamma)\le2(\kappa-\gamma)/\gamma\)
reduces positivity to \(a\gamma>49\kappa^2/2\), exactly as claimed.

## 6. Both-positive single-bridge cuts

Here \(p=1\), \(e,f\in(0,3/20)\), and
\(t=e+f<3/10\). The denominators \(m-e\), \(\ell-f\), and \(1-t\) are
strictly positive, both on the feasible set and on the larger closed
certificate square. The product envelopes obey

\[
u_r=P_a(e)-R\ge0,\quad u_c=P_b(f)-C\ge0,
\quad u=\delta-(2-P_a-P_b)\ge u_r+u_c,
\quad H=K-u.
\]

### Conditional energy

The pointwise inequality behind the conditional-energy lemma is valid
even when a line sum is below its group mean. If \(z,\mu>0\), then

\[
z/\mu-1-\log(z/\mu)
\ge\frac{\min(z,\mu)^2}{2}(1/z-1/\mu)^2.
\]

To see this, integrate \(t/(1-t)^2\) from zero to \(1-\mu/z\).
For a nonnegative endpoint the denominator factor is at least one. For a
negative endpoint, reversing the limits gives a positive integral whose
denominator factor is at least \((z/\mu)^2\). Both yield the display.
Every group mean and every line sum exceeds \(17/20\). Sum the inequality
within both row groups; the linear deviations within each group sum to
zero. Minimizing squared reciprocal deviation at its own mean gives

\[
\log(P_a/R)\ge(17/20)^2V_I/2.
\]

Since \(R\ge1-\gamma\),
\(u_r=R(e^{\log(P_a/R)}-1)\ge V_I/3\). The analogous argument gives
\(V_J\le3u_c\). Thus the constant three used in the squeeze has its
required hypotheses, without assuming that individual rows are uniform
inside either group.

### Stationarity and entropy squeeze

If \(H_k\) is the permanent contribution using \(k\) entries in the forced
opposite block, its monomials have \(1+k\) core entries. The core has mass
\(\theta\) and row/column masses \(\theta\xi_i,\theta\zeta_j\).
The normalized block variation therefore gives exactly

\[
R\left(\sum_i\xi_i/r_i-1\right)
+C\left(\sum_j\zeta_j/c_j-1\right)
=\frac{\tau H+\sum_{k\ge1}kH_k}{1-\tau}.
\]

Here the variation scales existing entries and renormalizes; it is feasible
for parameters on both sides of one even though the maximizer is on the
boundary of the full simplex. Zero entries stay zero. No unauthorized
two-sided variation of a zero coordinate is being assumed.

All perfect matchings of \(B\) avoid its forced zero block. Consequently

\[
H_0\ge\theta^7\operatorname{per}(B)
\ge A_0e^{s/2},\qquad A_0=L_{7,a,b}^{\sharp}(1-e-f)^7>0,
\]

using \(\theta=1-e-f+x\ge1-e-f\).
Also \(\sum kH_k\le d(H-H_0)\), and
\(((\tau+d)H-dH_0)/(1-\tau)\) increases with \(\tau\), since its
derivative numerator is \((1+d)H-dH_0\ge H>0\).
The upper bound on the stationarity right side in TeX lines 583--588 is
therefore valid.

Harmonic mean and Cauchy--Schwarz give the stated lower bounds for its
left side. After substitution of \(R=P_a-u_r, C=P_b-u_c\), one obtains

\[
\mathcal B+cu-Eu_r-Fu_c
\le R\sqrt{s_IV_I}+C\sqrt{s_JV_J},
\quad c=(e+f+d)/(1-e-f),
\quad E=e/(m-e),\ F=f/(\ell-f).
\]

Since \(c\ge\max(E,F)\), \(u\ge u_r+u_c\), and \(0<R,C\le1\),

\[
\mathcal B\le\sqrt{s_IV_I}+\sqrt{s_JV_J}\le\sqrt{3su}.
\]

For \(\mathcal B>0\), squaring gives \(su\ge\mathcal B^2/3\).
From \(K-u=H\ge A_0(1+s/2)\),

\[
su\le\frac{2u(K-A_0-u)}{A_0}
\le\frac{(K-A_0)^2}{2A_0}.
\]

This covers \(u=0\) and \(s=0\), as well as their positive values. It does
not divide by either of them. If \(K<A_0\), the direct permanent bound has
already given a contradiction.

## 7. Exact formulas and certificate coverage

I read the primary implementation's sparse rational polynomial operations,
box rescaling, power-to-Bernstein conversion, de Casteljau subdivision,
all n=7 scalar and bridge builders, tree traversal, case-completeness checks,
and CLI. I also read the corresponding independently implemented
SymPy/NumPy tensor conversion, subdivision, n=7 scalar checks, bridge
builders and traversal, and CLI. The relevant code paths have no network
operations, subprocess calls, external mutations, or inexact comparisons.

The formula map is exact:

| Analytic object | Primary implementation | Independent implementation |
| --- | --- | --- |
| \(P_a(e),P_b(f)\) | `n7_product_envelope` | `n7_bridge_expressions` |
| \(K=\gamma-2+P_a+P_b\) | `upper_permanent` | `upper_permanent` |
| \(A_0=L(1-e-f)^7\) | `a0` | `a0` |
| \(\Delta=(m-e)(\ell-f)(1-e-f)\) | `denominator` | `delta` |
| \(\mathcal G=A_0-K\) | `direct` | `direct` |
| \(\mathcal N=\Delta\mathcal B\) | Explicit cleared `numerator` | `cancel(delta * squeeze)` |
| \(\mathcal F=2A_0\mathcal N^2-3(K-A_0)^2\Delta^2\) | `entropy` | `entropy` |

Both builders use \(d=\min(a,b)=a\) on the three canonical pairs and box
width \(3/20\) in each coordinate. Denominator clearing does not change
sign because \(\Delta>0\) throughout the closed box. The polynomial
\(K\) is not required to be positive throughout that larger box: a point
with \(K<A_0\) satisfies the direct alternative, and all feasible points
in the other alternative necessarily have \(K\ge A_0>0\).

For a tensor Bernstein representation, each basis function is nonnegative
and their sum is one on the closed box. A strictly positive minimum
coefficient therefore proves strict positivity at every point, including
edges. The conversion in both implementations uses the identity

\[
x^j=\sum_{i=j}^d\frac{\binom{i}{j}}{\binom{d}{j}}B_i^d(x).
\]

Both subdivision implementations are the exact de Casteljau construction
at \(1/2\). At each unresolved node the same coordinate is bisected for
all three polynomials, and both child boxes are added. A terminal node is
accepted only if all coefficients of \(\mathcal G\) are positive or all
coefficients of both \(\mathcal N\) and \(\mathcal F\) are positive.
The finite tree therefore certifies a pointwise alternative on the whole
square, not separate existential statements about unrelated boxes. Expected
tree counts are compared only after actual positivity tests; they are not
accepted in place of the tests.

The accepted alternative implies the needed contradiction. If
\(\mathcal G>0\), then \(H\ge A_0>K\ge H\). Otherwise
\(\mathcal N>0\) implies \(\mathcal B>0\), and \(\mathcal F>0\)
is precisely

\[
\frac{\mathcal B^2}{3}>\frac{(K-A_0)^2}{2A_0}.
\]

This is incompatible with the two bounds on \(su\). The test on the sign
of \(\mathcal N\) is essential and is present in both implementations.

The reported trees to be reproduced are

| Pair | Nodes | Direct leaves | Squeeze leaves | Depth |
| --- | ---: | ---: | ---: | ---: |
| \((1,5)\) | 39 | 10 | 10 | 8 |
| \((2,4)\) | 35 | 9 | 9 | 6 |
| \((3,3)\) | 47 | 11 | 13 | 8 |

For safe sequential execution from
`attack/dittert-completion-tree`, the n=7-only primary command is:

```sh
python3 -B study/external-proof/n6-n7/verify_dittert_n6_n7.py --dimension 7 --json
```

The independent CLI also runs n=6. Its n=7-only functions can be invoked
without changing the package:

```sh
python3 -B -c 'import sys,json; sys.path.insert(0,"study/external-proof/n6-n7"); import audit_dittert_n6_n7_sympy as a; print(json.dumps({"scalars":a.audit_n7_scalars(),"bridges":a.audit_n7_bridges()},sort_keys=True))'
```

The second command requires the package's declared NumPy/SymPy environment.
These are proposed execution commands; this audit does not represent them
as executed. Running all 98 n=6 four-variable certificates is unnecessary
to discharge the independent n=7 obligations reviewed here.

## 8. Equality and final logical scope

The supplemented proof starts with an arbitrary global maximizer and
excludes every boundary global maximizer through the exhaustive cut list.
The positive branch proves that every remaining maximizer is \(U_7\).
The compactness argument therefore establishes the inequality for every
matrix in \(K_7\). A matrix attaining the claimed bound is then a global
maximizer and hence is \(U_7\). Conversely \(U_7\) has the claimed value.
No equality classification is needed in the permanent entropy inequalities
or the Hall construction, because every boundary case ends in a strict
contradiction.

This review does not establish Dittert's conjecture in any dimension other
than seven, does not assess the n=6 smoothing reduction, and does not
establish novelty or priority. The rectangular zero-block lemma in section 3
is valid in every dimension with the stated parameters.
The resulting computer-assisted proof remains attributed to Lu's
source architecture and Nascimento's reconstruction. The only outstanding
evidence boundary for the n=7 conclusion in this review is the coordinating
agent's recorded exact certificate execution.
