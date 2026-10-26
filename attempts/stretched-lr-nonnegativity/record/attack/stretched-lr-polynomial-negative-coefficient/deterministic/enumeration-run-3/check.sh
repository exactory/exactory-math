#!/bin/sh
# Independent checks of the exhaustive 6-part scan: completeness recount for sizes <= 14 and
# classical lattice-word recounts of the extreme and random records.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py 6 scan-n6 30 4
