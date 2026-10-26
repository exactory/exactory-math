"""Route 3 probes (follow-up).  (a) Check the partition formula for P_4(E) numerically.
(b) At n = 7, on the region ||E||_F^2 <= 0.186 forced by Theorem 2 in the application, measure
    r(E) = (per(B)/gamma_n - 1) / ||E||^2, the cubic term, and the k >= 4 remainder, by random
    sampling and by minimising r over the region (Nelder-Mead on Sinkhorn coordinates, rescaled
    onto the ball).  Reports the smallest r found, for scale only (not a proof)."""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(5)


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


def P_k_direct(E, k):
    n = E.shape[0]
    tot = 0.0
    for S in itertools.combinations(range(n), k):
        for T in itertools.combinations(range(n), k):
            tot += permanent(E[np.ix_(S, T)])
    return tot


def P4_formula(E):
    r = (E ** 2).sum(axis=1)
    c = (E ** 2).sum(axis=0)
    F2 = (E ** 2).sum()
    return (36 * (E ** 4).sum() - 18 * (r ** 2).sum() - 18 * (c ** 2).sum() + 3 * F2 ** 2
            + 6 * np.trace((E @ E.T) @ (E @ E.T))) / 24


print("(a) P_4 partition formula vs direct sum of 4x4 subpermanents (zero-margin E):")
for n in (4, 5, 6):
    for t in range(3):
        E = rng.standard_normal((n, n))
        E -= E.mean(axis=0, keepdims=True)
        E -= E.mean(axis=1, keepdims=True)
        d, f = P_k_direct(E, 4), P4_formula(E)
        print(f"   n={n}: direct={d:.10f} formula={f:.10f} ok={abs(d - f) <= 1e-9 * max(1, abs(d))}")
    # P_3 formula too
    E = rng.standard_normal((n, n)); E -= E.mean(axis=0, keepdims=True); E -= E.mean(axis=1, keepdims=True)
    print(f"   n={n}: P_3 direct={P_k_direct(E, 3):.10f}  (2/3) sum e^3={(2/3)*(E**3).sum():.10f}")


def sinkhorn(X, iters=5000, tol=1e-13):
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


n = 7
gam = math.factorial(n) / n ** n
RMAX2 = 2 * n * math.log(math.factorial(n - 2) * ((n - 2) / (n - 1) ** 2) ** (n - 2) / gam)
print(f"\n(b) n = 7, region ||E||^2 <= 2 n log(m_n/gamma_n) = {RMAX2:.4f}")
loc = n / (2 * (n - 1))
a3 = n ** 3 * math.factorial(n - 3) / math.factorial(n)


def stats(B):
    E = B - 1 / n
    e2 = float((E ** 2).sum())
    r = (permanent(B) / gam - 1) / e2
    cubic = a3 * (2 / 3) * (E ** 3).sum() / e2
    return e2, r, cubic, r - loc - cubic


worst = (math.inf, None)
rows = []
for t in range(3000):
    kind = t % 4
    if kind == 0:
        B = sinkhorn(np.exp(rng.uniform(0.05, 0.8) * rng.standard_normal((n, n))))
    elif kind == 1:
        lam = rng.uniform(0, 0.2)
        B = (1 - lam) / n + lam * np.eye(n)[rng.permutation(n)]
    elif kind == 2:   # push toward a zero entry: J/n + t * (T_n - J/n)
        T = np.full((n, n), (n - 2) / (n - 1) ** 2); T[0, :] = 1 / (n - 1); T[:, 0] = 1 / (n - 1); T[0, 0] = 0
        s = rng.uniform(0, 1)
        B = (1 - s) / n + s * T
    else:
        m = rng.integers(2, 4)
        w = rng.dirichlet(np.ones(m) * 3)
        P = sum(w[i] * np.eye(n)[rng.permutation(n)] for i in range(m))
        s = rng.uniform(0, 0.5)
        B = (1 - s) / n + s * P
    e2, r, cubic, rem = stats(B)
    if e2 > RMAX2 or e2 < 1e-8:
        continue
    rows.append((e2, r, cubic, rem))
    if r < worst[0]:
        worst = (r, B.copy())
rows = np.array(rows)
print(f"   samples in region: {len(rows)};  min r = {rows[:,1].min():.4f} (local n/(2(n-1)) = {loc:.4f});"
      f"  min cubic/||E||^2 = {rows[:,2].min():.4f};  k>=4 remainder/||E||^2 in [{rows[:,3].min():.4f}, {rows[:,3].max():.4f}]")


def obj(theta):
    B = sinkhorn(np.exp(np.clip(theta.reshape(n, n), -20, 20)))
    E = B - 1 / n
    e2 = float((E ** 2).sum())
    if e2 < 1e-10:
        return 10.0
    if e2 > RMAX2:               # rescale onto the ball boundary
        B = 1 / n + E * math.sqrt(RMAX2 / e2)
        if B.min() < 0:
            return 10.0
        E = B - 1 / n
        e2 = RMAX2
    return (permanent(B) / gam - 1) / e2


best = (math.inf, None)
for s in range(12):
    th0 = np.log(np.maximum(worst[1], 1e-6)).ravel() + 0.3 * rng.standard_normal(n * n) if s % 2 == 0 \
        else rng.uniform(0.2, 1.5) * rng.standard_normal(n * n)
    res = minimize(obj, th0, method="Nelder-Mead", options={"maxiter": 2500, "xatol": 1e-7, "fatol": 1e-10})
    if res.fun < best[0]:
        best = (res.fun, res.x)
print(f"   minimised r over the region (12 Nelder-Mead runs): {best[0]:.4f}   [1/n = {1/n:.4f}, 1/(2n) = {1/(2*n):.4f}]")
