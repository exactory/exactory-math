"""Independent check of certificate5.json (the exact n = 5 certificate).

The certificate lists lambda > 0 and, in orbit coordinates, three rational Gram
matrices: M0 (2925 x 2925, constant on the G_5-orbits of ordered pairs of degree-3
monomials) and M_al, M_ge (325 x 325, constant on the orbits of the stabilisers of
the pairs {x_0, x_1} and {x_0, x_6} on ordered pairs of degree-2 monomials).  The
claim is the polynomial identity

    Q - lambda D = z3^T M0 z3 + sum_{p={u,v}} x_u x_v z2(x o g_p)^T M_{type(p)} z2(x o g_p)

with every Gram matrix positive semidefinite, which proves phi(U_5) - phi(A) >=
(lambda/3125) ||A - U_5||_F^2 on K_5.

This checker recomputes everything from the definitions with its own code:
Q and D by expanding row products, column products and the permanent; the orbit
structure by label propagation over the group generators; the transports by
breadth-first search; the identity by a full expansion over all 593775 degree-6
monomials in exact integer arithmetic; M 1 = 0 exactly for every Gram matrix;
positive definiteness of the deflated multiplier matrices (324 x 324) by
fraction-free Bareiss elimination over Z (Sylvester's criterion); and positive
definiteness of the deflated main matrix (2924 x 2924) by a floating-point
Cholesky factorisation with a rigorous rounding-error bound (Higham, Accuracy
and Stability of Numerical Algorithms, Thm 10.3), reported separately as the one
step that is verified rather than exact.
"""
import itertools
import json
import math
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr

import numpy as np

n, N = 5, 25
T0 = time.time()


def log(m):
    print(f"[{time.time() - T0:6.1f}s] {m}", flush=True)


cert = json.load(open("certificate5.json"))
lam = Fr(cert["lambda"])
assert lam > 0
coords = {k: [Fr(x) for x in cert[k]] for k in ("main", "aligned", "generic")}


def var(i, j):
    return i * n + j


def vperm(rowp=None, colp=None, tr=False):
    rowp = rowp or list(range(n))
    colp = colp or list(range(n))
    g = np.zeros(N, dtype=np.int64)
    for i in range(n):
        for j in range(n):
            a, b = (j, i) if tr else (i, j)
            g[var(i, j)] = var(rowp[a], colp[b])
    return g


GENS = [vperm([1, 0, 2, 3, 4]), vperm([1, 2, 3, 4, 0]), vperm(colp=[1, 0, 2, 3, 4]), vperm(colp=[1, 2, 3, 4, 0]), vperm(tr=True)]
STAB = {"aligned": [vperm(rowp=[0, 2, 1, 3, 4]), vperm(rowp=[0, 2, 3, 4, 1]), vperm(colp=[0, 1, 3, 2, 4]),
                    vperm(colp=[0, 1, 3, 4, 2]), vperm(colp=[1, 0, 2, 3, 4])],
        "generic": [vperm(rowp=[0, 1, 3, 2, 4]), vperm(rowp=[0, 1, 3, 4, 2]), vperm(colp=[0, 1, 3, 2, 4]),
                    vperm(colp=[0, 1, 3, 4, 2]), vperm(rowp=[1, 0, 2, 3, 4], colp=[1, 0, 2, 3, 4]), vperm(tr=True)]}
REP = {"aligned": (0, 1), "generic": (0, 6)}


class Mon:
    def __init__(self, d):
        self.d = d
        self.m = np.array(list(itertools.combinations_with_replacement(range(N), d)), dtype=np.int64)
        self.w = N ** np.arange(d, dtype=np.int64)
        k = (self.m * self.w).sum(1)
        self.order = np.argsort(k)
        self.sk = k[self.order]

    def idx(self, arr):
        k = (np.sort(np.asarray(arr, dtype=np.int64), axis=-1) * self.w).sum(-1)
        p = np.searchsorted(self.sk, k)
        assert np.all(self.sk[p] == k)
        return self.order[p]


V3, V2, V6 = Mon(3), Mon(2), Mon(6)
M3, M2, M6 = len(V3.m), len(V2.m), len(V6.m)


def pair_labels(V, gs):
    M = len(V.m)
    ps = [V.idx(g[V.m]) for g in gs]
    ps += [np.argsort(p) for p in ps]
    lab = np.arange(M * M, dtype=np.int64)
    a, b = lab // M, lab % M
    while True:
        old = lab
        for p in ps:
            lab = np.minimum(lab, lab[p[a] * M + p[b]])
        if np.array_equal(old, lab):
            return lab


def expand(coordlist, lab, M):
    """Integer matrix (object array) scaled by the lcm of denominators; returns (matrix, scale)."""
    L = 1
    for c in coordlist:
        L = L * c.denominator // math.gcd(L, c.denominator)
    ints = np.array([int(c * L) for c in coordlist], dtype=object)
    u = np.unique(lab)
    assert len(u) == len(coordlist), "coordinate count does not match the orbit count"
    pos = np.searchsorted(u, lab)
    return ints[pos].reshape(M, M), L


log("orbits")
lab3 = pair_labels(V3, GENS)
Mi = {"main": expand(coords["main"], lab3, M3)}
for typ in REP:
    Mi[typ] = expand(coords[typ], pair_labels(V2, STAB[typ]), M2)
L = 1
for typ in Mi:
    L = L * Mi[typ][1] // math.gcd(L, Mi[typ][1])
scaled = {typ: Mi[typ][0] * (L // Mi[typ][1]) for typ in Mi}   # every matrix times the common scale L
for typ, A in scaled.items():
    assert np.array_equal(A, A.T), f"{typ} not symmetric"
    assert all(int(x) == 0 for x in A.sum(axis=1)), f"{typ}: M 1 != 0"
log(f"symmetry and M 1 = 0 hold exactly; common scale L has {len(str(L))} digits")

# transports
tr = {}
for typ, rep in REP.items():
    e = np.arange(N)
    tr[frozenset(rep)] = (typ, e)
    fr = [(frozenset(rep), e)]
    while fr:
        nx = []
        for pr, pm in fr:
            for g in GENS:
                im = frozenset(int(g[x]) for x in pr)
                if im not in tr:
                    tr[im] = (typ, g[pm])
                    nx.append((im, g[pm]))
        fr = nx
assert len(tr) == 300

# full expansion of the certificate side, times L
log("expanding the certificate side over all degree-6 monomials")
acc = np.zeros(M6, dtype=object)
acc[:] = 0
A0 = scaled["main"]
for a in range(M3):
    idx = V6.idx(np.concatenate([np.repeat(V3.m[a][None, :], M3, axis=0), V3.m], axis=1))
    np.add.at(acc, idx, A0[a])
for pr, (typ, pm) in tr.items():
    u, v = sorted(pr)
    ginv = np.argsort(pm)
    p2 = V2.idx(ginv[V2.m])              # index of g^{-1}(a) for every degree-2 monomial a
    Mp = scaled[typ][np.ix_(p2, p2)]      # Mp[a', b'] = M_rep[g^{-1} a', g^{-1} b']
    A2 = np.repeat(V2.m[:, None, :], M2, axis=1)
    B2 = np.repeat(V2.m[None, :, :], M2, axis=0)
    idx = V6.idx(np.concatenate([np.full((M2, M2, 2), (u, v)), A2, B2], axis=2).reshape(M2 * M2, 6))
    np.add.at(acc, idx, Mp.reshape(-1))
log("expansion done")

# Q and D from the definitions
def padd(P, Qd, c=1):
    for k, v in Qd.items():
        P[k] = P.get(k, 0) + c * v
        if P[k] == 0:
            del P[k]
    return P


def pmul(P, Qd):
    R = defaultdict(Fr)
    for k1, v1 in P.items():
        for k2, v2 in Qd.items():
            R[tuple(x + y for x, y in zip(k1, k2))] += v1 * v2
    return {k: v for k, v in R.items() if v != 0}


def lin(cf):
    P = {}
    for k, c in cf.items():
        e = [0] * N
        e[k] = 1
        P[tuple(e)] = Fr(c)
    return P


log("expanding Q and D")
s = lin({k: 1 for k in range(N)})
one = {tuple([0] * N): Fr(1)}
pr_ = dict(one)
for i in range(n):
    pr_ = pmul(pr_, lin({var(i, j): 1 for j in range(n)}))
pc_ = dict(one)
for j in range(n):
    pc_ = pmul(pc_, lin({var(i, j): 1 for i in range(n)}))
per = {}
for p in itertools.permutations(range(n)):
    e = [0] * N
    for i in range(n):
        e[var(i, p[i])] = 1
    per[tuple(e)] = Fr(1)
s2 = pmul(s, s)
s4 = pmul(s2, s2)
s6 = pmul(s4, s2)
gamma = Fr(120, 3125)
Q = {}
padd(Q, s6, Fr(3125) * (2 - gamma) / Fr(5 ** 6))
padd(Q, pmul(padd(padd(dict(pr_), pc_), per, -1), s), -Fr(3125, 5))
D = {}
for k in range(N):
    lk = lin({k: 1})
    padd(lk, s, -Fr(1, 25))
    padd(D, pmul(lk, lk))
D = {k: v / Fr(5 ** 4) for k, v in pmul(D, s4).items()}
target = {}
for e, c in Q.items():
    target[e] = target.get(e, 0) + c
for e, c in D.items():
    target[e] = target.get(e, 0) - lam * c
log("comparing coefficients")
key_of = {tuple(m): i for i, m in enumerate(V6.m)}
seen = np.zeros(M6, dtype=bool)
bad = 0
for e, c in target.items():
    t = tuple(k for k, ek in enumerate(e) for _ in range(ek))
    i = key_of[t]
    seen[i] = True
    if Fr(int(acc[i]), L) != c:
        bad += 1
for i in np.nonzero(~seen)[0]:
    if int(acc[i]) != 0:
        bad += 1
identity_ok = bad == 0
log(f"identity: {'holds exactly' if identity_ok else f'FAILS at {bad} monomials'}")

# positive definiteness of the deflated multiplier matrices: Bareiss (fraction-free) elimination over Z
def bareiss_pd(A):
    A = [[int(x) for x in row] for row in A]
    m = len(A)
    prev = 1
    for k in range(m):
        if A[k][k] <= 0:
            return False
        for i in range(k + 1, m):
            for j in range(k + 1, m):
                A[i][j] = (A[k][k] * A[i][j] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return True


mult_ok = True
for typ in REP:
    A = scaled[typ][:M2 - 1, :M2 - 1]
    ok = bareiss_pd(A)
    log(f"{typ}: deflated 324 x 324 positive definite (Bareiss over Z): {ok}")
    mult_ok &= ok

# main block: verified floating-point Cholesky of the deflated 2924 x 2924 matrix
A = scaled["main"][:M3 - 1, :M3 - 1]
Af = np.array([[float(Fr(int(x), L)) for x in row] for row in A])
u_round = 2.0 ** -53
lam_min = float(np.linalg.eigvalsh(Af)[0])
alpha = 0.5 * lam_min
main_ok = False
try:
    Lc = np.linalg.cholesky(Af - alpha * np.eye(M3 - 1))
    gam = (M3) * u_round / (1 - M3 * u_round)
    err = 10 * (gam * float((Lc ** 2).sum()) + u_round * float(np.sqrt((Af ** 2).sum())) + M3 * u_round * float(np.abs(Af).max()))
    main_ok = alpha > err
    log(f"main: deflated 2924 x 2924, floating Cholesky of A - alpha I succeeded with alpha = {alpha:.3e}, "
        f"rigorous error bound {err:.3e}: {'positive definite' if main_ok else 'inconclusive'}")
except np.linalg.LinAlgError:
    log("main: floating Cholesky failed")
ok = identity_ok and mult_ok and main_ok
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
