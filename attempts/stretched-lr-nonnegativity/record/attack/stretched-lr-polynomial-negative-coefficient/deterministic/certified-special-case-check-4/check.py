#!/usr/bin/env python3
"""Second implementation of the census (certified-special-case-check-4).

Recomputes, from the same records, the ratios, volumes and h*-vectors by different formulas:
the simplex coefficients as unsigned Stirling numbers of the first kind, s_k = c(D+1, k+1)/D!,
and the h*-vector as the coefficients of (1 - z)^{D+1} sum_t P(t) z^t obtained by D + 1
successive multiplications by (1 - z). It rebuilds every aggregate of census.summary.json and
the histogram of census.below1.jsonl and compares. Exit 0 iff everything agrees.
"""
import glob
import gzip
import json
import os
import sys
from fractions import Fraction
from math import factorial
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
DET = os.path.join(HERE, "..")
SOURCES = [
    (5, sorted(glob.glob(os.path.join(DET, "enumeration-run-2", "scan-n5-*.jsonl")))),
    (6, [os.path.join(DET, "enumeration-run-3", "scan-n6.jsonl.gz")]),
    (7, [os.path.join(DET, "enumeration-run-4", "scan-n7.jsonl.gz")]),
]


def stirling_row(n):
    """Unsigned Stirling numbers of the first kind c(n, k), k = 0..n."""
    row = [1]
    for m in range(n):
        new = [0] * (len(row) + 1)
        for k, v in enumerate(row):
            new[k] += m * v
            new[k + 1] += v
        row = new
    return row


_S = {}


def simplex(D):
    if D not in _S:
        c = stirling_row(D + 1)
        f = factorial(D)
        _S[D] = [Fraction(c[k + 1], f) for k in range(D + 1)]
    return _S[D]


def value(p, t):
    return sum(a * Fraction(t) ** i for i, a in enumerate(p))


def hstar(p):
    D = len(p) - 1
    series = [value(p, t) for t in range(D + 1)]
    for _ in range(D + 1):
        series = [series[i] - (series[i - 1] if i else 0) for i in range(D + 1)]
    return tuple(series)


def coeffs_of(rec):
    if "coeffs" in rec:
        p = [Fraction(x) for x in rec["coeffs"]]
    else:
        p = [Fraction(x, rec["den"]) for x in rec["num"]]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def process(lines):
    st = {"records": 0, "below1": 0, "eq_24_25": 0, "min_minr": None, "hstar1_zero": {},
          "max_V_hstar1_zero": Fraction(0), "max_V_c_le_D_plus_2": Fraction(0), "below1_keys": {}, "below1_nverts": {}}
    for line in lines:
        rec = json.loads(line)
        if "coeffs" not in rec and "num" not in rec:
            continue
        p = coeffs_of(rec)
        D = len(p) - 1
        s = simplex(D)
        minr = min(p[k] / s[k] for k in range(1, D + 1))
        V = p[D] * factorial(D)
        h = hstar(p)
        st["records"] += 1
        if st["min_minr"] is None or minr < st["min_minr"]:
            st["min_minr"] = minr
        if h[1] == 0:
            key = f"D={D},V={V}"
            st["hstar1_zero"][key] = st["hstar1_zero"].get(key, 0) + 1
            st["max_V_hstar1_zero"] = max(st["max_V_hstar1_zero"], V)
        if rec["c"] <= D + 2:
            st["max_V_c_le_D_plus_2"] = max(st["max_V_c_le_D_plus_2"], V)
        if minr == Fraction(24, 25):
            st["eq_24_25"] += 1
        if minr < 1:
            st["below1"] += 1
            key = f"D={D};hstar={','.join(str(x) for x in h)};V={V};minr={minr}"
            st["below1_keys"][key] = st["below1_keys"].get(key, 0) + 1
            if "nverts" in rec:
                nk = f"D={D},nverts={rec['nverts']}"
                st["below1_nverts"][nk] = st["below1_nverts"].get(nk, 0) + 1
    return st


def chunks(paths, size=20000):
    for path in paths:
        opener = gzip.open if path.endswith(".gz") else open
        buf = []
        with opener(path, "rt") as f:
            for line in f:
                buf.append(line)
                if len(buf) >= size:
                    yield buf
                    buf = []
        if buf:
            yield buf


def main():
    summary = json.load(open(os.path.join(HERE, "census.summary.json")))
    below = [json.loads(l) for l in open(os.path.join(HERE, "census.below1.jsonl"))]
    bad = 0
    with Pool(6) as pool:
        for n, paths in SOURCES:
            tot = {"records": 0, "below1": 0, "eq_24_25": 0, "min_minr": None, "hstar1_zero": {},
                   "max_V_hstar1_zero": Fraction(0), "max_V_c_le_D_plus_2": Fraction(0), "below1_keys": {}, "below1_nverts": {}}
            for st in pool.imap_unordered(process, chunks(paths), chunksize=1):
                for k in ("records", "below1", "eq_24_25"):
                    tot[k] += st[k]
                if st["min_minr"] is not None and (tot["min_minr"] is None or st["min_minr"] < tot["min_minr"]):
                    tot["min_minr"] = st["min_minr"]
                for k in ("hstar1_zero", "below1_keys", "below1_nverts"):
                    for kk, v in st[k].items():
                        tot[k][kk] = tot[k].get(kk, 0) + v
                tot["max_V_hstar1_zero"] = max(tot["max_V_hstar1_zero"], st["max_V_hstar1_zero"])
                tot["max_V_c_le_D_plus_2"] = max(tot["max_V_c_le_D_plus_2"], st["max_V_c_le_D_plus_2"])
            mine = {"records": tot["records"], "below1": tot["below1"], "eq_24_25": tot["eq_24_25"],
                    "min_minr": str(tot["min_minr"]), "max_V_hstar1_zero": str(tot["max_V_hstar1_zero"]),
                    "max_V_c_le_D_plus_2": str(tot["max_V_c_le_D_plus_2"]), "hstar1_zero": tot["hstar1_zero"],
                    "below1_keys": tot["below1_keys"], "below1_nverts": tot["below1_nverts"]}
            theirs = {k: summary[str(n)][k] for k in mine}
            if mine != theirs:
                bad += 1
                print(f"CENSUS MISMATCH at {n} parts:\n mine {json.dumps(mine)}\n census {json.dumps(theirs)}")
            else:
                print(f"{n} parts: {mine['records']} polynomials, {mine['below1']} with ratio < 1 "
                      f"({json.dumps(mine['below1_keys'])}), {mine['eq_24_25']} at 24/25, min ratio {mine['min_minr']}, "
                      f"largest V with D + 1 lattice points {mine['max_V_hstar1_zero']}, with c <= D + 2 {mine['max_V_c_le_D_plus_2']}; "
                      f"vertex counts of the ratio < 1 records {json.dumps(mine['below1_nverts'])}")
            listed = {}
            for r in below:
                if r["n"] == n:
                    key = f"D={r['D']};hstar={','.join(str(x) for x in r['hstar'])};V={r['V']};minr={r['minr']}"
                    listed[key] = listed.get(key, 0) + 1
            if listed != tot["below1_keys"]:
                bad += 1
                print(f"BELOW-1 LIST MISMATCH at {n} parts: listed {listed}, recomputed {tot['below1_keys']}")
    print(f"below-1 list: {len(below)} records, agrees with the recomputation: {bad == 0}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
