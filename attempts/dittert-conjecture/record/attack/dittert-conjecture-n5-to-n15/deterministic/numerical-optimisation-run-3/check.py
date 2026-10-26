"""Independent check for numerical optimisation run 3 (the n = 6 symmetry-reduced SDP).

Rebuilds the full Gram matrices from the saved numerical blocks and bases, evaluates
the certificate side by direct polynomial evaluation (monomial vectors; transports by
its own breadth-first search) and Q_6 - lambda D_6 from the definitions (row products,
column products, the permanent as a sum over permutations) at 200 random points of
K_6, and requires relative agreement 1e-4 and block eigenvalues above -1e-3.
"""
import itertools
import math
import sys

import numpy as np

n = 6
N = n * n
Dg = (n + 1) // 2
sol = np.load(f"sdp{n}-solution.npz", allow_pickle=True)
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


def cyc(k, lo=0):
    p = list(range(n))
    for t in range(k):
        p[lo + t] = lo + (t + 1) % k
    return p


def swap(i, j):
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return p


gens = [varperm(swap(0, 1)), varperm(cyc(n)), varperm(colp=swap(0, 1)), varperm(colp=cyc(n)), varperm(transpose=True)]
reps = {"aligned": (var(0, 0), var(0, 1)), "generic": (var(0, 0), var(1, 1))}
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
assert len(transport) == N * (N - 1) // 2


def full_gram(B, blocks, vals):
    M = np.zeros((B.shape[0], B.shape[0]))
    for (m, d, s), X in zip(blocks, vals):
        for al in range(d):
            cols = [s + k * d + al for k in range(m)]
            Bk = B[:, cols]
            M += np.einsum("ik,kl,jl->ij", Bk, X, Bk)
    return M


M0 = full_gram(sol["BmatD"], [tuple(int(t) for t in b) for b in sol["blocksD"]], list(sol["main_blocks"]))
Mrep = {typ: full_gram(sol[f"{typ}_B"], [tuple(int(t) for t in b) for b in sol[f"{typ}_blocks"]], list(sol[f"{typ}_vals"]))
        for typ in reps}
mins = [np.linalg.eigvalsh(X).min() for X in sol["main_blocks"]] + \
       [np.linalg.eigvalsh(X).min() for typ in reps for X in sol[f"{typ}_vals"]]
print(f"min block eigenvalue {min(mins):.2e}")
zD = np.array(list(itertools.combinations_with_replacement(range(N), Dg)))
zD1 = np.array(list(itertools.combinations_with_replacement(range(N), Dg - 1)))


def sigma(M, z, x):
    v = np.prod(x[z], axis=1)
    return float(np.einsum("i,ij,j->", v, M, v))


def QD(x):
    A = x.reshape(n, n)
    s = x.sum()
    per = sum(math.prod(A[i, p[i]] for i in range(n)) for p in itertools.permutations(range(n)))
    eps = n % 2
    Q = n ** n * ((2 - gamma) * (s / n) ** (2 * Dg) - (np.prod(A.sum(1)) + np.prod(A.sum(0)) - per) * (s / n) ** eps)
    D = (s / n) ** (2 * Dg - 2) * ((x ** 2).sum() - s ** 2 / N)
    return Q, D


rng = np.random.default_rng(3)
worst, qmax = 0.0, 0.0
for trial in range(200):
    x = rng.exponential(size=N) if trial % 2 else np.abs(1 / n + 0.05 * rng.standard_normal(N))
    x = n * x / x.sum()
    Q, D = QD(x)
    C = sigma(M0, zD, x)
    for pr, (typ, perm) in transport.items():
        u, v = tuple(pr)
        C += x[u] * x[v] * sigma(Mrep[typ], zD1, x[perm])
    worst = max(worst, abs(C - (Q - lam * D)))
    qmax = max(qmax, abs(Q))
print(f"lambda = {lam:.6f}; max |certificate - (Q - lambda D)| = {worst:.3e} over 200 points, max |Q| = {qmax:.3e}, relative {worst / qmax:.2e}")
ok = worst / qmax < 1e-4 and min(mins) > -1e-3
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
