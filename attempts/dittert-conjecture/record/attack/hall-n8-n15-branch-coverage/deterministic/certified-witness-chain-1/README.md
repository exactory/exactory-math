# Certified witness chain for every Hall branch, n=8,...,15

Inputs: the exact formulas and analytic interfaces in ../../PROOF.md and the
pinned source at
../../../dittert-completion-tree/study/external-proof/unified/verify_unified_reductions.py.

Run ./check.sh. No third-party packages are needed. Jobs are sequential, run
with nice level 15, and thread environment variables are fixed to one.

The first implementation is the source's power-basis polynomial arithmetic,
power-to-Bernstein conversion, and Sturm sequence checker. source_certificate.py
executes only the relevant n=8,...,15 finite families, not any large permanent
matrix computation. The source's SHA256 is printed in source-output.txt.

The independent implementation imports no source or older checker code.
It enumerates all 596 ordered omitted-size pairs including full cuts and
every marginal size/orientation. Its 428 ordered scalar cases include each
proper ordered pair and one proved normalized marginal case per n. Both
scalar programs leave exactly the n=8 and n=9 marginal rows, then prove all
9 residual interval certificates, corresponding to 2 near-zero intervals,
6 dimension-8 support cases, and 1 dimension-9 compressed support case.
The full dimension-9 support set z=1,...,7 is covered by the proved
monotonicity argument, explicitly validated in the coverage metadata.

The independent program evaluates the literal cleared polynomial directly
in the Bernstein basis on its required interval. For degree m and n factors,
B_i^m B_j^n =
choose(m,i) choose(n,j)/choose(m+n,i+j) B_(i+j)^(m+n).
Addition uses exact degree elevation. This derives the coefficients from
the formula without using the source's power expansion or conversion.
Strictly positive Bernstein coefficients imply strict positivity at every
point of the closed interval because the basis is nonnegative and sums to
one. All 9 polynomials passed without subdivision. In particular the two
near-zero certificates need no Sturm theorem in this independent route.

The independent file also checks every n's global deficit localization
constants, both signs through the analytic lemma, positive denominators,
ceil-rounded square-root enclosures, exact marginal tail endpoints,
transposition invariance, and the complete cut and support sets.
Its 65 mutation and arithmetic regressions reject omitted full/proper/marginal
cases, omitted support sizes, missing junctions and endpoints, gaps,
rounding down the localization, unjustified n=8 support compression, and a
negative polynomial. Polynomial evaluation identity checks at four rational
points are extra implementation checks, not a substitute for the explicit
polynomial construction.

Coverage range: every dimension 8,...,15, every Hall deficiency 0<=u<1,
every minimizing cut and every feasible selected-column zero count.
No first uncovered dimension is claimed; n=16 is outside this task.
The high-dimensional quadratic is positive on all [0,1]; the n<=10
localization is derived from a global deficit bound; marginal n=8,9 use
[0,s] union [s,v], with the remaining feasible tail excluded by monotonicity
and the total deficit budget. All junctions are included.

Trusted base: the analytic proof in ../../PROOF.md; its explicitly listed
structural and permanent-floor theorems, audited separately by the parent;
Python 3 integer and fractions.Fraction arithmetic; the exact polynomial
and Bernstein identities just described. This is not a Lean proof.
A passed result.json certifies the finite residue and coverage checks; it
does not independently verify a theorem whose proof is outside this step.

