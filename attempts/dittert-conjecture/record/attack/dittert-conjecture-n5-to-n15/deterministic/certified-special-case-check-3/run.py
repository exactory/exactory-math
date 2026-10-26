"""Certified special-case check 3: the exact status of the published boundary-exclusion
inequality in every dimension 4 <= n <= 17.

Kafidov's argument (arXiv:2607.19439) proves Dittert's conjecture at n whenever

    K_n := m_n - gamma_n - n^3 m_n^2 / (4 (1 - gamma_n)) > 0,

gamma_n = n!/n^n, m_n = (n-2)! ((n-2)/(n-1)^2)^(n-2), and every other step of that
argument is dimension-free for n > 3 (the Knopp-Sinkhorn value m_n needs n > 3 and
t < 1 needs n gamma_n/(1 - gamma_n) < 1, which holds for n >= 4 as checked here).
This run evaluates K_n exactly over Q (Python fractions) and records the sign and
the ratio r_n = (m_n - gamma_n) / (n^3 m_n^2/(4(1-gamma_n))) for 4 <= n <= 17.
"""
import json
from fractions import Fraction as Fr
from math import factorial

out = {}
for n in range(4, 18):
    g = Fr(factorial(n), n ** n)
    m = Fr(factorial(n - 2)) * Fr(n - 2, (n - 1) ** 2) ** (n - 2)
    lhs = m - g
    rhs = Fr(n ** 3) * m * m / (4 * (1 - g))
    K = lhs - rhs
    t2 = n * g / (1 - g)
    out[n] = {"gamma_n": str(g), "m_n": str(m), "K_n": str(K), "K_n_sign": "positive" if K > 0 else "not positive",
              "ratio": str(lhs / rhs), "ratio_float": float(lhs / rhs), "t_below_one": bool(t2 < 1)}
    print(f"n={n:2d}: ratio = {float(lhs / rhs):.6f}  K_n {'> 0' if K > 0 else '<= 0'}  t<1: {t2 < 1}")
json.dump(out, open("kafidov-threshold.json", "w"), indent=1)
