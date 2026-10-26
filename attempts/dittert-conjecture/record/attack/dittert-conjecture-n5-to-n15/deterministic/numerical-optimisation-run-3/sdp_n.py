"""Symmetry-reduced SOS relaxation of the Dittert gap polynomial at general n (numerical).

Generalises deterministic/numerical-optimisation-run-2 (n = 5) to any n: with
D = ceil(n/2), s = sum x, gamma_n = n!/n^n and eps = n mod 2,

    Q_n = n^n [ (2 - gamma_n) (s/n)^{2D} - (prod_i r_i + prod_j c_j - per) (s/n)^eps ]   (degree 2D),
    D_n = (s/n)^{2D-2} ( sum_k x_k^2 - s^2/n^2 )                                        (degree 2D),

so that on K_n: Q_n = n^n (phi(U_n) - phi(A)) and D_n = ||A - U_n||_F^2.  Template:
Q_n - lambda D_n = sigma_0 + sum_{p={u,v}} x_u x_v sigma_p, sigma_0 a Gram form in the
degree-D monomials, sigma_p a Gram form in the degree-(D-1) monomials, all G_n-invariant
(G_n = (S_n x S_n) x| Z_2), block-diagonalised numerically as in run 2.
Usage: python sdp_n.py <n> [solver]   (prints lambda*, saves sdp<n>-solution.npz)
The same code as a module: build(n) returns every structure; recover_n.py uses it.
"""
import itertools
import math
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


class MonoIndex:
    def __init__(self, N, d):
        self.d = d
        self.mons = np.array(list(itertools.combinations_with_replacement(range(N), d)), dtype=np.int64)
        self.w = N ** np.arange(d, dtype=np.int64)
        self.keys = (self.mons * self.w).sum(1)
        self.order = np.argsort(self.keys)
        self.sk = self.keys[self.order]

    def index(self, arr):
        arr = np.asarray(arr, dtype=np.int64)
        k = (np.sort(arr, axis=-1) * self.w).sum(-1)
        pos = np.searchsorted(self.sk, k)
        assert np.all(self.sk[pos] == k)
        return self.order[pos]


def orbits(V, gs):
    M = len(V.mons)
    perms = [V.index(g[V.mons]) for g in gs]
    perms += [np.argsort(p) for p in perms]
    lab = np.arange(M, dtype=np.int64)
    while True:
        old = lab
        for p in perms:
            lab = np.minimum(lab, lab[p])
        if np.array_equal(old, lab):
            return lab


def pair_orbits(V, gs):
    M = len(V.mons)
    perms = [V.index(g[V.mons]) for g in gs]
    perms += [np.argsort(p) for p in perms]
    lab = np.arange(M * M, dtype=np.int64)
    a, b = lab // M, lab % M
    while True:
        old = lab
        for p in perms:
            lab = np.minimum(lab, lab[p[a] * M + p[b]])
        if np.array_equal(old, lab):
            return lab


def block_diagonalise(lab, M, rng, tol=1e-6):
    u, inv = np.unique(lab, return_inverse=True)
    K = len(u)

    def rand_inv():
        R = rng.standard_normal(K)[inv].reshape(M, M)
        return (R + R.T) / 2

    R1, R2, R3 = rand_inv(), rand_inv(), rand_inv()
    w, V = np.linalg.eigh(R1)
    scale = np.abs(w).max()
    clusters, start = [], 0
    for i in range(1, M + 1):
        if i == M or w[i] - w[i - 1] > tol * scale:
            clusters.append(list(range(start, i)))
            start = i
    Y = np.einsum("ji,jk->ik", V, R2, optimize=True)
    Y = np.einsum("ij,jk->ik", Y, V, optimize=True)
    yscale = np.abs(Y).max()
    parent = list(range(len(clusters)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            if len(clusters[i]) == len(clusters[j]) and np.abs(Y[np.ix_(clusters[i], clusters[j])]).max() > tol * yscale:
                parent[find(i)] = find(j)
    groups = {}
    for i in range(len(clusters)):
        groups.setdefault(find(i), []).append(i)
    Bmat = np.zeros((M, M))
    blocks, col = [], 0
    for g in groups.values():
        cl = [clusters[i] for i in g]
        d = len(cl[0])
        assert all(len(c) == d for c in cl)
        m = len(cl)
        cols = [V[:, cl[0]]]
        for c in cl[1:]:
            Bk = np.einsum("ij,jk->ik", V[:, c], Y[np.ix_(c, cl[0])])
            Bk = Bk / np.linalg.norm(Bk[:, 0])
            assert np.allclose(np.einsum("ji,jk->ik", Bk, Bk), np.eye(d), atol=1e-6)
            cols.append(Bk)
        for k, Bk in enumerate(cols):
            Bmat[:, col + k * d: col + (k + 1) * d] = Bk
        blocks.append((m, d, col))
        col += m * d
    assert col == M
    Z = np.einsum("ji,jk->ik", Bmat, R3, optimize=True)
    Z = np.einsum("ij,jk->ik", Z, Bmat, optimize=True)
    err = 0.0
    for (m, d, s) in blocks:
        Tm = Z[s:s + m * d, s:s + m * d].reshape(m, d, m, d)
        X = Tm[:, 0, :, 0]
        for al in range(d):
            for be in range(d):
                err = max(err, np.abs(Tm[:, al, :, be] - (X if al == be else 0)).max())
    off = Z.copy()
    for (m, d, s) in blocks:
        off[s:s + m * d, s:s + m * d] = 0
    err = max(err, np.abs(off).max())
    assert err < 1e-6 * np.abs(Z).max(), f"block verification failed: {err}"
    return Bmat, blocks


def W_matrix(lab, M, Bmat, blocks):
    u = np.unique(lab)
    a, b = u // M, u % M
    parts = []
    for (m, d, s) in blocks:
        Ba = Bmat[a][:, s:s + m * d].reshape(len(u), m, d)
        Bb = Bmat[b][:, s:s + m * d].reshape(len(u), m, d)
        parts.append(np.einsum("kmd,knd->kmn", Ba, Bb).reshape(len(u), m * m))
    return np.concatenate(parts, axis=1), {int(o): i for i, o in enumerate(u)}


def padd(P, Q, c=1):
    for k, v in Q.items():
        P[k] = P.get(k, 0) + c * v
        if P[k] == 0:
            del P[k]
    return P


def pmul(P, Q):
    R = defaultdict(Fr)
    for k1, v1 in P.items():
        for k2, v2 in Q.items():
            R[tuple(x + y for x, y in zip(k1, k2))] += v1 * v2
    return {k: v for k, v in R.items() if v != 0}


def build(n, seed=20260903):
    N = n * n
    Dg = (n + 1) // 2

    def var(i, j):
        return i * n + j

    def varperm(rowp=None, colp=None, transpose=False):
        rowp = rowp or list(range(n))
        colp = colp or list(range(n))
        g = np.zeros(N, dtype=np.int64)
        for i in range(n):
            for j in range(n):
                a, b = (j, i) if transpose else (i, j)
                g[var(i, j)] = var(rowp[a], colp[b])
        return g

    def cyc(k, lo=0):
        p = list(range(n))
        for t in range(k):
            p[lo + t] = lo + (t + 1) % k
        return p

    def swap(i, j):
        p = list(range(n))
        p[i], p[j] = p[j], p[i]
        return p

    def lin(cf):
        P = {}
        for k, c in cf.items():
            e = [0] * N
            e[k] = 1
            P[tuple(e)] = Fr(c)
        return P

    GENS = [varperm(swap(0, 1)), varperm(cyc(n)), varperm(colp=swap(0, 1)), varperm(colp=cyc(n)), varperm(transpose=True)]
    PAIR_REPS = {"aligned": (var(0, 0), var(0, 1)), "generic": (var(0, 0), var(1, 1))}
    STAB_GENS = {
        "aligned": [varperm(swap(1, 2)), varperm(cyc(n - 1, 1)), varperm(colp=swap(2, 3)) if n > 3 else None,
                    varperm(colp=cyc(n - 2, 2)), varperm(colp=swap(0, 1))],
        "generic": [varperm(swap(2, 3)), varperm(cyc(n - 2, 2)), varperm(colp=swap(2, 3)), varperm(colp=cyc(n - 2, 2)),
                    varperm(rowp=swap(0, 1), colp=swap(0, 1)), varperm(transpose=True)],
    }
    STAB_GENS = {k: [g for g in v if g is not None] for k, v in STAB_GENS.items()}
    for typ, (u0, v0) in PAIR_REPS.items():
        for g in STAB_GENS[typ]:
            assert {int(g[u0]), int(g[v0])} == {u0, v0}

    log(f"n = {n}, D = {Dg}: expanding Q_n and D_n")
    s = lin({k: 1 for k in range(N)})
    one = {tuple([0] * N): Fr(1)}
    spow = {0: one}
    for k in range(1, 2 * Dg + 1):
        spow[k] = pmul(spow[k - 1], s)
    prodr = dict(one)
    for i in range(n):
        prodr = pmul(prodr, lin({var(i, j): 1 for j in range(n)}))
    prodc = dict(one)
    for j in range(n):
        prodc = pmul(prodc, lin({var(i, j): 1 for i in range(n)}))
    per = {}
    for p in itertools.permutations(range(n)):
        e = [0] * N
        for i in range(n):
            e[var(i, p[i])] = 1
        per[tuple(e)] = Fr(1)
    gamma = Fr(math.factorial(n), n ** n)
    eps = n % 2
    phi_part = padd(padd(dict(prodr), prodc), per, -1)
    Q = {}
    padd(Q, spow[2 * Dg], Fr(n ** n) * (2 - gamma) / Fr(n ** (2 * Dg)))
    padd(Q, pmul(phi_part, spow[eps]), -Fr(n ** n) / Fr(n ** eps))
    sq = {}
    for k in range(N):
        e = [0] * N
        e[k] = 2
        sq[tuple(e)] = Fr(1)
    padd(sq, spow[2], -Fr(1, N))
    Dp = {k: v / Fr(n ** (2 * Dg - 2)) for k, v in pmul(sq, spow[2 * Dg - 2]).items()}
    log(f"Q_n: {len(Q)} monomials, D_n: {len(Dp)} monomials")

    V6 = MonoIndex(N, 2 * Dg)
    VD, VD1 = MonoIndex(N, Dg), MonoIndex(N, Dg - 1)
    M6, MD, MD1 = len(V6.mons), len(VD.mons), len(VD1.mons)
    lab6 = orbits(V6, GENS)
    reps6 = np.unique(lab6)
    log(f"{M6} degree-{2 * Dg} monomials in {len(reps6)} orbits; main Gram {MD}, multiplier Grams {MD1}")

    def coeff_at(P, r):
        e = [0] * N
        for k in V6.mons[r]:
            e[k] += 1
        return P.get(tuple(e), Fr(0))

    Qrep = {int(r): coeff_at(Q, r) for r in reps6}
    Drep = {int(r): coeff_at(Dp, r) for r in reps6}

    rng = np.random.default_rng(seed)
    log("main block: pair orbits")
    labD = pair_orbits(VD, GENS)
    log(f"  {len(np.unique(labD))} pair orbits; block diagonalisation")
    BmatD, blocksD = block_diagonalise(labD, MD, rng)
    log("  main blocks: " + ", ".join(f"{m}({d})" for m, d, _ in sorted(blocksD, reverse=True)))
    WD, orbD = W_matrix(labD, MD, BmatD, blocksD)

    transport = {}
    for typ, rep in PAIR_REPS.items():
        e = np.arange(N)
        transport[frozenset(rep)] = (typ, e)
        frontier = [(frozenset(rep), e)]
        while frontier:
            nxt = []
            for pr, perm in frontier:
                for g in GENS:
                    img = frozenset(int(g[x]) for x in pr)
                    if img not in transport:
                        transport[img] = (typ, g[perm])
                        nxt.append((img, g[perm]))
            frontier = nxt
    assert len(transport) == N * (N - 1) // 2
    mult = {}
    for typ in PAIR_REPS:
        lab2 = pair_orbits(VD1, STAB_GENS[typ])
        B2, bl2 = block_diagonalise(lab2, MD1, rng)
        W2, orb2 = W_matrix(lab2, MD1, B2, bl2)
        log(f"  multiplier ({typ}): {len(np.unique(lab2))} pair orbits; blocks: " + ", ".join(f"{m}({d})" for m, d, _ in sorted(bl2, reverse=True)))
        mult[typ] = dict(lab=lab2, B=B2, blocks=bl2, W=W2, orb=orb2, mono_orb=orbits(VD1, STAB_GENS[typ]))

    log(f"assembling {len(reps6)} constraints (block coordinates and integer orbit counts)")
    rows = {"main": np.zeros((len(reps6), WD.shape[1])), **{typ: np.zeros((len(reps6), mult[typ]["W"].shape[1])) for typ in mult}}
    cnt = {"main": np.zeros((len(reps6), len(orbD)), dtype=np.int64), **{typ: np.zeros((len(reps6), len(mult[typ]["orb"])), dtype=np.int64) for typ in mult}}
    for ri, r in enumerate(reps6):
        mu = tuple(int(x) for x in V6.mons[r])
        seen = set()
        for Ss in itertools.combinations(range(2 * Dg), Dg):
            seen.add((tuple(mu[i] for i in Ss), tuple(mu[i] for i in range(2 * Dg) if i not in Ss)))
        for a, b in seen:
            ia, ib = int(VD.index(a)), int(VD.index(b))
            o = orbD[int(labD[ia * MD + ib])]
            rows["main"][ri] += WD[o]
            cnt["main"][ri, o] += 1
        for u, v in itertools.combinations(sorted(set(mu)), 2):
            rest = list(mu)
            rest.remove(u)
            rest.remove(v)
            typ, perm = transport[frozenset((u, v))]
            ginv = np.argsort(perm)
            seen = set()
            for Ss in itertools.combinations(range(2 * Dg - 2), Dg - 1):
                seen.add((tuple(rest[i] for i in Ss), tuple(rest[i] for i in range(2 * Dg - 2) if i not in Ss)))
            mt = mult[typ]
            for a, b in seen:
                ia, ib = int(VD1.index(ginv[list(a)])), int(VD1.index(ginv[list(b)]))
                o = mt["orb"][int(mt["lab"][ia * MD1 + ib])]
                rows[typ][ri] += mt["W"][o]
                cnt[typ][ri, o] += 1

    def rowsum_matrix(lab, mono_orb, orb, M):
        reps = np.unique(mono_orb)
        RS = np.zeros((len(reps), len(orb)), dtype=np.int64)
        for i, a in enumerate(reps):
            for o in lab[a * M:(a + 1) * M]:
                RS[i, orb[int(o)]] += 1
        return RS

    rowsum = {"main": rowsum_matrix(labD, orbits(VD, GENS), orbD, MD),
              **{typ: rowsum_matrix(mult[typ]["lab"], mult[typ]["mono_orb"], mult[typ]["orb"], MD1) for typ in mult}}
    return dict(n=n, N=N, Dg=Dg, V6=V6, VD=VD, VD1=VD1, reps6=reps6, Qrep=Qrep, Drep=Drep, labD=labD, BmatD=BmatD,
                blocksD=blocksD, WD=WD, orbD=orbD, transport=transport, mult=mult, rows=rows, cnt=cnt, rowsum=rowsum,
                PAIR_REPS=PAIR_REPS, GENS=GENS, STAB_GENS=STAB_GENS)


def solve_max_lambda(S, solver="CLARABEL"):
    import cvxpy as cp
    lam = cp.Variable()

    def block_vars(blocks):
        vs, cons, vec = [], [], []
        for (m, d, s_) in blocks:
            X = cp.Variable((m, m), symmetric=True)
            vs.append(X)
            cons.append(X >> 0)
            vec.append(cp.reshape(X, (m * m,), order="C"))
        return vs, cons, cp.hstack(vec)

    rows, mult, reps6 = S["rows"], S["mult"], S["reps6"]
    rhsQ = np.array([float(S["Qrep"][int(r)]) for r in reps6])
    rhsD = np.array([float(S["Drep"][int(r)]) for r in reps6])
    varsD, cons, vecD = block_vars(S["blocksD"])
    lhs = rows["main"] @ vecD
    vars_m = {}
    for typ in mult:
        vs, cs, vec = block_vars(mult[typ]["blocks"])
        vars_m[typ] = vs
        cons += cs
        lhs = lhs + rows[typ] @ vec
    cons.append(lhs + lam * rhsD == rhsQ)
    prob = cp.Problem(cp.Maximize(lam), cons)
    nv = sum(v.size for v in varsD) + sum(v.size for vs in vars_m.values() for v in vs)
    log(f"solving with {solver}: {nv} block entries, {len(reps6)} equations")
    prob.solve(solver=solver, verbose=False)
    n = S["n"]
    log(f"status {prob.status}, lambda* = {lam.value}, kappa = lambda/n^n = {None if lam.value is None else lam.value / n ** n:.6g}")
    if lam.value is not None:
        mins = [np.linalg.eigvalsh(v.value).min() for v in varsD] + [np.linalg.eigvalsh(v.value).min() for vs in vars_m.values() for v in vs]
        resid = np.abs(rows["main"] @ vecD.value + sum(rows[t] @ np.hstack([v.value.reshape(-1) for v in vars_m[t]]) for t in mult) + lam.value * rhsD - rhsQ).max()
        log(f"max residual {resid:.2e}, min block eigenvalue {min(mins):.2e}")
        np.savez(f"sdp{n}-solution.npz", lam=lam.value, BmatD=S["BmatD"], blocksD=np.array(S["blocksD"]),
                 main_blocks=np.array([v.value for v in varsD], dtype=object),
                 **{f"{t}_B": mult[t]["B"] for t in mult}, **{f"{t}_blocks": np.array(mult[t]["blocks"]) for t in mult},
                 **{f"{t}_vals": np.array([v.value for v in vars_m[t]], dtype=object) for t in mult})
    return lam.value


if __name__ == "__main__":
    n_ = int(sys.argv[1])
    solver_ = sys.argv[2] if len(sys.argv) > 2 else "CLARABEL"
    solve_max_lambda(build(n_), solver_)
