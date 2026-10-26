#!/usr/bin/env python3.11
"""Search for Leung-Schmidt (2016) Theorem 6.3 certificates over the Borwein-Mossinghoff list.

Input : BarkerCandidates100.txt (237,807 values u with their prime factorisations).
Output: certificates_thm63.jsonl (one JSON object per eliminated u) and survivors_thm63.txt.

Theorem 6.3 (Leung-Schmidt, J. Combin. Theory Ser. A 139 (2016) 87-131). Let u > 1 be odd and
suppose a circulant Hadamard matrix of order 4u^2 exists. Let d | u with gcd(d, u/d) = 1, let p be
a prime divisor of u/d with phi(d^2) < p phi(u^2) / (2u^2), let p^a be the largest power of p
dividing u/d, and let q != p be a prime dividing u such that
    nu_p(ord_{p^{2a}}(r)) > nu_p(ord'_{u/d}(r))                                           (108)
for every prime r | u with r != p, r != q. Let q^b be the largest power of q dividing u, let S be
the prime divisors of u/d other than p, let S' = {s in S : nu_2(ord_s(q)) = nu_2(ord_p(q))} when
nu_2(ord_p(q)) >= 1 and S' = {} otherwise, and for s in S \ S' let
    f_s = min(ord_{ps}(q) / ord_p(q), (s-1)/2).
Then
    ord_p(q) <= q^{4b} * max({2/q^2} union {(s-1) / (f_s (s - f_s)) : s in S \ (S' union {q})}).   (109)
A value u is eliminated when some (d, p, q) violates (109).

ord'_{x}(r) is the order of r modulo the r-free part of x (Notation 2.15 of the paper). The
multiplicative orders come from sympy (n_order); the independent checker recomputes everything
with its own arithmetic.
"""
import json
import re
import sys
from fractions import Fraction
from itertools import combinations
from math import gcd, prod

from sympy.ntheory import n_order

LIST_FILE = "BarkerCandidates100.txt"
CERT_FILE = "certificates_thm63.jsonl"
SURVIVOR_FILE = "survivors_thm63.txt"


def read_list(path):
    values = []
    with open(path) as fh:
        for line in fh:
            m = re.match(r"^(\d+)\s+\[([\d,\s]+)\]\s*$", line)
            if m:
                u = int(m.group(1))
                primes = [int(x) for x in m.group(2).split(",")]
                fac = {}
                for p in primes:
                    fac[p] = fac.get(p, 0) + 1
                assert prod(p ** e for p, e in fac.items()) == u
                values.append((u, fac))
    return values


ORD = {}


def ord_mod(q, p):
    """Multiplicative order of q modulo the prime p (q != p)."""
    key = (q, p)
    if key not in ORD:
        ORD[key] = n_order(q % p, p)
    return ORD[key]


def nu(p, x):
    """The p-adic valuation of the positive integer x."""
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def nu_p_ord_ppow(r, p, k):
    """nu_p(ord_{p^k}(r)) for a prime r != p and k >= 1.

    ord_{p^k}(r) = ord_p(r) * p^{max(0, k - c)} with c = nu_p(r^{ord_p(r)} - 1), and nu_p(ord_p(r)) = 0.
    """
    x = pow(r, ord_mod(r, p), p ** k)
    c = 0
    while c < k and x % (p ** (c + 1)) == 1:
        c += 1
    return k - c


def lcm(a, b):
    return a * b // gcd(a, b)


def unitary_divisor_supports(others, fac, bound):
    """Subsets D of `others` with phi(d^2) < bound, d = prod_{r in D} r^{fac[r]}.

    phi(d^2) grows when a prime is added, so the search is pruned by size.
    """
    result = []

    def rec(start, chosen, phi):
        result.append((tuple(chosen), phi))
        for i in range(start, len(others)):
            r = others[i]
            phi2 = phi * r ** (2 * fac[r] - 1) * (r - 1)
            if phi2 < bound:
                rec(i + 1, chosen + [r], phi2)

    rec(0, [], Fraction(1))
    return result


def thm63(u, fac):
    primes = sorted(fac)
    phi_ratio = Fraction(prod(r - 1 for r in primes), prod(primes))  # phi(u^2) / u^2
    for p in primes:
        a = fac[p]
        others = [r for r in primes if r != p]
        bound = Fraction(p) * phi_ratio / 2  # (107): phi(d^2) < p phi(u^2) / (2u^2)
        lhs108 = {r: nu_p_ord_ppow(r, p, 2 * a) for r in others}
        for D, phi_d2 in unitary_divisor_supports(others, fac, bound):
            Dset = set(D)
            not_in_d = [s for s in others if s not in Dset]  # primes of u/d other than p
            # nu_p(ord'_{u/d}(r)) for every r != p: the maximum over the prime powers of u/d
            # other than r itself; p^a contributes nu_p(ord_{p^a}(r)), s^e (s != p) contributes nu_p(ord_s(r)).
            rhs108 = {}
            for r in others:
                m = nu_p_ord_ppow(r, p, a)
                for s in not_in_d:
                    if s != r:
                        m = max(m, nu(p, ord_mod(r, s)))
                rhs108[r] = m
            failing = [r for r in others if not lhs108[r] > rhs108[r]]
            if len(failing) > 1:
                continue
            candidates_q = failing if failing else others
            for q in candidates_q:
                b = fac[q]
                S = not_in_d
                o = ord_mod(q, p)
                e0 = nu(2, o)
                terms = [Fraction(2, q * q)]
                for s in S:
                    if s == q:
                        continue
                    if e0 >= 1 and nu(2, ord_mod(q, s)) == e0:
                        continue  # s in S'
                    ops = lcm(o, ord_mod(q, s))  # ord_{ps}(q)
                    fs = min(ops // o, (s - 1) // 2)
                    terms.append(Fraction(s - 1, fs * (s - fs)))
                M = max(terms)
                rhs = q ** (4 * b) * M
                if o > rhs:
                    d = prod(r ** fac[r] for r in D)
                    return {
                        "u": u,
                        "factorisation": {str(r): fac[r] for r in primes},
                        "d": d,
                        "p": p,
                        "a": a,
                        "q": q,
                        "b": b,
                        "ord_p_q": o,
                        "max_num": M.numerator,
                        "max_den": M.denominator,
                        "rhs_num": rhs.numerator,
                        "rhs_den": rhs.denominator,
                    }
    return None


def main():
    list_file = sys.argv[1] if len(sys.argv) > 1 else LIST_FILE
    cert_file = sys.argv[2] if len(sys.argv) > 2 else CERT_FILE
    survivor_file = sys.argv[3] if len(sys.argv) > 3 else SURVIVOR_FILE
    values = read_list(list_file)
    eliminated = 0
    with open(cert_file, "w") as cert, open(survivor_file, "w") as surv:
        for i, (u, fac) in enumerate(values):
            c = thm63(u, fac)
            if c is None:
                surv.write(f"{u} [{', '.join(str(r) for r in sorted(fac) for _ in range(fac[r]))}]\n")
            else:
                eliminated += 1
                cert.write(json.dumps(c) + "\n")
            if (i + 1) % 20000 == 0:
                print(f"{i + 1} values done, {eliminated} eliminated", file=sys.stderr, flush=True)
    print(f"values: {len(values)}  eliminated by Theorem 6.3: {eliminated}  survivors: {len(values) - eliminated}")


if __name__ == "__main__":
    main()
