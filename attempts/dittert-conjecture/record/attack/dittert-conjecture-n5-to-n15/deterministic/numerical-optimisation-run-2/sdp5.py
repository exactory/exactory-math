"""Symmetry-reduced SDP for the n = 5 pairwise SOS template (numerical optimisation run).

Certificate template (homogeneous, degree 6):
    Q - lambda D = sigma_0 + sum_{p} x_p sigma_p,
where p runs over the 300 unordered pairs {u, v} of distinct entries, x_p = x_u x_v,
sigma_0 = z3^T M0 z3 (z3 = the 2925 monomials of degree 3), sigma_p = z2^T Mp z2
(z2 = the 325 monomials of degree 2), every Gram matrix PSD.

Symmetry: G = (S_5 x S_5) x| Z_2 acts on entries; Q and D are G-invariant, so a
certificate can be taken G-invariant (average it).  Then M0 commutes with G, and
the pairs fall into two G-orbits (aligned: same row or column, 100 pairs; generic:
different rows and columns, 200 pairs); for each orbit one Gram matrix M_rep,
invariant under the stabiliser H_rep of the representative pair, and Mp is its
transport.  Every invariant Gram matrix is block-diagonalised numerically by the
two-generic-element method (Murota-Kanno-Kojima-Kojima 2010): the eigenspaces of
one random invariant matrix R1 are the (irrep, copy) pieces; a second random
invariant matrix R2 links the copies of one irrep and aligns their bases.  The
SDP variables are the small blocks; the linear constraints are the coefficient
equations at one representative of each G-orbit of degree-6 monomials (both sides
are invariant, so representatives suffice).

Output: the optimal lambda (evidence), the block structure, residuals, and the
numerical Gram data (blocks and bases) in sdp5-solution.npz for later recovery.
"""
import itertools
import pickle
import sys
import time

import cvxpy as cp
import numpy as np

n = 5
N = n * n
t_start = time.time()
data = pickle.load(open("poly5.pkl", "rb"))
mons6, labels6, reps6 = data["mons"], data["labels"], data["reps"]
Qrep, Drep, gens = data["Q_at_rep"], data["D_at_rep"], data["gens"]


def log(msg):
    print(f"[{time.time() - t_start:7.1f}s] {msg}", flush=True)


class MonoIndex:
    def __init__(self, d):
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


V3, V2 = MonoIndex(3), MonoIndex(2)
assert np.array_equal(MonoIndex(6).mons, mons6)
M3, M2 = len(V3.mons), len(V2.mons)


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


def pair_orbits(V, gs):
    """Orbit label (= smallest pair id in the orbit) of every ordered pair of monomials of V."""
    M = len(V.mons)
    perms = [V.index(g[V.mons]) for g in gs]
    perms += [np.argsort(p) for p in perms]
    lab = np.arange(M * M, dtype=np.int64)
    a, b = lab // M, lab % M
    sweeps = 0
    while True:
        old = lab.copy()
        for p in perms:
            lab = np.minimum(lab, lab[p[a] * M + p[b]])
        sweeps += 1
        if np.array_equal(old, lab):
            return lab, sweeps


def block_diagonalise(lab, M, rng, tol=1e-6):
    """Numerical symmetry-adapted basis for the algebra of matrices constant on the pair orbits `lab`.
    Returns (Bmat, blocks) with Bmat orthogonal (M x M) and blocks = [(m, d, start)]: columns
    start .. start + m*d hold copies alpha = 0..d-1 of the m basis vectors of one irrep, ordered
    (k, alpha) with alpha fastest."""
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
        B1 = V[:, cl[0]]
        cols = [B1]
        for c in cl[1:]:
            Bk = np.einsum("ij,jk->ik", V[:, c], Y[np.ix_(c, cl[0])])
            nrm = np.linalg.norm(Bk[:, 0])
            Bk = Bk / nrm
            assert np.allclose(np.einsum("ji,jk->ik", Bk, Bk), np.eye(d), atol=1e-6), "copy basis not orthonormal"
            cols.append(Bk)
        for k, Bk in enumerate(cols):
            Bmat[:, col + k * d: col + (k + 1) * d] = Bk
        blocks.append((m, d, col))
        col += m * d
    assert col == M
    assert np.allclose(np.einsum("ji,jk->ik", Bmat, Bmat), np.eye(M), atol=1e-6)
    # verification on a fresh invariant matrix: block form, alpha-independent, zero across irreps
    Z = np.einsum("ji,jk->ik", Bmat, R3, optimize=True)
    Z = np.einsum("ij,jk->ik", Z, Bmat, optimize=True)
    err = 0.0
    for (m, d, s) in blocks:
        T = Z[s:s + m * d, s:s + m * d].reshape(m, d, m, d)
        X = T[:, 0, :, 0]
        for al in range(d):
            for be in range(d):
                target = X if al == be else np.zeros_like(X)
                err = max(err, np.abs(T[:, al, :, be] - target).max())
    off = Z.copy()
    for (m, d, s) in blocks:
        off[s:s + m * d, s:s + m * d] = 0
    err = max(err, np.abs(off).max())
    assert err < 1e-6 * np.abs(Z).max(), f"block verification failed: {err}"
    return Bmat, blocks


def W_matrix(lab, M, Bmat, blocks):
    """Rows: pair orbits (ordered by label); columns: block variables (rho, k, l). W[O, (rho,k,l)] =
    sum_alpha B[a,(rho,k,alpha)] B[b,(rho,l,alpha)] at the representative pair (a, b) of O."""
    u = np.unique(lab)
    a, b = u // M, u % M
    parts = []
    for (m, d, s) in blocks:
        Ba = Bmat[a][:, s:s + m * d].reshape(len(u), m, d)
        Bb = Bmat[b][:, s:s + m * d].reshape(len(u), m, d)
        parts.append(np.einsum("kmd,knd->kmn", Ba, Bb).reshape(len(u), m * m))
    W = np.concatenate(parts, axis=1)
    return W, {int(o): i for i, o in enumerate(u)}


rng = np.random.default_rng(20260903)

# ---- main block: G-invariant Gram over degree-3 monomials
log("main block: pair orbits under G on 2925^2 pairs")
lab3, sw = pair_orbits(V3, gens)
K3 = len(np.unique(lab3))
log(f"  {K3} pair orbits ({sw} sweeps); expected 1128 from the character computation")
assert K3 == 1128
Bmat3, blocks3 = block_diagonalise(lab3, M3, rng)
log("  main blocks (m x m, copies d): " + ", ".join(f"{m}({d})" for m, d, _ in sorted(blocks3, reverse=True)))
assert sum(m * m for m, d, _ in blocks3) == K3
W3, orb3 = W_matrix(lab3, M3, Bmat3, blocks3)

# ---- multiplier blocks: two pair-orbit representatives with their stabilisers
pair_reps = {"aligned": (0, 1), "generic": (0, 6)}
stab_gens = {
    "aligned": [varperm(rowp=[0, 2, 1, 3, 4]), varperm(rowp=[0, 2, 3, 4, 1]),
                varperm(colp=[0, 1, 3, 2, 4]), varperm(colp=[0, 1, 3, 4, 2]), varperm(colp=[1, 0, 2, 3, 4])],
    "generic": [varperm(rowp=[0, 1, 3, 2, 4]), varperm(rowp=[0, 1, 3, 4, 2]),
                varperm(colp=[0, 1, 3, 2, 4]), varperm(colp=[0, 1, 3, 4, 2]),
                varperm(rowp=[1, 0, 2, 3, 4], colp=[1, 0, 2, 3, 4]), varperm(transpose=True)],
}
for typ, (u0, v0) in pair_reps.items():
    for g in stab_gens[typ]:
        assert {g[u0], g[v0]} == {u0, v0}, f"stabiliser generator of {typ} does not fix the pair"
    # closure size of the stabiliser (sanity against the orbit-stabiliser theorem)
    seen = {tuple(range(N))}
    frontier = [tuple(range(N))]
    while frontier:
        nxt = []
        for h in frontier:
            for g in stab_gens[typ]:
                hg = tuple(g[list(h)])
                if hg not in seen:
                    seen.add(hg)
                    nxt.append(hg)
        frontier = nxt
    log(f"  stabiliser of the {typ} pair has order {len(seen)} (expected {28800 // (100 if typ == 'aligned' else 200)})")
    assert len(seen) == 28800 // (100 if typ == "aligned" else 200)

# transport: for every pair p a variable permutation g_p with g_p(rep) = p, by BFS over the generators
transport = {}
for typ, rep in pair_reps.items():
    ident = tuple(range(N))
    transport[frozenset(rep)] = (typ, np.array(ident))
    frontier = [(frozenset(rep), np.array(ident))]
    while frontier:
        nxt = []
        for pr, perm in frontier:
            for g in gens:
                img = frozenset(int(g[x]) for x in pr)
                if img not in transport:
                    transport[img] = (typ, g[perm])
                    nxt.append((img, g[perm]))
        frontier = nxt
assert len(transport) == 300
assert sum(1 for t, _ in transport.values() if t == "aligned") == 100
for pr, (typ, perm) in transport.items():
    assert frozenset(int(perm[x]) for x in pair_reps[typ]) == pr

mult = {}
for typ in pair_reps:
    log(f"multiplier block ({typ}): pair orbits under the stabiliser on 325^2 pairs")
    lab2, sw = pair_orbits(V2, stab_gens[typ])
    K2 = len(np.unique(lab2))
    B2, bl2 = block_diagonalise(lab2, M2, rng)
    W2, orb2 = W_matrix(lab2, M2, B2, bl2)
    log(f"  {K2} orbits; blocks: " + ", ".join(f"{m}({d})" for m, d, _ in sorted(bl2, reverse=True)))
    mult[typ] = dict(lab=lab2, B=B2, blocks=bl2, W=W2, orb=orb2, nvar=W2.shape[1])

# ---- constraints at the degree-6 orbit representatives
log(f"assembling {len(reps6)} coefficient constraints")
nv3 = W3.shape[1]
nvar = {"main": nv3, **{typ: mult[typ]["nvar"] for typ in mult}}
rows = {k: np.zeros((len(reps6), v)) for k, v in nvar.items()}
rhsQ = np.zeros(len(reps6))
rhsD = np.zeros(len(reps6))
for ri, r in enumerate(reps6):
    mu = tuple(int(x) for x in mons6[r])
    rhsQ[ri], rhsD[ri] = float(Qrep[int(r)]), float(Drep[int(r)])
    # main: distinct ordered factorisations mu = a * b, a, b of degree 3
    seen = set()
    for S in itertools.combinations(range(6), 3):
        a = tuple(mu[i] for i in S)
        b = tuple(mu[i] for i in range(6) if i not in S)
        seen.add((a, b))
    for a, b in seen:
        ia, ib = int(V3.index(a)), int(V3.index(b))
        rows["main"][ri] += W3[orb3[int(lab3[ia * M3 + ib])]]
    # multipliers: x_u x_v with u != v both in mu, remaining degree-4 part split into two quadratics
    distinct = sorted(set(mu))
    for u, v in itertools.combinations(distinct, 2):
        rest = list(mu)
        rest.remove(u)
        rest.remove(v)
        typ, perm = transport[frozenset((u, v))]
        ginv = np.argsort(perm)
        seen = set()
        for S in itertools.combinations(range(4), 2):
            a = tuple(rest[i] for i in S)
            b = tuple(rest[i] for i in range(4) if i not in S)
            seen.add((a, b))
        mt = mult[typ]
        for a, b in seen:
            ia = int(V2.index(ginv[list(a)]))
            ib = int(V2.index(ginv[list(b)]))
            rows[typ][ri] += mt["W"][mt["orb"][int(mt["lab"][ia * M2 + ib])]]

# ---- the SDP
log("building the SDP")
lam = cp.Variable()


def block_vars(blocks):
    vs, cons, vec = [], [], []
    for (m, d, s) in blocks:
        X = cp.Variable((m, m), symmetric=True)
        vs.append(X)
        cons.append(X >> 0)
        vec.append(cp.reshape(X, (m * m,), order="C"))
    return vs, cons, cp.hstack(vec)


vars3, cons, vec3 = block_vars(blocks3)
lhs = rows["main"] @ vec3
vars_mult = {}
for typ in mult:
    vs, cs, vec = block_vars(mult[typ]["blocks"])
    vars_mult[typ] = vs
    cons += cs
    lhs = lhs + rows[typ] @ vec
cons.append(lhs + lam * rhsD == rhsQ)
prob = cp.Problem(cp.Maximize(lam), cons)
solver = sys.argv[1] if len(sys.argv) > 1 else "CLARABEL"
log(f"solving with {solver}: {sum(v.size for v in vars3) + sum(v.size for vs in vars_mult.values() for v in vs)} block entries, {len(reps6)} equations")
prob.solve(solver=solver, verbose=False)
log(f"status {prob.status}, lambda* = {lam.value}")
if lam.value is not None:
    resid = np.abs(rows["main"] @ vec3.value + sum(rows[t] @ np.hstack([v.value.reshape(-1) for v in vars_mult[t]]) for t in mult) + lam.value * rhsD - rhsQ).max()
    log(f"max equation residual {resid:.2e}; kappa = lambda/3125 = {lam.value / 3125:.6g}")
    mins = [np.linalg.eigvalsh(v.value).min() for v in vars3] + [np.linalg.eigvalsh(v.value).min() for vs in vars_mult.values() for v in vs]
    log(f"min eigenvalue over all blocks {min(mins):.2e}")
    np.savez("sdp5-solution.npz", lam=lam.value, Bmat3=Bmat3, blocks3=np.array(blocks3),
             main_blocks=np.array([v.value for v in vars3], dtype=object),
             **{f"{t}_B": mult[t]["B"] for t in mult}, **{f"{t}_blocks": np.array(mult[t]["blocks"]) for t in mult},
             **{f"{t}_vals": np.array([v.value for v in vars_mult[t]], dtype=object) for t in mult})
    log("saved sdp5-solution.npz")
