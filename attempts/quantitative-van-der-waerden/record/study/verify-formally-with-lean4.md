# Strategy study: verify-formally-with-lean4

Written 2026-09-04 (step 1 of the plan). Contract: STUDY.md.

## 1. Queries

The formalisation sources of `references/sources.md`, section 3, and the Mathlib checkout the
sibling attack builds against (toolchain `leanprover/lean4:v4.33.1`, manifest of 2026-09-03),
read directly. The sibling attack's survey of that checkout
(`attack/spectral-gap-near-maximisers/study/verify-formally-with-lean4.md`) is reused: it lists
the declarations of `Mathlib/LinearAlgebra/Matrix/Permanent.lean` and
`Mathlib/Analysis/Convex/DoublyStochasticMatrix.lean`.

## 2. What was found

- No formalisation of the van der Waerden inequality exists in any repository searched, and no
  formalisation of any deficiency version of it.
- Mathlib defines `Matrix.permanent` and `doublyStochastic`, so the objects of the claim exist,
  but it has no expansion of the permanent along a row and no inequality about it at all.
- The `n = 3` case of the claim is, after the six margin equations, a polynomial inequality in
  four real variables, and the proof in the record (`route-interpolation.md`, Theorem 2) is an
  exact identity plus Schur's inequality in three non-negative variables. Both are within reach
  of `nlinarith` once the three Schur instances are supplied as hints.

## 3. What was learned, as constraints on the plan

1. **Encode the finite residue, not the chain.** The general claim rests on Theorem 1 and 2 of
   the capacity route, whose proof goes through Gurvits' theorem on H-stable polynomials, which
   Mathlib does not have; encoding that chain means building the capacity library first (the
   sibling survey's item list). Precondition question 4 is yes, so step 3 of the plan sends the
   attack to step 4: encode the one dimension where the claim is sharp and its proof is a
   polynomial certificate, `n = 3`.
2. **State it on the entries.** Writing the theorem on nine real entries with the six margin
   equations as hypotheses keeps it readable as the claim; `Matrix.permanent` on `Fin 3` would
   need unfolding to the same six monomials anyway.
3. **Schur needs a case split.** `nlinarith` does not find Schur's inequality from the
   non-negativity hypotheses alone; the standard proof orders the variables, and the encoding
   splits on the three pairwise orders and supplies the products it needs in each case.
4. **A kernel-checked result is possible here.** Unlike the sibling attack's certificate checks,
   nothing here needs `native_decide`: `nlinarith` produces a proof term the kernel checks, so
   the expected axiom list is Lean's standard three.

## 4. Stop reason

The queries ran dry at the library: the objects exist, no inequality about them does, and the
one encodable residue is the `n = 3` certificate.
