# What the h vector is, algebraically, and what that buys

Date: 2026-09-05. A derivation, with no computation in it.

## The Hilbert series

Let `H` be the hive polytope of a triple, `D` the number of interior entries, and `d = dim H`.
Let `C` be the cone over `H` at height one in `R^(D+1)` and `S = C ∩ Z^(D+1)` the set of lattice
points in it, graded by the height. The degree-`t` part of `S` is `tH ∩ Z^D`, so its Hilbert
function is the stretched polynomial `P`.

Summing the binomial basis, `sum over t of C(t + d - i, d) z^t = z^i / (1-z)^(d+1)`, because
`C(t+d-i, d)` vanishes for `t < i` and the substitution `t = i + s` turns it into `C(s+d, d)`.
Therefore the expansion of move 3,

    P(t) = sum over i of h_i * C(t + d - i, d),

is exactly the statement

    sum over t of P(t) z^t  =  h(z) / (1-z)^(d+1),   h(z) = sum over i of h_i z^i.

So the `h` vector of move 3 is the numerator of the Hilbert series of the semigroup ring of `S`,
and it is an algebraic invariant of that ring rather than a bookkeeping device.

## What follows

`S` is the full set of lattice points of a pointed rational cone, so it is a saturated, hence
normal, affine semigroup, and by Hochster's theorem its semigroup ring is Cohen-Macaulay. For a
Cohen-Macaulay graded ring generated in degree one, the numerator of the Hilbert series over
`(1-z)^(dimension)` is the Hilbert function of an Artinian reduction and therefore has nonnegative
coefficients. Generation in degree one is exactly the integer decomposition property of `H`: every
lattice point of `tH` a sum of `t` lattice points of `H`.

**So: if the hive polytopes have the integer decomposition property, their `h` vectors are
nonnegative.** That is a known kind of question about a well-studied family, and it is a cleaner
target than anything about the individual coefficients.

## What does not follow

Nonnegativity of `h` does not give the conjecture, and the counterexample is again Reeve's
tetrahedron: its `h` is `(1, 0, r-1, 0)`, nonnegative for every `r`, while its linear coefficient
`(12-r)/6` is negative for `r > 12`. So `h >= 0` is a floor, not the statement, and the target
remains the asymmetry inequality of move 3, that the even-indexed part of `sum h_i / (i C(d,i))`
does not exceed the harmonic number plus the odd-indexed part.

The direction is also not reversible: Reeve's tetrahedron has nonnegative `h` and is not integrally
closed, so the integer decomposition property is sufficient for `h >= 0` and not necessary.

## What this changes for the attack

Two things. The `h` vector is now attached to a ring, which is the setting in which the
inequalities of the subject are proved, rather than to a change of basis. And the first
measurable question is sharp: do the hive polytopes the project holds have nonnegative `h`, and if
so, is that because they are integrally closed. Both are questions about data the project already
has, and any run for them is gated by an admission record and an independent review.
