"""Is the quadratic strengthening of the van der Waerden inequality true?

Claim Q(n):  for every doubly stochastic n x n matrix B,

    per(B) >= gamma_n ( 1 + (n / (2(n-1))) ||B - J_n/n||_F^2 ),      gamma_n = n!/n^n.

Three facts already point at it and fix the constant.

  * At `n = 2` it is an identity: with B = [[t, 1-t], [1-t, t]], both sides are
    1/2 + 2(t - 1/2)^2.
  * The constant is exactly the local Hessian of the permanent at `J_n/n`
    (attack/spectral-gap-near-maximisers, unit 3), so no larger constant can hold.
  * At the Knopp-Sinkhorn extremal `T_n`, which has ||T_n - J/n||_F^2 = 1/(n-1)^2 exactly,
    the two sides agree to leading order.

So `T_n` and `J_n/n` are both near-equality cases and the claim is tight at two very different
points.  This script looks for a violation: over the vertices (permutation matrices), over the
block-diagonal matrices, over random doubly stochastic matrices, and by direct minimisation of
the slack `per(B) - gamma_n (1 + c_n ||B - J/n||^2)` with multi-start Nelder-Mead on the
Birkhoff polytope parametrised by Sinkhorn.
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize


def permanent(A):
    n = A.shape[0]
    idx = np.arange(1 << n)
    S = np.zeros((1 << n, n))
    sizes = np.zeros(1 << n, dtype=np.int64)
    for b in range(n):
        has = (idx >> b) & 1 == 1
        S[has] += A[:, b]
        sizes[has] += 1
    sign = np.where((n - sizes) % 2 == 0, 1.0, -1.0)
    return float((sign * np.prod(S, axis=1))[1:].sum())


def sinkhorn(X, iters=20000, tol=1e-14):
    n = X.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = np.einsum("ij,j->i", X, d2) * d1
        d1 = d1 / r
        c = np.einsum("ij,i->j", X, d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return np.einsum("i,ij,j->ij", d1, X, d2)


def slack(B, n, gamma, c):
    d2 = float(((B - 1.0 / n) ** 2).sum())
    return permanent(B) - gamma * (1 + c * d2)


rng = np.random.default_rng(20260904)
print(f"{'n':>3} {'c_n':>9} {'perm mats':>12} {'blocks':>12} {'random':>12} "
      f"{'optimised':>12} {'holds':>7}")
for n in [int(a) for a in sys.argv[1:]] or [2, 3, 4, 5, 6, 7]:
    gamma = math.factorial(n) / n ** n
    c = n / (2 * (n - 1))

    worst_perm = min(slack(np.eye(n)[list(p)], n, gamma, c)
                     for p in itertools.permutations(range(n)))
    worst_block = math.inf
    for k in range(1, n):
        B = np.zeros((n, n))
        B[:k, :k] = 1.0 / k
        B[k:, k:] = 1.0 / (n - k)
        worst_block = min(worst_block, slack(B, n, gamma, c))
        for t in np.linspace(0.0, 1.0, 41):          # segment to J/n
            worst_block = min(worst_block, slack((1 - t) * B + t / n, n, gamma, c))

    worst_rand = math.inf
    for _ in range(4000):
        spread = rng.choice([0.2, 0.8, 2.0, 4.0])
        B = sinkhorn(np.exp(spread * rng.standard_normal((n, n))))
        worst_rand = min(worst_rand, slack(B, n, gamma, c))

    def neg(theta):
        return slack(sinkhorn(np.exp(np.clip(theta.reshape(n, n), -40, 40))), n, gamma, c)

    worst_opt = math.inf
    for s in range(30):
        th0 = [0.3, 1.0, 3.0][s % 3] * rng.standard_normal(n * n)
        res = minimize(neg, th0, method="Nelder-Mead",
                       options={"maxiter": 4000, "xatol": 1e-9, "fatol": 1e-13})
        worst_opt = min(worst_opt, float(res.fun))

    lo = min(worst_perm, worst_block, worst_rand, worst_opt)
    print(f"{n:>3} {c:>9.6f} {worst_perm:>12.4e} {worst_block:>12.4e} {worst_rand:>12.4e} "
          f"{worst_opt:>12.4e} {'yes' if lo > -1e-11 else 'NO':>7}")
print("\nA negative slack is a counterexample; 0 within 1e-11 is an equality case.")
