#!/bin/sh
# Independent check: the summary against the records, the counts against
# certified-special-case-check-4, and, on a sample of cells recomputed from the polytope, the
# local-formula identity at every ray, the soundness of the discharging rule, and the domination.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
