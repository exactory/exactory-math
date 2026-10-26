#!/bin/sh
# Independent check: every recorded few-point polynomial recomputed from the tableau-polytope
# encoding, checked by lrcalc (and pinned when small), a third implementation on a sample,
# counts and filters re-verified, largest empty-simplex volume reported.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
