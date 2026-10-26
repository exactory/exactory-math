#!/bin/sh
# Independent checks of the exhaustive 5-part scan: completeness recount for sizes <= 18 and
# classical lattice-word recounts of the extreme and random records.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py 30 5
