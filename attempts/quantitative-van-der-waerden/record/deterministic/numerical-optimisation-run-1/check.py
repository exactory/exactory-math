"""The check: no matrix found anywhere on the polytope has ratio below 1/4.

`search.py` minimises `ratio(B) = (per(B)/gamma_n - 1)/||B - J_n/n||_F^2` over the Birkhoff
polytope for `n = 3` to 9, globally and on a grid of distances from the centre, and evaluates
three explicit families.  This asserts that every value it produces is at least `1/4`, to a
tolerance of `1e-9`.

It is computational evidence, not a proof: a multi-start local optimiser gives an upper bound on
the true minimum, so a pass says no counterexample was found under the schedule `search.py`
fixes, not that none exists.  The run is reproducible: the seed is 20260904 and both the Sinkhorn
iteration and Nelder-Mead are deterministic.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from search import run  # noqa: E402

NS = [3, 4, 5, 6, 7, 8, 9]
TOL = 1e-9
rows = run(NS)
bad = []
for r in rows:
    n = r["n"]
    print(f"n = {n}: c*(n) = {r['c_star']:.6f}  (local upper bound {r['local_upper']:.6f})",
          flush=True)
    print("   profile  " + "  ".join(f"t={t:.2f}:{v:.3f}" if math.isfinite(v) else f"t={t:.2f}:--"
                                     for t, v in r["profile"]))
    print("   explicit " + "  ".join(f"{k}={v:.4f}" for k, v in r["explicit"].items()))
    if r["c_star"] < 0.25 - TOL:
        bad.append(f"n = {n}: global minimum {r['c_star']:.9f} is below 1/4")
    if r["c_star"] > r["local_upper"] + TOL:
        bad.append(f"n = {n}: global minimum exceeds the local upper bound")
    for t, v in r["profile"]:
        if math.isfinite(v) and v < 0.25 - TOL:
            bad.append(f"n = {n}: profile at t = {t:.3f} is {v:.9f}, below 1/4")
    for k, v in r["explicit"].items():
        if v < 0.25 - TOL:
            bad.append(f"n = {n}: {k} has ratio {v:.9f}, below 1/4")

if bad:
    print("FAIL")
    for b in bad:
        print("  " + b)
    raise SystemExit(1)
print(f"PASS: no ratio below 1/4 at n = {', '.join(map(str, NS))}, globally, on the distance "
      f"profile, or at any explicit family")
