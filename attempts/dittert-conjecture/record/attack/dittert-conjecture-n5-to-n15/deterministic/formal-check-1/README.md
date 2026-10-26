# formal-check-1: Lean 4 project for the attack

Step kind: formal check. Built 2026-09-03 with Lean 4 v4.33.1 and Mathlib v4.33.1
(`lake new formal-check-1 math`, `lake exe cache get`; project files `lakefile.toml`,
`lean-toolchain`, `Main.lean`, `step.json`).

## What `Main.lean` contains

1. `kafidov_inequality_16 : 0 < kafidovK 16` and `kafidov_fails_15 : kafidovK 15 < 0`,
   where `kafidovK n = mN n - gammaN n - n^3 (mN n)^2 / (4 (1 - gammaN n))`,
   `gammaN n = n!/n^n`, `mN n = (n-2)! ((n-2)/(n-1)^2)^(n-2)` over `ℚ`. This is the
   only dimension-dependent inequality of the boundary-exclusion proof of
   arXiv:2607.19439 (its (4.3)); the two theorems certify, by kernel-checked rational
   arithmetic (`decide` for the factorials, `norm_num` for the rational comparison),
   that the published argument closes `n = 16` and does not reach `n = 15`. The
   theorem named in `step.json` is `kafidov_inequality_16`; `verify lean` records its
   axiom list.
2. `dittert_five` and `dittert_five_stability`: the statement of Dittert's conjecture
   at `n = 5` (`phi5 A ≤ 2 - 120/3125` for nonnegative `5 x 5` real matrices with entry
   sum 5) and its quantitative form with `c_1 = 32/3125`, exactly as certified by
   `certified-special-case-check-1`. Both proofs are `sorry`. They state the theorem
   the certificate proves, read against the claim quantifier by quantifier (the
   permanent is defined as the sum over `Equiv.Perm (Fin 5)`), and are the blueprint
   for the formal verification that this record does not contain.

## What it decides

The exact status of the published analytic route at `n = 15` and `n = 16`, now with
the trusted base of Lean's kernel (standard axioms only, see `result.json`), in
agreement with `certified-special-case-check-3`. Nothing about `n = 5` beyond the
statement: the certificate check in Lean is open work (a 2925 x 2925 rational
positive-semidefiniteness check needs either the isotypic reduction inside Lean or
a native evaluation, both beyond this attack's budget).
