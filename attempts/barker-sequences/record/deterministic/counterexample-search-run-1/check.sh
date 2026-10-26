#!/bin/sh
# Independent recomputation of the Theorem 6.1 feasibility scan over the survivors.
cd "$(dirname "$0")" && exec python3 check_scan.py survivors_thm63.txt scan_thm61.jsonl
