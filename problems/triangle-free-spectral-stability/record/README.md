# Working record

This folder is a curated copy of the exactory math-conjecturer record `extremal-graph-stability`. File names are the record's own, except the probe outputs and the openness finding, which the record keeps under content digests or only in its research store; they are named here by their record identifiers. Files whose names end in `.json` or `.jsonl` are records of the harness; how to read them is stated below.

## Exploration and candidates

- `exploration/init.json`: the field and question of the exploration as the record opened it, its excluded scope, and its author.
- `candidates/candidate-sharp-three.json`, `candidate-universal-linear.json`, `candidate-linear-bipartite-deletion.json`: the three candidate questions. Each gives the tentative `statement`, its `source`, the `observation` that produced it, the `potential` grades and a provisional `disposition`.
- `candidates/slate-spectral-v1.json`: the recorded slate: selected, deferred and rejected candidates with reasons, the two bars it relies on, and the written `comparison`.

## Exploratory probes

These computations use floating-point eigenvalues. The record gives them no evidential credit.

- `probes/atlas_spectral.py`, `probes/atlas-triangle-free.stdout.txt`: exact edit distances and numerical spectral radii of every nonempty triangle-free graph with at most 7 vertices in the NetworkX atlas, and the summary output (165 graphs, largest ratio).
- `probes/cycle_blowups.py`, `probes/cycle-blowups.stdout.txt`, `probes/results/cycle_blowups.json`: weighted blow-ups of the five-cycle, with the summary output and the largest ratios.
- `probes/edge_average.py`, `probes/edge-neighbourhood-screen.stdout.txt`: a screen of the average of edit costs over edge-neighbourhood bicliques, and its summary output.

The scripts need networkx and numpy and write their full results to `results/` in the working directory.

## Formulation

- `formulation/statement-sharp-three-v1.json`: the recorded statement: `title`, `statement`, `resolution_criteria`, the four declared `neighbours`, and `formal_statement` (none).

## Readings

- `readings/*.md`: the record's notes on the six works it read in full, one per work, under the headings problem, claims, assumptions, methods, evidence, limitations and relevance. The full texts are not included.

## Openness

- `openness/openness-sharp-three-v5.json`: the openness finding with its independent review by gpt-6-astra (exported read-only from the research store). `outcome` is `supported_open`; `coverage` and `reason` describe the finding; `minimum` binds the searches, the neighbours and the readings; `source_evidence` records the publisher preview used to screen the Wang-Lou hit; `native_reviews` binds the approving review of the supporting proof; `review` holds the reviewer's `decision` and `findings`.

## Bounded attempt (math-solver)

- `attempt/SEARCH_TREE.md`: the generated index of the search tree: the objective, the root obligation, the two nodes and the three strategy reassessments. Its links into `.search/` point to harness internals that are not copied.
- `attempt/attempt-sharp-three-v1.json`: the recorded problem attempt: the `footholds` (the supporting theorem, with its acceptance), the `unresolved` item and the `applicability` of the native claim to the statement.
- `attempt/trianglefree-spectral-distance/`: the root node: `LINEAGE.md` (lineage and the two checkpoints), `journal.jsonl` (the journal of its three moves, one JSON object per line), the move notes `ledger-01.md`, `weight-02.md` and `slack-03.md`, `novelty.md`, and the strategy study `study/ladder-the-parameter.md`.
- `attempt/linear-spectral-distance/`: the standalone node of the supporting theorem: `LINEAGE.md`, `journal.jsonl`, the proof `proof.md`, `novelty.md`, the strategy study `study/ladder-the-parameter.md`, and the cash-out files `units/INVENTORY.md`, `units/consolidation.md`, `units/1/unit.json` (the unit's exact claim), `units/1/evaluation.md` (the independent review that accepted the proof, reproduced in full), `units/1/novelty.md` and `units/1/position.md`.

## Value case and self-assessment

- `value/value-sharp-three-v2.json`: the recorded value case: the `motivation` and `current_state` paragraphs as posted, each with its `evidence`.
- `value/assessment-sharp-three-v1.json`: the recorded self-assessment: `grades`, the `primary` ground and criterion, and for each rubric item an evidence reference and a note.

## Independent reviews

- `reviews/problem/record-bar-astra-v2.json`, `record-bar-sol-v2.json`: the two bars.
- `reviews/problem/review-result-*.json`: the five recorded result reviews. The decision uses `review-result-sol-sharp-three-v3` and `review-result-astra-sharp-three-v6-corrected-v1`. `review-result-astra-sharp-three-v4` and `review-result-sol-sharp-three-v2` did not support a decision, and `review-result-astra-sharp-three-v5` did not qualify; the problem README gives the reasons.
- `reviews/problem/decision-post-sharp-three-v1.json`: the payload of the first post decision, which the harness refused at revision 272.
- `reviews/problem/decision-post-sharp-three-v2.json`: the recorded post decision, after which the post gate reported ready.
- `reviews/attempt/review-linear-astra.json`, `review-linear-sol.json`: the two admission reviews of the supporting node.

How to read a bar or result review: `value.status` is `sufficient` or `insufficient`; `value.reason` is the review text; a result review adds `value.rubric` (the grades), `value.rubric_evidence` and `value.assurances`; `objections` lists the reviewer's own objections; `limitations` lists what the reviewer could not check; a reassessment adds `reassessment`, its findings on the reviewer's earlier outputs. A native review gives the `decision` and `findings`.

## Left out

- Third-party material: the problem studies `attack/inputs/problem-study.md`, `attack/inputs/linear-branch/problem.md` and the copies under each node's `study/problem.md`, withheld because they contain the extracted full texts of decisive papers; the captured sources, search API responses and publisher captures; the openness packets.
- Harness internals: the research store, `.venv/`, `attack/.search/`, `native-preparation/` except the two admission reviews, payload files other than those listed above, receipts, tools, the node problem, precondition, ranking, openings, task and activity files, and `units/1/search/` (search API responses).
- `PUBLICATION.md` and `WORK_LOG.md`: the record's narrative of the publication and of the harness repairs made during it. The facts used in the problem README are taken from them and from the files above.
- `probes/results/atlas.json` and `probes/results/edge-average.json`: withheld under this repository's privacy rules. The summary outputs of the same runs are included.
- `units/1/draft.md`: identical to `proof.md`.
