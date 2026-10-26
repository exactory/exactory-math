"""Explicit radii of the local theorem.

With x = n ||E||_F, the proven lower bound is

  per(B)/gamma_n - 1 >= [ n/(2(n-1)) - 2n/(3(n-1)(n-2)) ] ||E||^2 - sum_{k=4}^n beta_k ||E||^k,

  beta_k = (n^k/(n)_k) Phi-free constant:  CS bound      beta_k = n^k/k!
                                            combined     beta_k = (n^k/(n)_k) min(D_k^2/k!, C(n,k))

(D_k = derangement number).  Q(c) holds whenever the bound is >= c ||E||^2.  For each n the
largest radius rho_n(c) with this property is found by bisection on ||E||, for c = 1/4 and
c = 1/n, with both bounds.  The n = 4 line uses the cubic bound with the exact constant
2n/(3(n-1)(n-2)) = 4/9 as well, so only c < 2/9 is reachable there.
"""
import math

import numpy as np


def derangements(k):
    d = [1, 0]
    for m in range(2, k + 1):
        d.append((m - 1) * (d[m - 1] + d[m - 2]))
    return d[k]


def lower_bound_coeffs(n, kind):
    """Return (quad, [beta_4..beta_n]) so that per/gamma - 1 >= quad*||E||^2 - sum beta_k ||E||^k."""
    quad = n / (2 * (n - 1)) - 2 * n / (3 * (n - 1) * (n - 2))
    betas = []
    for k in range(4, n + 1):
        cs = n ** k / math.factorial(k)
        if kind == "cs":
            betas.append(cs)
        else:
            moebius = (n ** k / math.perm(n, k)) * derangements(k) ** 2 / math.factorial(k)
            betas.append(min(cs, moebius))
    return quad, betas


def holds(n, c, d, kind):
    quad, betas = lower_bound_coeffs(n, kind)
    tail = sum(b * d ** k for b, k in zip(betas, range(4, n + 1)))
    return quad * d * d - tail >= c * d * d


def radius(n, c, kind):
    lo, hi = 0.0, 1.0
    if not holds(n, c, 1e-9, kind):
        return 0.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if holds(n, c, mid, kind):
            lo = mid
        else:
            hi = mid
    return lo


print(f"{'n':>3} {'quad':>8} | {'rho(1/4) CS':>12} {'n*rho':>7} | {'rho(1/4) comb':>14} {'sqrt(n)*rho':>11} | "
      f"{'rho(1/n) CS':>12} | {'rho(1/n) comb':>14}")
for n in [4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 30, 50]:
    quad, _ = lower_bound_coeffs(n, "cs")
    r1, r2 = radius(n, 0.25, "cs"), radius(n, 0.25, "comb")
    r3, r4 = radius(n, 1.0 / n, "cs"), radius(n, 1.0 / n, "comb")
    print(f"{n:>3} {quad:8.4f} | {r1:12.5f} {n*r1:7.3f} | {r2:14.5f} {math.sqrt(n)*r2:11.3f} | "
          f"{r3:12.5f} | {r4:14.5f}")
