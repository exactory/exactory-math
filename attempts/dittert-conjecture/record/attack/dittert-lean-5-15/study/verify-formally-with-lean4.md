# Strategy study: verify-formally-with-lean4

Queries (2026-09-06): the tier-one and code-search queries in study/problem.md; the local Mathlib
checkout grep listed there; the READMEs and Lean sources of the two prior Dittert formalizations;
the DCPRevere/maths-pub Lean project sources and axiom freeze; the local formal-check packages of
attack/hall-scalar-lean-n11-n15 and attack/hall-near-zero-lean-n8-n9.

## Settled before step 2

1. Canonical formal statement: none (formal-conjectures has no Dittert entry). The statement is
   written here as `Dittert.Statement n`, over `Matrix (Fin n) (Fin n) ℝ` with
   `Matrix.permanent`, row sums `∑ j, A i j`, column sums `∑ i, A i j`, and the constant
   `(n.factorial : ℝ) / (n : ℝ) ^ n`.
2. What core or Mathlib defines: `Matrix.permanent` with multilinearity in one row or column and
   invariance under transposition and permutations (Mathlib/LinearAlgebra/Matrix/Permanent.lean);
   `doublyStochastic` and Birkhoff (Mathlib/Analysis/Convex); Hall's marriage theorem
   (Mathlib/Combinatorics/Hall); Gauss-Lucas (Mathlib/Analysis/Complex/Polynomial/GaussLucas.lean);
   the maximum modulus principle (Mathlib/Analysis/Complex/AbsMax.lean); compactness maxima
   (`IsCompact.exists_isMaxOn`); `MvPolynomial`. Absent: row expansion of the permanent along a
   row with minors, max-flow/min-cut, H-stable polynomials, Gurvits's capacity theorem, the van der
   Waerden bound.
3. Formal proofs and native evaluations in print:
   - kernel-checked, standard axioms: Gurvits's theorem and van der Waerden in DCPRevere/maths-pub
     (Lean v4.32.2); the local n = 11..15 scalar certificates and the n = 8, 9 near-zero polynomials
     (Lean v4.33.1, Mathlib 0df444a3);
   - native evaluation only: the n = 4 and n = 5 SOS formalizations in print, and the local n = 5, 6
     certificate check (attack/dittert-conjecture-n5-to-n15/deterministic/formal-check-2).

## Constraints on steps 2 to 6

- Encode the proof as a blueprint of obligation statements, each a Lean `Prop`, with the case
  bridges as conditional theorems taking the obligation `Prop`s as hypotheses, so that every bridge
  can be checked before its premises are proved (references/lean4.md, section 8).
- Port the Gurvits and van der Waerden modules from maths-pub (Apache-2.0, attribution retained)
  to Lean v4.33.1 and the pinned Mathlib; derive the rectangle floors from the per-variable
  extraction step if it is available, otherwise prove that step on top of the ported closure lemmas.
- Build the Hall domination theorem by the augmenting-path argument on a maximizing flow
  (compactness gives a maximizer; the reachable set gives the cut), since Mathlib lacks max-flow.
- Scalar certificates are proved in the kernel by the chunked Bernstein method measured today: the
  degree-82 support polynomial elaborates in 65 s with `-M 16384`; the baseline memory of a module
  holding 840-digit coefficients is 1.7 GB, so `-M 2048` is not a usable limit. Lean modules that
  carry certificates set `-M 16384` and build with one job.
- `native_decide`, `decide +native`, custom axioms and `sorry` are excluded by the contract's proof
  policy; the finite residue is discharged by `decide`, `norm_num`, `ring`, `positivity`, `linarith`
  and reflection-style evaluation lemmas only.
- The build reuses the shared Mathlib cache through an absolute `packagesDir` in
  `lake-manifest.json`; a relative `packagesDir` makes a fresh copy re-clone and recompile Mathlib.
