"""Test the lemma candidates behind (H).

(M)  matrix form:  A^2 <= diag(beta),  beta_u = (A^4)_{uu}/d(u) + Z_u,  Z_u = edges with
     no end in N(u). Then Q_H = [diag(Ad) - A^2] + 2[diag(beta) - A^2] is PSD.
(M') Perron form:  lam^2 <= sum_u x_u^2 beta_u.
Also lists every connected triangle-free graph on <= 9 vertices on which (H) is tight
(slack below 1e-9 relative), to compare the equality cases with K_{s,t} and C5 blow-ups.

Usage: python probe_M.py OUT_JSON GENG_PATH [NMAX]
"""
import json
import subprocess
import sys

import networkx as nx
import numpy as np

import tflib
from probe_hub_phi import double_hub, make_hub, random_big
from probe_quadratic_forms import biclique_plus, c5_blowup_plus_hub, spider
from probe_weightings import c5_blowups, graph6_to_adj


def apex_biclique_minus_matching(k):
    n = 2 * k + 1
    a = np.zeros((n, n), dtype=np.int64)
    for i in range(k):
        for j in range(k):
            if i != j:
                a[i, k + j] = a[k + j, i] = 1
        a[2 * k, i] = a[i, 2 * k] = 1
    return a


def random_bipartite(rng):
    s, t = int(rng.integers(2, 12)), int(rng.integers(2, 12))
    p = float(rng.uniform(0.2, 0.95))
    n = s + t
    a = np.zeros((n, n), dtype=np.int64)
    for i in range(s):
        for j in range(s, n):
            if rng.random() < p:
                a[i, j] = a[j, i] = 1
    return a


def random_tree(rng):
    n = int(rng.integers(4, 40))
    g = nx.random_labeled_tree(n, seed=int(rng.integers(0, 2**31 - 1)))
    return nx.to_numpy_array(g, dtype=np.int64)


def analyse(a):
    deg = a.sum(1)
    keep = deg > 0
    a = a[np.ix_(keep, keep)]
    if not nx.is_connected(nx.from_numpy_array(a)):
        return None
    n = a.shape[0]
    m = int(a.sum()) // 2
    deg = a.sum(1).astype(float)
    lam, x = tflib.spectral_data(a)
    af = a.astype(float)
    a2 = af @ af
    a4 = a2 @ a2
    ad = af @ deg
    Z = m - ad
    beta = np.diag(a4) / deg + Z
    M_min = float(np.linalg.eigvalsh(np.diag(beta) - a2).min()) / lam ** 2
    Mp = float((x * x * beta).sum() - lam * lam) / lam ** 2
    QH = np.diag(2 * np.diag(a4) / deg + m + Z) - 3 * a2
    H = float(x @ QH @ x) / lam ** 2
    return {"n": n, "m": m, "M_min_eig": M_min, "Mprime": Mp, "H": H}


KEYS = ["M_min_eig", "Mprime", "H"]


def run_family(name, graphs, report, tight_out=None):
    worst = {k: None for k in KEYS}
    viol = {k: 0 for k in KEYS}
    cnt = 0
    for a in graphs:
        s = analyse(a) if a.sum() else None
        if s is None:
            continue
        cnt += 1
        for k in KEYS:
            if s[k] < -1e-9:
                viol[k] += 1
            if worst[k] is None or s[k] < worst[k][0]:
                worst[k] = (round(s[k], 9), s["n"], s["m"])
        if tight_out is not None and s["H"] < 1e-9:
            g = nx.from_numpy_array(a)
            tight_out.append({"n": s["n"], "m": s["m"], "graph6": nx.to_graph6_bytes(g, header=False).decode().strip(),
                              "degrees": sorted(int(d) for d in a.sum(1))})
    report[name] = {"graphs": cnt, "violations": viol, "worst": worst}
    print(name, cnt, "viol:", {k: v for k, v in viol.items() if v}, "worst:", worst, flush=True)


def main(out, geng, nmax=10):
    report = {}
    tight = []
    for n in range(2, nmax + 1):
        res = subprocess.run([geng, "-t", "-q", "-c", str(n)], capture_output=True, text=True, check=True)
        run_family("geng_tf_conn_n%d" % n, (graph6_to_adj(l) for l in res.stdout.splitlines() if l.strip()), report,
                   tight if n <= 9 else None)
    run_family("apex_biclique_minus_matching", (apex_biclique_minus_matching(k) for k in range(2, 30)), report)
    run_family("hub_glued_biclique", (make_hub(t, k, j) for t in range(3, 61, 3) for k in range(1, 9) for j in range(0, 5) if j + 1 <= t), report)
    run_family("double_star_edge", (double_hub(t1, t2, "edge") for t1 in range(1, 31, 3) for t2 in range(1, 31, 3)), report)
    run_family("double_star_path3", (double_hub(t1, t2, "path3") for t1 in range(1, 31, 3) for t2 in range(1, 31, 3)), report)
    rng = np.random.default_rng(7)
    run_family("random_n12_30", (random_big(rng) for _ in range(400)), report)
    run_family("random_bipartite", (random_bipartite(rng) for _ in range(600)), report)
    run_family("random_trees", (random_tree(rng) for _ in range(400)), report)
    run_family("biclique_plus_pendants", (biclique_plus(rng) for _ in range(400)), report)
    run_family("spiders", (spider(d, k) for d in range(2, 15) for k in range(1, 6)), report)
    run_family("c5_blowups", c5_blowups(), report)
    run_family("c5_blowup_plus_hub", (c5_blowup_plus_hub(sizes, hc, lv) for sizes in [(1, 1, 1, 1, 1), (2, 2, 2, 2, 2), (3, 1, 3, 1, 1)]
                                        for hc in range(5) for lv in range(1, 25, 4)), report)
    report["tight_for_H_n_le_9"] = tight
    print("tight graphs for (H), n<=9:", len(tight))
    for t in tight:
        print(" ", t)
    with open(out, "w") as fh:
        json.dump(report, fh, indent=1, default=float)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 10)
