"""Check Lemma E2 (exact Hessian quadratic form) and Lemma E3 (floor) at random tau, u, (v, v')."""
import numpy as np
n = 7
rng = np.random.default_rng(35)
worst_e2, worst_e3 = 0.0, 0.0
for trial in range(3000):
    v = rng.dirichlet(np.full(n, rng.choice([0.5, 1.0, 3.0])))
    vp = rng.dirichlet(np.full(n, rng.choice([0.5, 1.0, 3.0])))
    if (v + vp).max() > 1:
        continue
    tau = rng.uniform(0.1, 1.0) * rng.standard_normal(n)
    y = np.exp(tau)
    off = np.ones((n, n)) - np.eye(n)
    M = (v * y)[:, None] * (vp * y)[None, :] * off
    lam = M / M.sum()
    m1, m2 = lam.sum(axis=1), lam.sum(axis=0)
    H = np.diag(m1 + m2) + lam + lam.T - np.outer(m1 + m2, m1 + m2)      # Cov of e_r + e_r'
    rho, rhop = v * y / (v @ y), vp * y / (vp @ y)
    rb = (rho + rhop) / 2
    q = rho @ rhop
    u = rng.standard_normal(n); u -= (rb @ u)                             # <rhobar, u> = 0
    lhs = u @ H @ u
    D1, D2 = float((rho * rhop * u).sum()), float((rho * rhop * u * u).sum())
    e2 = (2 * (rb * u * u).sum() - 2 * (rho @ u) ** 2 - 4 * D2) / (1 - q) - 4 * D1 ** 2 / (1 - q) ** 2
    worst_e2 = max(worst_e2, abs(lhs - e2) / max(abs(lhs), 1e-12))
    # E3 floor
    V = float((rb * u * u).sum())
    chi = float(((rho - rhop) ** 2 / (2 * (rho + rhop))).sum())
    hr = 2 * rho * rhop / (rho + rhop)
    Hm = hr.max()
    Xi = float((rb * (hr - rb @ hr) ** 2).sum())
    floor = V * ((2 * (1 - chi) - 4 * Hm) / (1 - q) - 4 * Xi / (1 - q) ** 2)
    worst_e3 = max(worst_e3, floor - lhs)
    # V >= e^{-osc} Var_m(u)
    m = (v + vp) / 2
    varm = float((m * (u - m @ u) ** 2).sum())
    assert V >= np.exp(-(tau.max() - tau.min())) * varm - 1e-12
print(f"Lemma E2: max relative error of the closed form = {worst_e2:.2e}")
print(f"Lemma E3: max (floor - true quadratic form) = {worst_e3:.2e}   [must be <= 0];  V >= e^-osc Var_m held in all samples")
