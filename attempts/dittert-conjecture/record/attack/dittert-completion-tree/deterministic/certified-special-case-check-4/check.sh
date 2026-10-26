#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
proof_root=$(cd ../../../.. && pwd)
library_root="$proof_root/attack/dittert-conjecture-n5-to-n15/deterministic/formal-check-1"
proof_lean_path="$library_root/.lake/build/lib/lean"
for package_library in "$library_root"/.lake/packages/*/.lake/build/lib/lean; do
  proof_lean_path="$proof_lean_path:$package_library"
done
export LEAN_PATH="$proof_lean_path"
nice -n 15 <elan>/bin/lean -j 1 Main.lean | tee lean-output.txt
rg -F "DittertScalar.positive_quadratic' depends on axioms: [propext, Classical.choice, Quot.sound]" lean-output.txt
rg -F "DittertScalar.exclusion' depends on axioms: [propext, Classical.choice, Quot.sound]" lean-output.txt
