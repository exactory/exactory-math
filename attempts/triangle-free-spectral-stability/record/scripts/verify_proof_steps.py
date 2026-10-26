"""Check every step of the proof of D(G) <= 3(m - lam^2) numerically on all connected
triangle-free graphs with at most NMAX vertices and on the adversarial families.

Steps (S = N(u), W = V - N[u], Z_u = e(G[W]), c(u,z) = (A^2)_{uz}):
 1. D_uv (direct symmetric-difference count of the target K_{N(v),N(u)}) equals
    m + d(u)d(v) - 2 (A^3)_{uv}; and sum_{v in N(u)} D_uv = d(u) m + d(u)(Ad)_u - 2 (A^4)_{uu}.
 2. (A^2 d)_u - (A^4)_{uu} = sum over edges zz' inside W of (d_S(z) + d_S(z')), and this is
    <= d(u) Z_u because adjacent vertices have disjoint neighbourhoods.
 3. Matrix inequalities: A^2 <= diag(Ad), A^2 <= diag((A^2 d)_u / d(u)) (checked as PSD).
 4. Q_H = diag(m + Z_u + 2 (A^4)_{uu}/d(u)) - 3 A^2 is PSD.
 5. sum_u x_u^2 mean_{v in N(u)} D_uv <= 3 xi, hence min_{uv} D_uv <= 3 xi.
Usage: python verify_proof_steps.py GENG_PATH [NMAX]
"""
import subprocess
import sys

import numpy as np

import tflib
from probe_hub_phi import double_hub, make_hub, random_big
from probe_M import apex_biclique_minus_matching, random_bipartite, random_tree
from probe_quadratic_forms import biclique_plus, c5_blowup_plus_hub, spider
from probe_weightings import c5_blowups, graph6_to_adj

TOL = 1e-8


def check(a, counts):
    deg0 = a.sum(1)
    keep = deg0 > 0
    a = a[np.ix_(keep, keep)]
    n = a.shape[0]
    if n == 0:
        return
    m = int(a.sum()) // 2
    deg = a.sum(1)
    a2 = a @ a
    a3 = a2 @ a
    a4 = a2 @ a2
    ad = a @ deg
    a2d = a2 @ deg
    Z = m - ad
    # step 1: direct edge costs
    for (u, v, direct, formula) in tflib.edge_certificates(a):
        assert direct == formula == m + deg[u] * deg[v] - 2 * a3[u, v], (u, v, direct, formula)
    for u in range(n):
        nb = np.nonzero(a[u])[0]
        s = sum(m + deg[u] * deg[v] - 2 * a3[u, v] for v in nb)
        assert s == deg[u] * m + deg[u] * ad[u] - 2 * a4[u, u], ("step1 sum", u)
    # step 2: combinatorial identity and inequality (exact integers)
    for u in range(n):
        S = a[u].astype(bool)
        Wmask = ~S
        Wmask[u] = False
        dS = a2[u]  # d_S(z) = c(u, z)
        lhs = int(a2d[u] - a4[u, u])
        total = 0
        Widx = np.nonzero(Wmask)[0]
        for i in Widx:
            for j in Widx:
                if j > i and a[i, j]:
                    assert dS[i] + dS[j] <= deg[u], "adjacent vertices share S-neighbours?"
                    total += int(dS[i] + dS[j])
        assert lhs == total, ("step2 identity", u, lhs, total)
        assert lhs <= deg[u] * Z[u], ("step2 inequality", u)
        counts["step2_tight"] += int(lhs == deg[u] * Z[u])
    # step 3, 4: PSD checks
    af = a.astype(float)
    a2f = af @ af
    e1 = np.linalg.eigvalsh(np.diag(ad.astype(float)) - a2f).min()
    e2 = np.linalg.eigvalsh(np.diag(a2d / deg) - a2f).min()
    QH = np.diag(m + Z + 2 * np.diag(a4) / deg) - 3 * a2f
    e3 = np.linalg.eigvalsh(QH).min()
    scale = max(float(deg.max()) ** 2, 1.0)
    assert e1 >= -TOL * scale and e2 >= -TOL * scale and e3 >= -TOL * scale, ("psd", e1, e2, e3)
    # step 5: Perron vector conclusion
    lam, x = tflib.spectral_data(a)
    xi = m - lam * lam
    mean_cost = 2 * m - Z - 2 * np.diag(a4) / deg
    avg = float((x * x * mean_cost).sum())
    assert avg <= 3 * xi + TOL * scale, ("step5", avg, 3 * xi)
    us, vs = np.nonzero(np.triu(a))
    dmin = (m + deg[us] * deg[vs] - 2 * a3[us, vs]).min()
    assert dmin <= avg + TOL * scale
    counts["graphs"] += 1
    counts["step5_tight"] += int(abs(avg - 3 * xi) <= 1e-9 * scale)


def main(geng, nmax=9):
    counts = {"graphs": 0, "step2_tight": 0, "step5_tight": 0}
    for n in range(2, nmax + 1):
        res = subprocess.run([geng, "-t", "-q", "-c", str(n)], capture_output=True, text=True, check=True)
        for line in res.stdout.splitlines():
            if line.strip():
                check(graph6_to_adj(line), counts)
        print("n", n, counts, flush=True)
    rng = np.random.default_rng(13)
    fams = [("hub", (make_hub(t, k, j) for t in range(3, 40, 3) for k in range(1, 8) for j in range(0, 4) if j + 1 <= t)),
            ("double_star", (double_hub(t1, t2, md) for t1 in range(1, 25, 3) for t2 in range(1, 25, 3) for md in ("edge", "path3"))),
            ("apex", (apex_biclique_minus_matching(k) for k in range(2, 16))),
            ("random", (random_big(rng) for _ in range(150))),
            ("bipartite", (random_bipartite(rng) for _ in range(150))),
            ("trees", (random_tree(rng) for _ in range(150))),
            ("biclique_plus", (biclique_plus(rng) for _ in range(150))),
            ("spiders", (spider(d, k) for d in range(2, 10) for k in range(1, 5))),
            ("c5_blowups", c5_blowups()),
            ("c5_hub", (c5_blowup_plus_hub(sz, hc, lv) for sz in [(1, 1, 1, 1, 1), (2, 2, 2, 2, 2)] for hc in range(5) for lv in range(1, 20, 6)))]
    for name, fam in fams:
        for a in fam:
            if a.sum():
                check(a, counts)
        print(name, counts, flush=True)
    print("ALL STEPS VERIFIED on", counts["graphs"], "graphs")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 9)
