# Independent strategy reassessment: phase-modular v2

Date: 2026-09-08.

Decision: approve. V2 corrects the placement of failure comparisons to match the installed validator. It preserves the substantive strategy and all its limitations. This is not approval of a theorem, a result acceptance, an execution reservation, or a claim that a public reassessment submission has succeeded. No blocking defect was found.

## Identity and bindings

The reviewer is the host-provided actor and attestation `01a080c9-5c43-7d53-b2f9-ace28df82d58`, source `host`. This is the same independent reviewer as for v1, not a newly invented reviewer or a new result review. The actor and attestation differ from the assessment author and both current admission authors in the unchanged packet. No delegation occurred.

The supplied v2 subject digest is `94d4a1d94d56777a0836e90e10c1ffd7eca59a0a7d8496750d84b005235ec570`. The original-claim digest remains `e2643caa3c2cab038a81cedfe16932ae0f90c248649774e3de82ff5f6278b9fe`. The assessment context digest remains `f30bf6128216ea6d8d4bbceada405c2fff126fa3f05433eeedfdd60b52122bdc`. These are supplied review bindings, not an independent cryptographic audit.

The reviewed files are `admission/strategy-reassessment-phase-modular-v2-draft.json` and `admission/strategy-reassessment-phase-modular-v2-context.json`, under `<workspace>/erdos-124/attack/`.

## Actual validator and the v1 defect

I inspected the installed `skills/math-solver/harness/search_controller/strategy_refresh.py`, including `_related_failures` and `record_assessment`, and `proof.py`'s `validate_review`. The source is from the installed Exactory 0.34.2 plugin, not a proposed replacement validator.

The validator distinguishes two obligations:

1. `considered_failure_ids` must contain every retained failure globally.
2. A row's `failure_resolutions` may contain only failures returned by `_related_failures` for that row's strategy. This predicate requires the same strategy name and at least one of the ancestor, account-lineage or claim relationships.

For a continuing row, the resolution IDs must equal the related-failure IDs. Each resolution must cite nonempty context evidence, with at least one checkpoint, acceptance, journal or run recorded after the failure. A same-node native failure cannot be cleared through this mechanism.

V1 placed all seven failures into node21's constructive resolution field. Six have different strategy names, so they fail the explicit guard with `Failure resolution does not match this strategy`. My v1 review missed this field restriction. It was a record-validation defect, not evidence that the mathematical comparisons should be removed.

Node8 is the only retained `make-the-proof-constructive` failure. Its inherited account-lineage relationship is preserved. The v2 singleton resolution therefore has the right scope. Node8's failure is recorded at revision158; the cited CP26 journal, checkpoint and acceptance are at revisions375, 376 and381, and CP22's acceptance is at301. The post-failure evidence requirement is met. Node21 is a distinct admitted node, not the failed node8 restarted under a cleared native flag.

I also reread the complete embedded accepted assessment-000004. Its constructive continuation uses only node8 in `failure_resolutions` while retaining all seven failures in the global considered list. This is consistent with the source-level interpretation, although the validator itself is the decisive evidence.

The packet records the rejected public submission and absence of a committed mutation. The coordinating agent reports that revision remains394. I did not query or change live controller state or replay the submission, so approval is not a report of end-to-end submission success.

## Verified narrow change

I read the complete v2 draft and compared both complete JSON packets structurally using their read-back contents. The standalone v2 draft equals the packet's proposed assessment. The differences are confined to:

- Node21's reason is extended with the six other-strategy failure IDs and their entire previous changed-input discussions.
- Node21's evidence list retains its original evidence and adds all seven retained failure IDs.
- Node21's resolution list retains exactly the original node8 resolution, including unchanged changed-input text and evidence IDs.
- The packet has the new subject digest and a `schema_correction` diagnostic.

The original contract, claim digest, full current context, all five previous assessments, accounts, admission authors, manual comparison, prescribed materials and reading limits are identical between packets. Within the proposed assessment, every other field is identical, including the 43 residual IDs, all seven global considered IDs, node14's entire row, both dispositions, native plan bindings, execution order, next action, complete hypothesis, success criterion and failure signal.

The six global comparisons moved; they did not disappear:

| Retained failed node and method | V2 location | Preserved substantive comparison |
| --- | --- | --- |
| node1, strengthen-and-generalise | Node21 reason, evidence list and global considered list | CP26's power-specific estimate is a new input; the failed all-input central initializer is not assumed. |
| node2, strengthen-and-generalise | Node21 reason, evidence list and global considered list | CP22's labelled lattice and CP26's estimate replace the abstract profile-to-seed inference; its counterexample remains. |
| node3, reduce-and-translate | Node21 reason, evidence list and global considered list | Each D uses its witnessing R and V; no fixed universal generating list is proposed. |
| node7, reduce-and-translate | Node21 reason, evidence list and global considered list | No Gaussian limit, coefficient positivity theorem or common scalar recurrence is assumed. |
| node8, make-the-proof-constructive | Node21 resolution, evidence list and global considered list | Each correction pays the CP26 one-label cost with a single ledger and a gap fixed before the first unit; fresh R supports remain outside V. |
| node15, attack-the-negative-side | Node21 reason, evidence list and global considered list | Only R supports shift, and V corrections use the actual modular-period orbit; no universal mixed-base normalizer is revived. |
| node18, ladder-the-parameter | Node21 reason, evidence list and global considered list | Individual V corrections do not require two disjoint whole mass-one base sets; the old limitation is not claimed to be generally defeated. |

Every relocated discussion is present verbatim, not merely replaced by its ID. The existing CP26 and CP22 evidence references supporting those discussions remain in the row. This is schema compliance without suppressing a gate or reducing substantive failure coverage.

## Substantive decision and limits retained

Node14 remains deferred: CP26 does not establish units for arbitrary subunit half-mass cores, its admitted constructive method is not its native first-ranked opening, and its original move account is exhausted. Node21 alone continues with its unchanged eligible constructive-first plan. Its preservation precondition remains unknown.

The proposed new input remains occurrence-level correction reuse. CP22 supplies a common-radix labelled lattice and disjoint-reserve amplification. CP26 supplies an all-scale one-label deletion interface. The new construction proposes selecting individual V powers as corrections and retaining the other powers of those bases. Their compatibility is a proof obligation, not already accepted input.

The single proposed computer-free application must retain V's original cutoff, finite-deletion charge, tolerance, gap and scale constants, fixed before the first correction, and one cumulative removed-weight ledger across every unit. It must justify the prefix interface without an unassumed gcd(V)=1, prove returns on the actual period-multiple orbit, obtain fresh legal R supports and a disjoint finite interval, and complete the all-cutoff finite-deletion amplification argument. Only R cutoffs may rise to avoid prior supports. Arbitrary-block deletion, restarted V ledgers, arbitrary syndetic intersections and modular fullness without legal finite identities remain unacceptable.

CP22 already restricts qualifying radices to two or three. Collective coprimality therefore does not add a case in which no individually coprime V base exists. The potential advance is retained correction-base mass, not that vacuous novelty claim.

The exact claim remains obligation-000052. Its complementary structural case053 and separate root bridge054 remain recorded. All 43 residual IDs are unchanged, including counterexample-bearing auxiliary assertions that cannot be used as premises. No general minimum-three result, equality case, arbitrary half-mass signed-unit theorem, T4=1 statement or original mass-one objective is closed. Neither approval nor the administrative correction changes proof status.

## Resources and authority

Account-000001 has `used_moves=24` out of `max_moves=24`. Account-000002 has `used_moves=4` out of `max_moves=24`, retains the same lineage owner and predecessor, and records 24 historical moves. Both accounts have `used_runs=0`, `historical_runs=0`, `reserved_moves=0` and `reserved_runs=0`. Move usage is not run usage.

This review provides no renewal, nonprogress reset, mathematical process, proof credit or automatic second analytical entry. The author must submit the new subject with this new review, obtain a fresh next instruction and satisfy the applicable begin and native checks before research. Freshness and acceptance remain the controller's responsibility at submission.

Only `admission/strategy-reassessment-phase-modular-v2-review.json` and its companion `.md` are written. The validator, controller, native files and old draft, review and submit records are not edited.

## Reading boundary and verification

This narrow review used source inspection, the complete v2 draft, the recorded diagnostic and structural comparisons of complete packet contents. It did not execute the validator or a controller command. The review JSON follows the actual five-key ResultReview shape with exactly the five required substantive findings and the supplied identity and bindings. Read-back checks verify the written artifacts and preservation of the old review files; they are administrative file checks, not mathematical runs.

The prior substantive review read the full prescribed context, all five previous assessments and seven failures, both current native plans and studies, manual frontier comparison2, CP26's complete proof artifact including Sections2-4, CP22's lattice/amplification/radix scope, and actual node8/node15/node18 failures. The unchanged packet retains that evidence. Closed-preflight summaries and query logs were sufficient under the clarified reading instruction. Relevant primary interfaces were read with their original limits; the return-time source was a saved extract, not a claim of reading the entire paper. This review does not assert exhaustive literature priority or recertify the transitive proof dependency closure.

No main-agent conversation, unrelated scratchpad, unbound progress report or prepared begin specification was inspected. No fresh theorem proof was attempted. The correction resolves the identified same-strategy placement defect on static inspection while retaining the full substantive approval and its limitations.
