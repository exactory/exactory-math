#!/usr/bin/env python3
"""The sign census of the h vectors, on top of the box attack's census.

This is `certified-special-case-check-4/census.py` of the box attack with three additions and no
other change: the smallest entry of each h vector, the count of records with a negative entry
broken down by index, and the records that have one. The original computes every h vector already
and was independently checked; it never tested an entry for negativity, which is the one question
root move 4 makes decisive. The original docstring follows.

Census of coefficient ratios and h*-vectors over every polynomial computed in the box.

Reads the polynomial records of enumeration-run-2 (scan-n5-*.jsonl, coefficient strings, with
the vertex count nverts), enumeration-run-3 (scan-n6.jsonl.gz) and enumeration-run-4
(scan-n7.jsonl.gz) (integer numerators over a common denominator), and computes for each
polynomial P of degree D, from its coefficients alone and in exact rational arithmetic:
  s_k = [t^k] binom(t + D, D), the coefficients of the unimodular D-simplex,
  the ratios a_k / s_k for k = 1..D and their minimum minr,
  the normalized volume V = D! a_D,
  the h*-vector h*_i = sum_{j=0}^{i} (-1)^j binom(D+1, j) P(i - j), i = 0..D.
Output: census.summary.json (per number of parts: the counts of polynomials, of minr < 1 and of
minr = 24/25; the histogram of (D, h*, V, minr) over the polynomials with minr < 1; the number
of polynomials with h*_1 = 0, i.e. with exactly D + 1 lattice points, per (D, V); the largest V
among those and among the polynomials with c <= D + 2; for 5 parts the vertex counts of the
polynomials with minr < 1) and census.below1.jsonl (every polynomial with minr < 1).
"""
import glob
import gzip
import json
import os
import sys
import time
from fractions import Fraction
from math import comb, factorial
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
DET = os.path.join(HERE, "..", "..", "..", "stretched-lr-polynomial-negative-coefficient",
                   "deterministic")
SOURCES = [
    (5, sorted(glob.glob(os.path.join(DET, "enumeration-run-2", "scan-n5-*.jsonl")))),
    (6, [os.path.join(DET, "enumeration-run-3", "scan-n6.jsonl.gz")]),
    (7, [os.path.join(DET, "enumeration-run-4", "scan-n7.jsonl.gz")]),
]
TARGET = Fraction(24, 25)


def simplex_coeffs(D):
    poly = [Fraction(1)]
    for j in range(1, D + 1):
        new = [Fraction(0)] * (len(poly) + 1)
        for k, b in enumerate(poly):
            new[k] += j * b
            new[k + 1] += b
        poly = new
    f = factorial(D)
    return [b / f for b in poly]


_SIMPLEX = {}


def simplex(D):
    if D not in _SIMPLEX:
        _SIMPLEX[D] = simplex_coeffs(D)
    return _SIMPLEX[D]


def evalp(coeffs, t):
    v = Fraction(0)
    for c in reversed(coeffs):
        v = v * t + c
    return v


def hstar(coeffs):
    D = len(coeffs) - 1
    values = [evalp(coeffs, t) for t in range(D + 1)]
    return tuple(sum((-1) ** j * comb(D + 1, j) * values[i - j] for j in range(i + 1)) for i in range(D + 1))


def coeffs_of(rec):
    if "coeffs" in rec:
        p = [Fraction(x) for x in rec["coeffs"]]
    else:
        p = [Fraction(x, rec["den"]) for x in rec["num"]]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def fresh():
    return {"records": 0, "below1": 0, "eq_24_25": 0, "min_minr": None, "hstar1_zero": {},
            "min_h": None, "negative_h": 0, "negative_by_index": {}, "negative_records": [],
            "max_V_hstar1_zero": Fraction(0), "max_V_c_le_D_plus_2": Fraction(0), "below1_keys": {},
            "below1_nverts": {}, "below1_records": []}


def process(lines):
    st = fresh()
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
        if any(x.denominator != 1 for x in h):
            raise ValueError(f"non-integral h* for {rec}")
        h = tuple(int(x) for x in h)
        c = rec["c"]
        st["records"] += 1
        mh = min(h)
        if st["min_h"] is None or mh < st["min_h"]:
            st["min_h"] = mh
        if mh < 0:
            st["negative_h"] += 1
            for i, x in enumerate(h):
                if x < 0:
                    st["negative_by_index"][i] = st["negative_by_index"].get(i, 0) + 1
            if len(st["negative_records"]) < 200:
                st["negative_records"].append({"lam": rec["lam"], "mu": rec["mu"], "nu": rec["nu"],
                                               "c": c, "D": D, "hstar": list(h)})
        if st["min_minr"] is None or minr < st["min_minr"]:
            st["min_minr"] = minr
        if h[1] == 0:
            key = (D, str(V))
            st["hstar1_zero"][key] = st["hstar1_zero"].get(key, 0) + 1
            if V > st["max_V_hstar1_zero"]:
                st["max_V_hstar1_zero"] = V
        if c <= D + 2 and V > st["max_V_c_le_D_plus_2"]:
            st["max_V_c_le_D_plus_2"] = V
        if minr == TARGET:
            st["eq_24_25"] += 1
        if minr < 1:
            st["below1"] += 1
            key = (D, ",".join(str(x) for x in h), str(V), str(minr))
            st["below1_keys"][key] = st["below1_keys"].get(key, 0) + 1
            if "nverts" in rec:
                nk = (D, rec["nverts"])
                st["below1_nverts"][nk] = st["below1_nverts"].get(nk, 0) + 1
            st["below1_records"].append({"lam": rec["lam"], "mu": rec["mu"], "nu": rec["nu"], "c": c, "D": D,
                                         "V": str(V), "hstar": list(h), "minr": str(minr),
                                         "nverts": rec.get("nverts")})
    return st


def merge(total, st):
    total["records"] += st["records"]
    total["negative_h"] += st["negative_h"]
    if st["min_h"] is not None and (total["min_h"] is None or st["min_h"] < total["min_h"]):
        total["min_h"] = st["min_h"]
    for k, v in st["negative_by_index"].items():
        total["negative_by_index"][k] = total["negative_by_index"].get(k, 0) + v
    total["negative_records"].extend(st["negative_records"][:200])
    total["below1"] += st["below1"]
    total["eq_24_25"] += st["eq_24_25"]
    if st["min_minr"] is not None and (total["min_minr"] is None or st["min_minr"] < total["min_minr"]):
        total["min_minr"] = st["min_minr"]
    for k, v in st["hstar1_zero"].items():
        total["hstar1_zero"][k] = total["hstar1_zero"].get(k, 0) + v
    total["max_V_hstar1_zero"] = max(total["max_V_hstar1_zero"], st["max_V_hstar1_zero"])
    total["max_V_c_le_D_plus_2"] = max(total["max_V_c_le_D_plus_2"], st["max_V_c_le_D_plus_2"])
    for k, v in st["below1_keys"].items():
        total["below1_keys"][k] = total["below1_keys"].get(k, 0) + v
    for k, v in st["below1_nverts"].items():
        total["below1_nverts"][k] = total["below1_nverts"].get(k, 0) + v
    total["below1_records"].extend(st["below1_records"])


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


def serialise(total):
    out = {k: v for k, v in total.items() if k not in ("below1_records", "negative_records")}
    out["min_h"] = str(total["min_h"])
    out["negative_by_index"] = {str(k): v for k, v in sorted(total["negative_by_index"].items())}
    out["min_minr"] = str(total["min_minr"])
    out["max_V_hstar1_zero"] = str(total["max_V_hstar1_zero"])
    out["max_V_c_le_D_plus_2"] = str(total["max_V_c_le_D_plus_2"])
    out["hstar1_zero"] = {f"D={k[0]},V={k[1]}": v for k, v in sorted(total["hstar1_zero"].items())}
    out["below1_keys"] = {f"D={k[0]};hstar={k[1]};V={k[2]};minr={k[3]}": v for k, v in sorted(total["below1_keys"].items())}
    out["below1_nverts"] = {f"D={k[0]},nverts={k[1]}": v for k, v in sorted(total["below1_nverts"].items())}
    return out


def main():
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    t0 = time.time()
    summary = {}
    with Pool(workers) as pool, open(os.path.join(HERE, "census.below1.jsonl"), "w") as below, \
            open(os.path.join(HERE, "h-negative.jsonl"), "w") as neg:
        for n, paths in SOURCES:
            total = fresh()
            for st in pool.imap_unordered(process, chunks(paths), chunksize=1):
                merge(total, st)
            for rec in total["below1_records"]:
                rec["n"] = n
                below.write(json.dumps(rec) + "\n")
            for rec in total["negative_records"]:
                rec["n"] = n
                neg.write(json.dumps(rec) + "\n")
            summary[str(n)] = serialise(total)
            print(f"{n} parts: {total['records']} polynomials, {total['below1']} with minr < 1, "
                  f"{total['negative_h']} with a negative h entry, smallest entry {total['min_h']}, "
                  f"{time.time() - t0:.0f}s", flush=True)
    summary["seconds"] = round(time.time() - t0, 1)
    json.dump(summary, open(os.path.join(HERE, "h-sign.summary.json"), "w"), indent=1)
    print("done", flush=True)


if __name__ == "__main__":
    main()
