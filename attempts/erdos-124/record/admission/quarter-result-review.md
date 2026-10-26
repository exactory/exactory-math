# Independent analytical result review of checkpoint-000017

Verdict: approve the mathematical result for obligation-000019. No blocking proof defect was found. This is analytical approval under the reviewed policy. It is neither service acceptance nor formal verification.

## Binding and independent provenance

The following identifiers and digests are supplied bindings, not independently computed hashes:

- Stored checkpoint: checkpoint-000017, digest `32513300fcc14d53726380aa9cfd2a598fef719a0f1e4131c8517d709508d879`.
- Exact Claim digest: `faff0e45e28f7b200dc097874a0fa20849146039a643c588213fdc9b6cc770c0`.
- Current analytical manifest digest: `ab59ab3fee5a4a4b9d8739030f497e216c4bbacb770525958dba5cda1ad0f884`.
- Conclusion: outcome `proof`, direct dependency IDs `["acceptance-000001","acceptance-000005"]`, and route bindings `[]`.

Actual read-only host shell output supplied `USER=<user>`. A separate non-login `/bin/sh` call to `/usr/bin/printenv CODEX_THREAD_ID` supplied `01a07ddc-61ea-7af2-b7ec-c53fcdaefa52`. The reviewer provenance is therefore source `host`, actor ID `<user>`, attestation ID `01a07ddc-61ea-7af2-b7ec-c53fcdaefa52`. Both identity fields differ from the supplied author's `/root` and `01a07806-b2c5-7163-86d2-92e8e272b9eb`. Earlier combined environment-variable reads returned only USER; the attestation above comes from the successful single-variable read, not an inferred session identifier.

I reviewed the prescribed result material in a fresh context without a parent transcript. I did not consult the current proposal review or a previous review of the current result. I first read the installed Codex README, then the required SEARCH.md sections on checkpoints, accepted results and immutable evidence manifests, and the shared math-solver workflow and provenance contract. No Exactory CLI, objective lifecycle operation, controller or native-record mutation, mathematical program, enumeration, solver, compilation, certificate checker or Lean kernel was executed. No hashing command or gate suppression was used.

## Exact statement and scope

The stored Claim states:

> For every nonempty finite set D of distinct integers at least 3, with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=3+min{1/4,2/m}, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

The proof establishes this statement with N depending on D, k and F. Its assumption-ID context is empty. It does not require pairwise coprimality, multiplicative independence, a bound on the size or largest base of D, or a uniform N. The positive-cutoff and finite-deletion quantifiers are universal. Numerical equality between different labels never merges their availability.

Approval concerns obligation-000019 only. Root obligation-000001, complementary obligation-000020 and bridge obligation-000021 remain open. Empty route bindings do not discharge that bridge. Zero publication units are consistent with an internal quantitative corollary and carry no root-closure or publication-priority implication.

## Material read and dependency closure

I read admission/quarter-result-context.json completely, including the exact stored checkpoint, Claim, author provenance and supplied accepted dependency records. I read all three manifests completely and the following complete artifacts.

The eight current artifacts, with paths relative to attack/, are:

1. erdos-124-quarter-mass/moves/001-quarter-mass-completeness.md.
2. erdos-124-quarter-mass/units/consolidation.md.
3. erdos-124-quarter-mass/study/problem.md.
4. erdos-124-quarter-mass/study/make-the-proof-constructive.md.
5. erdos-124-quarter-mass/study/REFERENCE_PATHS.md.
6. erdos-124-quarter-mass/novelty.md.
7. erdos-124-quarter-mass/problem.json.
8. preflight/quarter-mass/QUERY_LOG.md.

The core manifest declares the complete proof erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md, which I read. It has no further dependencies. Its supplied manifest digest is `3e7c431c41912315994774e1ac3338ce3f47919d6677ff4394db38a9a9c40882`, matching the evidence reference in acceptance-000001.

I read all nine mass-partition manifest artifacts: erdos-124-mass-partition/moves/001-high-mass-completeness.md; units/consolidation.md, study/problem.md, study/make-the-proof-constructive.md, study/REFERENCE_PATHS.md, novelty.md and problem.json under that same attack; preflight/mass-partition/sources/fan-v3-reading.txt; and preflight/mass-partition/QUERY_LOG.md. Its supplied manifest digest is `49c309e171825be70b3a3c683d9154b0d2871e2e0c22c82a36fcf628ec706d53`, matching acceptance-000005. Its sole accepted-proof dependency is acceptance-000001, and its sole manifest dependency is the core manifest.

I read the entire externally pinned research-root sources/bergelson-simmons.txt, including Definition 1.26, Theorem 2.1, Section 2.1, Lemma 2.12, the multiset qualification, Section 2.7 and references. Its supplied external digest is `656e855d776687b761dba78128e3f537fa8408aaf82a721a482b6a2c82c7c157`. Lemma 2.12 explicitly states the needed syndetic-sumset theorem and attributes it to Bergelson-Furstenberg-Weiss, Theorem I. The saved Fan response includes the full finite-correction Lemma 2.2 and Corollaries 2.3 and 2.5. The local proof supplies its own occurrence-preserving argument rather than assuming the numerical-set version applies unchanged.

For the historical statement references, I also read research-root sources/begl1996.txt and attack/preflight/mass-partition/sources/canonical-124-reading.txt completely. Their role is background and comparison with the original objective. Neither supplies an additional mathematical premise of the current deduction. Likewise, the query logs' raw discovery responses and unrelated hits are not proof inputs. The current proof does not rely on the predecessor profile counterexamples mentioned in the studies.

Manifest artifact paths are relative to attack/, not to attack/checkpoints/. The current move explicitly anchors its sibling-attack references at the attack workspace; an additional ../ is needed when resolving from moves/. Its consolidation's ../moves/ reference resolves from units/. The study REFERENCE_PATHS.md files locate copied QUERY_LOG.md and sources/ references in their preflight directories. The Bergelson-Simmons external path is an absolute read-only input. These conventions resolve the mathematical references without inventing a dependency outside the declared proof closure.

The supplied records mark both dependencies as accepted analytical proofs under reviewed policy. Historical pending or prospective wording in their frozen proof and study artifacts predates those records; immutable snapshots need not be rewritten when a separate acceptance is created. The dependency graph is acyclic, its conclusion lists agree, and no computational premise or missing local mathematical proof was found. This is a substantive closure review, not a claim that current bytes, freshness or provenance were cryptographically audited.

## Analytical verification

The accepted core proof is valid independently of its status record. Least eligible gcd descent always finds a new base, strictly decreases the gcd, and stops at one. If q additions occur, the first new gcd g1 satisfies g1<=floor(m/2), and there are at most g1-1 later decreases. Thus q<=floor(m/2), and the seed has at most m-1 elements. At least one exceeds m, so its mass is strictly less than its cardinality divided by m-1, hence below one. The first subsequent crossing retains m and gcd one and adds a weight at most 1/m to mass strictly below one. This proves the precise inherited bound, including m=3 and m=4.

For the new core, m>=8 follows from that strict bound. For 3<=m<=7, a last augmentation base at least nine adds at most 1/8 to mass strictly below one. The exceptional case is a crossing by eight, with the completed gcd seed already present.

If that seed contains a base above eight, consider the first such choice. Its current gcd g>1 divides every available base in S=D intersect {m,...,8}; otherwise the least eligible choice would be small. In particular g divides m. The possible S are contained in {3,6}, {4,6,8}, {5}, {6,8}, {7}, respectively for m=3,4,5,6,7. For m=6, divisors three and six allow only {6}, also contained in {6,8}. Every large seed element has weight at most 1/8, and their number is at most q<=floor(m/2). The resulting exact bounds are:

| m | Upper bound for sigma(S union seed) |
|---|---|
| 3 | 1/2+1/5+1/8=33/40<1 |
| 4 | 1/3+1/5+1/7+2/8=389/420<1 |
| 5 | 1/4+2/8=1/2<1 |
| 6 | 1/5+1/7+3/8=201/280<1 |
| 7 | 1/6+3/8=13/24<1 |

Small seed elements are already counted in S. Charging all q possible additions as large elements only increases the bound. A stopping set reached by adjoining bases at most eight would lie in S union seed, contradicting its mass being at least one. This rules out the ordering issue explicitly.

If the entire seed is small and m>=4, every early stopping set lies in {4,...,8}, whose total is 153/140. Its difference from 9/8 is 9/280>0. This handles m=4,5,6,7 without imposing increasing order on the seed itself.

For m=3, one gcd addition suffices, and its least eligible base b is exactly one of 4,5,7,8 when the seed is small. I checked all alternatives and fractions:

- b=4: the seed is 5/6. Presence of 5 gives the first crossing 13/12; absence of 5 and presence of 6 gives 31/30; absence of both and presence of 7 gives exactly 1. If 5,6,7 are absent, even adding 8 gives only 41/42. The positive margins below 9/8 for the three crossing masses are 1/24, 11/120 and 1/8.
- b=5: base 4 is absent and the seed is 3/4. Adding 6 gives 19/20. With both 6 and 7 present, the crossing is 67/60 at 7, with margin 1/120 below 9/8; 8 is not added afterward. With 6 present and 7 absent, a crossing by 8 requires 8 and gives 153/140. With 6 absent and 7 present, the mass after 7 is 11/12, and a crossing by 8 requires 8 and gives 89/84, with margin 11/168. With neither 6 nor 7 present, even adding 8 gives only 25/28. Absence of the required last base simply means no early crossing.
- b=7: bases 4 and 5 are absent by the least eligible rule. Even the full possible early set {3,6,7,8} has mass 106/105, below 9/8 by 97/840. This includes the case where 6 is adjoined after the seed already contains 7.
- b=8: bases 4,5,7 are absent. The entire possible early set {3,6,8} has mass 59/70<1, so it cannot cross.

These alternatives exhaust the seed choices and the remaining increasing augmentation. They prove a minimum-preserving gcd-one C with 1<=sigma(C)<9/8 for every m>=3. No finite experiment supports this conclusion.

For the second bin, every remaining base is at least four because C contains the original minimum. An increasing first crossing ending at a base at least nine again has mass below 9/8. If it ends earlier, the entire bin is bounded by the same 153/140 total. No gcd hypothesis is needed for this bin.

At sigma(D)>=13/4, removing C leaves mass strictly greater than 17/8, so the second crossing exists. Removing both C and B1 leaves sigma(B2)>13/4-9/8-9/8=1. Both strict inequalities survive equality in the input threshold. All three groups are nonempty. For 3<=m<=7 the claimed threshold equals 13/4. For m>=8 it equals 3+2/m, where the accepted old theorem applies directly; at m=8 the thresholds agree. Thus the improved range retains the old, better large-minimum bound.

## Verification of the intermediate completeness criterion

The old quantitative theorem alone would not prove the new small-minimum range. The current deduction instead reuses the complete intermediate argument in Sections 1-3 and 5-6 of the accepted mass proof. I checked that argument itself, including the following points.

The induction for bounded subset-sum gaps applies to sorted occurrences with ties. At each step the two translated finite sumsets either have overlapping spans or have a separating gap bounded by the ordered deficit. Their endpoints and unbounded total sum give syndeticity. A finite deletion increases a valid gap constant by at most the total deleted value.

For any base group A of reciprocal mass at least one, the exact geometric bound for terms strictly below x gives an ordered deficit at most K_A=sum_{d in A}d^k/(d-1)+sum_{(d,j) in F,d in A}d^j. Every tied label may retain additional predecessors, so this lower bound on preceding mass remains valid. Further finite correction-label removal is accounted for in a new gap constant.

For the correction group, convergence of ||beta*d^j|| to zero forces the nearest-integer recurrence z_{j+1}=d*z_j eventually. Its errors then satisfy e_{j+1}=d*e_j, and convergence forces them eventually to vanish. Thus the denominator of beta divides a power of every base in C. Collective gcd one rules out every nontrivial denominator. This proves divergence of the nonnegative norm series for every nonzero beta, including rational beta, after every positive cutoff and finite deletion. Pairwise coprimality is unnecessary.

The published sumset theorem applies to the two numerical sets of positive attainable sums, which are syndetic and need not be disjoint. Their representing label supplies are disjoint. In the compact torus, the intersection of closures of tail-sum phases is a nonempty compact semigroup: approximating two points on successive disjoint tail supports proves closure under addition. The compact multiple-subsequence argument supplies inverses. If theta were outside this subgroup, a separating integer character would yield a nonzero beta. One sign of its norm representatives has divergent total in every tail; stopping that total on reaching 1/4 gives a phase of character norm at least 1/4. A limit belongs to the subgroup and contradicts annihilation. Hence the subgroup is the entire orbit closure K.

Density and compactness then extract finitely many correction sums whose translates cover K. Choosing one representation for each and taking their union gives a finite label set E. These alternative correction representations may overlap each other because only one is used at a time. Trimming the thick set by every shift from zero to the largest correction sum proves thickness of sums on B1, B2 and E. After E is fixed, the remaining C supply has a finite gap constant g_E, and thickness supplies an interval of exactly that required length. The disjoint interval-plus-reserve argument represents every sufficiently large integer. No correction label is reused.

The dovetailed finite interval search in the accepted proof also remains valid as a mathematical construction: a correction prefix eventually contains E, thickness then supplies an interval of its own recomputed gap length, and finitely many representations fit in some finite prefixes of B1 and B2. The search is not executed and no complexity bound is claimed. The separate modular audit is consistent but is not an additional unproved hypothesis.

Consequently the intermediate criterion requires precisely three groups of mass at least one with collective gcd one in the correction group, independently of the old allocation threshold. The new allocation verifies these exact hypotheses. This is a new deduction to the exact current Claim using the supplied dependency proofs, not controller propagation of an old theorem beyond its accepted scope.

## Acceptance boundary

The accompanying quarter-accept.json contains only the requested public fields and this independent analytical approval. It supplies no audit, classification, certificate, formal-verification claim or acceptance status. All bindings and artifact digests remain supplied values. The controller must still perform its immutable inventory and complete transitive-closure audit, current external-byte checks, policy checks, journal-origin and reservation checks, provenance validation and pinned-review checks before service acceptance. Those mandatory checks are not waived by this report.
