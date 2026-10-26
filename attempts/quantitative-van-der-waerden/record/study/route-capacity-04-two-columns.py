"""Two-column generalisation of Lemma A.

For the last m columns V = B[:, n-m:] with row sums w = V 1, let
    P_V(y) = sum_{|S|=m} per(V[S,:]) prod_{s in S} y_s,     C_m(V) = inf_{y>0} P_V(y) / prod_s y_s^{w_s}.
Claim (Lemma A_m): cap(q_{n-m}) >= C_m(V) K(w), K(w) = prod_s (1-w_s)^(1-w_s); hence
    per(B) >= gamma_{n-m} C_m(V) K(w).
For m = 1, C_1 = 1 and this is Lemma A.  This script measures, for m = 2,
    ratio_2(B) = min over column pairs of per(B) / (gamma_{n-2} C_2 K)          [must be >= 1]
and the constant
    c_2(n) = min over B, pairs of (C_2 K / (g(n) g(n-1)) - 1) / (||v-1/n||^2 + ||v'-1/n||^2).
If c_2(n) >= 1/2 then the best pair gives Q(1/n).
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize


def permanent(A):
    n = A.shape[0]
    return sum(math.prod(A[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n)))


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


def C2(v, vp):
    """C_2(v, v') = inf_y sum_{r != r'} v_r v'_{r'} y_r y_{r'} / prod y^(v+v'), cancellation-free."""
    w = v + vp
    n = len(v)
    off = np.ones((n, n)) - np.eye(n)

    def f(u):
        u = np.clip(u - u.mean(), -25, 25)          # homogeneity: shift-invariant objective
        y = np.exp(u)
        M = (v * y)[:, None] * (vp * y)[None, :] * off   # M_{rr'} = v_r y_r v'_{r'} y_{r'}, r != r'
        P = float(M.sum())
        dP = M.sum(axis=1) + M.sum(axis=0)              # y_s dP/dy_s = row s + column s
        return math.log(P) - float(w @ u), dP / P - w

    best = math.inf
    rng = np.random.default_rng(0)
    for s in range(3):
        u0 = np.zeros(n) if s == 0 else rng.standard_normal(n)
        res = minimize(f, u0, jac=True, method="BFGS", options={"gtol": 1e-11, "maxiter": 3000})
        best = min(best, res.fun)
    return math.exp(best)


rng = np.random.default_rng(7)
ns = [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6]
for n in ns:
    gam = math.factorial(n) / n ** n
    gam2 = math.factorial(n - 2) / (n - 2) ** (n - 2) if n > 2 else 1.0
    mats = []
    C = np.roll(np.eye(n), 1, axis=1)
    mats.append((np.eye(n) + C) / 2)
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1)
    T[:, 0] = 1 / (n - 1)
    T[0, 0] = 0
    mats.append(T)
    for t in range(60):
        spread = [0.3, 1.0, 2.5, 5.0][t % 4]
        mats.append(sinkhorn(np.exp(spread * rng.standard_normal((n, n)))))
    for t in range(30):
        m = rng.integers(2, 5)
        wts = rng.dirichlet(np.ones(m))
        mats.append(sum(wts[i] * np.eye(n)[rng.permutation(n)] for i in range(m)))
    for t in range(20):
        lam = rng.uniform(0, 1)
        mats.append((1 - lam) / n + lam * np.eye(n)[rng.permutation(n)])
    worst_ratio, worst_c2, arg = math.inf, math.inf, None
    for B in mats:
        p = permanent(B)
        e2 = float(((B - 1 / n) ** 2).sum())
        for j, l in itertools.combinations(range(n), 2):
            v, vp = B[:, j], B[:, l]
            bound = gam2 * C2(v, vp) * K(v + vp)
            worst_ratio = min(worst_ratio, p / bound)
            d2 = float(((v - 1 / n) ** 2).sum() + ((vp - 1 / n) ** 2).sum())
            if d2 > 1e-12:
                c2 = (bound / gam - 1) / d2
                if c2 < worst_c2:
                    worst_c2, arg = c2, (B.copy(), j, l)
    print(f"n={n}: min per/(gamma_(n-2) C_2 K) = {worst_ratio:.9f}   min c_2 = {worst_c2:.6f}")
    B, j, l = arg
    print(f"   worst pair columns {j},{l} of\n{np.round(B, 4)}")
    # also: the best-pair bound as a quadratic constant against ||E||^2
    worst_q = math.inf
    for B in mats:
        e2 = float(((B - 1 / n) ** 2).sum())
        if e2 < 1e-12:
            continue
        best = max(gam2 * C2(B[:, j], B[:, l]) * K(B[:, j] + B[:, l]) for j, l in itertools.combinations(range(n), 2))
        worst_q = min(worst_q, (best / gam - 1) / e2)
    print(f"   min over B of (best-pair bound/gamma - 1)/||E||^2 = {worst_q:.6f}   (1/n = {1/n:.4f}, 1/(2n) = {1/(2*n):.4f})")
