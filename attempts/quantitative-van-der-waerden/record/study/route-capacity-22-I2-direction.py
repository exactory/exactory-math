"""Is I2  C_2(v,v') K(v+v') >= g(n) g(n-1) exp(a' (d + d'))  true, and for which a'?
Pairs (v, v') are sampled directly (any pair of probability vectors with v + v' <= 1 is a column pair
of some doubly stochastic matrix).  Three families:
  (T) the tight direction v = 1/n + e, v' = 1/n - e  (w uniform, K = K(2/n) exactly), e random and extreme;
  (R) the n = 7 application region: d, d' <= 0.0266;
  (G) global: Dirichlet pairs at several concentrations, sparse pairs, and pairs from random matrices.
Prints min over samples of C_2 K / (gg exp(a'(d + d'))) for a' in {0.5, 0.45, 0.4, 0.36}.
"""
import math
import sys

import numpy as np
from scipy.optimize import minimize


def K(w):
    return float(np.prod([(1 - t) ** (1 - t) if t < 1 else 1.0 for t in w]))


def g(k):
    return ((k - 1) / k) ** (k - 1)


def C2(v, vp):
    w = v + vp
    n = len(v)
    off = np.ones((n, n)) - np.eye(n)

    def f(u):
        u = np.clip(u - u.mean(), -25, 25)
        y = np.exp(u)
        M = (v * y)[:, None] * (vp * y)[None, :] * off
        P = float(M.sum())
        dP = M.sum(axis=1) + M.sum(axis=0)
        return math.log(P) - float(w @ u), dP / P - w
    best = math.inf
    rng = np.random.default_rng(0)
    for s in range(3):
        u0 = np.zeros(n) if s == 0 else 0.5 * rng.standard_normal(n)
        res = minimize(f, u0, jac=True, method="BFGS", options={"gtol": 1e-12, "maxiter": 5000})
        best = min(best, res.fun)
    return math.exp(best)


rng = np.random.default_rng(22)
APRIMES = [0.5, 0.45, 0.4, 0.36]
for n in [int(a) for a in sys.argv[1:]] or [4, 5, 6, 7]:
    gg = g(n) * g(n - 1)
    fams = {"T": [], "R": [], "G": []}
    # (T) tight direction
    for t in range(300):
        if t % 3 == 0:
            e = rng.uniform(-1, 1, n)
        elif t % 3 == 1:
            e = rng.choice([-1.0, 1.0, 0.0], n)
        else:
            e = rng.standard_normal(n)
        e -= e.mean()
        if abs(e).max() < 1e-12:
            continue
        e = e / abs(e).max() * (1 / n) * rng.uniform(0.05, 1.0)   # entries within [-1/n, 1/n]
        fams["T"].append((1 / n + e, 1 / n - e))
    # (R) region
    for t in range(300):
        while True:
            a = rng.uniform(-1, 1, n); a -= a.mean(); b = rng.uniform(-1, 1, n); b -= b.mean()
            a *= rng.uniform(0, 0.163) / np.linalg.norm(a); b *= rng.uniform(0, 0.163) / np.linalg.norm(b)
            v, vp = 1 / n + a, 1 / n + b
            if v.min() >= 0 and vp.min() >= 0 and (v + vp).max() <= 1:
                break
        fams["R"].append((v, vp))
    # (G) global
    for t in range(300):
        conc = [0.2, 0.5, 1.0, 3.0][t % 4]
        v = rng.dirichlet(np.full(n, conc)); vp = rng.dirichlet(np.full(n, conc))
        if (v + vp).max() > 1:
            continue
        fams["G"].append((v, vp))
    for t in range(100):   # sparse pairs
        k1, k2 = rng.integers(2, n + 1), rng.integers(2, n + 1)
        v = np.zeros(n); vp = np.zeros(n)
        v[rng.choice(n, k1, replace=False)] = 1 / k1
        vp[rng.choice(n, k2, replace=False)] = 1 / k2
        if (v + vp).max() <= 1:
            fams["G"].append((v, vp))
    out = []
    for name, pairs in fams.items():
        mins = {a: math.inf for a in APRIMES}
        arg = None
        for v, vp in pairs:
            d, dp = float(((v - 1 / n) ** 2).sum()), float(((vp - 1 / n) ** 2).sum())
            val = C2(v, vp) * K(v + vp) / gg
            for a in APRIMES:
                r = val / math.exp(a * (d + dp))
                if r < mins[a]:
                    mins[a] = r
                    if a == 0.5:
                        arg = (v, vp, d, dp)
        out.append(f"   {name} ({len(pairs)} pairs): " + "  ".join(f"a'={a}: {mins[a]:.6f}" for a in APRIMES))
        if name == "T":
            v, vp, d, dp = arg
            out.append(f"      worst T pair at a'=0.5: d={d:.4f}, v={np.round(v,3)}")
    print(f"n={n}:")
    print("\n".join(out))
