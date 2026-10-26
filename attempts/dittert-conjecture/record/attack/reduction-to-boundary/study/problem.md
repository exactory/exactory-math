# Problem study: reduction to boundary maximizers (obligation `reduction`)

Claim: for every integer n >= 2, if every maximizer of Phi on K_n is entrywise positive, then
Phi(A) <= 2 - n!/n^n for every A in K_n with equality if and only if A is the uniform matrix.
Formal reading: `Dittert.Reduction` in the blueprint.

## Queries (source, string, date)

- The root study's tier-one queries (attack/dittert-lean-5-15/study/problem.md, 2026-09-06).
  Relevant hits: Hwang 1986 (DOI 10.1016/0024-3795(86)90212-0, publisher abstract: a positive
  maximizing matrix must be the uniform matrix) and Hwang 1987; Cheon-Wanless 2010 (which
  reports Hwang's positive-maximizer result).
- Local record: attack/dittert-branch-complete-audit/BRANCH_TRANSPORT.md sections 2 and 3
  (compactness, stationarity, the pair-averaging argument with the strict Hessian at the
  uniform matrix, valid for every n >= 2); attack/dittert-completion-tree/study/audit-n7.md
  ("Complete interior argument").
- Mathlib (rev 0df444a3): `Matrix.permanent` with `permanent_updateRow_smul`,
  `permanent_updateRow_add` (multilinearity in a row), `permanent_permute_rows`,
  `permanent_transpose`; `IsCompact.exists_isMaxOn`; no row expansion with minors.

## What was learned, as constraints on the plan

1. The proof used here avoids the Hessian and the convergence of iterated averaging. Mixing two
   rows i and k of a matrix A along ((1-t) x + t y, t x + (1-t) y) keeps all column sums and the
   total, and Phi(A_t) is a quadratic polynomial in t that is symmetric under t -> 1 - t (the
   permanent is multilinear in rows and invariant under swapping rows i and k; the row product
   is (r_i + t (r_k - r_i)) (r_k + t (r_i - r_k)) times the others), so Phi(A_t) = Phi(A) + alpha
   t (1 - t). At a positive maximizer both directions t in (-epsilon, epsilon) are feasible, so
   alpha = 0 and Phi is constant along the whole mixing line. If a positive maximizer N has two
   distinct rows (or, symmetrically, two distinct columns), the direction X = mixing direction is
   nonzero and has a negative entry, so following the line to the first zero entry gives a
   feasible matrix with a zero entry and the same value: a boundary maximizer, contradicting the
   hypothesis. Hence every maximizer has all rows equal and all columns equal, so it is uniform.
2. Existence of a maximizer: K_n is closed and bounded in the finite-dimensional space of
   matrices (entries in [0, n]) and Phi is continuous (a polynomial in the entries), so
   `IsCompact.exists_isMaxOn` applies.
3. The value at the uniform matrix: per(J_n/n) = n!/n^n (every permutation contributes
   1/n^n) and both products equal 1, so Phi(J_n/n) = 2 - n!/n^n.
4. Conclusion: every A in K_n satisfies Phi(A) <= Phi(max) = Phi(J_n/n), and Phi(A) = Phi(J_n/n)
   makes A a maximizer, hence uniform; conversely the uniform matrix attains the value.

## Stop reason

The queries ran dry: the argument's inputs are elementary and the sources agree.
