#!/usr/bin/env python3
"""Independent checker for the certificates written by search_tests.py (Turyn's self-conjugacy test,
Leung-Schmidt 2012 Theorem 3.5, Leung-Schmidt 2012 Theorem 3.1).

Shares no code with the search: own primality test, own trial-division factorisation, own order
routine, and every self-conjugacy claim is verified by an explicit exponent J with p^J = -1
(mod s_p), computed by modular exponentiation. Standard library only.

Usage: check_tests.py LIST CERTS SURVIVORS
Exit status 0 when every certificate is valid, the eliminated values are distinct members of the
list, and eliminated plus survivors is exactly the list.
"""
import json
import re
import sys
from math import gcd


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
    return f


def order_prime_power(x, s, e):
    """Order of x modulo s^e (s prime, x coprime to s)."""
    mod = s ** e
    fac = factor_trial(s - 1)
    if e > 1:
        fac[s] = fac.get(s, 0) + (e - 1)
    o = (s - 1) * s ** (e - 1)
    for ell in fac:
        while o % ell == 0 and pow(x, o // ell, mod) == 1:
            o //= ell
    return o


def lcm(a, b):
    return a * b // gcd(a, b)


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
            m = re.match(r"^\s*(\d+)\s+\[([\d,\s]+)\]\s*$", line)
            if m:
                u = int(m.group(1))
                fac = {}
                for p in (int(x) for x in m.group(2).split(",")):
                    fac[p] = fac.get(p, 0) + 1
                values[u] = fac
    return values


def factorisation_ok(u, fac):
    prod = 1
    for s, e in fac.items():
        if not is_prime(s):
            return False
        prod *= s ** e
    return prod == u and u % 2 == 1 and u > 1


def semiprimitive_witness(p, modulus):
    """Return J with p^J = -1 (mod modulus), or None. modulus is coprime to p."""
    if modulus <= 2:
        return 0
    fac = factor_trial(modulus) if modulus < 10 ** 12 else None
    if fac is None:
        # the moduli here are products of known prime powers; factor by the list primes instead
        return None
    J = 1
    for s, e in fac.items():
        if s == 2:
            continue
        J = lcm(J, order_prime_power(p, s, e))
    if J % 2:
        return None
    J //= 2
    return J if pow(p, J, modulus) == modulus - 1 else None


def semiprimitive_witness_fac(p, mod_fac):
    """Same as semiprimitive_witness, with the modulus given by its factorisation {s: e}."""
    modulus = 1
    for s, e in mod_fac.items():
        modulus *= s ** e
    if modulus <= 2:
        return 0
    J = 1
    for s, e in mod_fac.items():
        if s == 2:
            continue
        J = lcm(J, order_prime_power(p, s, e))
    if J % 2:
        return None
    J //= 2
    return J if pow(p, J, modulus) == modulus - 1 else None


def check_turyn(c, u, fac):
    n = 4 * u * u
    R, S, two = c["r_primes"], c["s_primes"], c["s_two_part"]
    if two not in (1, 2, 4):
        return "bad 2-part"
    if any(p not in fac for p in R) or any(q not in fac for q in S) or len(set(R)) != len(R) or len(set(S)) != len(S):
        return "r or s carries a prime not in u"
    r = 1
    for p in R:
        r *= p ** fac[p]
    s_fac = {q: 2 * fac[q] for q in S}
    if two > 1:
        s_fac[2] = val(2, two)
    s = two
    for q in S:
        s *= q ** (2 * fac[q])
    if r != c["r"] or s != c["s"] or u % r or n % s:
        return "r or s wrong or not a divisor"
    k = len(set(R) & set(S))
    if k < 1 or k != c["k"]:
        return "k wrong"
    for p in R:
        s_p_fac = {q: e for q, e in s_fac.items() if q != p}
        if semiprimitive_witness_fac(p, s_p_fac) is None:
            return f"{p} is not semiprimitive modulo the p-free part of s"
    if not r * s > 2 ** (k - 1) * n:
        return "Turyn's inequality is not violated"
    return None


def check_thm35(c, u, fac):
    p, a, r = c["p"], c["a"], c["r"]
    if p not in fac or fac[p] != a:
        return "p or a wrong"
    m = u // p ** a
    if m != c["m"] or not p ** a > 2 * m:
        return "p^a > 2m fails"
    if m % r:
        return "r does not divide m"
    r_fac = factor_trial(r) if r < 10 ** 12 else {q: fac[q] for q in c["r_primes"]}
    rr = 1
    for q, e in r_fac.items():
        rr *= q ** e
    if rr != r or any(q not in fac or e > fac[q] for q, e in r_fac.items()):
        return "r factorisation wrong"
    for q in r_fac:
        o = order_prime_power(q, p, 1)
        if o % 2 or pow(q, o // 2, p) != p - 1:
            return f"{q} has odd order modulo p"
    Q = [q for q in fac if q != p and q not in r_fac]
    if sorted(Q) != sorted(c["q_primes"]):
        return "q list wrong"
    if Q:
        f = 0
        for q in Q:
            f = gcd(f, order_prime_power(q, p, 1))
        if f != c["f"] or not f * r * r > m * m:
            return "gcd condition fails"
    return None


def F_of(v_fac, Dn):
    """F(v, n') of Leung-Schmidt 2012, Definition 2.10, for v given by its factorisation and D(n') = Dn."""
    odd = [l for l in v_fac if l != 2]
    v_even = 2 in v_fac
    F = {}
    for l in v_fac:
        if l == 2:
            qs = list(Dn)
        else:
            qs = [q for q in Dn if q != l]
        if not qs:
            b = 2 if l == 2 else 1
        else:
            b = 0
            for q in qs:
                # v_q: primes of v other than q (odd v or q = 2), else 4 * (odd primes of v other than q)
                if not v_even or q == 2:
                    mod_fac = {lp: 1 for lp in v_fac if lp != q}
                else:
                    mod_fac = {lp: 1 for lp in odd if lp != q}
                    mod_fac[2] = 2
                o = 1
                for lp, e in mod_fac.items():
                    o = lcm(o, order_prime_power(q, lp, e))
                if l == 2:
                    b = max(b, val(2, q * q - 1) + val(2, o) - 1)
                else:
                    b = max(b, val(l, pow(q, l - 1, l ** 6) - 1 if pow(q, l - 1, l ** 6) != 1 else l ** 6) + val(l, o))
        F[l] = min(v_fac[l], b)
    return F


def check_thm31(c, u, fac):
    n = 4 * u * u
    S, two, Rm = c["v_primes"], c["v_two_part"], c["m_primes"]
    if two not in (1, 2, 4) or any(l not in fac for l in S) or any(p not in fac for p in Rm):
        return "bad support"
    if set(Rm) == set(fac):
        return "m = u is not allowed (n' = 1)"
    v_fac = {l: 2 * fac[l] for l in S}
    if two > 1:
        v_fac[2] = val(2, two)
    v = 1
    for l, e in v_fac.items():
        v *= l ** e
    if v != c["v"] or n % v:
        return "v wrong"
    w = n // v
    if w != c["w"]:
        return "w wrong"
    m = 1
    for p in Rm:
        m *= p ** fac[p]
    if m != c["m"]:
        return "m wrong"
    for p in Rm:
        s_p_fac = {l: e for l, e in v_fac.items() if l != p}
        if semiprimitive_witness_fac(p, s_p_fac) is None:
            return f"{p} is not semiprimitive modulo the p-free part of v"
    Dn = [q for q in fac if q not in Rm]
    F = F_of(v_fac, Dn)
    Fval = 1
    phiF = 1
    for l, e in F.items():
        Fval *= l ** e
        if e > 0:
            phiF *= (l - 1) * l ** (e - 1)
    if Fval != c["F_value"]:
        return f"F differs: checker {Fval}, certificate {c['F_value']}"
    if not n * phiF > w * w * Fval * Fval:
        return "the inequality of Theorem 3.1 is not violated"
    return None


CHECKS = {"turyn": check_turyn, "thm35": check_thm35, "thm31": check_thm31}


def main():
    list_file, cert_file, surv_file = sys.argv[1], sys.argv[2], sys.argv[3]
    values = read_list(list_file)
    eliminated = set()
    bad = 0
    n = 0
    per_test = {}
    with open(cert_file) as fh:
        for line in fh:
            if not line.strip():
                continue
            c = json.loads(line)
            n += 1
            u = c["u"]
            if u not in values or not factorisation_ok(u, values[u]):
                print(f"value not in the list or bad factorisation: {u}")
                bad += 1
                continue
            if u in eliminated:
                print(f"duplicate certificate: {u}")
                bad += 1
                continue
            err = CHECKS[c["test"]](c, u, values[u])
            if err:
                print(f"INVALID {c['test']} certificate for u = {u}: {err}")
                bad += 1
            else:
                eliminated.add(u)
                per_test[c["test"]] = per_test.get(c["test"], 0) + 1
    survivors = set(read_list(surv_file))
    ok = bad == 0
    if survivors & eliminated:
        print("a value is both eliminated and surviving")
        ok = False
    if survivors | eliminated != set(values):
        print("eliminated and surviving values do not partition the list")
        ok = False
    print(f"certificates read: {n}, valid: {len(eliminated)} {per_test}, invalid: {bad}, survivors: {len(survivors)}, list: {len(values)}")
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
