#!/usr/bin/env python3
"""Independent check of the sharper residue.

1. The summary against `classified.jsonl`, every field recomputed.
2. The list of negative classes recomputed from the weight files of `enumeration-run-1` and
   `enumeration-run-2`, by canonical form, together with the check that no class carries two
   different weights across the two files.
3. The premise of the reduction, on the records themselves: every cell classified as carrying no
   edge of a negative-weight class must have a nonnegative value at every extreme ray in the step
   that built it, and every cell that does carry one must have its recorded ray values equal to
   the positive part minus the negative part this run recorded at the worst ray.
4. The functional at a point neither this run nor the sweep evaluated: for the cells with the
   smallest ray sums among those carrying a negative class, the linear coefficient from the
   Ehrhart quasi-polynomial must equal the sum of the ray values recorded by the step that built
   the cell.
Exit 0 iff all four hold.
"""
import json
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chamber import a1_of, unpack  # noqa: E402
from isotypes import canonical  # noqa: E402

N = 5
bad = 0
recs = [json.loads(l) for l in open(os.path.join(HERE, "classified.jsonl"))]
summary = json.load(open(os.path.join(HERE, "classified.summary.json")))
with_neg = [r for r in recs if r["negative edges"]]
recomputed = {
    "cells classified": len(recs),
    "cells carrying an edge of a negative-weight class": len(with_neg),
    "cells the reduction settles with no computation": len(recs) - len(with_neg),
    "edges examined": sum(r["edges"] for r in recs),
    "edges of a negative-weight class": sum(r["negative edges"] for r in recs),
}
for k, v in recomputed.items():
    if summary[k] != v:
        bad += 1
        print(f"SUMMARY MISMATCH {k}: summary {summary[k]}, recomputed {v}")
print(f"summary: {len(recs)} cells, {len(with_neg)} carry an edge of a negative-weight class, "
      f"{recomputed['edges examined']} edges of which "
      f"{recomputed['edges of a negative-weight class']} are of such a class")

seen = {}
conflicts = 0
for f in (os.path.join(HERE, "..", "enumeration-run-1", "atlas.jsonl"),
          os.path.join(HERE, "..", "enumeration-run-2", "weights.jsonl")):
    for line in open(f):
        r = json.loads(line)
        k = canonical([tuple(v) for v in r["normals"]])
        w = Fraction(r["weight"])
        if k in seen and seen[k] != w:
            conflicts += 1
            print(f"WEIGHT CONFLICT for one class: {seen[k]} and {w}")
        seen[k] = w
neg = {k: w for k, w in seen.items() if w < 0}
if len(seen) != summary["classes held"] or len(neg) != summary["negative classes"] \
        or str(min(neg.values())) != summary["most negative class weight"]:
    bad += 1
    print(f"CLASS MISMATCH: {len(seen)} held and {len(neg)} negative against the summary")
bad += conflicts
print(f"weights: {len(seen)} distinct classes, {len(neg)} negative, {conflicts} conflicts between "
      f"the two files, most negative {min(neg.values())}")

built = {}
for path, tag in ((os.path.join(HERE, "..", "certified-special-case-check-3", "cells.jsonl"),
                   "certified-special-case-check-3"),
                  (os.path.join(HERE, "..", "enumeration-run-2", "cells.jsonl"),
                   "enumeration-run-2")):
    for line in open(path):
        c = json.loads(line)
        built.setdefault((tag, tuple(tuple(x) for x in c["triple"])), c)
premise_bad = premise_checked = 0
for r in recs:
    c = built.get((r["source"], tuple(tuple(x) for x in r["triple"])))
    if c is None:
        continue
    premise_checked += 1
    vals = [Fraction(x) for x in c["ell"]]
    if not r["negative edges"] and min(vals) < 0:
        premise_bad += 1
        print(f"PREMISE BROKEN {r['triple']}: no negative-weight edge but a negative ray value")
    if r["negative edges"] and "worst ray positive part" in r:
        if Fraction(r["worst ray positive part"]) - Fraction(r["worst ray negative part"]) \
                not in vals:
            premise_bad += 1
            print(f"SPLIT MISMATCH {r['triple']}: the worst ray split is not a recorded value")
bad += premise_bad
print(f"the reduction's premise: {premise_checked} cells matched to the step that built them, "
      f"{premise_bad} failures")

points = sorted(((r, built.get((r["source"], tuple(tuple(x) for x in r["triple"])))) for r in with_neg),
                key=lambda p: sum(sum(x[i] for x in p[1]["ray_list"]) for i in range(N))
                if p[1] else 10 ** 9)
ehr_checked = ehr_bad = 0
for r, c in points[:8]:
    if c is None:
        continue
    bs = [sum(x[i] for x in c["ray_list"]) for i in range(3 * N)]
    if sum(unpack(bs, N)[0]) > 500:
        continue
    want = sum(Fraction(x) for x in c["ell"])
    got = a1_of(list(bs), N)
    ehr_checked += 1
    if got != want:
        ehr_bad += 1
        print(f"EHRHART MISMATCH at the ray sum of {r['triple']}: {got} against {want}")
bad += ehr_bad
print(f"cells carrying a negative class, at the sum of their rays, by the Ehrhart "
      f"quasi-polynomial: {ehr_checked} checked, {ehr_bad} mismatches")
sys.exit(1 if bad else 0)
