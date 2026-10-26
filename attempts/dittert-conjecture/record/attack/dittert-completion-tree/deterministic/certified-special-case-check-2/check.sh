#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
nice -n 15 ../../../../.venv/bin/python -I -u ../../study/external-proof/n8/verify_dittert_n8.py | tee n8-primary.txt
nice -n 15 ../../../../.venv/bin/python -I -u ../../study/external-proof/n8/audit_dittert_n8_stdlib.py | tee n8-independent.txt
nice -n 15 ../../../../.venv/bin/python -I -u ../../study/external-proof/n9/verify_dittert_n9.py | tee n9-primary.txt
nice -n 15 ../../../../.venv/bin/python -I -u ../../study/external-proof/n9/audit_dittert_n9_stdlib.py | tee n9-independent.txt
