# Record of the attack `barker-lengths-below-10-100-residue`

This folder holds the curated working record of the math-solver attack. Paths such as `deterministic/enumeration-run-1/` in the copied files refer to this folder; `../_sources/` held third-party material that is not copied.

## Files

- `problem.json`: the attack's claim, a structured analysis of the problem (`shape`) and the list of known results (`known`). Read the `claim` and `known` fields first.
- `journal.jsonl`: the journal of research moves, one JSON object per line. It has one move; the field `output` states what the move established.
- `novelty.md`: the novelty check of the claim, with queries and verdict.
- `tasks.json`: the attack's task list. Tasks 1 and 2 are done; tasks 3 to 6 are open and describe the remaining plan.
- `study/problem.md`: the problem-level literature study (queries, sources read, constraints on the plan).
- `study/reduce-to-a-finite-computation.md`: the strategy-level study of how the statement was computed before.

## Computation runs (`deterministic/`)

- `enumeration-run-1/`: Theorem 6.3 of Leung-Schmidt (2016) on the whole list; the only journalled run.
  - `README.md`: what the run decided, the files, the trusted base and how to reproduce it.
  - `search_thm63.py`: the search; `check_thm63.py` and `check.sh`: the independent checker.
  - `survivors_thm63.txt`: the 8,125 survivors (the residue $R$), in the input format `u [p1, p2, ...]`.
  - `result.json`: the harness's record of the checker run (status `pass`); `run.log`: the run's log.
  - `test_top19_certs.jsonl`, `test_top19_surv.txt`: a smoke test on the 19 values with $n \le 10^{50}$ (all eliminated; the survivor file is empty).
  - Not copied: the input list (third-party data, linked in the main README), its smoke-test subset, and `certificates_thm63.jsonl` (76.7 MB; regenerate it with the search).
- `enumeration-run-2/`: Turyn's test and Leung-Schmidt (2012) Theorems 3.5 and 3.1 on the whole list. No README and no journal entry.
  - `search_tests.py`: the search (its docstring states the three tests as implemented); `check_tests.py`, `check.sh`: the checker.
  - `certificates_tests.jsonl`: the 238 certificates of the whole-list run (228 Turyn, 10 Theorem 3.1); `run.log`: its log.
  - `validation/*.certs.jsonl`: certificates of validation runs on published sets of eliminations; the input sets and survivor lists were extracts of third-party data and are not copied. The file name gives the set, and for most sets also its size.
  - Not copied: the input list and `survivors_tests.txt` (29 MB, the list minus the 238 certified values).
- `enumeration-run-3/`: the same three tests on the residue $R$. No README and no journal entry.
  - `search_tests.py`, `check_tests.py`, `check.sh`: identical copies of the run-2 scripts, with `check.sh` pointed at this run's files.
  - `certificates_R.jsonl`: empty (no value of $R$ was eliminated); `run.log`: the log with the final counts.
  - Not copied: `R_survivors_thm63.txt` and `survivors_R.txt`, both byte-identical to `enumeration-run-1/survivors_thm63.txt`.
- `counterexample-search-run-1/`: the feasibility scan for Theorem 6.1 of Leung-Schmidt (2016) on $R$. Not journalled.
  - `README.md`: the question, the result and the files.
  - `scan_thm61.py`: the scan; `check_scan.py`, `check.sh`: the independent recomputation.
  - `scan_thm61.jsonl`: one JSON object per survivor with `u`, `min_bad`, `empty_bad`, `feasible` and `feasible_multi`, as defined in the run's README.
  - Not copied: its copy of the survivor list (identical to the one in `enumeration-run-1/`).

## Not copied

- `activity.jsonl` (tool-activity log of the harness, with local paths), `openings.json`, `preconditions.json`, `ranking.json` and `.continue_count` (harness strategy-selection and stop-hook files).
- `../_sources/`: captured third-party material (papers and their extracted text, the LaTeX source of arXiv:1306.0045, Mossinghoff's data files, the formal-conjectures Lean statements) and two download scripts that contain a local path and a personal contact address.
