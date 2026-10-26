#!/bin/sh
# Independent check: the rank modulo a prime by a separate elimination, the counts from the raw
# data, and explicit isometry witnesses for the merged classes.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
exec "$PY" check.py
