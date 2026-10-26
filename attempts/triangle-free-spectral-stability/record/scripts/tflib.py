"""Exact edit distance to a complete bipartite graph plus isolates, spectral deficit,
and the candidate certificates for triangle-free graphs.

Conventions. G is a simple graph with adjacency matrix A (0/1 symmetric). m = e(G),
lam = spectral radius, xi = m - lam^2 (the Nosal deficit; xi >= 0 for triangle-free G).
D(G) = min over disjoint A, B of |E(G) symmetric-difference E(K_{A,B})|.

Writing gain(A, B) = 2 e(A, B) - |A||B|, D(G) = m - max gain(A, B). For a fixed A the
best B is {w not in A : 2 d_A(w) > |A|}, so D(G) is a minimum over the 2^n choices of A.
"""
import itertools

import numpy as np


def adjacency_from_edges(n, edges):
    a = np.zeros((n, n), dtype=np.int64)
    for u, v in edges:
        a[u, v] = 1
        a[v, u] = 1
    return a


def edit_distance_exact(a):
    """D(G) by enumerating every A-part (2^n subsets); exact integer arithmetic."""
    n = a.shape[0]
    m = int(a.sum()) // 2
    if n == 0:
        return 0
    masks = np.arange(1 << n, dtype=np.int64)
    members = ((masks[:, None] >> np.arange(n)) & 1).astype(np.int64)  # (2^n, n)
    sizes = members.sum(axis=1)
    d_a = members @ a  # d_A(w) for every subset A and vertex w
    contrib = np.maximum(0, 2 * d_a - sizes[:, None]) * (1 - members)
    best_gain = int(contrib.sum(axis=1).max())
    return m - best_gain


def edit_distance_with_parts(a):
    """D(G) together with one optimal pair (A, B)."""
    n = a.shape[0]
    m = int(a.sum()) // 2
    masks = np.arange(1 << n, dtype=np.int64)
    members = ((masks[:, None] >> np.arange(n)) & 1).astype(np.int64)
    sizes = members.sum(axis=1)
    d_a = members @ a
    contrib = np.maximum(0, 2 * d_a - sizes[:, None]) * (1 - members)
    gains = contrib.sum(axis=1)
    k = int(gains.argmax())
    part_a = [v for v in range(n) if members[k, v]]
    part_b = [w for w in range(n) if not members[k, w] and 2 * d_a[k, w] > sizes[k]]
    return m - int(gains[k]), part_a, part_b


def spectral_data(a):
    """Largest eigenvalue and a unit eigenvector with nonnegative entries."""
    if a.shape[0] == 0:
        return 0.0, np.zeros(0)
    vals, vecs = np.linalg.eigh(a.astype(float))
    lam = float(vals[-1])
    x = vecs[:, -1]
    if x.sum() < 0:
        x = -x
    x = np.abs(x)  # for disconnected graphs the Perron vector is not unique; abs keeps a valid unit vector
    return lam, x


def is_triangle_free(a):
    return int(np.trace(a @ a @ a)) == 0


def is_bipartite(a):
    n = a.shape[0]
    colour = [-1] * n
    for s in range(n):
        if colour[s] >= 0:
            continue
        colour[s] = 0
        stack = [s]
        while stack:
            u = stack.pop()
            for v in np.nonzero(a[u])[0]:
                if colour[v] < 0:
                    colour[v] = 1 - colour[u]
                    stack.append(int(v))
                elif colour[v] == colour[u]:
                    return False
    return True


def edge_certificates(a):
    """For each edge uv: cost of the target K_{N(v), N(u)} (LLN form), computed directly
    and by the closed formula m + d(u)d(v) - 2 (A^3)_{uv}, valid for triangle-free G."""
    n = a.shape[0]
    m = int(a.sum()) // 2
    deg = a.sum(axis=1)
    a3 = a @ a @ a
    out = []
    for u in range(n):
        for v in range(u + 1, n):
            if a[u, v]:
                nu = np.nonzero(a[u])[0]
                nv = np.nonzero(a[v])[0]
                target = set()
                for p in nv:
                    for q in nu:
                        if p != q:
                            target.add((min(p, q), max(p, q)))
                edges = {(min(p, q), max(p, q)) for p in range(n) for q in range(p + 1, n) if a[p, q]}
                direct = len(edges ^ target)
                formula = m + int(deg[u] * deg[v]) - 2 * int(a3[u, v])
                out.append((u, v, direct, formula))
    return out


def vertex_certificates(a):
    """For each vertex v: the untruncated target K_{N(v), V - N(v)} and the truncated
    target K_{N(v), B*} with B* = {w not in N(v): 2|N(v) and N(w)| > d(v)}."""
    n = a.shape[0]
    m = int(a.sum()) // 2
    deg = a.sum(axis=1)
    a2 = a @ a  # codegrees, with a2[v, v] = d(v)
    out = []
    for v in range(n):
        d = int(deg[v])
        nbr = a[v].astype(bool)
        # edges with both ends outside N[v]
        outside = ~nbr
        outside[v] = False
        s_v = int(a[np.ix_(outside, outside)].sum()) // 2
        untruncated = d * (n - d) - m + 2 * s_v
        b_star = [w for w in range(n) if not nbr[w] and 2 * int(a2[v, w]) > d]
        e_ab = int(a[np.ix_(np.nonzero(nbr)[0], b_star)].sum()) if b_star else 0
        truncated = m + d * len(b_star) - 2 * e_ab
        out.append((v, untruncated, truncated, s_v))
    return out


def analyse(a):
    """All statistics for one graph as a dict (floats where spectral)."""
    n = a.shape[0]
    m = int(a.sum()) // 2
    lam, x = spectral_data(a)
    xi = m - lam * lam
    dist = edit_distance_exact(a)
    deg = a.sum(axis=1)
    rec = {"n": n, "m": m, "lam2": lam * lam, "xi": xi, "D": dist,
           "bipartite": is_bipartite(a), "triangle_free": is_triangle_free(a)}
    if m > 0:
        certs = edge_certificates(a)
        costs = np.array([c[2] for c in certs], dtype=float)
        formula_ok = all(c[2] == c[3] for c in certs)
        weights = np.array([x[c[0]] * x[c[1]] for c in certs])
        rec["edge_min"] = float(costs.min())
        rec["edge_mean"] = float(costs.mean())
        rec["edge_perron_mean"] = float((weights * costs).sum() / weights.sum()) if weights.sum() > 0 else None
        rec["edge_formula_ok"] = formula_ok
        vcerts = vertex_certificates(a)
        rec["vertex_untrunc_min"] = min(c[1] for c in vcerts)
        rec["vertex_trunc_min"] = min(c[2] for c in vcerts)
        l1 = x / x.sum() if x.sum() > 0 else x
        rec["vertex_untrunc_perron_l1_mean"] = float(sum(l1[c[0]] * c[1] for c in vcerts))
        rec["s_perron_l1_mean"] = float(sum(l1[c[0]] * c[3] for c in vcerts))  # should equal xi (LLN identity) when connected
        rec["max_degree"] = int(deg.max())
    return rec
