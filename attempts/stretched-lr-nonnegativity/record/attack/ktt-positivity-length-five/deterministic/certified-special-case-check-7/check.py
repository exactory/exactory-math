#!/usr/bin/env python3
"""Independent check of the form screen.

1. The recorded counts against the recorded weight lists in `screen.json`.
2. The codimension-five identity on the unimodular six-simplex, recomputed for two forms with the
   simplex's edges derived from the polytope by Normaliz rather than from the hand-written normal
   sets the run used. The sum must be H_6 = 49/20.
3. The module against recorded weights on a fresh sample, disjoint from the run's.
4. The five classes that survive every form: recomputed under the best form the screen found.
Exit 0 iff all four hold.
"""
import json
import os
import random
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from forms import named  # noqa: E402
from transverse_q import transverse_weight_q  # noqa: E402

D = 6
bad = 0
s = json.load(open(os.path.join(HERE, "screen.json")))
for f in s["forms"]:
    if "the twenty-one, under this form" not in f:
        continue
    vals = [Fraction(x) for x in f["the twenty-one, under this form"]]
    ctl = [Fraction(x) for x in f["control, ten smallest positive weights held"]]
    if (sum(1 for v in vals if v < 0) != f["still negative"]
            or sum(1 for v in vals if v >= 0) != f["lifted"]
            or sum(1 for v in ctl if v < 0) != f["control gone negative"]):
        bad += 1
        print(f"COUNT MISMATCH {f['form']}")
print(f"recorded: {len(s['forms'])} forms, counts recomputed from the weight lists, "
      f"{bad} mismatches")


def simplex_edges_by_normaliz():
    """The edges of conv(0, e_1..e_6) as normal sets, from the polytope rather than by hand."""
    from PyNormaliz import Cone
    ineq = [[1 if k == i else 0 for k in range(D)] + [0] for i in range(D)]
    ineq.append([-1] * D + [1])
    C = Cone(inhom_inequalities=ineq)
    sup = C.SupportHyperplanes()
    verts = [tuple(Fraction(x, v[-1]) for x in v[:D]) for v in C.VerticesOfPolyhedron()]

    def tight(p):
        return [i for i, h in enumerate(sup)
                if sum(Fraction(h[j]) * p[j] for j in range(D)) + h[D] == 0]

    out = []
    for a in range(len(verts)):
        for b in range(a + 1, len(verts)):
            common = sorted(set(tight(verts[a])) & set(tight(verts[b])))
            if len(common) != D - 1:
                continue
            out.append(tuple(sorted(tuple(-x for x in sup[k][:D]) for k in common)))
    return out


edges = simplex_edges_by_normaliz()
ident_bad = 0
if len(edges) != 21:
    ident_bad += 1
    print(f"EDGE COUNT MISMATCH: {len(edges)} against 21")
forms = dict(named())
for name in ("standard", "I plus 1/4 off the diagonal"):
    tot = sum(transverse_weight_q(list(e), forms[name]) for e in edges)
    if tot != Fraction(49, 20):
        ident_bad += 1
        print(f"IDENTITY MISMATCH {name}: {tot}")
bad += ident_bad
print(f"the codimension-five identity on the six-simplex, edges taken from the polytope: "
      f"{len(edges)} edges, 2 forms, {ident_bad} mismatches")

ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
held = [json.loads(l) for l in open(ATLAS)]
rng = random.Random(20260913)
reg_bad = 0
for r in rng.sample(held[10:], 6):
    n = [tuple(v) for v in r["normals"]]
    if transverse_weight_q(n, forms["standard"]) != Fraction(r["weight"]):
        reg_bad += 1
        print(f"REGRESSION MISMATCH {n}")
bad += reg_bad
print(f"the module against recorded weights on a fresh sample: 6 classes, {reg_bad} mismatches")

CHECK4 = os.path.join(HERE, "..", "certified-special-case-check-4")
negs = json.load(open(os.path.join(CHECK4, "negative-classes.json")))["the negative classes"]
best = next(f for f in s["forms"] if f["form"] == "I plus 1/4 off the diagonal")
vals = [Fraction(x) for x in best["the twenty-one, under this form"]]
survivors = [negs[i] for i, v in enumerate(vals) if v < 0]
surv_bad = 0
for x in survivors:
    w = transverse_weight_q([tuple(v) for v in x["normals"]], forms["I plus 1/4 off the diagonal"])
    if w >= 0:
        surv_bad += 1
        print(f"SURVIVOR MISMATCH {x['normals']}: {w}")
bad += surv_bad
print(f"the {len(survivors)} classes surviving the best form, recomputed: {surv_bad} mismatches")
sys.exit(1 if bad else 0)
