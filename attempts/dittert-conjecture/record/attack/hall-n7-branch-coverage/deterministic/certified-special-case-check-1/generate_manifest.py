#!/usr/bin/env python3
"""Emit every exact terminal rectangle from the pinned primary n=7 code."""
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parents[2] / "dittert-completion-tree/study/external-proof/n6-n7/verify_dittert_n6_n7.py"
spec = importlib.util.spec_from_file_location("pinned_primary", SOURCE)
primary = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = primary
spec.loader.exec_module(primary)


def cut_class(a, b):
    if a == b == 0:
        return "full"
    if min(a, b) == 0:
        return "marginal"
    if 7 - a - b >= 2:
        return "ordinary"
    return "single-bridge"


def emit_tree(a, b):
    tensors = tuple(primary.power_to_bernstein(primary.rescale_from_zero(p, (Fraction(3, 20),) * 2))
                    for p in primary.build_n7_single_bridge_polynomials(a, b))
    queue = [("", tensors, ((Fraction(0), Fraction(3, 20)),) * 2)]
    leaves = []
    while queue:
        path, ts, box = queue.pop()
        minima = [min(t.data) for t in ts]
        branch = "direct" if minima[0] > 0 else "entropy" if minima[1] > 0 and minima[2] > 0 else None
        if branch:
            leaves.append({"path": path, "box": [[str(l), str(r)] for l, r in box],
                           "branch": branch, "minima": [str(v) for v in minima]})
            continue
        if len(path) >= 12:
            raise RuntimeError("Unresolved source branch: " + path)
        axis = len(path) % 2
        pairs = [primary.split_tensor_half(t, axis) for t in ts]
        lo, hi = box[axis]
        mid = (lo + hi) / 2
        for child in (0, 1):
            child_box = list(box)
            child_box[axis] = (lo, mid) if child == 0 else (mid, hi)
            queue.append((path + str(child), tuple(p[child] for p in pairs), tuple(child_box)))
    return sorted(leaves, key=lambda x: x["path"])


def main():
    output = {"source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              "primary_scalar_and_tree_run": primary.verify_n7(),
              "cut_types": {f"{a},{b}": cut_class(a, b) for a in range(7) for b in range(7-a)},
              "trees": {f"{a},{6-a}": emit_tree(a, 6-a) for a in range(1, 4)}}
    (HERE / "manifest.json").write_text(json.dumps(output, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"generated": {k: len(v) for k, v in output["trees"].items()},
                      "cut_types": len(output["cut_types"]), "source_sha256": output["source_sha256"]}))


if __name__ == "__main__":
    main()
