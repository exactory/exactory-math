"""Exact polynomial data for the n = 5 SOS residue (route B of move 1).

Variables x_0..x_24 are the entries of a 5x5 matrix, row-major (x_{5i+j} = a_ij).
With s = sum_k x_k,
  Q(x) := 5^5 [ (2 - 120/3125) (s/5)^6 - (prod_i r_i + prod_j c_j - per) (s/5) ]  (degree 6, homogeneous)
  D(x) := sum_k (x_k - s/25)^2 (s/5)^4                                            (degree 6, homogeneous)
On K_5 (s = 5): Q = 5^5 (phi(U_5) - phi(A)) and D = ||A - U_5||_F^2, so an identity
Q - lambda D = sigma_0 + sum_{p<q} x_p x_q sigma_pq with SOS sigma's proves
phi(U_5) - phi(A) >= (lambda / 3125) ||A - U_5||_F^2 on K_5.

Outputs poly5.pkl: the 593775 degree-6 monomials (sorted 6-tuples of variable
indices), their G_5-orbit labels (label propagation over five generators of
G_5 = (S_5 x S_5) x| Z_2), the orbit representatives, and the exact coefficients
of Q and D at every representative (Fractions).  Checks: Q(U_5) = D(U_5) = 0,
Q >= 0 at random rational points of K_5, and Q, D constant on every orbit.
"""
import itertools
import pickle
import random
import time
from collections import defaultdict
from fractions import Fraction as Fr

import numpy as np

n = 5
N = n * n


def var(i, j):
    return i * n + j


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
            R[tuple(a + b for a, b in zip(k1, k2))] += v1 * v2
    return {k: v for k, v in R.items() if v != 0}


def lin(coeffs):
    P = {}
    for k, c in coeffs.items():
        e = [0] * N
        e[k] = 1
        P[tuple(e)] = Fr(c)
    return P


def ppow(P, k):
    R = {tuple([0] * N): Fr(1)}
    for _ in range(k):
        R = pmul(R, P)
    return R


t0 = time.time()
s = lin({k: 1 for k in range(N)})
rows = [lin({var(i, j): 1 for j in range(n)}) for i in range(n)]
cols = [lin({var(i, j): 1 for i in range(n)}) for j in range(n)]
prodr = {tuple([0] * N): Fr(1)}
for r in rows:
    prodr = pmul(prodr, r)
prodc = {tuple([0] * N): Fr(1)}
for c in cols:
    prodc = pmul(prodc, c)
per = {}
for p in itertools.permutations(range(n)):
    e = [0] * N
    for i in range(n):
        e[var(i, p[i])] = 1
    per[tuple(e)] = Fr(1)
s4 = ppow(s, 4)
s5 = pmul(s4, s)
s6 = pmul(s5, s)
gamma = Fr(120, 3125)
phi_part = padd(padd(dict(prodr), prodc), per, -1)
Q = {}
padd(Q, s6, Fr(3125) * (2 - gamma) / Fr(5 ** 6))
padd(Q, pmul(phi_part, s), -Fr(3125, 5))
D = {}
for k in range(N):
    lk = lin({k: 1})
    padd(lk, s, -Fr(1, 25))
    padd(D, pmul(lk, lk))
D = pmul(D, s4)
D = {k: v / Fr(5 ** 4) for k, v in D.items()}
print(f"Q: {len(Q)} monomials, D: {len(D)} monomials, built in {time.time() - t0:.1f}s", flush=True)


def ev(P, x):
    tot = Fr(0)
    for e, c in P.items():
        t = c
        for k, ek in enumerate(e):
            if ek:
                t *= x[k] ** ek
        tot += t
    return tot


U = [Fr(1, 5)] * N
assert ev(Q, U) == 0 and ev(D, U) == 0, "Q or D does not vanish at U_5"
random.seed(1)
for _ in range(20):
    w = [Fr(random.randint(0, 20)) for _ in range(N)]
    tot = sum(w)
    x = [5 * v / tot for v in w]
    assert ev(Q, x) >= 0, "Q negative at a point of K_5"
print("sanity: Q(U_5) = D(U_5) = 0 and Q >= 0 at 20 random rational points of K_5", flush=True)

# degree-6 monomials as sorted 6-tuples of variable indices, and the G_5 action
mons = np.array(list(itertools.combinations_with_replacement(range(N), 6)), dtype=np.int64)
M = len(mons)
weights = N ** np.arange(6, dtype=np.int64)


def keys_of(arr):
    return (np.sort(arr, axis=1) * weights).sum(axis=1)


keys = keys_of(mons)
order = np.argsort(keys)
sorted_keys = keys[order]


def index_of(arr):
    k = keys_of(arr)
    pos = np.searchsorted(sorted_keys, k)
    assert np.all(sorted_keys[pos] == k)
    return order[pos]


def varperm(rowp, colp, transpose=False):
    g = np.zeros(N, dtype=np.int64)
    for i in range(n):
        for j in range(n):
            a, b = (j, i) if transpose else (i, j)
            g[var(i, j)] = var(rowp[a], colp[b])
    return g


ident = list(range(n))
gens = [varperm([1, 0, 2, 3, 4], ident), varperm([1, 2, 3, 4, 0], ident),
        varperm(ident, [1, 0, 2, 3, 4]), varperm(ident, [1, 2, 3, 4, 0]),
        varperm(ident, ident, transpose=True)]
perms6 = [index_of(g[mons]) for g in gens]
labels = np.arange(M, dtype=np.int64)
it = 0
while True:
    old = labels.copy()
    for p in perms6:
        labels = np.minimum(labels, labels[p])
        np.minimum.at(labels, p, labels)
    it += 1
    if np.array_equal(old, labels):
        break
reps, inv, sizes = np.unique(labels, return_inverse=True, return_counts=True)
print(f"{M} degree-6 monomials in {len(reps)} G_5-orbits (label propagation, {it} sweeps); "
      f"orbit sizes min {sizes.min()} max {sizes.max()}", flush=True)
assert sizes.sum() == M

# coefficients at representatives; check invariance on every orbit
mon_index = {tuple(m): i for i, m in enumerate(mons)}


def expo_to_tuple(e):
    return tuple(k for k, ek in enumerate(e) for _ in range(ek))


Qarr = np.zeros(M)
Darr = np.zeros(M)
Qexact = {}
Dexact = {}
for e, c in Q.items():
    Qarr[mon_index[expo_to_tuple(e)]] = float(c)
for e, c in D.items():
    Darr[mon_index[expo_to_tuple(e)]] = float(c)
for arr, name in ((Qarr, "Q"), (Darr, "D")):
    mx = np.full(len(reps), -np.inf)
    mn = np.full(len(reps), np.inf)
    np.maximum.at(mx, inv, arr)
    np.minimum.at(mn, inv, arr)
    assert np.allclose(mx, mn), f"{name} is not constant on some orbit"
for r in reps:
    t = tuple(mons[r])
    e = [0] * N
    for k in t:
        e[k] += 1
    Qexact[int(r)] = Q.get(tuple(e), Fr(0))
    Dexact[int(r)] = D.get(tuple(e), Fr(0))
pickle.dump({"mons": mons, "labels": labels, "reps": reps, "sizes": sizes,
             "Q_at_rep": Qexact, "D_at_rep": Dexact, "gens": gens},
            open("poly5.pkl", "wb"))
print("Q and D constant on every orbit; saved poly5.pkl", flush=True)
