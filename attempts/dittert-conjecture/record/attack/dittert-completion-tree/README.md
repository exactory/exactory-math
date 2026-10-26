# Dittert completion: evidence and replay

The requested statement is Dittert's inequality with its unique equality
case for every nonnegative real matrix of total entry sum n, for 5<=n<=15.
Read [PROOF.md](PROOF.md) for the assembled argument and the dimension map.
The source material was already public. This package does not claim a new
solution, a second independent analytic proof, or a full Lean formalization.

## Evidence

- Dimensions 5 and 6 inherit the existing checked SOS certificates linked
  in PROOF.md. Their expensive computations were not rerun.
- Dimensions 10 through 15 use the analytic audit and deterministic step 1.
- Dimensions 8 and 9 additionally use the independent audit and step 2.
- Dimension 7 uses the supplemented independent audit and step 3.
- Step 4 checks only a common scalar quadratic lemma in Lean. It is not a
  dependency of the matrix proof and does not formalize the matrix reduction.
- Step 5 tests a repaired negative-slack failure exit in the older n=6
  integer checker. The original full integer-run log is preserved in study/;
  the large matrix computation was not rerun.
- [The search tree](search-tree.json) records the dimension-specific nodes,
  their refinements, and the unused fallback strategies. Older unresolved
  spectral or capacity conjectures are not marked proved by this work.

The exact arithmetic checks were run in this session. Each step directory
contains its reproducible check.sh, outputs, scope and trust-base README,
and the harness-written result.json. The independent assembly review is
recorded in [study/final-evaluation.md](study/final-evaluation.md).

## Replay

Run from the research workspace:

```sh
bash attack/dittert-completion-tree/verify_all.sh
```

This runs the new checks sequentially. Their mathematical processes use
one thread and nice priority 15. Do not start another replay concurrently
on a shared machine. The local Python environment and cached Lean/Mathlib
libraries used by each check are documented in its README and check.sh.
There is no large SOS search, exhaustive matrix enumeration, or Mathlib
rebuild. This replay updates the step output files and result.json records.

## Attribution and publication status

Hongyuan Lu supplied the dimension 7 proof architecture; Pedro Paulo
Marques do Nascimento supplied the audited reconstruction and the unified
dimension 8 and above proof. The source repository is pinned to
894066bbaa715138c98bf3cb7c6fdb4f39a37701 under study/external-proof,
with its original licenses. The upstream proof is not journal-peer-reviewed.
The added audits, verification implementation, and exposition remain local.
No publication, upload, or Git commit is part of this task.
