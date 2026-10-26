#!/bin/sh
# Independent check of the Turyn / Theorem 3.5 / Theorem 3.1 certificates over the residue R (the 8,125 survivors of Theorem 6.3).
cd "$(dirname "$0")" && exec python3 check_tests.py R_survivors_thm63.txt certificates_R.jsonl survivors_R.txt
