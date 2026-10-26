"""Numerical optimisation run 1: boundary gaps of the Dittert functional.

For each n given on the command line, maximise phi(A) = prod r_i + prod c_j - per(A)
over the face F_n = {A in K_n : a_11 = 0} by multi-start local optimisation
(L-BFGS-B on a softmax parametrisation of the 24..63 free entries) and record
  g_n := (2 - n!/n^n) - max_{F_n} phi          (the boundary gap; evidence only)
against the Knopp-Sinkhorn gap m_n - gamma_n, where m_n is the minimum permanent on
the boundary of the doubly stochastic polytope.  T_n (the Knopp-Sinkhorn extremal)
lies in F_n with phi(T_n) = 2 - m_n, so g_n <= m_n - gamma_n always.  The optimiser
and its (R, C, per) are recorded in optima.json.  Seeds are fixed.  No numpy matmul
(pathologically slow on this machine); the permanent is Ryser's formula.
"""
import itertools
import json
import math
import sys

import numpy as np
from scipy.optimize import minimize


def permanent(A):
    n = A.shape[0]
    total = 0.0
    for r in range(1, n + 1):
        sgn = (-1) ** (n - r)
        for cols in itertools.combinations(range(n), r):
            total += sgn * np.prod(A[:, cols].sum(axis=1))
    return total


def phi_of(A):
    return np.prod(A.sum(axis=1)) + np.prod(A.sum(axis=0)) - permanent(A)


def unpack(theta, n):
    z = np.zeros(n * n)
    z[1:] = theta
    w = np.exp(z - z.max())
    w[0] = 0.0
    return (n * w / w.sum()).reshape(n, n)


def ks_extremal(n):
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1)
    T[:, 0] = 1 / (n - 1)
    T[0, 0] = 0.0
    return T


def solve(n, starts, rng):
    def f(theta):
        return -phi_of(unpack(theta, n))

    z = np.log(ks_extremal(n).flatten()[1:] / n)  # softmax pre-image of T_n
    inits = [z]
    for _ in range(starts):
        s = rng.choice([0.02, 0.1, 0.3, 1.0])
        inits.append(z + s * rng.standard_normal(n * n - 1))
    best = None
    for th0 in inits:
        res = minimize(f, th0, method="L-BFGS-B",
                       options={"maxiter": 3000, "ftol": 1e-15, "gtol": 1e-10})
        val = -res.fun
        if best is None or val > best[0]:
            best = (val, unpack(res.x, n))
    return best


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [5, 6, 7, 8]
    rng = np.random.default_rng(20260903)
    out = {}
    for n in ns:
        gamma = math.factorial(n) / n ** n
        m = math.factorial(n - 2) * ((n - 2) / (n - 1) ** 2) ** (n - 2)
        starts = {5: 200, 6: 120, 7: 60, 8: 30}.get(n, 20)
        val, A = solve(n, starts, rng)
        R, C, P = np.prod(A.sum(1)), np.prod(A.sum(0)), permanent(A)
        g = (2 - gamma) - val
        out[n] = {"n": n, "gamma_n": gamma, "m_n": m, "ks_gap": m - gamma,
                  "max_phi_on_face": val, "boundary_gap": g,
                  "boundary_gap_over_ks_gap": g / (m - gamma),
                  "R": R, "C": C, "per": P, "phi_T_n": phi_of(ks_extremal(n)),
                  "optimiser": A.tolist(), "starts": starts + 1}
        print(f"n={n}: max phi on face = {val:.12f}, 2-gamma = {2 - gamma:.12f}, "
              f"g_n = {g:.3e}, m_n-gamma_n = {m - gamma:.3e}, g/(m-gamma) = {g / (m - gamma):.4f}; "
              f"optimiser R={R:.8f} C={C:.8f} per={P:.6e} (gamma={gamma:.6e}, m={m:.6e})")
        sys.stdout.flush()
        json.dump(out, open("optima.json", "w"), indent=1)
