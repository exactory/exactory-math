#!/bin/sh
# Independent check: the summary recomputed from the records, the identity recomputed with no
# cache on sampled contracted polytopes, the contraction checks, and the move-18 table.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
