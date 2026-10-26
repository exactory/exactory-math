#!/bin/sh
# Independent check: the closed formulas of Castillo-Liu in dimensions two and three, the
# vertex-weight sum of the unit square, the valuation property on a non-unimodular cone, and
# multiplicativity over orthogonal sums, all rewritten in the checker.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py
