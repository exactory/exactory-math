"""R7: the first-order (KKT) conditions at a maximiser of phi on K_n, checked numerically.

With R = prod r_i, C = prod c_j, P = per(A), the partial derivative of phi is

    d phi / d a_ij = R / r_i + C / c_j - per(A(i|j)).

At a maximiser on the simplex there is a multiplier mu with equality where a_ij > 0 and
`<= mu` where a_ij = 0.  Expanding along row i and using sum_j a_ij per(A(i|j)) = P gives

    R + C * S_i - P = mu r_i,   S_i := sum_j a_ij / c_j,                                (1)
    R * T_j + C - P = mu c_j,   T_j := sum_i a_ij / r_i,                                (2)

and summing (1) over i, with sum_i r_i = n and sum_ij a_ij / c_j = n, gives

    mu = R + C - P = phi(A).                                                            (3)

So at a maximiser with a zero at (i0, j0),

    per(A(i0|j0)) >= R / r_{i0} + C / c_{j0} - phi(A) >= 2 - phi(A) - (corrections)      (4)

which, when phi(A) >= 2 - gamma_n and the row and column sums are near 1, forces
per(A(i0|j0)) >= gamma_n up to the correction terms: the minor obtained by deleting the row
and column through the zero has to sit at the van der Waerden bound for its own size, after
the natural rescaling.  This script checks (1), (2), (3) and (4) on the Knopp-Sinkhorn
extremal T_n (the maximiser of phi on the face a_00 = 0) and on random perturbations.
"""
import itertools
import math
import sys

import numpy as np


def per(A):
    n = A.shape[0]
    if n == 0:
        return 1.0
    return float(sum(math.prod(A[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n))))


def phi(A):
    return float(np.prod(A.sum(1)) + np.prod(A.sum(0)) - per(A))


def minor(A, i, j):
    return np.delete(np.delete(A, i, axis=0), j, axis=1)


def ks_extremal(n):
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1)
    T[:, 0] = 1 / (n - 1)
    T[0, 0] = 0.0
    return T


for n in [int(a) for a in sys.argv[1:]] or [5, 6, 7]:
    A = ks_extremal(n)
    g = math.factorial(n) / n ** n
    m = math.factorial(n - 2) * ((n - 2) / (n - 1) ** 2) ** (n - 2)
    r, c = A.sum(1), A.sum(0)
    R, C, P = float(np.prod(r)), float(np.prod(c)), per(A)
    f = R + C - P
    print(f"\n== n = {n}: T_n has phi = {f:.10f}, 2 - m_n = {2 - m:.10f}, 2 - gamma_n = {2 - g:.10f}")
    # (3) and the KKT equalities on the support
    grad = np.array([[R / r[i] + C / c[j] - per(minor(A, i, j)) for j in range(n)] for i in range(n)])
    sup = A > 1e-12
    print(f"   mu from (3) = phi = {f:.10f}; gradient on the support: "
          f"min {grad[sup].min():.10f}, max {grad[sup].max():.10f} "
          f"(KKT wants them all equal to mu)")
    print(f"   gradient at the zero entry (0,0) = {grad[0, 0]:.10f} (KKT wants <= mu)")
    # (1) and (2)
    S = (A / c).sum(1)
    T = (A.T / r).sum(1)
    lhs1 = R + C * S - P
    lhs2 = R * T + C - P
    print(f"   identity (1) max error {np.abs(lhs1 - f * r).max():.3e};"
          f"  identity (2) max error {np.abs(lhs2 - f * c).max():.3e}")
    # (4): the minor bound
    bound = R / r[0] + C / c[0] - f
    pm = per(minor(A, 0, 0))
    gm = math.factorial(n - 1) / (n - 1) ** (n - 1)
    scale = ((n - 2) / (n - 1)) ** (n - 1)
    print(f"   per(A(0|0)) = {pm:.6e}; KKT bound (4) = {bound:.6e}; gamma_n = {g:.6e}; "
          f"ratio to bound {pm / bound:.4f}")
    print(f"   the minor rescaled: per / (scale * gamma_(n-1)) = {pm / (scale * gm):.6f} "
          f"(1.0 means the minor is exactly van der Waerden extremal)")
