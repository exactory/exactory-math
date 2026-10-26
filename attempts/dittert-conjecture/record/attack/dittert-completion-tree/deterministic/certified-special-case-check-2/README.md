# Dimensions eight and nine, primary and independent checks

Both implementations come from Nascimento's pinned public working proof,
commit 894066bbaa715138c98bf3cb7c6fdb4f39a37701. The dimension-specific
auditor shares no code with its primary verifier. The primary uses exact
polynomial arithmetic and Sturm/Bernstein certificates; the auditor derives
the permanent by exact Ryser interpolation and reconstructs the scalar
polynomials independently. The independent reviewer read both analytic
reductions and the executable paths before these runs.

All four commands run sequentially at nice 15 with one thread. Results
are written next to this README. This verifies the whole parameter intervals
and discrete support sizes used in the proof, not a numerical grid. Analytic
coverage is audited separately in study/audit-n8-n9.md. No inference from
finite certificates to arbitrary matrices is made without that audit.
