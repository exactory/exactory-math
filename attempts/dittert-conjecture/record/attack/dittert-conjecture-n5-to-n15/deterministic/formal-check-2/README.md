# formal-check-2: the n = 5 and n = 6 certificates, checked in Lean 4

Step kind: formal check. Theorem: `certOK56_true` in `Theorem56.lean`. Toolchain
`leanprover/lean4:v4.33.1`.

## What the theorem says

`certOK56 () = true`, where `certOK56` is the conjunction of the two certificate checks. For each
of `n = 5` and `n = 6` the check

1. rebuilds the symmetry-adapted monomial orbits from the group generators of `sdp_n.py`, and
   requires their count to equal the number of values the certificate carries (1128, 1400, 1811 at
   `n = 5`; 1159, 1426, 1851 at `n = 6`, each matching the Python side);
2. assembles every Gram matrix from those orbits and the rational data, and requires it to be
   symmetric with zero row sums;
3. requires every Gram matrix to be positive semidefinite;
4. expands the sum-of-squares identity against the Dittert polynomial over every monomial of
   degree 6 (593775 at `n = 5`, 4496388 at `n = 6`) and requires the difference to be zero
   coefficient by coefficient.

Only the group generators and the orbit values are data. The monomial indexing, the orbit
structure, the Gram matrices and the Cholesky factors are all recomputed inside Lean.

## No Mathlib

This project depends on nothing but core Lean. There is no `Real` anywhere in it: every step is a
decidable computation over `Int`, `Nat` and `Float`. That is a statement about the residue, not
about the tooling.

## The two positive-semidefiniteness routes

At `n = 5`, and for the two 666 x 666 multiplier Grams at `n = 6`, the route is **exact**: an
integer Cholesky factor `N` of `F^2 (A + d J) - delta I` is computed with truncating division, and
the certificate is that the residual `F^2 (A + d J) - N N^T` is diagonally dominant with
non-negative diagonal. Then it is positive semidefinite by Gershgorin, `N N^T` is positive
semidefinite, and with `A . 1 = 0` the conclusion follows over the integers.

For the 8436 x 8436 main Gram at `n = 6` the route is a **floating-point Cholesky with Higham's
rigorous backward-error bound** (Higham, *Accuracy and Stability of Numerical Algorithms*, 2nd
ed., Thm 10.3), the same criterion the second implementation of the n = 6 certificate already
uses. It is rigorous given IEEE-754 semantics; it is not integer arithmetic. Measured in Lean:
sum of squares of the factor 3269833.159583, bound 3.06e-5, alpha 0.0625, margin 2040 times. Both
numbers agree with the Python side to every printed digit.

The exact route is out of reach at that dimension: about 3e11 big-integer operations and three
71-million-entry integer arrays.

## Why `A + d J` rather than deleting a row and column

`A . 1 = 0`, so `lambda_min(A + d J) = min(lambda_2(A), d * dim)`, while deleting a row costs a
factor of `dim` in conditioning. At `n = 6` that is the difference between lambda_2 = 1.5e-4
(deflated, margin 2.45 times) and lambda_2 = 0.156 (this route, margin 2040 times).

## `precompileModules`

`lakefile.toml` sets it on the `Cert` library. It is what makes `native_decide` run the checks as
compiled code: without it Lean interprets every imported definition, which measured three times
slower on the n = 5 check (100 minutes and still running, against 47 minutes compiled).

## What the result is, and is not

`native_decide`, so the theorem rests on the axiom `native_decide` introduces in addition to
Lean's standard `propext`, `Classical.choice` and `Quot.sound`. `result.json` records the list
the harness read. It is computational evidence with a machine-checked structure, not a
kernel-checked proof, and the n = 6 main block is floating-point on top of that.

The step certifies the arithmetic residue. The deduction from that residue to Dittert's
conjecture at n = 5 and n = 6 is the argument in the two certified-special-case-check steps, and
it is not formalised: the sibling attack's Lean study lists the six pieces of library Mathlib
would need first.
