#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 ../../../../.venv/bin/python -I -u ../../study/external-proof/unified/verify_unified_reductions.py | tee primary-output.txt
nice -n 15 ../../../../.venv/bin/python -I -u independent_check.py | tee independent-output.txt
