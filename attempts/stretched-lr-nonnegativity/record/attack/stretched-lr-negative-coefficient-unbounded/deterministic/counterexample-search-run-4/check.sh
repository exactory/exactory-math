#!/bin/sh
# Independent check: every hit re-verified from the definition, lrcalc at t = 1 on every 8-part record, the tableau-polytope encoding on a sample, a third
# implementation on a sample, counts and filters re-verified.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
