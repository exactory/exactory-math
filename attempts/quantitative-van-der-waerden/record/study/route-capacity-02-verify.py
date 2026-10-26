"""Numerical check of Lemma A and of the theorem per(B) >= gamma_{n-1} * max_j K(col_j).

Lemma A: for doubly stochastic B with column v = B[:, n-1] and q(x) = sum_r v_r prod_{s != r} l_s(x),
    q(x) >= K(v) prod_j x_j for all x > 0,  K(v) = prod_s (1 - v_s)^(1 - v_s).
Checked as: cap(q) / K(v) >= 1 (cap by convex minimisation), at random and structured B.

Theorem: per(B) >= gamma_{n-1} K(col_j) for every column j; hence
    per(B) >= gamma_n exp(max_j ||col_j - 1/n||^2 / 2) >= gamma_n (1 + ||B - J/n||_F^2 / (2n)).
Checked as: minimum over B of per(B) / (gamma_{n-1} max_j K(col_j)) >= 1, plus the three weaker forms.
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


def K(v):
    return float(np.prod([(1 - t) ** (1 - t) if t < 1 else 1.0 for t in v]))


def g(k):
    return ((k - 1) / k) ** (k - 1)


def q_val_grad(Bp, v, u):
    x = np.exp(u)
    ell = Bp @ x
    n = len(v)
    pre = np.ones(n + 1)
    suf = np.ones(n + 1)
    for s in range(n):
        pre[s + 1] = pre[s] * ell[s]
    for s in range(n - 1, -1, -1):
        suf[s] = suf[s + 1] * ell[s]
    excl = np.array([pre[r] * suf[r + 1] for r in range(n)])
    q = float(np.dot(v, excl))
    tot = q
    inner = np.array([(tot - v[s] * excl[s]) / ell[s] if ell[s] > 0 else 0.0 for s in range(n)])
    dq_dx = Bp.T @ inner
    return q, dq_dx * x


def cap_q(B, col):
    n = B.shape[0]
    idx = [j for j in range(n) if j != col]
    Bp, v = B[:, idx], B[:, col]

    def f(u):
        q, gr = q_val_grad(Bp, v, u)
        return math.log(q) - u.sum(), gr / q - 1.0

    best = math.inf
    rng = np.random.default_rng(0)
    for s in range(3):
        u0 = np.zeros(n - 1) if s == 0 else rng.standard_normal(n - 1)
        res = minimize(f, u0, jac=True, method="BFGS", options={"gtol": 1e-12, "maxiter": 3000})
        best = min(best, res.fun)
    return math.exp(best)


rng = np.random.default_rng(20260904)
ns = [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6]
print("Lemma A check: min over (B, column) of cap(q_{n-1}) / K(v)   [must be >= 1]")
for n in ns:
    mats = []
    C = np.roll(np.eye(n), 1, axis=1)
    mats.append((np.eye(n) + C) / 2)
    mats.append(np.full((n, n), 1.0 / n))
    # Knopp-Sinkhorn face minimiser T_n: zero at (1,1), 1/(n-1) elsewhere in row 1 / column 1,
    # and (n-2)/(n-1)^2 in the rest
    T = np.full((n, n), (n - 2) / (n - 1) ** 2)
    T[0, :] = 1 / (n - 1)
    T[:, 0] = 1 / (n - 1)
    T[0, 0] = 0
    mats.append(T)
    for t in range(40):
        spread = [0.3, 1.0, 2.5, 5.0][t % 4]
        mats.append(sinkhorn(np.exp(spread * rng.standard_normal((n, n)))))
    # sparse matrices: random convex combinations of a few permutation matrices
    for t in range(20):
        m = rng.integers(2, 4)
        w = rng.dirichlet(np.ones(m))
        M = sum(w[i] * np.eye(n)[rng.permutation(n)] for i in range(m))
        mats.append(M)
    worst = math.inf
    for B in mats:
        for col in range(n):
            r = cap_q(B, col) / K(B[:, col])
            worst = min(worst, r)
    print(f"  n={n}: min cap/K = {worst:.12f} over {len(mats)} matrices x {n} columns")

print("\nTheorem check: min over B of per(B) / (gamma_{n-1} max_j K(col_j))   [must be >= 1]")
print("  and of per(B) / (gamma_n exp(max_j ||col_j-1/n||^2/2)), per(B) / (gamma_n (1 + ||E||^2/(2n)))")
for n in ns:
    gam = math.factorial(n) / n ** n
    gam1 = math.factorial(n - 1) / (n - 1) ** (n - 1)
    w1 = w2 = w3 = math.inf
    arg = None
    for t in range(400):
        kind = t % 3
        if kind == 0:
            B = sinkhorn(np.exp([0.3, 1.0, 2.5, 5.0][(t // 3) % 4] * rng.standard_normal((n, n))))
        elif kind == 1:
            m = rng.integers(2, 5)
            w = rng.dirichlet(np.ones(m))
            B = sum(w[i] * np.eye(n)[rng.permutation(n)] for i in range(m))
        else:
            lam = rng.uniform(0, 1)
            B = (1 - lam) * np.full((n, n), 1.0 / n) + lam * np.eye(n)[rng.permutation(n)]
        p = permanent(B)
        kmax = max(K(B[:, j]) for j in range(n))
        dmax = max(float(((B[:, j] - 1 / n) ** 2).sum()) for j in range(n))
        e2 = float(((B - 1 / n) ** 2).sum())
        r1 = p / (gam1 * kmax)
        r2 = p / (gam * math.exp(dmax / 2))
        r3 = p / (gam * (1 + e2 / (2 * n)))
        if r1 < w1:
            w1, arg = r1, B.copy()
        w2, w3 = min(w2, r2), min(w3, r3)
    print(f"  n={n}: min per/(gamma_(n-1) max K) = {w1:.9f}, min per/(gamma_n e^(d/2)) = {w2:.9f}, "
          f"min per/(gamma_n(1+||E||^2/2n)) = {w3:.9f}")
    # local sanity: sharp constant of the max-column bound near J/n along a random direction
    E = rng.standard_normal((n, n))
    E -= E.mean(axis=0, keepdims=True)
    E -= E.mean(axis=1, keepdims=True)
    for eps in [1e-2, 1e-3]:
        B = 1 / n + eps * E
        p = permanent(B)
        kmax = max(K(B[:, j]) for j in range(n))
        print(f"      eps={eps}: (per/gamma-1)/||E||^2 = {(p/gam-1)/((B-1/n)**2).sum():.6f}, "
              f"(gamma_(n-1) max K/gamma - 1)/||E||^2 = {(gam1*kmax/gam-1)/((B-1/n)**2).sum():.6f}, "
              f"n/(2(n-1)) = {n/(2*(n-1)):.6f}")
