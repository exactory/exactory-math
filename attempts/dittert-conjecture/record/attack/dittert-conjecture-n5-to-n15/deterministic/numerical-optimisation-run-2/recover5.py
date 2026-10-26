"""Exact rational recovery of the n = 5 certificate (route B, plan steps 4-5).

1. Solve the symmetry-reduced SDP with lambda fixed to a rational value (default 32)
   and the margin t = min block eigenvalue (off the forced null direction) maximised,
   so that rounding has room.
2. Round the multiplier Gram matrices in orbit coordinates to a common denominator,
   project them exactly onto the equations M 1 = 0 (the certificate must vanish at
   U_5, where every monomial vector is a multiple of 1), and verify positive
   definiteness of the deflated matrices exactly (fraction-free LU over Z).
3. Solve the main Gram matrix's orbit coordinates exactly from the coefficient
   equations and M 1 = 0, as the point of the affine solution space nearest the
   rounded numerical solution.
4. Verify the main Gram matrix positive semidefinite exactly through the rational
   isotypic projectors of G_5 (characters of S_5 by Murnaghan-Nakayama, wreath-product
   extension), reducing to blocks of size at most 560.
5. Save certificate5.json: lambda and every orbit coordinate as exact fractions.
"""
import itertools
import json
import math
import sys
import time
from fractions import Fraction as Fr

import cvxpy as cp
import flint
import numpy as np
import scipy.linalg

from sdpcore5 import GENS, PAIR_REPS, N, build, log, n, var

sys.path.insert(0, "../../study/gate-symmetry-blocks")
from blocks import class_size, mn_char, partitions  # noqa: E402

LAMBDA = Fr(sys.argv[1]) if len(sys.argv) > 1 else Fr(32)
DENOMS = [int(sys.argv[2])] if len(sys.argv) > 2 else [10 ** 10, 10 ** 12]
S = build()
V3, V2 = S["V3"], S["V2"]
M3, M2 = len(V3.mons), len(V2.mons)

# ---------------------------------------------------------------- 1. SDP with fixed lambda, maximal margin
log(f"SDP with lambda = {LAMBDA}, maximising the margin")
t = cp.Variable()
cons = []


def block_vars(B, blocks, null_dir):
    """Variables per block; the block carrying the null direction gets X v = 0 and X >= t off v."""
    vs, vec = [], []
    v = B.T @ null_dir
    for (m, d, s) in blocks:
        X = cp.Variable((m, m), symmetric=True)
        vs.append(X)
        vb = v[s:s + m * d].reshape(m, d)
        if np.linalg.norm(vb) > 1e-8:
            assert d == 1, "null direction outside a one-copy block"
            u = vb[:, 0] / np.linalg.norm(vb[:, 0])
            cons.append(X >> t * (np.eye(m) - np.outer(u, u)))
        else:
            cons.append(X >> t * np.eye(m))
        vec.append(cp.reshape(X, (m * m,), order="C"))
    return vs, cp.hstack(vec)


vars3, vec3 = block_vars(S["Bmat3"], S["blocks3"], np.ones(M3))
lhs = S["cnt"]["main"] @ (S["W3"] @ vec3)
vars_m, vecs_m = {}, {}
for typ in PAIR_REPS:
    mt = S["mult"][typ]
    vars_m[typ], vecs_m[typ] = block_vars(mt["B"], mt["blocks"], np.ones(M2))
    lhs = lhs + S["cnt"][typ] @ (mt["W"] @ vecs_m[typ])
rhs = np.array([float(S["Qrep"][int(r)] - LAMBDA * S["Drep"][int(r)]) for r in S["reps6"]])
cons.append(lhs == rhs)
prob = cp.Problem(cp.Maximize(t), cons)
try:
    prob.solve(solver="CLARABEL", max_iter=500)
except cp.error.SolverError:
    log("Clarabel failed; falling back to SCS")
    prob.solve(solver="SCS", eps=1e-9, max_iters=200000)
log(f"status {prob.status}, margin t = {t.value:.3e}")
assert t.value is not None and t.value > 0, "no strictly feasible certificate at this lambda"
m_main = S["W3"] @ vec3.value
m_mult = {typ: S["mult"][typ]["W"] @ vecs_m[typ].value for typ in PAIR_REPS}

# ---------------------------------------------------------------- exact helpers
def fmpq_from(fr):
    return flint.fmpq(fr.numerator, fr.denominator)


def fr_from(q):
    return Fr(int(q.p), int(q.q))


def exact_project(E, q_float, f, D):
    """A rational point q' with E q' = f near the numerical q_float: first the least-norm
    numerical correction onto E q = f, then rounding to denominator D, then the exact
    (and tiny) fix of the pivot coordinates of the reduced row echelon form of [E | f]."""
    R, C = E.shape
    Ef = E.astype(float)
    r = np.array([float(x) for x in f]) - Ef @ q_float
    q1 = q_float + np.linalg.lstsq(Ef, r, rcond=None)[0]
    q = [Fr(int(round(x * D)), D) for x in q1]
    aug = flint.fmpq_mat(R, C + 1, [flint.fmpq(int(x)) for x in E.reshape(-1)] and
                         [flint.fmpq(int(E[i, j])) if j < C else fmpq_from(f[i]) for i in range(R) for j in range(C + 1)])
    rr, rank = aug.rref()
    assert rank == R, "dependent or inconsistent equations"
    qp = list(q)
    pivots = []
    for i in range(R):
        p = next(j for j in range(C) if rr[i, j] != 0)
        pivots.append(p)
    pivset = set(pivots)
    for i, p in enumerate(pivots):
        val = fr_from(rr[i, C])
        for j in range(C):
            if j != p and j not in pivset and rr[i, j] != 0:
                val -= fr_from(rr[i, j]) * q[j]
        qp[p] = val
    Eq = flint.fmpq_mat(R, C, [flint.fmpq(int(x)) for x in E.reshape(-1)])
    res = Eq * flint.fmpq_mat(C, 1, [fmpq_from(x) for x in qp]) - flint.fmpq_mat(R, 1, [fmpq_from(x) for x in f])
    assert all(res[i, 0] == 0 for i in range(R))
    return qp


def independent_rows(E):
    """Indices of a maximal independent set of rows of the integer matrix E (exact)."""
    R, C = E.shape
    Et = flint.fmpz_mat(C, R, [int(x) for x in E.T.reshape(-1)])
    res = Et.rref()          # fmpz_mat.rref returns (rref, denominator, rank)
    rr, rank = res[0], int(res[-1])
    piv = []
    for i in range(rank):
        for j in range(R):
            if rr[i, j] != 0:
                piv.append(j)
                break
    return piv


def integer_matrix(coords, lab, M):
    """The M x M matrix with entry coords[orbit(a,b)] (Fractions) scaled to integers; returns (fmpz_mat, denominator)."""
    L = 1
    for c in coords:
        L = L * c.denominator // math.gcd(L, c.denominator)
    ints = np.array([int(c * L) for c in coords], dtype=object)
    u = np.unique(lab)
    pos = {int(o): i for i, o in enumerate(u)}
    idx = np.array([pos[int(o)] for o in lab], dtype=np.int64)
    flat = [int(ints[i]) for i in idx]
    return flint.fmpz_mat(M, M, flat), L


def is_pd(A):
    """Exact test: A (fmpz_mat, symmetric) positive definite via fraction-free LU (no pivoting needed for PD)."""
    P, Lw, D, U = A.fflu()
    if not P.is_one():
        return False
    return all(U[i, i] > 0 for i in range(A.nrows()))


def delete_rc(A, k):
    keep = [i for i in range(A.nrows()) if i != k]
    return flint.fmpz_mat(len(keep), len(keep), [int(A[i, j]) for i in keep for j in keep])


def symmetry_rows(lab, orb, M):
    """Rows m_O - m_{O^T} = 0 for every orbit O of ordered pairs whose transpose orbit differs."""
    u = np.unique(lab)
    rows = []
    for i, o in enumerate(u):
        a, b = int(o) // M, int(o) % M
        j = orb[int(lab[b * M + a])]
        if j > i:
            r = np.zeros(len(u), dtype=np.int64)
            r[i], r[j] = 1, -1
            rows.append(r)
    return np.array(rows, dtype=np.int64).reshape(-1, len(u))


# ---------------------------------------------------------------- 2. multiplier blocks
cert = {"lambda": str(LAMBDA)}
q_mult = {}
for typ in PAIR_REPS:
    mt = S["mult"][typ]
    E = np.vstack([S["rowsum"][typ], symmetry_rows(mt["lab"], mt["orb"], M2)])
    keep = independent_rows(E)
    E = E[keep]
    for D in DENOMS:
        q = exact_project(E, m_mult[typ], [Fr(0)] * E.shape[0], D)
        Mi, L = integer_matrix(q, mt["lab"], M2)
        ones = flint.fmpz_mat(M2, 1, [1] * M2)
        assert (Mi * ones).is_zero()
        assert (Mi - Mi.transpose()).is_zero(), "multiplier Gram matrix not symmetric"
        pd = is_pd(delete_rc(Mi, M2 - 1))
        log(f"  {typ}: denominator {D}: scaled denominator {L}, deflated 324 x 324 PD = {pd}")
        if pd:
            q_mult[typ] = q
            cert[typ] = [str(x) for x in q]
            break
    assert typ in q_mult, f"no denominator worked for {typ}"

# ---------------------------------------------------------------- 3. main block, exact projection
sym_main = symmetry_rows(S["lab3"], S["orb3"], M3)
E_main = np.vstack([S["cnt"]["main"], S["rowsum"]["main"], sym_main])
f_main = [S["Qrep"][int(r)] - LAMBDA * S["Drep"][int(r)]
          - sum(Fr(int(S["cnt"][typ][ri, j])) * q_mult[typ][j] for typ in PAIR_REPS for j in np.nonzero(S["cnt"][typ][ri])[0])
          for ri, r in enumerate(S["reps6"])] + [Fr(0)] * (S["rowsum"]["main"].shape[0] + sym_main.shape[0])
keep = independent_rows(E_main)
log(f"main: {E_main.shape[0]} equations, {len(keep)} independent")
E_main, f_main = E_main[keep], [f_main[i] for i in keep]
q_main = None
for D in DENOMS:
    q = exact_project(E_main, m_main, f_main, D)
    M0i, L0 = integer_matrix(q, S["lab3"], M3)
    ones = flint.fmpz_mat(M3, 1, [1] * M3)
    assert (M0i * ones).is_zero()
    assert (M0i - M0i.transpose()).is_zero(), "main Gram matrix not symmetric"
    log(f"  main: denominator {D}: scaled denominator has {len(str(L0))} digits; checking PSD via isotypic projectors")
    # ---- isotypic projectors of G_5 on degree-3 monomials
    parts = list(partitions(n))
    chi = {lam: {mu: mn_char(lam, mu) for mu in parts} for lam in parts}
    dim = {lam: chi[lam][(1,) * n] for lam in parts}

    def ctype(p):
        seen, out = [False] * n, []
        for i in range(n):
            if not seen[i]:
                L, x = 0, i
                while not seen[x]:
                    seen[x] = True
                    x = p[x]
                    L += 1
                out.append(L)
        return tuple(sorted(out, reverse=True))

    perms = list(itertools.permutations(range(n)))
    irreps = []
    for i, lam in enumerate(parts):
        for mu in parts[i + 1:]:
            irreps.append(("pair", lam, mu, 2 * dim[lam] * dim[mu]))
        irreps.append(("diag+", lam, lam, dim[lam] ** 2))
        irreps.append(("diag-", lam, lam, dim[lam] ** 2))
    elems, chis = [], []
    for sg in perms:
        for pi in perms:
            for eps in (0, 1):
                g = np.zeros(N, dtype=np.int64)
                for i in range(n):
                    for j in range(n):
                        g[var(i, j)] = var(sg[j], pi[i]) if eps else var(sg[i], pi[j])
                elems.append(g)
                ts, tp = ctype(sg), ctype(pi)
                tps = ctype(tuple(pi[sg[i]] for i in range(n)))
                row = []
                for kind, lam, mu, d in irreps:
                    if eps == 0:
                        row.append(chi[lam][ts] * chi[mu][tp] + (chi[mu][ts] * chi[lam][tp] if kind == "pair" else 0)
                                   if kind == "pair" else chi[lam][ts] * chi[lam][tp])
                    else:
                        row.append(0 if kind == "pair" else (chi[lam][tps] if kind == "diag+" else -chi[lam][tps]))
                chis.append(row)
    chis = np.array(chis, dtype=np.int64).T          # irreps x |G|
    Tact = np.zeros((len(elems), M3), dtype=np.int16)  # g -> image of every degree-3 monomial
    for gi, g in enumerate(elems):
        Tact[gi] = V3.index(g[V3.mons])
    u3 = np.unique(S["lab3"])
    a_rep, b_rep = u3 // M3, u3 % M3
    Pint = np.zeros((len(irreps), len(u3)), dtype=np.int64)   # sum of chi over {g : g(b) = a}, per pair orbit
    for oi in range(len(u3)):
        mask = Tact[:, b_rep[oi]] == a_rep[oi]
        Pint[:, oi] = chis[:, mask].sum(axis=1)
    orbpos = S["orb3"]
    idx3 = np.array([orbpos[int(o)] for o in S["lab3"]], dtype=np.int64)
    G = 28800
    all_pd = True
    checked = 0
    for ri_, (kind, lam, mu, d) in enumerate(irreps):
        Pf = Pint[ri_][idx3].reshape(M3, M3)          # integer multiple of the projector: P = d/|G| * Pf
        tr = int(Pf.trace())
        assert (d * tr) % G == 0
        md = d * tr // G
        if md == 0:
            continue
        checked += md
        # coordinate columns spanning the isotypic component: pivoted QR on the numerical basis of this component
        Pfl = Pf.astype(float)
        _, _, piv = scipy.linalg.qr(Pfl, pivoting=True, mode="economic")   # rank-revealing: first md pivots span Im P
        cols = list(piv[:md])
        trivial = (kind == "diag+" and lam == (n,))
        if trivial:
            cols = cols[:md - 1]
        C = flint.fmpz_mat(M3, len(cols), [int(Pf[i, j]) for i in range(M3) for j in cols])
        if trivial:
            C = flint.fmpz_mat(M3, md, [1 if j == 0 else int(Pf[i, cols[j - 1]]) for i in range(M3) for j in range(md)])
        assert C.rank() == md, f"chosen columns do not span the {kind}{lam}{mu} component"
        Nrho = C.transpose() * (M0i * C)
        if trivial:
            assert all(Nrho[0, j] == 0 for j in range(md))
            Nrho = delete_rc(Nrho, 0)
        pd = is_pd(Nrho)
        log(f"    irrep {kind} {lam} {mu}: dim {d}, multiplicity {md // d}, block {md}{' (deflated)' if trivial else ''}: PD = {pd}")
        all_pd &= pd
    assert checked == M3
    if all_pd:
        q_main = q
        cert["main"] = [str(x) for x in q]
        log(f"  main block positive semidefinite exactly (denominator {D})")
        break
assert q_main is not None, "main block recovery failed at every denominator"
json.dump(cert, open("certificate5.json", "w"))
log("saved certificate5.json")
