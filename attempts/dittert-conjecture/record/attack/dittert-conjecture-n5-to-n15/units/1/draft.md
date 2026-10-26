# Dittert's conjecture in dimension 5 via a symmetry-reduced exact sum-of-squares certificate

## Statement

**Theorem 1.** For every nonnegative real 5 x 5 matrix A whose entries sum to 5,

    phi(U_5) - phi(A) >= (32/3125) ||A - U_5||_F^2,

where phi(A) = prod_i r_i(A) + prod_j c_j(A) - per(A), r_i and c_j are the row and column
sums, and U_5 is the matrix with every entry 1/5. Consequently phi(A) <= 2 - 5!/5^5 = 2 - 120/3125 for every such A, with equality if and only if A = U_5: Dittert's conjecture
(Minc, Theory of permanents 1978-1981, Linear Multilinear Algebra 12 (1983), Conjecture 28)
holds at n = 5.

The inequality has the quantitative form used at n = 4 by Li, Xiong and Yang
(arXiv:2607.29191, where c_1 = 1/52); here c_1 = 32/3125 = 0.01024. The cases n = 2, 3 are
Sinkhorn (Linear Multilinear Algebra 16 (1984)) and Hwang (Linear Algebra Appl. 95 (1987),
doi:10.1016/0024-3795(87)90032-2); n = 16 and n >= 17 are Kafidov (arXiv:2607.19439) and Pang
(arXiv:2606.01531). No result for 5 <= n <= 15 was in print on 2026-09-03 (novelty.md).

## The certificate

Write x_0, ..., x_24 for the entries of A (row-major), s = sum x, and

    Q(x) = 5^5 [ (2 - 120/3125) (s/5)^6 - (prod_i r_i + prod_j c_j - per(A)) (s/5) ],
    D(x) = (s/5)^4 ( sum_k x_k^2 - s^2/25 ),

both homogeneous of degree 6; on the simplex s = 5 they equal 5^5 (phi(U_5) - phi(A)) and
||A - U_5||_F^2. The certificate (`deterministic/certified-special-case-check-1/certificate5.json`)
is the polynomial identity in Q[x_0, ..., x_24]

    Q - 32 D = z3^T M0 z3 + sum_{p = {u, v}} x_u x_v z2(x o g_p)^T M_type(p) z2(x o g_p),   (1)

where z3 is the vector of the 2925 monomials of degree 3, z2 the vector of the 325 monomials of
degree 2, p runs over the 300 unordered pairs of distinct entries, g_p is a group element of
G_5 = (S_5 x S_5) x| Z_2 (row permutations, column permutations, transpose) carrying a fixed
representative pair to p, and M0, M_aligned, M_generic are rational positive semidefinite
matrices (2925 x 2925 and two 325 x 325), given by 1128, 1400 and 1811 rational numbers
respectively, one per orbit of ordered pairs of monomials under G_5 (for M0) or under the
stabiliser of the representative pair (for the multipliers). Every term on the right of (1)
is nonnegative on the simplex and D > 0 off U_5, which proves Theorem 1.

## Verification

Two independent implementations verify (1) and the positive semidefiniteness.

1. `deterministic/numerical-optimisation-run-2/recover5.py` (which also produced the
   certificate): the coefficient equations (one per G_5-orbit of degree-6 monomials, 156 in
   all), M 1 = 0 and M = M^T are checked exactly over Q; the deflated 324 x 324 multiplier
   matrices are positive definite by fraction-free LU over Z (flint); M0 is positive
   semidefinite exactly: its restrictions to the 21 isotypic components of G_5 (rational
   projectors from the characters of S_5 and the wreath-product extension; blocks of sizes
   560, 480, 360, 256, 180, 150, 144, 120, 120, 120, 100, 80, 60, 50, 48, 36, 25, 16, 10, 6, 3)
   are positive definite by fraction-free LU over Z, the trivial component being deflated by
   the known null vector 1 (z3(U_5) is a multiple of 1).
2. `deterministic/certified-special-case-check-1/check.py`: the identity (1) is expanded over
   all 593775 monomials in exact integer arithmetic and compared with Q - 32 D computed from
   the definitions; M 1 = 0 and symmetry are checked exactly; the deflated multiplier matrices
   are positive definite by Bareiss elimination over Z (Sylvester's criterion); the deflated
   2924 x 2924 main matrix is positive definite by a floating-point Cholesky factorisation of
   A - alpha I with alpha = 5.87e-5 against the rigorous bound 5.33e-7 (Higham, Accuracy and
   Stability of Numerical Algorithms, 2nd ed., Thm 10.3). `result.json` records `pass`.

The trusted base is Python integer arithmetic and python-flint in the first implementation;
the second adds IEEE-754 double precision and LAPACK for one step, which the first checks
exactly. No Lean 4 check has been done; the theorem is stated in Lean
(`deterministic/formal-check-1/Main.lean`, `dittert_five_stability`, proof `sorry`).

## How the certificate was found

The symmetry-reduced pipeline of unit 4: the numerical optimum of the template is lambda* =
40.1156 (`deterministic/numerical-optimisation-run-2`, Clarabel, 4339 block entries); lambda
was fixed at 32 and the smallest block eigenvalue off the null vector maximised (0.343); the
orbit coordinates were projected numerically onto the exact equations, rounded to
denominator 10^10, and the pivot coordinates of the reduced row echelon form of the equations
were fixed exactly. The constant 32/3125 is below the numerical optimum 40.1/3125 by choice
(rounding room), which is the only quality given up.

## Reproduction

`poly.py` (exact Q and D and the monomial orbits), `sdpcore5.py`, `sdp5.py`, `recover5.py 32`
in `deterministic/numerical-optimisation-run-2`, then `check.sh` in
`deterministic/certified-special-case-check-1`. Python 3.13, numpy, scipy, cvxpy 1.7 with
Clarabel, python-flint 0.9. Wall time: 24 minutes for the recovery, 25 minutes for the check.
