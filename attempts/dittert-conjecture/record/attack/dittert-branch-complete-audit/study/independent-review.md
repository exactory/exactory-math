# Independent review of the complete branch audit

Review date: 2026-09-05. This reviewer inspected mathematical claims and evidence only. This report is the reviewer's only saved output. No proof, harness, source, or certificate was modified.

## Verdict and scope

The current package supports the complete statement for every integer `5 <= n <= 15`: for every nonnegative real matrix of order `n` and total entry sum `n`,

    prod(row sums) + prod(column sums) - per(A) <= 2 - n!/n^n,

with equality exactly at the uniform matrix. I found no unresolved analytic branch, missing Hall cut, unjustified sign choice, or incomplete interval cover. This is an attributed computer-assisted proof with cited mathematical inputs and exact finite certificates. It is not a Lean formalization.

I compared the parent's new `../PROOF.md` against `../BRANCH_TRANSPORT.md`, both child proofs, the detailed predecessor derivations, and the checker implementations. The assembled claim agrees with those components. Other reviewers' PASS statements were not mathematical premises.

The substantive certificate records for dimensions five and six are inherited. Their large matrix computations were not repeated here. For dimensions seven through fifteen, I inspected the fresh full child outputs and repeated the light checks specified below. Full bivariate arithmetic and full residual-polynomial generation were run by the children and coordinator, not rerun by this reviewer.

## 1. The old branch objection

The barrier in `../../quantitative-van-der-waerden/units/6/draft.md`, Section 2, is real: the old scalar Sinkhorn fixed-point inequality allows a large-cost branch. The new proof does not establish that this abstract scalar region is empty.

Instead, it starts from an arbitrary global maximizer without a restriction on its old Sinkhorn cost. The Hall scale and dominated doubly stochastic matrix are separately defined. There is no identity with the old scale, least-fixed-point selection, spectral-gap estimate, or assumption that the old cost is small.

Every hypothetical boundary global maximizer, including one in the old large-cost region, satisfies the new hypotheses and belongs to an excluded Hall case. This is sufficient. A violating matrix would yield a global maximizer by compactness, and every equality matrix is a global maximizer once the maximum value has been established. A stronger permanent bound for every abstract near-decomposable doubly stochastic matrix is not needed or claimed.

## 2. Positive maximizers and uniqueness

The dimension-independent interior proof is valid. Mixing two columns preserves row sums and makes the objective a quadratic symmetric under `t -> 1-t`. At a positive maximizer, small negative and positive parameters are feasible, so its derivative at zero vanishes and the quadratic is constant. Pair averaging preserves positivity and the global maximum.

A complete cycle of pair-averaging orthogonal projections strictly contracts the zero-mean subspace. Equality in norm would require every projection to fix the same vector, forcing all columns equal, impossible for a nonzero zero-mean vector. Compactness of the unit sphere supplies a uniform contraction. Column averaging converges to entries `r_i/n`; row averaging then converges to the uniform matrix. The limiting matrices remain positive.

I independently checked the tangent Hessian. If the total sum of `X` is zero, the permanent's second derivative at the uniform matrix is

    c_n (||X||_F^2 - ||X 1||^2 - ||X^T 1||^2),

where `c_n=(n-2)!/n^(n-2)`. Subtracting this from the two product Hessians gives the strictly negative formula in the common note, including `n=2`. The uniform matrix is consequently isolated among nearby feasible matrices of its value. The averaging sequences eventually enter that neighborhood. Flatness rules out a first pair-average reaching the uniform matrix from a distinct maximizer. Finite backtracking proves uniqueness. General averaging is not assumed to converge finitely.

## 3. Hall construction and complete cut classification

The global comparison gives `rho+sigma <= delta <= gamma < 1` and positive line sums before any division. Euler's identity correctly identifies the common derivative on positive entries with the objective value. Subsequent boundary variations preserve existing support.

For a positive-right-side Hall cut, inclusion-exclusion gives `s_A(I,J)=p-e-f+z`, where `z>=0`. The subset bounds give absolute excess below `7/47` in dimension seven and below `1/10` in dimensions eight through fifteen. Hence every relevant numerator is positive before Hall scaling. The binary entropy estimate works for either sign: integrating toward a negative excess reverses both orientation and derivative sign.

The real-capacity network has the correct cut capacity:

    n lambda + s_A(I,J) - lambda (|I|+|J|-n).

For a nonpositive last factor, nonnegativity suffices. For a positive factor, the defining minimum suffices. A maximum flow of value `n lambda` saturates each source-row and column-sink arc; division by the already positive scale gives doubly stochastic `B` with `lambda B<=A`.

At a tight cut, double stochasticity and domination force `B[I^c,J^c]=0`. Equality of the summed core domination also gives the entrywise core equality required in dimension seven. The proof does not wrongly conclude that the opposite rectangle of `A` is zero.

Every cut has `a,b>=0` and `a+b<=n-1`. The full case forces `lambda=1`, then equal masses give `A=B`; van der Waerden's equality classification excludes a boundary maximizer. A marginal ratio is an average of line sums, and the singleton cuts prove this equals a minimum line sum. Proper cuts are the remaining positive pairs. Ties cause no exception because the deductions hold for each minimizing cut. Both scale endpoints are handled.

## 4. Permanent floors and primary sources

The rectangle capacity argument is valid. The row-form product starts with capacity one. After extracting `h` exceptional column variables, each surviving term has used `h` distinct rows outside the zero block, so the next degree is at most `n-a-h`. Positive capacity and stability persist. These are the hypotheses of Gurvits, Fact 4.9 and Theorem 4.10, which I checked in the [primary text](https://arxiv.org/html/0711.3496v2). The factors telescope to the claimed rectangle floor. Additional zeros do not invalidate the argument.

I read the relevant full Cheon--Wanless statements in the local primary PDF extraction. Theorem 3.2 excludes partly decomposable maximizers; Theorem 3.7 excludes a maximizer whose entire nonempty zero set is one rectangle. These match their uses. Fixing one zero shows that a nonempty zero set without an independent pair must lie in one row or column: zeros in both off-intersection directions would themselves be independent. The whole zero set is then a rectangle, so the claimed independent pair exists. The source is [Cheon--Wanless, DOI 10.1016/j.laa.2010.08.041](https://doi.org/10.1016/j.laa.2010.08.041).

I independently opened the [Pula--Song--Wanless primary PDF](https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1022.pdf) and visually inspected complete page 3. Section 2 visibly assumes `m,n >= 2`. Web text extraction again returned `>2`, confirming the extraction error. The repeated-support minimizing form includes the required `V_(m,2)` case. The original Minc article was not separately obtained; its explicit application in this published primary paper is an imported theorem input, not an unresolved parameter exclusion.

The independent face checker compares its permanent polynomial with integer subset-DP permanents at `n+1` distinct points. Both have degree at most `n`, making this an exact polynomial identity check. It then checks positive endpoints and absence of roots on the full feasible closed interval. I reran these checks for `n=8,9,10`; all completed successfully. No optimizer root or interval branch is selected.

## 5. Dimension seven

The six ordinary types and six mixed-sign conditions exhaust their classes. Both excesses nonpositive are incompatible with a positive Hall deficit. Zero axes are included in the mixed cases. The three remaining types enter full closed squares.

I checked the predecessor's complementary-minor entropy derivation directly. Its auxiliary polynomial is extracted from a product of nonnegative linear forms, hence stable. Weighted AM-GM gives the capacity estimate. A positive entry of a doubly stochastic matrix belongs to a positive permutation, so its required complementary minor is positive. For zero entries, the smoothing exponent times the minor's logarithm tends to zero. This justifies the zero-exponent limit and the exponential core bound.

The marginal proof establishes `D>0` and `s>0` before division. Its AM-GM squeeze applies to every positive `s`, without a discarded large-entropy branch. In the positive-core proof, reciprocal variance control holds on either side of the group mean, and the normalized variation scales only existing entries. The slack `u` dominates both envelope deficits; `c` dominates `E,F`. Thus the lower and upper bounds concern the same nonnegative product `su`. Neither zero endpoint requires division. The entropy leaf separately checks `N>0` before squaring.

The independent manifest checker rebuilds the three rational polynomials. Its direct restriction is the tensor product of affine binomial expansion and the monomial-to-Bernstein identity. It imports neither the generator's polynomial code nor its subdivision routine. Both entropy inequalities are checked on the same entire leaf.

Every internal prefix must have both children; each closed leaf rectangle must equal its path-defined rectangle; the roots are full squares. These establish continuous coverage including junctions, rather than merely comparing counts. I reran the exact scalar, coverage, and omission checks:

| Check | Observed result |
| --- | --- |
| Actual subset-pair Hall cuts | 6,476 |
| Full, marginal, ordinary, single-bridge counts | 1, 252, 3,234, 2,989 |
| Closed leaf counts | 20, 18, 24 |
| Tree node counts | 39, 35, 47 |
| Omission mutations rejected | 94 |
| Six ordinary margins, six sign margins, W | All strictly positive |

The fresh full child output records direct exact checking of all 62 leaves. I inspected the checker and per-leaf evidence. This review did not repeat the full bivariate arithmetic.

## 6. Dimensions eight through fifteen

The signed deficit lemma is global. Its third-derivative estimate and rational comparison give the stated coefficient on the already localized interval. Weighted Cauchy-Schwarz uses signed excesses; its final squaring is legitimate because `e+f>=pu>=0`. Marginal stationarity proves the denominator positive and selects a column incident to the minimum row, as required by the later stationarity use.

For dimensions eleven through fifteen, the completed-square lower bound holds on all of `[0,1]`. For dimensions eight through ten, `u^2<=gamma/C` follows from the global deficit. The rounded square root encloses the whole feasible range, and the decreasing integral remainder proves the quadratic bound on that range. This does not select a small fixed-point solution.

I independently recomputed every dimension's localization inequalities and all 428 scalar margins across 596 uncompressed size pairs. The exact nonpositive set was `(8,7,0)` and `(9,8,0)`. The 65 mutation and arithmetic regressions completed successfully.

For those two marginal cases, monotonicity and the global budget exclude the whole feasible tail. Positivity of the stationarity denominator and the column-product domain follows from feasibility before monotonicity is used. The remaining cover is `[0,s]` and `[s,v]`, including their junctions.

The selected-column support argument excludes zero counts `0,n-1,n`, leaving `1,...,n-2`. Product maximization increases each capped row to its cap because the remaining average exceeds one. In dimension nine, freeing one cap increases the product envelope while its permanent floor stays fixed, justifying reduction to `z=7`. Dimension eight correctly retains all six cases because its floor changes with `z`.

I checked the cleared polynomial against the literal inequality. Its multiplier is `z^z Q^(n-1) E^n>0`, and its degree is at most `n^2+1`. The independent implementation directly constructs it in the Bernstein basis with correct multiplication and degree elevation. Rational sample comparisons are supplementary checks, not the polynomial identity proof.

The fresh complete source and independent outputs certify two near-zero intervals, six dimension-eight support polynomials, and one dimension-nine support polynomial. All nine Bernstein arrays are positive on their entire closed intervals without subdivision. The source separately uses Sturm root counting near zero. Its wrapper executes both near-zero checks even though its support-name summary lists only the seven support polynomials.

## 7. Inheritance and residual obligations

The inherited dimension-five and dimension-six certificates give positive constants `32/3125` and `128/46656` times the squared Frobenius distance as lower bounds on the objective gap. Their coefficient identities are full polynomial identities, not local approximations. I inspected the exact-identity run records, stated Gram-positivity interfaces, and complete inherited integer dimension-six log. That log reports exact residual diagonal-dominance slack `1691794048955`; the substantive positive result supports the historical run despite its old exit-status bug. The predecessor retains the corrected gate and its regression evidence.

There is no remaining mathematical branch obligation within the declared computer-assisted standard. Boundary exclusion for dimensions seven through fifteen, positive-maximizer uniqueness, and the inherited full-domain certificates for dimensions five and six give the original claim and equality case. Published theorem inputs and software arithmetic remain explicit trust boundaries. Formalization of the real-matrix theorem would be additional work.

## Reviewed file identities

SHA256 values fix the substantive versions inspected.

| File | SHA256 |
| --- | --- |
| Common BRANCH_TRANSPORT.md | `5bfbf6509175126506d6de05902c4b74e18fa92b45af24c1fc78e47ea935c8f0` |
| n7 COVERAGE_PROOF.md | `facdcfdb73dd3176acdc82badbb5ef25c6f1713d8f9fe4aaef274ed4342a06c2` |
| n7 check_manifest.py | `0531442b3febb9194ff55fc9f42bf01e57577d349984461db195f5033973fde8` |
| n7 manifest.json | `fcc6950afb9391841925d00489a303f545276446c439745430e4561d78b6f90e` |
| n8..15 PROOF.md | `e3489974247b33cadbfa31156f45db7b08bd770b0c9a2c3888bd6c256e5cca9d` |
| n8..15 independent_coverage.py | `21eb9eb2e82441c3dbd7bfa95b1883ae002cd7d13f31c4f0bdcc912729804698` |
| Saved Pula--Song--Wanless PDF | `b6da230c790cbf18aaae182aa9c4775a50b29fe30a42606a1937d254394ab908` |

