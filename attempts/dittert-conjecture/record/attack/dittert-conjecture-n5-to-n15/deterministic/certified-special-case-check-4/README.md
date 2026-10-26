# certified-special-case-check-4: the n = 6 main Gram matrix, positive semidefinite over the integers

Step kind: certified special-case check. Produced 2026-09-04.

## What it closes

`certified-special-case-check-2` proves Dittert's conjecture at `n = 6`. Its one step that is not
integer arithmetic is the positive semidefiniteness of the 8436 x 8436 main Gram matrix, which it
establishes by a floating-point Cholesky factorisation with Higham's rigorous backward-error
bound. That is a theorem given IEEE-754 semantics, not a gap, but it is weaker evidence than the
`n = 5` certificate, which is exact throughout. This step replaces it with integer arithmetic.

## The certificate

The exact route of `formal-check-2/Cert/Sym.lean`, at `F = 1`:

    B := A + d J - delta I,     N := integer Cholesky of B, with truncating division,
    E := A + d J - N N^T   is diagonally dominant with non-negative diagonal.

Then `E >= 0` by Gershgorin and `N N^T >= 0`, so `A + d J >= 0`; and `A . 1 = 0` gives `A >= 0`,
hence `M = A / den >= 0`.

No `F` scaling is needed at this size. The integer entries reach `2.479e16`, so the pivots are
around `4.6e12` and their integer square roots carry seven significant digits, which is what `F`
buys at `n = 5` where the entries are smaller.

## Result

    lambda_2 = 4.552920e+12,  d = 539701313,  delta = 2276460137976
    max |N| = 1.4110e+08
    diagonal dominance slack: min 1691794048955
    EXACT PSD PASS

The slack is positive by twelve orders of magnitude, so the certificate is not marginal.

The complete original run log is retained at scratch/n6-exact-psd.log relative
to the research root, and copied into the completion attack as
study/inherited-n6-exact-psd.log. The tuning values above have been corrected
to match that log; the exact final slack is unchanged.

The 2026-09-05 assembly review found that the original script printed FAIL
for negative slack without failing its exit status. The final gate now
raises SystemExit on negative slack. The completion attack's deterministic
step 5 records a regression test that failed before this fix and passed
after it. The large matrix computation was not rerun after this gate-only
change. The original result.json remains a historical run record; its
success is supported by the complete log, not merely its exit status.

## How it runs at this size

Two things make it feasible.

* **The Cholesky stays in `int64`.** A float64 shadow of every column update is computed
  alongside, and the run stops if any partial sum passes `4e18`. It did not: `max |N|` is
  `1.41e8`, and the column updates stayed inside the range.
* **The residual uses FLINT.** `N N^T` is formed once by `python-flint`'s multi-precision integer
  matrix multiplication, which is multi-modular inside and cannot overflow. That step took 254
  seconds; the whole run takes about 16 minutes, of which 6 are rebuilding the orbit structure.

## What this does not do

It certifies the main Gram matrix. The polynomial identity and the two 666 x 666 multiplier Gram
matrices were already exact in `certified-special-case-check-2`, so with this step every part of
the `n = 6` certificate is integer arithmetic, and `n = 6` now stands on the same footing as
`n = 5`.

The Lean check of `formal-check-2` still uses the floating-point route for this block, because the
exact route needs FLINT's multi-modular multiplication and about 3e11 big-integer operations,
which Lean has no equivalent for.
