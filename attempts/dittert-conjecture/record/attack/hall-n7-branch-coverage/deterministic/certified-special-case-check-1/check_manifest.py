#!/usr/bin/env python3
"""Independent direct restriction, scalar checks, and exhaustive coverage.

This checker imports neither the encoder nor either pinned verifier.
Polynomial expressions are rebuilt with SymPy. Each leaf is restricted
directly using the binomial theorem, without de Casteljau subdivision.
"""
import copy
import json
from collections import Counter
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

import sympy as S

HERE = Path(__file__).resolve().parent
WIDTH = Q(3, 20)
GAMMA = Q(720, 117649)


def require(value, message):
    if not value:
        raise ValueError(message)


def check_coverage(data):
    classes = {}
    counts = Counter()
    for rowmask in range(128):
        for colmask in range(128):
            i, j = rowmask.bit_count(), colmask.bit_count()
            if i + j <= 7:
                continue
            a, b = 7-i, 7-j
            kind = ("full" if a+b == 0 else "marginal" if a*b == 0
                    else "single-bridge" if a+b == 6 else "ordinary")
            classes[f"{a},{b}"] = kind
            counts[kind] += 1
    require(data["cut_types"] == classes, "Cut type omitted or misclassified")
    require(set(data["trees"]) == {"1,5", "2,4", "3,3"}, "Bridge type omitted")
    summaries = {}
    for pair, leaves in data["trees"].items():
        paths = [leaf["path"] for leaf in leaves]
        require(len(paths) == len(set(paths)) and len(paths) > 0, "Duplicate or empty leaves")
        prefixes = {path[:i] for path in paths for i in range(len(path)+1)}
        terminal = set(paths)
        for prefix in prefixes:
            children = {prefix + "0", prefix + "1"}
            if prefix in terminal:
                require(not children & prefixes, "Leaf contains descendants")
            else:
                require(children <= prefixes, "Internal node has missing child")
        rectangles = []
        for leaf in leaves:
            require(leaf["branch"] in {"direct", "entropy"}, "Missing required sign predicate")
            expected = [[Q(0), WIDTH], [Q(0), WIDTH]]
            for level, bit in enumerate(leaf["path"]):
                require(bit in "01", "Invalid path")
                axis = level % 2
                middle = sum(expected[axis]) / 2
                expected[axis][1 if bit == "0" else 0] = middle
            box = [[Q(x) for x in interval] for interval in leaf["box"]]
            require(box == expected, "Incorrect closed rectangle for path")
            rectangles.append(box)
        area = sum((b[0][1]-b[0][0])*(b[1][1]-b[1][0]) for b in rectangles)
        require(area == WIDTH**2, "Leaf area does not cover the square")
        for index, box in enumerate(rectangles):
            for other in rectangles[index+1:]:
                require(any(max(box[d][0], other[d][0]) >= min(box[d][1], other[d][1])
                            for d in (0, 1)), "Leaf interiors overlap")
        # Arrangement-cell corners and interiors explicitly exercise all junctions.
        coordinates = []
        for axis in (0, 1):
            ends = sorted({q for box in rectangles for q in box[axis]})
            require(ends[0] == 0 and ends[-1] == WIDTH, "Root endpoints missing")
            coordinates.append(sorted(set(ends + [(x+y)/2 for x, y in zip(ends, ends[1:])])))
        for x in coordinates[0]:
            for y in coordinates[1]:
                require(any(b[0][0] <= x <= b[0][1] and b[1][0] <= y <= b[1][1]
                            for b in rectangles), "Uncovered junction or arrangement cell")
        summaries[pair] = {"nodes": len(prefixes), "leaves": len(leaves),
                           "branches": dict(Counter(leaf["branch"] for leaf in leaves)),
                           "depth": max(map(len, paths)), "area": str(area),
                           "junction_probes": len(coordinates[0])*len(coordinates[1])}
    return dict(counts), summaries


def v(k):
    return Q(factorial(k), k**k)


def alpha(k):
    q = Q(k, 7)
    endpoint = q+Q(1, 47) if k <= 3 else q
    return 14*endpoint*(1-endpoint)


def margin(a, b, c, lam):
    lower = v(7-a)*v(7-b)/v(7-a-b)
    denominator = 4*(lam*lower+(1-GAMMA)/c)
    require(denominator > 0, "Nonpositive scalar denominator")
    return lower-GAMMA-49*lower**2/denominator


def scalar_checks():
    require(Q(1,47)**2 > GAMMA/(14*(1-GAMMA)), "Localization")
    require(Q(3,7)+Q(1,47) < Q(1,2), "Entropy monotonic interval")
    require(Q(7,47) < WIDTH and Q(40,47) > Q(17,20), "Subset/line endpoints")
    require((1-GAMMA)*Q(17,20)**2/2 > Q(1,3), "Conditional energy")
    require(v(6)*Q(5,6)**5 > GAMMA, "Zero matrix permanent floor")
    require(Q(5,24)**2 > 7*GAMMA/(1-GAMMA), "Ordinary range")
    require(WIDTH**2 > max(alpha(k) for k in range(1,7))*GAMMA/(1-GAMMA), "Mixed range")
    ordinary = {}
    mixed = {}
    for a in range(1,7):
        for b in range(a,7):
            p = 7-a-b
            if p >= 2:
                ordinary[f"{a},{b}"] = margin(a,b,(alpha(a)+alpha(b))/p**2,Q(329,24))
            if p == 1:
                for sign, positive_size in (("e<=0",b),("f<=0",a)):
                    mixed[f"{a},{b}:{sign}"] = margin(a,b,alpha(positive_size),Q(63,4))
    require(len(ordinary)==6 and len(mixed)==6, "Scalar case omission")
    require(min(ordinary.values())>0 and min(mixed.values())>0, "Scalar sign")
    t = S.Symbol("t")
    g = S.Rational(GAMMA.numerator,GAMMA.denominator)
    w = S.Poly(S.Rational(2,3)*(1-g)**2*(1-t)**6-g*(7-21*t+35*t*t)**2,t)
    coeffs = [Q(w.nth(k)) for k in range(7)]
    bernstein = [sum(coeffs[k]*WIDTH**k*Q(comb(j,k),comb(6,k)) for k in range(j+1))
                 for j in range(7)]
    require(min(bernstein)>0, "Marginal W certificate")
    return {"ordinary_minimum":str(min(ordinary.values())), "mixed_minimum":str(min(mixed.values())),
            "W_minimum":str(min(bernstein)), "ordinary":{k:str(vv) for k,vv in ordinary.items()},
            "mixed":{k:str(vv) for k,vv in mixed.items()}}


def independent_polynomials(a,b):
    e,f=S.symbols("e f")
    m,ell,d=7-a,7-b,min(a,b)
    pa=(1+e/a)**a*(1-e/m)**m
    pb=(1+f/b)**b*(1-f/ell)**ell
    g=S.Rational(GAMMA.numerator,GAMMA.denominator)
    lower=v(m)*v(ell)
    a0=S.Rational(lower.numerator,lower.denominator)*(1-e-f)**7
    k=g-2+pa+pb
    denominator=(m-e)*(ell-f)*(1-e-f)
    squeeze=pa*e/(m-e)+pb*f/(ell-f)-((e+f+d)*k-d*a0)/(1-e-f)
    numerator=S.cancel(denominator*squeeze)
    expressions=(a0-k,numerator,2*a0*numerator**2-3*(k-a0)**2*denominator**2)
    return tuple(S.Poly(expr,e,f,domain=S.QQ) for expr in expressions)


def direct_bernstein_minimum(poly,box):
    # For x=l+wz, x^k = sum_j T[j,k] B_j^d(z).
    degrees=poly.degree_list()
    transforms=[]
    for degree,(left,right) in zip(degrees,box):
        width=right-left
        table=[[sum(Q(comb(k,h))*left**(k-h)*width**h*Q(comb(j,h),comb(degree,h))
                    for h in range(min(j,k)+1)) for k in range(degree+1)]
               for j in range(degree+1)]
        transforms.append(table)
    dx,dy=degrees
    # Contract sparse monomials in the first coordinate, then the second.
    intermediate=[[Q(0) for _ in range(dy+1)] for _ in range(dx+1)]
    for (kx,ky),coefficient in poly.terms():
        value=Q(coefficient)
        for j in range(dx+1):
            intermediate[j][ky]+=value*transforms[0][j][kx]
    return min(sum(intermediate[i][k]*transforms[1][j][k] for k in range(dy+1))
               for i in range(dx+1) for j in range(dy+1))


def mutation_checks(data):
    rejected=0
    def reject(mutated):
        nonlocal rejected
        try:
            check_coverage(mutated)
        except (ValueError, KeyError):
            rejected+=1
        else:
            raise ValueError("Omission mutation was accepted")
    for pair,leaves in data["trees"].items():
        for index in range(len(leaves)):
            bad=copy.deepcopy(data)
            del bad["trees"][pair][index]
            reject(bad)
        bad=copy.deepcopy(data)
        del bad["trees"][pair]
        reject(bad)
    for pair in data["cut_types"]:
        bad=copy.deepcopy(data)
        del bad["cut_types"][pair]
        reject(bad)
    bad=copy.deepcopy(data)
    bad["trees"]["1,5"][0]["branch"]="entropy_without_sign"
    reject(bad)
    return rejected


def main():
    data=json.loads((HERE/"manifest.json").read_text())
    cuts,trees=check_coverage(data)
    scalars=scalar_checks()
    minima={}
    for pair,leaves in data["trees"].items():
        polynomials=independent_polynomials(*map(int,pair.split(",")))
        records=[]
        for leaf in leaves:
            box=[[Q(vv) for vv in interval] for interval in leaf["box"]]
            required=(0,) if leaf["branch"]=="direct" else (1,2)
            bounds={str(i):direct_bernstein_minimum(polynomials[i],box) for i in required}
            require(all(vv>0 for vv in bounds.values()),f"Nonpositive leaf {pair}/{leaf['path']}")
            require(all(vv==Q(leaf["minima"][int(i)]) for i,vv in bounds.items()),"Direct restriction disagrees with emitted coefficients")
            records.append({"path":leaf["path"],"branch":leaf["branch"],"minima":{i:str(vv) for i,vv in bounds.items()}})
        minima[pair]=records
        print(json.dumps({"verified_pair":pair,**trees[pair]}),flush=True)
    rejected=mutation_checks(data)
    output={"status":"pass","cut_mask_count":sum(cuts.values()),"cut_counts":cuts,"trees":trees,
            "scalars":scalars,"leaf_minima":minima,"rejected_omissions":rejected}
    (HERE/"independent-result.json").write_text(json.dumps(output,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"status":"pass","cut_mask_count":sum(cuts.values()),"rejected_omissions":rejected}),flush=True)


if __name__=="__main__":
    main()
