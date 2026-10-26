#!/bin/sh
# Independent check: the summary against the record files, an independent h computed by solving
# the triangular system instead of the alternating sum, and a positive control that the detector
# fires on a synthetic polynomial with a negative entry.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
