# Working record

This folder is a curated copy of the attack folder `attack/quantitative-van-der-waerden` of the math-solver workspace `dittert-conjecture`, with the original file names and relative layout. The rest of that workspace, including `STATUS.md` with the attack summary in its section 3.3, is in [../../dittert-conjecture/record/](../../dittert-conjecture/record/). The Lean sources of the step `deterministic/formal-check-1` are in [../lean/](../lean/).

How to read the JSON files:

- `journal.jsonl`: one JSON object per line, one line per move (6 moves), with the fields `move`, `strategy`, `entry`, `action` (what was done), `steps` (the deterministic steps run), `output` (what the move established), `costs_paid`, `failure_signal_fired` and `closes`. `units/INVENTORY.md` lists the same moves in prose.
- `problem.json`: the claim and its structured `shape` analysis (objects, extremal candidates, known bounds, missing input), written before the attack.
- `deterministic/numerical-optimisation-run-1/result.json`: the harness verdict and the first lines of the run's output.

## Files and folders

| Path | What it is and why it is here |
|---|---|
| `novelty.md` | literature and novelty search for the claim |
| `problem.json` | claim and shape analysis |
| `journal.jsonl` | the six moves |
| `study/problem.md` | problem-level literature study |
| `study/attack-the-negative-side.md`, `ladder-the-parameter.md`, `prove-the-barrier-first.md`, `verify-formally-with-lean4.md` | strategy studies, one per strategy of the walk |
| `study/route-capacity.md` | the capacity route: Theorems 1 and 2 with proofs, the $m$-column form, the two-column work, the drop lemma and what remains |
| `study/route-interpolation.md` | the interpolation route: $n = 2$, the sharp $n = 3$ theorem, the local theorem, exact identities, and why the one-variable route cannot reach the claim |
| `study/lemma2-prime.md` | Lemma 2': the scaling cost bounded through the scaling's own spectral gap; the branch correction |
| `study/application.md` | what the claim would give Dittert's conjecture, with the correction of 2026-09-04 |
| `study/route-capacity-*.py`, `route-interpolation-*.py` with `*-output.txt` | the numerical and exact checks cited in the two route files, each with its saved output |
| `study/verify-capacity-claim.py` | independent reimplementation that checks Theorems 1 and 2 |
| `study/qvdw-constant.py`, `qvdw-test.py`, `two-column-test.py` with outputs | measured sharp constant, global failure of the local constant, the two-column test |
| `study/lemma2-prime*.py`, `branch-structure.py`, `application*.py`, `lambda2-comparison.py`, `n7-sensitivity.py` | scripts for Lemma 2', the two fixed-point branches and the application tables |
| `units/1` to `6` | write-ups (`draft.md`), evaluations and positions: Theorem 1, Theorem 2, the $n = 3$ case, the measured constant, the structure theorem for Dittert counterexamples, the barrier |
| `units/INVENTORY.md` | every move in prose, with the costs paid |
| `deterministic/numerical-optimisation-run-1/` | multi-start search for $c^*(n)$ at $n = 3, \dots, 9$ (`search.py`, `check.py`, `check.sh`, `result.json`) |
| `deterministic/formal-check-1/README.md` | the Lean step for $n = 3$ and why it was recorded as not run |
| `deterministic/formal-check-1/lean-direct3.log` | output of the failed run of the first version of `QvdW3b.lean` |

## Not copied

- Harness internals: `activity.jsonl`, `openings.json`, `preconditions.json`, `ranking.json`, `.continue_count`, `units/*/unit.json`, `units/*/check-unit.json`, `units/*/journal-excerpt.md` (the full journal is copied), `units/FINISHED.json`, `deterministic/formal-check-1/step.json`, `__pycache__/`, `.lake/` (a link to the Mathlib packages of another project).
- Empty logs of the Lean step: `build.log`, `lean-direct.log`, `lean-direct2.log`, `lean-direct4.log` (all 0 bytes).
- The Lean sources and project files of `deterministic/formal-check-1`, which are in `../lean/`.
