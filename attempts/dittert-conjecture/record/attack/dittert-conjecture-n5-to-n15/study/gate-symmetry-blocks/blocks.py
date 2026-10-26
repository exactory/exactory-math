"""Gate computation: symmetry-adapted block sizes of the SOS Gram spaces for the
Dittert polynomial at dimension n under G_n = (S_n x S_n) x| Z_2 (rows, columns,
transpose), |G_n| = 2 (n!)^2.

Main SOS block: Gram over homogeneous monomials of degree D in the n^2 entries,
D = ceil(n/2) (the certificate has even degree 2D >= n; for odd n the gap
polynomial is multiplied by (sum x)/n first).  Multiplier blocks x_i x_j s_ij:
Gram over monomials of degree D-1, one block per unordered pair of entries,
permuted by G_n; we decompose the direct sum of all of them.

For each irrep rho of G_n with multiplicity m_rho in the monomial space, the
Gram matrix in a symmetry-adapted basis has dim(rho) identical copies of one
m_rho x m_rho block, so the SDP has one PSD variable of size m_rho per irrep.
Multiplicities come from characters: m_rho = (1/|G|) sum_g chi_rho(g) Fix(g),
with Fix(g) the number of monomials fixed by g (permutation action).
Self-checks: S_n character orthogonality, sum m_rho dim(rho) = #monomials,
sum m_rho^2 = #orbits of G on ordered pairs of monomials (Burnside), and every
m_rho a nonnegative integer.
"""
import math, sys
from collections import Counter
from fractions import Fraction

def partitions(n, m=None):
    if m is None: m = n
    if n == 0:
        yield (); return
    for k in range(min(n, m), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest

def class_size(mu, n):
    d = 1
    for k, mk in Counter(mu).items():
        d *= k ** mk * math.factorial(mk)
    return math.factorial(n) // d

def mn_char(lam, mu):
    """Murnaghan-Nakayama rule via beta-numbers."""
    lam = tuple(x for x in lam if x > 0)
    if not mu:
        return 1 if not lam else 0
    k, rest = mu[0], mu[1:]
    L = len(lam)
    beta = [lam[i] + (L - 1 - i) for i in range(L)]
    total = 0
    for i in range(L):
        b = beta[i] - k
        if b < 0 or b in beta:
            continue
        height = sum(1 for x in beta if b < x < beta[i])
        nb = sorted(beta[:i] + [b] + beta[i + 1:], reverse=True)
        newlam = tuple(nb[j] - (L - 1 - j) for j in range(L))
        total += (-1) ** height * mn_char(newlam, rest)
    return total

def perm_of_type(mu, n):
    p = list(range(n)); start = 0
    for k in mu:
        for t in range(k):
            p[start + t] = start + (t + 1) % k
        start += k
    return p

def cycle_lengths(fmap, n):
    seen = [False] * (n * n); out = []
    for s in range(n * n):
        if seen[s]: continue
        L = 0; x = s
        while not seen[x]:
            seen[x] = True; x = fmap(x); L += 1
        out.append(L)
    return out

def fixed_monomials(cycles, D):
    # coefficient of t^D in prod 1/(1 - t^l)
    poly = [0] * (D + 1); poly[0] = 1
    for l in cycles:
        for e in range(l, D + 1):
            poly[e] += poly[e - l]
    return poly[D]

def fixed_pairs(cycles):
    # unordered pairs of distinct entries fixed setwise: both fixed, or a 2-cycle
    f1 = sum(1 for l in cycles if l == 1)
    f2 = sum(1 for l in cycles if l == 2)
    return f1 * (f1 - 1) // 2 + f2

def analyse(n, D):
    parts = list(partitions(n))
    N = n * n
    # S_n character table
    chi = {lam: {mu: mn_char(lam, mu) for mu in parts} for lam in parts}
    dim = {lam: chi[lam][(1,) * n] for lam in parts}
    # orthogonality self-check
    for a in parts:
        for b in parts:
            s = sum(class_size(mu, n) * chi[a][mu] * chi[b][mu] for mu in parts)
            assert s == (math.factorial(n) if a == b else 0), "character table failed orthogonality"
    # classes of G: ('e', mu1, mu2) size |C1||C2| ; ('t', nu) size n! |C_nu|
    classes = []
    for mu1 in parts:
        for mu2 in parts:
            s, p = perm_of_type(mu1, n), perm_of_type(mu2, n)
            cyc = cycle_lengths(lambda x: s[x // n] * n + p[x % n], n)
            classes.append(('e', mu1, mu2, class_size(mu1, n) * class_size(mu2, n), cyc))
    for nu in parts:
        s = perm_of_type(nu, n)
        cyc = cycle_lengths(lambda x: s[x % n] * n + (x // n), n)   # (i,j) -> (s(j), i)
        classes.append(('t', nu, None, math.factorial(n) * class_size(nu, n), cyc))
    G = 2 * math.factorial(n) ** 2
    assert sum(c[3] for c in classes) == G
    # irreps of G
    irreps = []
    for i, lam in enumerate(parts):
        for mu in parts[i + 1:]:
            irreps.append(('pair', lam, mu, 2 * dim[lam] * dim[mu]))
        irreps.append(('diag+', lam, lam, dim[lam] ** 2))
        irreps.append(('diag-', lam, lam, dim[lam] ** 2))
    assert sum(r[3] ** 2 for r in irreps) == G
    def chi_rho(r, c):
        kind, lam, mu, _ = r
        if c[0] == 'e':
            a, b = c[1], c[2]
            if kind == 'pair':
                return chi[lam][a] * chi[mu][b] + chi[mu][a] * chi[lam][b]
            return chi[lam][a] * chi[lam][b]
        nu = c[1]
        if kind == 'pair': return 0
        return chi[lam][nu] if kind == 'diag+' else -chi[lam][nu]
    results = {}
    for label, fixfn, total in (
        (f'main Gram: degree-{D} monomials', lambda c: fixed_monomials(c, D), math.comb(N + D - 1, D)),
        (f'multiplier Grams x_i x_j s_ij: pairs x degree-{D-1} monomials',
         lambda c: fixed_pairs(c) * fixed_monomials(c, D - 1), math.comb(N, 2) * math.comb(N + D - 2, D - 1)),
    ):
        fix = [fixfn(c[4]) for c in classes]
        orbits_pairs = Fraction(sum(c[3] * f * f for c, f in zip(classes, fix)), G)
        assert orbits_pairs.denominator == 1
        mult = []
        for r in irreps:
            m = Fraction(sum(c[3] * chi_rho(r, c) * f for c, f in zip(classes, fix)), G)
            assert m.denominator == 1 and m >= 0, (r, m)
            if m > 0: mult.append((int(m), r[3], r))
        assert sum(m * d for m, d, _ in mult) == total
        assert sum(m * m for m, d, _ in mult) == orbits_pairs
        mult.sort(key=lambda t: -t[0])
        results[label] = (total, int(orbits_pairs), mult)
    return results

if __name__ == '__main__':
    for n in [int(a) for a in sys.argv[1:]] or [4, 5, 6, 7, 8]:
        D = (n + 1) // 2
        print(f"\n===== n = {n}, |G| = {2*math.factorial(n)**2}, certificate degree 2D = {2*D} =====")
        for label, (total, orb, mult) in analyse(n, D).items():
            print(f"-- {label}: unreduced size {total}; commutant dim (sum m^2) = {orb}; "
                  f"{len(mult)} nonzero irreps; largest block {mult[0][0]}")
            print("   blocks (m_rho x m_rho, copies = dim rho): " +
                  ", ".join(f"{m}x{m}(x{d})" for m, d, _ in mult[:12]) + (" ..." if len(mult) > 12 else ""))
