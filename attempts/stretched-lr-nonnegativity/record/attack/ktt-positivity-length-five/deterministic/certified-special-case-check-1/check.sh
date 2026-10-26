#!/bin/sh
# Independent check: the summary against the files, the right-hand sides against the certified
# records of the box attack, the edges against Normaliz's face lattice with its own volumes,
# and the weight formula against its self-test.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
