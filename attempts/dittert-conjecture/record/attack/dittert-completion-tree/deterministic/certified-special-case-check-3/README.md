# Dimension seven, attributed reconstruction and independent exact audit

Mathematical source: Hongyuan Lu's argument, pinned source commit
56397b70299278b338a286b90361180833dbf983. The executable reconstruction
and separate SymPy audit are Nascimento's, pinned in study/external-proof
at commit 894066bbaa715138c98bf3cb7c6fdb4f39a37701.

The primary verifier runs its explicit dimension-seven branch. The independent
runner loads only the reviewed independent module and executes its n7 scalar
and bridge routines, avoiding unrelated n6 recomputation. No checks are
disabled. Both implementations check exact coefficients, rational domains,
case completeness and positivity. The reviewer inspected these executable
paths before recommending the commands.

Analytic reductions and supplementary details are in study/audit-n7.md.
Software uses Python integers/Fraction and independently SymPy/NumPy object
arrays of exact rationals. Runs are sequential, nice 15, one thread.
