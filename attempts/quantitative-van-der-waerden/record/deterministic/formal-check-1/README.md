# formal-check-1: the n = 3 sharp case in Lean 4, not run

Step kind: formal check. Theorem: `qvdw_three` in `QvdW3b.lean` (and the first variant
`QvdW3.lean`). Toolchain `leanprover/lean4:v4.33.1`, Mathlib from the sibling attack's build,
shared through `.lake/packages`.

## The statement encoded

For real `a, ..., i` with all nine non-negative and the six margin equations,

    (2/9) (1 + sum (entry - 1/3)^2 / 4) <= a e i + b f g + c d h + a f h + b d i + c e g,

which is unit 3 of this attack on the nine entries. The proof encodes the argument of
`study/route-interpolation.md`, Theorem 2: substitute the margin equations, then `nlinarith`
closes the polynomial inequality from three instances of Schur's inequality, `schur_three`, which
is proved by splitting on the order of its three variables.

## Status: not run

The build did not complete on this machine on 2026-09-04. `lake build` sat for 16 minutes with
10 seconds of CPU and no output; `lean` invoked directly with the Mathlib search path sat for 28
minutes at about 1 percent CPU. The cause is the machine, not the file:

    20:21  up 74 days, 18:25, 1 user, load averages: 174.96 144.16 137.57

with under 70 MB of free memory, from other sessions' processes. This is the failure signal of
the formalising strategy in its third form, infrastructure rather than mathematics, and the step
is recorded as not run: no `result.json` is written, and unit 3 rests on the exact rational check
of the identity and on Schur's inequality, not on this file.

## How to run it

From this directory, with the load gone:

    LEAN_PATH=<the sibling's .lake/packages/*/.lake/build/lib/lean joined by colons> lean QvdW3b.lean

The expected output is the axiom list `[propext, Classical.choice, Quot.sound]`: nothing here
needs `native_decide`, so a successful run is a kernel-checked proof. If `schur_three` fails in
some branch of the case split, the hints in the `first` alternatives are the products the
standard proof uses and can be extended with the two missing ones for that order.
