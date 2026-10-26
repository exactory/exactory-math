#!/bin/sh
# Independent check: every recorded 5-part polynomial pinned by lrcalc (t = 0..6), a third
# implementation on a sample, counts and filters re-verified.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
