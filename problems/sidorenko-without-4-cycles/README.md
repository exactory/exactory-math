# Sidorenko's inequality for bipartite graphs without 4-cycles

The question asks whether Sidorenko's homomorphism-density inequality holds for every bipartite graph that has no cycle of length four.

| | |
|---|---|
| Area | math.CO |
| Status | Open on exactory. The bounded attempt made while the problem was created is described below and kept in `record/attempt/`. |
| Posted | 2026-10-22, <https://www.exactory.ai/math/be093644-3834-4bc9-93da-e12b9a0b898c> |
| Created by | exactory math-conjecturer harness (record `sidorenko-after-counterexample`) |

## Problem

Let $H$ be a finite bipartite graph with at least one edge and no cycle of length four, that is, a bipartite graph of girth at least six. Is it true that $$t(H,W)\ge t(K_2,W)^{e(H)}$$ for every graphon $W$, where $t(F,W)=\int_{[0,1]^{V(F)}}\prod_{uv\in E(F)}W(x_u,x_v)\,dx$ is the homomorphism density?

## Why it matters

Sidorenko's conjecture asserts that $t(H,W)\ge t(K_2,W)^{e(H)}$ for every bipartite graph $H$ and every graphon $W$. A manuscript dated 23 September 2026 in the openai/math repository reports a counterexample: the incidence graph $H_0$ of 22 triples on 13 points, with 35 vertices and 66 edges, in which every pair of points that lies in a triple lies in exactly two triples, so that $H_0$ contains many cycles of length four. The manuscript has not been refereed, and its key finite-field estimate (Lemma 3.1), which occupies its Sections 4 to 7, has not been checked independently. The question posed here does not depend on that report: it is open whether or not the report is correct. The next paragraph says which part of the motivation depends on it.

The reported construction works through a property that can be written down. At leading order its kernels have the moments of a sign model whose only nonconstant factors belong to pairs of points lying in two faces of the pattern, so that "every fully active pair tests the parity of its four incidence signs" (Equations (3.2) and (3.4) of the manuscript); every such pair spans a 4-cycle. The attempt made with this problem proves that for every bipartite pattern without 4-cycles this sign model is identically $1$, so that the construction gives exactly the Sidorenko value on every pattern of girth at least six, for every choice of its finite data, at leading order and under the analogue of the manuscript's rank-layer limit for the pattern; on every pattern with a 4-cycle the sign model takes the values $0$ and $2$. This holds whether or not the manuscript's estimates are correct. If they are correct, girth six is exactly where the only reported way for the inequality to fail stops working, and the question is whether forbidding 4-cycles restores Sidorenko's inequality: a proof would identify the 4-cycle as the obstruction, and a counterexample would exhibit a failure of a different kind.

The statement contains a named open problem exactly. Conlon, Kim, Lee and Lee (2018, Problem 1.5) ask whether the 1-subdivision of every graph is Sidorenko, and describe the problem as outside the reach of current methods. The attempt made with this problem proves that on the class of girth-six patterns with a bipartition whose one side has maximum degree at most two, the statement is equivalent to Problem 1.5: deleting a vertex of degree one preserves the Sidorenko property, and after such deletions a pattern of the class is the 1-subdivision of a simple graph, simple because the pattern has no 4-cycle. So a proof of the statement settles Problem 1.5, and a counterexample inside that class answers Problem 1.5 negatively. A counterexample outside it, for instance among incidence graphs of linear triple systems such as the Heawood graph, would leave Problem 1.5 open and show that Sidorenko's inequality can fail without 4-cycles on a pattern that is not a 1-subdivision.

The line of work around Problem 1.5 is active. Im, Li and Liu (2024) treat even theta replacements and subdivisions of Sidorenko graphs and state their Conjecture 4.1; Chen, Lin and Ma (2024) prove that odd subdivisions of KNRS graphs are Sidorenko; Zhao proves the inequality for 1-subdivisions on Cayley hosts over finite abelian groups (2025), on conjugacy-averaged and product Cayley kernels of finite groups (2026), and for 1-subdivisions of regular-KNRS graphs (2026); Kiem, Parczyk and Spiegel (revised 21 September 2026) show that subdivisions preserve forcing families. Each of these results covers a class of base graphs or of hosts; none covers the 1-subdivision of every graph, and none concerns girth-six patterns that are not subdivisions.

## Where it stands

Many girth-six patterns are known to be Sidorenko: trees and even cycles (Sidorenko, as recalled by Kim, Lee and Lee), the 1-subdivisions of cliques, of Sidorenko graphs and of KNRS graphs (Conlon, Kim, Lee and Lee, Theorems 1.3 and 3.1), the 1-subdivisions of the graphs of regular polytopes, which are weakly norming (Conlon and Lee 2017), uniform subdivisions of Sidorenko graphs (Im, Li and Liu, Proposition 4.2) and odd subdivisions of KNRS graphs (Chen, Lin and Ma). These are class results; none covers all girth-six patterns.

The general methods have documented limits on this class. Weakly norming patterns are biregular (Hatami), and the smallest open case named in the literature, $K_{5,5}$ minus a 10-cycle, is not weakly norming (Lee and Schülke); it has 4-cycles. The one-side-regular criterion of Conlon and Lee (2021) needs many vertices of each degree on one side and does not cover the Heawood graph, the smallest cubic bipartite graph of girth six (7 lines against $\binom{7}{3}=35$).

Sidorenko's inequality holds locally for every bipartite pattern (Lovász 2011): a host scaled to mean one that is close to the constant graphon in cut norm, with values at most two, cannot violate it. A counterexample to the statement must therefore be far from the constant graphon.

The attempt made with this problem reduces one part of the statement to a named problem: on girth-six patterns with a bipartition whose one side has maximum degree at most two, the statement is equivalent to Problem 1.5 of Conlon, Kim, Lee and Lee, and known cases of Problem 1.5 transfer to this class through the reduction. The girth-six patterns outside it, in which every bipartition has vertices of degree at least three on both sides, are not reached. Both results of the attempt were accepted after an independent automated review.

On the negative side, the attempt proves that the reported construction cannot produce a counterexample on any girth-six pattern at leading order: its sign model is identically $1$ without 4-cycles, while every pattern with a 4-cycle admits active sets on which it takes the values $0$ and $2$. The barrier is conditional on the analogue of the rank-layer limit for the pattern, which the manuscript proves only for its own pattern, and it says nothing about the error at a fixed field size or about other constructions.

## What resolves it

A positive resolution proves $t(H,W)\ge t(K_2,W)^{e(H)}$ for every finite bipartite graph $H$ of girth at least six with at least one edge and every graphon $W$; equivalently, $t(H,G)\ge \bigl(2e(G)/v(G)^2\bigr)^{e(H)}$ for every finite simple graph $G$, where $t(H,G)$ counts all homomorphisms $H\to G$, including noninjective ones, divided by $v(G)^{v(H)}$. A negative resolution exhibits one bipartite graph $H$ of girth at least six and a graphon $W$, or a finite simple graph $G$, with $t(H,W)<t(K_2,W)^{e(H)}$, together with a complete proof of the strict inequality.

## References

- David Conlon, Jacob Fox, Benny Sudakov. An approximate version of Sidorenko's conjecture. [1004.4236v2](https://arxiv.org/abs/1004.4236v2)
- David Conlon, Jeong Han Kim, Choongbum Lee, Joonkyung Lee. Some advances on Sidorenko's conjecture. [10.1112/jlms.12142](https://doi.org/10.1112/jlms.12142)
- Hao Chen, Yupeng Lin, Jie Ma. Kohayakawa-Nagle-R{ö}dl-Schacht conjecture for subdivisions. [2407.10861v2](https://arxiv.org/abs/2407.10861v2)
- David Conlon, Joonkyung Lee. Finite reflection groups and graph norms. [1611.05784v2](https://arxiv.org/abs/1611.05784v2)
- David Conlon, Joonkyung Lee. Sidorenko's conjecture for blow-ups. [1809.01259v3](https://arxiv.org/abs/1809.01259v3)
- Leonardo N. Coregliano, Alexander A. Razborov. Biregularity in Sidorenko's Conjecture. [2108.06599v2](https://arxiv.org/abs/2108.06599v2)
- Hamed Hatami. Graph norms and Sidorenko's conjecture. [0806.0047v1](https://arxiv.org/abs/0806.0047v1)
- Seonghyuk Im, Ruonan Li, Hong Liu. Sidorenko's conjecture for subdivisions and theta substitutions. [2408.03491v2](https://arxiv.org/abs/2408.03491v2)
- Jeong Han Kim, Choongbum Lee, Joonkyung Lee. Two Approaches to Sidorenko's Conjecture. [1310.4383v3](https://arxiv.org/abs/1310.4383v3)
- Daniel Král', Taísa Martins, Péter Pál Pach, Marcin Wrochna. The step Sidorenko property and non-norming edge-transitive graphs. [1802.05007v4](https://arxiv.org/abs/1802.05007v4)
- Aldo Kiem, Olaf Parczyk, Christoph Spiegel. Adjunctions, Box Products, and Forcing Families. [2412.12904v2](https://arxiv.org/abs/2412.12904v2)
- Joonkyung Lee, Bjarne Schülke. Convex graphon parameters and graph norms. [1910.08454v2](https://arxiv.org/abs/1910.08454v2)
- László Lovász. Subgraph densities in signed graphons and the local Sidorenko conjecture. [1004.3026v1](https://arxiv.org/abs/1004.3026v1)
- A counterexample to Sidorenko's conjecture. [https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/paper.pdf)
- Yuqi Zhao. Sidorenko-Type Inequalities for Even Subdivisions over Finite Abelian Groups. [2507.15723v1](https://arxiv.org/abs/2507.15723v1)
- Yuqi Zhao. Conjugacy Class Averages and Sidorenko's Conjecture. [2606.15368v1](https://arxiv.org/abs/2606.15368v1)
- Yuqi Zhao. Sidorenko Inequalities for Two-Sided Group Correlation Kernels. [2606.23018v1](https://arxiv.org/abs/2606.23018v1)
- Yuqi Zhao. $L^p$-form of the KNRS conjecture. [2606.30010v1](https://arxiv.org/abs/2606.30010v1)

## How this problem was made

The exactory math-conjecturer harness keeps one research record per exploration. This problem comes from the record `sidorenko-after-counterexample` (area math.CO), whose studies are dated 2026-10-21. The record states its field as homomorphism density inequalities for bipartite graphs after the counterexample to Sidorenko's conjecture reported in the openai/math repository (family 161, manuscript dated 2026-09-23), together with the forcing, local Sidorenko and Kohayakawa-Nagle-Rödl-Schacht (KNRS) conjectures. Its literature budget allowed 400 network requests and 60 full readings, and its experiment budget allowed 4 hours of probe time.

Terms used below. A problem bar is a blind review, written before any candidate is shown, that fixes what significance and priority mean in the field. The harness rubric has admission items A1 to A6 (precision, openness, contribution, clarity, non-routine character, readiness), two significance grounds graded 0 to 3 (B1, standing in an active line; B2, influence), a priority grade 0 to 3 (comparison with neighbouring questions), pass or fail items for the attempt and for calibration, and an accessibility class (E-F means that known footholds give a meaningful entry). Posting requires every admission item to pass, a significance grade (the higher of B1 and B2) of at least 2, priority of at least 2, and passing attempt and calibration items, both in the self-assessment and in two independent result reviews.

### Candidate slate

Two blind bars were obtained first, from Claude Fable 5.1 and Claude Opus 5.5 (record ids `problem-bar-fable` and `problem-bar-opus`). The record then compared seven candidates. The slate `slate-1` selected this question (girth six) and a question about biregular patterns. It deferred two questions until decisive readings exist: whether every Sidorenko graph with a cycle is forcing, and whether the 35-vertex counterexample graph satisfies the KNRS inequality. It rejected three: edge-transitive patterns (a sub-question of the biregular candidate), 1-subdivisions of graphs (a restatement of Problem 1.5 of Conlon, Kim, Lee and Lee, which the girth-six question contains), and incidence graphs of triangulated spheres with at most 12 vertices (it varies the triple system of the reported construction without a new mechanism, and its threshold rests on one computation without a structural explanation).

The slate gives this reason for girth six: as the record reads Equation (3.4) of the manuscript, the construction's only correction term comes from pairs of points that lie in two faces, and every such pair spans a 4-cycle of the pattern. The record holds no formulated statement for the biregular candidate.

The sphere candidate came from exploratory probes. An enumeration with plantri 5.8 of the triangulations of the 2-sphere with 4 to 13 vertices found no sphere with at most 12 vertices that satisfies both combinatorial hypotheses used by the manuscript (discrete colour refinement on the incidence graph, and three Hamiltonian cycles covering every edge), and exactly two 13-vertex spheres that satisfy both, one of them the manuscript's sphere. The record states that this computation says nothing about the Sidorenko property of any sphere.

### Formulation

The recorded statement `statement-girth-six` declares eight neighbouring formulations: Problem 1.5 of Conlon, Kim, Lee and Lee; the 1-subdivision of the reported counterexample; a girth threshold above which every bipartite graph is Sidorenko; incidence graphs of linear $k$-uniform hypergraphs; the Heawood graph; forcing for girth-six graphs with a cycle; biregular girth-six graphs; and Conjecture 4.1 of Im, Li and Liu. It also carries a Lean statement of the finite-host form named in the resolution criteria, kept in `formal/`. The formulation draft names the strongest objection, that the question restricts a refuted conjecture to a class, and the answer the record argues: the class is exactly where the only known mechanism produces no correction term.

### Openness

Nine search records, one for the statement and one for each neighbour, bind 25 responses captured on 2026-10-21 from the arXiv API and OpenAlex. The seventeen works that these searches found relevant were read in full; with the manuscript and a 2020 paper of Sidorenko, the record holds full readings of nineteen works. An independent review by Claude Fable 5.1 (`assignment-openness-fable-2`) found the statement and its eight neighbours `supported_open`: no captured work states or settles the statement, and the positive results in the works read cover only subclasses. Further study queries used Crossref, zbMATH Open and MathOverflow. Semantic Scholar returned HTTP 429 to every attempt and is recorded as unavailable, and the full text of Fox and Wei (2017) was not read.

### Bounded attempt

A math-solver objective took the exact statement as its claim, with a reviewed proof policy and a limit of 24 moves. It split the statement by a case-split route into the class $\mathcal{C}_2$ of girth-six patterns with a bipartition whose one side has maximum degree at most two, and the girth-six patterns outside $\mathcal{C}_2$. Two investigation nodes made one move each. Each result was accepted after an independent review by Claude Fable 5.1.

- Reduction (`acceptance-000001`, node `class-c2-reduction`). On $\mathcal{C}_2$ the statement is equivalent to Problem 1.5 of Conlon, Kim, Lee and Lee (Proposition B). The main tool is Lemma A: deleting a vertex of degree one preserves the Sidorenko property in both directions, proved from finite lemmas. The reviewer checked each step and found no gap.
- Barrier (`acceptance-000002`, node `sign-model-barrier`). For every bipartite pattern without 4-cycles, the pairwise sign model of the reported construction is identically $1$ (Lemma O). Conditional on the analogue RL(H) of the manuscript's rank-layer limit for the pattern, every choice of the construction's finite data therefore gives exactly the Sidorenko value at leading order (Corollary O′). On every pattern with a 4-cycle the sign model takes the values $0$ and $2$. The reviewer checked the proof against the text of the manuscript and noted one notational slip that does not affect the result. The first admission review of this node asked for a revision, because the milestone was bound to the positive route and the hypothesis overstated the scope. A revised proposal was admitted after a local harness repair.

The record states the proof status of the full statement as open. Its attempt record lists as unresolved Problem 1.5 itself, the positive direction outside $\mathcal{C}_2$ (for example the Heawood graph), and the rank-layer limit for girth-six patterns together with the error terms at a fixed field size.

### Value case and self-assessment

The motivation and current state above are the recorded value case. The self-assessment passes A1 to A6, grades B1 = 2, B2 = 2 and priority 2, passes the attempt and calibration items, and classifies accessibility as E-F. It names B1 with the criterion V7 (programme position: reductions that fix the question's place in a named line) as the primary account.

### Independent reviews and the decision

Both bars were sufficient. The Fable result review could not run because the Fable model had reached its weekly usage limit. Under a recorded route retirement, its review slot continued with Claude Sonnet 5.5, which re-derived the bar of that slot (the decision cites `problem-bar-sonnet-3`). The two result reviews used for the decision, by Claude Opus 5.5 (`problem-result-opus-2`) and Claude Sonnet 5.5 (`problem-result-sonnet`), found the problem sufficient with the same grades as the self-assessment.

The bars and result reviews raised nine material objections. Both result reviews resolved the objection that no Lean artifact of the counterexample had been delivered. A focused adjudicator, Claude Opus 5.5 at effort xhigh, found two objections not upheld: that the counterexample is unverified (in the Fable slot's version) and that no small-graph computations were supplied. It first found the other six upheld. A local change to the harness, approved on 2026-10-21, then added a `not_binding` disposition for an objection whose claim holds while no affected part of the posted text depends on it or the text states that dependence. Under it the adjudicator found those six not binding. They concern the unverified counterexample (in the Opus bar's version), the Lean formalization of the counterexample, which was not built and was checked only by a textual audit, the missing small-graph computations (in the Opus bar's version), the absence of evidence of activity after the counterexample, reductions of Szegedy known only through other authors' restatements, and the Sonnet result review's objection that the case for girth six as the threshold rests on one conditional, leading-order barrier.

The Opus result review also lists inconsistencies it found in the record: the openness review says the manuscript is not in evidence although a full reading of it was delivered, the self-assessment mentions a Semantic Scholar gap that the delivered search records do not list, and the attempt's internal openness binding refers to a different statement digest. The decision `decision-girth-six-post` recorded the post, and the problem was posted on 2026-10-22.

## Contents of this folder

- `README.md`: this file.
- `formal/`: the Lean 4 statement `SidorenkoGirthSix.Statement` of the finite-host form, with its Lake project files. It states the problem and proves nothing. The record's build log reports a successful build with Lean v4.33.1 and Mathlib v4.33.1. To build it, install elan and run `lake exe cache get` and then `lake build` in `formal/`. In `lake-manifest.json` the record's absolute local `packagesDir` was replaced by the default `.lake/packages`; nothing else was changed. The exactory problem page lists no formal statement.
- `record/`: the curated working record of the harness. `record/README.md` describes every file.
