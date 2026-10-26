#!/bin/sh
# Independent check: the summary against the atlas file, the orthogonally splitting classes
# against the products of the published closed formulas, and the end-to-end local-formula
# identity against the certified linear coefficients of hive polytopes.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
