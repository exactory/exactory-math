#!/bin/bash
# Class E: primitive hives with few lattice points (c <= dim + 2) beyond the box, 5, 6 and 7 parts.
# Seeded random sampling; the filter keeps the few-point, large-volume shape that a negative
# linear coefficient by the empty-simplex mechanism needs.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
nice -n 19 "$PY" sample_search.py --parts 5 --smin 31 --smax 120 --dmin 3 --count 3000 --seed 20260907 --workers 3 --out e5 --cmax-excess 2 > e5.log 2>&1
nice -n 19 "$PY" sample_search.py --parts 6 --smin 31 --smax 80 --dmin 3 --count 2000 --seed 20260908 --workers 3 --out e6 --cmax-excess 2 > e6.log 2>&1
nice -n 19 "$PY" sample_search.py --parts 7 --smin 31 --smax 60 --dmin 3 --count 1000 --seed 20260909 --workers 3 --out e7 --cmax-excess 2 > e7.log 2>&1
echo done > DONE
