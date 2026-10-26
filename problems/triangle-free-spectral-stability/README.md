# Sharp spectral-deficit stability for triangle-free graphs

The question asks whether every triangle-free graph can be turned into one complete bipartite graph plus isolated vertices with at most three times as many edge additions and deletions as its spectral deficit $e(G)-\lambda(G)^2$.

| | |
|---|---|
| Area | math.CO |
| Status | Open on exactory. A complete proof of the statement, checked in Lean, is in [attempts/triangle-free-spectral-stability](../../attempts/triangle-free-spectral-stability/). No human mathematician has reviewed it yet. |
| Posted | 2026-10-22, <https://www.exactory.ai/math/5aa390a0-bf63-4326-9b97-b50c46334fd8> |
| Created by | exactory math-conjecturer harness (record `extremal-graph-stability`) |

## Problem

For every finite simple triangle-free graph $G$, put $m=e(G)$ and let $\lambda(G)$ denote its adjacency spectral radius (with $\lambda(G)=0$ when $G$ has no vertices). Define $D(G)=\min_{A,B\subseteq V(G),\ A\cap B=\varnothing}|E(G)\mathbin{\triangle}E(K_{A,B})|$, where $K_{A,B}$ has all edges between $A$ and $B$ and no other edges on $V(G)$; empty parts are permitted. Then $D(G)\le 3\bigl(m-\lambda(G)^2\bigr)$.

## Why it matters

Nosal's inequality $\lambda(G)^2\le e(G)$ makes the spectral deficit $\xi=e(G)-\lambda(G)^2$ a measure of departure from the complete-bipartite extremal situation. Recent edge-spectral stability work controls structural distance when this deficit is small. The present question asks for an exact finite inequality, valid at every deficit and independent of graph order: does the same coefficient three that controls complete-bipartite editing for bipartite graphs also control every triangle-free graph? Both additions and deletions count, and the target may have arbitrary part sizes and isolated vertices. This is the target and deficit of the cited bipartite theorem, with only the bipartiteness hypothesis removed.

The coefficient is fixed by mathematics: the five-cycle has $D(C_5)=3$ and $\xi(C_5)=1$, while a proved supporting bound gives $D(G)\le15\xi$ and an asymptotic upper coefficient three as $\xi/e(G)\to0$. An affirmative answer would determine the optimal uniform coefficient exactly and show that allowing odd cycles introduces no extra coefficient beyond the bipartite theorem. A counterexample would refute that proposed uniform law. These are the established bounds and the explanatory distinction supporting the question; no classification of equality graphs or consequence for other open conjectures is asserted.

The strongest objection is that this is merely a constant improvement after a linear bound is available. The intended gain is narrower and exact: deciding whether the bipartite coefficient remains valid throughout the triangle-free class, including finite positive deficits, despite the non-bipartite sharp example. Asking only for some finite linear coefficient is now settled by the supporting theorem, and asking only for deletion distance to bipartiteness is already settled by the cited cut lemma. Qualitative stability and the asymptotic upper coefficient do not decide the displayed exact inequality. This comparison identifies the remaining gain without claiming that every improvement of the bound fifteen is significant or that the available methods cannot settle the question.

## Where it stands

Li, Liu and Zhang, arXiv:2508.15271v2, Theorem 4.1, establish qualitative triangle-free edge-spectral stability. Li, Liu and Ning, arXiv:2609.20225v2, Lemma 4.3, prove $D(H)\le3(e(H)-\lambda(H)^2)$ for bipartite graphs. Their Lemma 4.4 also supplies a triangle-free cut obtained by deleting at most $e(G)-\lambda(G)^2$ edges. That deletion conclusion has a different target: a bipartite graph need not be complete bipartite. These fully read results are the direct comparisons.

A supporting analytical theorem, independently reviewed in this study, establishes $D(G)\le15\xi$ for every finite simple triangle-free graph and, when $\lambda(G)>0$, $D(G)\le3\xi+18\sqrt{6}\,\xi^{3/2}/\lambda(G)$. Its proof cuts along the signs of a least-eigenvalue eigenvector, applies the published bipartite editing lemma, and uses the triangle-free trace identity $\operatorname{tr}(A^3)=0$ to control the gap between the extreme eigenvalue magnitudes. Consequently, for any sequence with positive deficit and $\xi/e(G)\to0$, one has $\limsup D(G)/\xi\le3$. The proof handles disconnected graphs, isolates, zero deficit and the empty graph. Historical priority of this supporting result is not claimed.

The supporting argument can be stated explicitly. For $m>0$, write the least adjacency eigenvalue as $-\mu$, with $0<\mu\le\lambda$. Retain only edges between opposite nonzero signs of a unit eigenvector for $-\mu$, obtaining a bipartite graph $F$ after $b$ deletions. The absolute value of that vector has Rayleigh quotient at least $\mu$ in $F$. Hence $D(G)\le b+D(F)\le3(m-\mu^2)-2b\le3(m-\mu^2)$. Since $\operatorname{tr}(A^3)=0$ and $\operatorname{tr}(A^2)=2m$, $\lambda^3\le\mu(2m-\lambda^2)$. With $r=\lambda^2/m\in(0,1]$, this implies $m-\mu^2\le\xi(r^2+4)/(2-r)^2\le5\xi$. Put $\delta=\lambda^2-\mu^2\le4\xi$. After removing one occurrence of each extreme eigenvalue, the remaining squared eigenvalues sum to $2\xi+\delta\le6\xi$. Their cubed absolute values sum to at most $(6\xi)^{3/2}$, so the trace-cube identity gives $\lambda\delta\le\lambda^3-\mu^3\le(6\xi)^{3/2}$. Substitution proves both bounds. When $m=0$, both $D$ and $\xi$ vanish.

The same reviewed evidence proves $D(C_5)=3$ exactly, with $e(C_5)-\lambda(C_5)^2=1$. Thus the optimal universal coefficient lies between three and fifteen. This five-cycle witness does not establish asymptotic sharpness when the relative deficit tends to zero. The bounded attempt on the exact statement leaves its universal coefficient-three conclusion unresolved. The signed-cut argument provides a concrete entry point, but its remaining spectral-gap and editing-slack terms have not been uniformly cancelled. This unresolved calculation is not a proof of a limitation of the method, and exploratory numerics are not used as support for the question.

## What resolves it

A proof must establish the stated inequality for every finite simple triangle-free graph, allowing disconnected graphs and isolated vertices and counting both edge additions and deletions in $D(G)$. A disproof must give a finite simple triangle-free graph and rigorously certify $D(G)>3(e(G)-\lambda(G)^2)$. Numerical eigenvalues or an upper bound on $D(G)$ alone do not certify a counterexample.

## References

- Yongtao Li, Hong Liu, Shengtong Zhang. Edge-spectral Turán theorems for color-critical graphs with applications. [2511.15431v3](https://arxiv.org/abs/2511.15431v3)
- Yongtao Li, Hong Liu, Shengtong Zhang. An edge-spectral Erdős-Stone-Simonovits theorem and its stability. [2508.15271v2](https://arxiv.org/abs/2508.15271v2)
- Yuantian Yu, Huihui Zhang, Minjie Zhang. A survey of edge-spectral-Turán type problems in spectral graph theory: Results, conjectures and open problems. [2512.19395v1](https://arxiv.org/abs/2512.19395v1)
- Yongtao Li. An entropy bridge from weighted to spectral Turán theorems. [2608.24388v2](https://arxiv.org/abs/2608.24388v2)
- Yongtao Li, Lele Liu, Bo Ning. The spectral Erdős book theorem: sharp bounds and stability. [2609.20225v2](https://arxiv.org/abs/2609.20225v2)
- V. Nikiforov. On a theorem of Nosal. [2104.12171v1](https://arxiv.org/abs/2104.12171v1)

## How this problem was made

The exactory math-conjecturer harness keeps one research record per exploration. This problem comes from the record `extremal-graph-stability` (area math.CO), whose work log begins on 2026-10-21. The record states its field as extremal graph theory, especially quantitative stability and the structure of graphs close to an extremal value, and excludes the Littlewood-Richardson, hive and Ehrhart line of an earlier record. Its literature budget allowed 150 network requests and 40 readings, and its probe budget allowed 600 seconds.

Terms used below. A problem bar is a blind review, written before any candidate is shown, that fixes what significance and priority mean in the field. The harness rubric has admission items A1 to A6 (precision, openness, contribution, clarity, non-routine character, readiness), two significance grounds graded 0 to 3 (B1, standing in an active line; B2, influence), a priority grade 0 to 3 (comparison with neighbouring questions), pass or fail items for the attempt and for calibration, and an accessibility class (E-F means that known footholds give a meaningful entry). Posting requires every admission item to pass, a significance grade (the higher of B1 and B2) of at least 2, priority of at least 2, and passing attempt and calibration items, both in the self-assessment and in two independent result reviews. Below, $\xi=e(G)-\lambda(G)^2$.

### Candidate slate

The exploration started from three lines of stability results: exact stability for Turán's theorem (Korándi, Roberts and Scott), strong stability from flag algebra calculations (Pikhurko, Sliačan and Tyros), and strong stability from vertex-extendability (Chen and Liu). Two blind bars were obtained through the Codex command-line client, `bar-astra-v2` by gpt-6-astra and `bar-sol-v2` by gpt-6.1-sol. Both bars describe these three lines from the supplied works and were sufficient.

The record compared three candidates in the slate `slate-spectral-v1`. It selected this question. It deferred the question whether some absolute constant $C$ gives $D(G)\le C\xi$, to be reconsidered if the sharp coefficient fails or a review asks to pose linearity separately. It rejected the question whether at most $\xi$ edge deletions make a triangle-free graph bipartite, because that follows from Lemma 4.4 of arXiv:2609.20225v2 at booksize zero. The comparison names the strongest objection, that removing bipartiteness could be an automatic corollary of a near-bipartite reduction, and answers it from the proofs read in full: a cut can be obtained by deleting at most $\xi$ edges, but the subsequent Weyl and Frobenius estimate loses a square root, so that composition gives no uniform linear law. The slate calls this a comparison of the displayed inequalities, not an impossibility claim about the methods.

The record also ran exploratory probes with floating-point eigenvalues, to which it gives no evidential credit. Over all 165 nonempty triangle-free graphs with at most 7 vertices, with exact edit distances, and over 13,126 weighted blow-ups of the five-cycle, the largest ratio $D(G)/\xi$ observed was 3 up to rounding. A screen of the average of the edit costs of edge-neighbourhood bicliques over 281 graphs observed a largest mean ratio of 3.05, on a graph with 7 vertices and 10 edges.

### Formulation

The recorded statement `statement-sharp-three-v1` declares four neighbouring formulations: the same inequality for bipartite graphs, the same inequality for regular triangle-free graphs, the existence of some absolute constant $C$ with $D(G)\le C\xi$, and the deletion-only statement. The recorded statement has no formal version.

### Openness

Five search records dated 2026-10-21, for the exact statement and the four neighbours, share seven bounded arXiv queries over math.CO and screened 36 distinct works. Six decisive works, the six references above, were read in full. Follow-up queries used Crossref and zbMATH Open; Semantic Scholar was rate limited. Nine searches in all were bound to the final finding. One hit, the paper of Wang and Lou on spectral stability for $K_{2,t}$ (DOI 10.1016/j.disc.2025.114914), was not available in full. The record screened it out of scope from its publisher preview: its Theorem 1.5 concludes that a graph contains $K_{2,t}$ or a large star, and triangle-free graphs may contain $K_{2,t}$.

The fifth openness review, by gpt-6-astra (`openness-sharp-three-v5`), found the statement `supported_open` and describes this as a literature-supported research status within the dated, bounded searches, not an exhaustive proof of absence. It states that every declared neighbour is resolved by the delivered evidence: the bipartite case by Lemma 4.3 of arXiv:2609.20225v2, the deletion-only case by Lemma 4.4, the regular case by a neighbourhood calculation, and the existence of a linear constant by the supporting theorem below. The four earlier openness reviews asked for further evidence (the supporting proof, the resolution of the Wang-Lou hit, the publisher capture) or failed on input size before any review.

### Bounded attempt

A math-solver objective took the exact statement as its claim, with a reviewed proof policy and 24 moves and 24 runs in total. The root node `trianglefree-spectral-distance` made three analytical moves.

1. A ledger of the losses in the published two-step argument. It gives the weaker estimate $D(G)\le\min(m,3\xi+6\sqrt{m\xi})$, where $m=e(G)$, and shows on the five-cycle that the two published estimates used separately give 4 where the target is 3. The record says this limits that composition only.
2. A signed auxiliary vector. The cut by the positive Perron vector fails its sufficient inequality on the five-cycle; the sign cut of a least-eigenvalue eigenvector gives the bounds of the supporting theorem below.
3. The joint remainder. The exact certificate $D(G)\le 3\xi+3\delta-2b-3r-s$, where $-\mu$ is the least adjacency eigenvalue, $\delta=\lambda^2-\mu^2$, $b$ is the number of edges deleted by the sign cut and $r,s\ge 0$ are slack terms, recovers the value 3 on the five-cycle, while dropping the bipartite slack leaves an excess of one. No general cancellation was established.

A standalone node `linear-spectral-distance`, admitted after approving admission reviews by gpt-6-astra and gpt-6.1-sol, proved the supporting theorem in one move: $D(G)\le 15\xi$ for every finite simple triangle-free graph; $D(G)\le 3\xi+18\sqrt6\,\xi^{3/2}/\lambda(G)$ when $\lambda(G)>0$; hence $\limsup D(G)/\xi\le 3$ along sequences with $\xi>0$ and $\xi/e(G)\to 0$; and $D(C_5)=3$ with $\xi(C_5)=1$. It was accepted (`acceptance-000001`) after an independent review by gpt-6-astra that approved the whole claim, including the boundary cases and the exhaustive count for the five-cycle, and left historical openness unresolved. The record states the proof status of the full statement as open. Its attempt record lists the coefficient-three inequality as unresolved, because the bounded attempt has not controlled the joint sign-cut and bipartite-edit slack.

This record's own attempt left the statement unresolved. The later proof named in the Status row is not part of this record.

### Value case and self-assessment

The motivation and current state above are the recorded value case. The self-assessment passes A1 to A6, grades B1 = 2, B2 = 2 and priority 2, passes the attempt and calibration items, and classifies accessibility as E-F. It names B1 with the criterion V4 (decisiveness: the known bounds and constructions and the gap between them) as the primary account.

### Independent reviews and the decision

The result reviews ran on the two bar slots, gpt-6-astra and gpt-6.1-sol, through the Codex command-line client. A first passing pair (`review-result-astra-sharp-three-v4` and `review-result-sol-sharp-three-v2`) did not support the decision: both marked the separate `stop` assurance as not assessed where the post gate requires `passed`, and the reviewers had not received the PDF page images that the visual inspections of the readings require. The later reviews received 19 rendered page images. The next Astra output (`v5`) did not qualify, because its actual input could not be authenticated: the reviewer client had removed a terminal space from the instruction.

The final pair, `review-result-sol-sharp-three-v3` and `review-result-astra-sharp-three-v6-corrected-v1`, found the problem sufficient: A1 to A6 pass, B1 = B2 = 2, priority 2, attempt and calibration pass, accessibility E-F, and no objections. The final Astra review is a reassessment in the same review slot. A bounded correction by the same reviewer changed only the disposition of its finding on the earlier `v5` output (from `confirmed` to `revised`) and the reason for it, and no scientific field. Both reviews list as limitations that openness is bounded by the dated searches, that the Wang-Lou article was not read, and that the coefficient-three inequality remains unresolved. The decision `decision-post-sharp-three-v2` recorded the post, and the problem was posted on 2026-10-22.

## Contents of this folder

- `README.md`: this file.
- `formal/`: the Lean statement of the posted problem, with `formal/README.md`, which explains what it states and how a solution is checked. The math-conjecturer record itself has no formal statement.
- `record/`: the curated working record of the harness. `record/README.md` describes every file.
