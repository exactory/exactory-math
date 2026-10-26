"""Which two-column intermediate statement is true?  For column pairs (j, l) of doubly stochastic B,
with v = col_l (peeled first), v' = col_j (peeled second), d = ||v - 1/n||^2, d' = ||v' - 1/n||^2,
q1 = q_{n-1} (peel x_l), q2 = q_{n-2} (peel x_l then x_j), gg = g(n) g(n-1), X = exp((d + d')/2):

    V1 : per(B) / (gamma_n X)
    I1 : cap(q2) / (gg X)
    I2 : C_2(v, v') K(v + v') / (gg X)
    I3 : cap(q2) / (g(n-1) exp(d'/2) cap(q1))
    I4 : cap(q2) / (g(n-1) exp(d'/2) K(v))            (weaker than I3 since cap(q1) >= K(v))
Minimum ratios over many B and all ordered pairs are printed; a value < 1 kills the statement.
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


def cap_generic(fun_logq_grad, m, starts=3):
    """inf_x q(x)/prod x_j via BFGS on u = log x; fun returns (log q(e^u), grad_u log q)."""
    def f(u):
        lq, gr = fun_logq_grad(u)
        return lq - u.sum(), gr - 1.0
    best = math.inf
    rng = np.random.default_rng(0)
    for s in range(starts):
        u0 = np.zeros(m) if s == 0 else 0.7 * rng.standard_normal(m)
        res = minimize(f, u0, jac=True, method="BFGS", options={"gtol": 1e-11, "maxiter": 4000})
        best = min(best, res.fun)
    return math.exp(best)


def make_q1(Bp, v):
    """q1(x) = prod_s a_s * sum_r v_r / a_r, a = Bp x (Bp is n x (n-1))."""
    def fun(u):
        x = np.exp(np.clip(u, -30, 30))
        a = Bp @ x
        z = 1 / a
        H = float(v @ z)
        lq = float(np.log(a).sum()) + math.log(H)
        # d/dx_j: sum_s b_sj/a_s - (sum_r v_r b_rj / a_r^2)/H
        grad_x = Bp.T @ (1 / a) - (Bp.T @ (v * z * z)) / H
        return lq, grad_x * x
    return fun


def make_q2(Bpp, v, vp):
    """q2(x) = prod_s a_s * P(1/a), P(z) = sum_{r != r'} v_r v'_{r'} z_r z_{r'}, a = Bpp x (n x (n-2))."""
    n = len(v)
    off = np.ones((n, n)) - np.eye(n)

    def fun(u):
        x = np.exp(np.clip(u, -30, 30))
        a = Bpp @ x
        z = 1 / a
        M = (v * z)[:, None] * (vp * z)[None, :] * off
        P = float(M.sum())
        dP_dz = (M.sum(axis=1) + M.sum(axis=0)) / z          # dP/dz_s = sum_{r' != s} v_s v'_{r'} z_{r'} + sum_{r != s} v_r v'_s z_r
        lq = float(np.log(a).sum()) + math.log(P)
        # dz_s/dx_j = -b_sj / a_s^2
        grad_x = Bpp.T @ (1 / a) - (Bpp.T @ (dP_dz * z * z)) / P
        return lq, grad_x * x
    return fun


def C2(v, vp):
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
        res = minimize(f, u0, jac=True, method="BFGS", options={"gtol": 1e-11, "maxiter": 4000})
        best = min(best, res.fun)
    return math.exp(best)


rng = np.random.default_rng(21)
ns = [int(a) for a in sys.argv[1:]] or [4, 5, 6]
for n in ns:
    gam = math.factorial(n) / n ** n
    gg = g(n) * g(n - 1)
    mats = []
    C = np.roll(np.eye(n), 1, axis=1)
    mats.append((np.eye(n) + C) / 2)
    T = np.full((n, n), (n - 2) / (n - 1) ** 2); T[0, :] = 1 / (n - 1); T[:, 0] = 1 / (n - 1); T[0, 0] = 0
    mats.append(T)
    for t in range(36):
        mats.append(sinkhorn(np.exp([0.3, 1.0, 2.5, 5.0][t % 4] * rng.standard_normal((n, n)))))
    for t in range(16):
        m = rng.integers(2, 5)
        wts = rng.dirichlet(np.ones(m))
        mats.append(sum(wts[i] * np.eye(n)[rng.permutation(n)] for i in range(m)))
    for t in range(8):
        lam = rng.uniform(0, 1)
        mats.append((1 - lam) / n + lam * np.eye(n)[rng.permutation(n)])
    worst = {k: (math.inf, None) for k in ("V1", "I1", "I2", "I3", "I4")}
    # sanity check of q1, q2 evaluations against direct formulas at one random point
    B = mats[2]
    v, vp = B[:, n - 1], B[:, n - 2]
    x = np.exp(rng.standard_normal(n - 2))
    a = B[:, : n - 2] @ x
    q2_direct = sum(v[r] * vp[rp] * np.prod(np.delete(a, [r, rp])) for r in range(n) for rp in range(n) if r != rp)
    lq2, _ = make_q2(B[:, : n - 2], v, vp)(np.log(x))
    assert abs(math.exp(lq2) - q2_direct) < 1e-9 * q2_direct
    for B in mats:
        p = permanent(B)
        for l, j in itertools.permutations(range(n), 2):
            v, vp = B[:, l], B[:, j]
            d, dp = float(((v - 1 / n) ** 2).sum()), float(((vp - 1 / n) ** 2).sum())
            X = math.exp((d + dp) / 2)
            rest = [c for c in range(n) if c not in (l, j)]
            Bpp = B[:, rest]
            Bp = B[:, rest + [j]]
            if (Bpp.sum(axis=1) <= 1e-12).any():
                continue                       # a row lives entirely in the two peeled columns
            cq2 = cap_generic(make_q2(Bpp, v, vp), n - 2)
            cq1 = cap_generic(make_q1(Bp, v), n - 1)
            c2 = C2(v, vp)
            vals = {"V1": p / (gam * X), "I1": cq2 / (gg * X), "I2": c2 * K(v + vp) / (gg * X),
                    "I3": cq2 / (g(n - 1) * math.exp(dp / 2) * cq1), "I4": cq2 / (g(n - 1) * math.exp(dp / 2) * K(v))}
            for k, val in vals.items():
                if val < worst[k][0]:
                    worst[k] = (val, (np.round(B, 3), l, j))
    print(f"n={n}: " + "  ".join(f"min {k} = {worst[k][0]:.6f}" for k in worst))
    for k in ("I2", "I3"):
        val, (B, l, j) = worst[k]
        print(f"   worst {k} at columns l={l} (first), j={j} (second) of\n{B}")
