# Exact audit of the unified finite reductions

Source: Nascimento's working proof, pinned repository commit
894066bbaa715138c98bf3cb7c6fdb4f39a37701, under study/external-proof/unified.
The source checker was read completely before execution. It uses standard
library integer and Fraction arithmetic and has no external side effects.

The primary checker certifies the two-zero floors, scalar Hall-cut margins,
and the exceptional n=8,9 marginal polynomials. The independent implementation
here imports no source code, checks the two-zero polynomial against integer
subset-DP permanents at n+1 distinct points, uses SymPy rational root counts,
and enumerates all ordered Hall cuts for n=8..15. Its exact exceptional set
must be precisely the two n=8,9 marginal cuts, checked separately by the
dimension-specific independent auditors. Decimal numbers are diagnostic only.

CPU policy: one job at a time, nice 15, one numerical-library thread. No
search, large SDP, or Lean compilation is performed. Software arithmetic and
the analytic reduction are distinct obligations. A passing result here does
not on its own prove Dittert; study/audit-n10-n15.md supplies the analytic audit,
and the other dimension audits are separate.
