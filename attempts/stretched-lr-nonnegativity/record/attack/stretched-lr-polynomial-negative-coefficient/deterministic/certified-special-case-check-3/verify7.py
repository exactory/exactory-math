#!/usr/bin/env python3
"""Second encoding for the 7-part box: every primitive polynomial recomputed from the tableau polytope.

Pinning a 7-part polynomial by lattice-word counts needs values up to t = 15 (deg P <= 15),
which is out of reach for the fat hives (hundreds of millions of tableaux already at t = 10).
This step instead recomputes every one of the 1,302,871 polynomial records of
enumeration-run-4 from a second polytope encoding, the tableau polytope of
tableau_polytope.py (the lattice-word conditions on the multiplicity matrix, no hive
inequality), with Normaliz, and checks lrcalc's c at t = 1 for every record and the value
at t = 2 when it is at most 1,000,000.  Agreement certifies the hive encoder and the
recorded polynomials against an independent encoding, with Normaliz as the shared solver.
Output: verify7.summary.json, verify7.mismatches.jsonl.
"""
import gzip
import json
import os
import sys
import time
from fractions import Fraction
from multiprocessing import Pool

import lrcalc  # type: ignore

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tableau_polytope import ehrhart_tableau  # noqa: E402

RUN4 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "enumeration-run-4", "scan-n7.jsonl.gz")
T2_LIMIT = 1_000_000


def recorded(rec):
    p = [Fraction(x, rec["den"]) for x in rec["num"]]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def evalp(p, t):
    return sum(c * Fraction(t) ** i for i, c in enumerate(p))


def check(rec):
    lam, mu, nu = rec["lam"], rec["mu"], rec["nu"]
    p = recorded(rec)
    t0 = time.time()
    ok_tab = ehrhart_tableau(lam, mu, nu)[1] == p
    c1 = int(lrcalc.lrcoef(lam, mu, nu))
    ok_lr = c1 == rec["c"] == evalp(p, 1)
    t2 = False
    if evalp(p, 2) <= T2_LIMIT:
        t2 = True
        ok_lr = ok_lr and int(lrcalc.lrcoef([2 * x for x in lam], [2 * x for x in mu], [2 * x for x in nu])) == evalp(p, 2)
    return ok_tab, ok_lr, t2, time.time() - t0, rec if not (ok_tab and ok_lr) else None


def records():
    recs = []
    with gzip.open(RUN4, "rt") as f:
        for line in f:
            r = json.loads(line)
            if "num" in r:
                recs.append(r)
    recs.sort(key=lambda r: -r["dim"])
    return recs


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    t0 = time.time()
    recs = records()
    print(f"{len(recs)} records", flush=True)
    n = tab = lr = t2n = 0
    slowest = 0.0
    with Pool(workers) as pool, open("verify7.mismatches.jsonl", "w") as mm:
        for ok_tab, ok_lr, t2, dt, bad in pool.imap_unordered(check, recs, chunksize=16):
            n += 1
            tab += ok_tab
            lr += ok_lr
            t2n += t2
            slowest = max(slowest, dt)
            if bad is not None:
                mm.write(json.dumps(bad) + "\n")
                mm.flush()
                print("MISMATCH", json.dumps(bad), flush=True)
            if n % 20000 == 0:
                print(f"{n} checked, tableau agree {tab}, lrcalc agree {lr}, {time.time()-t0:.0f}s, slowest {slowest:.1f}s", flush=True)
    summary = {"records": n, "tableau_agree": tab, "lrcalc_agree": lr, "t2_checked": t2n,
               "mismatches": n - min(tab, lr), "slowest_seconds": round(slowest, 1),
               "seconds": round(time.time() - t0, 1), "second_encoding": "tableau polytope (Normaliz)"}
    json.dump(summary, open("verify7.summary.json", "w"), indent=1)
    print("done", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
