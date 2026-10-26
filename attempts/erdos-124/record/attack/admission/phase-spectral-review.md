# Independent proposal admission review: proposal-000020

Decision: approve as an analytical research proposal. This is not approval of a proof, a computation, a resource renewal, or root closure. There is no unresolved blocking objection to admission.

Reviewer: Jason, host identity `01a0803b-47d5-7bd2-ae3c-87289dbcd5a4`. The host supplied this exact identity for both actor and attestation. It differs from the proposal author's recorded actor and attestation.

Subject digest: `0fd1282a98f0d7e5d6b5f67cea1952902cd111c66106bd17a1441dd7f02ebeb0`.

Claim digest: `ce55e60fe225a57375df15c00783d6d8ea63155631beb2535596ac3fe2c174ab`.

## Mathematical admission judgment

The proposed operation addresses a specific limitation in the inherited proof. In CP25, section 2.1, equation (7), the retained strict-prefix lower bound is

    sigma(D minus {h}) x + q_i/(h-1) - C - W_(i-1).

The conclusion there uses `sigma(D minus {h})>=1`. Increasing the next chosen power does not make that coefficient inequality true for a newly allowed base. Accordingly, CP25 does not justify copying its invariant while replacing its active core H by all of D.

The new proposal introduces an actual mathematical question at that point: choose powers at a fixed simultaneous near-alignment, with a scale threshold depending on prior removed weight, and seek a different strict-prefix estimate that pays for removal at every later scale. The fixed rational tolerance and multiplier, positive absolute margin, and preservation for the actual complement are expressly goals of the first amplification argument. Their absence as proved formulas is appropriate at proposal admission. It would be a defect at proof acceptance.

This satisfies the constructive strategy as an unknown common-extension question. The finite-prefix object, proposed extension, invariant to preserve, analytical seed, success condition, and concrete failure signals are identifiable. The entry requires the amplification lemma before the seed. The study observes this order, skips the inapplicable extremal-constant and forcing branches, and retains the maximum of two applications at strategy step 3. Admission should not change that unknown precondition to yes or authorize indefinite iterations after a failure.

The extension is substantive even at the level of its input domain. For `D={4,5,6,7,8}`, the reciprocal mass is `153/140`, and the collective gcd is one. Removing the lightest reciprocal term leaves `19/20`; every other removal leaves less. Thus CP25 has an empty active core on an input covered by the new proposal. Moreover, on overlapping domains the new assertion asks for bounded exponent gaps for every base, rather than only CP25's active bases. This is not a claim that the proposed construction has been proved on this example.

## What the recurrence sources actually supply

I read the primary Li-Oprocha-Ye-Zhang HTML at the definitions in sections 2.1-2.3 and Lemma 2.1(2), rather than relying on the study's label. Minimality is minimality of the orbit closure. Positive syndeticity means a fixed bound on return gaps in the nonnegative integers. The lemma characterizes minimal points using returns to every neighborhood of the point. It does not turn mere recurrence into bounded waiting, give an explicit numerical return bound, or prove the proposed power-prefix inequality.

For a fixed active base h, the relevant rotation has logarithmic coordinates `log(h)/log(d)` modulo one. Its actual orbit closure is the appropriate compact space; rational relations may make it a proper subgroup. The compact-semigroup argument in Bergelson-Simmons, footnote 10 adjoining Claim 2.13, is applicable to this closure. The proof still has to state the restricted rotation and its minimality and relate a fixed neighborhood of the identity to the rational power-comparison test. This interface permits rational dependencies and exact alignments. Full-torus equidistribution is unnecessary and has not been supplied.

Bounded return gaps for each fixed neighborhood are relevant to the proposed least-eligible rule. They are not by themselves the claim that selected exponents have bounded gaps: that conclusion must also account for the moving threshold `Lambda(C+W)` and the complete cycle through D. If the proof replaces the fixed neighborhood by tolerances tending to zero, it loses the stated uniform-in-iteration return interface. None of these missing transfers is treated as inherited evidence.

## Quantifiers, legality, and the infinite complement

The claimed constant is fixed from the original input:

    C = sum_d d^k/(d-1) + sum_(d,j in F) d^j,
    g = ceil(C).

The amplification proof must cover the first selection as well as later ones. Its eventual formulas must ensure the chosen label is above the cutoff, outside F, and larger in numerical value than previous selections. A scale inequality with a multiplier merely described as greater than one does not already establish all those facts. They are explicitly part of the proposed proof obligation.

The essential gap estimate concerns retained labels strictly below each test value. It must include the chosen power itself as a boundary, powers of other bases on either side of a near-alignment, exact numerical ties, and scales between alignments. A prefix result at selected values alone would not suffice. Nor may the complement gap be increased with the number of selections. An eventual argument must pass to the actual infinite complement by control of every fixed finite value range; finite-prefix existence alone does not justify an interchange with the operation of taking subset sums.

The label convention is consistent throughout the packet and inherited proof. Only the selected occurrence is removed. Other labels with the same numerical value remain available. At numerical ties, all strictly smaller labels precede a label in a nondecreasing enumeration. These are the correct conventions for the inherited deficit-to-gap lemma. Finite deletions are charged in C; they cannot be discarded by silently claiming an unchanged zero-cutoff theorem.

The target asks for one Q that works for every nonzero character. CP25 section 4 shows why bounded selected exponent gaps for each active base are useful: convergence on selected powers would imply convergence on each full base tail, hence a rational denominator dividing powers of every active base. Collective gcd one is the relevant condition, not pairwise coprimality. Both rational and irrational characters are covered by that inherited argument, provided the new sequence has the required spacing. No common positive lower bound or Fourier convergence rate over all characters is demanded.

## The spectral and interval continuation

I checked the inherited CP25 proof in full and followed its CP24 dependency to the primary Griesmer interfaces. Definition 3.4 concerns Fourier-Stieltjes averaging of all unitary matrix coefficients. Lemma 9.5(ii) supplies its positive finite Radon measure characterization. Lemma 10.3 and Remark 10.4 specifically support sequential dominated convergence before passage to a cluster mean. Question 10.5 explains why merely annihilating characters with an arbitrary finitely additive mean is not an interchangeable input.

CP25 uses labelled Bernoulli subset choices to obtain one sequence of countably additive measures. Coincident sums accumulate probability. After every-character decay, the sequential argument supplies the full mean property, supported on the finite subset sums of Q. The fixed-gap complement supplies positive upper Banach density. Observation 1.3 gives an extreme invariant mean, and Corollary 4.2(ii) then applies with the precise mass inequality. The resulting intervals use disjoint Q and R labels. This is a coherent continuation if the new partition and spacing claims are proved.

The literature theorem remains a trusted input. I did not independently audit the entire underlying proof of Theorem 3.17. I also did not construct a new sequence, prove the new preservation lemma, or execute the described witness procedure. The exhaustive finite-prefix procedure is a legitimate prospective terminating algorithm once thickness is established, without any claimed feasible time bound. Its mathematical description does not authorize running it under this proof proposal.

## Exact connection to the original objective

Within the half-mass target, the proposed strict-mass minimum-four class and the class `min(E)=3 or sigma(E)<=1` are exact complements. Equality at one and the endpoint one half are retained by the complementary premise. On the first class, supports representing two consecutive integers give a legal signed unit after cancelling their common labels. They need not initially have disjoint supports; cancellation supplies disjointness. This validates the stated implication to obligation 28 as an admission-level route, with its separate bridge still requiring acceptance.

I also inspected the relevant downstream statements of obligations 29-31 and the half-signed-unit problem study. The existing route from half-mass units to the root needs a gcd-one core E of mass in `[1/2,1)`, the disjoint reserve outside E, and a separate solution of the original mass range `[1,2)`. Finite deletions in the unit assertion allow successive unit supports to avoid earlier supports, while the reserve supplies its independently fixed gap. Those are additional obligations, not conclusions of this proposal.

There is a material limitation to the contribution: the small cores used by this downstream route lie entirely in the new proposal's complementary premise. Success here would strengthen the available partition and thickness theorem but would not resolve the units needed on those cores. I record this as a nonblocking limitation because this is an analytical prerequisite proposal with an honest exact route, not a claim of necessary finite computation or root completion. In particular, the thickness of the full remaining supply cannot also be assigned to a supply disjoint from the already used complement reserve.

## Lineage, resource account, and novelty

The supplied packet records CP25's acceptance as acceptance 12, despite its historical proof and checkpoint headers still saying pending. I use that supplied acceptance record, not those historical headers, for the predecessor's status. The proposal binds its exact checkpoint and evidence manifest, creates a logical successor with no native parent, and leaves the old failed methods intact. The changed input is CP25's occurrence construction and its identified coefficient obstruction, not an attempt to resume the failed finite unit-switch method.

Account 2 has three used moves and no used runs or reservations, and preserves 24 historical moves from account 1. This is inheritance, not renewal. It leaves 21 moves in the current segment and 27 moves already used across the stated lineage. The native step-3 limit is tighter for the planned strategy. The proposal's nominal limits do not grant a fresh allowance or permission to execute mathematical programs. Necessity, significance, and renewal findings are empty because their corresponding finite-task, standalone, and renewal contracts do not apply.

The three exact bound studies give a bounded twenty-query novelty investigation. I checked their source classifications against the relevant primary texts. BEGL96 treats general sufficiency as a conjecture, proves results with stronger resource hypotheses, and describes strict mass as an expectation of easier completeness in its concluding discussion. Its dense-base proof uses disjoint resources. It is not the proposed strict-mass theorem. The recurrence and compact-group tools are classical and must not be claimed as the new contribution.

The inherited related report and its saved #254 excerpt concern an abundance assumption that fixed finitely many power streams do not satisfy. I did not verify its purported formal proof. The report is relevant to prior support-allocation ideas, not an accepted theorem for this input class. The bounded searches and selected hits do not certify originality or priority. An exact-unit novelty check remains due if the attack produces a candidate result.

## Reading and verification boundaries

I read the installed Codex README, the shared math-solver workflow, the constructive strategy and seed-and-amplify entry, and the SEARCH.md proposal, decomposition, provenance, and account contracts. I read the complete prescribed context packet, all three exact proposal studies, and their query log. Ordinary SHA-256 checks matched all fourteen listed input files to the packet. Canonical sorted compact JSON hashing reproduced both supplied subject and claim digests. The CP25 proof, CP24 proof, and pinned Griesmer text also matched their artifact names.

Evidence reading comprised the full frozen CP25 proof, its manifest, the CP24 manifest and full proof, the inherited primary-reading boundary record, and the relevant Mass manifest. CP25 repeats the elementary gap and character arguments needed here, so I did not audit every artifact in the transitive Mass/Core evidence graph. The proposed theorem has no evidence of its own yet.

Primary reading comprised the full local canonical Lean source and BEGL96 extracted text; Bergelson-Simmons around Claim 2.13 and footnote 10; the saved Li-Oprocha-Ye-Zhang primary HTML definitions and Lemma 2.1; and Griesmer Observation 1.3, Definition 3.4, Theorem 3.17's statement and displayed derivation, Corollary 4.2 and its proof, Lemma 9.5 and its proof, Definition 10.1, Lemma 10.3 and its proof, Remark 10.4, and Question 10.5. Reading the displayed derivation of Theorem 3.17 is not an audit of its underlying lemmas. I inspected saved recurrence excerpts, query-hit headings and relevant problem-discussion passages selectively; I did not read every unrelated search hit or fetch their full papers. I read the prescribed related-source addendum and its underlying saved #254 excerpt. Downstream root connection was checked using the relevant search-tree statements and the half-signed-unit problem study, without reading reviewer reports or full controller histories.

No author conversation, other review report, mathematical producer, experiment, formal checker, or controller mutation was used. A read-only inline metadata-hashing command was refused by a hook because its code argument was misinterpreted as an overlong path; standard jq and shasum utilities subsequently completed the digest checks. No hook configuration or managed state was changed. The only written files are this report and its accompanying Review-schema JSON, both created with apply_patch.
