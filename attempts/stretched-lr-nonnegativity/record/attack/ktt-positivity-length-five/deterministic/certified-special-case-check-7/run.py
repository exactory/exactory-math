#!/usr/bin/env python3
"""The screen: do the twenty-one negative classes stay negative under another scalar product?

Approved with seven amendments by the fourth independent review of 2026-09-05. The order is the
one that review required: screen every named form on the twenty-one negative representatives and
on a positive control first, because a five-dimensional weight costs about a second, and leave the
expensive vertex-sum gate at dimension six for forms that lift all twenty-one.

Before any of that, two exact checks on the new module, which the vertex-sum gate of
enumeration-run-4 does not cover because it exercises full-dimensional tangent cones at
codimension six while this module builds codimension-five transverse cones:

  * under the standard form the module must reproduce recorded weights exactly;
  * the codimension-five identity on the unimodular six-simplex, whose Ehrhart polynomial is
    C(t+6,6), so the sum over its twenty-one edges of the transverse cone weight times the lattice
    length is H_6 = 49/20. Every edge of that simplex has lattice length one.

The second is run under every form and is the necessary validity test at the codimension that
matters. A lift under a form that has not passed the vertex-sum gate is not evidence, and the
record says so.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from forms import named  # noqa: E402
from transverse_q import transverse_weight_q  # noqa: E402

CHECK4 = os.path.join(HERE, "..", "certified-special-case-check-4")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
D = 6
H6 = Fraction(49, 20)


def simplex_edges():
    """The 21 edges of conv(0, e_1, ..., e_6), as their sets of outward facet normals.

    Facets: x_i >= 0 with outward normal -e_i, and sum x_i <= 1 with outward normal (1,...,1).
    """
    minus = [tuple(-1 if k == i else 0 for k in range(D)) for i in range(D)]
    top = tuple(1 for _ in range(D))
    out = []
    for i in range(D):                                   # the edge from 0 to e_i
        out.append(tuple(sorted(minus[j] for j in range(D) if j != i)))
    for i, j in itertools.combinations(range(D), 2):     # the edge from e_i to e_j
        out.append(tuple(sorted([minus[k] for k in range(D) if k not in (i, j)] + [top])))
    return out


def main():
    budget = float(os.environ.get("BUDGET", "1600"))
    t0 = time.time()
    negatives = json.load(open(os.path.join(CHECK4, "negative-classes.json")))["the negative classes"]
    held = []
    for line in open(ATLAS):
        r = json.loads(line)
        held.append((Fraction(r["weight"]), [tuple(v) for v in r["normals"]]))
    for line in open(os.path.join(RUN2, "weights.jsonl")):
        r = json.loads(line)
        held.append((Fraction(r["weight"]), [tuple(v) for v in r["normals"]]))
    control = [n for w, n in sorted((x for x in held if x[0] > 0), key=lambda x: x[0])[:10]]
    recorded = {tuple(sorted(n)): w for w, n in held}

    result = {"regression": {}, "forms": []}
    std = named()[0][1]

    # regression one: recorded weights reproduced under the standard form
    sample = [n for _, n in held[:6]] + [x["normals"] for x in negatives[:3]]
    bad = 0
    for n in sample:
        n = [tuple(v) for v in n]
        got = transverse_weight_q(n, std)
        want = recorded[tuple(sorted(n))]
        if got != want:
            bad += 1
            print(f"REGRESSION MISMATCH {n}: {got} against {want}", flush=True)
    result["regression"]["recorded weights reproduced under the standard form"] = \
        {"checked": len(sample), "mismatches": bad}
    print(json.dumps(result["regression"]), flush=True)

    edges = simplex_edges()
    for name, Q in named():
        if time.time() - t0 > budget:
            break
        rec = {"form": name}
        s = Fraction(0)
        for e in edges:
            s += transverse_weight_q(list(e), Q)
        rec["the codimension-five identity on the unimodular six-simplex"] = str(s)
        rec["identity holds"] = (s == H6)
        if not rec["identity holds"]:
            print(json.dumps(rec), flush=True)
            result["forms"].append(rec)
            continue
        neg = []
        for x in negatives:
            neg.append(str(transverse_weight_q([tuple(v) for v in x["normals"]], Q)))
        ctl = [str(transverse_weight_q(n, Q)) for n in control]
        rec["the twenty-one, under this form"] = neg
        rec["still negative"] = sum(1 for v in neg if Fraction(v) < 0)
        rec["lifted"] = sum(1 for v in neg if Fraction(v) >= 0)
        rec["control, ten smallest positive weights held"] = ctl
        rec["control gone negative"] = sum(1 for v in ctl if Fraction(v) < 0)
        rec["seconds so far"] = round(time.time() - t0)
        print(json.dumps(rec), flush=True)
        result["forms"].append(rec)
    result["seconds"] = round(time.time() - t0)
    result["note"] = ("a lift under a form that has not passed the vertex-sum gate of "
                      "enumeration-run-4 is not evidence; only the standard form and A_6 have "
                      "passed it")
    json.dump(result, open(os.path.join(HERE, "screen.json"), "w"), indent=2)


if __name__ == "__main__":
    main()
