# Primary-source reading and import boundaries

Date: 2026-09-08. This file records literature already inspected, not new mathematical execution.

## Griesmer

John T. Griesmer, Discrete sumsets with one large summand, arXiv:2507.10512v1, https://arxiv.org/pdf/2507.10512v1. The published record is DOI:10.1017/fms.2026.10205, but the proposed import is pinned to v1.

Local PDF: <workspace>/erdos-124/sources/griesmer2507.10512v1.pdf.
Local extracted text: <workspace>/erdos-124/sources/griesmer2507.10512v1.txt.

A proposal-bound copy is sources/griesmer2507.10512v1.txt in this preflight directory. It preserves every extracted character and adds a final newline after the terminal form-feed. The input digest binds that exact copy, not the PDF bytes. The original PDF and extracted text are retained unchanged.

Read the introduction's definitions of means and upper Banach density, Observation 1.3, Lemma 1.9 and its proof, Definition 3.4, Corollary 4.2 with its full proof, Lemma 9.5 with its full proof, Definition 10.1, Lemma 10.3 with its full proof, and Remark 10.4. Printed pages 18-19 and 34-35 were rendered locally and visually inspected after the web screenshot attempts failed. Other parts of the paper were not read in full. The statement of Theorem 3.17 was located, but its complete underlying proof is not claimed as inspected.

Proposed imported facts:

1. Every numerical set A of positive upper Banach density admits an extreme invariant mean nu with nu(A)>0, by Observation 1.3.
2. Corollary 4.2(ii) applies to arbitrary subsets A,B of a discrete abelian group: if nu is an extreme invariant mean, eta is an FS-mean and nu(A)+eta(B)>1, then nu(A+B)=1, hence A+B is thick.
3. Definition 3.4 uses FS to mean Fourier-Stieltjes averaging through unitary matrix coefficients, not finite-sum closure.
4. Lemma 10.3 and Lemma 9.5(ii) provide the relevant way from a SEQUENCE of countably additive probability measures with decay at every nontrivial character to an FS-mean. Merely declaring a finitely additive mean character-annihilating would leave the paper's Question 10.5 unresolved, and is not permitted.
5. Weak-star compactness of the space of means is available. The finite averages in Lemma 1.9's proof are ordinary means before a Folner hypothesis; its printed M_tau notation there must not be copied as a claim of invariance.

The unproved proposed application is to Bernoulli finite-subset-sum measures on an entire gcd-one power supply, respecting all occurrence labels. Neither its character decay, its FS-mean property, the final disjoint allocation, nor the new threshold is imported from this paper.

## Canonical problem

The complete local sources/124.lean was read again. Its Erdos124.erdos124.ne_zero has every positive cutoff, finite distinct bases at least three, reciprocal mass at least one and collective gcd one. The ne_zero_three_four_seven theorem is only cutoff one. The solved zero-cutoff statement has different hypotheses. The converse records Pomerance's necessary reciprocal mass one for finite base sets, and cites a pinned formal proof. Melfi's small-mass construction quantifies over infinitely many bases and cannot refute the finite-base threshold here.

The new T_4 claim is a strict-mass/minimum-four prerequisite, not the canonical original claim. Minimum-three inputs and reciprocal equality remain a separate original-domain obligation. Finite deletion is retained and can be handled only by a proved cutoff increase.

## Accepted local evidence, with exact scope

- Core: acceptance-000001, checkpoint-000008, attack/erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md. The full proof was read. Sections 2-3 construct a gcd-one seed containing the minimum with mass below one, without requiring the seed's mass to reach one. Its old cardinal bound is floor(m/2)+1, not the proposed logarithmic improvement.
- Mass: acceptance-000005, checkpoint-000016, attack/erdos-124-mass-partition/moves/001-high-mass-completeness.md. Sections 1-5 were reread, and the full proof was inspected earlier. Sections 1-2 and 5.1 give labelled bounded gaps and disjoint-reserve amplification. Section 5.2 proves that norms at every nonzero multiplier do not even tend to zero on any full finite gcd-one base supply with finite deletion; the proof of this intermediate fact needs no mass-one hypothesis. The final theorem has threshold 3+2/m.
- Quarter: acceptance-000006, checkpoint-000017, attack/erdos-124-quarter-mass/moves/001-quarter-mass-completeness.md. The full proof was inspected. The unconditional bound is 3+min{1/4,2/m}, giving T_4<=13/4. Its improvement is a three-supply allocation result, not the proposed FS-mean mechanism.
- WOC bridge: acceptance-000010, checkpoint-000023, attack/erdos-124-one-class-conditional/moves/002-woc-restricted-bridge.md, together with its Move 1. The exact implication only is accepted. WOC permits gcd greater than one and remains unproved. This proposal does not infer WOC from generic bounded gaps or from its new gcd-one averaging hypothesis.

These are accepted analytical results, not a new formal verification. Historical proof headers still say candidate; current acceptance IDs state their present controller status.

## Excluded discovery leads

Eggleston-type characterizing-sequence references were insufficient to justify a disjoint allocation here and are not imported. A research blog's Erdos254 claim was not verified; its increasing dyadic-abundance assumption is absent from finite fixed-base power supplies. Host-Kra Delta-star implications, ordinary Gaussian estimates and Cantor real-support results do not supply the new discrete once-only seed. None of these leads is a theorem dependency of the proposed rung.
