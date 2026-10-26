"""Is there a LAPLACIAN certificate for the Dittert gap polynomial?

The certificates of units 1 and 2 need the positive semidefiniteness of a 2925 x 2925
(n = 5) or 8436 x 8436 (n = 6) rational Gram matrix, which no proof assistant can check
by kernel reduction.  This script looks for a certificate in a much smaller cone, whose
nonnegativity is checkable by inspection:

    Q_n - lambda D_n = sum_{i<j} w_ij (z_i - z_j)^2
                     + sum_{p={u,v}} x_u x_v sum_{i<j} w^p_ij (y_i - y_j)^2,    all w >= 0,

z the degree-D monomials, y the degree-(D-1) monomials.  Each square vanishes at U_n
(where every monomial takes the same value), which is exactly what the certificate needs,
and the Gram matrix of such a sum is the weighted graph Laplacian
  M_ii = sum_{j != i} w_ij,  M_ij = -w_ij,
so "w >= 0" replaces "M is positive semidefinite".

By G_n-invariance the weights are constant on orbits of unordered pairs, so the unknowns
are one w per orbit (1128 at n = 5) and the equations are one per orbit of degree-2D
monomials (156 at n = 5).  Maximising lambda is then a linear program.

Usage: python laplacian-lp.py <n>
"""
import json
import sys
import time

import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, "../deterministic/numerical-optimisation-run-3")
from sdp_n import build, log  # noqa: E402

n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
S = build(n)
reps6, mult, PAIR_REPS = S["reps6"], S["mult"], S["PAIR_REPS"]
MD, MD1 = len(S["VD"].mons), len(S["VD1"].mons)


def laplacian_map(lab, orb, M):
    """Linear map T from the unordered-pair weights w (one per unordered-pair orbit) to the
    ordered-pair orbit coordinates m of the Laplacian.  Returns (T, n_w, pair_index)."""
    u = np.unique(lab)
    npairs = len(u)
    # unordered orbit of an ordered-pair orbit k with representative (a, b): min(k, orbit(b,a))
    a_rep, b_rep = u // M, u % M
    transposed = np.array([orb[int(lab[int(b) * M + int(a)])] for a, b in zip(a_rep, b_rep)])
    undirected = np.minimum(np.arange(npairs), transposed)
    diag = a_rep == b_rep
    w_orbits = sorted(set(int(x) for x, d in zip(undirected, diag) if not d))
    w_index = {o: i for i, o in enumerate(w_orbits)}
    T = np.zeros((npairs, len(w_orbits)))
    for k in range(npairs):
        if not diag[k]:
            T[k, w_index[int(undirected[k])]] = -1.0
    # diagonal orbits: M_aa = sum over c != a of w_{orbit{a,c}}; count by scanning row a of lab
    for k in np.nonzero(diag)[0]:
        a = int(a_rep[k])
        row = lab[a * M:(a + 1) * M]
        for c, o in enumerate(row):
            if c == a:
                continue
            oi = orb[int(o)]
            T[k, w_index[int(undirected[oi])]] += 1.0
    return T, len(w_orbits), w_index


log("building the Laplacian parametrisation")
T_main, nw_main, _ = laplacian_map(S["labD"], S["orbD"], MD)
T_mult, nw_mult = {}, {}
for typ in PAIR_REPS:
    mt = mult[typ]
    T_mult[typ], nw_mult[typ], _ = laplacian_map(mt["lab"], mt["orb"], MD1)
log(f"weights: main {nw_main}, " + ", ".join(f"{t} {nw_mult[t]}" for t in PAIR_REPS))

# equations: cnt @ m = rhsQ - lambda rhsD, with m = T w
A_main = S["cnt"]["main"] @ T_main
blocks = [A_main] + [S["cnt"][t] @ T_mult[t] for t in PAIR_REPS]
rhsQ = np.array([float(S["Qrep"][int(r)]) for r in reps6])
rhsD = np.array([float(S["Drep"][int(r)]) for r in reps6])
A_eq = np.hstack(blocks + [rhsD.reshape(-1, 1)])      # last column: +lambda
nvar = A_eq.shape[1]
c = np.zeros(nvar)
c[-1] = -1.0                                          # maximise lambda
bounds = [(0, None)] * (nvar - 1) + [(None, None)]
log(f"LP: {A_eq.shape[0]} equations, {nvar} variables")
t0 = time.time()
res = linprog(c, A_eq=A_eq, b_eq=rhsQ, bounds=bounds, method="highs")
log(f"status: {res.message}")
if res.success:
    lam = res.x[-1]
    resid = np.abs(A_eq @ res.x - rhsQ).max()
    print(f"n={n}: LAPLACIAN certificate exists, lambda* = {lam:.6f}, kappa = {lam / n ** n:.6g}, "
          f"residual {resid:.2e}, min weight {res.x[:-1].min():.3e}, nonzero weights {(res.x[:-1] > 1e-12).sum()}")
    np.savez(f"laplacian-{n}.npz", x=res.x, lam=lam, nw_main=nw_main,
             **{f"nw_{t}": nw_mult[t] for t in PAIR_REPS})
    json.dump({"n": n, "lambda": lam, "kappa": lam / n ** n, "nw_main": nw_main,
               **{f"nw_{t}": nw_mult[t] for t in PAIR_REPS}}, open(f"laplacian-{n}.json", "w"), indent=1)
else:
    print(f"n={n}: NO Laplacian certificate at this template ({res.message})")
