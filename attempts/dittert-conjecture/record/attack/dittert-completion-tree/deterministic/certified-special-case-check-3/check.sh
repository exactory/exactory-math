#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 ../../../../.venv/bin/python -I -u ../../study/external-proof/n6-n7/verify_dittert_n6_n7.py --dimension 7 --json | tee n7-primary.json
nice -n 15 ../../../../.venv/bin/python -I -u audit_n7_only.py | tee n7-independent.txt
