# Exhaustive Hall-cut coverage in dimensions 8 through 15

This is an independent reconstruction of the coverage argument in Pedro Paulo
Marques do Nascimento's pinned proof, not a novelty claim:
https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701.
The prior review verdicts are not premises. The finite arithmetic obligations
below are separately identified so that a successful arithmetic check cannot
hide an omitted analytic branch.

## 1. Statement and imported interfaces

For each integer \(8\le n\le15\), no boundary global maximizer exists for
\(\Phi(A)=R+C-P\) on nonnegative real \(n\) by \(n\) matrices whose entry sum
is \(n\). Here \(R=\prod r_i\), \(C=\prod c_j\), \(P=\operatorname{per}(A)\),
and \(\gamma_n=n!/n^n\).

The argument imports these precise mathematical inputs.

1. Cheon--Wanless, DOI 10.1016/j.laa.2010.08.041, excludes partly decomposable
   maximizers and maximizers whose entire nonempty zero set is one rectangle.
   Their Hall criterion says a nonnegative matrix dominates a doubly
   stochastic matrix if its \(I\) by \(J\) sum is at least
   \(|I|+|J|-n\) for every positive right-hand side.
2. A doubly stochastic matrix with an \(a\) by \(b\) zero rectangle,
   \(a,b\ge1,\ p=n-a-b\ge1\), has permanent at least
   \(\nu_{n,a,b}=\gamma_{n-a}\gamma_{n-b}/\gamma_p\).
   In particular a matrix with one zero has permanent at least
   \(\kappa_n=(n-2)!((n-2)/(n-1)^2)^{n-2}\).
   The parent's capacity proof, based on Gurvits arXiv:0711.3496, supplies
   this interface without assuming a particular face minimizer.
3. For \(n=8,9,10\), two zeros in distinct rows and columns give the stronger
   floor \(L_n=\kappa_n(1+1/(2n^2))\). The parent's separate Minc-averaging
   and exact-polynomial audit supplies this interface. The parent visually
   inspected Pula--Song--Wanless, Section 2, page 3, which assumes BOTH
   parameters are at least 2, and therefore includes the required face
   with second parameter 2. The earlier audits' report of a strict
   inequality here was a text-extraction error. The primary PDF is
   https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1022.pdf;
   its parent archive has SHA256
   b6da230c790cbf18aaae182aa9c4775a50b29fe30a42606a1937d254394ab908.
4. Van der Waerden's permanent bound has equality only at the uniform
   doubly stochastic matrix.

This child proves coverage after those mathematical interfaces. It does not
claim that an exact checker itself proves a published structural theorem or
the Minc averaging theorem. The common floor interfaces must be discharged
by the parent for the assembled matrix theorem.

## 2. Global budget and a complete classification of minimizing cuts

The feasible simplex is compact. The uniform matrix gives
\(\Phi\ge2-\gamma_n\) at any global maximizer. Since \(R,C\le1\), write
\[
 P=\gamma_n-\delta,\qquad R=1-\rho,\quad C=1-\sigma,\qquad
 0\le\rho,\sigma,\quad \rho+\sigma\le\delta\le\gamma_n.
\]
Thus \(R,C\ge1-\gamma_n>0\), and every row and column sum is positive.

A nonempty zero set without two independent zeros lies in one row or one
column. To prove this, fix a zero \((i,j)\). Every other zero must lie in
row \(i\) or column \(j\); a zero in each direction outside \((i,j)\) would
be an independent pair. Such a complete zero set is a rectangle. The
structural exclusion therefore supplies two independent zeros.

Define
\[
 \lambda=\min_{|I|+|J|>n}
 \frac{s_A(I,J)}{|I|+|J|-n},\qquad u=1-\lambda.
\]
The minimum is attained because there are finitely many cuts. A zero
numerator would contain a zero rectangle whose dimensions sum to \(n\),
contrary to full indecomposability. The full numerator is \(n>0\).
Consequently \(0<\lambda\le1\) and \(0\le u<1\). The Hall criterion applied
to \(A/\lambda\) supplies doubly stochastic \(B\) with \(\lambda B\le A\).
All zeros of \(A\) remain zeros of \(B\), and monotonicity and homogeneity
of the permanent give \(P\ge(1-u)^n\operatorname{per}(B)\).

Every minimizing cut has unique omitted-size parameters
\[
 a=n-|I|\ge0,\quad b=n-|J|\ge0,\quad a+b\le n-1.
\]
These parameters divide into exactly three cases.

- Full: \(a=b=0\).
- Marginal: exactly one of \(a,b\) is zero.
- Proper: \(a,b\ge1\) and \(a+b\le n-1\).

In the full case \(\lambda=1\). More generally, ANY cut with \(\lambda=1\)
gives \(B\le A\) and equal total mass, hence \(A=B\). It follows that
\(P>\gamma_n\) for a boundary matrix, contradicting the budget. This
also handles the endpoint \(u=0\), including tied cuts.

For a marginal cut with \(b=0\), its ratio is the average row sum over
\(I\). Singleton row cuts occur in the same global minimum, so
\[
 \lambda\le\min_i r_i\le \frac{\sum_{i\in I}r_i}{|I|}=\lambda.
\]
Thus its minimum is realized by one smallest row. A cut with \(a=0\)
becomes this case under transposition. Every marginal cut, including
ties and larger subsets, therefore reduces to \((a,b)=(n-1,0)\).
This is a proved reduction, not an omitted loop range.

For a proper tight cut put \(p=n-a-b\). Double stochasticity gives
\(s_B(I,J)=p+s_B(I^c,J^c)\ge p\), while domination gives
\(\lambda s_B(I,J)\le s_A(I,J)=\lambda p\).
Since \(\lambda>0\), \(B[I^c,J^c]=0\). The proper floor \(\nu_{n,a,b}\)
therefore applies even if \(B\) has other zeros. There is no assertion
that the added rectangle is zero in \(A\).

The scalar constants depend only on \(n,a,b\) and are symmetric in
\(a,b\). Arbitrary index sets of the same cardinalities therefore satisfy
the same bound. Transposition merely identifies equal scalar formulas.
The independent checker nevertheless enumerates every ordered proper
pair and both marginal orientations. It also checks that all uncompressed
size pairs map to a certified case.

## 3. A deficit bound derived before localization

Let \(x_i>0\), \(\sum x_i=n\), \(X=\prod x_i\ge1-\gamma_n\), and let a
\(d\)-element subset have sum \(d+e\), with \(1\le d<n\). Positivity gives
\(-d<e<n-d\). Grouped AM--GM gives \(X\le\exp(-g(e))\), where
\[
 g(e)=-d\log(1+e/d)-(n-d)\log(1-e/(n-d)).
\]
We have \(g(0)=g'(0)=0\) and
\[
 g'(e)=\frac{ne}{(d+e)(n-d-e)}.
\]
The denominator is at most \(n^2/4\). Integrating towards either sign of
\(e\) gives \(g(e)\ge2e^2/n\). Also
\[
 g(e)\le-\log X\le-\log(1-\gamma_n)
 \le\frac{\gamma_n}{1-\gamma_n}.
\]
The finite exact checks establish, for EACH \(8\le n\le15\),
\[
 \frac{n\gamma_n}{2(1-\gamma_n)}<\frac1{100},
 \qquad \frac{\gamma_n}{1-\gamma_n}<\frac1{400}.
\]
Thus \(|e|<1/10\) follows globally from the product budget, with no
small-branch assumption.

On this interval,
\[
 g''(0)=\frac{n}{d(n-d)},\qquad
 |g'''(e)|\le\frac{2000}{729}g''(0).
\]
Indeed each cubic denominator is bounded below using
\(1\pm e/d\ge9/10\), and
\(1/d^2+1/(n-d)^2\le1/d+1/(n-d)\).
Taylor's theorem yields
\[
 g(e)\ge\frac{1987}{4374}g''(0)e^2.
\]
Using \(1-e^{-g}\ge g/(1+g)\), \(g<1/400\), and the strict rational
comparison \((1987/2187)(400/401)>7/8\), we obtain
\[
 1-X\ge \frac{7n}{16d(n-d)}e^2. \tag{D}
\]
This proof covers positive, zero, and negative deviations.

For a proper cut let \(e,f\) be the omitted row and column excesses, and
let \(t=s_A(I^c,J^c)\ge0\). Inclusion-exclusion gives exactly
\[
 s_A(I,J)=p-e-f+t,\qquad pu=e+f-t\le e+f.
\]
Apply (D) to rows and columns, and use weighted Cauchy--Schwarz:
\[
 \delta\ge\rho+\sigma\ge
 \frac{7n e^2}{16a(n-a)}+\frac{7n f^2}{16b(n-b)}
 \ge\frac{7n(e+f)^2}{16\{a(n-a)+b(n-b)\}}
 \ge C_{n,a,b}u^2,
\]
where
\[
 C_{n,a,b}=\frac{7np^2}{16\{a(n-a)+b(n-b)\}}>0. \tag{C}
\]
The final inequality is legitimate because \(e+f\ge pu\ge0\).
No sign of either excess is omitted.

## 4. Marginal stationarity, including all denominator domains

At a global maximizer, all partial derivatives on positive entries agree,
because both directions of a sufficiently small mass transfer are feasible.
Euler's identity and the total mass \(n\) identify this derivative as
\(\Phi(A)\). Hence
\[
 R/r_i+C/c_j-\operatorname{per}A(i\mid j)=\Phi(A)
 \quad\hbox{whenever }a_{ij}>0. \tag{S}
\]
No derivative condition on a zero entry is used.

For the selected minimum row \(r_i=1-u\), multiply (S) by \(a_{ij}\) and
sum. The result is
\[
 q_i=\sum_j a_{ij}/c_j=1-(1+\theta)u,\qquad
 \theta=(R-P)/C\ge1-\gamma_n.
\]
The inequality follows from \(R-P=\Phi-C\ge1-\gamma_n>0\) and \(C\le1\).
Since the row has positive mass, \(q_i>0\). Therefore
\[
 E(u)=1-(2-\gamma_n)u\ge q_i>0.
\]
This establishes positivity BEFORE dividing. Since \(q_i\) is the weighted
sum of \(1/c_j\) over the positive row entries, at least one incident
column has \(c_j\ge r_i/q_i\). For that same incident column,
\[
 c_j\ge \frac{1-u}{E(u)}=1+h(u),\qquad
 h(u)=\frac{(1-\gamma_n)u}{E(u)}\ge(1-\gamma_n)u.
\]
The actual column has \(c_j<n\) since every other column sum is positive.
Thus \(0\le h(u)<n-1\) for every feasible parameter.

Applying (D) to the minimum row and the selected column gives
\[
 \delta\ge C_{n,n-1,0}u^2,\qquad
 C_{n,n-1,0}=\frac{7n}{16(n-1)}
      \{1+(1-\gamma_n)^2\}>0. \tag{CM}
\]
This is global for marginal cuts. In particular it does not presuppose
that \(u\) is near zero.

## 5. All proper cuts for n=8,9 and every cut for n=10,...,15

For \(n=11,\ldots,15\), use \(M=\nu\) on each proper cut and \(M=\kappa_n\)
on the normalized marginal cut. Exact rational arithmetic verifies
\[
 M-\gamma_n-\frac{n^2M^2}{4C}>0. \tag{H}
\]
Here \(C\) is (C) or (CM). For every \(u\in[0,1]\), Bernoulli and
completion of the square imply
\[
 M(1-u)^n-\gamma_n+Cu^2
 \ge C\left(u-\frac{nM}{2C}\right)^2
    +M-\gamma_n-\frac{n^2M^2}{4C}>0.
\]
The interval is the whole possible Hall domain. There is no fixed-point
branch choice and no parameter cutoff.

For \(n=8,9,10\), use \(M=\max(\nu,L_n)\) on proper cuts and \(M=L_n\)
on normalized marginal cuts. Equations (C),(CM), already proved globally,
give \(u^2\le\gamma_n/C\). Choose the least positive multiple \(\bar u\)
of \(10^{-6}\) satisfying \(\bar u^2\ge\gamma_n/C\).
The checker verifies both the enclosure and \(0<\bar u<1\) separately
for every cut, including all the weakest \(p=1\) cases.

Define
\[
 \beta=\frac{(1-\bar u)^n-1+n\bar u}{\bar u^2}.
\]
For \(0\le u\le\bar u\), the integral remainder
\[
 \frac{(1-u)^n-1+nu}{u^2}
 =n(n-1)\int_0^1(1-t)(1-ut)^{n-2}\,dt
\]
extends continuously to \(u=0\) and decreases with \(u\).
Thus \((1-u)^n\ge1-nu+\beta u^2\) throughout the entire feasible range,
including both endpoints. Exact arithmetic verifies
\[
 M-\gamma_n-\frac{n^2M^2}{4(C+\beta M)}>0 \tag{L}
\]
for every proper cut in \(n=8,9,10\), and also the marginal cut in \(n=10\).
The only nonpositive margins are exactly \((8,7,0)\) and \((9,8,0)\).

Positive (H) or (L) contradicts
\[
 0=P-\gamma_n+\delta
 \ge M(1-u)^n-\gamma_n+Cu^2.
\]
The counts of proper ordered pairs are \((n-1)(n-2)/2\), namely
21,28,36,45,55,66,78,91. Adding one normalized marginal type gives
22,29,37,46,56,67,79,92. The full cuts were excluded analytically.
No statement for \(n>15\) or monotonic extension is needed.

## 6. All remaining marginal parameters for n=8 and n=9

Write
\[
 f(u)=(1-u)(1+u/(n-1))^{n-1},\qquad
 g(h)=(1+h)(1-h/(n-1))^{n-1}.
\]
The selected minimum row gives \(R\le f(u)\), and the selected excessive
column gives \(C\le g(h(u))\). The second inequality uses that \(g\)
decreases on \(0\le h<n-1\), as follows directly by logarithmic
differentiation. Likewise \(f\) decreases for \(0\le u<1\), and \(h\)
increases while \(E>0\). Consequently
\(D(u)=2-f(u)-g(h(u))\) increases throughout the feasible domain.

Exact rational tests show \(D(v)>\gamma_n\), with
\[
 (n,s,v)=(8,1/400,1/20)\quad\hbox{or}\quad(9,1/500,3/100).
\]
The checker also verifies \(E(v)>0\) and \(h(v)<n-1\).
If a feasible \(u\ge v\) existed, its entire intervening interval would
have \(E>0\) and \(h<n-1\) by monotonicity and feasibility. Hence
\(\delta\ge D(u)\ge D(v)>\gamma_n\), impossible.
This excludes the whole tail \([v,1)\) wherever the stationarity
denominators could be feasible. Parameters beyond the pole are already
impossible by \(E>0\). This is a global tail proof, not an endpoint test
assumed to imply monotonicity.

On the closed interval \([0,s]\), certify
\[
 L_n(1-u)^n-\gamma_n+D(u)>0. \tag{N}
\]
The independent checker clears only \(E(u)^n>0\) and uses rational
Bernstein subdivision; the source independently uses Sturm root counts.
In particular \(u=0\) is included and has gap \(L_n-\gamma_n>0\).

It remains to cover \([s,v]\). Define
\[
 q(u)=2-\gamma_n-(1-h(u)/(n-1))^{n-1}.
\]
The checker verifies \(q(s)>1\); monotonicity then gives \(q>1\)
throughout this closed interval. For every row \(\ell\) meeting the
same chosen column, (S), cofactor nonnegativity, and AM--GM on the other
columns give
\[
 R/r_\ell\ge \Phi-C/c_j
 \ge2-\gamma_n-(1-h(u)/(n-1))^{n-1}=q(u).
\]
Since \(R\le1\), all these rows satisfy \(r_\ell\le1/q(u)<1\).

Let \(z\) be the zero count in that column. These are all possible cases:
\(z=n\) contradicts positive column sum; \(z=n-1\) contradicts the
partly-decomposable exclusion; \(z=0\) caps all row sums below one and
contradicts their sum \(n\). Therefore \(1\le z\le n-2\).

Set \(m=n-1-z\) and \(b_0=1/q<1\). Besides the fixed row \(1-u\), there
are \(m\) other incident rows \(x_j\le b_0\), and \(z\) remaining rows.
Their product is bounded above by
\[
 (1-u)\prod_{j=1}^m x_j
 \left(\frac{n-1+u-\sum x_j}{z}\right)^z.
\]
The remaining average is larger than one on the entire box
\(0<x_j\le b_0\): its numerator exceeds \(z+u\).
The derivative of the logarithm with respect to \(x_j\) is
\(1/x_j-z/(n-1+u-\sum x_j)>0\). Raising every \(x_j\) to its cap is
therefore legitimate and gives
\[
 R\le U_z(u)=(1-u)q^{-m}
 \left(\frac{n-1+u-m/q}{z}\right)^z.
\]
This maximizes over a larger feasible set, so no hidden realizability
assumption is needed.

For \(n=8\), the column's \(z\) by 1 zero block persists in \(B\). Use
\(M_z=\max(L_8,\gamma_{8-z}\gamma_7/\gamma_{7-z})\) and check every
\(z=1,\ldots,6\). For \(n=9\), use the uniform floor \(M_z=L_9\).
Removing one cap enlarges the feasible product set, proving
\(U_z\le U_{z+1}\). Thus the certificate at \(z=7\) implies every case
\(z=1,\ldots,7\). This implication relies on the floor being independent
of \(z\), which is why the same compression is not used in dimension 8.

For each necessary certificate prove
\[
 M_z(1-u)^n-\gamma_n+2-U_z(u)-g(h(u))>0. \tag{S8/9}
\]
For an explicit polynomial version set \(E=1-(2-\gamma_n)u\),
\(H=(1-\gamma_n)u\), \(T=E-H/(n-1)\), and
\[
 Q=(2-\gamma_n)E^{n-1}-T^{n-1},\quad
 W=(n-1+u)Q-mE^{n-1},
\]
\[
 S=(2-\gamma_n+M_z(1-u)^n)E^n-(E+H)T^{n-1}.
\]
Then (S8/9) is exactly positivity of
\[
 G_z=z^zQ^{n-1}S-(1-u)E^{n+(n-1)m}W^z.
\]
The cleared multiplier is \(z^zQ^{n-1}E^n>0\), since \(z\ge1\),
\(E>0\) and \(Q=E^{n-1}q>0\). Also \(T>0\) follows from \(h<n-1\).
The literal polynomial has degree at most \(n^2+1\), namely 65 or 82.
The independent checker builds it directly in the Bernstein basis on
the required closed interval; the source uses power coefficients and
a separate basis conversion.

All junctions are included:
\[
 [0,s]\ \cup\ [s,v]\ \cup\ [v,1)=[0,1).
\]
The first two have strictly positive certificates; the third violates
the budget (or the already proved stationarity denominator condition).
This covers every feasible marginal parameter and support pattern.

## 7. Deduction and scope

Every minimizing cut is full, marginal, or proper. Sections 2 through 5
exclude all except the two marginal dimension cases; Section 6 excludes
those for all real parameters, all column supports, and all endpoints.
Thus, after the stated permanent-floor and structural interfaces are
discharged, no boundary global maximizer remains in any of n=8,...,15.

This conclusion does not certify the old Sinkhorn large-cost route.
It replaces that incomplete route by a different scalar parameter whose
entire feasible range was handled above. The hypotheses used here hold
at EVERY boundary global maximizer, independent of the value of the old
Sinkhorn cost.
