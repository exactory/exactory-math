"""The exact local stability constant of the van der Waerden inequality.

The natural strengthening of everything in this attack is

    S(n, c):  per(B) >= gamma_n ( 1 + c ||B - J_n/n||_F^2 )   for every B in Omega_n.

Its local constant is computable in closed form.  The permanent is multilinear, so with
A = J_n/n + E and E having zero row and column sums,

    per(A) = gamma_n + sum_ij E_ij per(A(i|j))|_{J/n}
             + (1/2) sum_{i != k, j != l} E_ij E_kl per(A(ik|jl))|_{J/n} + O(E^3).

The first-order term vanishes because per(A(i|j)) is the constant (n-1)!/n^(n-1) at J/n and
sum E = 0.  In the second-order term per(A(ik|jl)) is the constant (n-2)!/n^(n-2), and

    sum_{i != k, j != l} E_ij E_kl = (sum E)^2 - sum_i (row sum)^2 - sum_j (col sum)^2
                                     + sum_ij E_ij^2 = ||E||_F^2,

so   per(J/n + E) = gamma_n ( 1 + (n / (2(n-1))) ||E||_F^2 ) + O(E^3),

and the local constant is n/(2(n-1)), which tends to 1/2.  This script checks that against
direct evaluation, and then checks the consequence: at the Knopp-Sinkhorn extremal, which has
||T_n - J/n||_F^2 = 1/(n-1)^2 exactly, the formula predicts per = gamma_n (1 + n/(2(n-1)^3)),
against the true m_n; so S(n, c) with the true constant says no more than Knopp-Sinkhorn does.
"""
import itertools
import math

import numpy as np


def per(A):
    n = A.shape[0]
    return float(sum(math.prod(A[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n))))


rng = np.random.default_rng(11)
print(f"{'n':>3} {'predicted c':>12} {'measured c':>12} {'rel err':>10} "
      f"{'m_n/gamma_n - 1':>16} {'formula at T_n':>15}")
for n in range(4, 9):
    g = math.factorial(n) / n ** n
    m = math.factorial(n - 2) * ((n - 2) / (n - 1) ** 2) ** (n - 2)
    c_pred = n / (2 * (n - 1))
    # measure on small doubly stochastic perturbations
    best = []
    for _ in range(40):
        E = rng.standard_normal((n, n))
        E -= E.mean(axis=1, keepdims=True)
        E -= E.mean(axis=0, keepdims=True)
        E *= 1e-4 / np.linalg.norm(E)
        B = np.full((n, n), 1 / n) + E
        best.append((per(B) / g - 1) / float((E ** 2).sum()))
    c_meas = float(np.mean(best))
    # the formula evaluated at the Knopp-Sinkhorn extremal
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1)
    T[:, 0] = 1 / (n - 1)
    T[0, 0] = 0.0
    d2 = float(((T - 1 / n) ** 2).sum())
    print(f"{n:>3} {c_pred:>12.6f} {c_meas:>12.6f} {abs(c_pred - c_meas)/c_pred:>10.2e} "
          f"{m/g - 1:>16.6e} {c_pred * d2:>15.6e}")
print("\n||T_n - J/n||_F^2 = 1/(n-1)^2 exactly; the last two columns agree to leading order,")
print("so S(n, c) with the true local constant says no more than Knopp-Sinkhorn already does.")
