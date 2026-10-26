# The coefficients in the h* basis: an exact, rank-uniform translation

Date: 2026-09-05. A derivation, with no computation in it beyond one check against a known
example.

## The identity

Let `P` be a polynomial of degree at most `d` with `P(0) = 1`, which is what the stretched
Littlewood-Richardson polynomial is with `d = dim H`. Write it in the binomial basis,

    P(t) = sum over i from 0 to d of  h_i * C(t + d - i, d),

which determines the `h_i` uniquely and gives `h_0 = P(0) = 1`. Reading off the coefficient of
`t` in each basis element:

- for `i = 0`, `C(t + d, d)` has constant term 1 and linear coefficient `H_d`, the `d`-th harmonic
  number, because none of its `d` linear factors vanishes at `t = 0`;
- for `i >= 1` one factor is `t` itself, so the constant term is 0 and the linear coefficient is
  the product of the other factors at `t = 0`, which is `(-1)^(i-1) / (i * C(d, i))`.

Hence, exactly,

    a_1  =  H_d  +  sum over i from 1 to d of  (-1)^(i-1) * h_i / (i * C(d, i)).

The magnitude `1 / (i * C(d,i))` equals `(i-1)! (d-i)! / d!`, which is unchanged when `i` is
replaced by `d + 1 - i`, while the sign flips exactly when `d` is even. So for even `d` the terms
pair,

    a_1  =  H_d  +  sum over i from 1 to d/2 of  (-1)^(i-1) * (h_i - h_{d+1-i}) / (i * C(d, i)),

and `a_1` differs from `H_d` only through the asymmetry of the `h` vector. For `d = 6`, the
dimension of a full-dimensional five-part hive polytope,

    a_1  =  49/20  +  (h_1 - h_6)/6  -  (h_2 - h_5)/30  +  (h_3 - h_4)/60.

The same computation gives every other coefficient as a fixed linear functional of the same
vector, so the translation covers the whole statement and not only `a_1`.

## Check against a known example

Reeve's tetrahedron with vertices at the origin, `(1,0,0)`, `(0,1,0)` and `(1,1,r)` has `d = 3`
and `h = (1, 0, r-1, 0)`. The identity gives `a_1 = 11/6 + 0 - (r-1)/6 + 0 = (12 - r)/6`, negative
exactly for `r > 12`, which is the known threshold. The identity is therefore not merely formal
bookkeeping; it reproduces the standard example of a negative linear Ehrhart coefficient.

## What the translation buys, and what it does not

It buys the language the subject's inequalities are stated in. Stanley's nonnegativity, Hibi's
lower bound, monotonicity and the unimodality results are all statements about `h`, and the survey
literature found in `reduce-and-translate.md` is organised around them.

It does not buy the conjecture. Ehrhart positivity is false in general, and the identity shows
exactly how: a large `h_2` alone drives `a_1` negative, and Reeve's tetrahedron is that case. So a
proof through this route has to say what the hive polytopes' `h` vectors satisfy that a general
polytope's do not.

Two cautions the record must carry. First, the hive polytopes are rational, not lattice, so `h`
here is a basis change of a polynomial and not the `h*` vector of a lattice polytope; the classical
inequalities do not apply to it without an argument, and nothing here supplies one. Second, the
identity is exact and adds no evidence for or against the conjecture by itself.
