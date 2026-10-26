#!/bin/sh
# Independent check: contingency-table counts from the definition against the recorded
# Ehrhart polynomials on a sample of every family, plus record counts.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py
