#!/bin/sh
set -e
OMP_NUM_THREADS=1 exec ../../../../.venv/bin/python check.py
