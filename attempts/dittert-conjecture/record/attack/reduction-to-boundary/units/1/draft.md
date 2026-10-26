# Formalisation unit: reduction-to-boundary

## Statement

For every integer n >= 2: if every n by n real matrix with nonnegative entries and total entry sum n that attains the maximum of Phi(A) = prod_i r_i(A) + prod_j c_j(A) - per(A) over that set has all entries positive, then Phi(A) <= 2 - n!/n^n for every such matrix A, with equality if and only if every entry of A equals 1/n. Lean theorem Dittert.reduction with requested type Dittert.Reduction, checked with propext, Classical.choice and Quot.sound only.

## Claim, quantifier by quantifier

The controller obligation reads: For every integer n >= 2: if every n by n real matrix with nonnegative entries and total entry sum n that attains the maximum of Phi(A) = prod_i r_i(A) + prod_j c_j(A) - per(A) over that set has all entries positive, then Phi(A) <= 2 - n!/n^n for every such matrix A, with equality if and only if every entry of A equals 1/n.

Quantifiers: For every integer n >= 2 and every n by n real matrix with nonnegative entries and total entry sum n.

The Lean declaration `Dittert.reduction` has the requested type `Dittert.Reduction`, whose definitions are the blueprint's (Dittert/Basic.lean, Dittert/Obligations.lean, Dittert/Scalar/Defs*.lean in the frozen step directory).

## Evidence

- Controlled formal check: `deterministic/formal-check-1/result.json`, status `pass`, axioms ["propext", "Classical.choice", "Quot.sound"].
- Journal moves: [1].

## Moves

- Move 1 (verify-formally-with-lean4 / formalise-while-fresh): Formalized the reduction obligation in Dittert/Reduction.lean: the feasible set is compact and Phi is continuous, so a maximizer exists; Phi at the uniform matrix equals 2 - gamma n; for two rows i, k of a matrix the mixing line (row i becomes (1-t) A i + t A k, row k the complementary mix) preserves the total and the column sums, the row product moves by t(1-t)(r_i - r_k)^2 times the other row sums, the column product is constant, and the permanent is per A + t(1-t)(per A_{k<-i} + per A_{i<-k} - 2 per A) by additivity of the permanent in one row (proved from the column form and transposition, since Mathlib v4.33.1 lacks it); hence Phi is Phi A + alpha t(1-t) along the line; a positive maximizer is feasible on both sides of t = 0, which forces alpha = 0, so Phi is constant along the line, and following the line to the first vanishing entry produces a maximizer with a zero unless the two rows agree; therefore, under the hypothesis that every maximizer is positive, all rows agree, all columns agree by transposition, and the maximizer is the uniform matrix; installed the frozen project and ran the controlled formal check of Dittert.reduction. Output: Dittert.reduction : Dittert.Reduction is kernel-checked with propext, Classical.choice and Quot.sound only (Dittert/Reduction.lean, 502 lines, no sorry).

## Provenance

See study/problem.md, study/verify-formally-with-lean4.md and novelty.md of this node; ported sources are attributed in their file headers.
