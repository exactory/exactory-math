# Independent analytical result review

Decision: approve the exact proof claim for node-000010, checkpoint-000016, obligation-000016, under the reviewed policy. No blocking mathematical gap was found. This is a result review, not a proposal review, controller acceptance, formal verification, or closure of the original objective.

## Subject and independence

The prescribed context supplies these bindings:

- Stored checkpoint digest: `98e41c9d8ea57e5aa3cb51b634cf7008427846c39dc9325b26c4dee9098fc735`.
- Claim digest: `0bb3cd98c01da1975ff7942d3c8120c112b4621b8fea5a10fa7c0d80e70c7e59`.
- Analytical evidence manifest digest: `49c309e171825be70b3a3c683d9154b0d2871e2e0c22c82a36fcf628ec706d53`.
- Accepted dependency: `acceptance-000001`, checkpoint-000008, obligation-000004.
- Dependency manifest digest: `3e7c431c41912315994774e1ac3338ce3f47919d6677ff4394db38a9a9c40882`.

Narrow metadata read from the non-login host shell returned `USER=<user>` and `CODEX_THREAD_ID=01a07db1-574d-7580-b5c7-7fa3ddfb15a9`. Reviewer provenance is therefore source `host`, actor ID `<user>`, attestation ID `01a07db1-574d-7580-b5c7-7fa3ddfb15a9`. The supplied author has actor ID `/root` and attestation ID `01a07806-b2c5-7163-86d2-92e8e272b9eb`. Both reviewer fields differ from the author's corresponding fields. These are actual host metadata values, not inferred identities.

This review used a fresh review context. No parent conversation or earlier review of the current proof was consulted. The inherited core's acceptance record was read only as part of the expressly prescribed dependency interface.

## Materials and identity limitation

I read the Codex README, the shared math-solver skill, SEARCH.md's requested checkpoint/result, public accept, and immutable-manifest sections, and the applicable CASHOUT.md few-lines rule. I read the complete current proof and consolidation, every artifact listed in mass-partition-001-manifest.json, the full saved Bergelson-Simmons text, core-001-manifest.json, and the complete inherited core proof. Fan's source was the manifest's saved primary-reader response, including its Lemma 2.2 and Corollaries 2.3 and 2.5 and their proofs. I did not claim to have read an unavailable raw HTML snapshot.

A direct `shasum -a 256` metadata check was refused by the PreToolUse hook as an unsupported managed shell operation. I did not retry it through another command, wrapper, interpreter, path, or controller operation. No digest was independently recomputed. All digests in this review and the accept spec are supplied bindings; the textual consistency checks below are distinct from byte-identity verification. The service must perform the immutable audit, including canonical checkpoint and claim hashes, manifest hashes, artifact bytes, external-source freshness, journal receipt, and complete transitive inventory. This optional hashing limitation is not a mathematical gap.

## Mathematical findings

### Exact claim and bounded gaps

The proof establishes eventual representation for every finite nonempty set of distinct integer bases D with minimum m at least three, collective gcd one, and reciprocal mass at least 3+2/m; every positive integer cutoff k; and every finite deletion F of allowed labelled occurrences. It retains coincident numerical powers as distinct resources. The threshold N may depend on D, k, and F. No bound on the size or largest element of D, pairwise coprimality, multiplicative independence, or uniform N is used.

The bounded-gap induction is valid for labelled finite subset sums. At each step the two copies of the previous subset-sum set have the same mesh bound within their spans. Disjoint spans introduce only the gap a_i-S_{i-1}, already bounded by g. For overlapping spans, a longer gap cannot pass a span endpoint without containing an available sum. The endpoints zero and S_i and the divergence of S_i then give a sum in every interval of g consecutive nonnegative integers. Deleting labels of total value W reduces each surviving preceding sum by at most W, so g+W is valid. Repeated numerical values affect neither argument.

The amplification interval has exactly the required length: for n at least A+g-1, the reserve interval [n-A-g+1,n-A] contains g nonnegative integers, and its chosen sum leaves a seed value in [A,A+g-1]. The supports are disjoint. The illustrative residue example only discusses the information available from a general gap bound and is not used to assert optimality for power supplies.

### Imported theorem and occurrence boundary

Bergelson-Simmons Lemma 2.12 states that the sum of two syndetic sets, and more generally two sets of positive upper Banach density, is piecewise Bohr. Definition 1.26 and the explicit application in section 2.1 give precisely the finite-dimensional torus, open set, and thick set formulation used here. Reference 4 identifies Bergelson, Furstenberg, and Weiss, Piecewise-Bohr sets of integers and combinatorial number theory, Topics in discrete mathematics, Algorithms and Combinatorics 26 (2006), pages 13-37; Lemma 2.12 attributes its assertion to their Theorem I. The imported assertion was checked in the prescribed Bergelson-Simmons source, not by independently reviewing the original BFW proof.

The numerical sets S_i=FS_0(B_i) with zero removed are syndetic, hence satisfy this theorem. They need not be disjoint numerical sets. Representations selected from them use the disjoint supplies B_1 and B_2, so their sums are legal. Only the inclusion into FS_0(B_1 union B_2) is needed and used. The proof does not rely on an equality with a sumset of nonempty subset sums.

Theorem 2.1 in Bergelson-Simmons has four numerical-set components. Its Theorem 1.23 discussion and footnote 6 explicitly distinguish numerical sets from the original occurrence convention when powers coincide. The current proof does not transfer those numerical-set power conclusions without checking multiplicities. It proves the necessary labelled lemmas itself. Fan's saved Lemma 2.2 gives exactly the finite correction extraction being adapted; its numerical disjointness assumption is replaced by disjoint label supports at every use.

### Tail group and all nonzero multipliers

The sets G_t are nested nonempty compact subsets of the compact orbit closure K. Their intersection G is compact. For two points of G, approximating the second point beyond the finite support chosen for the first proves closure under addition in every G_t. This avoids reusing an occurrence. The displayed convergent-subsequence proof of inverses uses positive multiples and is valid, so G is a closed subgroup.

If theta is outside G, character separation for closed subgroups of a finite-dimensional torus gives an integer character vanishing on G with nonzero beta=chi(theta). The proof requires divergence for this beta even if it is rational, and its hypothesis supplies exactly that. Signed representatives have magnitude at most one half. One sign has divergent total magnitude, so in every tail a first crossing of one quarter has total magnitude between one quarter and three quarters. Its character norm is at least one quarter. A convergent subsequence with supports tending to infinity has its limit in every G_t and thus in G, contradicting annihilation. Consequently theta belongs to G and G=K. This also proves density for each tail. No irrational-only assumption is silently substituted for the full multiplier condition.

### Finite correction and reserve

The nonempty piecewise-Bohr intersection ensures U meets K. Density of the correction phases shows that their translates of U cover K; compactness selects finitely many correction sums. Choosing one labelled representation of each and taking the union of their supports gives a fixed finite E. Those representations may share labels, since a single correction sum is selected in each representation of n.

Trimming long intervals of J by M=max D_0 and a bounded initial portion gives the claimed thick set T. Each n in T has n-u in the piecewise-Bohr set for a selected u, so it is represented on B_1, B_2, and E. The gap constant of C minus E is then taken after this exact deletion. Thickness supplies an interval of that new length. The final reserve and all seed representations have disjoint label supports. There is no circular choice of interval length and no unaccounted consumption of the reserve.

### Core, partition, and inclusive endpoint

The inherited core proof is sound under its stated assumptions. Strict gcd descent constructs a seed containing m with at most floor(m/2)+1 elements, which is at most m-1 for m at least three. At least one element exceeds m, making the seed's mass strictly less than one. The first crossing adds at most 1/m, preserving gcd one and the minimum, and gives the strict upper bound 1+1/m. This includes m=3 and m=4.

The current D satisfies every hypothesis of that accepted lemma. Removing its core C_D leaves mass strictly greater than 2+1/m. A first crossing in the remaining bases gives B_{1,D} with mass in [1,1+1/m), because every remaining base exceeds m. Subtracting these two strict upper bounds from the inclusive input bound gives sigma(B_{2,D})>1. All three base groups are nonempty and disjoint. Only C_D needs gcd one. Both strict inequalities survive at sigma(D)=3+2/m.

### Cutoffs, deletions, and arithmetic condition

The geometric lower bound using strictly smaller powers is correct for x at or below d^k and, otherwise, for the least r with d^r at least x. It remains correct when x equals a power. Summing it over a group and subtracting the total deleted value gives sigma(A)x-K_A. Every strictly smaller remaining label precedes a label of value x, irrespective of ties. Thus its ordered deficit is at most K_A when sigma(A) is at least one, and ceil(K_A) is a positive integer gap bound. Additional finite deletion has the claimed additive cost.

For a fixed base, convergence of the nearest-integer errors to zero makes the integer z_{j+1}-d z_j eventually zero. The resulting recurrence e_{j+1}=d e_j can converge to zero only with eventual zero error. Hence beta d^J is integral. Finite deletion leaves a full sufficiently late exponent tail for every base, so convergence on the correction supply implies this integrality for every base in C_D. A reduced denominator of beta must divide a power of each base; any prime in that denominator would divide their collective gcd. Therefore beta is integral. For each nonzero beta, the norm terms fail to tend to zero and their nonnegative series diverges. This verifies the full condition used by the group argument for every k and F.

The separate modular audit is also valid. Eventual stabilization of finite subset-sum sets modulo q makes their stabilizer contain every sufficiently late residue. Tail gcd one makes those residues generate the whole cyclic group. The nonempty zero-sum observation follows from equal partial sums. This audit is not an additional missing prerequisite of the stronger character proof.

### Termination claim

The described search is a terminating mathematical procedure on each admissible encoded input. The supplies can be enumerated from finite D, k, and F. Every test for a fixed pair (t,p) is finite. Once t contains the finite correction support furnished by compactness, the seed supply is thick for that fixed t, including an interval of its possibly large length g_t. Finitely many representations of that interval use a common finite prefix p of the other supplies. Dovetailing eventually reaches this pair. There is no requirement that this occur with p=t or with a uniform bound on t.

For each n beyond the stored threshold, the reserve gap bound ensures a finite subset in the prescribed interval, so exhaustive enumeration of finite subsets eventually finds one. Combining it with the stored seed support is legal. This termination proof does not execute or depend on enumeration, a solver, compilation, Lean, or a proof-producing program, and claims no complexity bound.

## Dependencies, policy, and remaining scope

The manifest's outcome, dependency IDs, and empty route bindings match the requested public accept spec. Its nine artifacts cover the proof, consolidation, input, studies, and saved Fan response. Its single external dependency pins the Bergelson-Simmons text containing the imported theorem and closed-subgroup facts. Its single manifest dependency is the core manifest, whose sole proof artifact was read in full and whose dependency and external lists are empty. The supplied accepted core is an analytical reviewed proof with no extra assumptions. There is no computational dependency in this closure and no missing local mathematical result used by the argument. Earlier counterexamples, discovery responses, the original conjecture's bibliographic sources, and the canonical Lean statement are background in the studies, not proof premises. Their referenced files are not needed to establish this checkpoint's exact claim.

Both contributing claims request reviewed proof, and both manifests have null verification. The result therefore fits analytical reviewed policy. It does not qualify as certificate or Lean-kernel evidence by this review. Actual immutable identity and continuing usability of the dependency remain subject to the service audit described above. No Exactory CLI or controller mutation was performed.

The CASHOUT.md rule says, "Does it follow from known literature in a few lines? If so, it is not a unit." Zero publication units are consistent with the stated internal-corollary disposition. Standalone novelty is not a condition for mathematical validity or approval of this obligation.

Approval is confined to obligation-000016. The original threshold-one objective, the complementary range 1<=sigma(D)<3+2/min D, and the mass-split implication bridge remain open. The public accept spec has no route bindings and cannot itself supply that bridge or root closure.
