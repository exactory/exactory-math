# Strategy study: verify-formally-with-lean4 (obligation `floors`)

Queries (2026-09-06): the ported project scratch/maths-pub-port (PORT-NOTES.md, AXIOMS.txt,
the ported modules Capacity, Gurvits, OneVarCapacity, HStableFac, HStableDerivative,
HStableOrbit, HStableClass, GurvitsInduction, SlicedTower, VanDerWaerden, GurvitsUnconditional);
the report scratch/study-2026-09-06/maths-pub-report.md sections 1-3; Mathlib's maximum
modulus principle (Mathlib/Analysis/Complex/AbsMax.lean) and Gauss-Lucas.

Settled before step 2:
1. Canonical statement: `Dittert.GurvitsFloors` (Dittert/Obligations.lean) over
   `doublyStochastic ℝ (Fin n)` and `Finset (Fin n)` zero blocks.
2. Defined in the port: H-stability (`Gurvits.HStable`, right half-plane), capacity
   (`Capacity.cap`), the row-form product (`Capacity.rowProd`), the extraction step
   (`OneVarCapacity.stone12`), the induction bridges. Defined in Mathlib: `MvPolynomial`,
   `Matrix.permanent`, complex analysis for the restriction lemma.
3. Formal proofs in print: the ported theorems; the restriction lemma and the rectangle
   extraction chain are new.

Constraints on the plan (lemma chain in `Dittert/Floors.lean`, importing the port):
- `vdw`: restate `GurvitsUnconditional.egorychev_falikman` for `B ∈ doublyStochastic ℝ (Fin n)`.
- `rowForm B`: the product of the row linear forms as an `MvPolynomial (Fin n) ℝ`; its
  H-stability (linear forms with nonnegative coefficients and a positive coefficient per row),
  homogeneity of degree n, nonnegative coefficients, top coefficient equal to `B.permanent`
  (the ported `coeff_topIdx` identity or a direct expansion), capacity at least 1 (weighted
  AM-GM with the row sums 1; ported `cap_rowProd` lemma if applicable).
- `restrict_zero_hstable`: H-stability is preserved by setting a variable to zero unless the
  restriction is the zero polynomial.
- `extract`: one extraction step on a homogeneous H-stable nonnegative polynomial whose degree
  in the extracted variable is at most d gives an H-stable (or zero) polynomial in one fewer
  variable with capacity at least ((d-1)/d)^(d-1) times the original, from `stone12`,
  `classFac_hstable`, the derivative closure and `restrict_zero_hstable`; positivity of the
  capacity rules out the zero polynomial.
- `degree_bound`: after extracting h of the b zero-block column variables from `rowForm B`, the
  degree in the next zero-block column variable is at most n - a - h.
- `chain`: iterate over the b variables and apply `gurvitsBound` to the remaining polynomial in
  n - b variables; `prod_G_one`-style telescoping gives the constant.
- The controlled check names `Dittert.gurvits_floors` with requested type `Dittert.GurvitsFloors`.
