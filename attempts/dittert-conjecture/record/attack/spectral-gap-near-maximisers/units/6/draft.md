# What Mathlib would need before Dittert's conjecture can be checked by machine

**Form.** Survey or problem paper. **Venue.** Off to the side of Dittert's conjecture, and on the
path of anyone who wants to check it, or Theorem R, in Lean 4.

## 1. What was read

Mathlib at toolchain `leanprover/lean4:v4.33.1`, manifest of 2026-09-03, the checkout the sibling
attack builds against. Every statement below was read from the declaration lists of the four
relevant modules, not recalled.

## 2. What Mathlib has

- `Mathlib/LinearAlgebra/Matrix/Permanent.lean`, 114 lines. `Matrix.permanent M` is defined as
  the sum over `Perm n` of the product of `M (sigma i) i`, with fifteen declarations, all
  algebraic: `permanent_diagonal`, `permanent_zero`, `permanent_one`, `permanent_isEmpty`,
  `permanent_transpose`, `permanent_permute_rows`, `permanent_permute_cols`, `permanent_smul`,
  `permanent_updateRow_smul`, `permanent_updateCol_smul`, and the cardinality 0 and 1 cases.
- `Mathlib/Analysis/Convex/DoublyStochasticMatrix.lean`, 169 lines. `doublyStochastic R n` as a
  submonoid, with membership, non-negativity, unit row and column sums,
  `le_one_of_mem_doublyStochastic`, convexity, permutation matrices, transpose, and reindexing.
- `Mathlib/Analysis/Convex/Birkhoff.lean`. Birkhoff's theorem as
  `doublyStochastic_eq_convexHull_permMatrix`, `extremePoints_doublyStochastic`, and
  `Matrix.l2_opNorm_le_one_of_mem_doublyStochastic`.
- `Mathlib/Analysis/InnerProductSpace/SingularValues.lean`, 222 lines. Singular values of an
  operator on an inner-product space.

## 3. The six pieces that are missing

Each is needed by Dittert's conjecture or by Theorem R, and none is present.

1. **Expansion of the permanent along a row.** Mathlib's permanent file has no minor, no cofactor,
   and no expansion. It is the first tool any argument about a permanent uses, and Theorem R uses
   it in three places. Cost: a submatrix development for the permanent, comparable to the
   determinant's own expansion file.
2. **The van der Waerden inequality** on the doubly stochastic matrices. Its proofs (Egorychev
   1981, Falikman 1981) go through Alexandrov's inequality for mixed discriminants, itself absent.
   A formalisation project in its own right; none was found in any repository searched.
3. **The Knopp-Sinkhorn boundary minimum**, the lower bound every step of the spectral route
   contradicts against. It rests on item 2.
4. **Sinkhorn scaling**: existence, uniqueness, and convergence of the diagonal scaling of a fully
   indecomposable non-negative matrix to a doubly stochastic one.
5. **Capacity**, and the identity relating the permanent of a matrix to the capacity times the
   permanent of its scaling. Rests on item 4.
6. **The spectral gap of a weighted bipartite graph**, as a Rayleigh quotient over the orthogonal
   complement of the all-ones vector, together with effective resistance. Mathlib has singular
   values of an operator, which is not the same object.

## 4. Why the sixth is different from the first five

The first five block a proof. The sixth blocks the statement: the spectral claim of the sibling
attack is a statement about the spectral gap of a weighted bipartite graph and cannot be written
in Lean before that quantity is defined. That is what turns the formalising strategy's
precondition question, whether the objects have definitions in core Lean or Mathlib, into a plain
no.

## 5. What is formalisable today

A fixed-dimension integer computation. The sibling attack encodes one in its Lean project: the
`n = 5` sum-of-squares certificate, rebuilt inside Lean from 52 KB of rational data, with the
monomial orbits recomputed from the group generators, the identity checked coefficient by
coefficient, and positive semi-definiteness checked by an exact integer Cholesky factorisation on
the kernel of the all-ones vector. Every step is a decidable computation over the integers; no
analysis and no reals appear. It discharges a single dimension and nothing uniform, and because it
takes about forty minutes of native code it is out of reach of the kernel's own reduction, so it
rests on the compiler-trusting axiom in addition to the standard ones.

## 6. References

- Mathlib, leanprover-community/mathlib4, toolchain v4.33.1, manifest of 2026-09-03.
- Egorychev, Advances in Mathematics 42 (1981) 299-305; Falikman, Matematicheskie Zametki 29
  (1981) 931-938.
- Knopp and Sinkhorn, Linear and Multilinear Algebra 11 (1982) 351-355.

## 7. Ledger

Obligations: the six statements of section 3, which the record now owes to anyone who wants a
machine-checked proof.
