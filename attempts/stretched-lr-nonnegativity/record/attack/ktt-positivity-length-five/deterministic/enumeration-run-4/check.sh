#!/bin/sh
# Independent check: the recorded sums, the same identity on a second non-unimodular simplex the
# run did not use, the scale invariance the classification argument rests on, and the closed value
# of a signed orthant under the standard form.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
