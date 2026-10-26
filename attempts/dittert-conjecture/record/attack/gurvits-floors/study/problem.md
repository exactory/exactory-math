# Problem study: the Gurvits permanent floors (obligation `floors`)

Claim: for every n >= 1 and every doubly stochastic n by n real B, per(B) >= n!/n^n, and for
all a, b >= 1 with a + b <= n - 1, if some a rows and b columns of B form a zero block then
per(B) >= gamma(n-a) gamma(n-b) / gamma(n-a-b). Formal reading: `Dittert.GurvitsFloors`.

## Queries (source, string, date)

- The root study's tier-one queries (attack/dittert-lean-5-15/study/problem.md, 2026-09-06);
  Gurvits arXiv:0711.3496 (Theorem 4.10 and Fact 4.9: the degree-refined extraction and the
  preservation of stability), Laurent-Schrijver (Amer. Math. Monthly 2010) as the elementary
  presentation; the local proof attack/dittert-completion-tree/study/audit-n7.md section 3
  ("Dimension-independent rectangular zero-block lemma", the extraction order and the degree
  bound n - a - h at step h, the telescoping product G(n-a) ... G(p+1) = v_{n-a} / v_p).
- github.com/DCPRevere/maths-pub (Apache-2.0, 2026-08-12), read in full by the study of
  2026-09-06 (scratch/study-2026-09-06/maths-pub-report.md) and ported to Lean v4.33.1 /
  Mathlib 0df444a3 on 2026-09-06 (scratch/maths-pub-port, PORT-NOTES.md, AXIOMS.txt): the
  following are kernel-checked with propext, Classical.choice and Quot.sound on our toolchain:
  `GurvitsUnconditional.gurvitsBound` (gamma_N cap(p) <= [x_1...x_N] p for H-stable homogeneous
  p of degree N in N variables with nonnegative coefficients; right half-plane convention
  Re z_i > 0), `GurvitsUnconditional.egorychev_falikman` (van der Waerden),
  `OneVarCapacity.stone12` with `g_eq` (the single-variable extraction with the exact constant
  ((d-1)/d)^(d-1), d the exact degree in the extracted variable), `HStableFac.classFac_hstable`
  (its factorisation hypothesis for homogeneous H-stable nonnegative polynomials),
  `GurvitsInduction.eval_reduce_of_fac`, `capOne_eq_cap`, `coeff_topIdx_reduce`, `prod_G_one`,
  and the closure of H-stability under partial derivatives, products, linear forms with
  nonnegative coefficients and substitution (HStableDerivative, HStableOrbit, HStableClass).
- The same report (section 2, item 5): closure of H-stability under setting a variable to zero is
  not proved there; the development works at `reduceAt delta`, delta > 0.

## What was learned, as constraints on the plan

1. Van der Waerden is the ported `egorychev_falikman` (statement over `Matrix (Fin n) (Fin n) ℝ`
   with row and column sums 1), so the first conjunct is a restatement.
2. The rectangle floor needs, on top of the port: (a) the restriction lemma: if p is H-stable
   and p(z', 0) is not the zero polynomial then z' -> p(z', 0) is H-stable (proof by the minimum
   modulus principle on a disc for the univariate family t -> p(w + t e, i epsilon), epsilon -> 0,
   or by the ported derivative and substitution closures where they suffice); (b) the degree
   bookkeeping: after extracting h of the b zero-block column variables from the row-form
   product of B, the degree in the next such variable is at most n - a - h, because the a
   zero-block rows contain none of these variables and each extraction removes one other row
   factor; (c) the telescoping identity prod_{h<b} G(n-a-h) = v_{n-a} / v_{n-a-b} (from
   `prod_G_one`) and the final application of `gurvitsBound` to the remaining polynomial in
   n - b variables whose top coefficient is per(B).
3. `Capacity.rowProd` and the weighted AM-GM lower bound cap >= 1 for doubly stochastic row
   forms are in the port (`cap_rowProd` lemmas of VanDerWaerden); the extraction chain is
   assembled in a new module `Dittert/Floors.lean` on top of the ported modules.

## Stop reason

The queries ran dry: the mathematical inputs are Gurvits's theorem and its extraction step,
both already formal, and one elementary closure lemma.
