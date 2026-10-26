#!/usr/bin/env python3.11
"""Feasibility scan of Leung-Schmidt (2016) Theorem 6.1 over the 8,125 survivors of Theorem 6.3.

Theorem 6.1 (general form: u/m need not be a prime power) bounds ord_p(t) by
    (u/m)^4 * max({2 m^2 / u^2} union {(s-1)/(f_s (s - f_s)) : s in S \ S'}),
and the maximum is at least 2 m^2 / u^2, so a violation needs
    ord_p(t) > 2 (u/m)^2,   hence   p - 1 > 2 (u/m)^2                                    (*)
for the chosen (d, p) and the largest admissible m, which is p^a times every prime of u satisfying
(101); u/m is then the product of the prime powers of the primes failing (101). For each survivor
this scan enumerates every prime p of u and every unitary divisor d coprime to p with
phi(d^2) < p phi(u^2) / (2u^2), computes the set B(p, d) of primes r != p, r | u, with
    nu_p(ord_{p^{2a}}(r)) <= nu_p(ord'_{u/d}(r))
(the primes that must go into u/m), and records whether (*) holds for u/m = prod_{r in B} r^nu_r(u).
It also records min |B(p, d)| and whether any B(p, d) is empty (in which case Theorem 3.5 of the paper
with m = u already forbids a circulant Hadamard matrix of order 4u^2, since it would produce a root of
unity X with X eta outside Z[zeta_{v/p}] for every root of unity eta).

Output: scan_thm61.jsonl, one line per survivor with u, min_bad, the best (p, d, B) under (*), or null.
"""
import json
import re
import sys
from fractions import Fraction
from math import prod

from sympy.ntheory import n_order

ORD = {}


def ord_mod(q, p):
    key = (q, p)
    if key not in ORD:
        ORD[key] = n_order(q % p, p)
    return ORD[key]


def nu(p, x):
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def nu_p_ord_ppow(r, p, k):
    x = pow(r, ord_mod(r, p), p ** k)
    c = 0
    while c < k and x % (p ** (c + 1)) == 1:
        c += 1
    return k - c


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
                assert prod(p ** e for p, e in fac.items()) == u
                values.append((u, fac))
    return values


def scan(u, fac):
    P = sorted(fac)
    ratio = Fraction(prod(r - 1 for r in P), prod(P))
    min_bad = None
    best = None
    best_multi = None  # the same, restricted to |B| >= 2 (the cases Theorem 6.3 cannot take)
    empty = []
    for p in P:
        a = fac[p]
        others = [r for r in P if r != p]
        bound = Fraction(p) * ratio / 2
        lhs = {r: nu_p_ord_ppow(r, p, 2 * a) for r in others}
        stack = [(0, [], Fraction(1))]
        while stack:
            i, chosen, phi = stack.pop()
            D = set(chosen)
            not_in_d = [s for s in others if s not in D]
            bad = []
            for r in others:
                m = nu_p_ord_ppow(r, p, a)
                for s in not_in_d:
                    if s != r:
                        m = max(m, nu(p, ord_mod(r, s)))
                if not lhs[r] > m:
                    bad.append(r)
            if min_bad is None or len(bad) < min_bad:
                min_bad = len(bad)
            if not bad:
                empty.append({"p": p, "d": prod(r ** fac[r] for r in chosen)})
            um = prod(r ** fac[r] for r in bad)
            if p - 1 > 2 * um * um and (best is None or um < best["u_over_m"]):
                best = {"p": p, "d": prod(r ** fac[r] for r in chosen), "bad": bad, "u_over_m": um}
            if len(bad) >= 2 and p - 1 > 2 * um * um and (best_multi is None or um < best_multi["u_over_m"]):
                best_multi = {"p": p, "d": prod(r ** fac[r] for r in chosen), "bad": bad, "u_over_m": um}
            for j in range(i, len(others)):
                r = others[j]
                phi2 = phi * r ** (2 * fac[r] - 1) * (r - 1)
                if phi2 < bound:
                    stack.append((j + 1, chosen + [r], phi2))
    return {"u": u, "min_bad": min_bad, "empty_bad": empty, "feasible": best, "feasible_multi": best_multi}


def main():
    list_file = sys.argv[1] if len(sys.argv) > 1 else "survivors_thm63.txt"
    out_file = sys.argv[2] if len(sys.argv) > 2 else "scan_thm61.jsonl"
    values = read_list(list_file)
    n_feasible = n_empty = n_multi = 0
    min_bad_hist = {}
    with open(out_file, "w") as out:
        for u, fac in values:
            rec = scan(u, fac)
            out.write(json.dumps(rec) + "\n")
            n_feasible += rec["feasible"] is not None
            n_multi += rec["feasible_multi"] is not None
            n_empty += bool(rec["empty_bad"])
            min_bad_hist[rec["min_bad"]] = min_bad_hist.get(rec["min_bad"], 0) + 1
    print(f"survivors: {len(values)}  with some empty B(p,d): {n_empty}  satisfying (*) for some (p,d): {n_feasible}  satisfying (*) with |B| >= 2: {n_multi}  min|B| histogram: {sorted(min_bad_hist.items())}")


if __name__ == "__main__":
    main()
