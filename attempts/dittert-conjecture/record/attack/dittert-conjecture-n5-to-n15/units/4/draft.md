# A symmetry-reduced exact-certificate pipeline for invariant inequalities on the matrix simplex

## Statement

Let G_n = (S_n x S_n) x| Z_2 act on R^{n x n} by row permutations, column permutations and
transpose, and let P be a G_n-invariant polynomial that is to be shown nonnegative on the
simplex K_n = {A >= 0, sum A = n}. The pipeline below decides membership of P - lambda D in the
pairwise sum-of-squares template

    P - lambda D = sigma_0 + sum_{p = {u, v}} x_u x_v sigma_p     (degree 2D, D = ceil(deg P / 2))

with an exact rational certificate, and its cost is governed by the G_n-symmetry-adapted
block sizes rather than by the monomial count. Its instances are units 1 and 2.

**Proposition (block sizes).** In a G_n-symmetry-adapted basis the Gram matrix of sigma_0
(monomials of degree D in n^2 variables) splits into blocks of size m_rho, one per irreducible
representation rho of G_n, with sum_rho m_rho dim rho = C(n^2 + D - 1, D) and sum_rho m_rho^2 =
the number of G_n-orbits of ordered pairs of monomials. For D = 3 the largest block is 16 at
n = 5 and n = 6 (commutant dimensions 1128 and 1159); for D = 4 it is 83 at n = 7 and n = 8; for
D = 5, 424 at n = 9, 10; for D = 6, 2099 at n = 11, 12. The block sizes at fixed D stabilise in n.
(`study/gate-symmetry-blocks/blocks.py`: characters of S_n by Murnaghan-Nakayama, the
wreath-product irreps as pairs {lambda, mu} and the two extensions of lambda x lambda, the
permutation character by cycle-type counting; self-checked by orthogonality, the two sums
above, and integrality.)

## The pipeline

1. **Exact data.** P and D expanded over Q; the G_n-orbits of the degree-2D monomials by label
   propagation over five generators (one coefficient equation per orbit: 156 at n = 5, 167
   at n = 6).
2. **Numerical symmetry adaptation.** For the main Gram matrix and for each of the two
   multiplier representatives (pairs in the same row or column; pairs in different rows and
   columns, with their stabilisers), the orbits of ordered pairs of monomials, a random
   invariant matrix R1 whose eigenspaces are the (irrep, copy) pieces, a second one R2 that
   links the copies of one irrep and aligns their bases (the two-generic-element method,
   Murota-Kanno-Kojima-Kojima 2010), verified on a third; the linear map W from block
   variables to orbit coordinates.
3. **SDP.** Maximise lambda, or fix a rational lambda and maximise the smallest block
   eigenvalue off the forced null direction 1 (every Gram matrix vanishes at U_n, and z(U_n) is
   a multiple of 1, which lies in the trivial isotypic component). Sizes: 4339 block entries at
   n = 5, 4436 at n = 6; seconds with Clarabel.
4. **Exact recovery in orbit coordinates.** Numerical least-norm projection onto the exact
   equations (coefficients, M 1 = 0, symmetry m_O = m_{O^T}), rounding to a common
   denominator, exact fix of the pivot coordinates of the reduced row echelon form of the
   augmented system over Q (the correction is of the size of the rounding error, so the
   margin of step 3 survives); exact positive definiteness of the deflated multiplier
   matrices by fraction-free LU over Z.
5. **Exact positive semidefiniteness of the main matrix** through the rational isotypic
   projectors P_rho = (dim rho/|G_n|) sum_g chi_rho(g) g, computed in orbit coordinates from
   the characters; for each rho, integer columns of the scaled projector spanning its
   component (rank checked exactly), the block C^T M0 C, fraction-free LU. At n = 5: 21 blocks,
   the largest 560, 24 minutes in python-flint. At n = 6 the element enumeration of G_6
   (1036800 elements) does not fit and the step was replaced by a verified floating-point
   Cholesky factorisation; a class-based computation of the projectors is the missing piece.
6. **Independent check** by full expansion of the identity over all monomials in exact
   integer arithmetic and independent positive-definiteness tests.

## Where it stops

At n = 7 the exact expansion of the degree-8 gap polynomial in 49 variables (1.4e9 monomials)
and the pair-orbit label propagation (7.3e10 pairs) exceed memory; the orbit structure must
then be computed from canonical forms of monomials under G_n directly, and the multiplier
Gram matrices reach block size 2514. From n = 9 the main blocks (424 and up) and the
multiplier blocks (22818 and up) put the minimal-degree template out of reach.

## Applications outside the target

Any G_n-invariant polynomial inequality on K_n or on the doubly stochastic polytope of the
same degree range: the permanent inequalities of Minc's list and the Lih-Wang convexity
statement at small n are of this form. The block-size proposition and steps 1-6 apply
unchanged; only the polynomial P changes.

## Reproduction

`study/gate-symmetry-blocks/blocks.py 4 5 6 7 8 9 10 11 12`; `deterministic/numerical-
optimisation-run-3/sdp_n.py <n>` and `recover_n.py <n> <lambda> <denominator>`;
`deterministic/numerical-optimisation-run-2/recover5.py 32` for the exact isotypic check.
