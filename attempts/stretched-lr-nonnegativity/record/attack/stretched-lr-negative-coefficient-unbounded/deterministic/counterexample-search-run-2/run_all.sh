#!/bin/bash
# Runs the transportation-polytope families listed in input.json, one after another.
cd "$(dirname "$0")"
PY=<workspace>/stretched-lr-negative-coefficient/.venv/bin/python
export OMP_NUM_THREADS=1
for spec in "3 4 16" "3 5 14" "4 4 14" "3 6 12" "4 5 11" "5 5 9"; do
  set -- $spec
  nice -n 5 "$PY" transport.py --k $1 --N $2 --total-max $3 --workers 4 --out t${1}x${2} > t${1}x${2}.log 2>&1
done
echo finished > DONE
