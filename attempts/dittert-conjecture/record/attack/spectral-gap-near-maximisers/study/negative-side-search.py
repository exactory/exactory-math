"""Is the counterexample space of G(n, c_n) empty where it matters?

The first version of this script searched the wrong domain.  Dittert's functional lives on
`K_n`, the non-negative matrices of total sum `n`, not on the doubly stochastic polytope, so a
segment between two doubly stochastic matrices says nothing about it.  The correct negative-side
question, and a structural fact that comes with it, are these.

**The set G(n, c_n) quantifies over is conjecturally empty.**  Its hypothesis is
`A in K_n`, `A` has a zero entry, and `phi(A) >= 2 - gamma_n`.  Dittert's conjecture says
`phi(A) <= 2 - gamma_n` on `K_n` with equality only at `J_n/n`, which has no zero.  So the
hypothesis set of G(n, c_n) is exactly the set of counterexamples to Dittert's conjecture at `n`.
G is therefore vacuous once Dittert is known, and Theorem R uses it in the only way it can be
used: as the hypothesis of a proof by contradiction.  Any search for a counterexample to G is a
search for a counterexample to Dittert's conjecture itself.

That makes the useful experiment the *contrapositive* one, and it is a genuine test:

    maximise  phi(A)   over  A in K_n  with a zero entry  and  lambda_2(A) <= c_n.

If the maximum sits below `2 - gamma_n` by a clear margin, then no matrix with a small spectral
gap comes anywhere near the Dittert ceiling, which is what G(n, c_n) asserts, checked on the
region where it is actually needed.  If the maximum reaches the ceiling, G is refuted at that
`n` and Theorem R's route is dead as stated.

`lambda_2(A) = 1 - sigma_2(D_r^{-1/2} A D_c^{-1/2})` with `D_r`, `D_c` the row and column sum
diagonals, as in Theorem R.
"""
import math
import sys

import numpy as np
from scipy.optimize import minimize


def permanent(A):
    """Ryser, vectorised over all 2^n column subsets."""
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


def lam2(A):
    r, c = A.sum(1), A.sum(0)
    M = np.einsum("i,ij,j->ij", 1 / np.sqrt(r), A, 1 / np.sqrt(c))
    return 1.0 - float(np.linalg.svd(M, compute_uv=False)[1])


def phi(A):
    return float(np.prod(A.sum(1)) + np.prod(A.sum(0)) - permanent(A))


def build(theta, n):
    X = np.exp(np.clip(theta.reshape(n, n), -60, 60))
    X[0, 0] = 0.0
    return X * (n / X.sum())


def c_of(n):
    g = math.factorial(n) / n ** n
    h = math.sqrt(2 * g)
    theta = 1 - 2 * h / 3
    kap = 1 / ((1 - g) * theta)
    return 2 * math.sqrt(g * kap) / theta, g


if __name__ == "__main__":
    ns = [int(a) for a in sys.argv[1:]] or [5, 6, 7, 8]
    penalty = 50.0
    rng = np.random.default_rng(20260904)
    print(f"{'n':>3} {'c_n':>8} {'ceiling 2-gamma_n':>18} {'max phi, lam2<=c_n':>20} "
          f"{'shortfall':>11} {'lam2 there':>11} {'starts':>7}", flush=True)
    for n in ns:
        c_n, g = c_of(n)
        ceiling = 2 - g

        def neg(theta):
            A = build(theta, n)
            return -(phi(A) - penalty * max(0.0, lam2(A) - c_n))

        best = (-math.inf, None)
        starts = {5: 40, 6: 32, 7: 24, 8: 18, 9: 14, 10: 10}.get(n, 8)
        for s in range(starts):
            spread = [0.2, 0.8, 2.0, 4.0][s % 4]
            th0 = spread * rng.standard_normal(n * n)
            if s % 4 == 3:                       # start near a decomposable matrix
                k = 1 + s % (n // 2 or 1)
                th0 = np.full((n, n), -6.0)
                th0[:k, :k] = 0.0
                th0[k:, k:] = 0.0
                th0 = th0.ravel() + 0.1 * rng.standard_normal(n * n)
            res = minimize(neg, th0, method="L-BFGS-B",
                           options={"maxiter": 900, "maxfun": 40000})
            A = build(res.x, n)
            if lam2(A) <= c_n + 1e-9 and phi(A) > best[0]:
                best = (phi(A), A)
        p, A = best
        if A is None:
            print(f"{n:>3} {c_n:>8.4f} {ceiling:>18.10f} {'no feasible point':>20} "
                  f"{'':>11} {'':>11} {starts:>7}", flush=True)
            continue
        print(f"{n:>3} {c_n:>8.4f} {ceiling:>18.10f} {p:>20.10f} "
              f"{ceiling - p:>11.3e} {lam2(A):>11.4f} {starts:>7}", flush=True)
    print("\nA shortfall that stays positive is G(n, c_n) holding on the region it is needed:")
    print("no matrix with a zero and a spectral gap below c_n comes near the Dittert ceiling.")
