"""Produce candidate Lean Bernstein identities; only Lean establishes correctness.

All output is written to stdout for a caller to save using apply_patch.
This independent power-basis generator imports no inherited checker code.
"""
from fractions import Fraction as Q
from math import comb, factorial
import json


def add(*terms):
    out = [Q(0)] * max(map(len, terms))
    for term in terms:
        for i, value in enumerate(term):
            out[i] += value
    return out


def scale(term, value):
    return [value * x for x in term]


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def power(a, k):
    out = [Q(1)]
    for _ in range(k):
        out = mul(out, a)
    return out


def rational(q):
    return f"({q.numerator} / {q.denominator} : ℝ)"


def candidate(n, d):
    g = Q(factorial(n), n**n)
    lower = Q(factorial(n-2) * (n-2)**(n-2), (n-1)**(2*n-4)) * (1+Q(1,2*n*n))
    e = [Q(1), -(2-g)/d]
    h = [Q(0), (1-g)/d]
    t = add(e, scale(h, -Q(1,n-1)))
    v = [Q(1), -Q(1,d)]
    f = mul(v, power([Q(1), Q(1,d*(n-1))], n-1))
    p = add(mul(add([2-g],scale(power(v,n),lower),scale(f,-1)),power(e,n)),
            scale(mul(add(e,h),power(t,n-1)),-1))
    degree = len(p)-1
    # Coefficients for the unnormalized homogeneous basis x^k*(1-x)^(N-k).
    b = [sum((p[i]*comb(degree-i,k-i) for i in range(k+1)),Q(0)) for k in range(degree+1)]
    assert degree == 2*n and min(b) > 0
    expr = " +\n    ".join(f"{rational(c)} * x^{k} * (1-x)^{degree-k}" for k,c in enumerate(b))
    source = f'''import Definitions
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

set_option maxHeartbeats 4000000

noncomputable section
namespace NearZero

def certificate{n} (x : ℝ) : ℝ :=
    {expr}

theorem identity{n} (x : ℝ) : p {n} (x/{d}) = certificate{n} x := by
  norm_num [p, gamma, lower, kappa, e, h, t, f, Nat.factorial, certificate{n}]
  ring

theorem positive{n} (x : ℝ) (hx : 0 ≤ x) (hx1 : x ≤ 1) :
    0 < certificate{n} x := by
  have hy : 0 ≤ 1-x := sub_nonneg.mpr hx1
  by_cases hlt : x < 1
  · have hyp : 0 < 1-x := sub_pos.mpr hlt
    unfold certificate{n}
    positivity
  · have heq : x = 1 := le_antisymm hx1 (le_of_not_gt hlt)
    subst x
    norm_num [certificate{n}]

end NearZero
'''
    return source, {"dimension":n,"interval_denominator":d,"degree":degree,
                    "positive_coefficients":len(b),"smallest":str(min(b)),
                    "coefficients":[str(x) for x in b]}


files = {}
metadata = []
for n,d in [(8,400),(9,500)]:
    source, info = candidate(n,d)
    files[f"Certificate{n}.lean"] = source
    metadata.append(info)
files["candidate-data.json"] = json.dumps(metadata,indent=2) + "\n"
print(json.dumps(files))
