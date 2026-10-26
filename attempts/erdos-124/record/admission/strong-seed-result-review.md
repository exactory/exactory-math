# Independent result review of the strong-surplus counterexample

Decision: APPROVE. No blocking mathematical or review-package finding remains. The analytical proof refutes exactly auxiliary obligation-000010. This review does not execute acceptance or close any controller obligation.

## Review identity and boundaries

The reviewer is the fresh-context agent assigned this result review, not the proposal author or an admission reviewer. Host provenance is `source: host`, `actor_id: <user>` (the actual output of `id -un`), and `attestation_id: 01a07a7e-f0da-7112-bca8-b3817c073d36` (the actual `CODEX_THREAD_ID`). The proposal author is `codex-root-01a07806`, with attestation `session-01a07806-b2c5-7163-86d2-92fd0ef5cf33`. Both reviewer fields differ from the corresponding author fields. These are observed host identifiers, not invented model identities or cryptographic attestations of intellectual independence.

I read the installed Codex README before the shared math-solver skill, and read the relevant SEARCH.md provenance, checkpoint, ResultReview, public acceptance, and immutable-manifest contracts. The proposal was used to identify the author and exact claim, not as an endorsement of the result. I inspected the complete 228-line proof independently against that claim. No admission reviews, literature, predecessor proofs, or coauthor reasoning were used as proof evidence.

Operations were confined to document and JSON reads, file metadata, host identity reads, identity hashing, and writing the two assigned review outputs. No mathematical process, finite experiment, solver, compilation, certificate run, controller command, or native mutation was performed. The algebra below is analytical inspection of the submitted proof.

## Exact package and identity checks

JSON hashes use SHA-256 of sorted-key, compact, UTF-8 JSON. Duplicate object keys were rejected during parsing. The proof hash covers its raw bytes.

| Subject | Observed SHA-256 | Finding |
| --- | --- | --- |
| Complete stored checkpoint, including `id: checkpoint-000010` | `6014f5c37e695e93914f12781f56f8605753f78f1fbe4bf411105fe08735a410` | Matches the assigned subject |
| Evidence manifest | `cf16896e3550b80ae9bd7d644b819279cb606c4959b777d339507d7fbc7709ac` | Matches the checkpoint evidence entry |
| Complete claim object | `b68655ee573a8a7b30cf9d0c12cefa386480e9a5c5dcacb0b627aebe81bb2cce` | Matches the assigned claim and manifest |
| Raw proof `attack/erdos-124-strong-surplus-seed/moves/001-paired-perturbation.md` | `aebacbcb9ff8e52559d022b9751b0f6520555a6dc6383b375780a7202effe3f0` | Matches the manifest proof artifact |

The proposal claim, its `strong-surplus-seed` decomposition claim, and the checkpoint claim are structurally equal, including statement, quantifiers, empty assumption IDs, named scope, and `proof_policy: reviewed`. The manifest artifact path is relative to `attack/`, and resolves to the inspected proof. Its conclusion is `counterexample`, with no acceptance dependencies or route bindings. Its kind is `analytical`, its single artifact has role `proof`, and its manifest dependencies and external dependencies are empty. Verification is null, consistently with analytical review.

The checkpoint's immutable `verification_status: pending` does not purport to be independent acceptance. Its `kind: proof` is compatible with a counterexample outcome under SEARCH.md. The complete stored object, not a checkpoint input with its ID omitted, is the subject of this review. Journal ownership, reservation provenance, and immutable-store freshness remain service audit responsibilities; I have not manufactured a ResultAudit or claimed to execute those checks.

## Exact statement and quantifiers

The bound claim states:

> For every nondecreasing locally finite infinite sequence (a_i) of positive integers with bounded numerical multiplicity, if every tail has gcd one and its finite subset sums meet every residue class modulo every positive integer, liminf_{X->infinity} (log 2)#{i:a_i<=X}/log X>1, sum_i ||alpha a_i||^2=infinity for every irrational real alpha (where ||x|| is distance to the nearest integer), and (S_m-a_{m+1})/a_{m+1}^beta tends to positive infinity for every real beta with 0<beta<1, where S_m=sum_{i=1}^m a_i, then there exist integers L>=0 and m_0>=1 such that for every m>=m_0, S_m>=2L and every integer in [L,S_m-L] is a subset sum of a_1,...,a_m using each labelled index at most once.

A counterexample must be one fixed infinite sequence satisfying all these hypotheses simultaneously, and must rule out every fixed pair `(L,m_0)`. The submitted sequence is independent of the tail, modulus, irrational multiplier, beta, and proposed central interval. Thresholds in the limits may depend on a fixed beta. Neither uniform convergence as beta approaches one nor the endpoint beta=1 is part of this claim. There are no extra assumed lemmas or conditional assumption IDs.

## 1. Construction, ordering, and encoding (proof lines 10-45)

The definitions are `u_t=floor(9^t/t)`, `b_(2t)=9^t+u_t`, and `b_(2t+1)=3b_(2t)+1`, for every integer t>=1. Exactly two separately labelled copies of each level b_j, starting at j=2, form a.

Since `0<=u_t<=9^t`, the stated bound `9^t<=b_(2t)<=2*9^t` holds. The odd level is strictly greater than its even predecessor, is at most `6*9^t+1`, and is strictly less than `9^(t+1)` because `1<3*9^t`. The latter is a lower bound on the next even level. Thus levels are strictly increasing. The resulting sequence is nondecreasing with exactly two occurrences of each numerical value, consists of positive integers, and is infinite. The exponential lower bound makes it locally finite.

For even j, (1) follows from the bounds just proved. For j=2t+1, the lower bound follows from `b_j>=3*9^t+1>=3^j`, and the upper bound follows from `6*9^t+1<=9*9^t=3*3^j`. Thus (1) applies to every level, not only one parity.

Any finite selection of labels has coefficients c_j in {0,1,2}. The integer `T=sum c_j*3^(j-2)` is a bijective encoding of finite coefficient vectors by ordinary ternary digits, with absent higher digits understood to be zero. Selecting the first or second copy alone gives the same coefficient vector; this causes no difficulty. Since `e_j=b_j-3^j>=0`, the equality and inequality `sum c_j*b_j=9T+sum c_j*e_j>=9T` are correct. No uniqueness of a numerical subset sum is used.

## 2. Extension increments and finite seed (lines 47-100)

With `Delta_j=3b_j-b_(j+1)`, summing from j=2 through n gives `3b_2+2 sum_(j=3)^n b_j-b_(n+1)`. Subtracting b_2 yields exactly `E_n=2 sum_(j=2)^n b_j-b_(n+1)`. This verifies (3), including its initial offset.

For even j=2t, the defining affine relation gives `Delta_(2t)=-1`. For odd j=2t+1, expanding the definitions cancels the geometric terms and gives `9 floor(9^t/t)+3-floor(9^(t+1)/(t+1))`, as in (4). Applying the lower floor estimate to the first term and the upper estimate to the subtracted term gives `9^(t+1)/(t(t+1))-6`, so the direction and constant in (5) are correct.

The ratio of consecutive main terms is `9t/(t+2)>1` for every t>=1. The first main term is 81/2, which exceeds six. All odd increments are therefore positive. Summing the next even and odd increments gives (6), with the constant seven accounting for the even decrement of one. Its right side is positive. Each intervening even endpoint satisfies `E_(2t+2)=E_(2t+1)-1`.

The seed equalities follow directly from the definitions: `b_2=18`, `b_3=55`, and `b_4=81+floor(81/2)=121`. Hence `E_2=-19` and `E_3=25`. Subsequent odd endpoints increase from 25 and their following even endpoints are at least 24. The initial negative endpoint is a finite exception and does not affect any limit. The claim of a smallest seed is expressly limited to nonempty complete pairs in this template; it does not assert an extremum over all sequences.

Appending two levels adds four labels, preserves strict order and multiplicity, preserves the ternary coefficient range and the support inequality, and introduces another pair with difference `b_(2t+1)-3b_(2t)=1`. Arithmetic properties of the infinite continuation are established separately below. They are not inferred merely from the finite seed.

## 3. Every-prefix surplus and every beta (lines 102-135)

For E_(2t), the sum in (3) contains exactly t even increments, each equal to -1, and t-1 positive odd increments. Retaining the last odd increment, indexed 2t-1, gives `9^t/((t-1)t)-6-t-18`. This is (7), valid for t>=2. For E_(2t+1), there are still t even increments and the last odd increment is indexed 2t+1. Its lower bound gives `9^(t+1)/(t(t+1))-t-24`, which is (8). There is no missing parity or incorrectly counted decrement.

Fix an arbitrary real beta with 0<beta<1. The next values satisfy `b_(2t+1)<=7*9^t` and `b_(2t+2)<=2*9^(t+1)`. After the lower numerators become positive, division by these upper denominator bounds gives valid lower bounds on the ratios. Their positive terms grow as a positive constant times `9^((1-beta)t)/t^2`; the negative terms tend to zero as `O(t)/9^(beta*t)`. The logarithm comparison in the proof establishes divergence of the positive terms for each such beta. Thus both parity subsequences in (9) tend to positive infinity. No positive lower bound on 1-beta shared by all beta is needed.

After completing both copies of levels 2 through n, write `P_n=2 sum_(j=2)^n b_j`. The next term is b_(n+1), so the surplus is `P_n-b_(n+1)=E_n`. After selecting just the first copy of b_(n+1), the next term is still b_(n+1), and the surplus is `P_n=E_n+b_(n+1)`. Both ratios have the same denominator b_(n+1)^beta, and the latter numerator is larger. These two types cover every sufficiently late labelled prefix. Therefore the asserted limit holds as m tends to infinity without restricting m to block boundaries. The finitely many initial prefixes do not matter.

## 4. Every tail, modulus, and irrational multiplier (lines 137-170)

Every tail contains later complete adjacent levels b_(2t), b_(2t+1), whose gcd is one by their integer linear combination equal to one. The gcd of the entire tail divides this gcd and is therefore one. A cut between the two copies of a value does not remove later complete pairs.

For a fixed tail and modulus h>1, only finitely many residue classes exist. Those outside R, the classes occurring infinitely often, contribute only finitely many terms in total. All sufficiently late terms consequently lie in R. If the subgroup generated by R were proper, it would consist of multiples of a divisor g>1 of h. This follows from the elementary description of subgroups of the cyclic group: the preimage in Z is gZ for a divisor g of h. All sufficiently late terms would be divisible by g, contradicting the proved tail gcd property.

Thus R generates the whole cyclic group. Every negative coefficient can be replaced by a nonnegative one modulo h, since `-r=(h-1)r` in that group. Every target residue has a finite nonnegative expression in R. There are infinitely many occurrences available for each residue used, so distinct labelled indices can realize all required coefficients. Each label is used at most once. This proves full finite-subset-sum residue coverage in the originally fixed tail. Modulus one is immediate. The argument works for each tail, each positive modulus, and each target residue, with no common bounded number of summands presumed.

For any fixed real alpha, convergence of the nonnegative squared-norm series would imply that each term tends to zero, including both subsequences corresponding to adjacent levels. The nearest-integer triangle inequality and integer multiplication bound give `||alpha||<=||alpha b_(2t+1)||+3||alpha b_(2t)||`, using the exact affine identity. The right side tends to zero. The left side is independent of t, so alpha must be an integer. Thus every noninteger alpha, in particular every irrational alpha, has a divergent squared-norm series. This argument includes all irrational parameters, not only almost all or a selected family. Removing finitely many labels leaves the same eventual pairs and argument.

## 5. Label counts, numerical support, and failure of the conclusion (lines 172-200)

By (1), every level with `3^(j+1)<=X` has appeared, and no level with `3^j>X` has appeared. The number of levels up to X differs from `log X/log 3` by a bounded amount. Exactly two labels per level give `A(X)=2 log X/log 3+O(1)`. Therefore the required liminf is a limit equal to `log 4/log 3>1`. This uses the label count in the admitted hypothesis; it does not confuse it with the number of distinct values or sums.

For a positive subset sum at most X, its coefficient vector is nonzero, and its ternary code satisfies `1<=T<=floor(X/9)`. There are only floor(X/9) possible codes and hence at most that many coefficient vectors. The image of these vectors under numerical summation cannot have more elements than its domain. If multiple vectors produce one numerical sum, the bound only becomes smaller. If multiple label subsets produce one vector, the bound is unaffected. This proves (11) for the set of all finite subset sums of the entire infinite sequence, not just one prefix. In particular its upper density among positive integers is at most 1/9, and there are arbitrarily large missing integers.

Suppose the claimed fixed L and m_0 existed. For every integer n>=L, positivity makes S_m unbounded, so a sufficiently large m>=m_0 satisfies both `S_m>=n+L` and `S_m>=2L`. Then n belongs to the promised prefix interval and therefore to the full finite-subset-sum set. This would make that set cofinite, contradicting (11). Equivalently, for any proposed L and m_0, choose a missing n>=max(1,L) and then such an m; the prefix fails at n. This verifies the negation of the complete existential conclusion, including the requirements on m and the central endpoints. It is stronger than demonstrating a few exceptional prefixes.

## 6. Template remarks and scope (lines 202-227)

For the stated base-q template, q-1 labels per level give labelled counting exponent `(q-1)log 2/log q`. The base-two exponent equals one, and the base-three exponent exceeds one. The minimal-base statement within integer bases q>=2 and this exact template is correct. The restriction to coefficients 0 through q-1 is essential to the unique positional encoding; an arbitrary increase in multiplicity would require a different argument.

The proved result is a counterexample to the generic abstract inference. It supplies no counterexample in the admissible pure-power class, no decision of C1 for that class, and no decision of the pure-power quantitative profile, bridge obligations, or original root. The counterexample and its proof do not require establishing any classification theorem about which sequences can be represented by pure powers. The absence of a pure-power realization in this package cannot supply proof credit about that class.

The conclusion also does not refute every conceivable stronger surplus hypothesis. It refutes the stated simultaneous family of limits for all fixed beta<1 together with the stated arithmetic profile. No conclusion at beta=1, or under an additional quantitative rate condition, follows from this review. The checkpoint's next-hypothesis suggestions should be understood as research guidance within that scope.

## Dependencies, policy, and publication assessment

Every proof dependency is supplied in the inspected proof: the construction, order bounds, telescoping identity, floor estimates, finite seed, both asymptotic subsequences, within-copy comparison, elementary cyclic-group argument, nearest-integer inequality, ternary encoding, and implication from central-prefix coverage to cofiniteness. These elementary steps have been checked above. There is no imported mathematical theorem, unresolved premise, computational result, accepted predecessor lemma, or route bridge needed to establish the counterexample.

The proposal's inherited evidence and checkpoint lineage explain why this question was posed. They are not used as mathematical premises. Empty `dependency_ids`, empty manifest dependencies, empty external dependencies, and empty `route_bindings` are therefore appropriate. The proof meets the exact `reviewed` policy through independent analytical inspection. This is not a claim of certificate verification or Lean kernel checking.

This is a locally proposed generic route test. Correctness establishes that this particular abstract inference cannot be used as a universal premise. It does not establish standalone novelty, publication priority, or broad significance. No draft or paper was supplied or assessed.

## Disposition

Blocking findings: none. Required corrections before this result review can approve: none.

The accompanying `admission/strong-seed-accept.json` is the public CLI acceptance spec for obligation-000010, with outcome `counterexample` and the exact ResultReview bindings above. It intentionally contains no acceptance wrapper, internal classification or standard, fabricated audit, or schema-version field. Creating that spec is independent review evidence only; the controller must perform its own acceptance checks if an authorized caller later submits it.

Files created: `admission/strong-seed-result-review.md` and `admission/strong-seed-accept.json`. No source, proof, study, frozen evidence, checkpoint, controller record, or native record was modified.
