# Record of the objective `stretched-lr-negative-coefficient`

The layout mirrors the original workspace, so that the paths quoted in the documents (`attack/...`, `deterministic/...`, `tools/...`) still lead to the right files. Large per-polynomial records, archives and harness files were not copied; each run folder keeps its code, its checker, its README, its summaries and its smaller outputs. Some copied scripts contain local absolute paths of the original workspace (see "How to check" in the main README).

## Top level of `attack/`

- `attack/SEARCH_TREE.md`: the cross-attack index: exact scope, lineage, status and next question of each attack, the checkpoints, and what is proved and what is only measured. Start here.
- `attack/HANDOFF.md`: the state when the user halted the session at move 19, and the next necessary actions.
- `attack/RETROSPECTIVE.md`: the record's own account of what was proved, what was measured, what went wrong and what a route to a proved case would need.
- `attack/checkpoints/`: 19 checkpoint notes `CP-<id>.md`, each with the exact statement added, the evidence paths, the open obligations and the next hypothesis. The `.tar` archives they name are not copied.

## The four attacks

Each attack folder holds:

- `problem.json`: the attack's claim (`claim`), a structured analysis of the problem (`shape`) and the known results with references (`known`).
- `journal.jsonl`: the journal of moves, one JSON object per line; the fields `action` and `output` describe each move and what it established.
- `novelty.md`: the novelty check of the attack's claim.
- `study/`: the literature and strategy studies (Markdown); `study/sources/` (papers, LaTeX sources and a clone of a third-party repository) is not copied.
- `deterministic/<run>/`: one folder per computation run, each with a `README.md` (what the run decided), the code, `check.sh` and the checker script (independent check), `input.json` where present, `result.json` (the harness's record of the checker run) and summary files.

The attacks:

- `attack/stretched-lr-polynomial-negative-coefficient/`: the box (length at most 7, size at most 30); finished, its claim of a counterexample in the box refuted on the evidence.
  - `units/INVENTORY.md`: every move, the candidate claims and the exact state of the attack; `units/FINISHED.json`: the harness outcome (`cashed-out`, units 1 and 2).
  - `units/1/`: `unit.json` (statement and form), `proof.md`, `position.md`, `evaluation.md` (the independent reader's third pass and the author's resolution). The unit's draft is `../paper/box-length-at-most-six.md`.
  - `units/2/`: the same files with `evidence.md` instead of `proof.md`. Draft: `../paper/box-length-at-most-seven.md`.
  - `deterministic/enumeration-run-1/`: calibration scan of a stratified sample of the box (9,477 polynomials); its record files are not copied (one is over 5 MB).
  - `deterministic/enumeration-run-2/`, `enumeration-run-3/`, `enumeration-run-4/`: the whole box at 5, 6 and 7 parts; logs and summaries copied, record files (24 MB to 455 MB each) not copied.
  - `deterministic/certified-special-case-check-1/` to `-3/`: the second program for 5 and 6 parts and the second encoding for 7 parts (summaries, logs, empty mismatch files).
  - `deterministic/certified-special-case-check-4/`: the census of coefficient ratios and $h^*$ vectors; `census.below1.jsonl` holds the 7,469 polynomials with a coefficient below the simplex value, one JSON object per line.
- `attack/stretched-lr-negative-coefficient-unbounded/`: the negative side beyond the box; finished, no counterexample.
  - `units/INVENTORY.md`, `units/FINISHED.json`, and `units/1/` (`evidence.md`, `evaluation.md`, `position.md`, `unit.json`) and `units/2/` (`proof.md`, `evaluation.md`, `position.md`, `unit.json`). The evaluations are the author's self-checks. Drafts: `../paper/beyond-the-box-samples.md` and `../paper/counterexample-necessary-conditions.md`.
  - `deterministic/counterexample-search-run-1/` to `-6/`: the samples of classes S1, S4 (transportation polytopes), S2, S3 and E (two runs), as named in each README. The records of run 1 are not copied (`s1.jsonl.gz` is over 5 MB); `counterexample-search-run-3/s2.jsonl.gz` (2.5 MB) and the records of runs 2, 4, 5 and 6 are.
- `attack/ktt-positivity-conjecture/`: the full claim, positive side; open, 7 moves of 24.
  - `LINEAGE.md`: its predecessors, inherited results and hypothesis; `ADMISSION.md`: the admission ledger, the review of the move-5 proposal and the move-8 proposal awaiting review.
  - `study/`: besides the studies, the derivations of moves 2, 3, 4, 6 and 7 (`rank-uniformity.md`, `h-star-translation.md`, `h-as-a-hilbert-numerator.md`, `not-integrally-closed.md`, `why-h-is-nonnegative.md`).
  - `deterministic/certified-special-case-check-1/`: the sign census of the $h$ vectors (`h-sign.summary.json`, empty `h-negative.jsonl`). Its copy of `census.below1.jsonl` is not copied: it holds the same 7,469 records as the box attack's census, in another order.
- `attack/ktt-positivity-length-five/`: every triple with at most 5 parts; open, 19 moves of 24, halted at the user's request.
  - `ADMISSION.md`: the ledger of what is proved (P1 to P5) and what is measured (M1 to M5), every proposal, and the seven independent reviews with their amendments.
  - `study/`: the problem and strategy studies and the derivations of moves 11 (`non-full-dimensional-reduction.md`) and 18 (`low-dimensional-weights-can-be-negative.md`).
  - `deterministic/certified-special-case-check-1/`: extraction of the local formula, validated on 2,000 polytopes (`edge-types.json`, 1.0 MB, the 8,305 edge types).
  - `deterministic/symbolic-computation-run-1/`: the exact linear system for the codimension-5 weights and its rank.
  - `deterministic/certified-special-case-check-2/`: the Berline-Vergne weight in dimensions 1 to 5 (`weights.json`).
  - `deterministic/enumeration-run-1/`: the weights of the 3,406 edge classes (`atlas.jsonl`).
  - `deterministic/certified-special-case-check-3/`: cells of the chamber complex and their extreme rays (`cells.jsonl`, 1.6 MB).
  - `deterministic/enumeration-run-2/`: the cell functional from the local formula and the sweep of full-dimensional cells (`cells.jsonl`, `weights.jsonl`).
  - `deterministic/certified-special-case-check-4/` to `-6/`: the sharper residue (`negative-classes.json`), local domination and the per-facet inequality.
  - `deterministic/enumeration-run-3/`: the search for a failing facet, with the full and the truncated mechanism passes (`per-facet.jsonl`, `per-facet.truncated.jsonl`) and the mediation analysis.
  - `deterministic/enumeration-run-4/`, `certified-special-case-check-7/`: the scalar-product gate and screen (`gate.json`, `screen.json`, `forms.py`).
  - `deterministic/certified-special-case-check-8/`: the zero-row test (`rows.jsonl`, 1.4 MB).
  - `deterministic/enumeration-run-5/`: the projected atlas of the non-full-dimensional hives; `types.jsonl` (9.8 MB), `projected.jsonl` (82 MB) and the 1.3 MB progress log are not copied, the summary is.

## `tools/`

The record's own tools, which the run folders copy: the hive polytope (`hivepoly.py`), the lattice-word counter (`lrtableaux.py`), the tableau polytope (`tableau_polytope.py`), the Horn inequalities (`horn.py`) with the computed essential Horn triples for 3 to 8 parts (`horn-essential-*.json`), the Berline-Vergne weight (`bvweight.py`), the cell and atlas machinery (`chamber.py`, `atlasform.py`, `localform.py`, `transverse.py`, `isotypes.py`), the samplers and scanners (`sample_search.py`, `scan.py`, `scan2.py`, `transport.py`), four helper scripts (`check_gz.py`, `count_strata.py`, `descent.py`, `summarize.py`) and three short logs.

## Not copied

- Per-polynomial and per-polytope records over 5 MB, and smaller record files of the same runs (`enumeration-run-1/scan-maxpart30.jsonl`, `counterexample-search-run-1/s1full.jsonl.gz`), which regenerate with the runs.
- The 19 checkpoint archives (`attack/checkpoints/*.tar`, 1.3 MB to 105 MB, harness snapshots of the record).
- `study/sources/` of the box attack (third-party papers, LaTeX sources and a clone of the ktt-positivity repository).
- Harness files: `activity.jsonl`, `openings.json`, `preconditions.json`, `ranking.json`, `tasks.json`, `.continue_count`, `parent.json`, `units/*/check-unit.json`, `units/*/journal-excerpt.jsonl`, `DONE` markers, `__pycache__/` and the workspace's `.venv/`.
- The unit drafts, which are in `../paper/`.
