# Strategy study: reduce-to-a-finite-computation

Written 2026-09-04 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

The query set of `novelty.md`, plus the sibling attack's own record of what a
sum-of-squares certificate costs on this family: `study/gate-symmetry-blocks/blocks-output.txt`
and `deterministic/numerical-optimisation-run-3` of `attack/dittert-conjecture-n5-to-n15`.

## 2. Hits worth reading

- arXiv:2607.29191 (Li, Xiong, Yang): the only finite computation in print on this family,
  an exact sum-of-squares certificate for a degree-4 polynomial in 16 variables.
- The sibling attack's own runs: the same method reaches `n = 5` (degree 6, 25 variables,
  main Gram 2925) and `n = 6` (degree 6, 36 variables, main Gram 8436) with symmetry
  reduction, and stops at `n = 7`.

## 3. What was learned, as constraints on the plan

1. **The claim of this attack is not a polynomial inequality.** `lambda_2(A)` is defined
   through the second singular value of `D_r^{-1/2} A D_c^{-1/2}`, so the constraint set is
   semialgebraic but only after introducing the characteristic polynomial of a `2n x 2n`
   matrix; the resulting formulation has degree of order `n` in `n^2 + O(n)` variables, far
   above the degree-6 problems the sibling attack could certify at `n = 5` and `6`.
2. **The relaxation route is worse, not better.** Replacing `lambda_2 >= c` by the
   equivalent `sigma_2 <= 1 - c`, that is `M^T M - (1-c)^2 I` having exactly one eigenvalue
   above the threshold, needs a determinantal condition of the same degree.
3. **The direct route is already spoken for.** Certifying the claim at fixed `n` by
   sum-of-squares is, by Theorem R, no easier than certifying Dittert's conjecture at that
   `n` directly, which the sibling attack did at `n = 5` and `6` and could not do at `n = 7`.
   So this strategy offers nothing that attack has not already tried on the cleaner statement.

## 4. Stop reason

The queries ran dry: the only prior finite computation is the sibling attack's own, and its
measured reach settles this strategy's ceiling before any run is made.
