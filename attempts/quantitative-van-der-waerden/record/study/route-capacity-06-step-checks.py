"""Step-by-step checks of every algebraic claim used in route-capacity.md.

(i)   Lemma A chain, pointwise at random x:  q(x) >= prod_s a_s^(1-v_s) >= K(v) prod_j x_j.
(ii)  Taylor bound:  K(v) >= g(n) exp(||v - 1/n||^2 / 2) for random v in the simplex, and phi'' = 1/(1-t).
(iii) Symbolic identity (sympy, n = 3, 4):  q_{n-1} = sum_r v_r prod_{s != r} l_s(x), and its coefficient of
      x_1...x_{n-1} equals per(B); also q_{n-m}(x) = prod_s a_s * P_V(1/a) for m = 2.
(iv)  Lemma A_m identity and second AM-GM, pointwise, m = 2, 3 at random x and random doubly stochastic B.
(v)   Application with the exp form ||E||^2 <= 2 n K (K = -log cap(A)), against (e^K - 1)/c with c = 1/(2n).
"""
import itertools
import math

import numpy as np
import sympy as sp

rng = np.random.default_rng(3)


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


def K(w):
    return float(np.prod([(1 - t) ** (1 - t) if t < 1 else 1.0 for t in w]))


def g(k):
    return ((k - 1) / k) ** (k - 1)


def permanent(A):
    n = A.shape[0]
    return sum(math.prod(A[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n)))


print("(i) Lemma A chain pointwise")
worst1 = worst2 = math.inf
for t in range(2000):
    n = rng.integers(2, 8)
    B = sinkhorn(np.exp(rng.uniform(0.2, 3.0) * rng.standard_normal((n, n))))
    if rng.uniform() < 0.3:      # sparse
        m = rng.integers(2, 4)
        wts = rng.dirichlet(np.ones(m))
        B = sum(wts[i] * np.eye(n)[rng.permutation(n)] for i in range(m))
    v, Bp = B[:, -1], B[:, :-1]
    x = np.exp(rng.uniform(0.5, 3.0) * rng.standard_normal(n - 1))
    a = Bp @ x
    if (a <= 0).any():
        continue
    q = sum(v[r] * np.prod(np.delete(a, r)) for r in range(n))
    mid = float(np.prod(a ** (1 - v)))
    worst1 = min(worst1, q / mid)
    worst2 = min(worst2, mid / (K(v) * np.prod(x)))
print(f"   min q / prod a^(1-v) = {worst1:.12f}   min prod a^(1-v) / (K prod x) = {worst2:.12f}   [both >= 1]")

print("(ii) Taylor bound K(v) >= g(n) exp(||v-1/n||^2/2)")
worst = math.inf
for t in range(20000):
    n = rng.integers(2, 12)
    v = rng.dirichlet(np.full(n, rng.choice([0.05, 0.3, 1.0, 5.0])))
    worst = min(worst, K(v) / (g(n) * math.exp(((v - 1 / n) ** 2).sum() / 2)))
print(f"   min K / (g e^(d/2)) = {worst:.12f}   [>= 1]")
tt = sp.symbols("t")
phi = (1 - tt) * sp.log(1 - tt)
print(f"   phi''(t) = {sp.simplify(sp.diff(phi, tt, 2))}")

print("(iii) symbolic identities")
for n in (3, 4):
    X = sp.symbols(f"x1:{n+1}")
    Bs = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"b{i}{j}"))
    p = sp.prod([sum(Bs[i, j] * X[j] for j in range(n)) for i in range(n)])
    q = sp.diff(p, X[n - 1]).subs(X[n - 1], 0)
    ell = [sum(Bs[s, j] * X[j] for j in range(n - 1)) for s in range(n)]
    q_formula = sum(Bs[r, n - 1] * sp.prod([ell[s] for s in range(n) if s != r]) for r in range(n))
    coeff = sp.Poly(sp.expand(q), *X[: n - 1]).coeff_monomial(sp.prod(X[: n - 1]))
    per = sum(sp.prod([Bs[i, s[i]] for i in range(n)]) for s in itertools.permutations(range(n)))
    print(f"   n={n}: q_(n-1) formula ok: {sp.expand(q - q_formula) == 0};  coeff of x1..x(n-1) == per(B): {sp.expand(coeff - per) == 0}")
    if n == 4:
        q2 = sp.diff(q, X[n - 2]).subs(X[n - 2], 0)
        ell2 = [sum(Bs[s, j] * X[j] for j in range(n - 2)) for s in range(n)]
        V = Bs[:, n - 2:]
        PV = sum(sp.prod([V[s, sig[k]] for k, s in enumerate(S)]) for S in itertools.combinations(range(n), 2)
                 for sig in itertools.permutations(range(2))) if False else None
        # P_V(y) = sum_{|S|=2} per(V[S,:]) y^S ; q_2 should equal prod_s ell2_s * P_V(1/ell2)
        y = [1 / e for e in ell2]
        PVy = sum(sp.Matrix([[V[s, 0], V[s, 1]] for s in S]).per() * y[S[0]] * y[S[1]]
                  for S in itertools.combinations(range(n), 2))
        ident = sp.simplify(q2 - sp.prod(ell2) * PVy)
        print(f"   n=4, m=2: q_(n-2) = prod a_s * P_V(1/a): {ident == 0}")

print("(iv) Lemma A_m pieces pointwise, m = 2, 3")
for m in (2, 3):
    worst = math.inf
    for t in range(1500):
        n = rng.integers(m + 1, 8)
        B = sinkhorn(np.exp(rng.uniform(0.2, 3.0) * rng.standard_normal((n, n))))
        V, Bp = B[:, n - m:], B[:, : n - m]
        w = V.sum(axis=1)
        x = np.exp(rng.uniform(0.5, 3.0) * rng.standard_normal(n - m))
        a = Bp @ x
        # q_{n-m}(x) = sum_{|S|=m} per(V[S,:]) prod_{s not in S} a_s ; identity with prod a * P_V(1/a)
        q = sum(permanent(V[list(S), :]) * np.prod(np.delete(a, list(S))) for S in itertools.combinations(range(n), m))
        PV = sum(permanent(V[list(S), :]) * np.prod(1 / a[list(S)]) for S in itertools.combinations(range(n), m))
        assert abs(q - np.prod(a) * PV) <= 1e-9 * abs(q), (q, np.prod(a) * PV)
        worst = min(worst, float(np.prod(a ** (1 - w))) / (K(w) * np.prod(x)))
    print(f"   m={m}: identity q = prod a * P_V(1/a) ok; min prod a^(1-w) / (K(w) prod x) = {worst:.12f}  [>= 1]")

print("(v) application: ||E||^2 <= 2 n K (exp form) vs (e^K - 1)/c, c = 1/(2n)")
import sys
sys.path.insert(0, ".")
import application  # noqa: E402


def fixed_point_exp(n, iters=400):
    gam, m, th, kap = application.constants(n)
    Kb = gam * kap / th
    for _ in range(iters):
        d2 = 2 * n * Kb
        if d2 >= 1.0:
            return None, None
        lam = 1 - math.sqrt(d2)
        K_new = gam * kap / (th * lam)
        if abs(K_new - Kb) < 1e-15:
            Kb = K_new
            break
        Kb = K_new
    return Kb, 1 - math.sqrt(2 * n * Kb)


print(f"{'n':>3} {'K (exp form)':>13} {'margin':>8} {'K ((e^K-1)/c)':>15} {'margin':>8} {'|alpha+beta|':>13}")
for n in range(6, 16):
    gam, m, th, kap = application.constants(n)
    need = math.log(m / gam)
    K1, lam1 = fixed_point_exp(n)
    K2, lam2 = application.fixed_point(n, 1 / (2 * n))
    s1 = f"{K1:.4e} {need/K1:>7.2f}x" if K1 else "none"
    s2 = f"{K2:.4e} {need/K2:>7.2f}x" if K2 else "none"
    ab = math.sqrt(2) * math.sqrt(2 * gam * kap) / (th * lam1) if K1 else float('nan')
    print(f"{n:>3} {s1:>22} {s2:>24} {ab:>13.4f}")
