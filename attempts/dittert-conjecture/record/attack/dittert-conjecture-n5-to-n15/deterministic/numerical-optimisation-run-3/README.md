# numerical-optimisation-run-3: the n = 6 symmetry-reduced SOS relaxation

Step kind: numerical optimisation run (evidence, not a proof). Run 2026-09-03 under the
walk's reduce-to-a-finite-computation step 4 (settle the instances), at n = 6.

## Ansatz (`sdp_n.py`, the general-n version of run 2)

Homogeneous degree-6 identity on R^36 (entries of a 6 x 6 matrix, row-major):

    Q_6 - lambda D_6 = sigma_0 + sum_{p = {u, v}} x_u x_v sigma_p,

Q_6 = 6^6 [ (2 - 720/46656) (s/6)^6 - (prod_i r_i + prod_j c_j - per) ], D_6 = (s/6)^4
(sum_k x_k^2 - s^2/36), s = sum x; on K_6 (s = 6) these are 6^6 (phi(U_6) - phi(A)) and
||A - U_6||_F^2. sigma_0 is a Gram form in the 8436 monomials of degree 3, each
sigma_p a Gram form in the 666 monomials of degree 2, p over the 630 unordered pairs
of distinct entries. Feasible lambda > 0 proves phi(U_6) - phi(A) >= (lambda/46656)
||A - U_6||_F^2 on K_6.

## Symmetry reduction

G_6 = (S_6 x S_6) x| Z_2, order 1036800. The 4496388 degree-6 monomials fall into 167
orbits (167 equations). The main Gram matrix has 1159 pair orbits (matching the
character computation in `study/gate-symmetry-blocks`), block-diagonalised
numerically into 16(x25), 15(x10), 14(x90), 10(x100), 9(x25), 8(x18), 7(x1), 6(x180),
6(x81), 5(x100), 5(x20), 4(x50), 3(x160), 3(x10), 3(x1), 2(x320), 2(x288), 2(x90), 2(x81),
1(x256), 1(x200), 1(x100), 1(x100), 1(x100), 1(x32), 1(x25). Two pair orbits (aligned:
1426 pair orbits under its stabiliser, blocks up to 21; generic: 1851, blocks up to
22). Total 4436 block entries.

The run itself is verified against n = 5: `sdp_n.py 5` reproduces lambda* = 40.11560
of run 2 to every printed digit.

## Result (`sdp6.log`)

Clarabel: status `optimal_inaccurate`,

    lambda* = 174.8926...,   kappa = lambda*/46656 = 0.0037486,

maximum equation residual 8.7e-7, minimum block eigenvalue -1.3e-4; 460 s in total, of
which 307 s expanding Q_6 exactly and 100 s in the 8436 x 8436 block diagonalisation.
So the minimal-degree pairwise template admits a positive stability parameter at
n = 6 as well; the stability constants so far are kappa_4 = 1/52 = 0.0192 (proved),
kappa_5 ~ 0.0128 (exact recovery at 32/3125 = 0.0102 in progress), kappa_6 ~ 0.0037.

## Independent check

`check.sh` runs `check.py`: it rebuilds the full Gram matrices from the saved blocks
and bases (`sdp6-solution.npz`), evaluates the certificate by direct polynomial
evaluation with its own breadth-first-search transports, and Q_6 - lambda D_6 from the
definitions (row products, column products, the permanent as a sum over the 720
permutations) at 200 random points of K_6; it requires relative agreement 1e-4 and
block eigenvalues above -1e-3. Trusted base: numpy in double precision.

## What it decides

Nothing exactly. It settles that the n = 6 residue of route B has the same shape and
size as the n = 5 one, so the exact recovery pipeline of run 2 applies unchanged
(with 8436 x 8436 main Gram matrix and blocks up to 14 x 90 = 1260 in the isotypic
check).
