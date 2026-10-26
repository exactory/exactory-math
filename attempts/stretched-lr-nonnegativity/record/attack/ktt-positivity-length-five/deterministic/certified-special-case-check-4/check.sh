#!/bin/sh
# Independent check: the summary against the records, the negative classes recomputed from the
# two weight files by canonical form, the reduction's premise against the steps that built the
# cells, and the Ehrhart value at the ray sum of the cells that carry a negative class.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
