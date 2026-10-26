"""Base-point convexity bound on the n = 7 region.

Phi(tau) = log P(e^tau) - <w, tau>.  For any tau~:  log C_2 >= Phi(tau~) - (sum_s grad_s^2 / m_s) / (2 kappa),
kappa = inf over the segment [tau~, tau*] and u perp 1 of u^T Hess u / Var_m(u), m = w/2, grad = grad Phi(tau~).
Base point: tau~_s = log y_s(1, p_ref), y_s the smaller root at theta = 1, p_ref = min(1 - hbar, 1/(4 h_max)).
Reports: drop bound D~ = Phi(0) - Phi(tau~) + corr against the true drop and the budget B (a' = 0.36),
the size of |grad|, kappa along the segment, and the corner frequency (h_max > 1/(4(1-hbar))).
"""
import math
import numpy as np
from scipy.optimize import minimize

n = 7


def solve(v, vp):
    w = v + vp
    off = np.ones((n, n)) - np.eye(n)

    def f(u):
        y = np.exp(u)
        M = (v * y)[:, None] * (vp * y)[None, :] * off
        P = float(M.sum())
        dP = M.sum(axis=1) + M.sum(axis=0)
        return math.log(P) - float(w @ u), dP / P - w
    res = minimize(f, np.zeros(n), jac=True, method="BFGS", options={"gtol": 1e-13, "maxiter": 5000})
    return res.x - res.x.mean()


def phi_grad_hess(tau, v, vp):
    w = v + vp
    y = np.exp(tau)
    off = np.ones((n, n)) - np.eye(n)
    M = (v * y)[:, None] * (vp * y)[None, :] * off
    P = float(M.sum())
    lam = M / P
    m1, m2 = lam.sum(axis=1), lam.sum(axis=0)
    grad = m1 + m2 - w
    # Hessian = Cov of alpha = e_r + e_r' under lam
    Ealpha = m1 + m2
    Eaa = np.diag(m1 + m2) + lam + lam.T
    H = Eaa - np.outer(Ealpha, Ealpha)
    return math.log(P) - float(w @ tau), grad, H


def kappa_min(H, m):
    """min over u perp 1 of u^T H u / Var_m(u); Var_m(u) = u^T (diag(m) - m m^T) u."""
    Mm = np.diag(m) - np.outer(m, m)
    # restrict to 1^perp
    Q, _ = np.linalg.qr(np.column_stack([np.ones(n), np.eye(n)[:, :n - 1]]))
    Bq = Q[:, 1:]
    Hr = Bq.T @ H @ Bq
    Mr = Bq.T @ Mm @ Bq
    L = np.linalg.cholesky(Mr)
    Li = np.linalg.inv(L)
    return float(np.linalg.eigvalsh(Li @ Hr @ Li.T).min())


rng = np.random.default_rng(33)
rows = []
corner = 0
for trial in range(600):
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
        if trial % 16 == 15:   # push toward the corner: both columns large at the same row
            k = rng.integers(n); a[k] = 10; b[k] = 10 + rng.standard_normal(); a -= a.mean(); b -= b.mean()
            ra, rb = 0.163, 0.163 * rng.uniform(0.95, 1)
        v = 1 / n + a * ra / np.linalg.norm(a); vp = 1 / n + b * rb / np.linalg.norm(b)
        if v.min() >= 0 and vp.min() >= 0 and (v + vp).max() <= 1:
            break
    w = v + vp
    m = w / 2
    d, dp = float(((v - 1 / n) ** 2).sum()), float(((vp - 1 / n) ** 2).sum())
    hbar = float(v @ vp)
    h = np.where(w > 0, 2 * v * vp / np.where(w > 0, w, 1), 0.0)
    if h.max() > 1 / (4 * (1 - hbar)):
        corner += 1
    p_ref = min(1 - hbar, 1 / (4 * h.max()))
    x = np.minimum(4 * h * p_ref, 1.0)
    ytil = 2 * p_ref / (1 + np.sqrt(1 - x))          # = 2 w p /(w + sqrt(w^2 - 8 v v' w p)) at theta = 1
    tau_t = np.log(ytil); tau_t -= tau_t.mean()
    tau_s = solve(v, vp)
    Phi0, _, _ = phi_grad_hess(np.zeros(n), v, vp)
    Phit, gt, Ht = phi_grad_hess(tau_t, v, vp)
    Phis, gs, Hs = phi_grad_hess(tau_s, v, vp)
    kap = min(kappa_min(phi_grad_hess(tau_t + th * (tau_s - tau_t), v, vp)[2], m) for th in np.linspace(0, 1, 6))
    corr = float((gt ** 2 / m).sum()) / (2 * kap)
    drop_true = Phi0 - Phis
    Dtil = Phi0 - Phit + corr
    term1 = math.log((1 - hbar) / (1 - 1 / n))
    term3 = float(sum(((1 - t) * math.log(1 - t) if t < 1 else 0.0) for t in w)) - n * (1 - 2 / n) * math.log(1 - 2 / n)
    B = term1 + term3 - 0.36 * (d + dp)
    rows.append((drop_true, Phi0 - Phit, corr, Dtil, B, kap, float(np.abs(gt).max()), d + dp, float(np.abs(tau_t - tau_s).max())))
R = np.array(rows)
print(f"pairs {len(R)}, corner pairs (h_max > 1/(4(1-hbar))): {corner}")
print(f"max drop_true/B = {(R[:,0]/R[:,4]).max():.3f};  max (Phi0 - Phi(tau~))/B = {(R[:,1]/R[:,4]).max():.3f};  "
      f"max corr/B = {(R[:,2]/R[:,4]).max():.4f};  max D~/B = {(R[:,3]/R[:,4]).max():.3f}")
print(f"min kappa along segments = {R[:,5].min():.3f} (centre value 2(n-2)/(n-1) = {2*(n-2)/(n-1):.3f});  max |grad Phi(tau~)|_inf = {R[:,6].max():.2e};  "
      f"max |tau~ - tau*|_inf = {R[:,8].max():.3f}")
i = int((R[:,3]/R[:,4]).argmax())
print(f"worst D~/B: d+d'={R[i,7]:.4f} drop={R[i,0]:.5f} Phi0-Phi~={R[i,1]:.5f} corr={R[i,2]:.6f} B={R[i,4]:.5f} kappa={R[i,5]:.3f}")
