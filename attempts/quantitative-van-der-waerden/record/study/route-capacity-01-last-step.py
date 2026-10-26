"""Measure the single-step constant c'(n) in

    cap(q_{n-1}) >= g(n) (1 + c' ||v - 1/n||^2),   v = column n of B,

where q_{n-1}(x) = sum_r v_r prod_{s != r} l_s(x), l_s(x) = sum_{j<n} b_sj x_j, and
g(n) = ((n-1)/n)^(n-1).  Gurvits applied to q_{n-1} gives per(B) >= gamma_{n-1} cap(q_{n-1}),
so (*) implies per(B) >= gamma_n (1 + c' max_j ||col_j - 1/n||^2) >= gamma_n (1 + (c'/n) ||E||^2).

cap(q_{n-1}) = inf_{x>0} q_{n-1}(x) / prod x_j is computed by minimising the convex function
u -> log q_{n-1}(e^u) - sum u_j with BFGS (analytic gradient), several starts.
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


def q_and_grad(Bp, v, u):
    """q_{n-1}(e^u) and its gradient in u, for Bp = B[:, :n-1] (n x (n-1)) and v = B[:, n-1]."""
    x = np.exp(u)
    ell = Bp @ x                       # n row values
    n = len(v)
    # q = sum_r v_r prod_{s != r} ell_s
    # use products excluding one index, computed stably by prefix/suffix products
    pre = np.ones(n + 1)
    suf = np.ones(n + 1)
    for s in range(n):
        pre[s + 1] = pre[s] * ell[s]
    for s in range(n - 1, -1, -1):
        suf[s] = suf[s + 1] * ell[s]
    excl = np.array([pre[r] * suf[r + 1] for r in range(n)])  # prod_{s != r} ell_s
    q = float(np.dot(v, excl))
    # d q / d x_j = sum_r v_r sum_{s != r} b_sj prod_{t != r, s} ell_t
    # = sum_r v_r sum_{s != r} b_sj excl_r / ell_s   (ell_s > 0 assumed)
    # write as sum_s b_sj (sum_{r != s} v_r excl_r) / ell_s
    tot = np.dot(v, excl)
    inner = np.array([(tot - v[s] * excl[s]) / ell[s] for s in range(n)])
    dq_dx = Bp.T @ inner
    grad_u = dq_dx * x                 # chain rule for x = e^u
    return q, grad_u


def cap_last_step(B, col=None, starts=2, rng=None):
    n = B.shape[0]
    if col is None:
        col = n - 1
    idx = [j for j in range(n) if j != col]
    Bp = B[:, idx]
    v = B[:, col]
    rng = rng or np.random.default_rng(0)

    def f(u):
        q, g = q_and_grad(Bp, v, u)
        return math.log(q) - u.sum(), g / q - 1.0

    best = math.inf
    for s in range(starts):
        u0 = np.zeros(n - 1) if s == 0 else rng.standard_normal(n - 1)
        res = minimize(f, u0, jac=True, method="BFGS", options={"gtol": 1e-12, "maxiter": 2000})
        best = min(best, res.fun)
    return math.exp(best)


def g(k):
    return ((k - 1) / k) ** (k - 1)


def ratio_col(B, col):
    n = B.shape[0]
    v = B[:, col]
    d2 = float(((v - 1.0 / n) ** 2).sum())
    if d2 < 1e-16:
        return math.inf
    return (cap_last_step(B, col) / g(n) - 1.0) / d2


if __name__ == "__main__":
    rng = np.random.default_rng(1)
    ns = [int(a) for a in sys.argv[1:]] or [3, 4, 5]
    for n in ns:
        gamma = math.factorial(n) / n ** n
        # 1. sanity: (I + C_n)/2, last column
        C = np.roll(np.eye(n), 1, axis=1)
        B = (np.eye(n) + C) / 2
        cap = cap_last_step(B)
        print(f"n={n} (I+C)/2: cap(q_{n-1})={cap:.6f}, g(n)={g(n):.6f}, ratio to g={cap/g(n):.6f}, "
              f"1/2 (degree-2 bound)={0.5:.4f}, per={permanent(B):.6f}, gamma_{n-1}*cap="
              f"{math.factorial(n-1)/(n-1)**(n-1)*cap:.6f}")
        print(f"        c' for this column = {ratio_col(B, n-1):.6f}")
        # 2. random search of min c' over doubly stochastic B
        worst = (math.inf, None)
        for trial in range(120):
            spread = [0.3, 1.0, 2.5, 5.0][trial % 4]
            B = sinkhorn(np.exp(spread * rng.standard_normal((n, n))))
            for col in range(n):
                r = ratio_col(B, col)
                if r < worst[0]:
                    worst = (r, B.copy(), col)
        r, B, col = worst
        print(f"n={n} random search: min c' = {r:.6f} at col {col}; B=\n{np.round(B, 4)}")
        # 3. Nelder-Mead refinement of the worst case over B (Sinkhorn parametrisation)
        def obj(theta):
            Bm = sinkhorn(np.exp(np.clip(theta.reshape(n, n), -30, 30)))
            return min(ratio_col(Bm, c) for c in range(n))
        th0 = np.log(np.maximum(B, 1e-9)).ravel()
        res = minimize(obj, th0, method="Nelder-Mead", options={"maxiter": 800, "xatol": 1e-8, "fatol": 1e-10})
        Bm = sinkhorn(np.exp(np.clip(res.x.reshape(n, n), -30, 30)))
        print(f"n={n} refined: min c' = {res.fun:.6f}; B=\n{np.round(Bm, 4)}")
        print(f"        per(B)/gamma-1 over ||E||^2 = {(permanent(Bm)/gamma-1)/((Bm-1/n)**2).sum():.6f}")
