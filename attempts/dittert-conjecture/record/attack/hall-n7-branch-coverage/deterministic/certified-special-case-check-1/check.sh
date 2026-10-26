#!/bin/sh
set -eu
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
cd "$(dirname "$0")"
nice -n 15 <workspace>/dittert-conjecture/.venv/bin/python -B generate_manifest.py
nice -n 15 <workspace>/dittert-conjecture/.venv/bin/python -B check_manifest.py
