# Binary-block mathematical result review

Verdict: approve the exact analytical result under the `reviewed` policy. The complete prescribed mathematical package was read, and no mathematical defect was found in its proof of the exact checkpoint claim. The initial provenance objection P1 is preserved below as review history and resolved using the reported host spawn identity, the independently observed matching thread identifier, and the exact provenance contract. The accompanying `binary-block-result-review.json` records this result approval. It does not constitute controller acceptance or a root proof.

## Review subject and boundary

The sole evidence package is `binary-block-result-review-context.json` and all ten artifacts enumerated by its manifest, resolved from `<workspace>/erdos-124/attack`. The reviewed node is `node-000013`, attack `erdos-124-binary-block-reserve`, and target obligation is `obligation-000025`. This is a result review of the supplied locally finished analytical candidate, not a review of proposal admission.

The context supplies these exact bindings:

- Stored checkpoint: `checkpoint-000019`.
- Full stored checkpoint digest, including its `id`: `ea6503d2b28f973d3ef696974434a7f2ddc63edddf0b7ba3612da307ca9967a3`.
- Exact Claim digest: `789757a19f66f0ab6cf2f3c8751aef32a01afc2615e5b802a0a3d904abb76a19`.
- Evidence manifest digest: `be2ef5ebfc05560c0653c822dca38f145d2daa763836f3a8f3749ed3782353d2`.
- Journal prefix digest: `a7331b5be3f833a2b80725dd8617394bd10ac3cb109ef58f8b1167e5d43c5bf4`.

These are supplied digest bindings, not a claim that this reviewer independently recomputed them. A read-only `shasum -a 256` command over the ten manifest files was rejected before execution by the installed PreToolUse hook with the reason "Unsupported managed shell operation; use a direct supported command or controller search run." No alternative execution route was used to bypass that rejection. Actual-byte digest verification therefore remains uncompleted in this review. No mathematical program, Exactory CLI command, lifecycle mutation, new attack, or evidence edit was performed.

The Codex README, math-solver wrapper, shared `SKILL.md`, and the relevant result, evidence and provenance sections of `SEARCH.md` were read directly. No author's transcript, private notes, admission reviews, predecessor proof files, or linked literature files were read. The prescribed journal and study artifacts were read as evidence within the explicit package.

## Original finding P1: provenance objection, subsequently resolved

The following records the initial finding and reasoning. Its conclusion is superseded by the resolution immediately below; its observations are retained.

The context identifies the author as:

```text
source: host
actor_id: /root
attestation_id: 01a07806-b2c5-7163-86d2-92e8e272b9eb
```

The present host context names this agent `/root`. A read-only environment inspection returned:

```text
CODEX_SESSION_ID=01a07806-b2c5-7163-86d2-92e8e272b9eb
CODEX_THREAD_ID=01a07e20-599d-7c52-aa3b-72a6be4c3f19
```

Thus the available actor name and session identifier both match the author's recorded values. The thread identifier is different from the supplied author session identifier, but it is explicitly a thread identifier. It does not establish a distinct actor or an independently attested reviewer session. Relabelling it as both fields, appending a reviewer suffix to `/root`, or inventing a new identifier would not provide host provenance.

`SEARCH.md`, "Review and provenance", requires: "The author and reviewers must have distinct actor IDs and attestation IDs." Its "Checkpoints and accepted results" section additionally states: "A local producer cannot supply its own result review." The shared math-solver `SKILL.md`, Stage 6, requires "independent result review" before proof credit. These are explicit requirements. Applying them to the observed identity collision is this reviewer's conclusion; this document does not assert that the user intentionally requested self-review or that the matching environment proves intellectual authorship.

The request describes an independent reviewer, and the proof was inspected without consulting the author's excluded material. Nevertheless, the available host records cannot support the required independent signature. This is an unresolved provenance defect, not a mathematical counterexample. The next review must have genuinely distinct host-supplied actor and session identities. The exact `ResultReview` schema permits only `decision: approve`, so a rejection object in that schema would be invalid. Accordingly, `binary-block-result-review.json` is not created.

## Resolution of P1

On reassessment, the user supplied the actual host spawn result: agent ID `01a07e20-599d-7c52-aa3b-72a6be4c3f19`, nickname Maxwell, with `fork_context:false`. This spawn result is reported by the operator in the conversation; I did not independently retrieve the original spawn-tool response. Separate read-only `printenv` calls under `/bin/sh` with `login:false` returned `USER=<user>` and `CODEX_THREAD_ID=01a07e20-599d-7c52-aa3b-72a6be4c3f19`. The latter directly corroborates the reported host agent identifier in this reviewer's environment. The operating-system username is not used as the review actor.

The original objection incorrectly treated the local agent name `/root` and inherited `CODEX_SESSION_ID` as the only permitted provenance fields. `SEARCH.md` defines both identity fields as Text and requires the reviewer's actor ID and attestation ID to differ from the author's respective fields. It does not require `attestation_id` to equal `CODEX_SESSION_ID`, require two different values within one reviewer's record, or prohibit a host-assigned agent ID as `actor_id`. A shared parent session variable therefore does not establish self-review. The reported separate spawn without forked context, this reviewer's observed thread identity, and the package-only mathematical inspection support the independent-review boundary required here.

The result review uses exactly:

```text
source: host
actor_id: 01a07e20-599d-7c52-aa3b-72a6be4c3f19
attestation_id: 01a07e20-599d-7c52-aa3b-72a6be4c3f19
```

The actor value is the reported actual host agent ID, independently corroborated as this thread's identifier. The attestation value identifies the actual reviewer thread in which this inspection occurred. The actor value differs from the author's `/root`; the attestation value differs from the author's `01a07806-b2c5-7163-86d2-92e8e272b9eb`. Their equality to each other violates no stated requirement. No suffix, synthetic identity, or claim to an unrelated session is introduced.

This is the explicit host/operator trust boundary documented by `SEARCH.md`, not cryptographic authentication of intellectual independence. The operator's spawn report and the directly observed environment value have distinct evidentiary roles, stated above. P1 is resolved without weakening the requirement for a separate reviewer or changing any mathematical finding.

The earlier hashing refusal is preserved as a verification limitation, and hashing was not retried. The ResultReview binds the full checkpoint and exact claim digests supplied in the prescribed context. It does not assert an independently recomputed digest or supply a ResultAudit. `SEARCH.md` assigns freshness, actual artifact checks and acceptance audit to the service before acceptance; this result approval does not bypass those checks. There is no unresolved mathematical or provenance defect in this review, and the existing mathematical findings below remain unchanged.

## Complete artifact coverage

Every file below was read completely. Paths are relative to `erdos-124-binary-block-reserve/` under the prescribed root.

| Artifact | Finding |
| --- | --- |
| `moves/001-binary-block-reserve.md` | Sections 1 through 8 were checked, including each lemma, the eight-row arithmetic table, all numeric constants, and the full quantified conclusion. The arithmetic table is reproduced below with its checks. |
| `units/consolidation.md` | The rewritten chain agrees with the proof. The broader direct reserve condition follows from the same argument. The proposed alternative presentation is correctly not called an independent second proof. |
| `units/INVENTORY.md` | The three mathematical candidates are supported by the proof. Publication disposition and historical comparisons supply no additional mathematical premise. Local closing is explicitly separated from independent acceptance. |
| `problem.json` | `claim` and `quadruple.statement` agree with the context's target statement. The quantifier and labelled-occurrence descriptions match the actual proof. Prior acceptances and literature are contextual comparisons. |
| `journal.jsonl` | The single move records the same proof chain, an empty deterministic-step list, and pending independent acceptance. Its local `closes` flag is not treated as acceptance. No lifecycle validation was performed. |
| `study/problem.md` | The study identifies the exact structural subfamily and the block, tail and reserve obligations subsequently discharged by the proof. |
| `study/make-the-proof-constructive.md` | The proof addresses the listed mathematical failure signals: alphabet coverage, distinct repeated labels, congruence and cutoff lifting, and sufficient reserve mass. Admission necessity and budget decisions were not reviewed. |
| `study/QUERY_LOG.md` | Recorded query limits, unavailable APIs and primary read boundaries were read. The record expressly does not establish exhaustive novelty. Its external search reports were not independently authenticated. |
| `study/REFERENCE_PATHS.md` | Resolves the study's historical source paths and states that the predecessor is not a dependency of the self-contained proof. No referenced file was needed to complete the mathematical argument. |
| `novelty.md` | The bounded novelty claim and preflight status are appropriately limited. No publication-priority conclusion is adopted here. |

## Statement, assumptions and scope

The exact checkpoint statement is:

> For every nonempty finite set D of distinct integers at least 4 with min D=4, {8,16} contained in D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=251/140, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

The context's checkpoint claim, target claim, manifest claim binding and `problem.json` agree in mathematical content. The quantifier order is every eligible finite D, every positive cutoff k, every finite labelled deletion F, then some N(D,k,F), then every integer n at least N, then a finite representation. There is no uniform threshold over inputs. The assumption-ID list is empty; this does not remove the explicit arithmetic hypotheses in the statement.

The proof uses elementary integer arithmetic, finite sets, geometric sums, finite modular cancellation and induction. Since 4 belongs to D, the gcd-one assumption guarantees at least one odd b in D. Such b is at least 5 and distinct from 4, 8 and 16. The hypothesis is used precisely here. The reserve itself needs no gcd-one assumption.

The result covers only the stated structural subfamily at reciprocal mass at least 251/140. It neither proves the original threshold-one objective nor all minimum-four cases. The direct condition with an odd b and residual mass at least one is a valid corollary of the proof, not a replacement for the checkpoint claim. No inference to the root or separate implication bridge is certified by this document.

## Mathematical findings

### 1. Fixed reserve and finite seed

Proof Section 1 correctly combines a g-syndetic reserve R with an interval `[A,A+g-1]` represented on a disjoint seed supply T. For `n >= A+g-1`, the interval `[n-A-g+1,n-A]` consists of exactly g nonnegative integers. A reserve sum r there makes `n-r` a seed sum. The two finite representations use disjoint labels.

The fresh-pair recursion excludes both alternatives of every previous pair. Therefore switching t of r pairs changes the total by t with no repeated label, producing `[A,A+r]`. Taking `r=g-1` is finite. The zero-pair case supplies `[0,0]` when g=1. The example using reserve values `g,2g,4g,...` correctly shows that g-1 consecutive seed sums do not suffice from gap information alone. Statements about each pair's increment refer to this guaranteed constructed interval and do not assert a maximum possible interval for the entire supply.

### 2. Signed interval lemma and complete arithmetic table

For a prefix with signed range `[-S,S]`, adjoining weight w produces three translated integer intervals. Their gaps disappear exactly under `w <= 2S+1`; their extreme endpoints are `-S-w` and `S+w`. This proves the lemma by induction while restricting each individual label to coefficients -1, 0 or 1.

The offsets for bases 4, 8 and 16 are respectively `{0,2,4,6,8,10}`, `{0,3,6,9}`, and `{0,4,8}`. There are 6+4+3=13 labels. The repeated weights arise from distinct bases. Every row in Section 3 checks as follows:

| Weight w | Copies | Sum S before first copy | 2S+1 | Row sum check |
| --- | --- | --- | --- | --- |
| 1 | 3 | 0 | 1 | 0+3=3 |
| 4 | 1 | 3 | 7 | 3+4=7 |
| 8 | 1 | 7 | 15 | 7+8=15 |
| 16 | 2 | 15 | 31 | 15+32=47 |
| 64 | 2 | 47 | 95 | 47+128=175 |
| 256 | 2 | 175 | 351 | 175+512=687 |
| 512 | 1 | 687 | 1375 | 687+512=1199 |
| 1024 | 1 | 1199 | 2399 | 1199+1024=2223 |

Every displayed w is at most its row's `2S+1`; subsequent copies only increase S. Thus the complete signed range is `[-2223,2223]`, which contains all 4096 integers of `E=[-2048,2047]`. No numerical deduplication or unrestricted coefficient is used.

### 3. Repeated blocks terminate

Section 4 uses the unique representative delta in E modulo 4096. For `1 <= q <= 2047`, delta=q and the next quotient is zero. For `q >= 2048`, `q-delta >= q-2047 > 0`. In every positive case the integer quotient satisfies `q' <= (q+2048)/4096 < q`, since `2048 < 4095q`. Nonnegativity and strict descent establish finite expansion by induction. In particular, the asymmetric endpoint q=2048 gives delta=-2048 and q'=1, which terminates. Negative integers are unnecessary for the unit construction; negating an expansion would still leave every block digit within the larger proved signed range.

### 4. Original exponents and legal tail units

For `e in {2,3,4}`, Section 5 assigns `(2^e,(L+12t+r)/e)` with `e|r`, `0 <= r < 12`, and L a positive multiple of 12 satisfying `L >= 4K`. The exponent is an integer at least K for every e. Its value is exactly `2^L 4096^t 2^r`. Within each base the half-open blocks are disjoint; across bases the labels differ even at equal numerical values. The normalized weight-one labels therefore become legal positive-exponent labels, not forbidden exponent-zero occurrences.

Odd b is invertible modulo `2^L`. Repetition among finitely many powers and cancellation give a positive period h with `b^h=1 mod 2^L`. A positive multiple J of h can be chosen at least K. Then `(b^J-1)/2^L` is a positive integer with a finite legal block expansion. Splitting signs gives `value(P)-value(negative labels)=b^J-1`; adjoining `(b,J)` to the negative side yields `value(Q)-value(P)=1`. P and Q are finite and disjoint, and every exponent is at least K.

Choosing K beyond every original exponent in a finite forbidden set excludes all its labels. Each subsequent pair excludes both earlier alternatives as well as the original deletion. This proves the required fresh-pair property for every cutoff and finite deletion, without a uniform bound on support size.

### 5. Reserve mesh, ties and equality

Section 6's finite-prefix mesh induction is valid. Translating a prefix subset-sum set preserves its internal gaps. Disjoint spans have intervening gap `a_i-S_{i-1}`; overlapping spans introduce no larger gap because their endpoints belong to the union. Since prefix endpoints tend to infinity, a gap bound of g implies a hit in every interval of g nonnegative integers, with the endpoint zero handled explicitly.

For each reserve base d, the strict-prefix geometric estimate also holds when x is exactly a power. If x exceeds `d^k`, take the least r with `d^r >= x`; the strict-prefix sum is `(d^r-d^k)/(d-1) >= (x-d^k)/(d-1)`. For `x <= d^k` the right side is nonpositive. Subtracting the total value of all deleted labels is a conservative lower bound, even when some deleted values exceed x.

Consequently `S_{i-1} >= sigma(B)a_i-C_B`, because every strictly smaller surviving label precedes a_i and earlier ties only increase the sum. Thus `a_i-S_{i-1} <= C_B` at `sigma(B) >= 1`. The choice `g=ceil(C_B)` is positive and finite. Finite deletion leaves an infinite locally finite reserve. The argument includes `sigma(B)=1` and preserves numerical multiplicities.

### 6. Mass and full quantifier order

Section 7's exact arithmetic is correct: `1/3+1/7+1/15=(35+15+7)/105=19/35=76/140`. The selected odd base contributes at most `1/4=35/140`. Hence `251/140-76/140-35/140=1`. The residual reserve B is nonempty and meets the lemma's hypotheses even at the stated boundary.

Fixing D,k,F determines b and B and their remaining labels. The reserve then determines g before any seed is constructed. Exactly g-1 fresh pairs determine A. Only after this does n vary. Taking `N=max{1,A+g-1}` yields every required representation with finite, disjoint surviving supports. This establishes the complete cutoff and finite-deletion quantifiers in the checkpoint statement.

## Dependencies, policy and final disposition

All mathematical ingredients needed for the theorem are proved in Sections 1 through 7 of the main artifact. The empty manifest dependencies, external dependencies, acceptance dependencies and route bindings are consistent with the actual proof. Literature and predecessor references in the other nine artifacts are contextual; their statements, novelty and priority are not necessary premises and were not independently certified here.

The argument is analytical and appropriate in substance for the requested `reviewed` policy. Its displayed finite arithmetic was checked directly, not by a mathematical execution. It provides no certificate-policy or Lean-kernel verification, publication-priority result, controller acceptance, or root proof. The immutable pending checkpoint status is not an error and is not changed by a review.

No mathematical correction to the prescribed proof is requested. P1 is resolved as recorded above, and the exact analytical result is approved in `binary-block-result-review.json`. Actual-byte digest checking remains uncompleted in this reviewer session due to the recorded hook refusal; no acceptance audit is asserted, and the service's mandatory checks remain in force. Only the two prescribed review outputs were changed. The proof, its evidence, the mathematical findings, and the checkpoint and claim bindings were not changed.
