"""Which weighted averages of the edge costs D_uv (target K_{N(v),N(u)}) and of the
vertex-rooted optimal costs c_v (target K_{N(v), B*(N(v))}) stay within 3 xi?

Also records the minimum over edges (the edge-certificate form of the claim) and the
minimum over vertices (c_v form) on every graph tested. Families: geng -t for n <= 9,
hubs with a glued K_{j+1,k}, double stars joined by an edge, random triangle-free graphs
on 12..30 vertices, unbalanced C5 blow-ups.

Usage: python probe_weightings.py OUT_JSON GENG_PATH
"""
import json
import subprocess
import sys

import numpy as np

import tflib
from probe_hub_phi import double_hub, make_hub, random_big


def graph6_to_adj(line):
    data = [ord(c) - 63 for c in line.strip()]
    n = data[0]
    bits = []
    for d in data[1:]:
        bits.extend(((d >> k) & 1) for k in range(5, -1, -1))
    a = np.zeros((n, n), dtype=np.int64)
    idx = 0
    for v in range(1, n):
        for u in range(v):
            if bits[idx]:
                a[u, v] = a[v, u] = 1
            idx += 1
    return a


def stats(a):
    n = a.shape[0]
    m = int(a.sum()) // 2
    lam, x = tflib.spectral_data(a)
    xi = m - lam * lam
    deg = a.sum(1).astype(float)
    a2 = a @ a
    a3 = a2 @ a
    us, vs = np.nonzero(np.triu(a))
    costs = m + deg[us] * deg[vs] - 2 * a3[us, vs]
    # vertex-rooted optimal targets
    cv = np.empty(n)
    for v in range(n):
        d = deg[v]
        nbr = a[v].astype(bool)
        gain = np.maximum(0.0, 2 * a2[v] - d)
        gain[nbr] = 0.0
        cv[v] = m - gain.sum()
    weightings = {
        "edge_uniform": np.ones(len(us)),
        "edge_perron": x[us] * x[vs],
        "edge_sq_sum": x[us] ** 2 + x[vs] ** 2,
        "edge_perron_over_degprod": x[us] * x[vs] / (deg[us] * deg[vs]),
        "edge_perron_over_degsum": x[us] * x[vs] / (deg[us] + deg[vs]),
        "edge_meanratio": (x[us] / deg[us]) ** 2 + (x[vs] / deg[vs]) ** 2,
        "edge_perron_times_a3": x[us] * x[vs] * a3[us, vs],
    }
    out = {"n": n, "m": m, "xi": float(xi), "edge_min": float(costs.min()), "vertex_min": float(cv.min())}
    for name, w in weightings.items():
        out[name] = float((w * costs).sum() / w.sum())
    out["vertex_uniform"] = float(cv.mean())
    out["vertex_perron2"] = float((x * x * cv).sum())
    out["vertex_degree"] = float((deg * cv).sum() / deg.sum())
    out["vertex_perron1"] = float((x * cv).sum() / x.sum())
    return out


KEYS = ["edge_min", "vertex_min", "edge_uniform", "edge_perron", "edge_sq_sum", "edge_perron_over_degprod",
        "edge_perron_over_degsum", "edge_meanratio", "edge_perron_times_a3", "vertex_uniform", "vertex_perron2",
        "vertex_degree", "vertex_perron1"]


def run_family(name, graphs, report):
    worst = {k: None for k in KEYS}
    viol = {k: 0 for k in KEYS}
    cnt = 0
    for a in graphs:
        if a.sum() == 0:
            continue
        s = stats(a)
        cnt += 1
        for k in KEYS:
            slack = 3 * s["xi"] - s[k]
            if slack < -1e-7:
                viol[k] += 1
            if worst[k] is None or slack < worst[k][0]:
                worst[k] = (round(slack, 6), s["n"], s["m"], round(s["xi"], 4))
    report[name] = {"graphs": cnt, "violations": viol, "worst_slack": worst}
    print(name, cnt, {k: v for k, v in viol.items() if v}, flush=True)


def c5_blowups():
    base = np.zeros((5, 5), dtype=np.int64)
    for i in range(5):
        base[i, (i + 1) % 5] = base[(i + 1) % 5, i] = 1
    for sizes in [(1, 1, 1, 1, 1), (3, 1, 1, 1, 1), (5, 1, 1, 1, 1), (4, 4, 1, 1, 1), (6, 1, 6, 1, 1), (2, 5, 2, 5, 1),
                  (7, 1, 1, 1, 1), (1, 7, 1, 7, 1), (3, 5, 2, 6, 4), (9, 1, 9, 1, 1), (1, 9, 1, 1, 9)]:
        idx = [i for i, k in enumerate(sizes) for _ in range(k)]
        nn = len(idx)
        a = np.zeros((nn, nn), dtype=np.int64)
        for p in range(nn):
            for q in range(nn):
                if base[idx[p], idx[q]]:
                    a[p, q] = 1
        yield a


def main(out, geng):
    report = {}
    for n in range(2, 10):
        res = subprocess.run([geng, "-t", "-q", str(n)], capture_output=True, text=True, check=True)
        graphs = (graph6_to_adj(l) for l in res.stdout.splitlines() if l.strip())
        run_family("geng_tf_n%d" % n, graphs, report)
    hubs = (make_hub(t, k, j) for t in range(3, 61, 3) for k in range(1, 9) for j in range(0, 5) if j + 1 <= t)
    run_family("hub_glued_biclique", hubs, report)
    run_family("double_star_edge", (double_hub(t1, t2, "edge") for t1 in range(1, 31, 3) for t2 in range(1, 31, 3)), report)
    run_family("double_star_path3", (double_hub(t1, t2, "path3") for t1 in range(1, 31, 3) for t2 in range(1, 31, 3)), report)
    rng = np.random.default_rng(11)
    run_family("random_n12_30", (random_big(rng) for _ in range(500)), report)
    run_family("c5_blowups", c5_blowups(), report)
    with open(out, "w") as fh:
        json.dump(report, fh, indent=1, default=float)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
