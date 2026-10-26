#!/bin/sh
# Checker: the tableau-polytope encoding and lrcalc agreed with every 7-part polynomial
# (verify7.summary.json), the second encoding is re-run here on a sample, and a third
# implementation (lattice-word counter) agrees on a sample at t = 0..3.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
