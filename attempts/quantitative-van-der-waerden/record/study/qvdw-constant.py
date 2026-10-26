"""The largest constant in the quadratic van der Waerden inequality.

`per(B) >= gamma_n (1 + c ||B - J_n/n||_F^2)` on the doubly stochastic polytope holds for

    c*(n) = min over B != J_n/n of  ( per(B)/gamma_n - 1 ) / ||B - J_n/n||_F^2,

which is positive because van der Waerden has `J_n/n` as its only equality point.  The local
value at `J_n/n` is `n/(2(n-1))` (attack/spectral-gap-near-maximisers, unit 3), so
`c*(n) <= n/(2(n-1))`, and `qvdw-test.py` showed the inequality fails at that value from `n = 3`
on: the minimum is attained away from `J_n/n`.

What matters for Dittert's conjecture is only how fast `c*(n)` decays.  The application feeds it
`per(B) <= (1 + eta) gamma_n` with `eta` of order `gamma_n = n!/n^n`, which is factorially small,
and reads off `||B - J/n||_F^2 <= eta / c*(n)`; so any `c*(n) >= 1/poly(n)` is enough.  This
script measures `c*(n)` and reports the minimiser, so that its shape can be recognised.
"""
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


def ratio(B, n, gamma):
    d2 = float(((B - 1.0 / n) ** 2).sum())
    if d2 < 1e-18:
        return math.inf
    return (permanent(B) / gamma - 1.0) / d2


rng = np.random.default_rng(20260904)
print(f"{'n':>3} {'local n/(2(n-1))':>17} {'c*(n)':>11} {'ratio to local':>15} "
      f"{'1/n':>9} {'c* * n':>9} {'minimiser':>28}")
for n in [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6, 7]:
    gamma = math.factorial(n) / n ** n
    local = n / (2 * (n - 1))

    def obj(theta):
        return ratio(sinkhorn(np.exp(np.clip(theta.reshape(n, n), -40, 40))), n, gamma)

    best = (math.inf, None)
    for s in range(60):
        th0 = [0.3, 1.0, 2.5, 5.0][s % 4] * rng.standard_normal(n * n)
        res = minimize(obj, th0, method="Nelder-Mead",
                       options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-14})
        if res.fun < best[0]:
            best = (float(res.fun), sinkhorn(np.exp(np.clip(res.x.reshape(n, n), -40, 40))))
    c, B = best
    # describe the minimiser: sorted entries, scaled by n
    ent = np.sort((B * n).ravel())
    desc = f"n*entries in [{ent[0]:.3f}, {ent[-1]:.3f}], {int((ent < 1e-6).sum())} zeros"
    print(f"{n:>3} {local:>17.6f} {c:>11.6f} {c/local:>15.4f} {1/n:>9.4f} {c*n:>9.4f}  {desc}")
print("\nc*(n) is the largest constant that holds; the Dittert application needs only")
print("c*(n) >= 1/poly(n), because it feeds in eta of order gamma_n = n!/n^n.")
