# certified-special-case-check-1: the exact n = 5 certificate

Step kind: certified special-case check. Produced 2026-09-03 by
`deterministic/numerical-optimisation-run-2/recover5.py 32` (first implementation,
exact); checked here by `check.py` (second implementation, independent code).

## The statement certified

For every A in K_5 (nonnegative 5 x 5, entry sum 5),

    phi(U_5) - phi(A) >= (32 / 3125) ||A - U_5||_F^2,

hence phi(A) <= 2 - 5!/5^5 with equality only at A = U_5: Dittert's conjecture at
n = 5, in the quantitative form of arXiv:2607.29191 with c_1 = 32/3125 = 0.01024.

## The certificate (`certificate5.json`, 114 kB)

lambda = 32 and three rational Gram matrices given in orbit coordinates:

- `main`: 1128 rationals with denominator 10^10 (after the exact pivot fix, 12 digits),
  one per G_5-orbit of ordered pairs of degree-3 monomials; M0 is the 2925 x 2925
  matrix with M0[a, b] = main[orbit(a, b)].
- `aligned`, `generic`: 1400 and 1811 rationals, one per orbit of the stabiliser of the
  pair {x_0, x_1} (resp. {x_0, x_6}) on ordered pairs of degree-2 monomials; M_al and
  M_ge are the 325 x 325 matrices they define; the Gram matrix of the pair p is the
  transport of its type's matrix by any group element g_p with g_p(rep) = p.

The identity is, with s = sum x, Q = 5^5 [(2 - 120/3125)(s/5)^6 - (prod r_i + prod c_j - per)(s/5)]
and D = (s/5)^4 (sum x_k^2 - s^2/25):

    Q - 32 D = z3^T M0 z3 + sum_{p={u,v}} x_u x_v z2(x o g_p)^T M_type(p) z2(x o g_p),

an identity in Q[x_0, ..., x_24] (593775 monomials of degree 6), with M0, M_al, M_ge
positive semidefinite. On K_5 every term on the right is nonnegative and D = ||A - U_5||_F^2.

## How it was produced (recover5.py)

Symmetry-reduced SDP with lambda fixed to 32 and the margin maximised (Clarabel:
margin 0.343 off the forced null vector 1); orbit coordinates; numerical least-norm
projection onto the exact equations, rounding to denominator 10^10, exact fix of the
pivot coordinates of the reduced row echelon form of [E | f] over Q (E: the 156
coefficient equations, the row-sum equations M 1 = 0, and the symmetry equations
m_O = m_{O^T}; 667 independent rows for the main block). Exact checks in the first
implementation: E q = f over Q; M 1 = 0 and M = M^T for all three matrices;
positive definiteness of the deflated 324 x 324 multiplier matrices by fraction-free
LU over Z (flint fflu, no pivoting, all pivots positive); positive semidefiniteness of
M0 through the 21 rational isotypic projectors of G_5 (characters of S_5 by
Murnaghan-Nakayama, wreath-product extension), each restricted block N_rho = C^T M0 C
(C integer columns of the scaled projector spanning the component, rank checked
exactly) positive definite by fraction-free LU, the trivial component deflated by the
known null vector 1. Blocks: 120, 80, 60, 10, 7 (deflated to 6), 3, 560, 480, 120, 256,
144, 360, 100, 150, 50, 120, 48, 180, 36, 25, 16; all positive definite. Wall time 24 min,
almost all in the flint products for the four largest blocks.

## Independent check (`check.sh` -> `check.py`)

Recomputes from the definitions with its own code: Q and D by expanding row
products, column products and the permanent; the orbit structure by label
propagation over the group generators; the transports by breadth-first search; the
identity by a full expansion over all 593775 monomials in exact integer arithmetic
(common scale L = lcm of the three denominators); M 1 = 0 and symmetry exactly;
positive definiteness of the deflated 324 x 324 multiplier matrices by Bareiss
fraction-free elimination over Z (Sylvester's criterion); and positive definiteness
of the deflated 2924 x 2924 main matrix by a floating-point Cholesky factorisation of
A - alpha I with the rigorous bound of Higham, Thm 10.3 (alpha above ten times the
sum of the backward-error term gamma_{n+1} ||L||_F^2 and the entry-rounding terms).
The last item is the one step of the second implementation that is verified in
IEEE-754 arithmetic rather than exact; the first implementation checks it exactly.

Trusted base: Python integers and fractions, python-flint (fflu, rref, rank) in the
first implementation; Python integers, numpy/LAPACK double precision in the second.

## What it decides

The n = 5 case of the claim, as a full proof by computation, once `result.json`
records `pass`. The formal (Lean 4) check of this certificate is not done: the
certificate has 4339 rational coordinates and the positive-semidefiniteness of a
2925 x 2925 matrix, so a kernel check needs either the isotypic reduction inside
Lean or a native evaluation; both are open work.
