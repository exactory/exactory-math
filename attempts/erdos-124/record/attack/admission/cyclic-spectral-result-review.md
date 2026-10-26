# Independent mathematical result review

Verdict: approve. No blocking mathematical defect was found in the exact checkpoint-000025 theorem. This is approval under the analytical reviewed policy, relative to the explicitly trusted Griesmer sumset theorem. It is not controller acceptance or a proof of the original completeness objective.

Reviewer: Godel, host thread `01a08011-97a1-7570-97c7-15ebe2b99cdb`. Both provenance fields use that identity, as specified by the host spawn receipt supplied in this review session. Source: `host`.

## Subject, independence and binding boundary

The prescribed packet is `attack/admission/cyclic-spectral-result-review-context.json`. The supplied full-checkpoint binding is `d4bd27ddc94cba4d102e89ba5c19266074b4ea8dea254df7d33625d0fac79dcd`; the supplied claim binding is `9bb854ce4d14bcf59bf06da3c57145500b68d36a1947ed48c401340978195000`. I read the checkpoint and exact claim embedded in that packet.

I did not independently recompute these two canonical object hashes. Attempts to read and hash files named for them under `attack/.search/blobs/` returned file-not-found. This does not contradict the supplied bindings: the packet provides the objects and the user expressly supplies their bindings. I neither searched controller state for substitute objects nor represented these unsuccessful attempts as verification.

I read the complete frozen proof at `attack/.search/artifacts/296ffdccd5bc5bf4f872201a3f6150b60ed4f820c19b8c2acbb95f61982732ee`, including all eight sections, and the complete requested unit draft. I read the main manifest's journal, problem and study artifacts, the three explicit dependency manifests, the local mathematical dependency proofs listed below, and the relevant primary source. Accepted labels were not treated as proofs.

The independence boundary is this fresh review context. I did not read the author's conversation, earlier reviewer reports, proposal or strategy reviews, search-tree history, or full controller status. The prescribed author-written packet, studies and proofs themselves include contextual descriptions of prior work. Those descriptions were visible; this is not a claim of blindness to author framing. I used the installed README, math-solver workflow, CASHOUT self-check, and ResultReview contract for procedure. No new literature search or research attack was undertaken.

## Exact mathematical statement

For each finite nonempty set D of distinct integers at least four, define sigma(D) as the sum of 1/(d-1), and define H by the inclusive condition sigma(D minus {h}) >= 1. Assume H is nonempty and gcd(H)=1. Fix any k>=1 and any finite set F of permitted occurrence labels. The claim constructs one infinite selected sequence Q and its complement R in the remaining supply P, with the stated gap constant, bounded selected exponent gaps for every h in H, divergent square character mass for every nonzero character, and legal intervals of every positive finite length in FS_0(P).

The proof's statement agrees with the packet's claim and the unit statement. There is no bound on D, k, F or L hidden in the proof. In particular, the hypothesis is collective gcd one of H, not merely gcd(D)=1, and not existence of a coprime pair. Numerical values may coincide across different labels.

## Recursive invariant and the complement

Write C=sum_D d^k/(d-1)+sum_F d^j, g=ceil(C), and W_i=sum_{r<=i}q_r. The least power q_i of the current cyclic base h_i strictly exceeding (h_i-1)(C+W_{i-1}) exists. Since C>=h_i^k/(h_i-1), its exponent is at least k+1. Since every deleted value is at most sum_F d^j<=C, q_i>3C avoids every deleted label. Also q_i>3(C+W_{i-1})>W_{i-1}; this proves strict numerical growth, absence of repeated selected labels, and divergence to infinity.

The buffer Delta_i=q_i/(h_i-1)-C-W_{i-1} is positive. If T=lcm_{d in D}(d-1), it belongs to (1/T)Z, so Delta_i>=1/T. This proves the claimed absolute positive bound. It makes no unjustified assertion about a normalized buffer.

The geometric estimate sum_{j>=k,d^j<x}d^j >= (x-d^k)/(d-1) is correct for all real x>0. At a power threshold its numerator uses the first power at least x, so the strict-prefix convention includes equality correctly. If x<=d^k the right side is nonpositive.

For an empty selected prefix, or before the first removed value, summing that estimate gives retained strict-prefix weight at least sigma(D)x-C>=x-C. The last inequality follows because H nonempty implies sigma(D)>1.

For a nonempty finite removal prefix or the infinite removal, let i be the last removed index with q_i<=x. This index exists in the applicable case and is finite. Use all strict-x-prefix labels from bases other than h_i, and all h_i labels of value strictly below q_i. Their original weight is bounded below by

    sigma(D minus {h_i})x + q_i/(h_i-1) - sum_D d^k/(d-1).

Subtracting the whole deleted weight and W_{i-1} is conservative even when some of these labels are absent from the subcollection. The current selection is outside it. Every later removed selection is greater than x. Thus the actual retained weight is at least x+Delta_i>x. No positive surplus in sigma(D minus {h_i})-1 is required. This handles the mass-one endpoint, x=q_i, and ties from other bases.

For every fixed x the infinite complement has only finitely many removed labels at or below x. The argument therefore applies to that complement directly. It does not interchange FS_0 with a decreasing intersection, and does not subtract the infinite total weight of Q. The same bound x-C holds for every finite complement and the infinite complement. It also proves that each retained supply is infinite and has unbounded prefix totals.

In any nondecreasing enumeration of retained labels, all strictly smaller labels precede a_n. Earlier ties only increase S_{n-1}. Consequently a_n-S_{n-1}<=C<=g. For finite prefix subset sums, the recurrence A_n=A_{n-1} union (a_n+A_{n-1}) preserves gaps at most g: disjoint spans have separating gap a_n-S_{n-1}; overlapping spans create no gap larger than a gap in a copy. The first prefix has a_1<=g. Since totals tend to infinity and zero is present, each interval of g nonnegative integers meets the infinite subset-sum set. The prescribed g remains fixed throughout.

## Bounded exponent gaps and all characters

The predecessor power to the least eligible q_i is at most its threshold, even if equality holds. Hence q_i<=h_i(h_i-1)(C+W_{i-1}). The preceding strict inequality gives C+W_i<(4/3)q_i. With M=max H and B=2M(M-1), this proves q_{i+1}<Bq_i.

Each h occurs every s=|H| selections. Thus q_{i+s}/q_i<=B^s, and the least positive E_h with h^{E_h}>=B^s bounds the difference of successive selected exponents of h between 1 and E_h. These bounds depend only on H. Least-power minimality is used for this upper bound, not merely for legality.

Suppose ||beta q_i|| tends to zero. For each h and every sufficiently late exponent j, choose the greatest selected exponent e<=j. Then 0<=j-e<=E_h and ||beta h^j||<=h^{E_h}||beta h^e|| tends to zero. The selected exponent and its sequence index tend to infinity; this is convergence along every sufficiently late power of h.

Choose nearest integers z_j to beta h^j with errors epsilon_j tending to zero. The integer z_{j+1}-hz_j=h epsilon_j-epsilon_{j+1} is eventually zero. The resulting recurrence epsilon_{j+1}=h epsilon_j and convergence to zero force eventual zero errors. Thus beta h^J is integral for some J for each h. Writing beta=a/b in lowest terms, every prime divisor of b would divide every h, contradicting gcd(H)=1 unless b=1.

For every nonzero beta the norms consequently fail to tend to zero. There is a beta-dependent positive epsilon attained infinitely often, and the sum of squared norms diverges. Q was defined solely from D,k,F and the fixed order on H. It is the same Q for every character, including irrational characters. No uniform epsilon or uniform Fourier decay is used.

## Full FS-mean and the sumset interface

The Bernoulli measures mu_n are finitely supported probability measures on Z supported in Y=FS_0(Q). Their Fourier transform is the product of (1+exp(2 pi i beta q_i))/2. Repeated numerical sums add probabilities. The absolute factors are |cos(pi beta q_i)|, so infinitely many factors are bounded below one at each nonzero beta. The products tend to zero off zero and equal one at zero.

For every positive finite Radon measure rho on the character circle, finite support permits interchange of integrals. The resulting continuous character-product integrands are bounded by one. Dominated convergence along the original sequence yields

    lim_n mu_n(rho_hat)=rho({0}).

Take a weak-star cluster point along n tending to infinity, or equivalently in the intersection of the closures of the tails. Every scalar limit just established passes to this same point for every rho; no diagonal selection over characters or measures is needed. It has eta(Y)=1 and eta(rho_hat)=rho({0}). This is precisely Lemma 9.5(ii), equivalent to the matrix-coefficient condition of Definition 3.4. The argument establishes a full Fourier-Stieltjes mean. It does not apply dominated convergence to a subnet of finitely additive means, or assume that character annihilation alone resolves Question 10.5.

For X=FS_0(R), nonnegative interval averages assign X mass at least floor(n/g)/n. Their weak-star tail cluster points are invariant on all bounded functions: a fixed shift changes at most 2|t| entries, giving an error at most 2|t| ||f||_infinity/n. Thus d*(X)>=1/g>0 under the source's definition. Observation 1.3 supplies an extreme invariant mean nu with nu(X)>0.

The exact Corollary 4.2(ii) hypotheses hold on the discrete abelian group Z: X and Y are numerical subsets, nu is extreme invariant, eta is an FS-mean, and nu(X)+eta(Y)>1 because eta(Y)=1. The conclusion is nu(X+Y)=1. No numerical disjointness of X and Y is required.

For any L>=1, intersect (X+Y)-j over 0<=j<L. Invariance and finite additivity give this intersection mass one and hence nonemptiness. The shift zero is included, so its chosen u lies in the nonnegative set X+Y. This produces L consecutive nonnegative integers. Combining a representation from R with one from Q is legal because the supplies are disjoint as labels. Conversely, every finite support in P splits between them. Therefore X+Y=FS_0(P), with no deduplication of equal-valued labels.

## Procedures and consequences

Repeated integer multiplication and rational comparison compute each selected label. Membership of a legal label in Q is decidable by running the strictly increasing sequence past its value and checking the finitely many selections. This also enumerates R.

For an interval witness, each finite prefix of P has finitely many labelled subsets. Their sums and supports are decidable finite data. An interval supplied by the existence proof has one finite support for each of its finitely many integers. Their union occurs in some prefix. Increasing-prefix search therefore reaches a successful stage and terminates. This proves totality on the stated domain despite the nonquantitative compactness input. No executable or finite enumeration was run in this review, and no complexity or exponent-height bound is inferred.

The sufficient condition sigma(D)>=1+1/(min D-1) correctly implies H=D, including equality. Cancelling common labels between representations of u+1 and u gives a legal signed unit. Neither deduction supplies the separate half-mass complement or a complete reserve argument. The empty-core and shared-prime observations correctly delimit this construction, not all possible representation methods. No extension to minimum three or root mass equality is approved here.

## Dependency reading and hash audit

The manifest chain is the main manifest `73f908145b8601b3f44dc351f0ac5330620a8e315aefc7e4eaba6484c336cb1e`, then CP24 manifest `c34b753e9129af8fd6fc65f54ef85887cee309ab7dddb872749b1aaa9d8c574a`, then Mass manifest `49c309e171825be70b3a3c683d9154b0d2871e2e0c22c82a36fcf628ec706d53`, then Core manifest `3e7c431c41912315994774e1ac3338ce3f47919d6677ff4394db38a9a9c40882`. All four raw file SHA-256 values were checked and matched their filenames.

I read the full CP24 proof `b2f2c285a623c8ae9ccfb38765f3579c0303f1b203f435391cd1d4ccc85dca3f`, the full Mass proof `3aa1c7292bb7b0b9f93026159b62a90cfa0e57930fb383a17451202658837924`, its consolidation `454bff7e31cd731e1a42c3ca88a2fa039767d4ef6f98d5d76b3154dd259b90a1`, and the full Core proof `f2e3fd8517cda7ce584a9f4d297bf9038fbc59f423c2058c9c4d03d0253acbdd`. Their raw SHA-256 values also matched. The actual reused mathematics is the elementary Mass gap argument and the CP24 spectral-mean and thickness transfer. The inherited high-mass completeness conclusions and their base partitions are not needed to prove this candidate. Reading the Core proof does not make its core-selection conclusion a necessary premise here.

The pinned primary source is John T. Griesmer, *Discrete sumsets with one large summand*, arXiv:2507.10512v1, https://arxiv.org/pdf/2507.10512v1. Its supplied text artifact `32880c56688e1e0e24eebf33c5400c9a8eafda5ba639da55f5eb022bc9a8ff30` was independently hashed with a matching result. I read Section 1.2, Definition 1.2 and Observation 1.3; the matrix-coefficient and FS-mean definitions through Definition 3.4; the statement and displayed proof of Theorem 3.17; Lemma 4.1 and Corollary 4.2 with their proofs; the spectral discussion around Theorem 9.3, polarization and Lemmas 9.4 and 9.5; and Definition 10.1 through Question 10.5, including the full proof of Lemma 10.3 and the sequential warning in Remark 10.4. These passages support the exact interfaces used above.

The source's main sumset theorem remains an explicitly trusted published input. Reading its displayed derivation does not amount to auditing its entire chain through the earlier main lemmas. I did not read the whole paper, verify every reference in it, inspect the original PDF, or independently verify its publication record. The inherited PRIMARY_READS artifact was read as an author's source-boundary record, not adopted as this reviewer's reading history. Older Fan and Bergelson-Simmons background results in the wider Mass package are not used by the elementary lemma extracted here, and their entire primary proofs were not independently audited. Nor was every unused study artifact in that wider closure read. The service's complete transitive freshness and policy audit remains separate.

The main proof's raw SHA-256 matched its supplied digest. The current local file named by unit.json's evidence field has that same digest. The journal excerpt has SHA-256 `3025e7aec35ce9817c4458432b3f8248d6fd56edb089b6ea8f4e03f768403156`, matching the frozen journal binding. These are actual byte-hash checks, unlike the supplied checkpoint and claim bindings noted above.

## Disposition

Approve the exact analytical result. No revisions are required for mathematical validity at the stated scope. Native draft evaluation is recorded separately at `attack/erdos-124-cyclic-spectral-thinning/units/1/evaluation.md`. Publication-level novelty, formal verification, controller acceptance, and original-objective closure are outside this approval. Only the three user-authorized review files were written.
