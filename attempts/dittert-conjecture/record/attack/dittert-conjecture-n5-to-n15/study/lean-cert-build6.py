"""Build and pre-verify, in Python, exactly the check Lean will run on the n = 6 certificate.

The n = 5 check (`lean-cert-build.py`) is exact throughout: an integer Cholesky of
`F^2 (A + d J) - delta I` followed by a Gershgorin diagonal-dominance test on the residual.
At n = 6 the main Gram is 8436 x 8436, so that route needs about 3e11 big-integer operations
and three 71-million-entry integer arrays, which is out of reach inside Lean.  The two 666 x 666
multiplier Grams stay on the exact route; the main Gram moves to a verified floating-point
Cholesky, the same criterion `check_verified.py` already uses at this dimension:

    M := Af + d - alpha I,   Af = A / den   (all entries, so J is added, not a row deleted)

    a floating-point Cholesky of M that runs to completion gives M + Delta = Lc Lc^T with
    |Delta| <= gamma_{m+1} |Lc| |Lc^T|   (Higham, Accuracy and Stability of Numerical
    Algorithms, 2nd ed., Thm 10.3), so ||Delta||_2 <= gamma_{m+1} sum Lc^2 =: err_chol.
    Adding the rounding of Af itself and of the shift gives the bound `err` below, with a
    factor 10 of safety.  `alpha > err` proves Af + d J is positive definite.

Adding `d J` rather than deleting a row and column is what makes the margin comfortable:
`A . 1 = 0`, so `lambda_min(A + d J) = min(lambda_2(A), d * dim)`, and deleting a row instead
costs a factor of `dim` in conditioning.  At n = 6 that is a factor of 8436.

Usage: python lean-cert-build6.py <certificate6.json> <out.json>
"""
import json
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
LIM = 2 ** 62
U = 2.0 ** -53


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def int_cholesky(Bd, dim):
    N = np.zeros((dim, dim), dtype=np.int64)
    for i in range(dim):
        s = int(Bd[i, i]) - (int(N[i, :i] @ N[i, :i]) if i else 0)
        if s <= 0:
            raise SystemExit(f"integer Cholesky failed at pivot {i}: {s} <= 0")
        nii = math.isqrt(s)
        if nii == 0:
            raise SystemExit(f"integer Cholesky pivot {i} is zero")
        N[i, i] = nii
        if i + 1 < dim:
            t = Bd[i + 1:, i] - (N[i + 1:, :i] @ N[i, :i] if i else 0)
            N[i + 1:, i] = t // nii
    return N


cert = json.load(open(sys.argv[1]))
out_path = sys.argv[2] if len(sys.argv) > 2 else "lean-cert6.json"
n = int(cert["n"])
lam = Fr(cert["lambda"])
sys.path.insert(0, "../deterministic/numerical-optimisation-run-3")
from sdp_n import build  # noqa: E402

S = build(n)
MD, MD1 = len(S["VD"].mons), len(S["VD1"].mons)
log(f"n = {n}, lambda = {lam}, main Gram {MD}, multiplier Grams {MD1}")
out = {"n": n, "lambda_num": str(lam.numerator), "lambda_den": str(lam.denominator)}


def orbit_matrix(name, lab, dim):
    coords = [Fr(x) for x in cert[name]]
    den = 1
    for c in coords:
        den = den * c.denominator // math.gcd(den, c.denominator)
    vals = [int(c * den) for c in coords]
    u = np.unique(lab)
    assert len(u) == len(coords), f"{name}: {len(coords)} values for {len(u)} orbits"
    A = np.array(vals, dtype=np.int64)[np.searchsorted(u, lab)].reshape(dim, dim)
    assert (A == A.T).all(), f"{name}: not symmetric"
    assert (A.sum(axis=1) == 0).all(), f"{name}: A . 1 != 0"
    return A, den, vals


# ---- the two multiplier Grams: the exact route, unchanged from n = 5 ----------------------
for name in ("aligned", "generic"):
    A, den, vals = orbit_matrix(name, S["mult"][name]["lab"], MD1)
    amax = int(np.abs(A).max())
    lam2 = float(np.linalg.eigvalsh(A.astype(np.float64))[1])
    assert lam2 > 0, f"{name}: lambda_2 = {lam2}"
    d = max(1, int(math.ceil(lam2 / MD1)))
    log(f"{name}: den = {den}, max |A| = {amax:.3e}, lambda_2 = {lam2:.4e}, d = {d}")
    F = 1 << 6
    while True:
        F *= 2
        if F * F * (amax + d) > LIM // 4:
            raise SystemExit(f"{name}: F = {F} overflows")
        B = (F * F) * (A + d)
        delta = int(F * F * lam2 // 2)
        Bd = B.copy()
        np.fill_diagonal(Bd, np.diagonal(Bd) - delta)
        log(f"  F = 2^{int(math.log2(F))}, delta = {delta:.4e}: integer Cholesky")
        try:
            N = int_cholesky(Bd, MD1)
        except SystemExit as e:
            log(f"    {e}; doubling F")
            continue
        E = B - np.einsum("ik,jk->ij", N, N)
        diag = np.diagonal(E).copy()
        off = np.abs(E).sum(axis=1) - np.abs(diag)
        slack = int((diag - off).min())
        log(f"    diagonal dominance slack: min {slack:.4e}")
        if slack >= 0:
            break
        log("    not diagonally dominant; doubling F")
    out[name] = {"dim": MD1, "den": str(den), "d": str(d), "F": str(F), "delta": str(delta),
                 "orbit_values": [str(v) for v in vals]}
    log(f"  {name}: certified exactly")

# ---- the main Gram: the verified floating-point route -------------------------------------
A, den, vals = orbit_matrix("main", S["labD"], MD)
log(f"main: den = {den}, max |A| = {int(np.abs(A).max()):.3e}")
Af = A.astype(np.float64) / float(den)
del A
ev = np.linalg.eigvalsh(Af)
lam2 = float(ev[1])
log(f"main: lambda_1 = {float(ev[0]):.4e}, lambda_2 = {lam2:.4e}, lambda_max = {float(ev[-1]):.4e}")
del ev
assert lam2 > 0
d = lam2 / MD                       # so that lambda_min(Af + d J) = min(lam2, d * MD) = lam2
alpha = 0.5 * lam2
M = Af + d
np.fill_diagonal(M, np.diagonal(M) - alpha)
log(f"main: d = {d:.6e}, alpha = {alpha:.6e}; floating Cholesky of Af + d - alpha I")
Lc = np.linalg.cholesky(M)
del M
gam = (MD + 1) * U / (1 - (MD + 1) * U)
sumL2 = float(np.einsum("ij,ij->", Lc, Lc))
del Lc
frob = float(math.sqrt(np.einsum("ij,ij->", Af, Af)))
mx = float(np.abs(Af).max())
err = 10 * (gam * sumL2 + 3 * U * frob + (MD + 1) * U * mx)
log(f"main: sum Lc^2 = {sumL2:.4e}, ||Af||_F = {frob:.4e}, max |Af| = {mx:.4e}")
log(f"main: rigorous error bound {err:.4e} against alpha {alpha:.4e}: "
    f"{'positive definite, margin %.2fx' % (alpha / err) if alpha > err else 'INCONCLUSIVE'}")
assert alpha > err, "the verified floating-point Cholesky is inconclusive at n = 6"
out["main"] = {"dim": MD, "den": str(den), "d_hex": float(d).hex(), "alpha_hex": float(alpha).hex(),
               "expected_sumL2": sumL2, "expected_err": err, "orbit_values": [str(v) for v in vals]}

json.dump(out, open(out_path, "w"))
log(f"wrote {out_path} ({len(json.dumps(out)) / 1e6:.3f} MB)")
