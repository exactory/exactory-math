# An assembled proof of Dittert's conjecture for 5 <= n <= 15

This document combines the existing local certificates with public proof
material located and independently checked in this attack. It does not claim
a new discovery or a Lean formalization of the full theorem. The dimension 7
method is attributed to Hongyuan Lu. The reconstruction used here and the
unified treatment of dimensions 8 and above are attributed to Pedro Paulo
Marques do Nascimento.

## Theorem

For every integer \(5\le n\le15\) and every nonnegative real matrix
\(A=(a_{ij})\in\mathbb R^{n\times n}\) whose entries sum to \(n\), let
\(r_i\) and \(c_j\) denote its row and column sums and put
\(\gamma_n=n!/n^n\). Then

\[
\Phi(A):=\prod_i r_i+\prod_j c_j-\operatorname{per}(A)
\le 2-\gamma_n.
\]

Equality holds if and only if every entry is \(1/n\).

## Proof components and computational evidence

| Dimension | Proof component | Computational evidence |
|---|---|---|
| 5 | [Existing SOS certificate](../dittert-conjecture-n5-to-n15/deterministic/certified-special-case-check-1/README.md) | Existing result.json in that directory |
| 6 | [Existing certificate](../dittert-conjecture-n5-to-n15/deterministic/certified-special-case-check-2/README.md) and [integer Gram verification](../dittert-conjecture-n5-to-n15/deterministic/certified-special-case-check-4/README.md) | Existing result.json files and [full integer-run log](study/inherited-n6-exact-psd.log); matrix computation not rerun |
| 7 | [Independent audit and supplementary proofs](study/audit-n7.md) | [Primary and independent checks](deterministic/certified-special-case-check-3/README.md), freshly passed |
| 8, 9 | [Independent analytic audit](study/audit-n8-n9.md) | [Four exact verifiers](deterministic/certified-special-case-check-2/README.md), freshly passed |
| 10 through 15 | [Analytic rederivation](study/audit-n10-n15.md) | [Unified check and new independent implementation](deterministic/certified-special-case-check-1/README.md), freshly passed |

The following argument connects these components. The linked audits supply
the detailed lemmas, denominator checks, boundary cases, and correspondence
between mathematical formulas and verifier code.

## 1. Reduction to global maximizers

The feasible set is compact and \(\Phi\) is polynomial, so a global maximizer
exists. The uniform matrix has value \(2-\gamma_n\). For any global
maximizer put \(R=\prod r_i\), \(C=\prod c_j\), and
\(P=\operatorname{per}(A)\). AM--GM gives \(R,C\le1\), and hence

\[
P=\gamma_n-\delta,\quad R=1-\rho,\quad C=1-\sigma,
\qquad 0\le\rho,\sigma,\quad \rho+\sigma\le\delta\le\gamma_n.
\]

In particular all line sums are positive. Hwang's positive-maximizer
theorem says that a strictly positive maximizer must be uniform. The
dimension 7 audit also gives a supplementary averaging argument with its
limiting step justified. It therefore suffices to exclude every boundary
maximizer.

## 2. Zero-preserving Hall scaling

Set

\[
\lambda=\min_{|I|+|J|>n}
\frac{\sum_{i\in I,j\in J}a_{ij}}{|I|+|J|-n},
\qquad u=1-\lambda.
\]

For \(n\ge8\), Cheon--Wanless's exclusion of partly decomposable
maximizers guarantees \(\lambda>0\). For \(n=7\), the independently proved
subset-sum localization does so. The full cut gives \(\lambda\le1\).
The capacitated Hall condition produces a doubly stochastic matrix \(B\)
such that

\[
\lambda B\le A,\qquad P\ge\lambda^n\operatorname{per}(B).
\]

This \(B\) is a dominated doubly stochastic matrix, not the Sinkhorn
scaling used in the earlier unsuccessful attack.

For a minimizing cut write \(a=n-|I|\), \(b=n-|J|\), and
\(p=n-a-b\ge1\). Double stochasticity and tightness imply
\(B[I^c,J^c]=0\). Every original zero of \(A\) also remains a zero of \(B\).
The cut is either full, marginal (one side full), or proper (neither side
full). A full minimizing cut gives \(A=B\); the equality condition in
van der Waerden's theorem then excludes a boundary maximizer.

For a proper cut the zero rectangle implies

\[
\operatorname{per}(B)\ge
\nu_{n,a,b}:=\frac{\gamma_{n-a}\gamma_{n-b}}{\gamma_p}.
\]

This bound follows directly from Gurvits's capacity inequality.
Successively extracting the \(b\) variables corresponding to the zero
rectangle's columns gives degree bounds
\(n-a,n-a-1,\ldots,p+1\). Multiplying their capacity factors
\(G(k)=((k-1)/k)^{k-1}=\gamma_k/\gamma_{k-1}\), and then the
van der Waerden factor for the remaining \(n-b\) variables, gives the
displayed bound. The [general lemma in the dimension 7 audit](study/audit-n7.md)
proves positive capacity, the successive degree bounds, and sharpness.
Thus this step needs no separate theorem about zero-rectangle minimizers.

For \(n\ge8\), Cheon--Wanless also excludes a boundary maximizer whose
entire zero set is a single rectangle. Consequently a boundary maximizer
has two zeros in distinct rows and distinct columns. Indeed, if no such
pair existed, all zeros would lie in a single row or a single column,
which itself is a rectangle. These two independent zeros persist in \(B\).

## 3. All cuts in dimensions 10 through 15

For \(n\ge8\), suppose positive line sums total \(n\), their product is
\(X\ge1-\gamma_n\), and a subset of \(d\) line sums totals \(d+e\), where
\(1\le d<n\). Then

\[
1-X\ge\frac{7n}{16d(n-d)}e^2.
\]

Grouped AM--GM, binary relative entropy, and Taylor bounds on
\(|e|<1/10\) prove this lemma. All rational constants used to localize
\(e\) have been checked.

For a proper tight cut this gives \(\delta\ge C_{n,a,b}u^2\), with

\[
C_{n,a,b}=\frac{7np^2}{16\{a(n-a)+b(n-b)\}}.
\]

A marginal minimizing cut reduces, after transposition if necessary, to
a minimum row sum \(1-u\). Summing the positive-support stationarity
conditions over that row produces an incident column satisfying

\[
c_j\ge1+\frac{(1-\gamma_n)u}{1-(2-\gamma_n)u}.
\]

The denominator is positive by the same stationarity identity. The
marginal coefficient therefore improves to
\(C_{n,n-1,0}=7n\{1+(1-\gamma_n)^2\}/[16(n-1)]\).

For \(n=11,\ldots,15\), use \(M=\nu_{n,a,b}\) on proper cuts and the
Knopp--Sinkhorn one-zero floor \(M=\kappa_n\) on marginal cuts, where

\[
\kappa_n=\frac{(n-2)!(n-2)^{n-2}}{(n-1)^{2n-4}}.
\]

Every cut satisfies the strict rational inequality

\[
M-\gamma_n-\frac{n^2M^2}{4C_{n,a,b}}>0.
\]

An independent exact implementation enumerated all ordered cuts. Thus,
for every \(u\in[0,1]\),

\[
0=P-\gamma_n+\delta
\ge M(1-u)^n-\gamma_n+Cu^2
\ge M-\gamma_n-nMu+Cu^2>0,
\]

a contradiction. For \(n=10\), the two independent zeros give
\(L=\kappa_n(1+1/(2n^2))\). Use \(M=\max(\nu,L)\) on proper cuts and
\(M=L\) on marginal cuts. On the localized range
\(u^2\le\gamma_n/C\), retaining the quadratic remainder gives

\[
M-\gamma_n-\frac{n^2M^2}{4(C+\beta M)}>0,\qquad
\beta=\frac{(1-\bar u)^n-1+n\bar u}{\bar u^2},
\qquad \bar u^2\ge\gamma_n/C.
\]

Here each chosen \(\bar u\) lies in \((0,1)\). The integral remainder
shows that this \(\beta\) is a valid uniform lower coefficient on
\([0,\bar u]\). The two-zero floor was checked by integer permanent
calculations from its definition and an independently implemented
exact polynomial reconstruction followed by Sturm root counting.
These arguments exclude every boundary maximizer for \(10\le n\le15\).

## 4. The remaining branches in dimensions 8 and 9

The unified quadratic bounds pass 49 of the 51 cuts in dimensions
8, 9, and 10, counted up to transposition. Only the marginal cuts in
dimensions 8 and 9 remain.

Write
\(h(u)=(1-\gamma_n)u/[1-(2-\gamma_n)u]\) and
\(q(u)=2-\gamma_n-(1-h(u)/(n-1))^{n-1}\).
On the residual intervals, \(q(u)>1\). If the large column incident to
the minimum row has \(z\) zeros, stationarity and cofactor
nonnegativity bound every other incident row sum by \(1/q(u)<1\).

The total row sum and exclusion of partial decomposability rule out
\(z=0,n-1,n\), leaving exactly \(1\le z\le n-2\). Maximizing the row
product under these caps gives

\[
R\le(1-u)q(u)^{-(n-1-z)}
\left(\frac{n-1+u-(n-1-z)/q(u)}z\right)^z.
\]

Combining this with the column-product bound reduces the contradiction
to exact polynomial positivity expressing
\(M(1-u)^n-\gamma_n+\Delta(u)>0\).
Primary and independent reconstructions check the complete intervals
and all required support cases. The [detailed audit](study/audit-n8-n9.md)
justifies the capped-product maximization, positive denominators, and
the interval cover including its junctions. This excludes the remaining
boundary maximizers for \(n=8,9\).

## 5. The dimension 7 branch trees

For \(n=7\), use Lu's Hall, stationarity, and complementary-minor
entropy method. First prove that every subset-sum deviation has absolute
value less than \(7/47<3/20\), so positivity of the Hall scaling is
established without circular reasoning.

Marginal cuts are excluded by a univariate entropy inequality. Proper
cuts split into six types with \(p\ge2\), six sign configurations with
\(p=1\) and at least one nonpositive deviation, and three types with
\(p=1\) and both deviations positive:
\((a,b)=(1,5),(2,4),(3,3)\).

For each of the final three types, a bivariate Bernstein subdivision
tree proves throughout the whole square \(0\le e,f\le3/20\) that

\[
\mathcal G>0\quad\text{or}\quad
(\mathcal N>0\ \text{and}\ \mathcal F>0).
\]

The first alternative contradicts a direct permanent lower bound.
The second gives incompatible upper and lower bounds on the same
variable product \(su\). The two simultaneous positive inequalities
are checked over each entire terminal box, not at unrelated points.

| (a,b) | All nodes | Direct-bound leaves | Entropy leaves | Depth |
|---|---:|---:|---:|---:|
| (1,5) | 39 | 10 | 10 | 8 |
| (2,4) | 35 | 9 | 9 | 6 |
| (3,3) | 47 | 11 | 13 | 8 |

Two independent implementations agree on these counts and classifications;
each independently verifies the strict inequalities on every leaf.
The [complete audited argument and supplements](study/audit-n7.md)
show that this covers every dimension 7 boundary maximizer.

## 6. Conclusion and scope of the evidence

There is no boundary maximizer for any \(7\le n\le15\), and every
strictly positive maximizer is uniform. Together with the existing
dimension 5 and 6 certificates, this proves the theorem throughout the
requested range. An equality matrix is itself a global maximizer, so
the uniqueness statement follows as well.

The result of this attack is an attributed assembly and independent
verification of a computer-assisted proof. The public source remains
unreviewed in the journal-publication sense; this local independent review
is not peer review. The full matrix theorem has not been formalized in
Lean. The new finite certificate decisions use integer and rational
arithmetic; printed decimal values are diagnostic only. The existing
dimension 5 and 6 computations were not rerun.

The final review found and repaired an exit-status bug in the older n=6
integer checker. Its original complete log confirms positive exact slack;
the truncated harness output alone would not have established this.
[Step 5](deterministic/certified-special-case-check-5/README.md) tests the
repaired failure gate without repeating the large matrix computation.
The original verified floating-point n=6 route also remains available,
under its stated IEEE-754/LAPACK backward-error assumptions.

Public sources include [Nascimento's pinned commit](https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701),
[Lu's pinned commit](https://github.com/lueluelue2006/dittert-n7-extension/tree/56397b70299278b338a286b90361180833dbf983),
[Gurvits](https://arxiv.org/abs/0711.3496), and
[Cheon--Wanless](https://doi.org/10.1016/j.laa.2010.08.041).
Source files and their licenses are retained in study/external-proof.
