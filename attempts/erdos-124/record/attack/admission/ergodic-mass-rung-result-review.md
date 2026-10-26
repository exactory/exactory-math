# Independent result review of checkpoint-000024

Decision: approve the exact checkpoint claim under the reviewed analytical standard. No blocking mathematical issue was found. This is a result review, not controller acceptance, a proof of the original objective, or authorization for another research strategy.

Reviewer provenance: source `host`; actor_id and attestation_id both `01a07fa5-7b0c-7ab2-8257-67adbb8a9964`; supplied nickname Dalton. The supplied identifier was checked against the current `CODEX_THREAD_ID`, which matched exactly. The author identifiers in the supplied context are different. Independence here means this review was performed in this supplied reviewer context without reading another review or the author's conversation. It makes no broader provenance claim.

Subject digest: `f6411470e7dd2ceb27a0af659ea2cfeeb0ef321d7f859bf5f56ffa4910f7f91a`.

Claim digest: `cb45ac4481b483ee9ecca4b2b505bfabc2f58203a88cd0d7899c086f1c1a82ce`.

## Evidence and reading boundaries

The complete governing context was read at `<workspace>/erdos-124/attack/admission/ergodic-mass-rung-result-context.json`.

The following names identify the exact frozen files used below. Section references concern their contents, not a mutable working copy.

- Candidate: `<workspace>/erdos-124/attack/.search/artifacts/b2f2c285a623c8ae9ccfb38765f3579c0303f1b203f435391cd1d4ccc85dca3f`, logically `erdos-124-ergodic-mass-threshold/moves/002-two-supply-ergodic-rung.md`. Read completely.
- Mass: `<workspace>/erdos-124/attack/.search/artifacts/3aa1c7292bb7b0b9f93026159b62a90cfa0e57930fb383a17451202658837924`, logically `erdos-124-mass-partition/moves/001-high-mass-completeness.md`. In particular, Sections 1, 2, 5.1 and 5.2 were read without truncation and audited as lemmas, independently of the supplied accepted status.
- Core: `<workspace>/erdos-124/attack/.search/artifacts/f2e3fd8517cda7ce584a9f4d297bf9038fbc59f423c2058c9c4d03d0253acbdd`, logically `erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md`. Read completely, including the gcd seed and first-crossing proof.
- Griesmer: `<workspace>/erdos-124/attack/.search/artifacts/32880c56688e1e0e24eebf33c5400c9a8eafda5ba639da55f5eb022bc9a8ff30`, the pinned extracted text of *Discrete sumsets with one large summand*, arXiv:2507.10512v1. Read Section 1.2 and Observation 1.3; Definition 3.4 and its matrix-coefficient setup; Theorem 3.17's statement; Lemma 4.1 and Corollary 4.2 with their proofs; Lemmas 9.2, 9.4, 9.5 and their proofs, the intervening spectral representation and polarization material; Definition 10.1, Lemma 10.3 with its proof, Remark 10.4, Question 10.5; and Lemma 13.1 with its proof.
- Primary reading boundary: `<workspace>/erdos-124/attack/.search/artifacts/713efd604a2eed758448b28f340d7e3c7dc1182e02c7fb4182d4367ae0ff633a`. Read completely.

The exact manifests read were `<workspace>/erdos-124/attack/.search/blobs/c34b753e9129af8fd6fc65f54ef85887cee309ab7dddb872749b1aaa9d8c574a.json`, `<workspace>/erdos-124/attack/.search/blobs/49c309e171825be70b3a3c683d9154b0d2871e2e0c22c82a36fcf628ec706d53.json`, and `<workspace>/erdos-124/attack/.search/blobs/3e7c431c41912315994774e1ac3338ce3f47919d6677ff4394db38a9a9c40882.json`.

The remaining candidate-manifest study artifacts were also read at their specified frozen digest paths: the loss ledger, two-entry journal, problem JSON, preflight problem, strategy study, novelty note and query log. The Mass consolidation was read at `<workspace>/erdos-124/attack/.search/artifacts/454bff7e31cd731e1a42c3ca88a2fa039767d4ef6f98d5d76b3154dd259b90a1`. These contextual records were not treated as mathematical certification.

The imported Griesmer main theorem is the explicitly permitted trusted literature boundary. Its complete underlying proof was not independently checked. The old Bergelson-Simmons and Fan engine, historical Quarter comparisons, WOC claims, and original-problem source are not needed to deduce this checkpoint from the elementary Mass lemmas and Griesmer's corollary. Their full proofs were not audited here. No literature priority or exhaustive-search assertion is approved.

Metadata limitation: the context and manifests specify the digests above, and the corresponding frozen files were inspected. Attempts to recompute SHA-256 using `shasum` and `sha256sum` were rejected by the environment's math-solver PreToolUse hook as unsupported shell operations. No recomputed content-hash match is claimed. No controller operation was substituted. This limits the metadata audit, not the analytical findings on the text read.

## Statement

Pass. Candidate Section 1 agrees with the context's checkpoint claim and obligation-000041. It quantifies over every nonempty finite set of distinct integer bases at least four, with its own minimum m, collective gcd one, and inclusive mass condition sigma(D) >= b(m). For each such D, every positive integer cutoff k and every permitted finite set F of deleted labels are fixed before selecting an eventual threshold N(D,k,F). Every integer n >= N has its own finite representing support. There is no exchange of these quantifiers, bound on the largest base, bound on F, or requirement of one finite support for infinitely many integers.

The explicit mass bound is b(m) = 2 + 1/(m-1) + (floor(log_2(m))+1)/m. The proof also establishes the asserted uniform bound 37/12 and the limit 2. The argument does not promise a uniform or explicitly computable value of N.

## Assumptions and analytical audit

### Character nonconvergence and label multiplicities

Pass, Candidate Sections 3.1 and 3.2; Mass Section 5.2. A finite base set gives a countable, locally finite power supply. Removing finitely many labels leaves every sufficiently late power of each base. Thus convergence of the norms along the enumerated supply would imply convergence along each base's tail.

For a fixed base, the nearest-integer recurrence has an integer left side tending to zero. It therefore vanishes eventually. The resulting recurrence e_(j+1) = d e_j, with d >= 2 and e_j tending to zero, forces eventual exact integrality. One base makes beta rational; each base forces its reduced denominator to divide a power of that base. Every prime divisor of that denominator would divide the collective gcd. Only the trivial character survives. The proof needs collective gcd one, not a coprime pair or multiplicative independence.

Failure of norm convergence at a nontrivial character supplies an epsilon > 0 and infinitely many factors with absolute value at most cos(pi epsilon) < 1. This proves product decay, including epsilon = 1/2. Epsilon may depend on the character. The Bernoulli measures are one common sequence, chosen before any character, and are probability measures on all subsets of Z. Coincident sums receive added probability; coincident values of distinct labels do not remove an available choice or reuse a label.

### Full Fourier-Stieltjes mean

Pass, Candidate Section 3.3; Griesmer Definition 3.4, Lemmas 9.5 and 10.3, and Remark 10.4. For each positive finite Radon measure rho on the circle, the Fourier integrands are measurable, bounded in absolute value by one, and converge pointwise to the indicator of the trivial character. Finite support justifies the interchange of integrals. Dominated convergence is applied to the original sequence of countably additive probability measures and yields rho({0}).

An arbitrary weak-star cluster point along indices tending to infinity then preserves each of these scalar limits and assigns S_A mass one. Evaluation at any fixed bounded function is weak-star continuous. No simultaneous countable enumeration of all rho is needed: every such scalar sequence already converges, so the same cluster point works for every rho.

Lemma 9.5(ii) is precisely sufficient for all unitary matrix coefficients, not just characters. Its spectral content also confirms the quantifier over arbitrary Hilbert spaces: the diagonal coefficient for a vector has a positive finite spectral measure on its cyclic subspace, and its atom at the trivial character is the squared norm of its invariant projection; polarization gives the mixed coefficients. The relevant spectral subspace is the cyclic subspace of that vector, as in the source's proof of Theorem 9.3. No assertion about the absence of eigenvectors elsewhere in the entire Hilbert space is needed. The candidate does not use the source's unresolved Question 10.5. There is no application of dominated convergence to a net, and eta is not assumed invariant.

### Gap lemma, inclusive powers and finite deletion

Pass, Candidate Section 4; Mass Sections 1, 2 and 5.1. If x <= d^k, the geometric lower bound is immediate. Otherwise, taking the least exponent t with d^t >= x gives exactly (d^t-d^k)/(d-1) for the sum of the powers strictly below x. This also holds when x itself is a power. It proves the claimed lower bound (x-d^k)/(d-1) with the correct endpoint convention.

Subtracting the total value of all deleted labels is a valid lower bound even if some deleted values are at least x. The deletion set is finite, so K_C is finite. In a sorted enumeration, every strictly smaller available label precedes the current one. Additional tied labels can only increase the preceding sum. Therefore the deficit is at most (1-sigma(C))a_i + K_C <= K_C, including sigma(C) = 1 exactly. The integer g_C = ceil(K_C) is positive.

The finite-prefix induction in Mass Section 2 is valid. Each prefix subset-sum set contains both endpoints of its span. Each of its two translates has mesh at most g_C. Disjoint spans introduce only the bounded deficit gap; overlapping spans cannot introduce a longer gap without either containing a span endpoint or lying within a copy's span. Prefix totals tend to infinity. Integer mesh at most g_C therefore gives a hit in every interval of g_C consecutive nonnegative integers, with no extra unit required. The empty sum correctly handles intervals starting at zero.

### Density, extreme mean, thickness and reserve

Pass, Candidate Section 4; Griesmer Observation 1.3 and Corollary 4.2(ii). Partitioning the initial interval into complete blocks of length g_B gives at least floor(n/g_B) hits. The initial-interval probability averages have a weak-star cluster point invariant under every fixed integer translation, since the normalized boundary contribution tends to zero. Its X mass is at least 1/g_B. The maximum of the continuous functional evaluating X on the compact convex set of invariant means has an extreme maximizer. This is the elementary face argument behind Observation 1.3 and Lemma 13.1, using nontrivial convex combinations. Thus the required extreme invariant nu has nu(X) > 0.

With eta(Y) = 1, the strict inequality nu(X) + eta(Y) > 1 holds. The pinned Corollary 4.2(ii) applies to X and Y as subsets of the discrete abelian group Z and yields nu(X+Y) = 1. Finite additivity, translation invariance and positivity imply that every finite intersection of the required shifts has mass one. This produces every finite interval length in X+Y. Nonnegativity of X+Y ensures that the interval starts at u >= 0.

The reserve gap g_R is fixed before selecting the interval of that length. For n >= u+g_R-1, the interval [n-u-g_R+1,n-u] has exactly g_R nonnegative integer points. A reserve sum r in it makes n-r belong to [u,u+g_R-1], with both endpoints correct. Its representing labels lie in R; those for n-r lie in A union B. Each chosen support is finite, and the base partition makes these supports disjoint regardless of numerical collisions. No part of the reserve was spent in producing the seed. The argument proves the assertion for the original arbitrary k and F, without relying on an unstated cutoff-increase reduction.

### Logarithmic seed and threshold equality

Pass, Candidate Section 5; Core Section 2. Whenever the current gcd exceeds one, collective gcd(D)=1 supplies a new base not divisible by it. Such a base was not already selected. The next gcd is a positive proper divisor and at most half the current gcd. Descent terminates at one. If q bases were added, 1 = g_q <= m/2^q implies 2^q <= m and hence q <= floor(log_2(m)); the direction of this inequality is correct.

Every added base exceeds m and has reciprocal weight at most 1/m. Thus the seed A has mass at most a(m) = 1/(m-1) + floor(log_2(m))/m. No mass-one hypothesis is imposed on A or needed for its FS-mean.

At the inclusive input threshold, the complement has mass at least 2+1/m. Its first crossing of mass one yields 1 <= sigma(B) < 1+1/m because the preceding partial mass is strictly below one. Consequently sigma(R) > 1, even if both sigma(D) = b(m) and sigma(A) = a(m). All three groups are nonempty and disjoint, and only A needs gcd one. This verifies the exact endpoint allocation rather than a version with an unstated positive slack in the input.

### Uniform bound and asymptotic limit

Pass, Candidate Section 6. For r = floor(log_2(m)) >= 2, the dyadic envelope c_r = 1/(2^r-1) + (r+1)/2^r bounds b(m)-2 from above. Both summands decrease with r. The second comparison is equivalent to r > 0. Thus c_r <= c_2 = 13/12 and b(m) <= 37/12, attained by the formula at m=4. This does not assume b(m) is monotone across dyadic jumps.

The ratio of successive second summands is (r+2)/(2(r+1)) <= 2/3 for r >= 2. Both envelope terms tend to zero; r tends to infinity with m, and b(m) > 2. The squeeze argument proves b(m) tends to 2 over every integer minimum m tending to infinity. This is a limit of sufficient mass bounds, not a limit of representing supports or an assertion of completeness at mass 2.

## Scope

Pass. Sections 7 and 8 preserve the distinction between this rung, T_4=1 and the original problem. The three disjoint groups necessarily spend more than two units of mass, since B and R each spend at least one and nonempty A has positive mass. This is a limitation of that criterion alone.

The rung supplies a nonempty set of valid global thresholds through 37/12. If its infimum were one, each fixed input of mass greater than one would admit a valid threshold below its own mass. Conversely, the all-input strict-mass assertion would imply every threshold above one. This verifies the stated equivalence without inferring the mass-one endpoint from an infimum. The unproved sub-rung premise, minimum-three inputs and reciprocal equality remain open. No claim of optimality, novelty priority, formal verification, or proof of the original objective follows from this approval.

## Dependencies

Pass within the stated literature boundary. The selected Mass lemmas were inspected directly and their weaker, mass-free nonconvergence scope was checked. Core's gcd descent was read, while the sharper logarithmic bound was verified in the candidate itself. The checkpoint does not need to apply Mass's old complete theorem with its stronger input threshold. Griesmer's cited corollary and the full FS-mean interface agree with the pinned text, and every hypothesis for their use on Z is supplied. Acceptance identifiers alone were not used as substitutes for reading the lemmas.

## Policy and disposition

Pass for the requested reviewed analytical result. Work consisted of read-only source and text inspection, the single current thread identity check, attempted metadata hashes, and writing the two requested review files with apply_patch. No mathematical executable, finite enumeration, new research strategy, native journal change, admission, or controller-state mutation was performed. No previous review, author conversation, or unrelated controller record was read.

Approve only checkpoint-000024's exact claim. The metadata limitation and trusted primary-theorem boundary above remain part of this review. Neither is represented as a completed formal or cryptographic verification.
