#!/bin/sh
# Independent check of the Turyn / Theorem 3.5 / Theorem 3.1 certificates over the whole list L.
cd "$(dirname "$0")" && exec python3 check_tests.py BarkerCandidates100.txt certificates_tests.jsonl survivors_tests.txt
