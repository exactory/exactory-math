# Working record

This folder keeps the layout of the original math-solver workspace `dittert-conjecture`, so that relative links inside the copied files resolve. Only a curated part is copied; links to material that is not copied (listed at the end) do not resolve. The attack `quantitative-van-der-waerden` of the same workspace is in [../../quantitative-van-der-waerden/record/](../../quantitative-van-der-waerden/record/).

Most attacks have the same parts: `novelty.md` (literature and novelty search), `journal.jsonl` (moves), `study/` (problem study, strategy studies, proofs, scripts), `units/` (cash-out write-ups `draft.md`, each with an `evaluation.md`, and `INVENTORY.md`, which lists every move in prose) and `deterministic/` (checks run by the harness, each with `README.md`, the scripts, their output and the harness verdict `result.json`).

How to read the JSON files:

- `journal.jsonl`: one JSON object per line, one line per move, with the fields `move`, `strategy`, `entry`, `action` (what was done), `steps` (the deterministic steps run), `output` (what the move established), `costs_paid`, `failure_signal_fired` and `closes`.
- `problem.json`: the claim of the attack and its structured `shape` analysis (objects, known bounds, missing input, base theory), written before the attack.
- `result.json` in a step folder: the harness verdict, with `status`, `exit_status` and the first lines of the output; for a Lean step also the checked theorem and its axioms.
- `search-tree.json` (completion tree): the dimension nodes and fallback strategies of that attack.
- `certificate5.json`, `certificate6.json`: the rational certificates, as orbit coordinates of the Gram matrices.
- the other JSON files in step folders are data read by the step's own check script.

## Files and folders

| Path | What it is and why it is here |
|---|---|
| `STATUS.md` | the record's own status and handover, newest section first; the authoritative summary of outcomes, corrections and the task board of 2026-09-04 |
| `FORMALIZATION_SCOPE.md` | exact scope of the Lean scalar developments of 2026-09-05 and what they do not formalize |
| `attack/SEARCH_TREE.md` | controller-generated view of the managed Lean objective `objective-000001`: its obligations and nodes |
| `attack/SEARCH_TREE_manual_2026-09-05.md` | manual cross-attack index of the attacks before the managed objective |
| `attack/checkpoints/` | five checkpoint descriptions; the archived snapshots they describe are not copied |
| `attack/dittert-conjecture-n5-to-n15/` | first attack, 13 moves, 2026-09-03: the $n = 5, 6$ certificates, Theorem R, the Kafidov threshold |
| `.../study/` | problem and strategy studies; `route-a-reduction-theorem.md` (Theorem R with proof); `route-a-capacity-notes.md`; numerical scripts; `gate-symmetry-blocks/` (block sizes of the symmetry-reduced Gram matrices) |
| `.../units/1` to `5` | write-ups: $n = 5$ certificate, $n = 6$ certificate, Theorem R, the certificate pipeline, the state of $7 \le n \le 15$ |
| `.../deterministic/certified-special-case-check-1`, `-2` | the $n = 5$ and $n = 6$ certificates with independent checkers |
| `.../deterministic/certified-special-case-check-3`, `-4` | the exact Kafidov threshold; the exact integer check that the $n = 6$ main Gram matrix is positive semidefinite |
| `.../deterministic/formal-check-1`, `-2` | README and verdict of two Lean steps; sources in `../lean/kafidov-threshold` and `../lean/certificates-n5-n6` |
| `.../deterministic/numerical-optimisation-run-1` to `-4` | numerical evidence; runs 2 and 3 also hold the sum-of-squares search and exact recovery code (`sdp_n.py`, `recover_n.py`, `recover5.py`) that produced the certificates |
| `attack/spectral-gap-near-maximisers/` | second attack, 11 moves, 2026-09-04: the spectral hypothesis of Theorem R; finished with a barrier |
| `.../study/` | strategy studies, `routes-rubric.md` (ten routes), `removing-condition-N.md`, scripts and outputs |
| `.../units/1` to `6`, `units-plan.md` | effective-resistance lemma, scaling-cost reduction, local van der Waerden constant, numerical test at $n = 5..12$, the barrier, missing Mathlib pieces; each with evaluation and position |
| `.../deterministic/numerical-optimisation-run-1` | the contrapositive search behind unit 4 |
| `attack/dittert-completion-tree/` | assembly attack, 7 moves, 2026-09-04/05: `PROOF.md`, the attributed assembled proof for all $5 \le n \le 15$; `README.md` |
| `.../study/audit-n7.md`, `audit-n8-n9.md`, `audit-n10-n15.md` | independent analytic audits of the public Lu and Nascimento arguments |
| `.../study/final-evaluation.md` | independent review of the assembly |
| `.../study/inherited-n6-exact-psd.log` | complete log of the exact $n = 6$ Gram check (slack 1691794048955) |
| `.../deterministic/certified-special-case-check-1` to `-3` | exact checks for $n = 10..15$, $n = 8, 9$ and $n = 7$; each runs Nascimento's verifier and an independent one |
| `.../deterministic/certified-special-case-check-4` | Lean check of a scalar quadratic lemma; source in `../lean/scalar-interface` |
| `.../deterministic/certified-special-case-check-5` | regression test of the repaired exit gate of the $n = 6$ integer checker |
| `attack/dittert-branch-complete-audit/` | final proof attack, 4 moves, 2026-09-05: `PROOF.md`, `BRANCH_TRANSPORT.md` (why the old large-cost branch is covered), `INTERFACES.md`, `SOURCE_CORRECTION.md`, `LINEAGE.md`; `study/independent-review.md` |
| `attack/hall-n7-branch-coverage/` | child attack for $n = 7$: `COVERAGE_PROOF.md` and the exact coverage certificate (`manifest.json`, `check_manifest.py`) |
| `attack/hall-n8-n15-branch-coverage/` | child attack for $8 \le n \le 15$: `PROOF.md`, `CODE_MAP.md` (source branches against cases) and the exact witness-chain check |
| `attack/hall-scalar-lean-n11-n15/` | Lean attack for the scalar layer at $11 \le n \le 15$: design, attempts, statement review, `study/final-review.md`; sources in `../lean/hall-scalar-n11-n15*` |
| `attack/hall-near-zero-lean-n8-n9/` | Lean attack for the near-zero polynomials: `PROOF.md`, `DEFINITIONS.md`, `independent-review.md`, the candidate generator and its data; sources in `../lean/near-zero-n8-n9` |
| `attack/dittert-lean-5-15/` | root node of the managed Lean objective: problem study (prior formalizations, what Mathlib has) and strategy study; it made no moves |
| `attack/reduction-to-boundary/`, `hall-domination/`, `gurvits-floors/` | accepted nodes of the managed objective: journal, unit write-up, independent evaluation, harness result and inspection log |
| `attack/core-entropy/` | accepted node of the managed objective; its evaluation was pending when work stopped |
| `scratch/ctl/gen_support.py` | generator of the support-polynomial Lean certificates in `../lean/blueprint/Dittert/Scalar/Cert/` |
| `scratch/lean-draft/build-draft-2026-09-07.log` | last full build log of the blueprint; it ends with "Build completed successfully (3476 jobs)" and lists the `sorry` stubs |
| `paper-hall-scalar-lean/reviews/` | reviews of the technical note in `../paper/`: independent manuscript review, write-stage report, replay of the relocated Lean packages, release and visual checks |

The Lean sources of the step folders `formal-check-*` and of `certified-special-case-check-4` of the completion tree were moved to `../lean/`. The file `attack/hall-scalar-lean-n11-n15/study/FinalScalarAxiomAudit.lean` is `../lean/hall-scalar-n11-n15/FinalScalarAxiomAudit.lean`.

## Not copied

Third-party material (link instead):

- `attack/dittert-conjecture-n5-to-n15/study/fetched/`: Cheon–Wanless PDF and text, arXiv LaTeX sources of 2606.01531, 2607.19439 and 2607.29191, search responses.
- `attack/dittert-completion-tree/study/external-proof/`: Nascimento's repository, [pinned commit](https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701). The Hall-route checks need it (see the main README).
- `attack/dittert-branch-complete-audit/study/pula-song-wanless.pdf` and `pula-page3.png`: the Pula–Song–Wanless preprint ([source](https://cs.du.edu/~mathfiles/preprints/nsm-math-preprint-1022.pdf)).
- `scratch/study-2026-09-06/`: paper PDFs, a clone of maths-pub and search responses; `scratch/maths-pub-port/` and every copy of `GurvitsPort/`: the port of maths-pub (Apache-2.0).
- `upstream-contribution-proposal/checkout/`: a clone of Nascimento's repository.

Search API dumps: `spectral-gap-near-maximisers/zb1.json`, `hall-near-zero-lean-n8-n9/study/*-arxiv.json`, `*-crossref.json`, `*-semantic.json`, `*-zbmath.json`, `hall-n8-n15-branch-coverage/study/unit-search-response.json`.

Harness internals: `.exactory/`, `attack/.search/` (controller store), `controller/` folders (proposals and review packets), `evidence/manifest-*.json`, `step.json`, `verification-review.json`, `activity.jsonl`, `openings.json`, `preconditions.json`, `ranking.json`, `tasks.json`, `parent.json`, `unit.json`, `check-unit.json`, unit journal excerpts (the full journals are copied), the harness input scripts `study/write-*.py` and `study/update-*.py`, `dittert-completion-tree/verify_all.sh` (a wrapper around the harness command), the driver scripts and review copies under `scratch/ctl/` and `scratch/reviews/`, staging copies under `scratch/`, `.venv/`, `.lake/`, `__pycache__/`.

Snapshot archives: `attack/checkpoints/*.tar`, `hall-n7-branch-coverage/n7-coverage-m2-2026-09-05.tar.gz` with `SNAPSHOT.txt`, `hall-n8-n15-branch-coverage/checkpoints/coverage-m2.tar`, `hall-near-zero-lean-n8-n9/checkpoints/CP-29b31b7c95983bc7/source-snapshot.tar.gz` with `SHA256SUMS`.

Files over 5 MB: `numerical-optimisation-run-2/poly5.pkl` (33 MB), `sdp5-solution.npz` (70 MB, in runs 2 and 3) and `numerical-optimisation-run-3/sdp6-solution.npz` (576 MB). They are numerical solver outputs; the certificates and their checkers do not need them.

Duplicates and intermediates: `numerical-optimisation-run-2/certificate5-1e10.json` (identical to `certified-special-case-check-1/certificate5.json`), `numerical-optimisation-run-2/certificate5.json` (a recovery with denominator $10^6$), `numerical-optimisation-run-3/certificate6.json` (identical to the one in check 2), `study/lean-cert-5.json` and `lean-cert6.json` (the data carried by `Cert/Data5.lean` and `Cert/Data6.lean`), the scripts copied into `scratch/` from the attacks, the unexecuted nodes of the managed objective (their obligations are in `attack/SEARCH_TREE.md`), and the paper workspace's evidence copies, release archives and literature notes.

Withheld because the file mixes publishable content with an excluded item:

- `scratch/lean-draft/Dittert/Bridge/Common.lean`: contains three theorems ported from third-party code (maths-pub).
- `scratch/maths-pub-port/PORT-NOTES.md`: reproduces third-party Lean statements.
- `paper-hall-scalar-lean/DEPOSIT_STATUS.md`, `PUBLICATION.md`: discuss the deposit credentials.
- `upstream-contribution-proposal/PROPOSAL.md`, `PR_BODY.md`: a contribution prepared for a third-party repository.

Planning documents: `docs/superpowers/plans/` and `scratch/ctl/brief-*.md`.
