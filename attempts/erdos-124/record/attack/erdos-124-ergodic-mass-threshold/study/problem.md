# Problem study: a critical reciprocal-mass threshold

Date: 2026-09-08. Proposed slug: erdos-124-ergodic-mass-threshold.
Status: pre-admission study. No new proof move or mathematical process has run.

## 1. Queries

The complete fixed batch is [QUERY_LOG.md](QUERY_LOG.md), with every query, date, source restriction and raw response. Twelve problem/discovery queries and seven neighbouring-statement queries cover the problem and the two related statements below; seven additional queries study the selected ladder strategy. Each group includes arXiv, Semantic Scholar, Crossref, zbMATH Open and the problem's own database at its floor. These are web-index queries, not exhaustive API searches.

## 2. Exact target and neighbouring statements

With sigma(D)=sum_{d in D}1/(d-1) and P_4(t) denoting the assertion that for every nonempty finite set D of distinct integers at least 4 with gcd(D)=1 and sigma(D)>=t, every integer k>=1 and every finite set F of labels (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N is a sum of finitely many remaining labelled occurrences d^j, each pair used at most once and coincident numerical values retained separately, the threshold T_4=inf{t>=1:P_4(t)} equals 1.

P_4(t) is monotone: increasing t asks for completeness of fewer base sets. T_4 is well-defined in [1,13/4] using the accepted Quarter theorem. The value one is the original problem's necessary reciprocal-mass boundary for finite base sets, as recorded in the canonical converse. It is not a numerical name assigned to the gcd-free WOC yes/no hypothesis.

The primary neighbour to be attempted is the following proposed unconditional rung, not a known result:

For every nonempty finite set D of distinct integers at least 4 with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=b(m)=2+1/(m-1)+(floor(log_2(m))+1)/m, every integer k>=1 and every finite set F of labels (d,j) with d in D and j>=k admit N(D,k,F) such that every integer n>=N is a sum of finitely many remaining labelled occurrences d^j, each pair used at most once and coincident numerical values retained separately; moreover b(m)<=37/12 for every integer m>=4 and b(m) tends to 2 as m tends to infinity.

The other neighbour is the open strict-mass assertion for finite gcd-one bases at least four with 1<sigma(D)<b(min D), every positive cutoff and finite deletion. It is the exact remainder between the proposed rung and T_4=1. The original objective additionally retains all minimum-three inputs and reciprocal-mass equality. Neither neighbour replaces the full original claim.

The intended root implication is: T_4=1 gives each strictly-superunit minimum-four input by an admissible mass threshold below its own mass; the remaining original-domain assertion handles minimum three and equality. This is a proposed explicit bridge, not accepted root closure. Raising a cutoff beyond a finite deletion is a separate elementary part of any representation proof.

## 3. Hits worth reading

The source identifiers, exact read boundaries and import conditions are in [PRIMARY_READS.md](PRIMARY_READS.md).

- The canonical problem page and local formal statement distinguish the open positive-cutoff problem from solved zero cutoff, cutoff-one base triple, necessary mass and infinite-base construction.
- Griesmer, arXiv:2507.10512v1, Corollary 4.2(ii), offers thickness from a positive-density set and a set of full FS-mean mass. Definition 3.4, Lemmas 9.5 and 10.3 identify the genuine averaging requirement.
- Accepted Core, Mass and Quarter proofs supply the existing finite gcd seed, full-multiplier nonconvergence, deletion-stable bounded gaps and the three-supply threshold.
- The accepted WOC implication isolates a costly density input but does not prove that input. Griesmer's theorem suggests a different unconditional application with a small gcd-one averaging supply, not WOC for a possibly non-coprime single supply.

Other returned hits were irrelevant or supplied no stronger matching theorem. Every hit remains in the raw responses, not silently discarded as proof evidence.

## 4. Constraints learned

The earlier three-supply proof uses two mass-one density supplies and a mass-one gcd-one correction/reserve. A new proof must identify the actual row whose mathematical input changes; merely tightening a partition constant is not the proposed method.

The prospective new chain is: keep one mass-one density supply and an independent mass-one final reserve, while attempting an FS-mean of mass one on finite sums of a much smaller gcd-one power supply. Such a mean would allow direct thickness by Griesmer, avoiding the old second positive-density requirement and the finite Bohr phase-correction stage. Every one of these new application steps remains to be proved after reservation.

The support on the numerical finite-sum set need not be uniform, because different labelled subsets may have the same value. Each finite probability measure must be the pushforward of independent labelled Bernoulli choices. A finitely additive character-annihilating mean alone is insufficient. No exchange of a net limit and a spectral integral is permitted.

The two mass-one supplies must be disjoint from each other and from the full averaging supply. Choosing an interval first and then charging its support to a reserve whose gap depends on that interval would be circular. No such reuse is planned.

The proposed logarithmic gcd-seed bound, reciprocal allocation inequalities, uniform 37/12 bound and limiting value two are new analytical tasks, not facts established during this study. Minimum four is part of their exact proposed scope. The accepted minimum-three and common-radix results remain available on their own domains.

## 5. Stop reason and novelty boundary

The fixed ceiling of26 queries was reached. No exact proof of T_4=1 or the stated unconditional b(m) rung was found in that batch. This is a bounded literature-search finding, not a claim that no proof exists or that a future result is publication-level novel. Before any cash-out unit, its final exact statement will receive its own required novelty check.
