#!/usr/bin/env python3
"""Independent recomputation of the Theorem 6.1 feasibility scan (scan_thm61.py).

Own arithmetic (deterministic Miller-Rabin, trial-division factorisation, own order routine, all
memoised), no code shared with the scan. For every survivor it recomputes min |B(p, d)|, whether some
B(p, d) is empty, and whether some (p, d) satisfies p - 1 > 2 (u/m)^2, and compares with the scan's
record. Exit 0 when every record agrees and the totals match the scan's summary line.
"""
import json
import re
import sys
from fractions import Fraction
from functools import lru_cache
from math import prod

LIST = sys.argv[1] if len(sys.argv) > 1 else "survivors_thm63.txt"
SCAN = sys.argv[2] if len(sys.argv) > 2 else "scan_thm61.jsonl"


def is_prime(n):
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for s in small:
        if n % s == 0:
            return n == s
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in small:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


@lru_cache(maxsize=None)
def factor_trial(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return tuple(sorted(f.items()))


@lru_cache(maxsize=None)
def order_prime_power(x, s, e):
    mod = s ** e
    fac = dict(factor_trial(s - 1))
    if e > 1:
        fac[s] = fac.get(s, 0) + (e - 1)
    o = (s - 1) * s ** (e - 1)
    for ell in fac:
        while o % ell == 0 and pow(x, o // ell, mod) == 1:
            o //= ell
    return o


def val(p, x):
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def read_list(path):
    values = []
    with open(path) as fh:
        for line in fh:
            m = re.match(r"^\s*(\d+)\s+\[([\d,\s]+)\]\s*$", line)
            if m:
                u = int(m.group(1))
                fac = {}
                for p in (int(x) for x in m.group(2).split(",")):
                    fac[p] = fac.get(p, 0) + 1
                values.append((u, fac))
    return values


def recompute(u, fac):
    P = sorted(fac)
    assert all(is_prime(p) for p in P) and prod(p ** e for p, e in fac.items()) == u
    phi_u2 = prod((p - 1) * p ** (2 * e - 1) for p, e in fac.items())
    min_bad = None
    any_empty = False
    feasible = False
    feasible_multi = False
    for p in P:
        a = fac[p]
        others = [r for r in P if r != p]
        # unitary divisors d coprime to p with 2 u^2 phi(d^2) < p phi(u^2)
        subsets = [()]
        for r in others:
            subsets = subsets + [s + (r,) for s in subsets]
        for D in subsets:
            phi_d2 = prod((r - 1) * r ** (2 * fac[r] - 1) for r in D) if D else 1
            if not 2 * u * u * phi_d2 < p * phi_u2:
                continue
            ud = {s: e for s, e in fac.items() if s not in D}
            bad = []
            for r in others:
                lhs = val(p, order_prime_power(r, p, 2 * a))
                rhs = 0
                for s, e in ud.items():
                    if s != r:
                        rhs = max(rhs, val(p, order_prime_power(r, s, e)))
                if not lhs > rhs:
                    bad.append(r)
            if min_bad is None or len(bad) < min_bad:
                min_bad = len(bad)
            if not bad:
                any_empty = True
            um = prod(r ** fac[r] for r in bad)
            if p - 1 > 2 * um * um:
                feasible = True
                if len(bad) >= 2:
                    feasible_multi = True
    return min_bad, any_empty, feasible, feasible_multi


def main():
    values = dict(read_list(LIST))
    recs = {}
    with open(SCAN) as fh:
        for line in fh:
            if line.strip():
                r = json.loads(line)
                recs[r["u"]] = r
    if set(recs) != set(values):
        print("scan records do not match the list")
        sys.exit(1)
    bad = 0
    n_feasible = n_empty = n_multi = 0
    for u, fac in values.items():
        min_bad, any_empty, feasible, feasible_multi = recompute(u, fac)
        r = recs[u]
        n_feasible += feasible
        n_multi += feasible_multi
        n_empty += any_empty
        scan_tuple = (r["min_bad"], bool(r["empty_bad"]), r["feasible"] is not None, r["feasible_multi"] is not None)
        if (min_bad, any_empty, feasible, feasible_multi) != scan_tuple:
            print(f"DISAGREEMENT for u = {u}: checker {(min_bad, any_empty, feasible, feasible_multi)} vs scan {scan_tuple}")
            bad += 1
    print(f"records: {len(values)}, disagreements: {bad}, with an empty B(p,d): {n_empty}, satisfying (*): {n_feasible}, satisfying (*) with |B| >= 2: {n_multi}")
    print("PASS" if bad == 0 else "FAIL")
    sys.exit(0 if bad == 0 else 1)


if __name__ == "__main__":
    main()
