I approve the exact mathematical result in checkpoint-000027 at the reviewed analytical standard. I found no mathematical blocker requiring a change to the frozen proof. This is a result review of the completed argument, not a strategy assessment, a unit evaluation or a formal verification.

The reviewer source is `host`. Both `actor_id` and `attestation_id` are `01a080ee-d787-7133-8589-2acbcbb3ca27`, distinct from the two authors identified in the prescribed packet. This review continues my original independent reading after its interruption. No incident or software verdict contributes mathematical evidence.

The subject digest is `b7d221ac6246cfe3ef3cc79083deb5f85cfeb1302451e000de9374fc6c54a427`. The claim digest is `69e557b241451524ca4540ec5090c992ec62ae738c9a0f588cd660399ca8ea11`. The evidence manifest is `4b0fa9c759a1b72def0fb17518f2cfb96eff8fb106ca417511116d35ee7f7c66`, with the sixteen artifacts and empty mathematical dependency lists specified in the prescribed context. The two mathematical artifacts are the [complete proof](<workspace>/erdos-124/attack/.search/artifacts/7af43ece21265de1190a3e22831f107251b6a8488e16fcc2745a853231f87551) and its [complete consolidation](<workspace>/erdos-124/attack/.search/artifacts/6e8c9e55b3a5d6a7603c7e2cf8125d9a107bf7dc99c57d53ab2ba1278911416f). Section and equation references below refer to the proof; the consolidation reproduces the same numbered argument.

The reviewed statement quantifies over every nonempty finite set D of distinct integers at least 3 with gcd(D)=1 for which there are an integer B>=2 and a nonempty finite set A of positive integers such that R={B^a:a in A} is contained in D, sigma(R)>=1/2, and V=D minus R has min(V)>=4 and sigma(V)>1. For every integer k>=1 and every finite forbidden set F of labels (d,j) with d in D and j>=k, there is an integer N(D,k,F) such that every integer n>=N has a finite positive representation by the remaining labels. Each label may be used once; coincident numerical values with different labels remain available separately. The proof establishes this statement without changing the order of these quantifiers.

I checked the constants and the deletion estimate directly. With sigma=sigma(V), delta=sigma-1, M=max(V), and

    C = sum_{d in V} d^k/(d-1) + value(F_V),
    g = ceil(C),
    K0 = 2+2/delta,
    epsilon = delta/[4(sigma+2K0)],
    eta = delta/(2 sigma),
    Lambda = 2M+2/eta,

the strict mass hypothesis gives 0<epsilon<1/4, 0<eta<1/2, K0>2, and Lambda>max(2M,2/eta). These parameters are fixed before the first unit. There is no charge based on the eventual R supports hidden inside C or g.

For equation (5), let m=ceil(z) with z>1. Each geometric sum (p_d(z)-1)/(d-1) is an integer. Their sum is at least sigma(m-1)>m-1, hence at least m and therefore at least z. Adding sigma proves the stated lower bound on sum p_d(z)/(d-1). This use of integrality is valid also when z is an integer and needs no coprimality of V. Equation (6) uses the least power at least x, so it correctly describes a strict prefix even at x=d^j.

At a scale x with a removed correction at most x, choose the latest such correction q and let W be the sum of every earlier selected V value. Growth makes corrections strictly increasing, so later removals cannot affect this prefix. From q>2MC and epsilon<1/4, equation (7) puts every aligned a_d above d^k. Also a_d/d<q. Thus the chosen powers strictly below a_d are legitimate original powers strictly below q. Subtracting the entire finite F_V charge and W can overcharge a subcollection, which only weakens a lower bound.

The three ranges in Section 2 give the following bounds for the retained strict-prefix total.

| Range | Verified lower bound | Reason for the current correction charge |
| --- | --- | --- |
| q<=x<=(1+epsilon)q | x+(3delta/4)q-C-W | Taking a_h=q excludes its label from the chosen subcollection. |
| (1+epsilon)q<x<=K0 q | x+(3delta/4)q-C-W | The whole strict prefix is used and the single current label q is subtracted. |
| x>=K0 q | x+(2delta+1)q-C-W, hence at least x+q-C-W | Equation (6) pays for all prior corrections and the current q. |

In the intermediate range, z=x/((1+epsilon)q)>1 and b_d(x)=a_d d^r with r>=1. Since d^r>=z, the least-power definition gives b_d(x)>=(1-epsilon)q p_d(z). After the current q is subtracted, the excess over x is

    [delta-epsilon sigma-(2epsilon/(1+epsilon))(x/q)]q-C-W.

It is at least [delta-epsilon(sigma+2K0)]q-C-W=(3delta/4)q-C-W. In the far range, delta K0-1=2delta+1. The ranges cover their boundary points and every x>=q.

Because eta<min(3delta/4,1) and C+W<q/Lambda<(eta/2)q, these estimates imply equation (11). Before the first removed correction relevant to x, equation (6) instead gives sigma x-C>=x-C. Consequently equation (12) holds simultaneously for all x>0 after every finite eligible list, with the same original C. The single W includes corrections from all earlier pairs. Equal numerical powers are counted by label in the geometric sums; removing q subtracts one occurrence only. Growth also gives q>C, which excludes every original forbidden V label, and q>h^k, which establishes the cutoff condition for the selected base h.

Section 3 correctly converts this estimate into a gap statement. In the nondecreasing labelled supply, every strictly smaller value precedes a_i, so a_i-S_{i-1}<=C<=g. For a finite prefix, adjoining a_i gives E union (a_i+E). The only possible gap between disjoint spans is a_i-S_{i-1}; within overlapping spans a gap is bounded by a gap of one copy, and cannot cross a span endpoint without containing a point of the union. The first gap is at most g. Prefix endpoint sums tend to infinity. An interval of g nonnegative integers missing all subset sums would then lie between consecutive finite-prefix sums separated by at least g+1. This proves the required gap property of the actual retained supply, including its lower endpoint at zero. No inference from bounded gaps to a signed unit is used.

Section 4 proves the necessary radix restriction rather than assuming it. For B>=4,

    sum_{a>=1} 1/(B^a-1) <= B/(B-1)^2 <= 4/9 < 1/2.

The second inequality follows upon expansion from (B-4)(4B-1)>=0. For B=3, omitting a=1 gives the geometric bound 1/4. Thus only the prime radices 2 and 3 can occur, and a qualifying ternary R contains 3. Since every R base is divisible by B, gcd(D)=1 supplies at least one c in V coprime to B. V itself can have nontrivial gcd. There is no additional collective-coprimality case to discharge on this domain.

For an arbitrary finite forbidden R set, choose K_R at least k and above all its exponents. A sufficiently large common multiple L of A satisfies L>=a K_R for each a. The map

    (a,t) -> (B^a,L/a+t),     t>=0,

is injective on labels, and after division by m=B^L its values are B^(at). At a positive level r carrying B^r, the sum of smaller normalized weights is exactly

    sum_{a in A} (B^(a ceil(r/a))-1)/(B^a-1)
      >= (B^r-1)sigma(R) >= (B^r-1)/2.

The formula remains correct when a divides r. Starting with the labelled copies of 1, every next weight w satisfies w<=2T+1. The three signed translates of [-T,T] therefore fill [-T-w,T+w]. Tied weights only increase the preceding T. Since the finite-prefix totals are unbounded, every integer has a finite normalized signed representation. Restoring m gives every multiple of m on R labels avoiding the arbitrary finite exclusion, with coefficients in {-1,0,1} and disjoint positive and negative supports.

The recurrence in Section 5 is compatible with the actual modulus. Invertibility of c modulo m supplies a positive period t with c^t=1 modulo m. For this t, set theta_d=t log(c)/log(d) modulo one. Cover the finite-dimensional torus by finitely many sets of diameter less than rho. One set contains n theta for infinitely many indices n. Two indices in this set can have a positive difference u above any prescribed bound, and translation invariance gives ||u theta_d||<rho in every coordinate. Infinitely many indices suffice even when there are only finitely many orbit points. No assertion of density in the full torus or intersection of independent return-time sets is necessary.

Choosing rho below the three bounds displayed in Section 5 makes q=c^(tu) satisfy 1-epsilon<d^{n_d}/q<1+epsilon for all d. The arbitrarily late returns allow q>Lambda(C+W) simultaneously, and q is already 1 modulo m. Equation (7) then forces the nearby powers above their cutoffs. Replacing m and t at the next unit is legitimate because the argument applies separately to every finite current modulus. The tolerance on V remains fixed.

The finite search descriptions in Sections 5 and 6 have mathematical termination arguments. A modular period exists in the finite unit group. Each rational phase test terminates by increasing powers of a base, and some sufficiently late period multiple passes all tests. The normalized signed prefix eventually reaches the target absolute value, allowing the three-interval induction to be reversed. There are exactly g-1 units. A sufficiently long reserve prefix contains the required gap interval within its span, so finite subset enumeration would find its witness. These are proofs of existence of terminating procedures, not executed computations or efficiency bounds.

Section 6 maintains capacity in both signs. Before each unit, K_R excludes F_R and both R supports of every preceding unit. A fresh eligible V power q is selected using the current global W. A signed R representation of 1-q exists because m divides 1-q; adding the positive label q gives an exact signed unit. R and V are disjoint sets of bases. The R supports are fresh by the cutoff choice and the V label is fresh by growth. Only that one V label is charged to the reserve, followed by W:=W+q. Arbitrarily large R supports do not enter V's deletion charge.

For r=g-1 units, let H be the sum of the negative-support values. Choosing the positive support instead of the negative support in the first t pairs gives H+t for every integer 0<=t<=r. Thus the finite seed represents [H,H+g-1] positively. Its labels are disjoint from the final unused V supply. For n>=H+g-1, the interval [n-H-g+1,n-H] contains exactly g nonnegative integers and hence a reserve sum v. The difference n-v lies in the seed interval. Combining the two positive supports represents n legally. Both endpoints, all finite deletions, all original exponents j>=k, and all cross-base numerical coincidences are handled. N=max(1,H+g-1) is chosen before n.

I also checked the scope comparisons in Section 7 against the actual CP22 interface, which dedicates whole correction bases C and requires sigma(D minus (R union C))>=1.

| Input D | Chosen R and its mass | V mass | Why CP22 cannot apply |
| --- | --- | --- | --- |
| {3,4,5,6,7,8} | {3}, mass 1/2 | 153/140 | The only ternary seed is {3}; every nonempty correction set costs at least 1/7, leaving at most 19/20. The binary supply {4,8} has mass 10/21<1/2. |
| {4,5,6,7,8,9,10,11,12,32} | {4,8,32}, mass 331/651 | 4133/3960 | Every proper binary subset has mass at most 10/21. There is no ternary seed because 3 is absent. A correction set coprime to 2 contains an odd base from {5,7,9,11}, costing at least 1/10 and leaving at most 3737/3960. |

Both inputs have gcd one. Direct addition gives 331/651=(217+93+21)/651 and 4133/3960=(990+792+660+495+440+396+360)/3960. For the first input, the total mass is 223/140, which is less than 11/6. Larger radices are already excluded by the general radix bound. Thus the examples do establish additional inputs beyond CP22's exact criterion. The separate historical theorem described by the 11/6 threshold was not supplied for re-review; my independent check of that comparison is the numerical inequality, not a new audit of its historical acceptance or proof.

For min(D)=3 and sigma(D)>3/2, the choice R={3} gives sigma(V)>1 and min(V)>=4. This consequence retains the theorem's standing gcd(D)=1 condition. It is one consequence of the same structural theorem, not a second proof or a separately reviewed checkpoint. The one-correction count is minimal within the stated recipe because every R value is divisible by B; this supplies no global optimality result for supports or N.

The dependency claim is accurate at the analytical standard. The proof itself supplies every needed prefix, gap, lattice, radix, modular-period, recurrence and amplification argument. The [CP22 proof](<workspace>/erdos-124/attack/.search/artifacts/f7541a762551247db3b8caf7ecd34f83e4c2d275da4dc59db9a108018f0d2865) and [CP26 proof](<workspace>/erdos-124/attack/.search/artifacts/1f1912a836b82220847fe89d5ce85f971165a7324f501e43699f92d46847d270) identify prior local interfaces, but no accepted theorem from them is required as a premise. CP26's spectral and full-supply thickness conclusions are not used. Empty accepted-dependency, external-dependency and route-binding lists do not conceal a mathematical premise. The ambient mathematics includes elementary logarithms and compactness of a finite-dimensional torus in ordinary classical mathematics, as the proof explicitly acknowledges.

The [canonical file](<workspace>/erdos-124/attack/.search/artifacts/7020ea91f349a2cb5807aced480e0c8604962f28674cc705d0dd2a985570ba1b) defines sumsOfDistinctPowers using a finite set of exponents for each base. Its pointwise sum over the finite base set permits the same numerical value from different bases to be used separately. The positive-cutoff declaration erdos124.ne_zero quantifies over k!=0 in the natural numbers, finite D, the reciprocal-mass condition and gcd one, followed by eventual membership. This matches the original objective's cutoff and label interpretation. The cutoff-zero declaration is separate. The file contains proof placeholders, so reading it checks the statement, not a completed formal proof.

The [supplied BEGL1996 text](<workspace>/erdos-124/attack/.search/artifacts/bee3747819fd4f0eb806190666cca0cb2dd57ada40d972d8b0848e8a8ed8b93d) was read in full, including its introduction, Theorem 1 and proof, concluding Theorems 2 and 3, small examples and references. Theorem 1 starts from an infinite base sequence of positive upper density and selects a finite subset depending on the cutoff. That quantifier pattern does not settle the current theorem for each fixed finite D. The interval-base results and reported cutoff-one examples likewise do not supply the full current structural assertion. This is a scope comparison, not a re-verification of their external machinery.

The [return-time extract](<workspace>/erdos-124/attack/.search/artifacts/6d4b587b0192d9adecdb0ef78f7a0e5e38cb7efdb1a78df628e0e09588cdcc2e) includes the definitions of minimality and positive syndeticity, the return-time sets, and Li, Oprocha, Ye and Zhang's Lemma 2.1(2). That lemma concerns the return times of a minimal point to each neighborhood. CP27 proves the weaker arbitrarily late return property directly, on the generator already multiplied by its modular period, and does not require this lemma as an external dependency.

The reading boundaries and verification limits are as follows.

| Material | Reading performed |
| --- | --- |
| Installed Codex README, Codex math entry and shared math-solver SKILL | Read for the workflow and analytical review boundary. The relevant SEARCH ResultReview, checkpoint and immutable-manifest instructions were also read. |
| Original prescribed context and resume context | Read completely, including the original contract, exact checkpoint claim, authors, all sixteen manifest entries, dependency declarations and allowed immutable paths. |
| New proof and consolidation | Read completely before the interruption and again from the prescribed immutable copies on resumption. Every operative mathematical argument was checked independently. |
| Frozen problem.json and one-move journal | Read completely to compare the exact claim and the reported analytical evidence with the proof. Their assertions of local closure were not treated as proof authority. |
| Top novelty.md, study/problem.md and study/make-the-proof-constructive.md | Read completely during the original review from the same immutable artifacts. |
| study/QUERY_LOG.md, study/novelty.md and study/ADMISSION_SCOPE.md | Read completely. ADMISSION_SCOPE is the packet's prescribed study note and contains a summary of earlier admission constraints. No underlying admission-review file was inspected, and that summary was not used to establish mathematical correctness. |
| canonical-124.lean | Read completely as source text only. No imported library source, linked formal proof or Lean process was inspected or run. |
| begl1996-extracted.txt | Read the entire supplied extraction of all six pages. No PDF rendering or independent typographical audit of the original PDF was performed. |
| return-time-primary.txt | Read the supplied extract through its end, around source line L213. The relevant check was limited to the recurrence/minimality definitions, Section 2.3 and Lemma 2.1(2). The full 1,035-line source paper was not read. |
| Three raw search-batch JSON files | Their roles and digest bindings were read in the manifest; their noisy hit contents were not read. The twelve-query log and studies provided the bounded discovery record. No claim of exhaustive novelty is based on those batches. |
| CP22 historical proof | Read its exact claim and Sections 1-8, including the lattice, modular correction, fixed-gap reserve and radix restriction. Section 9's author checks were not read. |
| CP26 historical proof | Read its exact claim and Sections 1-4 for the deletion and compact-return interfaces, plus the opening of Section 5 returned with the selected excerpt. Its later spectral argument was outside this comparison and was not reviewed. |

No author conversation, scratchpad, main research note, progress report, underlying admission or strategy review, other result review, unit draft, unit evaluation, runtime code or incident report was read for the mathematical review. No delegation occurred. The prescribed scope note is the expressly identified reading exception to any broader description of avoiding summaries of previous review constraints; it supplied no proof premise.

All resumed research reads used the specified immutable paths. I attempted a read-only hash command, but the host rejected it before execution as an unsupported managed shell operation. I did not bypass that rejection and do not claim independent recomputation of the artifact hashes. The digest identities in this review are the supplied immutable bindings; their byte freshness and controller acceptance remain subject to the separate service audit. This limitation does not supply a mathematical objection to the text actually reviewed. No mathematical program, finite search, solver, formal build, native/controller mutation or proof/evidence edit was performed.

This approval establishes the restricted theorem at the reviewed analytical standard. It does not establish complement mass equality: delta=0 invalidates the constants and the strict integer-margin argument, and taking a limit is not an equality proof. It supplies no signed lattice for arbitrary mixed bases of half mass. Every input to this theorem has total mass greater than 3/2, so it cannot by itself resolve the original mass-one cases. The complete original objective, complementary obligation-000053, bridge obligation-000054 and all nonqualifying structural cases remain outside this approval. No quantitative fraction of root completion is assigned.

Unit-level novelty, publication priority, draft evaluation, formal-kernel verification, immutable-evidence acceptance and root closure are distinct tasks. None is certified by this review. There are no required mathematical repairs to report for the exact frozen checkpoint claim.
