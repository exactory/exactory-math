"""Does a near-minimiser of the permanent with a zero have an entrywise lower bound?

The effective-resistance lemma (*) of `removing-condition-N.md` makes condition (N)
automatic at every entry with `a_ij >= Phi`, and the truncation repair for the entries below
`Phi` costs more than (N) itself, so the whole question is whether a near-maximiser can have
a very small positive entry.

Mechanism to test: `per(A) = per(A^0) + a_ij per(A(i|j))` where `A^0` is `A` with the (i,j)
entry set to zero, so `per(A) >= per(A^0)`, and `A^0` has one more zero than `A`.  Extra
zeros raise the minimum permanent on the doubly stochastic polytope, so a small entry should
force the permanent up, which the hypothesis `per <= gamma_n` forbids.

The test minimises the smallest off-`(0,0)` entry over doubly stochastic matrices with
`b_00 = 0` and `per(B) <= (1 + eta) gamma_n`, the same relaxation the sibling attack used for
the spectral gap.  If the minimum stays bounded below by something like `c/n`, the entrywise
bound is real and the route is open; if it goes to zero, the route is dead.
"""
import itertools
import math
import sys

import numpy as np
from scipy.optimize import minimize


def sinkhorn(A, iters=3000, tol=1e-13):
    n = A.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = np.einsum("ij,j->i", A, d2) * d1
        d1 = d1 / r
        c = np.einsum("ij,i->j", A, d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return np.einsum("i,ij,j->ij", d1, A, d2)


def permanent(A):
    n = A.shape[0]
    S = np.zeros((1 << n, n))
    sizes = np.zeros(1 << n, dtype=np.int64)
    idx = np.arange(1 << n)
    for b in range(n):
        has = (idx >> b) & 1 == 1
        S[has] += A[:, b]
        sizes[has] += 1
    return float((np.where((n - sizes) % 2 == 0, 1.0, -1.0) * np.prod(S, axis=1))[1:].sum())


def build(theta, n):
    X = np.exp(theta.reshape(n, n) - theta.max())
    X[0, 0] = 0.0
    return sinkhorn(X)


if __name__ == "__main__":
    eta, penalty = 0.05, 200.0
    rng = np.random.default_rng(4242)
    print(f"{'n':>3} {'min entry found':>16} {'1/n':>8} {'ratio':>7} {'per/gamma':>10} {'starts':>7}")
    for n in [int(a) for a in sys.argv[1:]] or [5, 6, 7, 8]:
        gamma = math.factorial(n) / n ** n

        def f(theta):
            B = build(theta, n)
            off = B[B > 0]
            small = off.min() if off.size else 0.0
            return small + penalty * max(0.0, permanent(B) / gamma - 1 - eta)

        best = (float("inf"), None)
        starts = {5: 80, 6: 60, 7: 40, 8: 20}.get(n, 12)
        for s in range(starts):
            spread = [0.5, 1.5, 3.0, 5.0][s % 4]
            th0 = spread * rng.standard_normal(n * n)
            if s % 3 == 1:                      # drive one entry towards zero
                th0.reshape(n, n)[1, 1] -= 8
            res = minimize(f, th0, method="Nelder-Mead",
                           options={"maxiter": 6000, "xatol": 1e-8, "fatol": 1e-11})
            B = build(res.x, n)
            p = permanent(B) / gamma
            off = B[B > 0]
            if p <= 1 + eta + 1e-6 and off.size and off.min() < best[0]:
                best = (float(off.min()), B, p)
        mn, B, p = best
        print(f"{n:>3} {mn:>16.6e} {1/n:>8.4f} {mn * n:>7.3f} {p:>10.4f} {starts:>7}")
