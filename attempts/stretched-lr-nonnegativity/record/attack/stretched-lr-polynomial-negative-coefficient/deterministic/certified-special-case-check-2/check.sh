#!/bin/sh
# Checker: the lrcalc pinning (t = 0..10) covered every 6-part polynomial with 0 mismatches,
# and a third implementation (lattice-word counter + Lagrange) agrees on a sample.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py
