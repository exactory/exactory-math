# Scalar Hall exclusion in dimensions 11 through 15

## What this package proves

For every natural n with11<=n<=15, every natural a,b with0<a+b<n, and every real u<=1, the explicitly defined rational constants in Definitions.lean satisfy

    curvature(n,a,b)*u^2 + floor(n,a,b)*(1-u)^n - gamma(n) > 0.

Main.lean proves this as HallScalar.scalar_positive. It then proves that no real P,delta can simultaneously satisfy the permanent lower bound, the quadratic deficit lower bound and P+delta<=gamma(n). Audit.lean exposes the same statement as hall_scalar_certificate, which step.json names for the harness.

This is not a theorem over matrices. The words floor, P and delta are scalar names, not definitions of a matrix permanent or its deficit. The Hall construction, marginal row selection, structural exclusions, permanent floors and matrix deficit bounds remain outside the formalization. The full cut(0,0) is excluded; the matrix proof handles it separately. There is no first-Dittert-formalization or new mathematical proof claim.

## Direct definitions and coverage

Definitions.lean implements factorial and rational formulas, exactly as stated in problem.json and the upstream scalar argument. Finite.lean checks each of five dimensions using decide +kernel. It quantifies over every ordered pair in Fin15, not only a<=b. Reduced means a,b>0 and a+b<n, or the normalized marginal(n-1,0). The counts46,56,67,79,92 and their sum340 are themselves Lean theorems. all_good embeds arbitrary valid natural sizes and handles both marginal orientations by equality of the formulas. The source-level independent review counts455 original nonfull size pairs.

Main.lean transports these rational inequalities to reals, proves the completed-square identity with ring, and applies Mathlib's Bernoulli inequality. The proof applies to all u<=1, not only a small root or a finite grid. Tests.lean checks domain boundaries, a hand-computed factorial ratio, and applications at u=0, u=1 and negative u.

## Reproduction and trusted base

Lean: leanprover/lean4:v4.33.1.
Mathlib: v4.33.1, commit0df444a360eaa60ab8c11dca51a86af692955474, with every dependency revision pinned in lake-manifest.json.

With elan and dependencies available, from this directory:

    lake exe cache get
    lake build

The local preparation reused cached dependencies with an optional .lake/packages symlink. That symlink is not in the portable archive; the pinned manifest has no absolute dependency path. A clean checkout may need a substantial dependency download. No full Mathlib source rebuild was needed in this workspace.

From the research root, with Exactory on PATH:

    nice -n 15 exactory-math verify lean hall-scalar-lean-n11-n15 formal-check-1

The package config sets one Lean thread and a2048MB memory ceiling. Set LEAN_NUM_THREADS=1 for the Lake driver too. Independent replay is sequential. The final result.json must say pass; its transitive axiom list must be a subset of propext, Classical.choice, Quot.sound. Merely compiling a file containing sorry is not success. The preserved initial-red-result.json demonstrates that the gate rejected such a skeleton.

The proof has no native_decide, compiler-trust axiom, new axiom, admitted lemma, external Python verdict, or rational result table as a premise. As usual, confidence still depends on Lean's kernel and standard axioms, the faithful statement, the installed toolchain, and the execution environment. No independent alternate-kernel checker was installed or run.

## Attribution and evidence

The mathematical scalar argument is due to Pedro Paulo Marques do Nascimento's public working proof, pinned at https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701. The local direct arithmetic reconstruction is in hall-n8-n15-branch-coverage. The completed-square Lean lemma adapts the pre-existing local DittertScalar proof, expanded here with dimension-dependent constants, coverage, Bernoulli and the relaxed budget.

Earlier Dittert Lean work: Li, Xiong and Yang, arXiv:2607.29191v2, dimension4. No priority claim is made. See the attack's study and manuscript source map.

Resource observations are in ../../study/resource-measurements.json. They separate incremental stages and do not measure total development effort, total API cost, or a clean dependency installation.
