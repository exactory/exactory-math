# Local correctness review of carry-seed move 1

## Verdict and scope

The conditional lemma is valid under its stated hypotheses. I found no mathematical error in the maximum-gap identity, deletion formula, switch accounting, coverage implication and its restricted converse, or finite-buffer diameter argument. This is a local analytical review only. It is not admission, independent result acceptance, or root acceptance. No full-root proof is checked.

The missing construction remains missing: the move does not produce, for every admissible D and positive k, a family of legal switches satisfying both (2) and (5). The accepted all-future surplus theorem is used solely as an auxiliary theorem. Its acceptance does not establish that construction.

## Reviewed material and actual reviewer provenance

- Primary document: `<workspace>/erdos-124/attack/erdos-124-carry-seed/moves/01-support-ledger.md`, read completely.
- Expected SHA-256: `ad3653e614850bed80e1b8cbf8c588fd0f989fdaa3a3f38e965bd47d519f4343`.
- Observed SHA-256: `ad3653e614850bed80e1b8cbf8c588fd0f989fdaa3a3f38e965bd47d519f4343`. The digest matches.
- Auxiliary primary proof inspected: `<workspace>/erdos-124/attack/erdos-124-tail-surplus/moves/001-sunit-tail-surplus.md`, read completely to check the auxiliary statement and its scope of use. Its accepted status is supplied by the review request; the historical candidate-status wording in that file is not a new acceptance decision here. The imported published finiteness theorem was not independently reverified.
- Reviewer: the active Codex assistant in this conversation, performing this review directly. No separate reviewer agent, external reviewer, or formal verification service was invoked. The session instructions identify Codex as based on GPT-6; an independently authenticated runtime model build identifier is not available to this reviewer.
- Observed execution host: `<host>`; operating system: `Darwin`; local account: `<user>`.
- Host metadata was observed at `2026-09-07T15:43:30Z`.

The direct `shasum` command was rejected before execution by the managed shell hook as an unsupported operation. The digest above was obtained by applying Node's SHA-256 implementation in memory to the complete, untruncated UTF-8 document text returned by a permitted `cat` read. It matches the supplied raw-file digest. This was metadata hashing only. No mathematical computation, search, controller/native CLI mutation, proof edit, or formal build was performed. The sole requested output is this review file, written with `apply_patch`.

## 1. Infinite labelled maximum-gap identity

The sequence assumptions suffice. Positive integer terms make finite subset sums nonnegative integers. The infinite stream has unbounded prefix sums, so its subset-sum set is unbounded, and every element has a successor. Numerical ties do not identify occurrence labels or permit repeated use of a label.

The finite-prefix recurrence is valid. When the two hulls are disjoint, the gap between them has endpoints T_j and r_{j+1}. When the hulls overlap, a consecutive gap in their union lies within a constituent hull: it cannot pass through a hull endpoint lying strictly inside the gap, since that endpoint is itself in the union. Within that hull, its length cannot exceed the old mesh bound. The initial singleton prefix is handled by G_0=0. Thus the induction establishes the claimed upper bound.

For the infinite upper bound, two consecutive elements of C have finite representations and therefore both belong to one sufficiently long prefix. They are consecutive in that prefix as well, since an intervening prefix sum would also belong to C. This justifies passing from finite prefixes to the infinite set without assuming convergence of meshes.

The reverse bound is exact. The nonempty set of integer deficits is bounded above, hence its supremum is attained. Its first member is r_1, so K is positive. At an attaining index j, T_{j-1}<r_j. Every subset using only indices below j has value at most T_{j-1}; every subset containing an index at least j has value at least r_j, by positivity and nondecreasing order. These two represented endpoints are therefore consecutive in the full infinite set. In the document's phrase "later occurrence," the relevant group includes index j itself. Ties cause no exception to this argument.

## 2. Exact deletion formula and auxiliary quantifiers

Fix admissible D and k, with the admissibility in the auxiliary statement: D is a finite set of distinct integers at least 3, gcd(D)=1, sum over D of 1/(d-1) is at least 1, and k is an integer at least 1. Fix a finite set V of original occurrence indices. Deleting it leaves an infinite, nondecreasing, locally finite positive integer stream.

For a retained original index i, its preceding retained weight is exactly S_{i-1}-W_{i-1}. Thus (1) uses the correct original index and preceding deletion total. It ranges only over retained indices. Finite deletion does not authorize replacing distinct labels of equal value by a single value, and the derivation does not do so.

For this fixed V, the auxiliary theorem applied to the original stream gives S_{i-1}-a_i tending to positive infinity. Beyond the deleted indices, W_{i-1}=W is fixed, so the deficits in (1) tend to negative infinity. If V is empty, this equality holds throughout, without needing a last deleted index. Only finitely many deficits are positive. At the first retained index the preceding retained weight is zero, so its deficit is positive. Consequently the description as the maximum of finitely many positive candidates is justified, and Section 1 applies. No effective cutoff is supplied or needed.

The auxiliary statement allows each fixed D, k, finite deletion set, and bound to have its own threshold. It supplies no uniform threshold over changing switch families or their changing B. The move correctly preserves this distinction, including at reciprocal equality.

## 3. Switch legality, interval coverage, and total weight

Disjointness within each pair and pairwise disjointness of the pair unions ensure that any selection of one side per pair is an allowed subset of the original labels. Equal numerical powers in different labels remain usable separately. The residual stream is disjoint from every selected side because all pair labels are reserved in V.

Condition h_1=1 implicitly requires at least one switch. Empty individual sides are harmless when allowed as finite subsets; h_t>0 remains required. There is no requirement that the gains themselves be powers. Their subset sums describe changes between legal assignments, not additional terms in the power stream.

Starting with every P side and replacing exactly the chosen sides by Q gives precisely B plus the subset sums of the gains. Duplicate represented values are harmless. The finite Brown induction applies in the order stipulated in (2): adjoining a gain no greater than one plus the accumulated span leaves no missing integer between the two resulting intervals. The first gain supplies the base case. Hence the selected assignments cover the entire integer interval from B through B+H.

Because all reserved occurrence sets are disjoint, W is the sum of all P weights and all Q weights. The latter sum is B+H by the definition of H. Thus W=2B+H is exact, including multiplicities of numerical values carried by distinct labels. It follows that W-H=2B. The P sides contribute positive support cost even though they are subtracted in the gain identities.

## 4. Integer endpoints, equivalent condition, and restricted necessity

For every integer n>=B, x=n-B is a nonnegative integer. There is a largest residual subset sum c<=x because the candidates lie in the finite set of integers from zero through x and include zero. Its successor c' exists because the residual subset-sum set is unbounded. Maximality gives x<c', and integrality gives x-c<=c'-c-1. This is exactly the source of the minus one and the permissible bound K_V<=H+1. Adding the switch representation of B+(x-c) to a finite residual representation of c is legal by occurrence disjointness.

The endpoint convention is correct: an interval with integer endpoints B and B+H covers H+1 integers. A residual gap of exactly H+1 leaves successive translated integer intervals adjacent without a missing integer, although their real intervals do not overlap. Whenever interval notation denotes represented values, it is understood to refer to the integers in that interval.

Condition (4) is equivalent to requiring a_i-S_{i-1}+W_{i-1}<=H+1 at every retained i. Rearranging and substituting H=W-2B gives exactly (5), with right side 2B-1. Beyond the reserved indices it reduces to (6). No removed index creates an additional residual-gap obligation.

The claimed necessity is correct for the specific switch-interval method. If consecutive residual sums c<c' have gap greater than H+1, the integer B+c+H+1 lies beyond every translated interval based at a residual sum at most c, and below every translated interval based at a residual sum at least c'. It is therefore missing from the stated union. This checks the move's existing equivalence; it is not a claim that all representations in FS(A) obey that restriction. Other choices in FS(V), or a later threshold, are expressly left open.

The order of quantifiers is correct: for each fixed legal switch family satisfying (2) and (5), every integer n>=B is represented, with a choice of representation allowed to depend on n. Neither this implication nor the auxiliary theorem proves that such a family exists for each admissible input.

## 5. Finite-buffer diameter argument

Under the explicit hypothesis C=sum(U)>0, the finite Minkowski sum FS(V)+FS(U) contains its minimum zero and its maximum W+C. Its diameter is therefore exactly W+C. Translation does not change that diameter. Every subset of FS(V) has diameter at most W, so the proposed containment is impossible for every integer translation t. Internal holes in either subset-sum set have no bearing on this argument.

For the displayed zero-cutoff decomposition, R, V, and U are read as the disjoint partition inherited from the setup: U is removed to obtain the positive-cutoff system, V is reserved inside that system, and R is its remainder. Finite subset sums then split across the three sets exactly. Without that partition, a Minkowski decomposition would not automatically be a legal occurrence decomposition; the stated setup supplies it.

The obstruction concerns one fixed translation and one finite V handling every old V choice together with every U choice. It does not exclude selecting different representations for different targets or changing residual support. If U were empty and C=0, the strict diameter obstruction would disappear, but that case is outside this section's explicit C>0 hypothesis. The section appropriately limits its conclusion to the overstrong fixed-buffer rule.

## 6. Construction status and final wording

Section 6 correctly says that no legal switch family satisfying the required conditions has been constructed. The analytical implication and exact support ledger are established; the existence obligation for the full root remains open.

The final sentence, "It pays the obligations of the switch seed and its support-cost bound," cannot be used as evidence that a switch seed has been constructed or that its numerical support inequalities have been met for all admissible inputs. If it is intended to assert that discharge, it is an unsupported completion claim and conflicts with Section 6. It is defensible only as a statement about providing the conditional seed criterion and its accounting. No harness bookkeeping meaning of "pays" was adjudicated or changed in this review.

The conditional lemma is valid. No full-root proof is checked, and no root or construction acceptance follows from this report.
