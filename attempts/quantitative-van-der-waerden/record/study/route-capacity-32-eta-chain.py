"""The chain  drop <= -<G, tau*> = eta(t*, p*) <= eta(1, p*) + tcorr <= eta_1(p_up) + tcorr  on the n = 7 region.

eta(t, p) = sum_s G_s [ log(beta_s / w_s) + log(1 + sqrt(1 - x_s)) ],  beta_s = v_s t + v'_s,
x_s = 8 v_s v'_s w_s p t / beta_s^2,  G_s = w_s (hbar - h_s) / (1 - hbar);  eta_1(p) = eta(1, p).
Checks: (a) -<G,tau*> == eta(t*,p*) (root formula, smaller root);  (b) eta_1 increasing in p;
(c) sizes: drop, -<G,tau*>, eta_1(p*), eta_1(p_up) with p_up = min(1 - hbar, 1/(4 h_max)), the t-correction,
against the budget B = term1 + term3 - 0.36 (d + d').  Reports the max of each ratio to B.
"""
import math
import numpy as np
from scipy.optimize import minimize


def solve(v, vp):
    w = v + vp
    n = len(v)
    off = np.ones((n, n)) - np.eye(n)

    def f(u):
        y = np.exp(u)
        M = (v * y)[:, None] * (vp * y)[None, :] * off
        P = float(M.sum())
        dP = M.sum(axis=1) + M.sum(axis=0)
        return math.log(P) - float(w @ u), dP / P - w
    res = minimize(f, np.zeros(n), jac=True, method="BFGS", options={"gtol": 1e-13, "maxiter": 5000})
    y = np.exp(res.x)
    y = y / float(v @ y)
    return math.exp(res.fun), y


def eta(t, p, v, vp, G):
    w = v + vp
    beta = v * t + vp
    x = 8 * v * vp * w * p * t / beta ** 2
    if (x > 1 + 1e-12).any():
        return None
    x = np.minimum(x, 1.0)
    return float((G * (np.log(beta / w) + np.log(1 + np.sqrt(1 - x)))).sum())


n = 7
rng = np.random.default_rng(32)
rows = []
bad_root = 0
for trial in range(700):
    kind = trial % 4
    while True:
        a = rng.standard_normal(n); b = rng.standard_normal(n)
        if kind == 1:
            b = a + 0.3 * rng.standard_normal(n)
        elif kind == 2:
            b = -a + 0.3 * rng.standard_normal(n)
        elif kind == 3:
            k = rng.integers(n); a[k] = -10; b[k] = -10 * rng.choice([0.0, 1.0])
        a -= a.mean(); b -= b.mean()
        ra, rb = rng.uniform(0, 0.163), rng.uniform(0, 0.163)
        if kind == 3:
            ra, rb = 0.163 * rng.uniform(0.8, 1), 0.163 * rng.uniform(0.3, 1)
        if trial % 8 == 7:
            ra, rb = 0.163, 0.163 * rng.uniform(0.9, 1)
        v = 1 / n + a * ra / np.linalg.norm(a); vp = 1 / n + b * rb / np.linalg.norm(b)
        if v.min() >= 0 and vp.min() >= 0 and (v + vp).max() <= 1:
            break
    w = v + vp
    d, dp = float(((v - 1 / n) ** 2).sum()), float(((vp - 1 / n) ** 2).sum())
    hbar = float(v @ vp)
    h = np.where(w > 0, 2 * v * vp / np.where(w > 0, w, 1), 0.0)
    G = w * (hbar - h) / (1 - hbar)
    C2, y = solve(v, vp)
    drop = math.log(1 - hbar) - math.log(C2)
    tau = np.log(y)
    Gtau = -float(G @ tau)
    tstar = float(vp @ y)
    pstar = (float(v @ y) * tstar - float((v * vp * y * y).sum())) / tstar   # P/(A A') with A = 1
    e_star = eta(tstar, pstar, v, vp, G)
    # root check: smaller root reproduces y
    beta = v * tstar + vp
    disc = beta ** 2 - 8 * v * vp * w * pstar * tstar
    y_root = 2 * w * pstar * tstar / (beta + np.sqrt(np.maximum(disc, 0)))
    if abs(y_root - y).max() > 1e-6:
        bad_root += 1
    p_up = min(1 - hbar, 1 / (4 * h.max()))
    e1_pstar = eta(1, pstar, v, vp, G)
    e1_pup = eta(1, p_up, v, vp, G)
    term1 = math.log((1 - hbar) / (1 - 1 / n))
    term3 = float(sum(((1 - t) * math.log(1 - t) if t < 1 else 0.0) for t in w)) - n * (1 - 2 / n) * math.log(1 - 2 / n)
    B = term1 + term3 - 0.36 * (d + dp)
    # monotonicity of eta_1 in p on [0.5 p_up, p_up]
    ps = np.linspace(0.5 * p_up, p_up, 6)
    vals = [eta(1, q, v, vp, G) for q in ps]
    mono = all(vals[i] <= vals[i + 1] + 1e-12 for i in range(5))
    rows.append((drop, Gtau, e_star, e1_pstar, e1_pup, B, tstar, mono, d + dp, e_star - e1_pstar))
R = np.array([r[:7] + (float(r[7]),) + r[8:] for r in rows])
print(f"pairs {len(R)}; root-formula mismatches: {bad_root}; eta(t*,p*) vs -<G,tau*> max abs diff = {abs(R[:,2]-R[:,1]).max():.2e}")
print(f"eta_1 monotone in p in all samples: {bool(R[:,7].min() == 1.0)}")
print(f"max drop/B = {(R[:,0]/R[:,5]).max():.3f}   max -<G,tau*>/B = {(R[:,1]/R[:,5]).max():.3f}   "
      f"max eta_1(p*)/B = {(R[:,3]/R[:,5]).max():.3f}   max eta_1(p_up)/B = {(R[:,4]/R[:,5]).max():.3f}")
print(f"t-correction eta(t*,p*) - eta(1,p*): max |.| = {abs(R[:,9]).max():.2e}, max ratio to B = {(abs(R[:,9])/R[:,5]).max():.3f}; "
      f"max |t*-1| = {abs(R[:,6]-1).max():.4f}")
i = int((R[:,4]/R[:,5]).argmax())
print(f"worst eta_1(p_up)/B pair: d+d'={R[i,8]:.4f}, drop={R[i,0]:.5f}, -<G,tau*>={R[i,1]:.5f}, eta_1(p_up)={R[i,4]:.5f}, B={R[i,5]:.5f}")
