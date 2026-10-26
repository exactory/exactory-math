"""Stress the Phi-lemma (yAy <= lam^3 + 2 lam T) and the Perron-weighted average inequality
(star) on hub families, double hubs and larger random triangle-free graphs.

Usage: python probe_hub_phi.py OUT_JSON
"""
import json
import sys

import numpy as np

import tflib


def forms(a):
    n = a.shape[0]
    m = int(a.sum()) // 2
    lam, x = tflib.spectral_data(a)
    deg = a.sum(1).astype(float)
    q = a @ (x * x)
    W = deg * q - (lam * x) ** 2
    T = 2 * W.sum()
    y = deg * x
    yAy = float(y @ a @ y)
    phi_slack = lam ** 3 + 2 * lam * T - yAy
    a3 = a @ a @ a
    us, vs = np.nonzero(np.triu(a))
    costs = m + deg[us] * deg[vs] - 2 * a3[us, vs]
    w = x[us] * x[vs]
    star_slack = 3 * (m - lam * lam) - float((w * costs).sum() / w.sum())
    return phi_slack, star_slack, lam, int(deg.max()), n, m


def make_hub(t, k, j):
    """Hub 0 with leaves 1..t; K_{j+1,k} glued on leaves 1..j+1 (needs j+1 <= t)."""
    n = 1 + t + k
    a = np.zeros((n, n), dtype=np.int64)
    for i in range(1, t + 1):
        a[0, i] = a[i, 0] = 1
    for w in range(t + 1, t + 1 + k):
        for l in range(1, 2 + j):
            a[l, w] = a[w, l] = 1
    return a


def double_hub(t1, t2, mode):
    n = 2 + t1 + t2 + (2 if mode == "path3" else 0)
    a = np.zeros((n, n), dtype=np.int64)
    for i in range(t1):
        a[0, 2 + i] = a[2 + i, 0] = 1
    for i in range(t2):
        a[1, 2 + t1 + i] = a[2 + t1 + i, 1] = 1
    if mode == "edge":
        a[0, 1] = a[1, 0] = 1
    else:
        p, q = n - 2, n - 1
        a[0, p] = a[p, 0] = 1
        a[p, q] = a[q, p] = 1
        a[q, 1] = a[1, q] = 1
    return a


def random_big(rng):
    n = int(rng.integers(12, 31))
    a = np.zeros((n, n), dtype=np.int64)
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(pairs)
    a2 = a @ a
    for u, v in pairs[: int(rng.integers(n, len(pairs)))]:
        if a2[u, v] == 0:
            a[u, v] = a[v, u] = 1
            a2 = a @ a
    return a


def main(out):
    report = {}
    worst_phi, worst_star, viol_phi, viol_star, cnt = None, None, [], [], 0
    for t in range(3, 61, 3):
        for k in range(1, 9):
            for j in range(0, 5):
                if j + 1 > t:
                    continue
                a = make_hub(t, k, j)
                assert np.trace(a @ a @ a) == 0
                ps, ss, lam, dm, n, m = forms(a)
                cnt += 1
                if ps < -1e-7:
                    viol_phi.append((t, k, j, ps))
                if ss < -1e-7:
                    viol_star.append((t, k, j, ss))
                if worst_phi is None or ps / lam ** 3 < worst_phi[0]:
                    worst_phi = (ps / lam ** 3, t, k, j, ps)
                if worst_star is None or ss < worst_star[0]:
                    worst_star = (ss, t, k, j)
    report["hub"] = {"graphs": cnt, "phi_violations": viol_phi[:10], "star_violations": viol_star[:10],
                     "min_phi_slack_over_lam3": worst_phi, "min_star_slack": worst_star}
    for mode in ["edge", "path3"]:
        w, v = None, 0
        for t1 in range(1, 31, 3):
            for t2 in range(1, 31, 3):
                ps, ss, lam, dm, n, m = forms(double_hub(t1, t2, mode))
                if ps < -1e-7:
                    v += 1
                if w is None or ps < w[0]:
                    w = (ps, t1, t2)
        report["double_hub_" + mode] = {"phi_violations": v, "min_phi_slack": w}
    rng = np.random.default_rng(3)
    vphi, vstar, done, minphi = 0, 0, 0, 1e9
    for _ in range(400):
        a = random_big(rng)
        if a.sum() == 0:
            continue
        ps, ss, lam, dm, n, m = forms(a)
        done += 1
        minphi = min(minphi, ps / lam ** 3)
        vphi += ps < -1e-7
        vstar += ss < -1e-7
    report["random_n_le_30"] = {"graphs": done, "phi_violations": int(vphi), "star_violations": int(vstar),
                               "min_phi_slack_over_lam3": minphi}
    with open(out, "w") as fh:
        json.dump(report, fh, indent=1, default=float)
    print(json.dumps(report, indent=1, default=float))


if __name__ == "__main__":
    main(sys.argv[1])
