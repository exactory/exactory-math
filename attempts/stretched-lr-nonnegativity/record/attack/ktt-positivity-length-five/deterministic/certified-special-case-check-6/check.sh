#!/bin/sh
# Independent check: the summary against the records, the counts against the steps that built the
# cells and against certified-special-case-check-4, and, on sampled cells recomputed from the
# polytope, that the facet shares add up to the functional and that every facet pays for its own
# negative edges.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
