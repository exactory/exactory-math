#!/bin/sh
set -eu
export PATH="<elan>/bin:$PATH"
export LEAN_NUM_THREADS=1
for module in Definitions Certificate8 Certificate9 Main; do
  nice -n 15 lake build "+$module"
done
nice -n 15 lake env lean -j1 -M2048 Audit.lean
