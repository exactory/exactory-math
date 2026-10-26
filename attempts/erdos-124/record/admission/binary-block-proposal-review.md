# Independent proposal admission review: proposal-000013

Decision: approve for proposal admission only. The exact bounded analytical attack is substantive, plausible, and distinct from the accepted ranges supplied for comparison. No blocking admission objection was identified. The signed binary block and its tail lift remain unproved. This review neither accepts the proposed theorem nor executes its construction.

## Bound subject and provenance

- Proposal: `proposal-000013`, `erdos-124-binary-block-reserve`.
- Full supplied immutable proposal digest: `64888439401bb6f6c33aab584033533ffdd8b664f0ee4263371f58b736fc0307`.
- Exact supplied Claim digest: `789757a19f66f0ab6cf2f3c8751aef32a01afc2615e5b802a0a3d904abb76a19`.
- Reviewer source: `host`.
- Actual observed reviewer actor: `<user>`.
- Actual observed reviewer attestation: `01a07e0c-e47d-7ad0-88a6-4d5158683e6e`.

The reviewer fields were obtained from separate `printenv USER` and `printenv CODEX_THREAD_ID` commands in non-login `/bin/sh`, working from `<home>/exactory`. Both differ from the supplied author's fields, `/root` and `01a07806-b2c5-7163-86d2-92e8e272b9eb`. These are actual environment observations, not invented reviewer names. They do not cryptographically authenticate intellectual independence, establish a different human operator, or authenticate the author's supplied fields. The mandatory host/operator provenance audit remains required.

I read the installed Codex README first, then the shared math-solver SKILL.md, the relevant SEARCH.md claim, proposal, decomposition, review, account, computation and checkpoint rules, and the study, source, constructive-strategy and seed-and-amplify instructions. I read both prescribed admission JSON files and all four preflight studies completely. I read the complete predecessor proof, its supplied manifest and acceptance, the complete saved canonical 124.lean response, and the prescribed weighing-paper sections through source line 163, covering pages 1-4 and the next page header. The paper response also contains later material; it is not a premise of this assessment.

Additional source inspection covered the saved direct-access failures, the empty strategy batch, and displayed excerpts of the neighbouring-search batch. I did not independently inspect every search batch or repeat the literature search. No parent transcript or other review of this proposal was consulted. The predecessor acceptance and its embedded result review were read only as expressly supplied predecessor material.

The digests above and the predecessor artifact bindings are taken from the supplied context. I compared the proposed statements and records as text but did not recompute hashes, inspect the immutable store, replay controller history, or authenticate current acceptance freshness. Those checks remain service gates. A JSON-formatting read using `jq` was refused by the existing hook; ordinary permitted file reading supplied the source text. No gate was changed. No mathematical program, seed enumeration, Exactory CLI, lifecycle command, native mutation, or Lean build was run. Only these two requested review files were written.

## Exact scope and original formulation

The proposed theorem quantifies over every finite set D of distinct integers with minimum 4, both 8 and 16 present, collective gcd one, and reciprocal mass at least 251/140. For every positive cutoff k and every finite deletion F of permitted occurrence labels, it seeks an input-dependent N(D,k,F) and a legal finite representation for every n at least N. The named infinite scope is appropriate. There is no bound on the largest base, cutoff, deletion size, or represented integer. The requirements that 8 and 16 belong to D are essential restrictions, not examples that may be dropped.

In the saved [canonical declaration](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/124.lean), lines 28-30 define a finite set of exponents separately for each base. Lines 50-54 sum those sets of possible values over the finite base set in `Erdos124.erdos124.ne_zero`. Consequently, equal values arising from different bases remain independently usable. For example, `(4,6)`, `(8,4)` and `(16,3)` are distinct available labels even though their values agree. This does not allow a second use of any identical pair. The canonical positive-cutoff quantifiers agree with the root supplied here; the solved zero-cutoff declaration and the fixed cutoff-one example cannot replace them. No current repository status or formal proof is authenticated by reading this saved declaration.

Finite-deletion robustness is an explicit interface of the candidate. It must be preserved throughout its proof, but is not by itself a novelty argument. All choices controlling the eventual threshold must precede the choice of the represented integer.

## Mathematical substance and plausibility

The new question is whether the actual labels on bases 4, 8 and 16 support the proposed periodic signed alphabet and fresh unit alternatives at arbitrary depth. The accepted ternary argument does not supply this assertion. Its balanced ternary digit step specifically uses base 3, absent here. Replacing that step by an occurrence-preserving construction in binary-exponent blocks is a distinct analytical task.

The proposed alignment has a mathematical basis: the relevant binary-exponent multipliers are 2, 3 and 4, with common period 12. The inspected [Bolker-Feuer-Zara primary source](https://www.cs.umb.edu/~eb/weighing.pdf), Theorem 2, its finite-prefix and varying-multiplicity corollaries, the complement lemma and Theorem 3, supplies classical context for interval coverage by signed weights with bounded multiplicity. It supports investigating this mechanism. It does not verify the particular finite block, justify unrestricted coefficients, or prove the new tail theorem. Source indexing and multiplicity hypotheses must be handled explicitly in any application.

The following are existing success obligations of the proposal, not findings that they have already been met:

1. Specify the block boundary convention, actual occurrence multiplicities and exact balanced radix-4096 digit interval. Prove full integer interval coverage analytically. A sufficient total weight or a residue count alone is not coverage.
2. Prove a terminating finite expansion using successive blocks, including the chosen endpoints for the even radix. Account for each label at block boundaries and map binary exponents back to integer exponents for its original base. Coverage modulo 4096 alone is not the required finite expansion theorem.
3. Establish the odd-base congruence at arbitrarily high permitted exponents. Combine it with the expansion with correct signs, producing two finite disjoint positive alternatives whose values differ by one. Both alternatives must use only allowed original exponents.
4. Handle every finite forbidden set, including the union of both alternatives from every previous pair. Distinct numerical values are not a substitute for label bookkeeping. A single low-cutoff unit identity is insufficient.
5. Use a reserve chosen independently before constructing the interval. Prove that no seed or later pair consumes any reserve label, and retain its gap through the final amplification.

These are coherent, falsifiable analytical obligations, and the proposal expressly requires them while naming failure signals for them. Their unproved status is appropriate to admission review. I did not calculate the block's signed sums, construct a seed, prove the repeated-block theorem, or discharge the tail lift in this review.

## Odd base, threshold and reserve interface

The odd-base premise is justified by the stated inputs: because 4 belongs to D, an all-even D would contradict collective gcd one. Thus an odd b in D exists, with b at least 5 and different from 4, 8 and 16. Pairwise coprimality of all bases is unnecessary; no primality assumption on b is proposed.

The proposed mass accounting is correct:

    1 + 1/3 + 1/7 + 1/15 + 1/4 = 251/140.

For B = D minus {4,8,16,b}, subtracting the three fixed seed contributions and at most 1/4 for b leaves reciprocal mass at least one, including total-mass equality. This checks the proposed threshold's rationale; it is not a proof of the new seed theorem or of optimality. There is no need to assume gcd(B)=1.

The predecessor proof's Sections 1, 2, 4 and 5 provide the relevant general interfaces. Its bounded-gap lemma retains ties as labels; the geometric reserve lemma includes every positive cutoff, finite deletions and reciprocal mass exactly one. Its interval amplification requires g consecutive seed sums for the already fixed reserve gap g. Its fresh-pair argument uses g-1 pairs and excludes both previous alternatives. These statements apply to arbitrary disjoint labelled supplies under their stated hypotheses, unlike the base-specific ternary step. Once the new tail property is actually proved, they offer the claimed route to the proposed eventual conclusion. Thickness or signed units alone do not do so.

The supplied predecessor anchor is checkpoint-000018 with digest `47dca12bc7966f05b1d183f2da943bf8bf28dbcc9f95f35d23c18ebeeff5072b`; acceptance-000007 accepts obligation-000022 under reviewed policy. Its evidence digest is `5228299a26499d6d0c5e382ffc4c716571975c1d44f2114d1eb8ea2a15fc85bd`, and the manifest identifies the inspected proof with digest `d09878ba6988b7fff86b42343202f26816a02169d2ca2dfd08e4f9018e024e0d`. These supplied bindings are consistent. The checkpoint's immutable pending field and the proof's historical pending heading do not negate a separately recorded acceptance. Neither acceptance nor lineage transfers the unproved binary step. Freshness and any eventual dependency closure still require the controller's audit.

## Root connection, exhaustiveness and duplication

The new obligation is a premise of an explicit route to obligation-000001. For minimum 3, the ternary range covers mass at least 11/6 and the complement contains the lower range. For minimum at least 4, the quarter-mass range covers mass at least 3+min{1/4,2/m}; below it, the stated binary configuration is separated from its negation in the complement. Inclusive high boundaries and strict complementary inequalities agree. At minimum 3 the quarter-mass premise is redundant above the ternary threshold; this overlap causes no omission. Finite deletions in the stronger premises are set empty for the original assertion.

The proposed complement and bridge therefore have the intended exhaustive logical scope on the supplied root domain. This is a proposal-level scope assessment, not an accepted bridge proof. The complement and separate bridge remain open obligations, and every required route premise still needs accepted proof. No coverage percentage is justified for this named infinite domain.

The candidate is not a semantic copy of the supplied accepted ternary theorem, which requires minimum 3, or the quarter-mass theorem, whose minimum-4 threshold is 13/4. The block construction is also not merely the predecessor reserve lemma renamed. Its intended contribution is the lower threshold for this specific minimum-4 family. The supplied comparison material supports an empty equivalent-node list; I did not audit every historical node in the controller.

The complete studies record both problem-level and strategy-level tier-one queries, neighbouring searches, primary reading and a fixed-count stop. The saved direct requests show four reader access errors and a 403 for the problem page; these are not negative literature results. The search log's numeric queries are noisy and much material was inspected only as snippets. No exact duplicate is identified in the prescribed material, which suffices for this bounded internal main-route proposal. Exhaustive novelty, publication priority and novelty of signed positional arithmetic are not established. The remaining saved search batches were not independently re-audited here.

## Budget and retained gates

The supplied account-000001 has 24 allowed moves, 18 used, zero reserved, and six remaining. The proposal inherits this account with null renewal bindings. Its template limits of 24 moves, 24 runs, 300 seconds and one worker cannot create a fresh 24-move allowance or increase the inherited account. The constructive seed branch allows at most two seed-and-amplify applications, subject to the shared remainder and earlier failure. The three-move stagnation criterion does not permit continuing a strategy after its failure signal fires.

This is version-2 `task.kind: proof` with `computation: null`. No enumeration, checker run or other mathematical process is admitted by the nonzero template run limit. A later computation would require its own reviewed authority. The predecessor checkpoint supplies lineage and reusable evidence, not renewal, refund or reset. An accepted exact new range may be substantive progress; a recorded failed-block hypothesis alone earns neither proof acceptance nor renewal credit. Neither kind of checkpoint independently triggers native cash-out.

Admission, current-account and remaining-resource checks, native planning, move reservation and journalling, failure handling, checkpoint identity, independent result review, evidence freshness, exact bridge acceptance and root closure all remain mandatory. This review authorizes none of their mutations. The final assessment is approval of the exact proposed bounded attempt, with no unresolved admission objection and with all stated proof obligations still required.
