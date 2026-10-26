#!/bin/sh
# Independent checks of the exhaustive 7-part scan: completeness recount for every size 7..30 and
# classical lattice-word recounts of the extreme and random records.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py 7 scan-n7 30 4
