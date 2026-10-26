#!/bin/bash
# Class E, small-third-partition corner: primitive hives beyond the box with few lattice points
# (c <= dim + 2) whose smaller partition nu has |nu| <= 8, at 5, 6 and 7 parts. The box's
# volume-2 empty simplices all have a small nu such as (2,2,1); uniform sampling of |nu| in
# [|lam|/4, 3|lam|/4] (run 5) never reaches that corner at sizes above 30.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
nice -n 19 "$PY" sample_search.py --parts 5 --smin 31 --smax 120 --dmin 3 --count 3000 --seed 20260910 --workers 3 --out f5 --cmax-excess 2 --nu-max 8 > f5.log 2>&1
nice -n 19 "$PY" sample_search.py --parts 6 --smin 31 --smax 80 --dmin 3 --count 2000 --seed 20260911 --workers 3 --out f6 --cmax-excess 2 --nu-max 8 > f6.log 2>&1
nice -n 19 "$PY" sample_search.py --parts 7 --smin 31 --smax 60 --dmin 3 --count 1000 --seed 20260912 --workers 3 --out f7 --cmax-excess 2 --nu-max 8 > f7.log 2>&1
echo done > DONE
