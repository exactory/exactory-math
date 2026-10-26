# numerical-optimisation-run-2: the n = 5 symmetry-reduced SOS relaxation

Step kind: numerical optimisation run (evidence, not a proof). Run 2026-09-03 under
move 2 (predict-the-value-and-test-it-numerically) of the walk; it is the
optimisation handed on by move 1, route B.

## Ansatz

Homogeneous degree-6 identity on R^25 (entries of a 5 x 5 matrix, row-major):

    Q - lambda D = sigma_0 + sum_{p = {u, v}} x_u x_v sigma_p,

Q = 5^5 [ (2 - 120/3125) (s/5)^6 - (prod_i r_i + prod_j c_j - per) (s/5) ], s = sum x,
D = sum_k (x_k - s/25)^2 (s/5)^4, so that on K_5 (s = 5): Q = 5^5 (phi(U_5) - phi(A))
and D = ||A - U_5||_F^2. sigma_0 is a Gram form in the 2925 monomials of degree 3;
each sigma_p is a Gram form in the 325 monomials of degree 2; p runs over the 300
unordered pairs of distinct entries. Every term is nonnegative on K_5, so any
feasible lambda > 0 gives phi(U_5) - phi(A) >= (lambda/3125) ||A - U_5||_F^2 on K_5.

## Symmetry reduction (`poly.py`, `sdp5.py`)

G_5 = (S_5 x S_5) x| Z_2 (row permutations, column permutations, transpose), order
28800. Q and D are G_5-invariant (checked exactly on every orbit), so the
certificate is taken G_5-invariant. The 593775 degree-6 monomials fall into 156
orbits (label propagation over five generators), so there are 156 coefficient
equations. The main Gram matrix is G_5-invariant: 1128 pair orbits (matching the
character computation in `study/gate-symmetry-blocks`), block-diagonalised
numerically by the two-generic-element method into blocks 16(x16), 15(x8),
14(x40), 10(x48), 9(x16), 8(x10), 7(x1), 6(x60), 6(x25), 5(x36), 5(x12), 3(x40),
3(x1), 2(x60), 2(x50), 2(x25), 1(x48), 1(x36), 1(x25), 1(x16), 1(x10) (block size m,
and the number d of identical copies). The 300 pairs form two G_5-orbits: aligned
(same row or column, 100 pairs, stabiliser of order 288) and generic (different
rows and columns, 200 pairs, stabiliser of order 144); one Gram matrix per orbit,
invariant under the stabiliser, transported to the other pairs by group elements
found by breadth-first search. Their blocks: aligned 21, 17, 14, 13, 10, 10, 5, 5,
5, 3, 2, ... (1400 pair orbits); generic 22, 21, 16, 12, 12, 12, 11, 5, 5, 4, ...
(1811 pair orbits). Total 4339 block entries, 156 equations.

## Result

Clarabel (double precision): status `optimal_inaccurate`,

    lambda* = 40.1156...,   kappa = lambda*/3125 = 0.012837,

maximum equation residual 6.0e-7, minimum block eigenvalue -1.3e-5 (solve time
4 s). So a degree-6 pairwise certificate exists numerically at n = 5, with a
stability constant of about 0.0128 (the proved value at n = 4 is 1/52 = 0.0192).
The saved solution (`sdp5-solution.npz`) holds the blocks and the numerical bases.

Prediction tested: whether the minimal-degree pairwise template, which needed no
higher degree at n = 4, still admits a positive lambda at n = 5. It does.

## Independent check

`check.sh` runs `check.py`: it rebuilds the full Gram matrices from the saved
blocks and bases, evaluates the certificate side by direct polynomial evaluation
(monomial vectors, transports found by its own breadth-first search) and Q - lambda D
from the definitions (row products, column products, the permanent as a sum over
permutations) at 200 random points of K_5, and requires relative agreement 1e-4
and block eigenvalues above -1e-4. No coefficient matching or orbit code is
shared with `sdp5.py`. Trusted base: numpy in double precision.

## What it decides

Nothing exactly: the Gram matrices are floating point and the bases are numerical
eigenvectors. It fixes the template, the block structure, and the target value for
the exact recovery (a rational lambda below 40, for instance 32 = 2^5 or 39), which
is the next step on route B.
