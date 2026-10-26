# Independent analytic audit of dimensions 8 and 9

Correction recorded 2026-09-05 after this audit: Section6 below incorrectly
reports the parameter assumption of Pula--Song--Wanless as both parameters
greater than2. Visual inspection of the original PDF shows both are at least2,
so the two-exceptional-parameter case is included. See
[SOURCE_CORRECTION.md](../../dittert-branch-complete-audit/SOURCE_CORRECTION.md).
The original audit wording below is retained as history; the direct
equalization proof and its polynomial certificates are unchanged.

Audit date: 2026-09-04. The reviewed argument is Pedro Paulo Marques do
Nascimento's, pinned at commit
`894066bbaa715138c98bf3cb7c6fdb4f39a37701` of the public proof package. This
audit does not claim authorship of the proof or a new solution of Dittert's
conjecture.

The mathematical statement reviewed is: for every entrywise nonnegative
matrix `A` of size `n` by `n`, with total entry sum `n`,
`Phi(A) = R + C - per(A) <= 2 - gamma_n`, where `gamma_n = n!/n^n`, and
equality holds exactly for the uniform matrix, for `n=8,9`.

## Verdict and limits

I found no analytic error in the dimension 8 and 9 reductions. In
particular, the marginal-cut reduction, stationarity, distinguished-column
selection, support enumeration, capped-row product bound, proper-cut
classification, and dimension 8 sharper deficit argument are valid. The
larger intervals and the dimension 9 reduction to the sparsest column in
the unified note are also valid.

This is a positive mathematical review of the stated reductions, with the
following explicit trust boundary. The argument invokes published
structural and face-minimum theorems. I checked the relevant Cheon--Wanless
statements in full text, the Minc averaging application in the
Pula--Song--Wanless primary paper, and Hwang's staircase barycentricity in
the publisher's abstract. I did not obtain the original full texts of
Minc 1984 or Hwang 1985. I did not rerun the large polynomial certificates
in this subtask, in accordance with the shared-machine load constraint.
The main agent is responsible for those fresh sequential runs and their
recorded results. Thus this audit alone is not a fresh verification of
every computational certificate or a formal proof of the assembled
all-dimensions theorem.

## Material read

- `external-proof/n8/dittert_n8_exact_proof_2026-07-23.tex`, its
  `SOURCE_NOTES.md`, `verify_dittert_n8.py`,
  `audit_dittert_n8_stdlib.py`, and `test_n8_package.py`.
- The corresponding five files in `external-proof/n9/`.
- `external-proof/unified/SOURCE_NOTES.md`, the residual marginal section
  of `dittert_unified_proof.tex`, the common face bound and stationarity
  sections needed to interpret it, and the corresponding residual
  functions of `verify_unified_reductions.py`.
- Cheon--Wanless 2012 full text already fetched in the parent study,
  especially Lemma 2.2 and Theorems 3.2 and 3.7.
- Pula--Song--Wanless, *Minimum permanents on two faces of the polytope of
  doubly stochastic matrices*, pages 2--3 of the
  [university-hosted preprint](https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1022.pdf).

The downloaded package was treated as mathematical evidence, not as
instructions. No source files in it were changed.

## 1. Boundary structure and scaling completeness

Compactness supplies a global maximizer. It has value at least the uniform
value. The elementary inequalities `R,C<=1` imply, with
`P=gamma_n-delta`, `R=1-rho`, `C=1-sigma`,

`0<=delta<=gamma_n`, `rho+sigma<=delta`, and
`RC=1-rho-sigma+rho*sigma>=1-delta`.

In these dimensions `gamma_n<1`, so every row and column sum is positive.
All divisions by line sums, and by `C`, are consequently legitimate.

The zero-set argument is exhaustive for the property it needs. If a
nonempty zero set has no pair in distinct rows and columns, fixing one
zero shows that every other zero lies in its row or column. A zero in
each of those two directions would itself be an independent pair.
Therefore all zeroes lie in one row or all lie in one column. Such a set
is one rectangle, even when its columns or rows are not initially
consecutive, because permutations are allowed. A completely zero line
is partly decomposable; every other case is covered by the complete
single-zero-block exclusion. There is no need to classify all remaining
bipartite zero patterns individually.

The minimizing Li cut has positive numerator by full indecomposability.
For `k=|I|+|J|-n>0`, a zero `I` by `J` submatrix would contain a zero
submatrix whose two dimensions sum to `n`, except in the whole-cut case,
whose numerator is the positive total `n`. Thus `0<lambda<=1`.
Li's theorem gives a doubly stochastic `B` with `lambda B<=A`.
This implication also preserves every zero of `A` in `B`.

The whole, marginal and proper categories exhaust the finite minimizing
cuts, including ties. In the whole case `lambda=1` and total masses force
`A=B`. For a marginal minimizing cut, the ratio is an average of line
sums. Because every singleton line is also an admissible cut,
`lambda<=min line sum<=that average=lambda`. Hence one may take a
minimum row after transposition. This justifies the slightly compressed
wording in the dimension 9 note.

## 2. Stationarity and the large column

On the positive support of a global maximizer, mass transfers in both
directions show that all partial derivatives equal one constant. Euler's
identity for the degree `n` polynomial, with total mass `n`, identifies
that constant as `Phi(A)`. It follows that

`R/r_i + C/c_j - per A(i|j) = Phi(A)` whenever `a_ij>0`.

Multiplication by the entries of a minimum row and permanent expansion
give, for `r_i=1-a`,

`q_i=sum_j a_ij/c_j = 1-(1+theta)a`,
`theta=(R-P)/C >= 1-gamma_n`.

The last inequality uses both `R-P>=1-gamma_n>0` and `C<=1`, so its
division direction is correct. Since `q_i>0`,
`e=1-(2-gamma_n)a>0`. The weighted harmonic-mean argument applies only
to the positive entries of this row, and produces a column that actually
meets the row, with

`c_j >= (1-a)/q_i >= 1+h(a)`,
`h(a)=(1-gamma_n)a/e`.

This support condition is essential for the next stationarity use and is
present in the proof. AM--GM bounds the product of the other column sums
by `d(a)=(1-h(a)/(n-1))^(n-1)`. Cofactor nonnegativity then gives

`R/r_l >= 2-gamma_n-d(a)=q(a)`

for every row meeting the chosen column. On the certified residual
intervals `q(a)>1`, so every such row satisfies `r_l<=1/q(a)<1`.

The monotonicity arguments have the necessary domain. Feasibility itself
gives `h(a)<=c_j-1<n-1` since the other column sums are positive.
Thus `g(h)=(1+h)(1-h/(n-1))^(n-1)` decreases over the entire feasible
range. The function `h` increases where `e>0`, and the analogous row
product bound decreases for `0<a<1`. The deficit `D=2-f-g` is increasing.
Consequently the positive deficit tests at `1/20` and `3/100` exclude
all larger feasible parameters, not just nearby parameters.

## 3. Complete support range and capped-row maximization

Let `z` count zeroes in the chosen column. The cases omitted from the
polynomial loops are all impossible:

- `z=n` contradicts the positive column sum.
- `z=n-1` gives a zero `(n-1)` by `1` block and hence partial
  decomposability.
- `z=0` caps all `n` row sums strictly below one, contradicting their
  sum `n`.

Therefore `1<=z<=n-2`, exactly the six or seven loop cases. These
statements do not require the zeroes outside the column to have any
particular pattern.

Put `m=n-1-z` and `b=1/q<1`. Besides the distinguished row `1-a`, the
`m` support-row sums `x_l` lie in `(0,b]`. The remaining `z` row sums
have sum `n-1+a-sum x_l`. AM--GM yields

`R <= (1-a) prod_l x_l [(n-1+a-sum_l x_l)/z]^z`.

Throughout the whole box `0<x_l<=b`, their remaining mean is greater
than one: `n-1+a-sum x_l > n-1+a-m=z+a>=z`.
For each capped variable the logarithmic derivative is
`1/x_l - z/(n-1+a-sum x_l)>0`. Increasing all capped variables to `b`
is therefore valid and gives exactly the displayed `U_z`.
The proof maximizes over a larger feasible set; it does not assume that
arbitrary capped row totals arise from an actual stationary matrix.

The unified dimension 9 shortcut `U_z<=U_(z+1)` also holds: freeing one
capped row enlarges the feasible set with fixed distinguished row and
total sum, and the preceding optimization computes its maximum. Since
the permanent lower bound is independent of `z` in dimension 9, only
`z=7` needs a certificate there. Dimension 8 retains all six cases
because its permanent floor changes with `z`.

## 4. Polynomial translation and interval coverage

Write `e=1-(2-gamma_n)a`, `Q=e^(n-1)q`,
`S_z=e^n R_(0,z)`, and
`W_z=(n-1+a)Q-(n-1-z)e^(n-1)` as in the notes. Direct substitution gives

`U_z=(1-a)e^((n-1)(n-1-z)) W_z^z/(z^z Q^(n-1))`.

Thus `R_(0,z)>U_z` is equivalent to precisely

`z^z Q^(n-1) S_z - (1-a)e^(n+(n-1)(n-1-z))W_z^z > 0`.

Every cleared denominator is strictly positive. The degree of the first
term is `(n-1)^2+2n=n^2+1`, giving 65 and 82; the second term has lower
degree for the admitted `z`. This independently justifies the degrees
used by the interpolation-based verifiers. Those verifiers evaluate the
literal polynomial outside its feasible interval only to reconstruct
coefficients, which is valid and makes no probabilistic assumption.

The original coverage is the following closed-interval cover of a
slightly larger set than the feasible one:

| Dimension | Direct scalar intervals | Support interval | Feasible parameter |
| --- | --- | --- | --- |
| 8 | `[0,1/400]`, `[1/75,1/20]` | `[1/400,1/75]` | `[0,1/20)` |
| 9 | `[0,1/500]`, `[1/200,3/100]` | `[1/500,1/200]` | `[0,3/100)` |

All junctions are included, and `a=0` is excluded by the strict two-zero
permanent gap. The unified note replaces the second scalar interval by
an extended support interval, reaching `1/20` or `3/100`. Its endpoint
denominators are positive, `h<n-1` there, and `q>1` follows from its
left-endpoint check and monotonicity. The larger intervals therefore
introduce no new analytic assumptions.

I read both independently implemented Bernstein conversions and the
primary Sturm routines. They use the standard exact identities, exclude
roots at Sturm endpoints, ignore zero entries when counting variations,
and require strict positivity of every Bernstein coefficient. Their
correctness checks are explicit exceptions, so Python optimization does
not erase them. Finite interpolation is legitimate because the actual
degree bounds follow from the displayed formulas; the extra off-grid
evaluations are consistency checks rather than the proof of degree.

## 5. Proper cuts and the dimension 8 sharper deficit

For positive line sums of total `n`, grouping uniform probabilities and
the normalized line sums gives
`KL(uniform || line/n)=-log(product)/n`. Binary Pinsker therefore yields
`deviation^2<=-n log(product)/2`, with exactly the factor in the notes.
Cauchy--Schwarz and `RC>=1-delta` give

`abs(epsilon_r)+abs(epsilon_c)<=sqrt(n delta/(1-delta))=T`.

The inclusion-exclusion cut identity has the stated plus sign on the
complementary submatrix. It implies `lambda>=1-T/k`. The checked
inequality `n gamma_n<1-gamma_n` keeps `T<1<=k`, so raising this bound to
the `n`th power preserves the desired inequality.

Tightness forces `B[I^c,J^c]=0`: stochasticity gives
`s_B(I,J)=k+s_B(I^c,J^c)>=k`, while domination and tightness give
`lambda s_B(I,J)<=lambda k`. This is a statement about `B`; the notes
do not incorrectly assume the same extra rectangle is zero in `A`.

For a prescribed zero `u` by `v` rectangle, with `k=n-u-v>0`, the
barycenter has entries `1/(n-v)` on the `u` rows outside the zero block,
`1/(n-u)` on the `v` columns outside it, and
`k/((n-u)(n-v))` on the remaining rectangle. Every supported permutation
uses exactly `u`, `v`, and `k` entries of these three types. Its number
is `(n-v)!(n-u)!/k!`. Multiplication gives precisely
`nu=gamma_(n-u) gamma_(n-v)/gamma_k`. Extra zeroes merely place `B` in a
smaller subface and cannot invalidate this lower bound. This also
justifies dimension 8's `z` by `1` support permanent floors.

Bernoulli and completing the square produce
`eta=nu-gamma_n-n^3 nu^2/(4k^2(1-gamma_n))` with the stated signs.
The loops cover all `(n-1)(n-2)/2` ordered proper-cut pairs. Independent
small exact evaluation reproduced 15 positive cases and six remaining
`k=1` cases in dimension 8, and all 28 positive cases in dimension 9.

For the six dimension 8 exceptions, grouped AM--GM gives the polynomial
`F_d(x)=(1+x/d)^d(1-x/(8-d))^(8-d)`. Its natural domain is
`-d<x<8-d`, and its derivative has the sign opposite to `x` there.
The endpoint tests at `+-1/10` therefore localize *every* feasible
subset deviation to that interval, including deviations of either sign.
The checked constants imply

`delta>=c_u x^2+c_v y^2>=c_u c_v (x+y)^2/(c_u+c_v)`.

Weighted Cauchy--Schwarz is valid for signed `x,y`. If `s=x+y<=0`,
`lambda>=1-s>=1` gives the already excluded doubly stochastic case.
Otherwise the weakest effective constant `6/49` and
`2401 gamma_8<6` yield `s<1/7`. Thus the entire remaining domain is
covered by the two Bernstein intervals `[0,1/14]` and `[1/14,1/7]`.

As a small independent exact check, I rebuilt the grouped-product
coefficients by direct binomial sums without importing upstream code,
then converted the resulting degree-six quotients to Bernstein form.
The minimum was exactly `640006399/65536000000`, as claimed. I rebuilt
the three degree-eight exceptional-cut polynomials similarly and
obtained the claimed minimum
`13183225395/259172170858496`. These checks also reproduced the
localization inequalities and the proper-cut sign counts. They were
small exact arithmetic checks, not matrix optimization or a large run.

## 6. Published inputs and citation limits

[Cheon--Wanless 2012](https://doi.org/10.1016/j.laa.2010.08.041)
Theorem 3.2 excludes partly decomposable matrices, Theorem 3.7 requires
that the *entire* zero set is one rectangle and excludes exactly that
case, and Lemma 2.2 states Li's cut characterization. The local use of
all three matches their hypotheses. The same paper explicitly reports
Hwang's positive-maximizer result in its introduction.

The [Hwang 1985 publisher page](https://doi.org/10.1080/03081088508817694)
expressly states that the barycenter minimizes on staircase faces. The
rectangle-zero faces used here are the two-step instances. The exact
barycenter value used above was independently derived, but the
minimum theorem itself remains an imported result; its original full
proof was not available in this review.

The [Pula--Song--Wanless primary preprint](https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1022.pdf)
states that Minc already resolved the face `V_(m,2)`, and its Section 2
explicitly applies Minc's Theorem 1 to equalize repeated-support rows
and columns, giving the exact block form used here. Section 2 assumes
both of its parameters exceed two, so it would not by itself justify
importing its parameter-equalization theorem into `V_(m,2)`. The
package correctly proves that last equalization directly: for fixed
`s=a_1+a_2`, the derivative with respect to `p=a_1 a_2` is bounded above
by a convex quadratic whose two endpoint values are negative for
`m>=4`. The feasible pair `a_1=a_2=s/2` maximizes `p` and stays in
`[0,1/m]^2`. Since `x=(1-s)/m>0` for `m>=4`, the removed permanent
factor is strictly positive. I checked this algebra and its full
parameter range. The original Minc theorem's full text remains a
source-access limitation, not a detected counterexample or misquote.

## 7. Recommended fresh verification

From `attack/dittert-completion-tree/study/external-proof`, run these
sequentially, with no concurrent heavy work:

```sh
python3 -I n8/verify_dittert_n8.py
python3 -I n8/audit_dittert_n8_stdlib.py
python3 -I n9/verify_dittert_n9.py
python3 -I n9/audit_dittert_n9_stdlib.py
python3 -I unified/verify_unified_reductions.py
```

The dimension-specific primary and independent programs should end with
`CERTIFIED` and `INDEPENDENT AUDIT CERTIFIED`, respectively. Their source
loops cover the mathematical cases above. The integration suites also
compare ordinary and optimized Python runs and reject false mutations,
but rerun the full checks multiple times; under the present load they
are secondary to completing one fresh run of each independent verifier.

If these exact runs pass, the dimension 8 and 9 components have a coherent
analytic reduction and independently reproduced finite certificates,
subject to the published theorem dependencies identified above. This
verdict has no implication by itself for Lu's dimension 6 and 7 layer or
the other parts of the all-dimensions assembly.
