"""Explicit lower bounds for C_2(v, v') = inf_y P(y)/y^(v+v'), P(y) = sum_{r != r'} v_r v'_{r'} y_r y_{r'}.

Entropy dual: log C_2 = max over lambda on ordered pairs r != r' with margins
lambda_{r.} + lambda_{.r} = v_r + v'_r of sum lambda log(v_r v'_{r'} / lambda).
Any feasible lambda gives a lower bound.  Two explicit choices:
  L1: lambda_{rr'} = mu_r v'_{r'}/(1 - v'_r)  with mu fixed by the margins (closed form),
  L2: same with the roles of v and v' swapped,
and the exact C_2 for comparison.  Also reports (bound * K / (g(n) g(n-1)) - 1) / (||d||^2 + ||d'||^2).
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize


def sinkhorn(X, iters=20000, tol=1e-14):
    n = X.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = (X @ d2) * d1
        d1 = d1 / r
        c = (X.T @ d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return d1[:, None] * X * d2[None, :]


def K(w):
    return float(np.prod([(1 - t) ** (1 - t) if t < 1 else 1.0 for t in w]))


def g(k):
    return ((k - 1) / k) ** (k - 1)


def C2_exact(v, vp):
    w = v + vp
    n = len(v)
    off = np.ones((n, n)) - np.eye(n)

    def f(u):
        u = np.clip(u - u.mean(), -25, 25)
        y = np.exp(u)
        M = (v * y)[:, None] * (vp * y)[None, :] * off
        P = float(M.sum())
        dP = M.sum(axis=1) + M.sum(axis=0)
        return math.log(P) - float(w @ u), dP / P - w

    best = math.inf
    rng = np.random.default_rng(0)
    for s in range(3):
        u0 = np.zeros(n) if s == 0 else rng.standard_normal(n)
        res = minimize(f, u0, jac=True, method="BFGS", options={"gtol": 1e-11, "maxiter": 3000})
        best = min(best, res.fun)
    return math.exp(best)


def L1(v, vp):
    """lambda_{rr'} = mu_r v'_{r'}/(1-v'_r); margins force
       mu_s (1 - 2 v'_s)/(1 - v'_s) = v_s + v'_s (1 - M),  M = sum_s mu_s/(1 - v'_s)."""
    if (vp >= 0.5 - 1e-12).any():
        return None
    w = v + vp
    M = float((w / (1 - 2 * vp)).sum() / (1 + (vp / (1 - 2 * vp)).sum()))
    mu = (1 - vp) * (v + vp * (1 - M)) / (1 - 2 * vp)
    if (mu < -1e-12).any():
        return None
    val = 0.0
    for r in range(len(v)):
        if mu[r] > 1e-300:
            if v[r] <= 0:
                return None
            val += mu[r] * math.log(v[r] * (1 - vp[r]) / mu[r])
    return math.exp(val)


def entropy_dual_check(v, vp, lam):
    """Value of sum lambda log(c/lambda) for a given lambda matrix (zero diagonal)."""
    n = len(v)
    val = 0.0
    for r in range(n):
        for s in range(n):
            if r != s and lam[r, s] > 0:
                val += lam[r, s] * math.log(v[r] * vp[s] / lam[r, s])
    return math.exp(val)


rng = np.random.default_rng(11)
ns = [int(a) for a in sys.argv[1:]] or [4, 5, 6]
for n in ns:
    gg = g(n) * g(n - 1)
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1)
    T[:, 0] = 1 / (n - 1)
    T[0, 0] = 0
    mats = [T, np.full((n, n), 1 / n)]
    for t in range(40):
        mats.append(sinkhorn(np.exp([0.3, 1.0, 2.0][t % 3] * rng.standard_normal((n, n)))))
    worst_gap, worst_cL, worst_cC = 0.0, math.inf, math.inf
    for B in mats:
        for j, l in itertools.combinations(range(n), 2):
            v, vp = B[:, j], B[:, l]
            c2 = C2_exact(v, vp)
            cands = [x for x in (L1(v, vp), L1(vp, v)) if x is not None]
            if not cands:
                continue
            L = max(cands)
            d2 = float(((v - 1 / n) ** 2).sum() + ((vp - 1 / n) ** 2).sum())
            worst_gap = max(worst_gap, c2 / L - 1)
            if d2 > 1e-10:
                worst_cL = min(worst_cL, (L * K(v + vp) / gg - 1) / d2)
                worst_cC = min(worst_cC, (c2 * K(v + vp) / gg - 1) / d2)
    print(f"n={n}: max relative gap C_2/L - 1 = {worst_gap:.4e};  min c_2 with exact C_2 = {worst_cC:.4f}; "
          f"with explicit L = {worst_cL:.4f}")
    # the T_n pair, explicitly
    v, vp = T[:, 0], T[:, 1]
    print(f"   T_n pair: C_2 = {C2_exact(v, vp):.6f}, L1(v,v') = {L1(v, vp)}, L1(v',v) = {L1(vp, v)}, "
          f"1 - <v,v'> = {1 - float(v @ vp):.6f}")
