# Working record

This folder is a curated copy of the exactory math-conjecturer record `sidorenko-after-counterexample`. File names are the record's own. Files whose names end in `.json` or `.jsonl` are records of the harness; how to read them is stated below.

## Exploration and candidates

- `exploration/init.json`: the field and question of the exploration as the record opened it, and its author.
- `candidates/candidate-*.json`: the seven candidate questions. Each gives the tentative `statement`, its `source`, the `observation` that produced it, the declared `neighbours`, the `potential` grades (what the question would be worth if it holds up) and a provisional `disposition`.
- `candidates/slate-1.json`: the recorded slate. It gives the final disposition of every candidate (`selected`, `deferred` with the evidence needed, `rejected` with the reason), the two bars it relies on, and the written `comparison`.

## Exploratory probes

These computations explored the reported construction. The record gives them no evidential credit.

- `probes/small_spheres.py`, `probes/small-spheres-spec.json`: enumerate the triangulations of the 2-sphere with 4 to 13 vertices and test the two combinatorial hypotheses of the manuscript. It needs plantri 5.8 at `probes/bin/plantri`, which is not included (third-party code; the spec records its checksum). Run it from this folder: `python3 probes/small_spheres.py probes/small-spheres-spec.json OUTDIR`.
- `probes/band_triangulations.py`, `probes/bands-spec.json`: band complexes and twisted blow-ups of cycles, for $5 \le k \le 11$.
- `probes/complex_structure.py`: the structure of the triple system of the reported counterexample, from its Table 1.
- `probes/table1.json`: Table 1 of the manuscript (22 faces on 13 points), transcribed with its source.
- `probes/small-spheres-1/`, `probes/band-triangulations-1/`, `probes/complex-structure-1/`: the standard output and result files of the three recorded runs.

## Formulation

- `formulation/girth-six-draft.md`: the working draft of the statement, the neighbours to declare and the strongest objection.
- `formulation/statement-girth-six.json`: the recorded statement: `statement`, `resolution_criteria`, the eight declared `neighbours`, and the Lean `formal_statement` (identical to `../formal/GirthSix.lean`).

## Readings

- `readings/*.json`: the record's twenty notes on works it read in full (`conlon-lee-2017.json` and `conlon-lee-2017-2.json` both concern arXiv:1611.05784v2). Each note lists `inspections` (an `anchor`, which is a short quotation that locates a passage of the source, and a `note` on what the record took from it) and `notes` under the headings problem, claims, assumptions, methods, evidence, limitations and relevance. The full texts are not included.

## Openness

- `openness/assignment-openness-fable-2.json`: the independent openness review by Claude Fable 5.1. `decision` is the reviewer's decision; `findings.openness` holds the `outcome` (`supported_open`), the `coverage` of the searches, the `reason` and the bound `minimum` (the nine search formulations and their digests); the other `findings` fields state the subject, scope, assumptions, dependencies and policy.

## Bounded attempt (math-solver)

- `attempt/SEARCH_TREE.md`: the generated index of the search tree: the objective, the four obligations of the case-split route, the two nodes and the three strategy reassessments. Its links into `.search/` point to harness internals that are not copied.
- `attempt/contract.json`: the solver contract: the claim, its quantifiers, the reviewed proof policy, the requested decision and the resource limits.
- `attempt/attempt-girth-six-solver-1.json`: the recorded problem attempt: `footholds`, `obstructions` (each with its scope and acceptance), `unresolved` items and the `applicability` of the native claim to the statement.
- `attempt/studies/problem.md`: the problem study: queries, hits read in full, and the constraints they put on the plan.
- `attempt/studies/novelty.md`: the novelty study for the root statement and the two premises.
- `attempt/studies/reduce-and-translate.md`: the strategy study of the reduction node.
- `attempt/studies/prove-the-barrier-first.md`: the strategy study of the barrier node. Its appendix transcribes the passages of the reported counterexample that the barrier uses; the bracketed line numbers refer to an extracted text of the manuscript that is not copied.
- `attempt/class-c2-reduction/LINEAGE.md`: lineage and checkpoint of the reduction node.
- `attempt/class-c2-reduction/journal.jsonl`: the journal of its one move, one JSON object per line (`strategy`, `entry`, `action`, `output`, and flags such as `problem_changed`).
- `attempt/class-c2-reduction/proofs/pendant-subdivision-reduction.md`: the accepted proof (acceptance-000001): Lemma A and Proposition B.
- `attempt/sign-model-barrier/LINEAGE.md`, `attempt/sign-model-barrier/journal.jsonl`: the same for the barrier node.
- `attempt/sign-model-barrier/proofs/sign-model-obstruction.md`: the accepted barrier (acceptance-000002): Lemma O and Corollary O′. It cites lines of the extracted manuscript text, which is not copied.

## Value case and self-assessment

- `value/problem-value-girth-six-2.json`: the recorded value case: the `motivation` and `current_state` paragraphs as posted, each with its `evidence` (full readings and accepted results).
- `value/assessment-girth-six-2.json`: the recorded self-assessment: `grades`, the `primary` ground and criterion, and for each rubric item an evidence reference and a note.

## Independent reviews

- `reviews/problem/assignment-bar-fable-3.json`, `assignment-bar-opus-3.json`, `assignment-bar-sonnet-repair-3.json`: the bars recorded as `problem-bar-fable`, `problem-bar-opus` and `problem-bar-sonnet-3`.
- `reviews/problem/assignment-result-opus-2.json`, `assignment-result-sonnet.json`: the two result reviews used for the decision.
- `reviews/problem/assignment-adjudication-*.json`: the fourteen focused adjudications by Claude Opus 5.5 at effort xhigh. A name ending in `-2` is the second decision on the same objection, made after the `not_binding` disposition was added.
- `reviews/problem/problem-decision-girth-six-post.json`: the recorded post decision with its reason.
- `reviews/attempt/assignment-admission-*.json`: the admission reviews of the two nodes. `assignment-admission-barrier-fable.json` asked for a revision; `-2` approved the revised proposal.
- `reviews/attempt/assignment-result-c2-fable.json`, `assignment-result-barrier-fable.json`: the independent reviews that accepted the two results.
- `reviews/attempt/assignment-reassess-*-fable.json`: the reviews of the three strategy reassessments.

How to read a bar or result review: `value.status` is `sufficient` or `insufficient`; `value.reason` is the review text; a result review adds `value.rubric` (the grades) and `value.rubric_evidence`; `objections` lists the reviewer's own objections, each with its claim, reason and resolution condition; `value.objection_findings` gives the reviewer's finding on each earlier objection; `limitations` lists what the reviewer could not check. An adjudication gives the `objection_id`, the `disposition` (`upheld`, `not_upheld` or `not_binding`) and the `reason`. A native review of the attempt gives the `decision` and `findings`.

## Left out

- Third-party material: the full texts and extracted texts of papers, including the manuscript of the reported counterexample and the copies under the attack root; the captured openai/math catalogue and Lean sources; search API responses; source previews; the plantri binary and source archive.
- Harness internals: the research store, `.venv/`, payload files other than the value case and the decision, `attack/.search/`, checkpoint, proposal and reassessment specifications, review packets and request specifications, run logs, receipts, tools, and `formal/.lake/`.
- Superseded review turns: the earlier versions of the bars, the first Opus result review, and the earlier repairs of the Sonnet bar. They remain in the source record.
- `attempt/drafts/`: earlier drafts of the two proofs, superseded by the accepted versions.
- `candidates/biregular-notes.md`: working notes on the other selected candidate, which this record did not formulate.
- `attempt/reviews/fable-route-retirement.txt`: withheld because it quotes a message of the record's owner; its facts (the Fable usage limit and the continuation of the slot on Claude Sonnet 5.5) are stated in the problem README.
