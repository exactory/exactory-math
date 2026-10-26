#!/bin/sh
# Independent check: the recorded counts recomputed from the weight lists; the codimension-five
# identity on the six-simplex with its edges taken from the polytope rather than by hand; the
# module against recorded weights on a fresh sample; and the classes that survive the best form.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
