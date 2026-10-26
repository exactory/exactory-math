"""Independent exact finite-core audit; imports no code from the source package.

The two-zero polynomial is checked against subset-DP permanents at n+1 points.
SymPy's exact Sturm implementation verifies its face lower bound. All ORDERED
proper Hall cuts are enumerated; the source enumerates up to transpose.
"""
from fractions import Fraction as F
from math import factorial, isqrt
import json
import sympy as s


def demand(condition, label):
    if not condition:
        raise ArithmeticError(label)


def gamma(n):
    return F(factorial(n), n**n)


def onezero(n):
    return F(factorial(n-2)) * F(n-2, (n-1)**2)**(n-2)


def permanent_integer(matrix):
    n = len(matrix)
    dp = [0]*(1 << n)
    dp[0] = 1
    for mask in range(1, 1 << n):
        row = mask.bit_count()-1
        bits = mask
        while bits:
            bit = bits & -bits
            column = bit.bit_length()-1
            dp[mask] += matrix[row][column]*dp[mask ^ bit]
            bits ^= bit
    return dp[-1]


def certify_face(n):
    m = n-2
    x = s.Symbol('x')
    special = (2-m+m*m*x)/2
    edge = (1-m*x)/2
    poly = s.Poly(factorial(m)*x**(m-2)*(x*x*special**2
                    + 2*m*x*special*edge**2 + m*(m-1)*edge**4), x)
    denominator = 2*m*m
    for t in range(n+1):
        matrix = [[2*t for _ in range(n)] for _ in range(n)]
        for i in range(2):
            for j in range(n):
                matrix[i][j] = matrix[j][i] = m*(m-t)
        matrix[0][0] = matrix[1][1] = (2-m+t)*m*m
        matrix[0][1] = matrix[1][0] = 0
        measured = F(permanent_integer(matrix), denominator**n)
        expected = poly.eval(s.Rational(t,m*m))
        demand(s.Rational(measured.numerator,measured.denominator)==expected,
               f'n={n}, t={t}: permanent interpolation identity')
    lower = onezero(n)*(1+F(1,2*n*n))
    gap = poly - s.Rational(lower.numerator,lower.denominator)
    left, right = s.Rational(m-2,m*m), s.Rational(1,m)
    demand(gap.eval(left)>0 and gap.eval(right)>0, f'n={n}: endpoints')
    demand(gap.count_roots(left,right)==0, f'n={n}: Sturm face bound')
    demand(lower>gamma(n), f'n={n}: strict face gap')


def coefficient(n,a,b):
    p = n-a-b
    c = F(7*n*p*p,16*(a*(n-a)+b*(n-b)))
    if not b:
        c *= 1+(1-gamma(n))**2
    return c


def rational_upper_sqrt(q):
    den = 10**6
    k = isqrt(q.numerator*den*den//q.denominator)
    if F(k,den)**2 < q:
        k += 1
    bound = F(k,den)
    demand(bound**2>=q and F(k-1,den)**2<q,'sqrt enclosure')
    return bound


def margin(n,a,b):
    p = n-a-b
    floor = gamma(n-a)*gamma(n-b)/gamma(p)
    if n<=10:
        floor = max(floor,onezero(n)*(1+F(1,2*n*n)))
    elif not b:
        floor = onezero(n)
    c = coefficient(n,a,b)
    if n<=10:
        upper = rational_upper_sqrt(gamma(n)/c)
        demand(0<upper<1,'localized interval')
        beta = ((1-upper)**n-1+n*upper)/upper**2
        c += beta*floor
    return floor-gamma(n)-F(n*n)*floor*floor/(4*c)


def run():
    for n in range(6,11):
        certify_face(n)
    demand(F(8)*gamma(8)/(2*(1-gamma(8)))<F(1,100),'Pinsker radius')
    demand(gamma(8)/(1-gamma(8))<F(1,400),'log radius')
    demand(F(1987,2187)*F(400,401)>F(7,8),'Taylor coefficient')
    expected_residue={(8,7,0),(9,8,0)}
    observed=set()
    rows=[]
    for n in range(8,16):
        cuts=[(a,b) for a in range(1,n) for b in range(1,n-a)]
        cuts.append((n-1,0))
        values=[]
        for a,b in cuts:
            value=margin(n,a,b)
            if value<=0:
                observed.add((n,a,b))
            values.append(value)
        minimum=min(values)
        rows.append({'n':n,'ordered_cuts':len(cuts),
                     'minimum_numerator':str(minimum.numerator),
                     'minimum_denominator':str(minimum.denominator),
                     'minimum_decimal_diagnostic':float(minimum)})
    demand(observed==expected_residue,'Complete Hall-cut sign pattern')
    print(json.dumps({'face_dimensions':list(range(6,11)),
                      'cut_dimensions':list(range(8,16)),
                      'residual_cuts':sorted(observed),'rows':rows},indent=2))
    print('INDEPENDENT FINITE CORE CERTIFIED; n=8,9 marginal rows remain separate')


if __name__=='__main__':
    run()
