# Independent final evaluation

Post-review correction recorded 2026-09-05: the original PDF of
Pula--Song--Wanless assumes both parameters are at least2, not greater than2
as the text extraction suggested in this review. The needed two-parameter
case is included. See
[SOURCE_CORRECTION.md](../../dittert-branch-complete-audit/SOURCE_CORRECTION.md).
The original review below remains unchanged as a historical record.

Review date: 2026-09-05.

Verdict: PASS for the assembled computer-assisted theorem for every integer
5 <= n <= 15, including the stated unique equality case, with the software
and source-access limitations below. I found no remaining mathematical gap
in the supplied matrix-to-certificate reductions. This is an attributed
assembly and independent verification, not a new discovery, a journal
referee decision, or formal verification of the full matrix theorem.

One substantive implementation defect was found in an inherited checker:
a negative result did not produce a nonzero exit status. The complete
historical output subsequently located for that computation establishes
that its actual residual slack was positive. The coordinating agent
repaired the exit behavior and tested its negative, zero, and positive
branches. I inspected the repair and the new evidence. This issue is
resolved for this handoff.

## Scope and method

I independently read PROOF.md, problem.json, novelty.md, journal.jsonl,
the three dimension audits, and the specified certificate READMEs and result
records. I also inspected the underlying arguments and relevant verifier
code, including the independent finite-core checker, dimension 7 bridge
builders and tensor subdivision, dimension 8 and 9 support-polynomial
reconstructions, and the inherited dimension 6 coefficient/Gram checker.
Existing audit verdicts were not premises of my review.

The public source clone has HEAD
894066bbaa715138c98bf3cb7c6fdb4f39a37701 and was clean when inspected.
Attribution to Hongyuan Lu and Pedro Paulo Marques do Nascimento is
preserved in PROOF.md, lines 3-8, and study/audit-n7.md, lines 19-26.

I did not rerun large certificate programs, compute large Gram matrices,
build Lean, or spawn agents. I ran a small independent rational-arithmetic
recalculation of every ordered scalar cut for n=8,...,15 from the displayed
formulas. It reproduced the case counts and exactly the two exceptional
marginal cuts listed below. I also recalculated the dimension 7 localization
margin and all eight finite-dimensional subset-radius tests.

## Statement, global maximum, and equality

The theorem at PROOF.md, lines 12-22, agrees quantifier by quantifier with
both claim and quadruple.statement in problem.json. The domain is all
nonnegative real matrices of the specified sizes and total mass. There is
no unstated stochasticity, positivity, support, or rational-entry restriction.

Compactness and continuity provide a global maximizer. At any such matrix,
comparison with the uniform matrix and AM--GM give R,C <= 1,
P = gamma - delta, and
0 <= (1-R)+(1-C) <= delta <= gamma < 1. All line products are therefore
positive. Stationarity is used only at global maximizers and on positive
entries, where two-sided mass transfers are feasible. Homogeneity of degree
n and total mass n identify the common derivative with Phi(A).

The positive-maximizer conclusion is the cited Hwang result, explicitly
reported in the stored Cheon--Wanless paper, lines 118-123. The supplementary
dimension 7 averaging argument at study/audit-n7.md, lines 81-135, is valid:
cyclic projections contract nonconstant column collections, continuity
preserves the maximum at their limit, and the negative tangent Hessian at
the uniform matrix justifies finite backtracking. The argument does not
assume finite termination of averaging for arbitrary matrices.

After excluding every boundary global maximizer, the maximum is the value
at the uniform matrix. Any equality matrix is then itself a global
maximizer. This proves the equality classification without equality analysis
of intermediate entropy inequalities. For dimensions 5 and 6, their positive
quantitative SOS remainder proves uniqueness directly.

## Hall cuts and the rectangular zero-block bound

The full, marginal, and proper categories exhaust all minimizing cuts,
including ties. A marginal ratio is an average of line sums, and every
singleton line ratio occurs in the same minimum. It therefore equals a
minimum line sum; transposition gives the chosen minimum row.

Positivity of lambda is established before division. For n>=8 a zero
admissible cut would contain a forbidden partly decomposable zero block.
For n=7, localization is independent of Hall domination and yields
p*tau <= e_+ + f_+ < 14/47 < 1. Empty complements have excess zero.
The full cut gives lambda<=1, so Hall domination applies to A/lambda.
Tightness, stochasticity, and domination imply
s_B(I,J)=p+s_B(I^c,J^c)=p. Thus the complementary rectangle is zero in B.
Every original zero also persists. The additional rectangle is never
incorrectly asserted to be zero in A.

The general argument at study/audit-n7.md, lines 231-296, correctly proves
the rectangular permanent floor. Weighted AM--GM and evaluation at one
give capacity one for the row-form product. After extracting h specified
columns, only n-a-h remaining row factors can contain the next specified
variable. Stability and positive capacity survive extraction, and the
actual variable degree cannot be zero. Monotonicity of G gives a capacity
factor gamma_(n-a)/gamma_p; remaining extractions contribute gamma_(n-b).
The extracted coefficient is the permanent. The displayed block matrix
is doubly stochastic and its matching count attains the bound.

The imported extraction and stability facts match Theorem 4.10, Fact 4.9,
and Corollary 2.5 of [Gurvits, arXiv:0711.3496v2](https://arxiv.org/html/0711.3496v2).
Consequently the separate staircase-face minimizer theorem is unnecessary
for the assembled proof. Its appearance in the earlier dimension 8-15
audits describes their original route and adds no unresolved assumption
to PROOF.md.

## Dimensions 10 through 15

The grouped-product deficit inequality has the correct direction and
constants. Each product exceeds 1-gamma. Pinsker localizes every subset
excess to |e|<1/10. Taylor's theorem gives
g(e) >= (1987/4374)g''(0)e^2, while
g(e) <= -log(1-gamma) < gamma/(1-gamma) < 1/400.
Conversion from logarithmic deficit yields the claimed coefficient 7/16.

For a proper cut, p*u <= e+f and the two product deficits yield exactly
C = 7*n*p^2/(16*(a*(n-a)+b*(n-b))). Negative excesses may be discarded.
For a marginal cut, summed support stationarity gives a positive weighted
reciprocal-column sum, proving the denominator in h(u) is positive and
producing a column that actually meets the minimum row. The one-line
deficit estimate on both lines supplies the factor 1+(1-gamma)^2.

The strict inequality M-gamma-n^2*M^2/(4*C)>0 is sufficient after
Bernoulli and completing the square. For n=10, localization and the
integral remainder give the larger curvature C+beta*M. Its remainder
coefficient decreases on the whole interval because the integrand does.
No choice of a fixed-point branch is hidden here.

The independent program in deterministic/certified-special-case-check-1,
independent_check.py, lines 86-125, enumerates every ordered proper cut and
the representative marginal cut. Its archived output and my small
independent recalculation agree:

| Dimension | Ordered proper cuts plus marginal representative | Nonpositive scalar margins |
| --- | ---: | --- |
| 8 | 22 | (a,b)=(7,0) only |
| 9 | 29 | (a,b)=(8,0) only |
| 10 | 37 | None |
| 11 | 46 | None |
| 12 | 56 | None |
| 13 | 67 | None |
| 14 | 79 | None |
| 15 | 92 | None |

For n=10 the independent minimum is the positive rational printed in its
output, approximately 5.944773234138357e-7. The decision uses the rational
sign, not the decimal.

## The two-zero face and dimensions 8 and 9

The proof uses Cheon--Wanless Theorem 3.7 with its complete-zero-set
hypothesis. Without two zeros in distinct rows and columns, all zeros
lie in one row or one column and constitute one rectangle after
permutation. Merely containing some zero rectangle would not justify
the theorem; the assembly does not make that mistake.

The two-zero floor still imports Minc's averaging theorem for repeated
support rows and columns. I checked the resulting block form and the full
direct equalization argument in the dimension 9 source TeX, lines 178-233.
For fixed sum s the derivative in the product parameter is at most the
convex quadratic D_m(s), negative at both endpoints for m>=4. Equalization
remains feasible and the removed factor is positive because x=(1-s)/m>0.
The independent finite-core checker verifies the degree-n permanent
polynomial by integer subset-DP at n+1 distinct points and exact root
counting on its whole feasible interval. The dimension-specific checkers
also reconstruct their own floors by exact Ryser interpolation and
Bernstein positivity. These computations prove the polynomial floor;
the averaging theorem supplies applicability to arbitrary matrices on
that face.

There is a source-access limitation. The
[Minc publication identifier](https://doi.org/10.1080/03081088408817592)
is identifiable, but I did not obtain and independently read its original
full theorem text. The
[Pula--Song--Wanless primary preprint](https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1022.pdf)
explicitly gives the repeated-support averaging application on page 3 and
reports on page 2 that Minc settled the two-exceptional-parameter face.
Its Section 2 assumes both parameters exceed two, so its later equalization
theorem cannot replace the package's direct argument. The package keeps
that distinction. This is a cited-theorem and source-access boundary, not
evidence of an invalid inequality.

For marginal cuts, the incident-column construction and cofactor
nonnegativity give the stated row caps. The omitted support cases
z=0,n-1,n respectively violate total row mass, partial indecomposability,
and positive column mass. Increasing each capped row to 1/q increases
the relaxed product because the uncapped mean exceeds one. This is a
valid upper bound even when its optimizing line totals do not come from
a stationary matrix.

The cleared polynomials in the independent checkers are exactly the
claimed product-gap inequalities. Their denominators are positive on the
certified intervals. Their degrees are at most 65 and 82, so interpolation
proves identities, not sampled positivity. The closed interval covers are
[0,1/400], [1/400,1/75], [1/75,1/20] in dimension 8 and
[0,1/500], [1/500,1/200], [1/200,3/100] in dimension 9.
All junctions are included. The monotone scalar deficit excludes larger
feasible parameters.

The dimension-specific proper-cut route covers 15 ordinary and six special
ordered cases for n=8 and all 28 ordered cases for n=9. The unified route
also covers every proper cut. The two routes need not use the same
numerical floor: each marginal certificate uses the floor established
by its own checker.

## Dimension 7

The six ordinary cut types, six mixed-sign configurations, and three
both-positive p=1 types at study/audit-n7.md, lines 402-417, exhaust the
proper cuts up to transposition. The one-sided argument covers all six
complement sizes. Zero excess is included in the mixed-sign cases, and
both excesses cannot be nonpositive when the Hall deficit is positive.

The complementary-minor entropy argument handles zeros by smoothing.
A positive selected entry lies in a positive permutation by Birkhoff
decomposition, so its complementary permanent is positive. When a weight
vanishes, the explicit smoothing lower bound makes its weighted logarithm
tend to zero. There is no hidden positivity assumption on all minors.
For a p=1 core every supported matching uses exactly one core edge, giving
the required exponential permanent bound.

The one-sided stationarity identity has positive denominators, and the
single W polynomial suffices for every positive entropy value. The
conditional-energy estimate also holds for line sums below their group
mean. The core variation scales existing entries, so it is feasible in
both directions at the boundary.

On each both-positive bridge square, the cleared numerator has the same
sign as the stationarity lower bound. The entropy polynomial compares
bounds on the same product s*u. Neither s nor u is divided out.
Requiring a positive unsquared numerator prevents a spurious implication
after squaring.

I compared the builders and traversal in the primary n6-n7 verifier,
lines 408-514, and the independent SymPy verifier, lines 253-322.
All three polynomials stay on the same box, and both children of every
unresolved box are enqueued. Each leaf requires strict coefficient
positivity of the direct polynomial or both entropy polynomials.
The recorded counts (39,10,10,8), (35,9,9,6), and (47,11,13,8)
agree. Those counts are checked after actual coefficient tests and do not
replace them. The primary and independent outputs therefore correspond
to the analytic obligations, including the whole square and its edges.

## Inherited dimensions 5 and 6 and the repaired defect

The SOS identities have the correct homogenization. On total mass n
their left sides equal
n^n*(Phi(U_n)-Phi(A))-lambda*||A-U_n||_F^2,
with lambda=32 and 128. All multipliers x_u*x_v are nonnegative.
The stated positive semidefinite Gram matrices prove the inequality and
unique equality case. With a zero row-sum Gram matrix, positivity of its
principal block is sufficient: subtracting the final coordinate times
the all-ones vector reduces its quadratic form to that principal block.

In the inherited dimension 6 check_verified.py, lines 129-132 check
symmetry and zero row sums with Python object integers, and lines 199-247
expand and compare every coefficient. Lines 251-291 use a posteriori
Cholesky error bounds and enforce the combined result by exit status.
The saved output includes alpha=7.514e-5 against error=3.064e-5 for
the main block and ends in CHECK PASS. This provides the recorded
computer-assisted proof under the stated IEEE-754/LAPACK backward-error
assumptions; it is not an unchecked eigenvalue estimate.

The inherited integer check.py originally computed slack and printed
EXACT PSD FAIL for negative slack but exited zero. Its result.json retained
only the first twenty output lines, omitting the final slack. That record
alone did not establish the integer strengthening. I reported this defect.

The full historical log was then located at scratch/n6-exact-psd.log under
the research workspace. I independently read it and verified that its copy
at [study/inherited-n6-exact-psd.log](inherited-n6-exact-psd.log) is byte-for-byte
identical. Lines 27-28 give exact residual slack 1691794048955 and
EXACT PSD PASS. Lines 11 and 13 give denominator 29160000000000,
d=539701313, and delta=2276460137976. The differing README tuning values
were corrected. This is historical evidence, not a new matrix computation.

The integer witness argument is valid. The final N*N^T uses FLINT
integers and the residual uses arbitrary precision integers. Diagonal
dominance gives A+d*J positive semidefinite; the independently checked
identity A*1=0 removes the rank-one term. Floating estimates and the int64
Cholesky loop select a candidate witness. An imperfect intermediate
overflow guard would not invalidate a successful final exact residual
test. In particular, the floating shadow's final-sum test need not certify
every intermediate partial sum for this witness argument to work.

The repaired production suffix now raises SystemExit for negative slack
and prints PASS only otherwise. The new
[step 5 regression test](../deterministic/certified-special-case-check-5/test_exit_gate.py)
extracts and executes that actual suffix, testing slack -1, 0, and
1691794048955. I inspected the source, the pre-fix failure record, and
the passing post-fix result, then independently reran the three small tests;
all passed. The test does not rebuild the large matrix
or pretend to reprove its PSD. The amended PROOF.md identifies both
the complete historical log and the separate gate test. The initial
failure-reporting finding is resolved.

## Evidence and reporting limits

The three new matrix-proof certificate directories have status pass, with
full outputs containing the required primary and independent success
markers and case counts. Their shell wrappers enforce pipeline errors.
The scalar Lean check initially failed during this review; I subsequently
read the corrected theorem source and passing result. Both scalar theorems
report only propext, Classical.choice, and Quot.sound. They prove the
stated real quadratic interface. They do not quantify over matrices or
verify the cut reductions or dimension-specific polynomial bounds. The
assembled matrix proof does not depend on this optional check.

The cited published inputs remain ordinary imported theorems. I read the
relevant statements in the stored Cheon--Wanless paper and the online
Gurvits primary text. Minc's original full theorem text and Hwang's
original positive-maximizer proof were not independently reconstructed.
This review also inherits the recorded dimension 5/6 large arithmetic
runs and does not claim a fresh replay or formalization of them.

The novelty record is appropriately conservative. The public package
already claims this theorem, and the current result is an attributed
assembly and verification. Claims of original discovery, unrestricted
dimension coverage, or full Lean formalization would exceed this verdict.

At initial inspection, several shape fields in problem.json still
described dimensions beginning at seven as locally unresolved. The
coordinating agent is updating them for closure. That is stale metadata,
not a changed theorem. Subject to the stated conventional mathematical
and software trust boundaries, the full requested finite range and its
equality statement are justified.
