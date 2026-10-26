"""Rational recovery of the degree-2D pairwise certificate at general n (route B).

Same pipeline as deterministic/numerical-optimisation-run-2/recover5.py, on the
structures of sdp_n.build(n):
1. SDP with lambda fixed to a rational value and the margin t (smallest block
   eigenvalue off the forced null direction 1) maximised.
2. Multiplier Gram matrices: numerical least-norm projection onto the equations
   M 1 = 0 and M = M^T in orbit coordinates, rounding to denominator D, exact fix of
   the pivot coordinates (reduced row echelon form), exact positive definiteness of
   the deflated integer matrices by fraction-free LU over Z (flint), symmetry and
   M 1 = 0 checked exactly.
3. Main Gram matrix: the same projection onto the coefficient equations (with the
   exact multipliers substituted), M 1 = 0 and symmetry; exactness of the equations
   is asserted over Q.  Positive semidefiniteness of the main matrix (size C(n^2+D-1, D))
   is verified by a floating-point Cholesky factorisation of the deflated matrix
   shifted by alpha, with the rigorous rounding-error bound of Higham (Accuracy and
   Stability of Numerical Algorithms, Thm 10.3) plus the entry rounding: the matrix is
   positive definite when alpha exceeds the bound.  (At n = 5 recover5.py verifies the
   same step exactly through the isotypic projectors of G_5; at n = 6 the group has
   1036800 elements and that exact step is deferred.)
4. Save certificate<n>.json (lambda and every orbit coordinate as an exact fraction)
   and a summary.
Usage: python recover_n.py <n> <lambda> [denominator]
"""
import json
import math
import sys
import time
from fractions import Fraction as Fr

import cvxpy as cp
import flint
import numpy as np

from sdp_n import build, log

n = int(sys.argv[1])
LAMBDA = Fr(sys.argv[2])
DENOM = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 10
S = build(n)
N, Dg = S["N"], S["Dg"]
MD, MD1 = len(S["VD"].mons), len(S["VD1"].mons)
reps6, mult, PAIR_REPS = S["reps6"], S["mult"], S["PAIR_REPS"]

# ---------------------------------------------------------------- 1. SDP with fixed lambda, maximal margin
log(f"SDP with lambda = {LAMBDA}, maximising the margin")
t = cp.Variable()
cons = []


def block_vars(B, blocks, null_dir):
    vs, vec = [], []
    v = B.T @ null_dir
    for (m, d, s) in blocks:
        X = cp.Variable((m, m), symmetric=True)
        vs.append(X)
        vb = v[s:s + m * d].reshape(m, d)
        if np.linalg.norm(vb) > 1e-8:
            assert d == 1
            u = vb[:, 0] / np.linalg.norm(vb[:, 0])
            cons.append(X >> t * (np.eye(m) - np.outer(u, u)))
        else:
            cons.append(X >> t * np.eye(m))
        vec.append(cp.reshape(X, (m * m,), order="C"))
    return vs, cp.hstack(vec)


varsD, vecD = block_vars(S["BmatD"], S["blocksD"], np.ones(MD))
lhs = S["cnt"]["main"] @ (S["WD"] @ vecD)
vecs_m = {}
for typ in PAIR_REPS:
    mt = mult[typ]
    _, vecs_m[typ] = block_vars(mt["B"], mt["blocks"], np.ones(MD1))
    lhs = lhs + S["cnt"][typ] @ (mt["W"] @ vecs_m[typ])
rhs = np.array([float(S["Qrep"][int(r)] - LAMBDA * S["Drep"][int(r)]) for r in reps6])
cons.append(lhs == rhs)
prob = cp.Problem(cp.Maximize(t), cons)
try:
    prob.solve(solver="CLARABEL", max_iter=500)
except cp.error.SolverError:
    log("Clarabel failed; falling back to SCS")
    prob.solve(solver="SCS", eps=1e-9, max_iters=200000)
log(f"status {prob.status}, margin t = {t.value:.3e}")
assert t.value is not None and t.value > 0, "no strictly feasible certificate at this lambda"
m_main = S["WD"] @ vecD.value
m_mult = {typ: mult[typ]["W"] @ vecs_m[typ].value for typ in PAIR_REPS}


# ---------------------------------------------------------------- exact helpers
def fmpq_from(fr):
    return flint.fmpq(fr.numerator, fr.denominator)


def fr_from(q):
    return Fr(int(q.p), int(q.q))


def independent_rows(E):
    R, C = E.shape
    Et = flint.fmpz_mat(C, R, [int(x) for x in E.T.reshape(-1)])
    res = Et.rref()
    rr, rank = res[0], int(res[-1])
    piv = []
    for i in range(rank):
        for j in range(R):
            if rr[i, j] != 0:
                piv.append(j)
                break
    return piv


def exact_project(E, q_float, f, D):
    R, C = E.shape
    Ef = E.astype(float)
    r = np.array([float(x) for x in f]) - Ef @ q_float
    q1 = q_float + np.linalg.lstsq(Ef, r, rcond=None)[0]
    q = [Fr(int(round(x * D)), D) for x in q1]
    aug = flint.fmpq_mat(R, C + 1, [flint.fmpq(int(E[i, j])) if j < C else fmpq_from(f[i]) for i in range(R) for j in range(C + 1)])
    rr, rank = aug.rref()
    assert rank == R, "dependent or inconsistent equations"
    qp = list(q)
    pivots = [next(j for j in range(C) if rr[i, j] != 0) for i in range(R)]
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


def symmetry_rows(lab, orb, M):
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


def integer_matrix(coords, lab, M):
    L = 1
    for c in coords:
        L = L * c.denominator // math.gcd(L, c.denominator)
    ints = np.array([int(c * L) for c in coords], dtype=object)
    u = np.unique(lab)
    pos = np.searchsorted(u, lab)
    return flint.fmpz_mat(M, M, [int(x) for x in ints[pos]]), L


def is_pd(A):
    P, Lw, Dd, U = A.fflu()
    return P.is_one() and all(U[i, i] > 0 for i in range(A.nrows()))


# ---------------------------------------------------------------- 2. multiplier blocks
cert = {"n": n, "lambda": str(LAMBDA)}
q_mult = {}
for typ in PAIR_REPS:
    mt = mult[typ]
    E = np.vstack([S["rowsum"][typ], symmetry_rows(mt["lab"], mt["orb"], MD1)])
    E = E[independent_rows(E)]
    q = exact_project(E, m_mult[typ], [Fr(0)] * E.shape[0], DENOM)
    Mi, L = integer_matrix(q, mt["lab"], MD1)
    ones = flint.fmpz_mat(MD1, 1, [1] * MD1)
    assert (Mi * ones).is_zero() and (Mi - Mi.transpose()).is_zero()
    sub = flint.fmpz_mat(MD1 - 1, MD1 - 1, [int(Mi[i, j]) for i in range(MD1 - 1) for j in range(MD1 - 1)])
    pd = is_pd(sub)
    log(f"  {typ}: denominator {DENOM}: scaled denominator {L}, deflated {MD1 - 1} x {MD1 - 1} PD (exact) = {pd}")
    assert pd, f"{typ} multiplier not positive definite after rounding; increase the denominator"
    q_mult[typ] = q
    cert[typ] = [str(x) for x in q]

# ---------------------------------------------------------------- 3. main block
sym_main = symmetry_rows(S["labD"], S["orbD"], MD)
E_main = np.vstack([S["cnt"]["main"], S["rowsum"]["main"], sym_main])
f_main = [S["Qrep"][int(r)] - LAMBDA * S["Drep"][int(r)]
          - sum(Fr(int(S["cnt"][typ][ri, j])) * q_mult[typ][j] for typ in PAIR_REPS for j in np.nonzero(S["cnt"][typ][ri])[0])
          for ri, r in enumerate(reps6)] + [Fr(0)] * (S["rowsum"]["main"].shape[0] + sym_main.shape[0])
keep = independent_rows(E_main)
log(f"main: {E_main.shape[0]} equations, {len(keep)} independent")
q_main = exact_project(E_main[keep], m_main, [f_main[i] for i in keep], DENOM)
log("main: equations, M 1 = 0 and symmetry hold exactly over Q; verified floating Cholesky of the deflated matrix")
u = np.unique(S["labD"])
pos = np.searchsorted(u, S["labD"])
Af = np.array([float(x) for x in q_main])[pos].reshape(MD, MD)[:MD - 1, :MD - 1]
lam_min = float(np.linalg.eigvalsh(Af)[0])
alpha = 0.5 * lam_min
u_round = 2.0 ** -53
main_ok = False
try:
    Lc = np.linalg.cholesky(Af - alpha * np.eye(MD - 1))
    gam = MD * u_round / (1 - MD * u_round)
    err = 10 * (gam * float((Lc ** 2).sum()) + u_round * float(np.sqrt((Af ** 2).sum())) + MD * u_round * float(np.abs(Af).max()))
    main_ok = alpha > err
    log(f"  deflated {MD - 1} x {MD - 1}: smallest eigenvalue {lam_min:.4e}, alpha = {alpha:.3e}, rigorous error bound {err:.3e}: "
        f"{'positive definite (verified floating point)' if main_ok else 'INCONCLUSIVE'}")
except np.linalg.LinAlgError:
    log("  Cholesky failed")
assert main_ok
cert["main"] = [str(x) for x in q_main]
cert["main_psd_method"] = "verified floating-point Cholesky (Higham Thm 10.3 bound); exact isotypic check not run at this n"
json.dump(cert, open(f"certificate{n}.json", "w"))
log(f"saved certificate{n}.json")
