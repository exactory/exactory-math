"""Emit Cert/Data6.lean from lean-cert6.json.

The two multiplier blocks carry the same five integers as at n = 5 (dim, den, d, F, delta) plus
their orbit values.  The main block carries its orbit values, its denominator, and the two
floating-point constants of the verified route.  Those two are rounded to exact powers of two,
`d` upwards and `alpha` downwards, so that the Lean literal is the same double as the Python one
with no reliance on how either language parses a decimal: a power of two has an exact, short
decimal form that every correctly-rounding parser reproduces.  Rounding `alpha` down and `d` up
only weakens the criterion, so the check Lean runs is no easier than the one verified here.

Usage: python lean-data6-emit.py lean-cert6.json ../deterministic/formal-check-1/Cert/Data6.lean
"""
import json
import math
import sys

src, dst = sys.argv[1], sys.argv[2]
c = json.load(open(src))
U = 2.0 ** -53
main = c["main"]
dim = main["dim"]

d_py = float.fromhex(main["d_hex"])
alpha_py = float.fromhex(main["alpha_hex"])
d = 2.0 ** math.ceil(math.log2(d_py))
alpha = 2.0 ** math.floor(math.log2(alpha_py))
gam = (dim + 1) * U / (1 - (dim + 1) * U)
err = 10 * (gam * main["expected_sumL2"] + 3 * U * 0.0 + (dim + 1) * U * 0.0)
err_full = main["expected_err"]
print(f"d: {d_py:.6e} -> 2^{int(math.log2(d))} = {d:.6e}")
print(f"alpha: {alpha_py:.6e} -> 2^{int(math.log2(alpha))} = {alpha:.6e}")
print(f"Higham bound {err_full:.6e}; margin with the rounded alpha: {alpha / err_full:.2f}x")
assert alpha > err_full, "rounding alpha down to a power of two loses the margin"

body = [
    "import Cert.Core",
    "",
    "/-! Certificate data for n = 6, produced by study/lean-data6-emit.py from",
    "  study/lean-cert6.json.  Each Gram matrix is M = A / den, with A the integer matrix whose",
    "  (a, b) entry is `Vals[orbit index of (a, b)]`.  The two 666 x 666 multiplier matrices carry",
    "  `d`, `F`, `delta` for the exact integer route of Cert/Sym.lean; the 8436 x 8436 main matrix",
    "  carries `denF`, `dF` and `alphaF` for the verified floating-point route, the last two exact",
    "  powers of two.  The orbit values are carried as strings and parsed at run time: array",
    f"  literals of this size exceed Lean's elaboration budget.  lambda = {c['lambda_num']}/{c['lambda_den']}. -/",
    "",
    "namespace Cert6",
    "open Cert",
    "",
    f"def lamNum : Int := {c['lambda_num']}",
    f"def lamDen : Int := {c['lambda_den']}",
    "",
    f"def mainDim : Nat := {dim}",
    f"def mainDen : Int := {main['den']}",
    f"def mainDenF : Float := {float(int(main['den']))!r}",
    f"def mainDF : Float := {d!r}",
    f"def mainAlphaF : Float := {alpha!r}",
    f'def mainValsStr : String := "{",".join(main["orbit_values"])}"',
    "def mainVals : Array Int := parseInts mainValsStr",
    "",
]
for name in ("aligned", "generic"):
    b = c[name]
    body += [
        f"def {name}Dim : Nat := {b['dim']}",
        f"def {name}Den : Int := {b['den']}",
        f"def {name}D : Int := {b['d']}",
        f"def {name}F : Int := {b['F']}",
        f"def {name}Delta : Int := {b['delta']}",
        f'def {name}ValsStr : String := "{",".join(b["orbit_values"])}"',
        f"def {name}Vals : Array Int := parseInts {name}ValsStr",
        "",
    ]
body += ["end Cert6", ""]
open(dst, "w").write("\n".join(body))
print(f"wrote {dst} ({len('\n'.join(body)) / 1e3:.1f} KB)")
