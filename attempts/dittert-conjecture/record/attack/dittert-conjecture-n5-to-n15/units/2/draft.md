# Dittert's conjecture in dimension 6 via a symmetry-reduced rational sum-of-squares certificate

## Statement

**Theorem 2.** For every nonnegative real 6 x 6 matrix A whose entries sum to 6,

    phi(U_6) - phi(A) >= (128/46656) ||A - U_6||_F^2,

with phi and U_6 as in unit 1. Consequently phi(A) <= 2 - 6!/6^6 = 2 - 720/46656 with equality
if and only if A = U_6: Dittert's conjecture holds at n = 6. The constant is c_1 = 128/46656 =
0.002743 (n = 4: 1/52, arXiv:2607.29191; n = 5: 32/3125, unit 1).

**What is verified exactly and what is verified in floating point.** The certificate below
is a rational identity with rational Gram matrices. The identity, M 1 = 0, symmetry, and the
positive definiteness of the two deflated 665 x 665 multiplier matrices are checked in exact
arithmetic. The positive definiteness of the deflated 8435 x 8435 main matrix is verified by
a floating-point Cholesky factorisation with a rigorous a posteriori bound (Higham, Accuracy
and Stability of Numerical Algorithms, 2nd ed., Thm 10.3): the factorisation of A - alpha I
succeeds with alpha = 7.51e-5 while the bound on the backward error and the entry rounding
is 3.06e-5, so A is positive definite in every model in which IEEE-754 arithmetic and the
LAPACK Cholesky routine satisfy the standard error analysis. This is the base theory the
theorem is stated relative to; an exact check of that one matrix through the isotypic
projectors of G_6 (as done at n = 5) is the open item.

## The certificate

With x_0, ..., x_35 the entries, s = sum x,

    Q(x) = 6^6 [ (2 - 720/46656) (s/6)^6 - (prod_i r_i + prod_j c_j - per(A)) ],
    D(x) = (s/6)^4 ( sum_k x_k^2 - s^2/36 ),

the certificate (`deterministic/certified-special-case-check-2/certificate6.json`) is the identity

    Q - 128 D = z3^T M0 z3 + sum_{p = {u, v}} x_u x_v z2(x o g_p)^T M_type(p) z2(x o g_p)

in Q[x_0, ..., x_35] (4496388 monomials of degree 6), with z3 the 8436 monomials of degree 3, z2
the 666 of degree 2, p over the 630 pairs of distinct entries, and rational positive
semidefinite M0 (8436 x 8436, 1159 orbit coordinates), M_aligned (666 x 666, 1426), M_generic
(666 x 666, 1851), all with denominator 10^10.

## Verification

1. `deterministic/numerical-optimisation-run-3/recover_n.py 6 128 10000000000`: the 167
   coefficient equations, M 1 = 0 and symmetry exactly over Q; the deflated multiplier
   matrices positive definite by fraction-free LU over Z (flint); the main matrix by the
   verified Cholesky above (smallest eigenvalue 1.50e-4).
2. `deterministic/certified-special-case-check-2/check_verified.py`: the identity expanded over
   all 4496388 monomials in exact integer arithmetic against Q - 128 D from the definitions;
   M 1 = 0 and symmetry exactly; all three deflated matrices by verified Cholesky (multipliers:
   alpha 1.05e-3 and 1.09e-3 against bounds 4.3e-7; main: as above). `result.json`: `pass`, 518 s.
   (A Bareiss-elimination variant of the multiplier check, `check.py`, exact over Z, was left
   running after 8 hours.)

## How it was found

Unit 4's pipeline at n = 6: numerical optimum lambda* = 174.89 (`numerical-optimisation-run-3`,
main Gram blocks at most 16, multiplier blocks at most 22, 4436 block entries, 460 s of which
307 s expand Q exactly); lambda fixed at 128, margin 1.25; projection, rounding to 10^10,
exact pivot fix (688 independent equations).

## Reproduction

`sdp_n.py 6`, `recover_n.py 6 128 10000000000`, then `check.sh` in
`certified-special-case-check-2`. Peak memory 17 GB for the checker.
