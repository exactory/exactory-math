#!/usr/bin/env python3
"""Independent checker for the Theorem 6.3 certificates written by search_thm63.py.

This program shares no code with the search: primality is decided by its own deterministic
Miller-Rabin test, p - 1 is factored by its own trial division, multiplicative orders are computed
by its own routine, and every quantity of Theorem 6.3 (Leung-Schmidt 2016) is recomputed from the
certificate's (u, d, p, q) alone. Standard library only.

Exit status 0 when every certificate is valid, the eliminated values are distinct members of the
list, the survivors are exactly the remaining members, and the totals agree with the published
counts (229,682 eliminated, 8,125 surviving, smallest survivor 30109 * 1128713 * 2167849 * 268813277).
"""
import json
import re
import sys
from fractions import Fraction
from functools import lru_cache
from math import gcd

LIST_FILE = sys.argv[1] if len(sys.argv) > 1 else "BarkerCandidates100.txt"
CERT_FILE = sys.argv[2] if len(sys.argv) > 2 else "certificates_thm63.jsonl"
SURVIVOR_FILE = sys.argv[3] if len(sys.argv) > 3 else "survivors_thm63.txt"
EXPECTED = None if len(sys.argv) > 4 and sys.argv[4] == "nocount" else (229682, 8125, 30109 * 1128713 * 2167849 * 268813277)


def is_prime(n):
    """Deterministic Miller-Rabin for n < 3,317,044,064,679,887,385,961,981 (bases up to 41)."""
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
    """Prime factorisation of n by trial division (n < 10^12 here); memoised, the list has 148 primes."""
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


@lru_cache(maxsize=None)
def order_mod_prime_power(x, s, e):
    """Multiplicative order of x modulo s^e for a prime s not dividing x; memoised."""
    mod = s ** e
    group = (s - 1) * s ** (e - 1)
    fac = dict(factor_trial(s - 1))
    if e > 1:
        fac[s] = fac.get(s, 0) + (e - 1)
    o = group
    for ell in fac:
        while o % ell == 0 and pow(x, o // ell, mod) == 1:
            o //= ell
    return o


def lcm(a, b):
    return a * b // gcd(a, b)


def order_mod_composite(x, fac):
    """Order of x modulo prod s^e for the factorisation fac = {s: e}, x coprime to it."""
    o = 1
    for s, e in fac.items():
        o = lcm(o, order_mod_prime_power(x, s, e))
    return o


def val(p, x):
    v = 0
    while x % p == 0:
        x //= p
        v += 1
    return v


def read_list(path):
    values = {}
    with open(path) as fh:
        for line in fh:
            m = re.match(r"^(\d+)\s+\[([\d,\s]+)\]\s*$", line)
            if m:
                u = int(m.group(1))
                fac = {}
                for p in (int(x) for x in m.group(2).split(",")):
                    fac[p] = fac.get(p, 0) + 1
                values[u] = fac
    return values


def phi_of(fac):
    r = 1
    for s, e in fac.items():
        r *= (s - 1) * s ** (e - 1)
    return r


def check_certificate(c, fac_list):
    u, d, p, a, q, b = c["u"], c["d"], c["p"], c["a"], c["q"], c["b"]
    fac = fac_list[u]
    # the factorisation of u: primes, product, all 1 mod 4, u odd
    prod = 1
    for s, e in fac.items():
        if not is_prime(s) or s % 4 != 1:
            return "bad prime in factorisation"
        prod *= s ** e
    if prod != u or u % 2 == 0 or u <= 1:
        return "factorisation does not give u"
    if p not in fac or q not in fac or p == q:
        return "p or q not a prime of u"
    if u % d != 0 or gcd(d, u // d) != 1 or d % p == 0:
        return "d is not a unitary divisor of u coprime to p"
    if a != fac[p] or b != fac[q]:
        return "wrong exponent a or b"
    ud_fac = {s: e for s, e in fac.items() if d % s != 0}  # factorisation of u/d
    # (107): phi(d^2) < p phi(u^2) / (2 u^2)   <=>   2 u^2 phi(d^2) < p phi(u^2)
    d_fac = {s: e for s, e in fac.items() if d % s == 0}
    phi_d2 = phi_of({s: 2 * e for s, e in d_fac.items()})
    phi_u2 = phi_of({s: 2 * e for s, e in fac.items()})
    if not 2 * u * u * phi_d2 < p * phi_u2:
        return "(107) fails"
    # (108) for every prime r of u other than p and q
    for r in fac:
        if r in (p, q):
            continue
        lhs = val(p, order_mod_prime_power(r, p, 2 * a))
        rfree = {s: e for s, e in ud_fac.items() if s != r}
        rhs = val(p, order_mod_composite(r, rfree))
        if not lhs > rhs:
            return f"(108) fails for r = {r}"
    # (109)
    o = order_mod_prime_power(q, p, 1)
    if o != c["ord_p_q"]:
        return "ord_p(q) differs"
    e0 = val(2, o)
    S = [s for s in ud_fac if s != p]
    terms = [Fraction(2, q * q)]
    for s in S:
        if s == q:
            continue
        os_ = order_mod_prime_power(q, s, 1)
        if e0 >= 1 and val(2, os_) == e0:
            continue
        ops = lcm(o, os_)
        fs = min(ops // o, (s - 1) // 2)
        terms.append(Fraction(s - 1, fs * (s - fs)))
    M = max(terms)
    if M != Fraction(c["max_num"], c["max_den"]):
        return "max term differs"
    rhs = q ** (4 * b) * M
    if rhs != Fraction(c["rhs_num"], c["rhs_den"]):
        return "right-hand side differs"
    if not o > rhs:
        return "(109) is not violated"
    return None


def main():
    values = read_list(LIST_FILE)
    eliminated = set()
    bad = 0
    n = 0
    with open(CERT_FILE) as fh:
        for line in fh:
            if not line.strip():
                continue
            c = json.loads(line)
            n += 1
            if c["u"] not in values:
                print(f"certificate for a value not in the list: {c['u']}")
                bad += 1
                continue
            if c["u"] in eliminated:
                print(f"duplicate certificate: {c['u']}")
                bad += 1
                continue
            err = check_certificate(c, values)
            if err:
                print(f"INVALID certificate for u = {c['u']}: {err}")
                bad += 1
            else:
                eliminated.add(c["u"])
    survivors = set(read_list(SURVIVOR_FILE))
    ok = bad == 0
    if survivors & eliminated:
        print("a value is both eliminated and surviving")
        ok = False
    if survivors | eliminated != set(values):
        print("eliminated and surviving values do not partition the list")
        ok = False
    print(f"certificates read: {n}, valid: {len(eliminated)}, invalid: {bad}, survivors: {len(survivors)}")
    if EXPECTED is not None:
        exp_elim, exp_surv, exp_min = EXPECTED
        if len(eliminated) != exp_elim or len(survivors) != exp_surv or min(survivors) != exp_min:
            print(f"counts differ from the published ones: expected {exp_elim} eliminated, {exp_surv} survivors, smallest {exp_min}; got smallest {min(survivors) if survivors else None}")
            ok = False
        else:
            print("counts agree with Leung-Schmidt 2016: 229,682 eliminated, 8,125 survivors, smallest survivor as published")
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
