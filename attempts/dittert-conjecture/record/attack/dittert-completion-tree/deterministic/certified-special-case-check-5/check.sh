#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
nice -n 15 ../../../../.venv/bin/python -I test_exit_gate.py 2>&1 | tee after-fix.txt
