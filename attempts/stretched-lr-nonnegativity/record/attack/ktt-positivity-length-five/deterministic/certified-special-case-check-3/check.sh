#!/bin/sh
# Independent check: the summary against the cell records, the certified linear coefficients
# against certified-special-case-check-1, the extreme rays as triples of partitions, and the
# functional at sampled cells recomputed by the depth-first hive enumerator instead of Normaliz.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
