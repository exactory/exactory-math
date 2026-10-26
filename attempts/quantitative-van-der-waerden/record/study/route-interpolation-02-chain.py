"""Test the monotone chain  q_1 <= q_2 <= ... <= q_n  on the Birkhoff polytope.

q_k = Sigma_k(B)/Sigma_k(J/n) is the normalised sum of k x k subpermanents (q_1 = 1,
q_n = per(B)/gamma_n).  The Bernstein form f(t) = gamma_n sum_k C(n,k) q_k t^k (1-t)^(n-k)
gives f'(t) = n gamma_n sum_k C(n-1,k) (q_{k+1} - q_k) t^k (1-t)^(n-1-k), so the chain says
the Bernstein coefficients of f' are nonnegative; the single step k = n-1 is

    per(B) >= mean_{i,j} per(B(i|j)),   i.e.  f'(1) = <B - J/n, grad per(B)> >= 0.

Part A (cheap, n = 3..7): minimise  f'(1)/(n gamma_n (q_2 - 1))  =  (q_n - q_{n-1})/(q_2 - q_1)
by multistart Nelder-Mead; a negative value is a counterexample to the last step.
Part B (n = 3, 4): minimise the smallest normalised step over all k.
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(2)


def permanent(A):
    n = A.shape[0]
    if n == 0:
        return 1.0
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


def minors(B):
    n = B.shape[0]
    M = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            M[i, j] = permanent(np.delete(np.delete(B, i, 0), j, 1))
    return M


def last_step_ratio(B):
    """(q_n - q_{n-1})/(q_2 - q_1) = f'(1) / (n gamma_n ||E||^2/(n-1)^2)."""
    n = B.shape[0]
    E = B - 1.0 / n
    d2 = (E ** 2).sum()
    if d2 < 1e-14:
        return 1e3
    gamma = math.factorial(n) / n ** n
    fp1 = (E * minors(B)).sum()
    return fp1 / (n * gamma * d2 / (n - 1) ** 2)


def q_sequence(B):
    n = B.shape[0]
    q = []
    for k in range(n + 1):
        Sig = sum(permanent(B[np.ix_(S, T)])
                  for S in itertools.combinations(range(n), k)
                  for T in itertools.combinations(range(n), k))
        q.append(Sig / (math.comb(n, k) ** 2 * math.factorial(k) / n ** k))
    return np.array(q)


def min_step_ratio(B):
    q = q_sequence(B)
    d = np.diff(q)
    if d[1] < 1e-14:
        return 1e3
    return (d[2:] / d[1]).min()


def random_ds(n):
    if rng.random() < 0.5:
        return sinkhorn(rng.random((n, n)) ** rng.integers(1, 8))
    k = rng.integers(2, 4)
    B = np.zeros((n, n))
    w = rng.dirichlet(np.ones(k))
    for a in range(k):
        B[np.arange(n), rng.permutation(n)] += w[a]
    return B


def search(n, objective, n_random, n_starts, maxiter):
    best, best_B = math.inf, None
    for _ in range(n_random):
        B = random_ds(n)
        v = objective(B)
        if v < best:
            best, best_B = v, B
    for start in range(n_starts):
        spread = [0.5, 2.0, 4.0][start % 3]
        x0 = spread * rng.standard_normal(n * n)
        res = minimize(lambda x: objective(param(x, n)), x0, method="Nelder-Mead",
                       options={"maxiter": maxiter, "xatol": 1e-8, "fatol": 1e-11})
        if res.fun < best:
            best, best_B = res.fun, param(res.x, n)
    return best, best_B


ns = [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6, 7]
print("Part A: last step  (q_n - q_(n-1))/(q_2 - q_1)  [negative = counterexample to f'(1) >= 0]")
for n in ns:
    best, B = search(n, last_step_ratio, n_random=400, n_starts=9,
                     maxiter={3: 2000, 4: 2000, 5: 1500, 6: 800, 7: 300}.get(n, 300))
    print(f"  n={n}: min = {best:+.6f}   at n*B =")
    print("    " + np.array2string(n * B, precision=3, suppress_small=True).replace("\n", "\n    "))

print("Part B: smallest step over all k, (q_(k+1) - q_k)/(q_2 - q_1)")
for n in [m for m in ns if m <= 4]:
    best, B = search(n, min_step_ratio, n_random=200, n_starts=6, maxiter=800)
    q = q_sequence(B)
    print(f"  n={n}: min = {best:+.6f};  q at minimiser = {np.array2string(q, precision=5)}")
    print("    " + np.array2string(n * B, precision=3, suppress_small=True).replace("\n", "\n    "))
