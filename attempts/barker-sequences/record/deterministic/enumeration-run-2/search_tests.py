#!/usr/bin/env python3.11
"""Search for certificates of three necessary conditions on the order 4u^2 of a circulant Hadamard
matrix: Turyn's self-conjugacy test, Leung-Schmidt (2012) Theorem 3.5, and Leung-Schmidt (2012)
Theorem 3.1. A Barker sequence of length n > 13 gives a circulant Hadamard matrix of order n, so a
certificate for u rules out a Barker sequence of length 4u^2.

Usage: search_tests.py LIST CERTS SURVIVORS [tests]
  LIST      lines "u [p1, p2, ...]" (prime factorisation with multiplicity)
  CERTS     output, one JSON certificate per eliminated u (the first test that succeeds, in the
            order turyn, thm35, thm31)
  SURVIVORS output, the values no test eliminated, in the input format
  tests     comma-separated subset of turyn,thm35,thm31 (default all three)

The three tests, in the form implemented here.

Turyn (Pacific J. Math. 15 (1965); Theorem 2 of Borwein-Mossinghoff 2014). If n = 4u^2 is the order
of a circulant Hadamard matrix, r | u, s | n, gcd(r, s) has k >= 1 distinct prime factors and r is
self-conjugate modulo s, then r s <= 2^(k-1) n. Self-conjugate: every prime p | r is semiprimitive
modulo the p-free part s_p of s, i.e. p^j = -1 (mod s_p) for some j. For odd q, whether such a j
exists modulo q^e does not depend on e >= 1 (ord_{q^e}(p) = ord_q(p) q^t), and a common j exists for
a set of odd prime powers exactly when the 2-adic valuations nu_2(ord_q(p)) are all equal and >= 1;
modulo 4 one needs p = 3 (mod 4) and j odd, which forces that common valuation to be 1; modulo 2
nothing is needed. So the search runs over the prime support S of s and the 2-part of s, takes
every exponent at its maximum (s | n allows q^(2 nu_q(u))), and takes r as the product of p^nu_p(u)
over every prime p compatible with S (adding a compatible prime to r never hurts: it multiplies
r s by p^nu_p(u) >= 3 and 2^(k-1) n by at most 2).

Leung-Schmidt 2012, Theorem 3.5. p odd prime, u = p^a m with (m, p) = 1, r | m with r
self-conjugate modulo p (every prime of r has even order modulo p), q_1..q_k the primes of m/r. If
gcd(ord_p(q_1), ..., ord_p(q_k)) > m^2 / r^2 and p^a > 2m then no circulant Hadamard matrix of
order 4u^2 exists. When r = m the gcd is over the empty set, and the conclusion holds by Lemma 3.4
of the paper (m self-conjugate modulo p already gives the congruence the proof needs). The search
takes r maximal, which is optimal on both sides of the inequality.

Leung-Schmidt 2012, Theorem 3.1 (for Hadamard difference sets). n = 4u^2, m | u, w | n, m
self-conjugate modulo v = n/w; then n phi(F) <= w^2 F^2 with F = F(v, u^2/m^2) of Definition 2.10.
F(v, n') = gcd(v, prod_{l in D(v)} l^b(l, v, n')), with
  b(2, v, n') = max_{q in D(n')} [nu_2(q^2 - 1) + nu_2(ord_{v_q}(q)) - 1],
  b(l, v, n') = max_{q in D(n') \ {l}} [nu_l(q^(l-1) - 1) + nu_l(ord_{v_q}(q))]  (l odd),
  v_q = product of the primes of v other than q when v is odd or q = 2, and 4 times the product of
        the odd primes of v other than q when v is even and q is odd,
  b(l, v, n') = 1 when D(n') = {l}.
The search runs over the prime support S of v with every exponent maximal (raising an exponent of v
never hurts), over the 2-part of v (1, 2 or 4), and takes m as the product of the full prime powers
of u over every prime compatible with (S, 2-part) (removing a prime from D(n') never enlarges F);
when every prime is compatible, every choice of one prime left out of m is tried, since n' > 1 is
required.

Orders come from sympy's n_order; the independent checker (check_tests.py) recomputes everything.
"""
import json
import re
import sys
from math import gcd, prod

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


WD = {}


def wieferich_depth(q, l):
    """nu_l(q^(l-1) - 1), capped at 4."""
    key = (q, l)
    if key not in WD:
        x = pow(q, l - 1, l ** 4)
        c = 0
        while c < 4 and x % l ** (c + 1) == 1:
            c += 1
        WD[key] = c
    return WD[key]


def lcm(a, b):
    return a * b // gcd(a, b)


def phi_from_fac(fac):
    return prod((l - 1) * l ** (e - 1) for l, e in fac.items())


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
                assert prod(p ** e for p, e in fac.items()) == u, u
                values.append((u, fac))
    return values


class Tables:
    """Per-u tables: the 2-adic classes and valuations the three tests read."""

    def __init__(self, u, fac):
        self.u = u
        self.fac = fac
        self.P = sorted(fac)
        self.idx = {p: i for i, p in enumerate(self.P)}
        self.w = len(self.P)
        # classmask[p][c] = bitmask of the primes q != p with nu_2(ord_q(p)) = c
        self.classmask = {}
        for p in self.P:
            cm = {}
            for q in self.P:
                if q != p:
                    c = nu(2, ord_mod(p, q))
                    cm[c] = cm.get(c, 0) | (1 << self.idx[q])
            self.classmask[p] = cm

    def compatible(self, p, S, two_part):
        """Is p semiprimitive modulo 2^two_part * prod_{q in S, q != p} q^e (any e >= 1)?

        Returns the common 2-adic class c (>= 1) or 0 when S \ {p} is empty; None when incompatible.
        """
        Q = S & ~(1 << self.idx[p])
        if two_part == 4 and p % 4 != 3:
            return None
        if Q == 0:
            return 0
        for c, mask in self.classmask[p].items():
            if c >= 1 and Q & ~mask == 0:
                if two_part == 4 and c != 1:
                    return None
                return c
        return None

    def support_product(self, S, exponent_factor):
        return prod(self.P[i] ** (exponent_factor * self.fac[self.P[i]]) for i in range(self.w) if S >> i & 1)

    def members(self, S):
        return [self.P[i] for i in range(self.w) if S >> i & 1]


def turyn(t):
    u, n = t.u, 4 * t.u * t.u
    full = (1 << t.w) - 1
    for S in range(1, full + 1):
        s_odd = t.support_product(S, 2)
        if s_odd <= u:  # r s <= u * 4 s_odd <= 4u^2 <= 2^(k-1) n whenever s_odd <= u
            continue
        for two_part in (4, 2):
            R = [p for p in t.P if t.compatible(p, S, two_part) is not None]
            k = sum(1 for p in R if S >> t.idx[p] & 1)
            if k == 0:
                continue
            r = prod(p ** t.fac[p] for p in R)
            s = two_part * s_odd
            if r * s > 2 ** (k - 1) * n:
                return {"test": "turyn", "u": u, "r_primes": R, "s_primes": t.members(S), "s_two_part": two_part,
                        "r": r, "s": s, "k": k}
    return None


def thm35(t):
    u = t.u
    for p in t.P:
        a = t.fac[p]
        m = u // p ** a
        if not p ** a > 2 * m:
            continue
        R = [l for l in t.P if l != p and ord_mod(l, p) % 2 == 0]
        r = prod(l ** t.fac[l] for l in R)
        Q = [q for q in t.P if q != p and q not in R]
        if Q:
            f = 0
            for q in Q:
                f = gcd(f, ord_mod(q, p))
            if not f * r * r > m * m:
                continue
        else:
            f = None
        return {"test": "thm35", "u": u, "p": p, "a": a, "m": m, "r": r, "r_primes": R, "q_primes": Q, "f": f}
    return None


def compute_F(t, S, two_part, Dn):
    """F(v, n') for v = two_part * prod_{l in S} l^(2 nu_l(u)) and D(n') = Dn (a list of primes).

    Returns (F as a factorisation dict, v).
    """
    Sl = t.members(S)
    F = {}
    for l in Sl:
        others = [q for q in Dn if q != l]
        if not others:
            b = 1
        else:
            b = 0
            for q in others:
                vq_val = 0
                for lp in Sl:
                    if lp != q:
                        vq_val = max(vq_val, nu(l, ord_mod(q, lp)))
                b = max(b, wieferich_depth(q, l) + vq_val)
        F[l] = min(2 * t.fac[l], b)
    if two_part > 1:
        e2 = nu(2, two_part)
        b2 = 0
        for q in Dn:
            vq_val = 1 if (two_part == 4 and q % 4 == 3) else 0  # ord_4(q) = 2 when q = 3 (mod 4)
            for lp in Sl:
                if lp != q:
                    vq_val = max(vq_val, nu(2, ord_mod(q, lp)))
            b2 = max(b2, nu(2, q * q - 1) + vq_val - 1)
        F[2] = min(e2, b2)
    v = two_part * t.support_product(S, 2)
    return F, v


def thm31(t):
    u, n = t.u, 4 * t.u * t.u
    full = (1 << t.w) - 1
    for S in range(1, full + 1):
        for two_part in (4, 2):
            compat = [p for p in t.P if t.compatible(p, S, two_part) is not None]
            # candidate sets of primes for m: the compatible primes, all of them, or all but one
            if len(compat) < t.w:
                choices = [compat]
            else:
                choices = [[p for p in compat if p != drop] for drop in compat]
            for Rm in choices:
                Dn = [q for q in t.P if q not in Rm]
                # pruning: F < v/w needs prod_{l in S} l^(2a_l - blow_l) > w, with blow_l a lower bound for b_l
                S_l = t.members(S)
                pmax = 1
                for l in S_l:
                    blow = max([1] + [wieferich_depth(q, l) for q in Dn if q != l])
                    pmax *= l ** max(0, 2 * t.fac[l] - blow)
                w_bound = n // (two_part * t.support_product(S, 2))
                if pmax <= w_bound:
                    continue
                F, v = compute_F(t, S, two_part, Dn)
                w = n // v
                Fval = prod(l ** e for l, e in F.items())
                phiF = phi_from_fac({l: e for l, e in F.items() if e > 0})
                if n * phiF > w * w * Fval * Fval:
                    m = prod(p ** t.fac[p] for p in Rm)
                    return {"test": "thm31", "u": u, "v_primes": S_l, "v_two_part": two_part, "v": v, "w": w,
                            "m_primes": Rm, "m": m, "F": {str(l): e for l, e in F.items()}, "F_value": Fval}
    return None


def main():
    list_file, cert_file, surv_file = sys.argv[1], sys.argv[2], sys.argv[3]
    tests = sys.argv[4].split(",") if len(sys.argv) > 4 else ["turyn", "thm35", "thm31"]
    runners = {"turyn": turyn, "thm35": thm35, "thm31": thm31}
    values = read_list(list_file)
    counts = {name: 0 for name in tests}
    with open(cert_file, "w") as cert, open(surv_file, "w") as surv:
        for i, (u, fac) in enumerate(values):
            t = Tables(u, fac)
            found = None
            for name in tests:
                found = runners[name](t)
                if found:
                    counts[name] += 1
                    cert.write(json.dumps(found) + "\n")
                    break
            if not found:
                surv.write(f"{u} [{', '.join(str(p) for p in sorted(fac) for _ in range(fac[p]))}]\n")
            if (i + 1) % 500 == 0:
                print(f"{i + 1} values done, eliminated so far: {counts}", file=sys.stderr, flush=True)
    print(f"values: {len(values)}  eliminated: {counts}  survivors: {len(values) - sum(counts.values())}")


if __name__ == "__main__":
    main()
