# Working record

This folder is a curated copy of the exactory math-conjecturer record `stretched-lr-positivity`. File names are the record's own. This record keeps its candidates, statements, openness findings, value case and reviews only in its research store, so those files were exported from the store, read-only, one record per file, under the record's own identifier. Files whose names end in `.json` or `.jsonl` are records of the harness; how to read them is stated below.

## Exploration and candidates

- `exploration/init.json`: the field and question of the exploration as the record opened it, and its author.
- `candidates/candidate-*.json`: the seven candidate questions (exported). Each gives the tentative `statement`, its `source`, the `observation` that produced it, the declared `neighbours`, the `potential` grades (what the question would be worth if it holds up), `notes` and the `disposition`.
- `candidates/problem-slate-1.json`: the recorded slate (exported): the selected, deferred and rejected candidates with reasons, the two bars it relies on, and the written `comparison`.

## Exploratory probes

These computations explored the field. The record gives them no evidential credit.

- `probes/hivepoly.py`: shared module: the hive inequalities, integer hive counts by enumeration, and Ehrhart quasi-polynomials by PyNormaliz.
- `probes/dim2_hives.py`, `probes/dim2-spec.json`: the probe `dim2-hives-1` (two-dimensional hive polytopes of at most five parts and size at most 22, tested against Scott's inequality and $b\ge 3$). It also needs lrcalc.
- `probes/dim2-hives-1/stdout.txt`: the summary output of that run.
- `probes/hstar_inequalities.py`: the program of the probe `hstar-inequalities-1` (five necessary $h^*$-inequalities on stored stretched polynomials). Its input files belong to another record and are not included.

## Formulation

- `formulation/statement-1.json` to `statement-4.json`: the four recorded statement versions (exported). Each gives `title`, `statement`, `resolution_criteria`, `neighbours` and `formal_statement` (none). `statement-4.json` is the posted version.

## Openness

- `openness/assignment-openness-claude-2.json`: the openness finding for `statement-4` with its independent review by Claude Fable 5.1 (exported). `outcome` is `supported_open`; `coverage`, `reason` and `minimum` (the four searches, the three neighbours and the bound readings) describe the finding; `review` holds the reviewer's `decision` and `findings`.
- `openness/assignment-openness-astra-5.json`: the earlier finding for `statement-3`, reviewed by gpt-6-astra (exported).

## Bounded attempt (math-solver)

- `attempt/SEARCH_TREE.md`: the generated index of the search tree: the objective, its obligations, the node and the two strategy reassessments. The second reassessment includes verbatim copies of move notes as delivered to its reviewer. Its links into `.search/` point to harness internals that are not copied.
- `attempt/problem-attempt-4.json`: the recorded problem attempt (exported): `footholds`, `unresolved` items and the `applicability` of the native claim to the statement.
- `attempt/studies/problem.md`: the problem study: queries, works read in full, and the constraints on the plan.
- `attempt/studies/novelty.md`: the novelty study of the statement and its neighbours.
- `attempt/studies/attack-the-negative-side.md`, `attempt/studies/make-the-proof-constructive.md`: the two strategy studies.
- `attempt/studies/scripts/instance_check.py`, `instance_check.out.txt`: the exploratory scan of five-part triples up to size 15 that found the seed instance, and its annotated output.
- `attempt/studies/scripts/seed_check.py`, `seed_check.out.txt`: an exploratory check of the seed construction with Normaliz, and its annotated output.
- `attempt/hive-equidecomposability/LINEAGE.md`: lineage and checkpoint of the node.
- `attempt/hive-equidecomposability/journal.jsonl`: the journal of the node's five moves, one JSON object per line (`strategy`, `entry`, `action`, `output`, and flags such as `failure_signal_fired` and `problem_changed`).
- `attempt/hive-equidecomposability/proofs/smallest-instance.md`: the accepted proof of the seed instance (acceptance-000001).
- `attempt/hive-equidecomposability/notes/`: the notes of moves 1, 2, 3 and 5, an index (`README.md`), and `corrections.md`, which records corrections to earlier wording, including a phrase of the accepted proof (the accepted text itself is left unchanged).
- `attempt/hive-equidecomposability/checks/`: exploratory checks with their outputs (`seed_check.py`, `zero_parts.py`, `five_instances.py`, `cut_shear_apply.py`) and an index (`README.md`).

## Value case and self-assessment

- `value/problem-value-10.json`: the recorded value case (exported): the `motivation` and `current_state` paragraphs as posted, each with its `evidence` (full readings and the accepted result).
- `value/problem-assessment-10.json`: the recorded self-assessment (exported): `grades`, the `primary` ground and criterion, and for each rubric item an evidence reference and a note.

## Independent reviews

- `reviews/problem/problem-bar-astra.json`, `problem-bar-luna.json`: the two bars (exported).
- `reviews/problem/problem-result-*.json`: the six recorded result reviews (exported). `problem-result-luna` is by gpt-6-luna; `problem-result-astra-claude` and `-2` are by Claude Opus 5.5; `problem-result-luna-claude`, `-2` and `-3` are by Claude Sonnet 5.5. The decision uses `problem-result-astra-claude-2` and `problem-result-luna-claude-3`, which review `statement-4`; the others review `statement-3`.
- `reviews/problem/problem-decision-1.json`: the recorded post decision with its reason (exported).
- `reviews/attempt/assignment-proposal-astra.json`, `assignment-proposal-astra-2.json`: the admission reviews of the attempt's proposal by gpt-6-astra (`revise`, then `approve`).
- `reviews/attempt/assignment-reassess-1-astra-4.json`, `assignment-reassess-2-astra-5.json`: the reviews of the two strategy reassessments.
- `reviews/attempt/assignment-seed-proof-astra.json`: the independent review that approved the seed proof.

How to read an exported review record: `reviewer_id` and `assignment_id` identify the reviewer and the run; `subject` names the reviewed statement; `payload` is the observed review. In it, `value.status` is `sufficient` or `insufficient`, `value.reason` is the review text, `value.rubric` holds the grades of a result review, `objections` lists the reviewer's own objections, `value.objection_findings` gives the finding on each earlier objection, and `limitations` lists what the reviewer could not check. A native review of the attempt gives the `decision` and `findings`.

## Changes made in this copy

- `attempt/studies/scripts/instance_check.py`, `attempt/hive-equidecomposability/checks/five_instances.py` and `checks/cut_shear_apply.py` inserted an absolute local path to the record's `probes/` folder into `sys.path`. In this copy that line computes the path of `../probes` from the file's own location (and `os` is imported for it); `instance_check.py` also had a local interpreter path in its docstring, replaced by `<venv>/bin/python`. `checks/README.md` had the same interpreter path, replaced the same way. Nothing else was changed.
- Re-run for this copy with Python 3.13 and PyNormaliz: `cut_shear_apply.py` and `zero_parts.py` reproduce their recorded outputs exactly, and `seed_check.py` reproduces every data line of its annotated output. `instance_check.py` reproduces its annotated output except one line: for the fifth triple, printed as `(5, 4, 3, 2, 1), (3, 2, 1, 1), (3, 2, 2, 1)`, the recorded output gives dimension 3, while the re-run gives dimension 4, as do `five_instances.py`, `cut_shear_apply.out.txt` and the note of move 5. This repository does not change the recorded output.

## Left out

- Third-party material: the full text of Cho, Jung and Moon (2008) under `attack/studies/sources/`, the raw search API responses under `attack/studies/queries/` and `sources/`, and the captured full texts in the research store.
- Harness internals: the research store itself, `attack/.search/`, `attack-specs/`, the node's problem, precondition, ranking, openings, task and activity files, the review assignment inputs, refusals and repair files under `reviews/`, the probe launchers, tools, and `problem-export/` (the posted parts, reproduced in the problem README).
- Large outputs: the result files of the two probes (10.5 MB and 6.7 MB).
- `probes/hstar-spec.json` and the standard output of `hstar-inequalities-1`: they name the input files by absolute local paths of another record. The probe's counts are stated in the candidate record and the studies.
- `reviews/contamination/route-retirement-2026-10-21.md`: withheld because it quotes messages of the record's owner. The other contamination files are harness records of the event described in the problem README.
- Duplicates: the node's `study/` folder and `novelty.md`, identical to the files under `attempt/studies/`.
