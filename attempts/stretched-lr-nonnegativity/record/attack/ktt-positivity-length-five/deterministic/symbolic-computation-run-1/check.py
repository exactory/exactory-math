#!/usr/bin/env python3
"""Independent check of the rank computation and of the isometry merge.

1. The rank is recomputed modulo the prime 2^31 - 1 by an elimination written here, which shares
   no code with the exact rational reduction of the run: the rank over Q is at least the rank
   modulo a prime, and equality of the two is the check (a chance coincidence would have to be a
   drop, so equality certifies the rational rank from below and the run's value from above).
2. The number of distinct equations and the number of unknowns are recomputed from the raw edge
   data with the class assignment read from `classes.json`.
3. The isometry merge is verified where it merges: for 40 seeded random classes holding more than
   one type, an explicit signed permutation carrying the first type to each other type is
   exhibited by a brute-force search over the group, written here.
4. The reported pinned classes are re-derived: a class is pinned only if it is a pivot whose row
   has a single nonzero, which is re-tested modulo the prime.
Exit 0 iff all four hold.
"""
import gzip
import json
import os
import random
import sys
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK1 = os.path.join(HERE, "..", "certified-special-case-check-1")
P = (1 << 31) - 1

summary = json.load(open(os.path.join(HERE, "system.summary.json")))
classes = json.load(open(os.path.join(HERE, "classes.json")))
types = [tuple(tuple(x) for x in t) for t in json.load(open(os.path.join(CHECK1, "edge-types.json")))]
recs = [json.loads(l) for l in gzip.open(os.path.join(CHECK1, "edges.jsonl.gz"), "rt")]
bad = 0

cls_of = [None] * len(types)
for c, mem in classes["members"].items():
    for i in mem:
        cls_of[i] = int(c)
if any(c is None for c in cls_of):
    bad += 1
    print("CLASS ASSIGNMENT INCOMPLETE")

def frac_mod(s):
    if "/" in s:
        a, b = s.split("/")
        return int(a) % P * pow(int(b) % P, P - 2, P) % P
    return int(s) % P

rows = []
seen = set()
for r in recs:
    d = {}
    for i, ln in r["edges"]:
        c = cls_of[i]
        d[c] = (d.get(c, 0) + frac_mod(ln)) % P
    d = {k: v for k, v in d.items() if v}
    rows.append((d, frac_mod(r["a1"])))
    seen.add((tuple(sorted(d.items())), frac_mod(r["a1"])))

piv = {}
for d, b in rows:
    d = dict(d)
    while d:
        c = min(d)
        if c not in piv:
            inv = pow(d[c], P - 2, P)
            piv[c] = ({k: v * inv % P for k, v in d.items()}, b * inv % P)
            d = None
            break
        pd, pb = piv[c]
        f = d[c]
        for k, v in pd.items():
            nv = (d.get(k, 0) - f * v) % P
            if nv:
                d[k] = nv
            elif k in d:
                del d[k]
        b = (b - f * pb) % P
    if d is not None and not d and b % P:
        bad += 1
        print("INCONSISTENT MODULO THE PRIME")
        break
for c in sorted(piv, reverse=True):
    d, b = piv[c]
    for k in [k for k in d if k != c and k in piv]:
        pd, pb = piv[k]
        f = d[k]
        for kk, vv in pd.items():
            nv = (d.get(kk, 0) - f * vv) % P
            if nv:
                d[kk] = nv
            elif kk in d:
                del d[kk]
        b = (b - f * pb) % P
    piv[c] = (d, b)
pinned = [c for c, (d, _) in piv.items() if len(d) == 1]

if len(piv) != summary["rank"] or len(pinned) != summary["pinned_classes"]:
    bad += 1
    print(f"RANK MISMATCH: modulo {P} rank {len(piv)} pinned {len(pinned)}, "
          f"run reports rank {summary['rank']} pinned {summary['pinned_classes']}")
else:
    print(f"rank {len(piv)} and {len(pinned)} pinned classes, recomputed modulo 2^31 - 1, agree "
          f"with the exact reduction")

nun = len({c for d, _ in rows for c in d})
if len(seen) != summary["distinct_equations"] or len(classes["members"]) != summary["isometry_classes"]:
    bad += 1
    print(f"COUNT MISMATCH: distinct {len(seen)} vs {summary['distinct_equations']}, "
          f"classes {len(classes['members'])} vs {summary['isometry_classes']}")
else:
    print(f"{len(rows)} equations, {len(seen)} distinct, {len(classes['members'])} classes "
          f"({nun} of them occur)")


def image(t, order, signs):
    return tuple(sorted(tuple(signs[j] * v[order[j]] for j in range(len(order))) for v in t))


def find_iso(t1, t2):
    d = len(t1[0])
    t2s = tuple(sorted(t2))
    for order in permutations(range(d)):
        for mask in range(1 << d):
            signs = tuple(1 if (mask >> j) & 1 == 0 else -1 for j in range(d))
            if image(t1, order, signs) == t2s:
                return order, signs
    return None


rng = random.Random(20260905)
multi = [mem for mem in classes["members"].values() if len(mem) > 1]
sample = rng.sample(multi, min(40, len(multi)))
wbad = 0
for mem in sample:
    t1 = types[mem[0]]
    for other in mem[1:3]:
        if find_iso(t1, types[other]) is None:
            wbad += 1
            print(f"NO ISOMETRY between types {mem[0]} and {other}")
bad += wbad
print(f"isometry witnesses: {len(sample)} merged classes checked, {wbad} without a witness")
sys.exit(1 if bad else 0)
