"""Two checks.

(A) The n = 3 identity behind the sharp proof of Q(1/4):

    per(B)/gamma_3 - 1 - ||E||_F^2/4  =  sum over rows b of  (1 - 4 e_2(b) + 9 e_3(b)),

and 1 - 4 e_2 + 9 e_3 >= 0 on the simplex is Schur's inequality (degree 1).  Both sides are
compared on random 3 x 3 doubly stochastic matrices and on (I + C_3)/2, and the minimum of the
Schur form over the simplex is confirmed to be 0.

(B) Size of the Taylor coefficients alpha_k of per(J/n + tE)/gamma_n relative to ||E||^k:
the largest value of |alpha_k| / ||E||_F^k over random and structured B, for n = 4..8, to see
whether a bound |alpha_k| <= C^k ||E||^k with C independent of n is plausible.  Coefficients
are obtained by interpolating the degree-n polynomial at Chebyshev nodes.
"""
import math

import numpy as np

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


def random_ds(n):
    r = rng.random()
    if r < 0.4:
        return sinkhorn(rng.random((n, n)) ** rng.integers(1, 10))
    if r < 0.7:
        k = rng.integers(2, 5)
        B = np.zeros((n, n))
        w = rng.dirichlet(np.ones(k))
        for a in range(k):
            B[np.arange(n), rng.permutation(n)] += w[a]
        return B
    # near the centre: J/n + small multiple of a random zero-margin direction
    X = rng.standard_normal((n, n))
    X -= X.mean(0, keepdims=True)
    X -= X.mean(1, keepdims=True)
    s = rng.random() * (1.0 / n) / abs(X).max()
    return 1.0 / n + s * X


def e2e3(b):
    x, y, z = b
    return x * y + y * z + z * x, x * y * z


print("(A) n = 3 identity and Schur form")
worst = 0.0
gamma3 = 2.0 / 9.0
for _ in range(2000):
    B = random_ds(3)
    E = B - 1.0 / 3.0
    lhs = permanent(B) / gamma3 - 1 - (E ** 2).sum() / 4
    rhs = sum(1 - 4 * e2e3(B[i])[0] + 9 * e2e3(B[i])[1] for i in range(3))
    worst = max(worst, abs(lhs - rhs))
print(f"    max |lhs - rhs| over 2000 random B: {worst:.2e}")
C3 = np.roll(np.eye(3), 1, axis=1)
B = (np.eye(3) + C3) / 2
E = B - 1.0 / 3.0
print(f"    at (I+C_3)/2: per/gamma - 1 - ||E||^2/4 = {permanent(B)/gamma3 - 1 - (E**2).sum()/4:.2e}")
smin = min(1 - 4 * e2e3(b)[0] + 9 * e2e3(b)[1] for b in rng.dirichlet(np.ones(3), 200000))
print(f"    min of 1 - 4e_2 + 9e_3 over 200000 random simplex points: {smin:.2e} (Schur: >= 0)")

print("(B) max |alpha_k| / ||E||^k")
for n in (4, 5, 6, 7, 8):
    gamma = math.factorial(n) / n ** n
    nodes = np.cos(np.pi * (2 * np.arange(n + 1) + 1) / (2 * (n + 1)))  # Chebyshev on [-1,1]
    V = np.vander(nodes, n + 1, increasing=True)
    worst = np.zeros(n + 1)
    worst_neg = np.zeros(n + 1)
    for trial in range(400):
        B = random_ds(n)
        E = B - 1.0 / n
        d = math.sqrt((E ** 2).sum())
        if d < 1e-8:
            continue
        vals = np.array([permanent(1.0 / n + t * E) / gamma for t in nodes])
        alpha = np.linalg.solve(V, vals)
        for k in range(2, n + 1):
            worst[k] = max(worst[k], abs(alpha[k]) / d ** k)
            worst_neg[k] = min(worst_neg[k], alpha[k] / d ** k)
    print(f"  n={n}: max|alpha_k|/||E||^k, k=2..n: " + ", ".join(f"{worst[k]:.3f}" for k in range(2, n + 1)))
    print(f"        most negative alpha_k/||E||^k:  " + ", ".join(f"{worst_neg[k]:+.3f}" for k in range(2, n + 1)))
