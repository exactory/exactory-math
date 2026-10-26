"""Budget for the drop lemma on the n = 7 region (d, d' <= 0.0266).

For pairs (v, v'):  h_s = 2 v_s v'_s / w_s (harmonic mean, 0 if w_s = 0), hbar = <v, v'>,
Var_w(h) = sum_s w_s (h_s - hbar)^2,  drop = log(1 - hbar) - log C_2 >= 0,
tau* = log y* centred (sum = 0), y* the minimiser of P(y)/y^w with <v, y> = 1.
Reports max drop / Var_w(h), max |tau*|_inf, the margin of (I2) at a' = 0.36 and 0.5, and the
size of each term.  Also the two scalars t* = <v', y*>, p* = 1 - <rho*, rho'*> against (1, 1 - hbar).
"""
import math
import sys

import numpy as np
from scipy.optimize import minimize


def K(w):
    return float(np.prod([(1 - t) ** (1 - t) if t < 1 else 1.0 for t in w]))


def g(k):
    return ((k - 1) / k) ** (k - 1)


def solve(v, vp):
    """Return (C_2, y*) with <v, y*> = 1."""
    w = v + vp
    n = len(v)
    off = np.ones((n, n)) - np.eye(n)

    def f(u):
        y = np.exp(u)
        M = (v * y)[:, None] * (vp * y)[None, :] * off
        P = float(M.sum())
        dP = M.sum(axis=1) + M.sum(axis=0)
        return math.log(P) - float(w @ u), dP / P - w
    best = (math.inf, None)
    rng = np.random.default_rng(0)
    for s in range(1):
        u0 = np.zeros(n)
        res = minimize(f, u0, jac=True, method="BFGS", options={"gtol": 1e-13, "maxiter": 5000})
        if res.fun < best[0]:
            best = (res.fun, res.x)
    y = np.exp(best[1])
    y = y / float(v @ y)
    return math.exp(best[0]), y


n = 7
gg = g(n) * g(n - 1)
rng = np.random.default_rng(31)
rows = []
for trial in range(1200):
    kind = trial % 4
    while True:
        if kind == 0:      # generic
            a = rng.standard_normal(n); b = rng.standard_normal(n)
        elif kind == 1:    # s-direction heavy (a ~ b)
            a = rng.standard_normal(n); b = a + 0.3 * rng.standard_normal(n)
        elif kind == 2:    # t-direction heavy (a ~ -b)
            a = rng.standard_normal(n); b = -a + 0.3 * rng.standard_normal(n)
        else:              # a hole: one coordinate pushed to zero in one or both columns
            a = rng.standard_normal(n); b = rng.standard_normal(n)
            k = rng.integers(n); a[k] = -10; b[k] = -10 * rng.choice([0.0, 1.0])
        a -= a.mean(); b -= b.mean()
        ra, rb = rng.uniform(0, 0.163), rng.uniform(0, 0.163)
        if kind == 3:
            ra, rb = 0.163 * rng.uniform(0.8, 1), 0.163 * rng.uniform(0.3, 1)
        v = 1 / n + a * ra / np.linalg.norm(a); vp = 1 / n + b * rb / np.linalg.norm(b)
        if v.min() >= 0 and vp.min() >= 0 and (v + vp).max() <= 1:
            break
    w = v + vp
    d, dp = float(((v - 1 / n) ** 2).sum()), float(((vp - 1 / n) ** 2).sum())
    hbar = float(v @ vp)
    h = np.where(w > 0, 2 * v * vp / np.where(w > 0, w, 1), 0.0)
    varw = float((w * (h - hbar) ** 2).sum())
    C2, y = solve(v, vp)
    drop = math.log(1 - hbar) - math.log(C2)
    tau = np.log(np.maximum(y, 1e-300)); tau = tau - tau.mean()
    tstar = float(vp @ y)
    rho = v * y; rhop = vp * y / tstar
    pstar = 1 - float(rho @ rhop)
    term1 = math.log((1 - hbar) / (1 - 1 / n))
    term3 = float(sum(((1 - t) * math.log(1 - t) if t < 1 else 0.0) for t in w)) - n * (1 - 2 / n) * math.log(1 - 2 / n)
    total = term1 + term3 - drop
    rows.append((d, dp, hbar, varw, drop, abs(tau).max(), tstar, pstar, term1, term3, total, total - 0.36 * (d + dp), total - 0.5 * (d + dp)))
R = np.array(rows)
print(f"pairs: {len(R)}  (region d,d' <= 0.0266)")
mask = R[:, 3] > 1e-9
print(f"max drop/Var_w(h)            = {(R[mask,4]/R[mask,3]).max():.4f}   (diagonal heuristic 1/(2(1-hbar)^2) = {1/(2*(1-1/7)**2):.4f})")
print(f"max drop                     = {R[:,4].max():.5f}")
print(f"max |tau*|_inf               = {R[:,5].max():.4f};  95th pct = {np.percentile(R[:,5], 95):.4f}")
print(f"t* - 1 in [{(R[:,6]-1).min():.4f}, {(R[:,6]-1).max():.4f}];   p* - (1 - hbar) in [{(R[:,7]-(1-R[:,2])).min():.5f}, {(R[:,7]-(1-R[:,2])).max():.5f}]")
print(f"min margin (I2, a'=0.36)     = {R[:,11].min():.6f};   min margin (a'=0.5) = {R[:,12].min():.6f}")
i = int(R[:, 11].argmin())
print(f"   at the a'=0.36 minimiser: d={R[i,0]:.4f} d'={R[i,1]:.4f} term1={R[i,8]:.5f} term3={R[i,9]:.5f} drop={R[i,4]:.5f} total={R[i,10]:.5f}")
# ratio of drop to the margin available for it
avail = R[:, 8] + R[:, 9] - 0.36 * (R[:, 0] + R[:, 1])
print(f"min (term1 + term3 - 0.36(d+d')) = {avail.min():.6f};  max drop/(that) = {(R[:,4]/np.maximum(avail,1e-12)).max():.4f}")
