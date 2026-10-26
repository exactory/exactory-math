"""The exact identity behind Lemma 2', and the inequalities that turn it into a bound.

Let A be in K_n with Sinkhorn scaling B = D1 A D2, log-scalings l1 = log d1, l2 = log d2, and
w_ij = l1_i + l2_j.  Write F(l) = sum_ij a_ij e^{l1_i + l2_j} - sum l1 - sum l2, convex, minimised
at l* with F(0) - F(l*) = K = -log cap(A).  Writing K as the integral of s l*^T H(s l*) l* over
s in [0, 1] and evaluating gives the exact formula

    (I)   K = sum_ij b_ij w_ij^2 psi(w_ij),      psi(w) = (e^{-w} - 1 + w) / w^2,  psi(0) = 1/2,

and the margins are exactly

    (II)  u_i = sum_j b_ij (1 - e^{-w_ij}),      v_j = sum_i b_ij (1 - e^{-w_ij}).

psi is decreasing, so on a support where w >= -delta,  K <= psi(-delta) Q  with
Q = sum_ij b_ij w_ij^2 = l^T L_B l.  And (II) is (u; v) = L_B l + e with the error
e_i = sum_j b_ij (1 - e^{-w} - w)_ij, |1 - e^{-w} - w| <= (w^2/2) e^{max(0, -w)}.

This script checks (I) and (II) to machine precision, then the chain

    Q >= lambda_2(B) |l|^2   (l normalised orthogonal to (1; -1)),
    Q <= |l| (|(u;v)| + |e|),
    K <= psi(-delta) Q,

on the same random near-doubly-stochastic matrices as lemma2-prime.py, and reports how much
each step loses at the application's margin size.
"""
import math
import sys

import numpy as np


def sinkhorn_factors(X, iters=400000, tol=1e-15):
    n = X.shape[0]
    d1, d2 = np.ones(n), np.ones(n)
    for _ in range(iters):
        r = np.einsum("ij,j->i", X, d2) * d1
        d1 = d1 / r
        c = np.einsum("ij,i->j", X, d1) * d2
        d2 = d2 / c
        if abs(r - 1).max() < tol and abs(c - 1).max() < tol:
            break
    return d1, d2


def psi(w):
    w = np.asarray(w, dtype=float)
    out = np.full_like(w, 0.5)
    m = np.abs(w) > 1e-6
    out[m] = (np.exp(-w[m]) - 1 + w[m]) / w[m] ** 2
    return out


rng = np.random.default_rng(11)
print(f"{'n':>3} {'max |(I) err|':>14} {'max |(II) err|':>15} {'worst K/Q':>10} {'worst psi(-d)':>14} "
      f"{'worst Q/(lam |l|^2)':>18} {'worst Q/(|l|(m+|e|))':>21} {'worst 2K lam/m^2':>17}")
for n in [int(a) for a in sys.argv[1:]] or [5, 7, 8, 10]:
    g = math.factorial(n) / n ** n
    mmax = math.sqrt(2 * g / ((1 - g) * (1 - 2 * math.sqrt(2 * g) / 3)))
    e1m, e2m, kq, pw, ql, qm, fin = 0, 0, 0, 0, math.inf, 0, 0
    for trial in range(400):
        spread = rng.choice([0.3, 1.0, 2.0, 3.5])
        X = np.exp(spread * rng.standard_normal((n, n)))
        X[0, 0] = 0.0
        if trial % 3 == 2:
            k = rng.integers(1, n // 2 + 1)
            t = rng.choice([0.05, 0.1, 0.2])
            X[:k, k:] *= t
            X[k:, :k] *= t
        d1, d2 = sinkhorn_factors(X)
        B = np.einsum("i,ij,j->ij", d1, X, d2)
        eps = rng.choice([0.3, 1.0]) * mmax / math.sqrt(2 * n)
        A = np.einsum("i,ij,j->ij", np.exp(eps * rng.standard_normal(n)), B,
                      np.exp(eps * rng.standard_normal(n)))
        A *= n / A.sum()
        u, v = 1 - A.sum(1), 1 - A.sum(0)
        f1, f2 = sinkhorn_factors(A)
        Bs = np.einsum("i,ij,j->ij", f1, A, f2)
        l1, l2 = np.log(f1), np.log(f2)
        K = float(l1.sum() + l2.sum())
        # normalise the potentials orthogonal to (1; -1): shift t = (sum l2 - sum l1)/(2n)
        t = (l2.sum() - l1.sum()) / (2 * n)
        l1, l2 = l1 + t, l2 - t
        W = l1[:, None] + l2[None, :]
        sup = Bs > 1e-300
        K_I = float((Bs * W ** 2 * psi(W))[sup].sum())
        e1m = max(e1m, abs(K_I - K))
        u_II = (Bs * (1 - np.exp(-W)))[:, :].sum(1)
        v_II = (Bs * (1 - np.exp(-W)))[:, :].sum(0)
        e2m = max(e2m, float(max(abs(u_II - u).max(), abs(v_II - v).max())))
        Q = float((Bs * W ** 2)[sup].sum())
        lam = 1.0 - float(np.linalg.svd(Bs, compute_uv=False)[1])
        ell = math.sqrt(float(l1 @ l1 + l2 @ l2))
        m = math.sqrt(float(u @ u + v @ v))
        err = np.concatenate([(Bs * (1 - np.exp(-W) - W)).sum(1), (Bs * (1 - np.exp(-W) - W)).sum(0)])
        en = float(np.linalg.norm(err))
        delta = max(0.0, -float(W[sup].min()))
        kq = max(kq, K / Q)
        pw = max(pw, float(psi(np.array([-delta]))[0]))
        ql = min(ql, Q / (lam * ell ** 2)) if ell > 0 else ql
        qm = max(qm, Q / (ell * (m + en)))
        fin = max(fin, 2 * K * lam / m ** 2)
    print(f"{n:>3} {e1m:>14.2e} {e2m:>15.2e} {kq:>10.4f} {pw:>14.4f} {ql:>18.4f} {qm:>21.4f} {fin:>17.4f}")
print("\n(I) and (II) exact to rounding; K/Q <= psi(-delta) < 1; Q lam/|l|^2 >= 1 and")
print("Q/(|l|(m+|e|)) <= 1 are the two chain inequalities; the last column is Lemma 2' itself.")
