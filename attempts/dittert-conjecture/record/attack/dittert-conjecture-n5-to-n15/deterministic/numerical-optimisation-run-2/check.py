"""Independent check for numerical optimisation run 2 (the n = 5 symmetry-reduced SDP).

Reconstructs the certificate polynomial from the saved numerical solution by direct
evaluation (no coefficient matching, no orbit machinery shared with sdp5.py):
    C(x) = sigma_0(x) + sum_{p = {u,v}} x_u x_v sigma_{type(p)}(x o g_p),
with sigma_0(x) = z3(x)^T M0 z3(x), M0 = sum_rho sum_alpha B_{rho,alpha} X_rho B_{rho,alpha}^T,
and compares it with Q(x) - lambda D(x), where Q and D are evaluated from their
definitions (row products, column products, the permanent by permutations) at
random points of K_5.  Also checks that every block is PSD to 1e-4.  Passes when
the relative residual max |C - (Q - lambda D)| / max |Q| is below 1e-4 at 200 points.
"""
import itertools
import math
import sys

import numpy as np

n, N = 5, 25
sol = np.load("sdp5-solution.npz", allow_pickle=True)
lam = float(sol["lam"])
gamma = math.factorial(n) / n ** n


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


ident = list(range(n))
gens = [varperm([1, 0, 2, 3, 4]), varperm([1, 2, 3, 4, 0]), varperm(colp=[1, 0, 2, 3, 4]),
        varperm(colp=[1, 2, 3, 4, 0]), varperm(transpose=True)]
reps = {"aligned": (0, 1), "generic": (0, 6)}
transport = {}
for typ, rep in reps.items():
    e = np.arange(N)
    transport[frozenset(rep)] = (typ, e)
    frontier = [(frozenset(rep), e)]
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


def full_gram(B, blocks, vals):
    M = np.zeros((B.shape[0], B.shape[0]))
    for (m, d, s), X in zip(blocks, vals):
        for al in range(d):
            cols = [s + k * d + al for k in range(m)]
            Bk = B[:, cols]
            M += np.einsum("ik,kl,jl->ij", Bk, X, Bk)
    return M


M0 = full_gram(sol["Bmat3"], [tuple(int(t) for t in b) for b in sol["blocks3"]], list(sol["main_blocks"]))
Mrep = {typ: full_gram(sol[f"{typ}_B"], [tuple(int(t) for t in b) for b in sol[f"{typ}_blocks"]], list(sol[f"{typ}_vals"]))
        for typ in reps}
mins = [np.linalg.eigvalsh(X).min() for X in sol["main_blocks"]] + \
       [np.linalg.eigvalsh(X).min() for typ in reps for X in sol[f"{typ}_vals"]]
print(f"min block eigenvalue {min(mins):.2e}")
z3 = np.array(list(itertools.combinations_with_replacement(range(N), 3)))
z2 = np.array(list(itertools.combinations_with_replacement(range(N), 2)))


def sigma(M, z, x):
    v = np.prod(x[z], axis=1)
    return float(np.einsum("i,ij,j->", v, M, v))


def QD(x):
    A = x.reshape(n, n)
    s = x.sum()
    per = sum(math.prod(A[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n)))
    Q = 3125 * ((2 - gamma) * (s / 5) ** 6 - (np.prod(A.sum(1)) + np.prod(A.sum(0)) - per) * (s / 5))
    D = ((x - s / 25) ** 2).sum() * (s / 5) ** 4
    return Q, D


rng = np.random.default_rng(3)
worst, qmax = 0.0, 0.0
for trial in range(200):
    x = rng.exponential(size=N) if trial % 2 else np.abs(0.2 + 0.05 * rng.standard_normal(N))
    x = 5 * x / x.sum()
    Q, D = QD(x)
    C = sigma(M0, z3, x)
    for pr, (typ, perm) in transport.items():
        u, v = tuple(pr)
        C += x[u] * x[v] * sigma(Mrep[typ], z2, x[perm])
    worst = max(worst, abs(C - (Q - lam * D)))
    qmax = max(qmax, abs(Q))
print(f"lambda = {lam:.6f}; max |certificate - (Q - lambda D)| = {worst:.3e} over 200 points, max |Q| = {qmax:.3e}, relative {worst / qmax:.2e}")
ok = worst / qmax < 1e-4 and min(mins) > -1e-4
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
