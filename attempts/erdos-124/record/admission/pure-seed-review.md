# Independent admission review of proposal-000007

Decision: approve for analytical admission. This decision admits a risky, bounded proof attempt. It accepts no coefficient-positivity theorem, seed, implication bridge, or root result. I find no concrete blocking defect in the prescribed proposal and supplied evidence.

## Review binding and provenance

- Subject digest: `e06e549d6781d3f79461f1f8748e81f66219e2aa1af6bee29084cd2b545168d5`.
- Claim digest: `9a7dcd0f2fee86f88d2fe373e456ad4cd167a7c875eab1bedc109b569f5bbc28`.
- Reviewer source: `host`.
- Reviewer actor ID: `/root`, the actual agent name supplied by the host.
- Reviewer attestation ID: `01a07abe-138c-71e2-82ac-9c727bbee811`, the actual thread ID exposed by `CODEX_THREAD_ID`.

Both reviewer identifiers differ from the proposal author's identifiers, `codex-root-01a07806` and `session-01a07806-b2c5-7163-86d2-92fd0ef5cf33`. These are provenance records, not a claim that this document cryptographically authenticates intellectual independence. Controller validation remains separate.

I read the complete immutable packet in `admission/pure-seed-proposal.json` and all three referenced studies in `attack/preflight/pure-power-seed/`: `problem.md`, `novelty.md`, and `reduce-and-translate.md`. I also read the installed Exactory README and the prescribed Review schema. Relevant evidence inspected includes the studies' `sources/queries.md`, both saved Semantic Scholar failure responses, the canonical `sources/124.lean`, the BEGL96 introduction and main theorem, the Bergelson-Simmons Section 2 theorem statements and Cassels comparison, and Fan's saved Section 2 statements and arguments through Corollary 2.5. Source references below are relative to this research directory.

The supplied controller status and historical summaries define the review boundary. I did not independently audit earlier attack journals or controller state. No mathematical program, attack, controller mutation, or agent was started. An attempted read-only checksum command was blocked by the inspection hook; I did not bypass it. The binding digests and input-digest associations are therefore taken from the prescribed packet and user instruction, without an independent recomputation of the hashes.

## Root connection

The target is precisely obligation-000008: for each admissible fixed input there must be one endpoint loss L and represented central intervals at arbitrarily late prefixes. Accepted checkpoint-000009 supplies divergent all-future surplus only. It neither supplies the initial represented interval nor resolves this target.

The proposed connection is logically relevant: first fix the seed's L, then choose a seed prefix beyond the surplus threshold for that same L. The prospective propagation compares the represented interval with its translate by the next labelled occurrence. It must check adjacency or overlap at every subsequent prefix. This explains the target's usefulness without accepting the implication. Route-000003 still needs bridge obligation-000009 to reach C1, and route-000001 still needs bridge obligation-000003 to reach the full root. Both bridges remain unaccepted. Root eventual completeness is open even after this admission.

The ordering of quantifiers is essential. Arbitrarily late prefixes with a single fixed L allow the threshold choice. A loss L_m that changes with the prefix would not supply that argument. The explicit condition S_m >= 2L prevents vacuous coverage of an empty interval.

## Mathematical substance and method applicability

The target concerns exact integer coverage and retains the substantive unresolved difficulty. For the first m remaining labelled occurrences a_1,...,a_m, the polynomial P_m(z) = product_{i=1}^m (1+z^{a_i}) has a positive coefficient at z^n exactly when those occurrences represent n. Equal numerical powers with different labels require separate factors. An exact Fourier coefficient or a correctly normalized exponential tilt preserves this support information. These identities explain why the proposed image is relevant; they are elementary reformulations and provide no positivity estimate by themselves.

The study proposes to compare these exact images, check the pull-back with the full quantifiers, and attempt coefficient bounds that use the actual powers. This is a coherent analytical attempt that avoids the specific loss of integer support reported for the earlier real-image route. Its applicability is limited: no usable lower bound, local-limit theorem, or Fourier estimate is supplied. In particular, nonnegative coefficients do not imply that every required coefficient is positive, and neither total subset count nor a zero-frequency contribution excludes holes.

Admission does not require the unknown seed theorem to be proved in advance. The absence of that proof is consequently an execution risk rather than a blocking defect here. This judgment depends on the packet's explicit success and failure criteria: a coefficient restatement alone, or a conditional estimate that merely renames the original difficulty, earns no root progress. A sharper residual must add a checked mathematical restriction, estimate, or obstruction and retain its exact unresolved obligations. Recording a hypothesis does not accept it.

## Assumptions and scope

The domain remains every finite set of distinct integer bases D with d >= 3, collective gcd(D) = 1, and sigma(D) = sum_{d in D} 1/(d-1) >= 1; every positive cutoff k; and every finite labelled deletion F. The equality case sigma(D) = 1 is included. Collective gcd one must not be strengthened silently to pairwise coprimality. The loss L may depend on D, k, and F, but not on M or the subsequently selected m.

The proof must preserve the inherited prefix ordering, the remaining labelled occurrences after deletion, and their total S_m. It cannot silently replace them by a deduplicated set, powers beginning at exponent zero, mixed products of bases, or a convenient special base set. Using a higher cutoff or a selected substream would require an explicit transfer back to the required prefixes and central intervals. Finite deletion robustness is part of the target; a proof only for F empty would leave a stated obligation open.

The saved formal statement distinguishes the open positive-cutoff root from the solved zero-cutoff assertion and the special k = 1 example D = {3,4,7}. BEGL96's main theorem permits a cutoff-dependent finite subset of an infinite base sequence. None of these supplies the proposed all-D, all-k seed theorem.

## Imported results and novelty limitations

Bergelson-Simmons Theorem 2.2 states Cassels's dyadic condition as |A intersect [N+1,2N]| / log log N tending to infinity, together with squared-norm divergence for every nonzero circle parameter. For fixed finite D with d >= 3, each stream contributes at most one occurrence to (N,2N]. The dyadic count is therefore bounded by |D|, even before deletions. The required density condition fails. A direct application of Cassels is unavailable, independently of any question about its norm condition. Cassels's full original paper was not supplied as a checked proof source here.

The saved Fan Corollary 2.5 requires three pairwise disjoint infinite sets B_1, B_2, C, finite prefix deficit for each, and sum_{c in C} ||c theta|| = infinity for every nonzero theta in the circle. Corollary 2.3 instead states the irrational divergence and modular coverage requirements separately. The finite-support refinement reduces the number of components, but does not produce them for this problem. Whole-stream surplus gives no such partition. The rho-adic block-count hypothesis is also not established in the packet. Moreover, applying a theorem stated for sets to labelled streams requires a valid treatment of repeated numerical values and disjoint supplies. None of these results is an available all-input positivity engine.

The query log records a bounded search, not exhaustive novelty verification. Both saved Semantic Scholar responses report 429 errors. The strategy arXiv hit is unrelated, the problem arXiv hit addresses a different question, and the Crossref strategy lead is not Cassels's paper. The studies acknowledge these limitations. No located source proves this exact target, but that is not evidence of originality or publication readiness. Any surviving new theorem needs statement-specific novelty assessment and independent validity review.

## Equivalence and budget

According to the prescribed historical summaries, earlier early-seed repairs, real-image translations, and generic arithmetic-plus-surplus implications encountered specific obstructions. The generic implication has an accepted counterexample. This proposal does not repair that implication merely by naming a generating function. It instead retains the full power factors and targets the separate seed obligation left by the accepted surplus checkpoint. The method is sufficiently distinct for a bounded attempt on the supplied record, though its success remains uncertain. I make no broader claim of non-equivalence to uninspected attacks or literature.

The budget is inherited from account-000001. Eleven of twenty-four moves are used, leaving thirteen; there are no reservations or runs, and prior admitted nodes have finished or retreated. The proposal grants no fresh allowance and requests no renewal. Its max_moves value is the existing account ceiling, not twenty-four additional moves. The numerical run limits do not authorize computation: task.kind is proof and computation is null. The move ceiling and stagnation-window retreat criterion remain operative. No budget evasion is identified.

## Findings and remaining risks

The JSON contains all nine findings. Necessity is empty because this is not a finite computational task. Significance is empty because no standalone admission is requested. Renewal basis is empty because there is no renewal. Novelty is addressed because the requested assessment explicitly includes the limitations of the literature study.

There are no unresolved blocking objections to analytical admission. The unresolved nonblocking risks are the absence of a proved coefficient-positivity mechanism, the unmet hypotheses of neighbouring theorems, and the two unaccepted implication bridges. These remain proof obligations or execution risks and receive no acceptance from this review. Approval does not itself admit the node, reserve moves, accept a checkpoint, or close the root.
