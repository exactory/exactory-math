# Independent result review of checkpoint-000023

Decision: approve the exact WOC-conditional implication for outcome `proof` on `obligation-000037`. No blocking mathematical gap was found. This decision concerns the implication, not the truth of WOC or an unconditional representation theorem. The accompanying JSON is the closed public accept specification with a `ResultReview`; it is not a completed service acceptance.

## Independence, provenance and limits

The first shell command was the direct command `printenv CODEX_THREAD_ID`. It returned `01a07f41-a636-7d32-b284-c631e3627747`. The coordinating agent subsequently reported that its host `spawn_agent` response assigned this same unique agent ID, with nickname Dirac, and that it sent the clarification to that exact target. The reviewer uses that existing host identifier as `actor_id` and the independently observed thread identifier as `attestation_id`, with `source: host`. The clarification came from the coordinating agent, not from the human user. The shared display label `/root` is not used as reviewer identity. The context identifies the author as actor `/root`, with a different attestation ID, `01a07806-b2c5-7163-86d2-92e8e272b9eb`.

I did not read parent conversation, private notes, author scratch, or prior admission or result reviewer reports. I read the supplied result context, exact candidate manifest, its proof and supporting artifacts, the inherited proofs and relevant immutable dependency manifests. No mathematical program, hash command, formal checker, Exactory CLI mutation, native mutation or external write was performed. Only the two requested review files were written.

All digests in this review are supplied bindings. I did not independently compute cryptographic hashes or authenticate the host through a new identity mechanism. The service must perform its normal provenance check, frozen-byte audit, journal/milestone audit and freshness audit of the complete immutable dependency closure. Reading a working proof path does not independently establish that it equals the frozen bytes. This review assesses the mathematical content presented under those bindings.

## Exact statement and quantifiers

Write `sigma(A)=sum_{d in A}1/(d-1)`. WOC quantifies over every nonempty finite set E of distinct integer bases at least four with sigma(E)>1, and every positive integer cutoff. For each such input it supplies a finite dimension r>=1, a torus point theta, an open U meeting K=closure{n theta:n in Z}, and a positive thick set J. Every n in J with n theta in U has a representation by a nonempty finite set of labels from E at that cutoff.

The consequence quantifies over every nonempty finite D of distinct integers at least three satisfying gcd(D)=1 and

    sigma(D) >= 2 + min{1/8,1/min D},

every positive k, and every finite set F of allowed labels. It asserts existence of N(D,k,F) such that every integer n>=N has a finite representation using labels (d,j) with d in D and j>=k outside F, each label at most once. Numerically equal values from different labels retain their separate capacities.

The candidate proves this whole implication. It does not prove WOC, replace its existential witnesses by uniform ones, or prove the consequent before assuming WOC. The empty `assumption_ids` of the implication are consistent with its proof in ordinary classical mathematics: its antecedent is part of the proposition being proved. The native problem still states the unconditional target and remains undecided; its journal does not claim local closure. Acceptance here instead targets the exact separately stated implication in the supplied stored checkpoint and obligation.

## Core selection and the inclusive mass endpoint

I checked the Core proof in full. Starting from {m}, each added base strictly lowers the current gcd until it is one. After the first addition the gcd is at most floor(m/2), so the number q of additions is at most floor(m/2). The seed has at most m-1 elements for m>=3, and at least one exceeds m. Its reciprocal mass is therefore strictly below its cardinality divided by m-1, hence below one. Adding bases until the first mass crossing preserves m and gcd one. The last base differs from m, so its weight is at most 1/m; the mass before crossing is strictly below one. This proves the strict upper bound 1+1/m without a pairwise-coprime hypothesis.

I also checked the sharper Quarter Section 2 lemma, not merely its final completeness theorem. If the first crossing ends at a base at least nine, its last weight is at most 1/8. A seed containing a base larger than eight can only have reached that choice when a nontrivial current gcd divided every available base at most eight. The five small-minimum rows then bound all possible early-crossing mass below one. Their rational totals and strict inequalities are correct. When the seed is small and m>=4, the full mass of {4,5,6,7,8} is 153/140<9/8. For m=3 the least eligible seed base is exactly one of 4,5,7,8. The listed first-crossing alternatives exhaust the possibilities; their largest relevant crossing, 67/60, is still below 9/8. In particular the case crossing at seven correctly does not charge a later eight. Thus the lemma preserves m and gcd one while giving 1<=sigma(C)<9/8.

For delta=min{1/8,1/m}, choose this Quarter core when m<=8 and the Core bound when m>=8. At m=8 either choice works. No common optimizer for two different selections is required. In all cases

    m in C, gcd(C)=1, 1<=sigma(C)<1+delta.

Consequently E=D minus C is nonempty and

    sigma(E)>1, min E>=m+1>=4.

The inequality remains strict when sigma(D)=2+delta. The target's inclusive endpoint is therefore retained, and the precise restricted WOC domain suffices. No gcd restriction on E is added.

## Positive cutoff and finite deletion

For F empty, the proof uses q=k. Otherwise it uses q=max{k,1+max{j:(d,j) in F}}. Finiteness makes q a finite positive integer, and every label at exponent at least q lies outside F. This removes finitely many additional available labels, which is legitimate for an existence assertion.

WOC is applied to E at q with no explicit deletion. The proof never needs WOC at base three or at reciprocal mass exactly one. It never fixes the cutoff at one, assumes a uniform threshold over cutoffs, or uses a deleted label in a later correction. The resulting N may depend on the chosen witnesses for E,q; existential quantification permits those choices to be made after D,k,F are fixed.

## The inherited gap and phase lemmas

Mass Section 5.1 gives, for each base d and real x>0,

    sum_{j>=q, d^j<x} d^j >= (x-d^q)/(d-1).

This is also correct at an exact power: the geometric prefix stops strictly below x. Summing over C and subtracting any finite deleted value total bounds the ordered deficit of the surviving supply. Earlier labels with the same numerical value only increase the available preceding sum, so the strict numerical prefix is a valid lower bound in any tie order.

Mass Section 2 proves that a positive integer ordered-deficit bound g gives gaps at most g for every finite-prefix subset-sum mesh, including its endpoints. The induction on T union (a+T) handles both disjoint and overlapping spans. Unbounded prefix endpoints then imply that every interval of g consecutive nonnegative integers meets the full sumset. Deleting labels of total value W changes the bound to at most g+W. This is a statement about labels, not a deduplicated sequence of values.

I checked Mass Section 5.2 independently. If ||beta d^j|| tends to zero, nearest-integer errors satisfy e_{j+1}=d e_j eventually, since their recurrence discrepancy is an integer tending to zero. An eventually expanding error sequence can tend to zero only if it is eventually zero. Hence beta d^J is integral. If convergence held on the full correction supply, this conclusion would hold for every d in C. A prime in the reduced denominator of beta would then divide every base in C, contradicting gcd(C)=1. For every nonzero beta the norm terms therefore fail to tend to zero, so their nonnegative sum diverges. Finite label deletion does not affect this conclusion.

Mass Section 3.2 obtains the required density from precisely this divergence. Let G_t be the closure of phases of subset sums supported in the t-th tail, and G their nested compact intersection. Two points of G can be approximated with disjoint successive finite supports, proving closure under addition. For x in the resulting compact semigroup, a convergent subsequence of positive multiples with successive indices separated by at least two gives positive multiples tending to -x. Thus G is a subgroup.

If theta were outside G, closed-subgroup character separation in the finite-dimensional torus would give an integer character chi annihilating G and beta=chi(theta) nonzero. Among signed representatives of beta times label values, one sign has divergent absolute sum. In every tail, stop that sign's partial selection when the absolute sum first reaches 1/4. Because each summand has size at most 1/2, the total lies in [1/4,3/4], so its character norm is at least 1/4. A convergent subsequence of these tail sums lies in G and has the same lower bound on character norm, a contradiction. Hence theta lies in G and G=K. This argument covers rational characters and finite or disconnected orbit closures as well as irrational ones.

These are the actual intermediate results needed here. The final higher-mass theorem of Mass alone would not justify their use at the candidate threshold.

## Nonvacuity, finite correction and amplification

The clause U intersect K nonempty is essential and is retained. The closure of the nonnegative orbit is a compact subsemigroup containing theta and hence equals K. Every forward orbit from x in K therefore meets U. Compactness selects finitely many nonnegative waiting times covering all starting phases, giving bounded waiting time for positive returns to U. Thus the return set intersects positive thick J unboundedly. This argument does not claim that this intersection is thick.

Density of correction phases in K implies that every relatively open set x-(U intersect K) contains a correction phase. Accordingly the translates u theta+U, for u in FS_0(Q_C), cover K. Compactness selects a nonempty finite set V of such numerical sums. Choosing one finite label representation for each u, and taking their finite union L, fixes the correction support. M=max V is a finite nonnegative integer. This remains valid if 0 belongs to V, if theta=0, if U misses zero, or if K is a proper subgroup of the torus.

For n>M whose previous M shifts all lie in J, choose u in V with (n-u)theta in U. Then n-u is positive and in J, so WOC represents it on Q_E. Adding the chosen representation of u uses Q_E union L legally. Different alternatives u may share labels, since only one is selected for each n.

The set of such n is thick: an interval in J of sufficiently large length survives trimming M positions from its left side and any bounded initial part. This gives thickness on Q_E union L before a reserve gap is chosen.

Only after L is fixed does the proof set

    g=ceil(sum_{d in C} d^q/(d-1)+sum_{ell in L} value(ell)).

This is a finite positive gap bound for FS_0(Q_C minus L). Thickness supplies an interval [A,A+g-1], A>=1, represented on Q_E union L. For every n>=A+g-1, the interval [n-A-g+1,n-A] consists of g nonnegative integers and contains a represented reserve value t. The value n-t lies in the fixed interval. Its support and the reserve support are disjoint. Their union represents n on legal original labels, establishing N=A+g-1.

The ordering of choices is correct and contains no dependence on an as-yet unchosen gap. Labels in L are removed from the reserve. Labels from C and E differ by base. Equal numerical values across these groups are not identified. The final representation uses each ordered pair at most once and, since n is positive, is nonempty even when the reserve or correction value is zero.

## Dependency and binding audit

The supplied candidate manifest is analytical and binds outcome proof, exactly three accepted dependency IDs and the exact route binding reproduced in the JSON. Its two proof artifacts jointly provide the OC argument and an explicit repetition using only WOC. The latter imports the unconditional correction steps, not the truth of OC.

I inspected the three inherited manifest blobs. Core has no manifest dependencies; Mass depends on Core; Quarter depends on Core and Mass. This is an acyclic analytical closure. I read the complete main proof of each, plus both additional consolidation proof artifacts listed by Mass and Quarter. The required intermediate statements are present in those proofs with their derivations. There is no circular reliance on the candidate, no additional assumption on the core, and no missing computational certificate.

The published two-syndetic input in Mass is present in its pinned Bergelson-Simmons source at Lemma 2.12, which I inspected with the adjacent compact-group argument. That input explains the inherited full theorem, but is not a theorem about one syndetic supply. In the present implication WOC directly supplies the needed one-class input; the proof does not invoke the two-syndetic theorem to establish WOC. Fan's method is explicitly proved on labels in Mass. Common-radix results and the Host-Kra and Griesmer material mentioned in the studies are not additional mathematical premises of this implication.

Bindings copied from the supplied context and manifests, without recomputation:

- Stored checkpoint: `checkpoint-000023`; digest `93cbb0ea5f738b14d8c36d261bf263866f2754429980ee7890d17bc10fdcbb59`.
- Exact claim digest: `23de60fc2b7ad598fa0a18d2861ef756bc46f1153aac24f91b3925be50c270d3`.
- Candidate evidence digest: `80c38432c8004dcb8958fd7860f87d6b246fd9c2fc872034190f1901127ed856`.
- Core: `acceptance-000001`, evidence digest `3e7c431c41912315994774e1ac3338ce3f47919d6677ff4394db38a9a9c40882`.
- Mass: `acceptance-000005`, evidence digest `49c309e171825be70b3a3c683d9154b0d2871e2e0c22c82a36fcf628ec706d53`.
- Quarter: `acceptance-000006`, evidence digest `ab59ab3fee5a4a4b9d8739030f497e216c4bbacb770525958dba5cda1ad0f884`.
- Route: `route-000013`; digest `631757df6833655b42162b63c4e7916d4dbeded8436c2d022950a2b0774bc8bf`; no cases; shared prerequisite `obligation-000036`; no discharged assumptions.

The public spec has `inputs: []`. It supplies neither an internal `ResultAudit` nor an invented acceptance ID or progress flag. The subject binding is to the complete stored checkpoint including its ID, as supplied, rather than to the manifest or a checkpoint-input record.

## Remaining obligations and budget

Approving outcome proof for a reduction checkpoint is appropriate here because its exact target is a proved implication. This does not discharge its route premise. WOC `obligation-000036`, unconditional high-mass target `obligation-000035`, lower-mass complement `obligation-000038`, root bridge `obligation-000039` and original objective `obligation-000001` remain unproved by this review.

The supplied account records 24 of 24 moves used. SEARCH.md permits reading and accepting existing immutable evidence after exhaustion, while a new verification workload or research move requires its own remaining authority. This review ran no such workload and changes no account. It does not approve automatic renewal, duplicate progress credit, publication significance, or a native cash-out. The mathematical contribution assessed is a routine explicit conditional corollary with an exact input restriction; no independent publication-priority determination was made.

## Inspected paths

The following paths are relative to `<workspace>/erdos-124/attack`, except where absolute. Candidate and main inherited proof files were read in full. No prior review file was opened.

- `admission/one-class-conditional-result-context.json`
- `preflight/one-class-conditional/evidence-manifest.json`
- `erdos-124-one-class-conditional/moves/001-oc-conditional-bridge.md`
- `erdos-124-one-class-conditional/moves/002-woc-restricted-bridge.md`
- `erdos-124-one-class-conditional/journal.jsonl`
- `erdos-124-one-class-conditional/problem.json`
- `preflight/one-class-conditional/problem.md`
- `preflight/one-class-conditional/work-conditionally-then-discharge.md`
- `preflight/one-class-conditional/novelty.md`
- `preflight/one-class-conditional/QUERY_LOG.md`
- `erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md`
- `erdos-124-mass-partition/moves/001-high-mass-completeness.md`
- `erdos-124-mass-partition/units/consolidation.md`
- `erdos-124-quarter-mass/moves/001-quarter-mass-completeness.md`
- `erdos-124-quarter-mass/units/consolidation.md`
- `erdos-124-mass-partition/study/REFERENCE_PATHS.md`
- `erdos-124-quarter-mass/study/REFERENCE_PATHS.md`
- `.search/blobs/3e7c431c41912315994774e1ac3338ce3f47919d6677ff4394db38a9a9c40882.json`
- `.search/blobs/49c309e171825be70b3a3c683d9154b0d2871e2e0c22c82a36fcf628ec706d53.json`
- `.search/blobs/ab59ab3fee5a4a4b9d8739030f497e216c4bbacb770525958dba5cda1ad0f884.json`
- `<workspace>/erdos-124/sources/bergelson-simmons.txt`, lines 575-695, including Lemma 2.12 and the compact-group proof.
- `<home>/.codex/plugins/cache/exactory-ai/exactory/0.34.2/codex/README.md`, read before the skill.
- `<home>/.codex/plugins/cache/exactory-ai/exactory/0.34.2/codex/skills/math-solver/SKILL.md`
- `<home>/.codex/plugins/cache/exactory-ai/exactory/0.34.2/skills/math-solver/SKILL.md`
- `<home>/.codex/plugins/cache/exactory-ai/exactory/0.34.2/skills/math-solver/SEARCH.md`, relevant provenance, stable-account and budget, checkpoint/result-review, public accept-spec, immutable-evidence and post-exhaustion rules.

The exact candidate studies and query log were read as recorded study evidence. Their raw search-response corpus and unrelated proof branches were not inspected. This review does not endorse an exhaustive literature search or make claims about uninspected results.
