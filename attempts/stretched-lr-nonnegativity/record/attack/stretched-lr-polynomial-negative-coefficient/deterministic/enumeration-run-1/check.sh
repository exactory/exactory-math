#!/bin/sh
# Independent check of the scan records: classical lattice-word counts vs the recorded polynomials.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py scan-maxpart10.jsonl,scan-maxpart30.jsonl 5
