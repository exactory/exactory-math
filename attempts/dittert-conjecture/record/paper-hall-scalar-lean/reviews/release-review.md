# Pre-publication release verification

Date: 2026-09-05. Coordinator verification, not a new independent review.

The user authorized production publication, explicitly skipped the
sandbox, confirmed full-manuscript review, and requested the most
permissive terms. The release uses CC0 1.0 for original contributions.

Fresh checks completed successfully:

1. exactory-check lookup verified all eight references, with zero blocking
   findings and zero registry warnings.
2. The n11..15 scalar package passed lake build and a direct Lean axiom
   audit of all four principal declarations.
3. The separate n8,n9 package passed replay.sh and all five axiom audits.
4. All nine axiom closures were checked against exactly propext,
   Classical.choice, and Quot.sound.
5. The newly packaged independent Python review passed: 17 and 19
   coefficients matched exactly, with strict positivity, exact degrees,
   metadata agreement, four literal regression points per dimension, and
   exact journal-excerpt agreement.
6. All eight added review-code/input files match their original sources
   byte-for-byte. The three duplicated certificate/data files match those
   in the primary near-zero package.
7. Plain-text draft/abstract.txt matches the PDF's abstract after whitespace
   and Unicode normalization. No wording or mathematical claim changed.

Logs are in evidence/release-scalar-build.log,
evidence/release-scalar-axioms.log, evidence/release-near-zero-replay.log,
and evidence/release-coefficient-review.json. Builds and audits ran
sequentially, at niceness 15, with one Lean thread and a 2048 MB ceiling.
Pinned dependency caches and existing build results were reused. These
were not fresh-cache installations or alternate-kernel checks.

The PDF SHA256 remains
50b6cc7942be54f342cecac8342f6d5843544c53022370575235afe69ea7d56b.
The manuscript SHA256 remains
61351e54e0206fa307e9fe2b250c5bbacd509326e58128a0af3733802e5761d7.
The eight-page layout therefore remains the previously inspected layout.

The installed deposit CLI has no license-selection flag. It will create
the production draft and its metadata with the citation gate intact.
Before publication, the existing license field will be updated through
Zenodo's API and read back. The current vocabulary endpoint identifies
CC0 as cc0-1.0. The older /api/licenses endpoint returned HTTP 404; no
metadata or gate was altered to conceal that API incompatibility.
