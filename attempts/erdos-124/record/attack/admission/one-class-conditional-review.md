# Admission assessment of proposal-000017

Decision: approve, following the provenance clarification documented below. The initial unsubmitted decision was revise solely because of an apparent actor collision. On the supplied mathematical and resource documents, I find the proposed two-application conditional plan coherent. The intended implication is a routine corollary of the existing correction method with a useful exact input audit. This assessment does not accept a proof, assert WOC, authorize research, or grant renewal.

## Provenance and binding limitation

Original concern, preserved: the environment displayed the agent name `/root`. The first shell command in this review was a direct `printenv CODEX_THREAD_ID`; it returned `01a07f2a-2cca-7b23-a830-091ddb5c27b2`. I initially used `/root` as actor_id and the observed UUID as attestation_id.

The proposal records author actor `/root` and author attestation `01a07806-b2c5-7163-86d2-92e8e272b9eb`. Under my initial mapping the attestations differed but the actors did not. [SEARCH.md, Review and provenance](<home>/.codex/plugins/cache/exactory-ai/exactory/0.34.2/skills/math-solver/SEARCH.md:699) requires: "The author and reviewers must have distinct actor IDs and attestation IDs." I therefore marked the initial report revise and said it could not serve as the required independent approval. That was a provenance objection, not a mathematical objection. Inventing a replacement name would not have resolved it.

Resolution: the coordinating agent, reporting its host spawn_agent response, subsequently supplied the assignment identifying this reviewer as agent_id `01a07f2a-2cca-7b23-a830-091ddb5c27b2`, nickname `Banach`, and explained that `/root` is the shared environment display name. That coordinating agent called spawn_agent and send_input and also reported that the initial review had not been submitted to the controller. The clarification came from the coordinating agent, not the human user. I reassessed only provenance and ran a second direct `printenv CODEX_THREAD_ID`, which returned the same UUID. I did not independently retrieve the spawn_agent response; the agent-to-thread mapping is the host assignment reported by the coordinating agent, corroborated by my own direct thread observation.

SEARCH.md permits host/operator-supplied provenance records and delegates validation of that boundary to the service. On this evidence, the supplied unique host agent identifier can faithfully serve as actor_id. It is an existing identifier for this reviewer, not a newly chosen nickname or another actor's identity. The JSON now records `source: host` and uses `01a07f2a-2cca-7b23-a830-091ddb5c27b2` for both actor_id and attestation_id. The reviewer actor differs from author actor `/root`, and the reviewer attestation differs from the author main thread. The contract requires these distinctions across author and reviewer; it does not require the two fields within a single reviewer to differ. The nickname is explanatory metadata only and is not used as an identifier.

The original blocking objection is therefore resolved for this unsubmitted document assessment. Decision changes to approve; all nine findings, mathematical qualifications, budget limits, and supplied digests remain unchanged. The service must still authenticate the reported host assignment and apply its normal provenance audit. This report does not claim that I personally observed the creation response or that an editable JSON field authenticates independence. If the service cannot validate that assignment, this clarification does not authorize bypassing its rejection.

I did not read parent conversation, other reviewer reports, private scratch, or private notes. During the provenance amendment I reread only the relevant SEARCH.md section and the affected portions of my own two unsubmitted files. No mathematical or resource-scope reassessment was performed.

The JSON uses these supplied public-registration values:

- Proposal subject: `a4579d5243312917e9500b284d9ac28bbeeb5363bab62df3dc7cb29fcba74dde`.
- Claim: `45dbe119d103e69f8b4bc8d261fa45fd9f0d8d42908ff7028e207f7343c3003e`.

I read the proposal content but did not recompute these values or authenticate the hashes of studies and accepted evidence. I did not use `shasum` or a substitute hashing workaround. The service's metadata, provenance, immutable-content, and dependency audits remain necessary. No review or admission CLI was run.

## Mathematical assessment of the intended implication

Write `delta=min{1/8,1/m}`. The relevant inherited statements are intermediate lemmas, not merely the old final mass thresholds. Quarter Section 2 supplies a minimum-preserving gcd-one core with mass in `[1,9/8)`. Core supplies one with mass in `[1,1+1/m)`. Use the former when `m<=8` and the latter when `m>=8`; either works at `m=8`. Thus the planned allocation can select `C` containing `m`, with gcd one and `1<=sigma(C)<1+delta`.

For the complementary base set `E=D minus C`, the intended calculation is

    sigma(E)=sigma(D)-sigma(C) > (2+delta)-(1+delta)=1.

Every base in E is at least `m+1>=4`. These are exactly the WOC restrictions. The strict upper bound for the core preserves the inclusive endpoint for D. No choice of two different cores satisfying simultaneous unrelated conditions is required.

I read Quarter's core argument, including its large-seed obstruction and minimum-three cases, and Core's gcd descent and first-crossing argument. I found no gap relevant to these uses. Their accepted status is reported by the sanitized context; I have not independently audited the controller's immutable acceptance records. A later result must explicitly bind acceptance-000001, acceptance-000005 and acceptance-000006 as appropriate dependencies and identify the intermediate lemmas used. The empty inherited_evidence list in this proposal is not an acceptance of those dependencies. Its checkpoint-000022 anchor is a lineage link, not the mathematical source of the core bounds.

For arbitrary k and a finite labelled deletion F, choose `k'>=k` larger than every deleted exponent, or use `k'=k` when F is empty. Both supplies can be restricted to exponents at least k'. WOC quantifies over every such cutoff, so it supplies the intended input without an explicit deletion clause. Ignoring the other available occurrences is allowed. This observation does not reduce the assertion to k=1 and does not require a threshold uniform in D,k,F.

WOC explicitly requires an open U meeting `K=closure{n*theta:n in Z}`. This is the right nonvacuity condition. Rotation by theta is minimal on K, so the return times to the relatively open nonempty `U intersect K` have bounded gaps. They meet a positive thick J arbitrarily far out. K need not be the ambient torus, theta need not be irrational, and U need not contain zero. The inherited argument needs none of these stronger conditions.

Mass Sections 3.2 and 5.2 give the needed phase-closure argument for the correction supply on C. For every nonzero beta, the norm sum over its surviving labelled powers diverges. The recurrence in Section 5.2 handles rational as well as irrational beta using collective gcd one. Section 3.2 then obtains K as the intersection of the closures of tail finite-sum phases. It uses finite labelled supports beyond earlier supports, so repeated numerical values do not invalidate the semigroup argument.

The intended finite correction in Mass Section 3.3 applies to the one WOC supply with the following support audit. For each x in K, the relatively open set `x-(U intersect K)` meets the dense correction phases. Compactness therefore supplies finitely many correction sums u whose translates `u*theta+U` cover K. Choose one finite support for each u and let L be their finite union. Different candidate corrections may share labels, since a single representation uses only one candidate correction.

Let M be the largest chosen correction sum. The set of n with `n>M` and `n-h in J` for every integer `0<=h<=M` is positive thick: sufficiently long positive intervals in J survive the finite trimming and removal of any bounded initial portion. Each such n selects a correction u with `(n-u)*theta in U`; WOC supplies the positive remainder on E. Its support is disjoint from L because the base groups are disjoint.

Only after L is fixed does the argument choose the gap g of the C supply minus L. Mass Sections 2 and 5.1 retain bounded gaps after this finite label deletion. The thick represented set on E together with L then supplies g consecutive sums. The final reserve uses C minus L, so the amplification in Mass Section 1 has disjoint supports. It does not spend the same correction labels twice or assume that the original Bohr intersection itself is thick. All these checks concern the intended implication; they neither establish WOC nor constitute a result acceptance.

## Scope, substance, and bounded execution

The proposal preserves the unconditional target at `2+min{1/8,1/m}`. Its two proposed analytical applications aim first at the OC-conditional form and then at the WOC-conditional form. The installed strategy expressly separates those two actions. Recording the final restricted bridge once is a reasonable way to identify the precise missing input. Treating the two formulations as separately substantial discoveries, or as repeated renewal grounds, would not be warranted.

The conditional corollary is routine relative to the inspected correction and core lemmas. It has modest value as an exact reduction and support audit. The material does not justify standalone publication significance, optimality of the threshold, or a priority claim. No equivalence between OC or WOC and the high-mass target is established. The supplied older high-mass theorem and structural common-radix theorem are different scoped conclusions; the proposal does not silently substitute either for an arbitrary-base input.

The root route has the inclusive high-mass range and the strict lower-mass complement as premises. These exhaust the original domain, using F empty on the high-mass side. Its implication bridge remains an acceptance obligation. The internal route separately requires WOC and the exact WOC-conditional bridge. Accepting that bridge alone cannot close the unconditional node or the root. Keeping assumption_ids empty on the bridge proposition is coherent because the WOC antecedent is written inside the implication; it does not authorize assuming WOC as an established execution prerequisite.

The sanitized account records 22 used moves out of 24, no reservations, and no runs. The proposal explicitly inherits that account and plans at most two analytical applications. The ordinary node limit of 24 does not replenish the shared account. At exhaustion, the declared account move-limit predicate can justify a truthful controller retreat. It does not imply that this newly created native workspace has reached a native stall or cash-out trigger. The proposal correctly preserves that distinction.

Leaving WOC open is neither a counterexample nor by itself evidence that an entry failure signal fired. The present record does not manufacture a failure to obtain a handoff. A later restricted-input investigation would need its own claim, studies, review, admissible method and valid account. If the shared account is exhausted, this proposal supplies no authority for another move. No renewal basis has been requested or approved. The JSON therefore leaves renewal_basis empty; necessity and significance are also empty because this is neither a finite-task admission nor a standalone-significance admission.

## Inspected material and remaining limits

Paths below are relative to `<workspace>/erdos-124/attack` unless specified otherwise.

- The exact `admission/one-class-conditional-proposal.json` and `admission/one-class-conditional-review-context.json`.
- All four studies under `preflight/one-class-conditional/`: `problem.md`, `work-conditionally-then-discharge.md`, `novelty.md`, and `QUERY_LOG.md`; also `sources/query-inputs.json`.
- The saved primary responses `sources/oc17primary0.txt` and `sources/oc17primary1.txt` in that preflight directory, including the Griesmer statements and Host-Kra theorem excerpts. I inspected relevant passages and search matches in `oc17problem0.txt`, `oc17problem4.txt`, `oc17strategy0.txt`, `oc17strategy4.txt`, `oc17neighbours0.txt`, and `oc17neighbours4.txt`. Unrelated hits were not treated as mathematical support or exhaustively reviewed.
- The complete inherited `erdos-124-mass-partition/moves/001-high-mass-completeness.md`, especially Sections 1-3 and 5; the complete `erdos-124-quarter-mass/moves/001-quarter-mass-completeness.md`, especially Section 2; and `erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md`.
- The positive-cutoff canonical statement in `preflight/mass-partition/sources/canonical-124-reading.txt`, including source lines 43-54. Its per-base sum preserves occurrence multiplicity. This is a statement comparison, not a Lean verification.
- The local primary text `<workspace>/erdos-124/sources/bergelson-simmons.txt`, Definition 1.26 and Section 2.1 around Lemma 2.12 and the compact-group correction argument. The common-radix acceptance's exact claim was read in the sanitized context; its proof was not needed for this bridge and was not independently reviewed here.
- The installed Codex README was read before the Exactory skill. I read the Codex math-solver entrypoint, shared SKILL.md, the relevant SEARCH.md proposal, provenance, decomposition, resource, checkpoint, retreat and computation-admission sections, and the selected strategy and entry instructions.

The primary responses support the studies' caution: Host-Kra requires a dual-set property not established for these finite-sum sets, and Griesmer requires an averaging input and another positive-density summand not allocated here. Bergelson-Simmons supplies a two-syndetic theorem, not a theorem about one arbitrary syndetic power supply. The relevant Fan mechanism was assessed through the self-contained inherited Mass argument; I did not conduct a fresh full-paper review of Fan.

The saved searches are bounded domain-filtered discovery rather than exhaustive database searches. I did not repeat web queries, authenticate retrieval dates, or verify priority. The studies bear a September 8 date whereas the supplied local environment date is September 7; this assessment makes no timestamp-authentication claim. Search snippets and extracted text contain formatting defects, so the exact target and inherited analytical arguments were used for the mathematical comparison.

No controller mutations, native writes, mathematical experiments, finite-question programs, formal checks, public posting, or Exactory CLI calls were performed. Only the two requested review files were written and amended with apply_patch. There is no remaining blocking objection in this assessment after the documented identity clarification. Approval is limited to this conditional research plan and remains subject to the service's provenance and metadata checks and the ordinary later evidence audits.
