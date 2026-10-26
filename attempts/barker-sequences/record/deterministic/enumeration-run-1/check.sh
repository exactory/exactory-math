#!/bin/sh
# Independent check of the Theorem 6.3 certificates: separate program, own arithmetic, exact rationals.
cd "$(dirname "$0")" && exec python3 check_thm63.py BarkerCandidates100.txt certificates_thm63.jsonl survivors_thm63.txt
