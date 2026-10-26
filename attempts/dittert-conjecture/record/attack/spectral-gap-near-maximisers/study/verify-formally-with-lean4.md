# Strategy study: verify-formally-with-lean4

Written 2026-09-04 (step 1 of the strategy's plan). Contract: STUDY.md.
Sources: `references/sources.md` section 3 (formalisation repositories), and the Mathlib
checkout the sibling attack already builds against, read directly rather than from memory.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| Mathlib checkout, `lean-toolchain` | v4.33.1, manifest of 2026-09-03 | 2026-09-04 | the version every claim below is read against |
| Mathlib file index | `perman`, `stochas`, `birkhoff`, `sinkhorn`, `singular` | 2026-09-04 | four relevant modules, listed below |
| `Mathlib/LinearAlgebra/Matrix/Permanent.lean` | full declaration list | 2026-09-04 | 114 lines, 15 declarations |
| `Mathlib/Analysis/Convex/DoublyStochasticMatrix.lean` | full declaration list | 2026-09-04 | 169 lines, 18 declarations |
| `Mathlib/Analysis/Convex/Birkhoff.lean` | full declaration list | 2026-09-04 | 4 declarations |
| `Mathlib/Analysis/InnerProductSpace/SingularValues.lean` | present | 2026-09-04 | 222 lines |

## 2. What Mathlib has

- `Matrix.permanent M = sum over Perm n of prod M (sigma i) i`, with the algebraic identities
  only: `permanent_diagonal`, `permanent_zero`, `permanent_one`, `permanent_isEmpty`,
  `permanent_transpose`, `permanent_permute_rows`, `permanent_permute_cols`, `permanent_smul`,
  `permanent_updateRow_smul`, `permanent_updateCol_smul`, and the card 0 and card 1 cases.
- `doublyStochastic R n` as a submonoid, with membership, non-negativity, unit row and column
  sums, `le_one_of_mem_doublyStochastic`, convexity, permutation matrices, transpose, reindex.
- Birkhoff's theorem: `doublyStochastic_eq_convexHull_permMatrix`,
  `extremePoints_doublyStochastic`, and `l2_opNorm_le_one_of_mem_doublyStochastic`.
- Singular values of an operator on an inner-product space.

## 3. What Mathlib does not have, and what each absence costs

Every one of these is needed by the claim of this attack or by Theorem R, and none is present.

1. **Expansion of the permanent along a row**, `per(A) = sum_j a_ij per(A(i|j))`. Mathlib's
   permanent file has no minor, no cofactor, no expansion. This is the first tool any argument
   about a permanent uses, and Theorem R uses it in three places. Cost: a `Matrix.submatrix`
   development for the permanent, comparable to `Matrix.det`'s own expansion file.
2. **The van der Waerden inequality** `per(B) >= n!/n^n` on `doublyStochastic`. Not present.
   Its proof (Egorychev 1981, Falikman 1981) goes through Alexandrov's inequality for mixed
   discriminants, itself absent. Cost: a formalisation project in its own right; no formal
   proof of it exists in any repository searched.
3. **The Knopp-Sinkhorn boundary minimum** `m_n = (n-2)! ((n-2)/(n-1)^2)^(n-2)`, which is the
   lower bound every step of this attack contradicts against. It rests on item 2.
4. **Sinkhorn scaling**: existence, uniqueness, and convergence of the diagonal scaling of a
   fully indecomposable non-negative matrix to a doubly stochastic one. Not present.
5. **Capacity** `cap(A) = inf over z > 0 of prod (Az)_i / prod z_j`, and the identity
   `per(A) = cap(A) per(B)` at the scaling. Not present, and it rests on item 4.
6. **The weighted bipartite Laplacian and its spectral gap.** Mathlib has singular values of an
   operator, but not `lambda_2` of a weighted bipartite graph as a Rayleigh quotient over the
   orthogonal complement of the all-ones vector, and not effective resistance. The claim of this
   attack is a statement about exactly that quantity, so it cannot even be *stated* without it.

## 4. Constraints on the plan

Precondition question 2 of this strategy asks whether the objects have definitions in core Lean
or Mathlib. For this attack's claim the answer is **no**, and item 6 makes it a no at the
statement, not merely at the proof: the theorem cannot be written down before a definition of
the spectral gap of a weighted bipartite graph is built.

The one thing that *is* formalisable without new library is a finite arithmetic residue over the
integers, which is what the sibling attack encodes in `attack/dittert-conjecture-n5-to-n15/
deterministic/formal-check-1`: orbit indices, a Gram matrix, an integer Cholesky, all decidable
`Bool` computations needing no analysis at all. That is a check of a fixed dimension, not of the
uniform statement this attack makes, so it does not discharge anything here.

## 5. Stop reason

The queries ran dry at the library itself: the six absences above are measured from the
checkout, not estimated, and item 6 is fatal to the statement step 2 would have to fix.
