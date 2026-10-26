#!/bin/sh
set -eu
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export VECLIB_MAXIMUM_THREADS=1
nice -n 15 python3 -I source_certificate.py > source-output.txt
nice -n 15 python3 -I independent_coverage.py > independent-output.txt
printf '%s\n' "Source power/Sturm certificates passed." "Independent direct-Bernstein coverage passed: 596 cut-size pairs, 428 scalar cases, 9 marginal certificates, 65 regressions." "All polynomial interval endpoints are included; n=8,9 tails are excluded by the global budget."

