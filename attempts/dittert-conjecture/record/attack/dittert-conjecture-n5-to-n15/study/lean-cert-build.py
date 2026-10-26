"""Build and pre-verify, in Python, exactly the check that Lean will run on the certificate.

For each Gram matrix M = A / den (A integer, symmetric, A . 1 = 0) the check is:

    B  := F^2 * (A + d*J)                      (J = all ones)
    N  := integer Cholesky of B - delta*I      (any rounding; accuracy is irrelevant)
    E  := B - N N^T
    E is diagonally dominant with nonnegative diagonal.

Then E >= 0 by Gershgorin and N N^T >= 0, so B >= 0, so A + d*J >= 0; and with A . 1 = 0,
for any y the vector z = y - mean(y)*1 has J z = 0 and y^T A y = z^T A z = z^T (A + d J) z >= 0.
So A >= 0 and M >= 0.

`d` is chosen so that d * dim >= lambda_2(A): that puts lambda_min(A + d J) at lambda_2(A)
instead of the lambda_2(A)/dim that deleting a row and column would give, which is what
keeps every number below 2^63 and lets Lean use machine integers.

Usage: python lean-cert-build.py <certificate.json> <out.json>
"""
import json
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np

T0 = time.time()
LIM = 2 ** 62


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def isqrt_arr(x):
    return math.isqrt(int(x))


def int_cholesky(Bd, dim):
    """Lower-triangular integer N with N N^T close to Bd (Bd symmetric positive definite)."""
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
out_path = sys.argv[2] if len(sys.argv) > 2 else "lean-cert.json"
n = int(cert.get("n", 5))
lam = Fr(cert["lambda"])
sys.path.insert(0, "../deterministic/numerical-optimisation-run-3")
from sdp_n import build  # noqa: E402

S = build(n)
MD, MD1 = len(S["VD"].mons), len(S["VD1"].mons)
log(f"n = {n}, lambda = {lam}, main Gram {MD}, multiplier Grams {MD1}")

pieces = {"main": (S["labD"], MD), "aligned": (S["mult"]["aligned"]["lab"], MD1),
          "generic": (S["mult"]["generic"]["lab"], MD1)}
out = {"n": n, "lambda_num": str(lam.numerator), "lambda_den": str(lam.denominator)}
for name, (lab, dim) in pieces.items():
    coords = [Fr(x) for x in cert[name]]
    den = 1
    for c in coords:
        den = den * c.denominator // math.gcd(den, c.denominator)
    vals = [int(c * den) for c in coords]
    u = np.unique(lab)
    assert len(u) == len(coords), f"{name}: {len(coords)} values for {len(u)} orbits"
    A = np.array(vals, dtype=object)[np.searchsorted(u, lab)].reshape(dim, dim)
    assert (A == A.T).all() and all(int(x) == 0 for x in A.sum(axis=1)), f"{name}: not symmetric or A.1 != 0"
    amax = int(np.abs(A).max())
    Ai = A.astype(np.int64)
    assert (Ai.astype(object) == A).all(), "A does not fit in int64"
    lam2 = float(np.linalg.eigvalsh(Ai.astype(np.float64))[1])
    assert lam2 > 0
    d = max(1, int(math.ceil(lam2 / dim)))
    log(f"{name}: den = {den} ({len(str(den))} digits), max |A| = {amax:.3e}, lambda_2 = {lam2:.4e}, d = {d}")

    F = 1 << 6
    while True:
        F *= 2
        Bmax = F * F * (amax + d)
        if Bmax > LIM // 4:
            raise SystemExit(f"{name}: F = {F} overflows (B up to {Bmax:.3e})")
        B = (F * F) * (Ai + d)
        delta = int(F * F * lam2 // 2)
        Bd = B.copy()
        np.fill_diagonal(Bd, np.diagonal(Bd) - delta)
        log(f"  F = 2^{int(math.log2(F))}, delta = {delta:.4e}, max B = {int(np.abs(B).max()):.3e}: integer Cholesky")
        try:
            N = int_cholesky(Bd, dim)
        except SystemExit as e:
            log(f"    {e}; doubling F")
            continue
        log(f"    max |N| = {int(np.abs(N).max()):.3e}; computing N N^T")
        NN = N @ N.T
        E = B - NN
        diag = np.diagonal(E).copy()
        absE = np.abs(E)
        off = absE.sum(axis=1) - np.abs(diag)
        slack = int((diag - off).min())
        log(f"    diagonal dominance slack: min {slack:.4e}, max |E| = {int(absE.max()):.3e}")
        if slack >= 0:
            break
        log("    not diagonally dominant; doubling F")
    out[name] = {"dim": dim, "den": str(den), "d": str(d), "F": str(F), "delta": str(delta),
                 "orbit_values": [str(v) for v in vals]}
    log(f"  {name}: certified (data: {len(vals)} orbit values, 4 integers)")

json.dump(out, open(out_path, "w"))
log(f"wrote {out_path} ({len(json.dumps(out)) / 1e6:.3f} MB)")
