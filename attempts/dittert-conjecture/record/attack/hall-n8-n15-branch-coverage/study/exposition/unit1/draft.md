# Independent verification of the n=8,...,15 Hall branches

For every integer n with 8 <= n <= 15, the Hall-cut argument in the pinned Nascimento proof excludes every boundary global maximizer of R+C-per(A) among nonnegative real n by n matrices of total entry sum n, with no omitted cut, support, parameter, or endpoint branch.

The proof is [PROOF.md](../../../PROOF.md), and [CODE_MAP.md](../../../CODE_MAP.md)
links every source branch reduction to its mathematical justification.
This is an attributed reconstruction of Pedro Paulo Marques do Nascimento's
[pinned proof](https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701),
not a new mathematical discovery.

Every minimizing cut is full, marginal, or proper. Full cuts force double
stochasticity; marginal averages reduce to a smallest line; proper cuts
force a zero rectangle in the dominated matrix. A deficit estimate valid for
both signs of each subset excess gives delta>=C*u² on the entire Hall domain.
Marginal stationarity strengthens this coefficient and proves denominator
positivity before division.

The completed-square contradiction holds on all [0,1] for n=11,...,15.
For n=8,9,10, the global deficit budget implies the required localization.
All proper cuts then close, as does the n=10 marginal case. The residual
marginal cases in n=8,9 use exact near-zero and support-cap inequalities on
closed intervals, including every junction. A proved increasing deficit
excludes the whole remaining feasible tail. The n=9 support compression
uses inclusion of feasible product domains and a floor independent of the
zero count.

The [fresh deterministic result](../../../deterministic/certified-witness-chain-1/result.json)
is pass. The source's power/Sturm checker and the independent direct-Bernstein
checker both pass. The independent implementation checks 596 ordered cut-size
pairs, 428 ordered scalar cases, 9 residual interval certificates, and 65
mutation/arithmetic regressions. All 9 residual polynomials have strictly
positive Bernstein coefficients on their full closed intervals without
subdivision.

The structural and permanent-floor inputs are explicit in PROOF section 1.
They include Cheon--Wanless (DOI 10.1016/j.laa.2010.08.041), the capacity
rectangle floor from Gurvits (arXiv:0711.3496), and the two-independent-zero
floor for n=8,9,10. The parent audits these interfaces separately.
The parent's visual inspection of
[Pula--Song--Wanless](https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1022.pdf)
Section 2 corrects an older text-extraction error: its two size parameters
are at least 2, which includes the required face.

The complete coverage follows after those cited interfaces. The older
omitted Sinkhorn large-cost branch is neither proved nor used by this
argument. No full Lean formalization or originality claim is made.
