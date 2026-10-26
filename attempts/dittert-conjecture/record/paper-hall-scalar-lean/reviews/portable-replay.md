# Coordinator verification of the relocated packages

Date: 2026-09-05. Result: PASS for both relocated paper packages.
This is an additional coordinator replay, not the independent review.

The proof sources were copied byte-for-byte from the reviewed attacks
to evidence/lean and evidence/near-zero. Portable documentation uses
paths within the paper workspace. The near-zero replay script was
adapted to use Lean and Lake already on PATH instead of the original
workstation's elan directory.

Each destination initially had no .lake directory. The coordinator
created only a .lake/packages symlink to the existing, pinned dependency
cache. Local project proof artifacts therefore compiled in the relocated
directories; Mathlib dependencies were not rebuilt. The symlinks and
all .lake contents are excluded from the distribution archive.

The commands below ran sequentially, with no other agent using the
mathematical computation slot. Each shell exported LEAN_NUM_THREADS=1
and the installed elan directory on PATH. No installation, download,
full Mathlib rebuild, or external write was performed.

From evidence/lean:

```sh
/usr/bin/time -l nice -n 15 lake build
/usr/bin/time -l nice -n 15 lake env lean -j1 -M2048 ../FinalScalarAxiomAudit.lean
```

Both commands exited with status 0. The build took 29.83 wall seconds
and maximum RSS 1,713,061,888 bytes. The direct audit took 6.10 wall
seconds and maximum RSS 1,496,383,488 bytes. The audit printed exactly
propext, Classical.choice, Quot.sound for scalar_positive,
scalar_exclusion, finite_certificate, and hall_scalar_certificate.
Raw outputs: ../evidence/portable-scalar-build.log and
../evidence/portable-scalar-axioms.log, relative to this review.

From evidence/near-zero:

```sh
/usr/bin/time -l sh replay.sh
```

The command exited with status 0. It compiled Definitions, Certificate8,
Certificate9, and Main, then directly audited identity8, positive8,
identity9, positive9, and near_zero_certificate. Every printed closure
was exactly propext, Classical.choice, Quot.sound. Wall time was 42.63
seconds and maximum RSS was 1,642,512,384 bytes. The raw output is
../evidence/portable-near-zero-replay.log.

These observations include reused dependency caches and shared machine
load. They are not empty-cache installation tests, alternative-kernel
checks, performance comparisons, or total development-cost estimates.
The commands print axiom lists; their current lists were inspected here.
They are not a general automatic allowlist checker for modified sources.

All mathematical processes started for these relocation checks have
finished. No background mathematical job remains from this replay.
