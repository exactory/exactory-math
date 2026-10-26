"""Exact (rational) verification of the identities used in the proofs.

With B = J/n + E doubly stochastic and F = nE:

  (i)   per(J/n + tE) = gamma_n * sum_k r_k(F) t^k / (n)_k   as polynomials in t (n = 3, 4, 5);
  (ii)  r_2(F) = ||F||^2 / 2   and   r_3(F) = (2/3) sum_ij F_ij^3;
  (iii) 24 r_4(F) = 36 p_4 - 18 (sum_i R_i^2 + sum_j C_j^2) + 3 ||F||^4 + 6 ||F F^T||_F^2;
  (iv)  n = 3:  per(B)/gamma_3 - 1 - ||E||^2/4 = sum_rows (1 - 4 e_2(row) + 9 e_3(row)),
        and 1 - 4 e_2 + 9 e_3 = (1/2) sum_sym x (x - y)(x - z)  (Schur, degree 1) on x+y+z = 1;
  (v)   q_2 - 1 = ||E||^2/(n-1)^2  where q_2 = Sigma_2(B)/Sigma_2(J/n).

Random rational doubly stochastic matrices are convex combinations of permutation matrices
with rational weights.  Everything is exact in sympy.
"""
import itertools
import random

import sympy as sp

random.seed(6)


def permanent(M):
    n = M.rows
    return sum(sp.prod([M[i, p[i]] for i in range(n)]) for p in itertools.permutations(range(n)))


def matching_sum(F, k):
    n = F.rows
    return sum(permanent(F.extract(list(S), list(T)))
               for S in itertools.combinations(range(n), k)
               for T in itertools.combinations(range(n), k))


def random_rational_ds(n, m=4):
    B = sp.zeros(n, n)
    weights = [sp.Rational(random.randint(1, 9), 1) for _ in range(m)]
    total = sum(weights)
    for w in weights:
        p = list(range(n))
        random.shuffle(p)
        for i in range(n):
            B[i, p[i]] += w / total
    return B


t = sp.symbols("t")
for n in (3, 4, 5):
    gamma = sp.Rational(sp.factorial(n), n ** n)
    for trial in range(3):
        B = random_rational_ds(n)
        assert all(sum(B.row(i)) == 1 for i in range(n)) and all(sum(B.col(j)) == 1 for j in range(n))
        E = B - sp.ones(n, n) / n
        F = n * E
        r = [matching_sum(F, k) for k in range(n + 1)]
        lhs = sp.expand(permanent(sp.ones(n, n) / n + t * E))
        rhs = sp.expand(gamma * sum(r[k] * t ** k / sp.ff(n, k) for k in range(n + 1)))
        assert sp.simplify(lhs - rhs) == 0, (n, trial, "(i)")
        Phi = sum(F[i, j] ** 2 for i in range(n) for j in range(n))
        assert r[2] == Phi / 2, "(ii) r2"
        assert r[3] == sp.Rational(2, 3) * sum(F[i, j] ** 3 for i in range(n) for j in range(n)), "(ii) r3"
        if n >= 4:
            G = F.multiply_elementwise(F)
            p4 = sum(F[i, j] ** 4 for i in range(n) for j in range(n))
            R = [sum(G.row(i)) for i in range(n)]
            C = [sum(G.col(j)) for j in range(n)]
            FFt = F * F.T
            rhs4 = (36 * p4 - 18 * (sum(x ** 2 for x in R) + sum(x ** 2 for x in C))
                    + 3 * Phi ** 2 + 6 * sum(FFt[i, j] ** 2 for i in range(n) for j in range(n))) / 24
            assert r[4] == rhs4, "(iii) r4"
        Sig2 = matching_sum(B, 2)
        Sig2J = sp.Rational(sp.binomial(n, 2) ** 2 * 2, n ** 2)
        d2 = sum(E[i, j] ** 2 for i in range(n) for j in range(n))
        assert Sig2 / Sig2J - 1 == d2 / (n - 1) ** 2, "(v) q2"
        if n == 3:
            lhs3 = permanent(B) / gamma - 1 - d2 / 4
            rhs3 = 0
            for i in range(3):
                x, y, z = B[i, 0], B[i, 1], B[i, 2]
                rhs3 += 1 - 4 * (x * y + y * z + z * x) + 9 * x * y * z
            assert lhs3 == rhs3, "(iv) n=3 identity"
    print(f"n={n}: identities (i)-(v) hold exactly on 3 random rational matrices")

x, y, z = sp.symbols("x y z")
schur = sp.expand(x * (x - y) * (x - z) + y * (y - x) * (y - z) + z * (z - x) * (z - y))
e1, e2, e3 = x + y + z, x * y + y * z + z * x, x * y * z
assert sp.expand(schur - (e1 ** 3 - 4 * e1 * e2 + 9 * e3)) == 0
print("Schur(1): sum x(x-y)(x-z) = e1^3 - 4 e1 e2 + 9 e3   (exact)")
# the 3 x 3 cycle matrix is an equality case
B = sp.Matrix([[1, 1, 0], [0, 1, 1], [1, 0, 1]]) / 2
E = B - sp.ones(3, 3) / 3
assert permanent(B) / sp.Rational(2, 9) - 1 - sum(E[i, j] ** 2 for i in range(3) for j in range(3)) / 4 == 0
print("(I + C_3)/2: per/gamma_3 - 1 - ||E||^2/4 = 0 exactly")
