# certified-special-case-check-2: the exact n = 6 certificate

Step kind: certified special-case check. Produced 2026-09-03 by
`deterministic/numerical-optimisation-run-3/recover_n.py 6 128 10000000000` (first
implementation); checked here by `check.py` (second implementation, independent code).

## The statement certified

For every A in K_6 (nonnegative 6 x 6, entry sum 6),

    phi(U_6) - phi(A) >= (128 / 46656) ||A - U_6||_F^2,

hence phi(A) <= 2 - 6!/6^6 with equality only at A = U_6: Dittert's conjecture at
n = 6, in the quantitative form with c_1 = 128/46656 = 0.002743.

## The certificate (`certificate6.json`)

lambda = 128 and three rational Gram matrices in orbit coordinates: `main` (1159
rationals, one per G_6-orbit of ordered pairs of degree-3 monomials; M0 is 8436 x 8436),
`aligned` (1426) and `generic` (1851) for the two 666 x 666 multiplier matrices, all
with denominator 10^10 (scaled denominators 10^10 and 2 x 10^10 after the exact fix).
With s = sum x, Q = 6^6 [(2 - 720/46656)(s/6)^6 - (prod r_i + prod c_j - per)] and
D = (s/6)^4 (sum x_k^2 - s^2/36), the identity in Q[x_0, ..., x_35] (4496388 monomials):

    Q - 128 D = z3^T M0 z3 + sum_{p={u,v}} x_u x_v z2(x o g_p)^T M_type(p) z2(x o g_p).

## How it was produced (recover_n.py)

As at n = 5 (certified-special-case-check-1): SDP with lambda fixed and the margin
maximised (margin 1.254); numerical least-norm projection onto the exact equations
(167 coefficient equations, M 1 = 0, symmetry; 688 independent rows for the main
matrix), rounding to denominator 10^10, exact fix of the pivot coordinates over Q;
E q = f, M 1 = 0 and M = M^T asserted exactly. Positive definiteness of the deflated
665 x 665 multiplier matrices exact (fraction-free LU over Z, flint). Positive
definiteness of the deflated 8435 x 8435 main matrix by a floating-point Cholesky
factorisation of A - alpha I with the rigorous bound of Higham Thm 10.3: smallest
eigenvalue 1.503e-4, alpha = 7.51e-5, bound 3.06e-5 (which includes a factor 10 of
safety). The exact isotypic check used at n = 5 was not run at n = 6: G_6 has
1036800 elements and the projector computation by element enumeration does not
fit in memory; a class-based computation is the open item. Wall time 37 min.

## Independent check (`check.sh` -> `check_verified.py certificate6.json`)

Same design as check 1, written for general n: Q_6 and D_6 from the definitions;
orbits by label propagation; transports by breadth-first search; the identity by
full expansion over all 4496388 monomials in exact integer arithmetic (Python
integers; the scaled entries reach 8.2e16, too large for int64 accumulation);
M 1 = 0 and symmetry exactly; positive definiteness of the deflated 665 x 665
multiplier matrices and of the deflated 8435 x 8435 main matrix by verified
floating-point Cholesky factorisations (Higham Thm 10.3, with the entry-rounding
term tripled to cover the two roundings of the integer-to-double conversion).
Result (`result.json`, 518 s): identity holds exactly; aligned alpha = 1.05e-3
against bound 4.3e-7, generic alpha = 1.09e-3 against 4.3e-7, main alpha = 7.5e-5
against 3.1e-5: all positive definite.

`check.py` is the same checker with the multiplier matrices tested by vectorised
Bareiss elimination over Z instead (Sylvester's criterion, exact); its run on this
certificate had not finished after 8 hours of big-integer arithmetic; `check_verified.py`
was adopted as the recorded second implementation and the Bareiss run was stopped when
the attack finished.
The exact positive definiteness of the multiplier matrices rests on the first
implementation (flint fraction-free LU).

Trusted base of the whole n = 6 check: Python integers, python-flint (first
implementation only), numpy/LAPACK in IEEE-754 double precision for the main
matrix's positive definiteness (both implementations). The last point makes this
step weaker than check 1, where the first implementation is exact throughout.

## What it decides

The n = 6 case of the claim as a full proof by computation whose one non-exact
step is a verified floating-point Cholesky factorisation, once `result.json` records
`pass`. No Lean check.
