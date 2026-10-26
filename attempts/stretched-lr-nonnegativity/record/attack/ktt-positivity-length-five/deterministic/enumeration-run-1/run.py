#!/usr/bin/env python3
"""The Berline-Vergne weight on the rank-five codimension-five atlas: are any negative?

The linear coefficient of a full-dimensional five-part hive polytope is, by the local formula,
the sum over its edges of the lattice length of the edge times the weight of the edge's transverse
cone. The edges of 2,000 such polytopes fall into 3,406 isometry classes
(`symbolic-computation-run-1`). This run computes the weight of every class, by converting the
class to its transverse cone in the projected lattice (`transverse.py`) and applying the defining
recursion (`bvweight.py`, validated in `certified-special-case-check-2`), and records the values
and their signs. A negative weight is printed at once.

Output: `atlas.jsonl` (one record per class: the canonical normal set, the number of rays of the
transverse cone, the weight, the time) and `atlas.summary.json`.
"""
import json
import os
import sys
import time
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from transverse import transverse_cone, transverse_weight  # noqa: E402

SYS1 = os.path.join(HERE, "..", "symbolic-computation-run-1")


def main():
    classes = json.load(open(os.path.join(SYS1, "classes.json")))["canonical"]
    start = 0
    out_path = os.path.join(HERE, "atlas.jsonl")
    if os.path.exists(out_path):
        with open(out_path) as f:
            start = sum(1 for _ in f)
    t0 = time.time()
    neg = 0
    mn = None
    with open(out_path, "a") as f:
        for i in range(start, len(classes)):
            normals = [list(map(int, v)) for v in classes[i]]
            t1 = time.time()
            rays, gram = transverse_cone(normals)
            w = transverse_weight(normals)
            rec = {"class": i, "normals": normals, "rays": len(rays), "dim": len(gram),
                   "weight": str(w), "seconds": round(time.time() - t1, 2)}
            f.write(json.dumps(rec) + "\n")
            f.flush()
            if w < 0:
                neg += 1
                print("NEGATIVE", json.dumps(rec), flush=True)
            if mn is None or w < mn:
                mn = w
            if (i + 1) % 25 == 0:
                print(f"{i + 1} of {len(classes)} classes, {neg} negative, minimum {mn}, "
                      f"{time.time() - t0:.0f}s", flush=True)
    recs = [json.loads(l) for l in open(out_path)]
    ws = [Fraction(r["weight"]) for r in recs]
    summary = {"classes": len(recs), "negative": sum(1 for w in ws if w < 0),
               "minimum": str(min(ws)), "maximum": str(max(ws)),
               "simplicial": sum(1 for r in recs if r["rays"] == r["dim"]),
               "seconds": round(time.time() - t0, 1)}
    json.dump(summary, open(os.path.join(HERE, "atlas.summary.json"), "w"), indent=1)
    print("done", json.dumps(summary), flush=True)


if __name__ == "__main__":
    main()
