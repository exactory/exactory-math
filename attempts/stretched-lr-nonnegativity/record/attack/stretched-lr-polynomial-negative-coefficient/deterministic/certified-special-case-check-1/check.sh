#!/bin/sh
# Checker: the lrcalc pinning covered every 5-part polynomial with 0 mismatches, and a third
# implementation (lattice-word counter + Lagrange interpolation) agrees on a sample.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py
