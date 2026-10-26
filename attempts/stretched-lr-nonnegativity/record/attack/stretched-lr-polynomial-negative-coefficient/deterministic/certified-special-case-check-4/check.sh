#!/bin/sh
# Second implementation of the census (Stirling-number simplex coefficients, series h*):
# rebuilds every aggregate and the below-1 histogram from the raw records and compares.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py
