#!/usr/bin/env python3
"""Test the recorded h*-vectors of hive polytopes against the inequalities that the
h*-vector of a lattice polytope must satisfy.

Input: a JSON file listing the certified polynomial records (JSONL, optionally gzip) with
their expected SHA-256 digests. Every file is hashed before use and a mismatch aborts.

For each record with a computed polynomial P of degree D (the Ehrhart polynomial of the
hive polytope H(lam, mu, nu), P(0) = 1), compute in exact arithmetic
  h*_i = sum_{j=0}^{i} (-1)^j C(D+1, j) P(i-j),   i = 0..D,
so that sum_t P(t) z^t = (sum_i h*_i z^i) / (1 - z)^{D+1}, and test:
  N  nonnegativity        h*_i >= 0 for all i                      (Stanley 1980, lattice case)
  I  interior bound       h*_D <= h*_1                               (interior points <= h*_1)
  H  Hibi lower bound     if h*_D > 0 then h*_1 <= h*_i, 1 <= i <= D-1 (Hibi 1994)
  S  Stanley inequality   h*_0+...+h*_i <= h*_s+...+h*_{s-i}, s = deg h*, 0 <= i <= s/2
                                                                      (Stanley 1991)
  K  Hibi 1990            h*_0+...+h*_{i+1} >= h*_D+...+h*_{D-i}, 0 <= i <= D/2 - 1
Each of N, I, H, S, K is a theorem for lattice polytopes, so a hive polytope violating one
is not Ehrhart-equivalent to any lattice polytope of dimension D. The tests are run on every
record, and the counts are broken down by the largest vertex denominator when the record
carries it (maxden 1 means the hive polytope is itself a lattice polytope and the tests are
vacuous for the question).

Output: summary JSON on stdout and, in the output directory, `violations.jsonl` (every
violating record, with the failing tests) and `hstar-table.jsonl` (the distinct
(parts, D, maxden, h*) keys with multiplicities and one witness triple each).
"""
import gzip
import hashlib
import json
import os
import sys
import time
from fractions import Fraction
from math import comb
from multiprocessing import Pool


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def coeffs_of(rec):
    if "coeffs" in rec:
        p = [Fraction(x) for x in rec["coeffs"]]
    else:
        p = [Fraction(x, rec["den"]) for x in rec["num"]]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def evalp(coeffs, t):
    v = Fraction(0)
    for c in reversed(coeffs):
        v = v * t + c
    return v


def hstar(coeffs):
    D = len(coeffs) - 1
    values = [evalp(coeffs, t) for t in range(D + 1)]
    h = tuple(sum((-1) ** j * comb(D + 1, j) * values[i - j] for j in range(i + 1)) for i in range(D + 1))
    if any(x.denominator != 1 for x in h):
        raise ValueError("non-integral h*")
    return tuple(int(x) for x in h)


def tests(h):
    D = len(h) - 1
    failed = []
    if min(h) < 0:
        failed.append("N")
    if h[D] > h[1]:
        failed.append("I")
    if h[D] > 0 and any(h[1] > h[i] for i in range(1, D)):
        failed.append("H")
    s = max(i for i in range(D + 1) if h[i] != 0)
    for i in range(s // 2 + 1):
        if sum(h[: i + 1]) > sum(h[s - i: s + 1]):
            failed.append("S")
            break
    for i in range(D // 2):
        if sum(h[: i + 2]) < sum(h[D - i: D + 1]):
            failed.append("K")
            break
    return failed


def process(job):
    parts, lines = job
    counts = {}
    table = {}
    violations = []
    for line in lines:
        rec = json.loads(line)
        if "coeffs" not in rec and "num" not in rec:
            continue
        p = coeffs_of(rec)
        D = len(p) - 1
        h = hstar(p)
        maxden = rec.get("maxden")
        key = (parts, D, maxden, h)
        if key in table:
            table[key][0] += 1
        else:
            table[key] = [1, [rec["lam"], rec["mu"], rec["nu"]], rec["c"]]
        failed = tests(h)
        ck = (D, maxden)
        c = counts.setdefault(ck, {"records": 0, "N": 0, "I": 0, "H": 0, "S": 0, "K": 0, "any": 0})
        c["records"] += 1
        if failed:
            c["any"] += 1
            for f in failed:
                c[f] += 1
            if len(violations) < 2000:
                violations.append({"parts": parts, "lam": rec["lam"], "mu": rec["mu"], "nu": rec["nu"],
                                   "c": rec["c"], "D": D, "maxden": maxden, "hstar": list(h),
                                   "coeffs": [str(x) for x in p], "failed": failed})
    return counts, table, violations


def chunks(parts, path, size=20000):
    opener = gzip.open if path.endswith(".gz") else open
    buf = []
    with opener(path, "rt") as f:
        for line in f:
            buf.append(line)
            if len(buf) >= size:
                yield parts, buf
                buf = []
    if buf:
        yield parts, buf


def main():
    spec = json.load(open(sys.argv[1]))
    outdir = sys.argv[2] if len(sys.argv) > 2 else "."
    os.makedirs(outdir, exist_ok=True)
    t0 = time.time()
    files = []
    for entry in spec["files"]:
        digest = sha256_of(entry["path"])
        if digest != entry["sha256"]:
            raise SystemExit(f"digest mismatch for {entry['path']}: {digest}")
        files.append((entry["parts"], entry["path"]))
    hashed = time.time() - t0
    counts = {}
    table = {}
    violations = []

    def jobs():
        for parts, path in files:
            yield from chunks(parts, path)

    with Pool(spec.get("workers", 6)) as pool:
        for c, t, v in pool.imap_unordered(process, jobs(), chunksize=1):
            for k, d in c.items():
                acc = counts.setdefault(k, {"records": 0, "N": 0, "I": 0, "H": 0, "S": 0, "K": 0, "any": 0})
                for f, n in d.items():
                    acc[f] += n
            for k, (n, wit, cval) in t.items():
                if k in table:
                    table[k][0] += n
                else:
                    table[k] = [n, wit, cval]
            violations.extend(v)
    with open(os.path.join(outdir, "violations.jsonl"), "w") as f:
        for v in violations:
            f.write(json.dumps(v) + "\n")
    with open(os.path.join(outdir, "hstar-table.jsonl"), "w") as f:
        for (parts, D, maxden, h), (n, wit, cval) in sorted(table.items(), key=lambda kv: (kv[0][0], kv[0][1], str(kv[0][2]), kv[0][3])):
            f.write(json.dumps({"parts": parts, "D": D, "maxden": maxden, "hstar": list(h), "count": n,
                                "witness": wit, "witness_c": cval}) + "\n")
    summary = {
        "files": [{"parts": p, "path": path} for p, path in files],
        "hash_seconds": round(hashed, 1),
        "seconds": round(time.time() - t0, 1),
        "records": sum(c["records"] for c in counts.values()),
        "violations": len(violations),
        "distinct_keys": len(table),
        "by_dimension_and_maxden": {f"D={k[0]},maxden={k[1]}": v for k, v in sorted(counts.items(), key=lambda kv: (kv[0][0], str(kv[0][1])))},
    }
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
