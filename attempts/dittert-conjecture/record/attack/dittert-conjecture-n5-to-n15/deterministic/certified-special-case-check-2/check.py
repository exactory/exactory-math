"""Independent check of certificate<n>.json (general n; here n = 6).

Same design as certified-special-case-check-1/check.py, with n read from the
certificate: recomputes Q_n and D_n from the definitions, the orbit structure by
label propagation, the transports by breadth-first search; expands the certificate
side over all degree-2D monomials in exact integer arithmetic and compares with
Q_n - lambda D_n coefficient by coefficient; checks M 1 = 0 and symmetry exactly;
positive definiteness of the deflated multiplier matrices by Bareiss elimination
over Z; positive definiteness of the deflated main matrix by a floating-point
Cholesky factorisation with Higham's rigorous bound (Thm 10.3).
"""
import itertools
import json
import math
import sys
import time
from collections import defaultdict
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


cert = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "certificate6.json"))
n = int(cert["n"])
N = n * n
Dg = (n + 1) // 2
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


def cyc(k, lo=0):
    p = list(range(n))
    for t in range(k):
        p[lo + t] = lo + (t + 1) % k
    return p


def swap(i, j):
    p = list(range(n))
    p[i], p[j] = p[j], p[i]
    return p


GENS = [vperm(swap(0, 1)), vperm(cyc(n)), vperm(colp=swap(0, 1)), vperm(colp=cyc(n)), vperm(tr=True)]
STAB = {"aligned": [vperm(swap(1, 2)), vperm(cyc(n - 1, 1)), vperm(colp=swap(2, 3)), vperm(colp=cyc(n - 2, 2)), vperm(colp=swap(0, 1))],
        "generic": [vperm(swap(2, 3)), vperm(cyc(n - 2, 2)), vperm(colp=swap(2, 3)), vperm(colp=cyc(n - 2, 2)),
                    vperm(rowp=swap(0, 1), colp=swap(0, 1)), vperm(tr=True)]}
REP = {"aligned": (var(0, 0), var(0, 1)), "generic": (var(0, 0), var(1, 1))}
for typ, (u0, v0) in REP.items():
    for g in STAB[typ]:
        assert {int(g[u0]), int(g[v0])} == {u0, v0}


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


VD, VD1, V6 = Mon(Dg), Mon(Dg - 1), Mon(2 * Dg)
MD, MD1, M6 = len(VD.m), len(VD1.m), len(V6.m)


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
    L = 1
    for c in coordlist:
        L = L * c.denominator // math.gcd(L, c.denominator)
    ints = np.array([int(c * L) for c in coordlist], dtype=object)
    u = np.unique(lab)
    assert len(u) == len(coordlist), "coordinate count does not match the orbit count"
    return ints[np.searchsorted(u, lab)].reshape(M, M), L


log("orbits")
labD = pair_labels(VD, GENS)
Mi = {"main": expand(coords["main"], labD, MD)}
for typ in REP:
    Mi[typ] = expand(coords[typ], pair_labels(VD1, STAB[typ]), MD1)
L = 1
for typ in Mi:
    L = L * Mi[typ][1] // math.gcd(L, Mi[typ][1])
scaled = {typ: Mi[typ][0] * (L // Mi[typ][1]) for typ in Mi}
for typ, A in scaled.items():
    assert np.array_equal(A, A.T), f"{typ} not symmetric"
    assert all(int(x) == 0 for x in A.sum(axis=1)), f"{typ}: M 1 != 0"
log(f"symmetry and M 1 = 0 hold exactly; common scale L has {len(str(L))} digits")

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
assert len(tr) == N * (N - 1) // 2

log("expanding the certificate side over all monomials")
maxabs = max(int(np.abs(scaled[t]).max()) for t in scaled)
use_int64 = maxabs * 200 < 2 ** 62      # every coefficient is a sum of at most 90 scaled entries
acc = np.zeros(M6, dtype=np.int64 if use_int64 else object)
if not use_int64:
    acc[:] = 0
log(f"largest scaled entry {maxabs:.3e}; accumulating in {'int64' if use_int64 else 'Python integers'}")
scaled = {t: (scaled[t].astype(np.int64) if use_int64 else scaled[t]) for t in scaled}
A0 = scaled["main"]
for a in range(MD):
    idx = V6.idx(np.concatenate([np.repeat(VD.m[a][None, :], MD, axis=0), VD.m], axis=1))
    np.add.at(acc, idx, A0[a])
A2 = np.repeat(VD1.m[:, None, :], MD1, axis=1)
B2 = np.repeat(VD1.m[None, :, :], MD1, axis=0)
for pr, (typ, pm) in tr.items():
    u, v = sorted(pr)
    ginv = np.argsort(pm)
    p2 = VD1.idx(ginv[VD1.m])
    Mp = scaled[typ][np.ix_(p2, p2)]
    idx = V6.idx(np.concatenate([np.full((MD1, MD1, 2), (u, v)), A2, B2], axis=2).reshape(MD1 * MD1, 2 * Dg))
    np.add.at(acc, idx, Mp.reshape(-1))
log("expansion done")


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


log("expanding Q and D from the definitions")
s = lin({k: 1 for k in range(N)})
one = {tuple([0] * N): Fr(1)}
spow = {0: one}
for k in range(1, 2 * Dg + 1):
    spow[k] = pmul(spow[k - 1], s)
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
gamma = Fr(math.factorial(n), n ** n)
eps = n % 2
Q = {}
padd(Q, spow[2 * Dg], Fr(n ** n) * (2 - gamma) / Fr(n ** (2 * Dg)))
padd(Q, pmul(padd(padd(dict(pr_), pc_), per, -1), spow[eps]), -Fr(n ** n) / Fr(n ** eps))
sq = {}
for k in range(N):
    e = [0] * N
    e[k] = 2
    sq[tuple(e)] = Fr(1)
padd(sq, spow[2], -Fr(1, N))
D = {k: v / Fr(n ** (2 * Dg - 2)) for k, v in pmul(sq, spow[2 * Dg - 2]).items()}
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


def bareiss_pd(A):
    """Sylvester's criterion by fraction-free (Bareiss) elimination over Z, vectorised
    on numpy object arrays of Python integers: every pivot is a leading principal minor."""
    A = np.array([[int(x) for x in row] for row in A], dtype=object)
    m = len(A)
    prev = 1
    for k in range(m):
        piv = A[k, k]
        if piv <= 0:
            return False
        if k + 1 < m:
            A[k + 1:, k + 1:] = (piv * A[k + 1:, k + 1:] - np.outer(A[k + 1:, k], A[k, k + 1:])) // prev
        prev = piv
    return True


mult_ok = True
for typ in REP:
    ok = bareiss_pd(scaled[typ][:MD1 - 1, :MD1 - 1])
    log(f"{typ}: deflated {MD1 - 1} x {MD1 - 1} positive definite (Bareiss over Z): {ok}")
    mult_ok &= ok

A = scaled["main"][:MD - 1, :MD - 1]
Af = A.astype(np.float64) / float(L)     # two correctly rounded operations per entry: relative error below 2u, covered below
u_round = 2.0 ** -53
lam_min = float(np.linalg.eigvalsh(Af)[0])
alpha = 0.5 * lam_min
main_ok = False
try:
    Lc = np.linalg.cholesky(Af - alpha * np.eye(MD - 1))
    gam = MD * u_round / (1 - MD * u_round)
    err = 10 * (gam * float((Lc ** 2).sum()) + 3 * u_round * float(np.sqrt((Af ** 2).sum())) + MD * u_round * float(np.abs(Af).max()))
    main_ok = alpha > err
    log(f"main: deflated {MD - 1} x {MD - 1}, floating Cholesky of A - alpha I succeeded with alpha = {alpha:.3e}, "
        f"rigorous error bound {err:.3e}: {'positive definite' if main_ok else 'inconclusive'}")
except np.linalg.LinAlgError:
    log("main: floating Cholesky failed")
ok = identity_ok and mult_ok and main_ok
print("CHECK", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
