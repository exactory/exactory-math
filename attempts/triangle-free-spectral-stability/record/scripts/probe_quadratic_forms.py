"""Candidate strengthenings of the claim as quadratic forms in the Perron vector.

For a triangle-free graph with adjacency A, degrees d, m edges, Perron unit vector x and
spectral radius lam, write c(u,z) = (A^2)_{uz} for the codegree and

    h_u = [2 (A^4)_{uu} - d(u) (A d)_u] / d(u)    (codegree-weighted gain of N(u)).

Because the gain of the target K_{N(u), B} is sum_{z in B} (2c(u,z) - d(u)), and the
weights c(u,z)/d(u) lie in [0,1], every vertex satisfies D(G) <= m - h_u. The claim
D <= 3 xi therefore follows from any weighted average of h_u being >= 3 lam^2 - 2m.

(A)  weights d(u) x_u^2:  x^T Q_A x >= 0 with
     Q_A = 2m D - D diag(A d) + 2 diag(A^4) - 3 A D A        (equivalent to the
     (x_u^2 + x_v^2)-weighted average of the edge costs D_uv being <= 3 xi).
(H)  weights x_u^2:       x^T Q_H x >= 0 with
     Q_H = 2m I - diag(A d) + 2 diag(A^4) D^{-1} - 3 A^2.
Also records the (x_u^2)-weighted average of the exact vertex-rooted optimal cost c_v,
and whether Q_A, Q_H are positive semidefinite (a PSD certificate would prove the
inequality for every vector, not only the Perron vector).

Usage: python probe_quadratic_forms.py OUT_JSON GENG_PATH [NMAX]
"""
import json
import subprocess
import sys

import numpy as np

import tflib
from probe_hub_phi import double_hub, make_hub, random_big
from probe_weightings import c5_blowups, graph6_to_adj


def forms(a):
    n = a.shape[0]
    m = int(a.sum()) // 2
    deg = a.sum(1).astype(float)
    if deg.min() == 0:  # drop isolated vertices (they change nothing in the claim)
        keep = deg > 0
        a = a[np.ix_(keep, keep)]
        n = a.shape[0]
        deg = a.sum(1).astype(float)
    lam, x = tflib.spectral_data(a)
    af = a.astype(float)
    a2 = af @ af
    a4 = a2 @ a2
    ad = af @ deg
    Dm = np.diag(deg)
    QA = 2 * m * Dm - Dm @ np.diag(ad) + 2 * np.diag(np.diag(a4)) - 3 * af @ Dm @ af
    QH = 2 * m * np.eye(n) - np.diag(ad) + 2 * np.diag(np.diag(a4) / deg) - 3 * a2
    h = (2 * np.diag(a4) - deg * ad) / deg
    cv = np.empty(n)
    for v in range(n):
        gain = np.maximum(0.0, 2 * a2[v] - deg[v])
        gain[a[v].astype(bool)] = 0.0
        cv[v] = m - gain.sum()
    xi = m - lam * lam
    scale = max(lam ** 3, 1.0)
    return {
        "n": n, "m": m, "xi": xi,
        "A_slack": float(x @ QA @ x) / scale,
        "A_min_eig": float(np.linalg.eigvalsh((QA + QA.T) / 2).min()) / scale,
        "H_slack": float(x @ QH @ x) / max(lam ** 2, 1.0),
        "H_min_eig": float(np.linalg.eigvalsh((QH + QH.T) / 2).min()) / max(lam ** 2, 1.0),
        "B_slack": float(3 * xi - (x * x * cv).sum()) / max(lam ** 2, 1.0),
        "h_max_slack": float(h.max() - (3 * lam * lam - 2 * m)) / max(lam ** 2, 1.0),
        "claim_slack": float(3 * xi - cv.min()) / max(lam ** 2, 1.0),
    }


KEYS = ["A_slack", "A_min_eig", "H_slack", "H_min_eig", "B_slack", "h_max_slack", "claim_slack"]


def run_family(name, graphs, report):
    worst = {k: None for k in KEYS}
    viol = {k: 0 for k in KEYS}
    cnt = 0
    for a in graphs:
        if a.sum() == 0:
            continue
        s = forms(a)
        cnt += 1
        for k in KEYS:
            if s[k] < -1e-9:
                viol[k] += 1
            if worst[k] is None or s[k] < worst[k][0]:
                worst[k] = (round(s[k], 8), s["n"], s["m"], round(s["xi"], 4))
    report[name] = {"graphs": cnt, "violations": viol, "worst": worst}
    print(name, cnt, "viol:", {k: v for k, v in viol.items() if v}, "minA", worst["A_slack"][0], "minH", worst["H_slack"][0], flush=True)


def biclique_plus(rng):
    s, t = int(rng.integers(2, 8)), int(rng.integers(2, 8))
    extra = int(rng.integers(1, 12))
    n = s + t + extra
    a = np.zeros((n, n), dtype=np.int64)
    a[:s, s:s + t] = 1
    a[s:s + t, :s] = 1
    # pendant vertices, pendant paths and small stars hung on random vertices; stays triangle-free
    for w in range(s + t, n):
        kind = rng.integers(0, 3)
        host = int(rng.integers(0, w))
        if kind == 2 and w >= s + t + 1:
            host = int(rng.integers(s + t, w))
        a[w, host] = a[host, w] = 1
    return a


def spider(d, k):
    n = 1 + d + d * k
    a = np.zeros((n, n), dtype=np.int64)
    for i in range(d):
        mid = 1 + i
        a[0, mid] = a[mid, 0] = 1
        for j in range(k):
            leaf = 1 + d + i * k + j
            a[mid, leaf] = a[leaf, mid] = 1
    return a


def c5_blowup_plus_hub(sizes, hub_class, leaves):
    base = np.zeros((5, 5), dtype=np.int64)
    for i in range(5):
        base[i, (i + 1) % 5] = base[(i + 1) % 5, i] = 1
    idx = [i for i, k in enumerate(sizes) for _ in range(k)]
    nn = len(idx)
    n = nn + leaves
    a = np.zeros((n, n), dtype=np.int64)
    for p in range(nn):
        for q in range(nn):
            if base[idx[p], idx[q]]:
                a[p, q] = 1
    hub = idx.index(hub_class)
    for l in range(nn, n):
        a[hub, l] = a[l, hub] = 1
    return a


def main(out, geng, nmax=10):
    report = {}
    for n in range(2, nmax + 1):
        res = subprocess.run([geng, "-t", "-q", "-c", str(n)], capture_output=True, text=True, check=True)
        run_family("geng_tf_conn_n%d" % n, (graph6_to_adj(l) for l in res.stdout.splitlines() if l.strip()), report)
    run_family("hub_glued_biclique", (make_hub(t, k, j) for t in range(3, 61, 3) for k in range(1, 9) for j in range(0, 5) if j + 1 <= t), report)
    run_family("double_star_edge", (double_hub(t1, t2, "edge") for t1 in range(1, 31, 3) for t2 in range(1, 31, 3)), report)
    run_family("double_star_path3", (double_hub(t1, t2, "path3") for t1 in range(1, 31, 3) for t2 in range(1, 31, 3)), report)
    rng = np.random.default_rng(5)
    run_family("random_n12_30", (random_big(rng) for _ in range(400)), report)
    run_family("biclique_plus_pendants", (biclique_plus(rng) for _ in range(600)), report)
    run_family("spiders", (spider(d, k) for d in range(2, 15) for k in range(1, 6)), report)
    run_family("c5_blowups", c5_blowups(), report)
    run_family("c5_blowup_plus_hub", (c5_blowup_plus_hub(sizes, hc, lv) for sizes in [(1, 1, 1, 1, 1), (2, 2, 2, 2, 2), (3, 1, 3, 1, 1), (4, 4, 4, 4, 4)]
                                        for hc in range(5) for lv in range(1, 25, 4)), report)
    with open(out, "w") as fh:
        json.dump(report, fh, indent=1, default=float)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 10)
