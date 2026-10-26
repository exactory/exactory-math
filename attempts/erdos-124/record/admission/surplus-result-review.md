# Independent analytical result review

Decision: approve the exact auxiliary surplus claim as an analytical proof at the reviewed standard. No blocking mathematical or evidence-binding finding was identified. This is a result review, not a proposal review, controller acceptance, formal verification, or root closure.

The reviewer is the host-supplied agent `/root`. The attestation is the actual `CODEX_THREAD_ID` read from the host environment: `01a07a53-837b-7e20-b4af-eeb219c22836`. These are distinct from the proposal author's actor and attestation. This review independently inspected the prescribed result package without using the producer's consolidation, inventory, or another result review.

## Subject and immutable bindings

The installed Codex README, shared math-solver workflow, and SEARCH.md sections on checkpoints, accepted results, provenance, and immutable evidence manifests were read. Canonical JSON hashes were independently recomputed using sorted keys, compact separators, UTF-8, and `ensure_ascii=False`. Artifact hashes cover raw bytes.

| Object | Verified SHA-256 |
| --- | --- |
| Complete stored checkpoint, including `id` | `48a5683c8865c6a3346c8d9be03eb25a8e14ecaab1c988487bd3f530d4bbdb71` |
| Exact claim object | `bae4fa11e19e2aca1ff8fcb1b738f54f42cd46ea794e5efd6c6dfc12941593ae` |
| Canonical evidence manifest | `bf7dd7cc79ac1f3ff8e7ecb6e5970ab2fc5eaa478a5f0eeb5c0c1662b63c37ef` |
| Proof, 9,088 bytes | `0778b0ba2fad32f4e72f6c1db2451c2f4e05f2d4d010671b6dfd2d1dc8163e65` |
| ESS HTML source, 1,016,877 bytes | `8931743d8b5ffe7034683bcbca56736738a6699dbd62eaf03fd421ef6f2320f0` |
| Problem study, 3,114 bytes | `d57055614b6011d3766fda24d80e12a903d43c659f89b4499c7c177f9ec93a00` |

The stored checkpoint is `checkpoint-000009`, with pending snapshot metadata, and the review target is `obligation-000007`. Its claim is structurally identical to both the proposal claim and the tail-surplus decomposition claim, including quantifiers, assumptions, scope, and proof policy. Its sole evidence digest equals the canonical manifest digest. The manifest claim digest equals the recomputed claim digest. All three artifacts resolve relative to `attack/` and match their declared hashes:

- `erdos-124-tail-surplus/moves/001-sunit-tail-surplus.md`
- `preflight/tail-surplus/sources/ess.html`
- `preflight/tail-surplus/problem.md`

The manifest conclusion is exactly `proof`, with empty acceptance dependencies and route bindings. It has no dependency manifests, external dependencies, or computational verification record. Controller checks of authoritative admission, journal reservation and prefix, freshness, and obligation identity remain the controller's audit responsibility. This review does not invent that audit or change the checkpoint's pending field.

## Exact statement and quantifiers

Fix any finite set D of distinct integers at least 3 with collective gcd one and sigma(D) = sum over d in D of 1/(d-1) at least one. Fix any integer k at least one and any finite set F of labelled occurrences (d,j), where d belongs to D and j is at least k. Order the remaining occurrences by value, with increasing base label breaking ties, and let S_m be the sum of the first m values. The conclusion is that for every real B there exists m_0 at least one such that S_m-a_{m+1}>B for every m at least m_0.

The proof establishes this precise statement. The threshold may depend on D, k, F, and B. It need not be uniform or effective. Equal numerical values from distinct labels remain separate terms. No assumption of pairwise coprimality is introduced.

## Published theorem and applicability

I read the exact ESS theorem and its preceding hypotheses and definitions in the pinned HTML, including the definition using every nonempty subset of summands. Section 1 assumes an algebraically closed field K of characteristic zero, a subgroup Gamma of (K*)^n of finite rank r, and a fixed vector of nonzero coefficients. For the equation sum alpha_i x_i = 1, the number of nondegenerate solutions in Gamma is at most exp((6n)^(3n)(r+1)). The HTML displays the theorem as 0.1; the surrounding paper refers to it as Theorem 1.1. The full sum is already one, so checking nonempty proper subsums together with that full sum is equivalent to the source's definition. Only finiteness is used here.

The [official arXiv record](https://arxiv.org/abs/math/0409604v1) confirms the authors, version, title, and publication in Annals of Mathematics 155 (2002), no. 3, pp. 807-836. ESS is imported as a published theorem. Its long internal proof is not newly certified by this review.

For each fixed nonzero integer c, take K to be the algebraic closure of Q and Gamma = {(a^u,b^v): u,v in Z}. The generators (a,1) and (1,b) are independent because a,b>1 and equality to (1,1) forces both exponents to be zero. Thus Gamma has rank two, even without any multiplicative independence assumption on a and b as scalars. It satisfies the source's finite-rank definition by taking Gamma_0=Gamma.

The coefficients 1/c and -1/c are fixed and nonzero. Both singleton summands are nonzero and their full sum is one. All solutions are therefore nondegenerate. The exponent-to-point map is injective. ESS consequently gives finitely many positive exponent pairs solving a^u-b^v=c. This step does not apply to c=0, and the proof correctly treats that case separately.

## Elementary deductions and complete prefix argument

1. Since D is nonempty, choose a in D and a prime p dividing a. Collective gcd one ensures that some b in D is not divisible by p. Then a and b are distinct, and their positive powers cannot coincide. Neither coprimality of a and b nor disjoint prime supports is needed. This prime-divisibility argument is valid under exactly the admitted assumption.

2. For every fixed real H>=0, only finitely many nonzero integers c have |c|<=H. Their finite solution sets have a finite union. There are no additional zero-difference pairs for the selected a,b. A finite maximum R_H of the power values in this union therefore exists, with zero used for an empty union. Once both selected power values exceed R_H, their difference exceeds H. This yields an eventual statement along any such sequence of exponent pairs, even if some pairs repeat at early prefixes. No subsequence selection, effective maximum, or computed exponent bound is used.

3. For each finite real bound there are only finitely many occurrences below it, whereas removing F leaves an infinite stream. Thus q_m=a_{m+1} tends to infinity. Each base retains infinitely many occurrences, so its first unused remaining power x_d(m) exists and satisfies x_d(m)>=q_m. The minimum of these next powers is q_m.

4. Eventually q_m exceeds every deleted value. At such a prefix, all deleted powers of a given base d lie below x_d(m). The used occurrences of that base are exactly its powers from exponent k up to, but excluding, the exponent of x_d(m), with that base's deleted occurrences removed. The geometric sum is (x_d(m)-d^k)/(d-1). Subtracting the deleted powers once per labelled occurrence gives the stated exact identity with C = sum_d d^k/(d-1) + sum_(d,j in F) d^j. The proof expressly restricts its per-base deletion sum to that base, resolving the otherwise potentially ambiguous displayed summation notation.

5. Ties do not invalidate this identity. A base whose occurrence at the tied value has been taken has advanced to its next power; a base whose tied occurrence is still pending has that value as its next power. No single base has two powers of the same value. Hence partial processing of a tie preserves both the per-base initial segment property and min_d x_d(m)=q_m. Deleting one labelled occurrence does not delete other occurrences with equal values.

6. Subtraction of q_m gives exactly S_m-q_m = (sigma-1)q_m + W_m-C, where W_m = sum_d (x_d(m)-q_m)/(d-1). Every summand of W_m is nonnegative. For M=max(a,b), choose the selected base d_* with the larger next power. Since q_m is at most the smaller next power and d_*-1<=M-1, W_m >= |x_a(m)-x_b(m)|/(M-1). Both inequality directions are correct, and all denominators are positive.

7. Both selected next powers tend to infinity because they are at least q_m. Their exponents remain at least k>=1. The finite-union conclusion therefore forces |x_a(m)-x_b(m)| to tend to infinity along all prefixes. Since sigma>=1, the term (sigma-1)q_m is nonnegative, proving the required surplus limit even at equality mass.

8. For any real B, set H=max(0,(M-1)(B+C)). Beyond both the finite-deletion threshold and the gap threshold, the lower bound |x_a(m)-x_b(m)|/(M-1)-C exceeds B. This remains true when B+C is negative. It establishes the full universal order of quantifiers and the strict final inequality. For sigma>1, the simpler linear lower bound also works, as stated in the proof.

The final fixed-L consequence follows immediately from the established limit. It supplies no represented central interval or late seed, and no change in the order of choosing L and the threshold is justified or used.

## Dependency completeness, policy, and significance

The dependency chain is complete for reviewed analytical evidence: the pinned published ESS theorem, followed by the explicitly proved prime-divisibility selection, finite union and finite maximum deductions, local finiteness of power streams, geometric summation, and elementary inequalities. The proof was read in its entirety. The pinned study was also read. Its references to earlier work are context, not premises in the deduction. In particular, the predecessor's geometric identity is independently rederived; the accepted reciprocal-core lemma and any inherited unaccepted theorem are not used. Empty acceptance dependency IDs and route bindings are therefore appropriate.

The optional local BEGL96 text was read only on printed p. 137. It supports the background remark that an estimate for the difference of powers of 3 and 4 appears there. Neither that quantitative estimate nor any completeness example on that page is used as a premise, so this background consultation does not add a missing proof dependency. Likewise, neither the study's query ledger nor a current problem-page status is needed for the proof.

No mathematical experiment, numerical test, certificate, checker, or formal theorem was used or run in this review. The executed computations were document handling and metadata hashing. The evidence supports `classification: analytical` and `standard: reviewed`, not a kernel-checked or effective result. The accompanying acceptance request contains no invented audit.

This is a short auxiliary corollary of established finiteness theory with a careful labelled-stream calculation. The ESS introduction itself explains that the two-variable finiteness theory predates the general theorem. The pinned study does not establish publication novelty, and this review does not certify an exhaustive priority search. The result is useful as an exact local prerequisite, but independent standalone publication novelty or significance has not been demonstrated.

Acceptance is limited to obligation-000007. No effective threshold, seed theorem, C1 assertion, implication bridge, or original Erdos 124 theorem is established. The original root remains open. The parent may integrate this result subject to the controller's own audit and must preserve the remaining obligations.
