#!/bin/sh
# Independent check: both summaries against their records, the band table's old rows recomputed,
# the per-facet inequality recomputed from the polytope on sampled new cells, and the mechanism
# medians regrouped from per-facet.jsonl.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
exec "$PY" check.py
