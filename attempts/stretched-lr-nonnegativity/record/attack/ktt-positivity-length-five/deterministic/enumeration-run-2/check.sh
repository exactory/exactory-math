#!/bin/sh
# Independent check: the summary against the cell records, the extreme rays as triples of
# partitions, and the functional at the sum of each cell's rays recomputed from the Ehrhart
# quasi-polynomial and, for the smallest cells, from the depth-first hive enumerator.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
