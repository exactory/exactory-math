"""Corner of the n = 7 region: both columns large at the same row.  For pairs with v_1, v'_1 in [0.27, 0.306]
and the rest nearly uniform (d, d' <= 0.0266), report: p* vs 1 - hbar and 1/(4 h_max), the discriminant at the
fixed point, rho*_max (must be < 1/2 for the smaller-root identification), the base-point bound D~ = Phi(0) -
Phi(tau~) + corr (corr with the numerically computed kappa) against the budget B (a' = 0.36), and the true drop."""
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



rng = np.random.default_rng(34)
rows = []
for trial in range(400):
    while True:
        a1 = rng.uniform(0.27, 0.306); b1 = rng.uniform(0.27, 0.306)
        rest_a = rng.standard_normal(n - 1); rest_a -= rest_a.mean()
        rest_b = rng.standard_normal(n - 1); rest_b -= rest_b.mean()
        v = np.empty(n); vp = np.empty(n)
        v[0], vp[0] = a1, b1
        ra = math.sqrt(max(0.0, 0.0266 - (a1 - 1 / n) ** 2)) * rng.uniform(0, 1)
        rb = math.sqrt(max(0.0, 0.0266 - (b1 - 1 / n) ** 2)) * rng.uniform(0, 1)
        v[1:] = (1 - a1) / (n - 1) + rest_a / np.linalg.norm(rest_a) * ra
        vp[1:] = (1 - b1) / (n - 1) + rest_b / np.linalg.norm(rest_b) * rb
        if v.min() >= 0 and vp.min() >= 0 and (v + vp).max() <= 1 and ((v - 1/n)**2).sum() <= 0.0266 and ((vp - 1/n)**2).sum() <= 0.0266:
            break
    w = v + vp; m = w / 2
    d, dp = float(((v - 1 / n) ** 2).sum()), float(((vp - 1 / n) ** 2).sum())
    hbar = float(v @ vp)
    h = 2 * v * vp / w
    p_ref = min(1 - hbar, 1 / (4 * h.max()))
    x = np.minimum(4 * h * p_ref, 1.0)
    ytil = 2 * p_ref / (1 + np.sqrt(1 - x))
    tau_t = np.log(ytil); tau_t -= tau_t.mean()
    tau_s = solve(v, vp)
    y = np.exp(tau_s); y = y / float(v @ y)
    theta = float(vp @ y)
    rho = v * y; rhop = vp * y / theta
    pstar = 1 - float(rho @ rhop)
    beta = v * theta + vp
    disc = beta ** 2 - 8 * v * vp * w * pstar * theta
    Phi0, _, _ = phi_grad_hess(np.zeros(n), v, vp)
    Phit, gt, Ht = phi_grad_hess(tau_t, v, vp)
    Phis, gs, Hs = phi_grad_hess(tau_s, v, vp)
    kap = min(kappa_min(phi_grad_hess(tau_t + th * (tau_s - tau_t), v, vp)[2], m) for th in np.linspace(0, 1, 6))
    corr = float((gt ** 2 / m).sum()) / (2 * kap)
    term1 = math.log((1 - hbar) / (1 - 1 / n))
    term3 = float(sum(((1 - t) * math.log(1 - t) if t < 1 else 0.0) for t in w)) - n * (1 - 2 / n) * math.log(1 - 2 / n)
    B = term1 + term3 - 0.36 * (d + dp)
    rows.append((Phi0 - Phis, Phi0 - Phit + corr, B, kap, pstar, 1 - hbar, 1 / (4 * h.max()), disc.min(), max(rho.max(), rhop.max()), 4 * h.max() * (1 - hbar), abs(theta - 1)))
R = np.array(rows)
print(f"corner pairs: {len(R)};  pairs with 4 h_max (1-hbar) > 1: {(R[:,9] > 1).sum()}")
print(f"max drop/B = {(R[:,0]/R[:,2]).max():.3f};  max D~/B = {(R[:,1]/R[:,2]).max():.3f};  min kappa = {R[:,3].min():.3f}")
print(f"p* - (1-hbar) max = {(R[:,4]-R[:,5]).max():.5f};  p* - 1/(4 h_max) max = {(R[:,4]-R[:,6]).max():.5f};  min disc at fixed point = {R[:,7].min():.2e}")
print(f"max tilted entry rho*_max = {R[:,8].max():.4f}  (must stay < 0.5);  max |theta*-1| = {R[:,10].max():.4f}")
