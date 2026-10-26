"""Profile of the quadratic van der Waerden ratio along the distance from the centre.

For each n, minimise  rho(B) = (per(B)/gamma_n - 1)/||E||_F^2  (E = B - J/n) over the Birkhoff
polytope and report, at the minimiser, ||E||_F^2, the entry range of nB, and the Taylor
coefficients alpha_k = r_k(F)/(n)_k of f(t)/gamma_n = per(J/n + tE)/gamma_n (F = nE), so that
the orders that fight the quadratic term can be seen.

Then, for a grid of radii, minimise  per(B)/gamma_n - 1 - ||E||^2/4  subject to ||E||^2 >= r^2
(penalty method) to see how much room the far region has at c = 1/4.
"""
import math
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(3)


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


def sinkhorn(X, iters=3000, tol=1e-13):
    d1, d2 = np.ones(X.shape[0]), np.ones(X.shape[0])
    B = X
    for _ in range(iters):
        d1 = 1.0 / (X @ d2)
        d2 = 1.0 / (X.T @ d1)
        B = d1[:, None] * X * d2[None, :]
        if abs(B.sum(0) - 1).max() < tol and abs(B.sum(1) - 1).max() < tol:
            break
    return B


def param(x, n):
    return sinkhorn(np.exp(np.clip(x.reshape(n, n), -30, 30)))


def taylor_coefficients(B):
    """alpha_k, k = 0..n, of per(J/n + tE)/gamma_n, by interpolation at n+1 points."""
    n = B.shape[0]
    gamma = math.factorial(n) / n ** n
    E = B - 1.0 / n
    ts = np.linspace(-1.0, 1.0, n + 1)
    vals = np.array([permanent(1.0 / n + t * E) / gamma for t in ts])
    V = np.vander(ts, n + 1, increasing=True)
    return np.linalg.solve(V, vals)


def ratio(B):
    n = B.shape[0]
    gamma = math.factorial(n) / n ** n
    d2 = ((B - 1.0 / n) ** 2).sum()
    if d2 < 1e-14:
        return 1e3
    return (permanent(B) / gamma - 1) / d2


def search(n, objective, n_random, n_starts, maxiter):
    best, best_B = math.inf, None
    for _ in range(n_random):
        B = sinkhorn(rng.random((n, n)) ** rng.integers(1, 8))
        v = objective(B)
        if v < best:
            best, best_B = v, B
    for start in range(n_starts):
        spread = [0.5, 1.0, 2.0, 4.0][start % 4]
        x0 = spread * rng.standard_normal(n * n)
        res = minimize(lambda x: objective(param(x, n)), x0, method="Nelder-Mead",
                       options={"maxiter": maxiter, "xatol": 1e-9, "fatol": 1e-12})
        if res.fun < best:
            best, best_B = res.fun, param(res.x, n)
    return best, best_B


ns = [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6, 7, 8]
for n in ns:
    maxiter = {3: 2000, 4: 2000, 5: 1500, 6: 1000, 7: 600, 8: 300}.get(n, 300)
    best, B = search(n, ratio, n_random=100, n_starts=4, maxiter=maxiter)
    E = B - 1.0 / n
    a = taylor_coefficients(B)
    d2 = (E ** 2).sum()
    print(f"n={n}: c*(n) ~ {best:.6f}; ||E||^2 = {d2:.5f} (max n-1 = {n-1}); "
          f"nB in [{(n*B).min():.3f}, {(n*B).max():.3f}]; zeros = {(B < 1e-6).sum()}")
    print("      alpha_k/||E||^2 for k=2..n: " +
          ", ".join(f"{a[k]/d2:+.4f}" for k in range(2, n + 1)) +
          f";  local n/(2(n-1)) = {n/(2*(n-1)):.4f}")
    print("      cumulative sum_{k<=m} alpha_k/||E||^2: " +
          ", ".join(f"{a[2:m+1].sum()/d2:+.4f}" for m in range(2, n + 1)))

print("\nFar region at c = 1/4: min of per/gamma - 1 - ||E||^2/4 subject to ||E||^2 >= r^2")
for n in [m for m in ns if m <= 7]:
    gamma = math.factorial(n) / n ** n
    line = []
    for r2 in [0.05, 0.1, 0.2, 0.35, 0.5, 0.75, 1.0, 1.5, 2.0]:
        if r2 > n - 1:
            continue

        def obj(x, n=n, r2=r2):
            B = param(x, n)
            d2 = ((B - 1.0 / n) ** 2).sum()
            pen = 1e3 * max(0.0, r2 - d2) ** 2
            return permanent(B) / gamma - 1 - d2 / 4 + pen

        best = math.inf
        for start in range(6):
            x0 = [0.5, 1.0, 2.0][start % 3] * rng.standard_normal(n * n)
            res = minimize(obj, x0, method="Nelder-Mead",
                           options={"maxiter": 1500, "xatol": 1e-9, "fatol": 1e-12})
            best = min(best, res.fun)
        line.append(f"r^2={r2}: {best:+.4f}")
    print(f"  n={n}: " + "; ".join(line))
