"""Exact check of the Kafidov (arXiv:2607.19439) boundary-exclusion inequality at each n.

Kafidov's proof for n=16 is dimension-generic except for the final numeric
inequality (4.3):  m_n - gamma_n - n^3 m_n^2 / (4 (1 - gamma_n)) > 0,
where gamma_n = n!/n^n and m_n = (n-2)! ((n-2)/(n-1)^2)^(n-2) (Knopp-Sinkhorn).
This script evaluates that inequality exactly over Q for n = 4..17, and also
the sharper form without Bernoulli:  min over x in (0, sqrt(gamma_n)] of
  F(x) = m_n (1 - t)^n - (gamma_n - x^2),  t = x sqrt(n/(1-x^2)),
evaluated in 60-digit floating point (mpmath) as evidence only.
"""
from fractions import Fraction as Fr
from math import factorial
import mpmath as mp
mp.mp.dps = 60

def gamma(n): return Fr(factorial(n), n**n)
def m(n):
    return Fr(factorial(n-2)) * Fr(n-2, (n-1)**2)**(n-2)

print(f"{'n':>2} {'gamma_n':>14} {'m_n':>14} {'(m-g)/g':>10} {'ratio=(m-g)/(n^3 m^2/(4(1-g)))':>32} exact?")
for n in range(4, 18):
    g, mm = gamma(n), m(n)
    lhs = mm - g
    rhs = Fr(n**3) * mm * mm / (4 * (1 - g))
    ratio = lhs / rhs
    print(f"{n:>2} {float(g):>14.6e} {float(mm):>14.6e} {float(lhs/g):>10.3e} {float(ratio):>32.6f} {'PASS' if lhs > rhs else 'fail'}")

print("\nSharper form (no Bernoulli), min of F(x) over 0<x<=sqrt(gamma), relative to gamma:")
for n in range(4, 18):
    g, mm = mp.mpf(factorial(n))/mp.mpf(n)**n, mp.mpf(factorial(n-2))*(mp.mpf(n-2)/mp.mpf((n-1)**2))**(n-2)
    def F(x):
        t = x*mp.sqrt(mp.mpf(n)/(1-x*x))
        return mm*(1-t)**n - (g - x*x)
    xs = [mp.sqrt(g)*mp.mpf(k)/4000 for k in range(1, 4001)]
    vals = [F(x) for x in xs]
    i = min(range(len(vals)), key=lambda k: vals[k])
    print(f"{n:>2} minF/gamma = {mp.nstr(vals[i]/g, 8):>14}  at delta/gamma = {mp.nstr(xs[i]**2/g, 5)}   {'PASS' if vals[i] > 0 else 'fail'}")
