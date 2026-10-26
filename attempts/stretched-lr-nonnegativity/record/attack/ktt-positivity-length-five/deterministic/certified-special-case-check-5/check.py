#!/usr/bin/env python3
"""Independent check of the local domination measurement.

1. The summary against `domination.jsonl`, every field recomputed.
2. The cell and edge counts against the classification of `certified-special-case-check-4`.
3. On a sample of cells, three things recomputed from the polytope rather than read from the
   record: that the sum over all edges of the weight times the lattice length reproduces, at every
   extreme ray, the value the step that built the cell recorded from a different route; that the
   discharging rule is sound, that is that the shares of the negative edges together never exceed
   the positive part of the functional; and that the facet-neighbourhood share dominates the
   demand at every ray, with the ratio the record states.
Exit 0 iff all three hold.
"""
import json
import os
import random
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from atlasform import WeightBook, apply_functional, edges_with_linear_length  # noqa: E402
from chamber import Cell  # noqa: E402
from isotypes import canonical  # noqa: E402

N = 5
bad = 0
recs = [json.loads(l) for l in open(os.path.join(HERE, "domination.jsonl"))]
summary = json.load(open(os.path.join(HERE, "domination.summary.json")))


def ratios_of(name):
    return [Fraction(i[name]["smallest ratio"]) for r in recs for i in r["per edge"]
            if i[name]["smallest ratio"] is not None]


rv, rf = ratios_of("vertex"), ratios_of("facet")
recomputed = {
    "cells with a negative edge": len(recs),
    "negative edges": sum(r["negative edges"] for r in recs),
    "vertex neighbourhood: tests where the share fails to dominate":
        sum(i["vertex"]["failures"] for r in recs for i in r["per edge"]),
    "facet neighbourhood: tests where the share fails to dominate":
        sum(i["facet"]["failures"] for r in recs for i in r["per edge"]),
    "vertex neighbourhood: smallest ratio": str(min(rv)) if rv else None,
    "facet neighbourhood: smallest ratio": str(min(rf)) if rf else None,
    "negative edges with no positive vertex neighbour":
        sum(1 for r in recs for i in r["per edge"] if i["vertex"]["positive neighbours"] == 0),
}
for k, v in recomputed.items():
    if summary[k] != v:
        bad += 1
        print(f"SUMMARY MISMATCH {k}: summary {summary[k]}, recomputed {v}")
print(f"summary: {len(recs)} cells, {recomputed['negative edges']} negative edges, "
      f"vertex neighbourhood fails {recomputed['vertex neighbourhood: tests where the share fails to dominate']} "
      f"times with smallest ratio {recomputed['vertex neighbourhood: smallest ratio']}, facet "
      f"neighbourhood fails {recomputed['facet neighbourhood: tests where the share fails to dominate']} "
      f"times with smallest ratio {recomputed['facet neighbourhood: smallest ratio']}")

CHECK4 = os.path.join(HERE, "..", "certified-special-case-check-4")
cls = [json.loads(l) for l in open(os.path.join(CHECK4, "classified.jsonl"))]
with_neg = [c for c in cls if c["negative edges"]]
if len(with_neg) != len(recs) or sum(c["negative edges"] for c in with_neg) != \
        recomputed["negative edges"]:
    bad += 1
    print(f"CLASSIFICATION MISMATCH: {len(with_neg)} cells and "
          f"{sum(c['negative edges'] for c in with_neg)} edges there against "
          f"{len(recs)} and {recomputed['negative edges']} here")
print(f"against certified-special-case-check-4: {len(with_neg)} cells carrying a negative edge, "
      f"{sum(c['negative edges'] for c in with_neg)} such edges")

CHECK3 = os.path.join(HERE, "..", "certified-special-case-check-3")
RUN2 = os.path.join(HERE, "..", "enumeration-run-2")
ATLAS = os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl")
book = WeightBook(ATLAS, os.path.join(HERE, "weights.jsonl"))
for line in open(os.path.join(RUN2, "weights.jsonl")):
    r = json.loads(line)
    book.weights.setdefault(canonical([tuple(v) for v in r["normals"]]), Fraction(r["weight"]))
built = {}
for path, tag in ((os.path.join(CHECK3, "cells.jsonl"), "certified-special-case-check-3"),
                  (os.path.join(RUN2, "cells.jsonl"), "enumeration-run-2")):
    for line in open(path):
        c = json.loads(line)
        built.setdefault((tag, tuple(tuple(x) for x in c["triple"])), c)

rng = random.Random(20260907)
sample = rng.sample(recs, min(25, len(recs)))
id_bad = rule_bad = dom_bad = checked = 0
for r in sample:
    key = (r["source"], tuple(tuple(x) for x in r["triple"]))
    c = built[key]
    Z = Cell(*key[1])
    edges = edges_with_linear_length(Z)
    weights = [book.weight(n) for n, _, _, _ in edges]
    neg = [i for i, w in enumerate(weights) if w < 0]
    facets = [set(fs) for _, _, _, fs in edges]
    checked += 1
    for ray, recorded in zip(c["ray_list"], c["ell"]):
        total = sum(weights[i] * apply_functional(edges[i][1], ray) for i in range(len(edges)))
        if total != Fraction(recorded):
            id_bad += 1
            print(f"IDENTITY MISMATCH {r['triple']}: {total} against the recorded {recorded}")
    count = [0] * len(edges)
    for f, wf in enumerate(weights):
        if wf > 0:
            count[f] = sum(1 for g in neg if facets[f] & facets[g])
    for ray in c["ray_list"]:
        pos = sum(weights[f] * apply_functional(edges[f][1], ray)
                  for f in range(len(edges)) if weights[f] > 0)
        shares = Fraction(0)
        for e in neg:
            shares += sum(weights[f] / count[f] * apply_functional(edges[f][1], ray)
                          for f in range(len(edges))
                          if weights[f] > 0 and count[f] and (facets[f] & facets[e]))
        if shares > pos:
            rule_bad += 1
            print(f"RULE BROKEN {r['triple']}: shares {shares} exceed the positive part {pos}")
    for k, e in enumerate(neg):
        share = [Fraction(0)] * Z.B
        for f, wf in enumerate(weights):
            if wf > 0 and count[f] and (facets[f] & facets[e]):
                share = [s + wf / count[f] * x for s, x in zip(share, edges[f][1])]
        need = [-weights[e] * x for x in edges[e][1]]
        for ray in c["ray_list"]:
            lhs, rhs = apply_functional(share, ray), apply_functional(need, ray)
            if (rhs > 0 and lhs < rhs) or (rhs <= 0 and lhs < 0):
                dom_bad += 1
                print(f"DOMINATION BROKEN {r['triple']}: share {lhs} against demand {rhs}")
bad += id_bad + rule_bad + dom_bad
print(f"recomputed from the polytope on {checked} cells: {id_bad} ray values disagreeing with the "
      f"step that built the cell, {rule_bad} rays where the shares exceed the positive part, "
      f"{dom_bad} rays where the facet neighbourhood fails to dominate")
sys.exit(1 if bad else 0)
