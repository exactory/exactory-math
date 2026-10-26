#!/usr/bin/env python3
"""Fresh scoped run of the independently implemented pinned source certificate."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import runpy

root = Path(__file__).resolve().parents[3]
source = root/"dittert-completion-tree/study/external-proof/unified/verify_unified_reductions.py"
namespace = runpy.run_path(str(source))
need = namespace["require"]
namespace["verify_subset_deficit_constants"]()
namespace["verify_quadratic_remainder_family"]()
count, worst = namespace["verify_cut_table"]()
need(count == 51, "source low-dimensional cut count")
expected = {8: (7,0), 9: (8,0), 10: (9,0)}
for n, (_,a,b) in worst.items():
    need((a,b) == expected[n], "source worst cut")
high_count = 0
for n in range(11,16):
    for a,b in namespace["cut_rows"](n):
        high_count += 1
        need(namespace["bernoulli_margin"](n,a,b)>0, "source high dimension gap")
supports = namespace["verify_residual_marginals"]()
need(set(supports) == {f"n8z{z}" for z in range(1,7)} | {"n9z7"},
     "source marginal support family")
print(json.dumps({"source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
                  "low_dimension_cut_rows":count,"high_dimension_cut_rows":high_count,
                  "support_certificates":sorted(supports)},indent=2))
print("PINNED SOURCE COVERAGE CERTIFIED")

