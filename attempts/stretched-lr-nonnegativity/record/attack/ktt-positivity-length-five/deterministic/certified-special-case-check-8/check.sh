#!/bin/sh
# Independent check: the summary recomputed from the records, the row counts against the steps
# that built the cells, and, on sampled cells, the lengths recomputed from the polytope.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
