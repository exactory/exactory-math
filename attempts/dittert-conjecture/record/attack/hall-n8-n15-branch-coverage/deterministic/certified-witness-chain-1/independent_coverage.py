#!/usr/bin/env python3
"""Independent finite coverage proof, using Bernstein arithmetic directly.

No code is imported from the source proof or older checkers. Proof decisions
use Fraction arithmetic only. Polynomial products are constructed in the
Bernstein basis on their actual intervals, without power-basis conversion.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from math import comb, factorial, isqrt
import json


def need(value, message):
    if not value:
        raise ArithmeticError(message)


def gamma(n):
    return F(factorial(n), n ** n)


def rectangle(n, a, b):
    return gamma(n - a) * gamma(n - b) / gamma(n - a - b)


def one_zero(n):
    return F(factorial(n - 2) * (n - 2) ** (n - 2), (n - 1) ** (2*n - 4))


def two_zeros(n):
    return one_zero(n) * (1 + F(1, 2*n*n))


def coefficient(n, a, b):
    if a == 0 or b == 0:
        return F(7*n, 16*(n - 1)) * (1 + (1 - gamma(n))**2)
    return F(7*n*(n-a-b)**2, 16*(a*(n-a) + b*(n-b)))


def enclosing_sqrt(q):
    denominator = 10**6
    k = isqrt(q.numerator * denominator**2 // q.denominator)
    if F(k, denominator)**2 < q:
        k += 1
    out = F(k, denominator)
    need(out**2 >= q and F(k-1, denominator)**2 < q, "square-root enclosure")
    return out


def margin(n, a, b):
    c = coefficient(n, a, b)
    m = rectangle(n, a, b) if a*b else one_zero(n)
    if n <= 10:
        m = max(m, two_zeros(n))
        upper = enclosing_sqrt(gamma(n)/c)
        need(0 < upper < 1, "localization is not a subset of [0,1]")
        need(upper**2 >= gamma(n)/c, "unproved discarded parameter tail")
        beta = sum(F(comb(n, k)) * (-upper)**(k-2) for k in range(2, n+1))
        need(beta > 0, "quadratic denominator has wrong sign")
        c = c + beta*m
    need(c > 0 and m > gamma(n), "nonpositive completed-square denominator")
    return m-gamma(n)-n*n*m*m/(4*c)


def expected_types(n):
    """All omitted-size pairs, including full and BOTH marginal orientations."""
    return {(a, b) for a in range(n) for b in range(n) if a+b <= n-1}


def canonical(n, a, b):
    if a == b == 0:
        return "full"
    if a*b == 0:
        return (n-1, 0)
    return (max(a, b), min(a, b))


def validate_types(n, types):
    need(set(types) == expected_types(n), f"n={n}: omitted or extra Hall cut")
    need(len(types) == len(set(types)), f"n={n}: duplicate disguises omitted cut")


@dataclass(frozen=True)
class Interval:
    left: F
    right: F
    closed_left: bool = True
    closed_right: bool = True


def validate_cover(pieces, left, right):
    """Exact closed-domain union check, including point gaps at junctions."""
    pieces = sorted(pieces, key=lambda part: part.left)
    need(bool(pieces), "empty interval cover")
    need(pieces[0].left == left and pieces[0].closed_left, "left endpoint omitted")
    end = pieces[0].right
    end_closed = pieces[0].closed_right
    need(end > left, "invalid first interval")
    for part in pieces[1:]:
        need(part.left < part.right, "invalid interval")
        need(part.left <= end, "interval gap")
        if part.left == end:
            need(end_closed or part.closed_left, "junction endpoint omitted")
        if part.right > end:
            end, end_closed = part.right, part.closed_right
        elif part.right == end:
            end_closed = end_closed or part.closed_right
    need(end == right and end_closed, "right endpoint omitted")


def validate_support(n, support, compressed=False):
    expected = set(range(1, n-1))
    need(set(support) == expected, f"n={n}: omitted support size")
    if compressed:
        need(n == 9, "support compression requires the n=9 constant floor")
        need(max(support) == 7, "largest support-zero count absent")


def elevated(coeff, degree):
    """Degree elevation by convex interpolation; coefficients on [left,right]."""
    result = list(coeff)
    while len(result)-1 < degree:
        old = result
        d = len(old)
        result = [old[0]]
        result += [F(i, d)*old[i-1] + F(d-i, d)*old[i] for i in range(1, d)]
        result += [old[-1]]
    return result


def add(*terms):
    degree = max(len(item)-1 for item in terms)
    padded = [elevated(item, degree) for item in terms]
    return [sum(values, F(0)) for values in zip(*padded)]


def scaled(poly, factor):
    return [factor*coefficient for coefficient in poly]


def times(left, right):
    m, n = len(left)-1, len(right)-1
    # B_i^m B_j^n = choose(m,i) choose(n,j)/choose(m+n,i+j) B_(i+j)^(m+n).
    left_weighted = [comb(m, i)*x for i, x in enumerate(left)]
    right_weighted = [comb(n, i)*x for i, x in enumerate(right)]
    out = [F(0)]*(m+n+1)
    for i, x in enumerate(left_weighted):
        for j, y in enumerate(right_weighted):
            out[i+j] += x*y
    return [value/comb(m+n, k) for k, value in enumerate(out)]


def power(poly, exponent):
    result = [F(1)]
    for _ in range(exponent):
        result = times(result, poly)
    return result


def linear(constant, slope, left, right):
    return [constant+slope*left, constant+slope*right]


def evaluate(poly, t):
    values = list(poly)
    while len(values) > 1:
        values = [(1-t)*x+t*y for x, y in zip(values, values[1:])]
    return values[0]


def bisect(poly):
    levels = [list(poly)]
    while len(levels[-1]) > 1:
        levels += [[(a+b)/2 for a,b in zip(levels[-1], levels[-1][1:])]]
    return [row[0] for row in levels], [row[-1] for row in reversed(levels)]


def positive(poly, depth=0):
    if min(poly) > 0:
        return 1, depth
    need(depth < 12, "Bernstein certificate did not close")
    left, right = bisect(poly)
    a, da = positive(left, depth+1)
    b, db = positive(right, depth+1)
    return a+b, max(da, db)


def base_polys(n, left, right):
    g = gamma(n)
    e = linear(F(1), -(2-g), left, right)
    h = linear(F(0), 1-g, left, right)
    t = add(e, scaled(h, -F(1,n-1)))
    q = add(scaled(power(e,n-1), 2-g), scaled(power(t,n-1), -1))
    v = linear(F(1), F(-1), left, right)
    return e,h,t,q,v


def near_poly(n, left, right):
    e,h,t,_,v = base_polys(n,left,right)
    f = times(v,power(linear(F(1), F(1,n-1),left,right),n-1))
    first = add([2-gamma(n)], scaled(power(v,n), two_zeros(n)), scaled(f,-1))
    return add(times(first,power(e,n)),scaled(times(add(e,h),power(t,n-1)),-1))


def support_poly(n, z, left, right):
    e,h,t,q,v = base_polys(n,left,right)
    m = n-1-z
    floor = two_zeros(n)
    if n == 8:
        floor = max(floor, rectangle(n,z,1))
    s = add(
        times(add([2-gamma(n)],scaled(power(v,n),floor)),power(e,n)),
        scaled(times(add(e,h),power(t,n-1)),-1))
    w = add(
        times(linear(F(n-1),F(1),left,right),q),
        scaled(power(e,n-1),-m))
    return add(
        scaled(times(power(q,n-1),s),z**z),
        scaled(times(times(v,power(e,n+(n-1)*m)),power(w,z)),-1))


def quantities(n, u):
    e = 1-(2-gamma(n))*u
    need(e>0, "marginal denominator")
    h = (1-gamma(n))*u/e
    need(0 <= h < n-1, "column-product domain")
    f = (1-u)*(1+u/F(n-1))**(n-1)
    g = (1+h)*(1-h/F(n-1))**(n-1)
    q = 2-gamma(n)-(1-h/F(n-1))**(n-1)
    return e,h,f,g,q


def near_literal(n, u):
    e,h,f,g,q = quantities(n,u)
    return (two_zeros(n)*(1-u)**n-gamma(n)+2-f-g)*e**n


def support_literal(n, z, u):
    e,h,f,g,q = quantities(n,u)
    m = n-1-z
    floor = max(two_zeros(n),rectangle(n,z,1)) if n == 8 else two_zeros(n)
    u_bound = (1-u)*q**(-m)*((n-1+u-m/q)/z)**z
    return (floor*(1-u)**n-gamma(n)+2-u_bound-g)*z**z*(e**(n-1)*q)**(n-1)*e**n


def check_literal(poly, literal, left, right):
    # These points check arithmetic implementation, not an interpolation proof.
    for t in (F(0), F(1,3), F(1,2), F(1)):
        need(evaluate(poly,t) == literal(left+(right-left)*t), "polynomial identity regression")


def must_reject(action, label):
    try:
        action()
    except ArithmeticError:
        return
    raise ArithmeticError(f"mutation was accepted: {label}")


def regression():
    for n in range(8,16):
        complete = expected_types(n)
        for missing in ((0,0),(0,1),(1,0),(1,1),(1,n-2),(n-2,1)):
            must_reject(lambda n=n,missing=missing: validate_types(n,complete-{missing}),
                        f"omitted n={n} cut={missing}")
        must_reject(lambda n=n: validate_support(n,range(1,n-2)), "largest support omitted")
    pieces = [Interval(F(0),F(1,2)),Interval(F(1,2),F(1))]
    validate_cover(pieces,F(0),F(1))
    must_reject(lambda:validate_cover([replace(pieces[0],closed_right=False),
                                     replace(pieces[1],closed_left=False)],F(0),F(1)),
                "open junction")
    must_reject(lambda:validate_cover([replace(pieces[0],closed_left=False),pieces[1]],F(0),F(1)),
                "open zero endpoint")
    must_reject(lambda:validate_cover([pieces[0],replace(pieces[1],closed_right=False)],F(0),F(1)),
                "open terminal endpoint")
    must_reject(lambda:validate_cover([pieces[0],replace(pieces[1],left=F(3,4))],F(0),F(1)),
                "positive-width gap")
    q = gamma(10)/coefficient(10,9,0)
    bound = enclosing_sqrt(q)
    must_reject(lambda:need((bound-F(1,10**6))**2 >= q,"localization"),
                "rounding down localization")
    must_reject(lambda:validate_support(8,range(1,7),compressed=True),
                "unproved n=8 support compression")
    # A nonpositive Bernstein polynomial must never pass, even under python -O.
    must_reject(lambda:positive([F(-1)]), "negative polynomial")
    need(times([F(0),F(1)],[F(0),F(1)])==[F(0),F(0),F(1)],"Bernstein product")
    need(elevated([F(0),F(1)],2)==[F(0),F(1,2),F(1)],"Bernstein elevation")
    return 65


def run():
    rows = []
    uncompressed = 0
    observed_residue = set()
    for n in range(8,16):
        need(n*gamma(n)/(2*(1-gamma(n))) < F(1,100),"global subset localization")
        need(gamma(n)/(1-gamma(n)) < F(1,400),"global log localization")
        need(F(1987,2187)*F(400,401)>F(7,8),"Taylor factor")
        need(rectangle(n,1,1)==one_zero(n),"one-zero rectangle identity")
        types = sorted(expected_types(n))
        validate_types(n,types)
        need(len(types)==n*(n+1)//2,"uncompressed cut count")
        uncompressed += len(types)
        representatives = {canonical(n,a,b) for a,b in types}-{ "full" }
        ordered = [(a,b) for a,b in types if a*b]+[(n-1,0)]
        need(len(ordered)==(n-1)*(n-2)//2+1,"ordered cut count")
        values = []
        for a,b in ordered:
            value = margin(n,a,b)
            values += [value]
            need(margin(n,a,b)==margin(n,b,a),"transposition changed a scalar margin")
            if value <= 0:
                observed_residue.add((n,a,b))
        # Every uncompressed type is either full or a checked representative.
        checked = {canonical(n,a,b) for a,b in ordered}
        need(representatives==checked,"cut normalization lost a case")
        rows += [{"n":n,"uncompressed":len(types),"ordered":len(ordered),
                  "minimum_margin":str(min(values))}]
    need(observed_residue=={(8,7,0),(9,8,0)},"unexpected finite residue")
    need(uncompressed==596,"full size-pair range was not covered")

    support_results = []
    for n,split,stop in ((8,F(1,400),F(1,20)),(9,F(1,500),F(3,100))):
        validate_cover([Interval(F(0),split),Interval(split,stop)],F(0),stop)
        e,h,f,g,q = quantities(n,stop)
        need(2-f-g>gamma(n),"entire marginal tail not excluded")
        need(quantities(n,split)[4]>1,"row cap not valid at left endpoint")
        poly = near_poly(n,F(0),split)
        need(len(poly)-1<=2*n,"near-zero degree")
        check_literal(poly,lambda u,n=n:near_literal(n,u),F(0),split)
        leaves,depth = positive(poly)
        support_results += [{"n":n,"case":"near-zero","leaves":leaves,"depth":depth}]
        validate_support(n,range(1,n-1),compressed=(n==9))
        zero_counts = range(1,7) if n==8 else (7,)
        for z in zero_counts:
            poly = support_poly(n,z,split,stop)
            need(len(poly)-1==n*n+1,"support polynomial degree")
            check_literal(poly,lambda u,n=n,z=z:support_literal(n,z,u),split,stop)
            leaves,depth = positive(poly)
            support_results += [{"n":n,"case":f"support z={z}","leaves":leaves,"depth":depth}]
    mutations = regression()
    print(json.dumps({"uncompressed_size_pairs":uncompressed,
                      "ordered_scalar_cases":sum(r["ordered"] for r in rows),
                      "rows":rows,"residual_certificates":support_results,
                      "mutation_and_arithmetic_regressions":mutations},indent=2))
    print("INDEPENDENT COVERAGE CERTIFIED: every n=8,...,15 Hall branch and endpoint")


if __name__ == "__main__":
    run()
