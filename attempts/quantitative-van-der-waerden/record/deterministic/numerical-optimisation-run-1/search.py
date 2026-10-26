"""The counterexample space of the quantitative van der Waerden inequality, profiled by distance.

A counterexample is a doubly stochastic `B` with

    ratio(B) := ( per(B)/gamma_n - 1 ) / ||B - J_n/n||_F^2   <   1/4,     gamma_n = n!/n^n.

Two things are computed for each `n`.

* **The global minimum** of `ratio` over the polytope, by multi-start L-BFGS-B on the Sinkhorn
  parametrisation `B = Sinkhorn(exp(theta))`.  That is the sharp constant `c*(n)`.
* **The profile** `rho_n(t) = min { ratio(B) : ||B - J_n/n||_F = t }` on a grid of `t`, by the
  same optimiser with a penalty on the distance.  The profile says *where* in the polytope the
  minimum sits, which is what a proof has to be tight against, and it shows that the danger is
  not near the centre: the exact local expansion gives `ratio -> n/(2(n-1)) >= 1/2` as `t -> 0`,
  so the counterexample space excludes a ball around `J_n/n`.

The grid runs from `t = 0.1` to the polytope's diameter from the centre, which is attained at a
permutation matrix: `||P - J_n/n||_F^2 = 2n - 3 + 1/n`.

Three explicit matrices are evaluated as well, because each is a candidate the claim must
survive: the Knopp-Sinkhorn extremal `T_n`, the average `(I + C_n)/2` of the identity and the
`n`-cycle, and the block matrix `blockdiag(J_k/k, J_{n-k}/(n-k))`.
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


def sinkhorn(X, iters=4000, tol=1e-13):
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


def build(theta, n):
    return sinkhorn(np.exp(np.clip(theta.reshape(n, n), -40, 40)))


def ratio(B, n, gamma):
    d2 = float(((B - 1.0 / n) ** 2).sum())
    if d2 < 1e-16:
        return math.inf
    return (permanent(B) / gamma - 1.0) / d2


def explicit(n):
    out = {}
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1)
    T[:, 0] = 1 / (n - 1)
    T[0, 0] = 0.0
    out["T_n"] = T
    C = np.eye(n)[[(i + 1) % n for i in range(n)]]
    out["(I+C)/2"] = 0.5 * (np.eye(n) + C)
    for k in range(1, n // 2 + 1):
        B = np.zeros((n, n))
        B[:k, :k] = 1.0 / k
        B[k:, k:] = 1.0 / (n - k)
        out[f"block {k}"] = B
    return out


def run(ns, seed=20260904):
    rng = np.random.default_rng(seed)
    rows = []
    for n in ns:
        gamma = math.factorial(n) / n ** n
        starts = {3: 60, 4: 60, 5: 50, 6: 40, 7: 30, 8: 24, 9: 18, 10: 14, 11: 10}.get(n, 8)

        best = math.inf
        for s in range(starts):
            th0 = [0.3, 1.0, 2.5, 5.0][s % 4] * rng.standard_normal(n * n)
            res = minimize(lambda th: ratio(build(th, n), n, gamma), th0,
                           method="Nelder-Mead",
                           options={"maxiter": 4000, "xatol": 1e-9, "fatol": 1e-13})
            best = min(best, float(res.fun))

        tmax = math.sqrt(2 * n - 3 + 1.0 / n)
        profile = []
        for t in np.linspace(0.1, tmax, 8):
            pen = 200.0

            def obj(th, t=t):
                B = build(th, n)
                d = math.sqrt(float(((B - 1.0 / n) ** 2).sum()))
                return ratio(B, n, gamma) + pen * (d - t) ** 2

            bp = math.inf
            for s in range(max(4, starts // 4)):
                th0 = [0.3, 1.0, 2.5][s % 3] * rng.standard_normal(n * n)
                res = minimize(obj, th0, method="Nelder-Mead",
                               options={"maxiter": 3000, "xatol": 1e-8, "fatol": 1e-12})
                B = build(res.x, n)
                d = math.sqrt(float(((B - 1.0 / n) ** 2).sum()))
                if abs(d - t) < 0.05 * t:
                    bp = min(bp, ratio(B, n, gamma))
            profile.append((float(t), bp))

        ex = {k: ratio(B, n, gamma) for k, B in explicit(n).items()}
        rows.append({"n": n, "c_star": best, "local_upper": n / (2 * (n - 1)),
                     "profile": profile, "explicit": ex, "starts": starts})
    return rows


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6, 7, 8, 9]
    for r in run(ns):
        n = r["n"]
        print(f"n = {n}: c*(n) = {r['c_star']:.6f}  (local upper bound {r['local_upper']:.6f}, "
              f"{r['starts']} starts)", flush=True)
        print("   profile  " + "  ".join(f"t={t:.2f}:{v:.3f}" if math.isfinite(v)
                                         else f"t={t:.2f}:--" for t, v in r["profile"]))
        print("   explicit " + "  ".join(f"{k}={v:.4f}" for k, v in r["explicit"].items()))
