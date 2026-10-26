# Erdős problem 124 with a positive cutoff

| | |
|---|---|
| Claim | For every finite set $D$ of distinct integers $d\ge 3$ with $\gcd(D)=1$ and $\sum_{d\in D}\frac{1}{d-1}\ge 1$, and every integer $k\ge 1$, there exists $N(D,k)$ such that every integer $n\ge N(D,k)$ is a sum of finitely many labelled occurrences $d^j$ with $d\in D$ and $j\ge k$, each pair $(d,j)$ used at most once; equal numerical values from different pairs remain separately available. |
| Outcome | Open. Partially proved: 15 results accepted at the record's "analytical reviewed" standard (independent AI result review, then the controller's audit of the frozen evidence): eight completeness theorems for structured families of base sets $D$, one conditional theorem, two theorems on arbitrarily long intervals of subset sums, two auxiliary lemmas, and two counterexamples to abstract proof routes (not to the problem). No computation was run. |
| Formal verification | None. The record cites the Lean statement `Erdos124.erdos124.ne_zero` in google-deepmind/formal-conjectures (tagged research open) and an existing Lean proof of the cutoff-zero case; it ran no Lean build. |
| Related problem | None in this repository. |
| Made by | exactory math-solver harness, objective `erdos-124` (23 investigation nodes), 2026-09-06 to 2026-09-08. The record is paused at checkpoint 29 at the user's request. |

## The problem as the record states it

The claim above is the record's exact objective (`record/attack/SEARCH_TREE.md`, from the controller contract). Its quantifiers, as the record writes them: for every admissible finite $D$, for every integer $k\ge 1$, there exists an integer $N$ such that for every integer $n\ge N$ there are finite subsets $S_d\subseteq\{k,k+1,\dots\}$ with $n=\sum_{d\in D}\sum_{j\in S_d}d^j$.

Source: Erdős problem 124, <https://www.erdosproblems.com/124>, which the record found marked open with no proof claims on 2026-09-06, and Burr, Erdős, Graham and Li, Complete sequences of sets of integer powers, Acta Arith. 77 (1996) 133-138, doi:10.4064/aa-77-2-133-138. The record's statement audit (`record/attack/erdos-124-positive-cutoff/study/problem.md`) uses the denominator $d-1$ as in that paper and the formal statement, and notes a typo on the website. The case $k=0$ is known; the record treats it as not part of the objective.

## Results

Notation: $D$ is a nonempty finite set of distinct integers at least 3, $m=\min D$, and $\sigma(E)=\sum_{d\in E}\frac{1}{d-1}$ for a set $E$ of bases. A label is a pair $(d,j)$ with value $d^j$; the cutoff is $k\ge1$; a deletion is a finite set $F$ of labels $(d,j)$ with $d\in D$, $j\ge k$. Most results end with the conclusion

> (C) every integer $k\ge1$ and every finite set $F$ of labelled occurrences $(d,j)$ with $d\in D$ and $j\ge k$ admit $N(D,k,F)$ such that every integer $n\ge N$ is a sum of finitely many remaining occurrences $d^j$, each pair $(d,j)$ used at most once, coincident numerical values from different pairs retained separately.

The checkpoint reports word (C) in slightly different but equivalent ways. Every result below was accepted by the controller (acceptance numbers in brackets) after an independent result review by a separate AI agent; the reviews record Codex agent sessions as reviewers. The record claims no computational certificate, no Lean check and no exhaustive novelty for any of them. Each item names its checkpoint report in `record/progress-reports/`, where the exact statement is quoted, and its proof.

### Completeness for families of base sets

1. If $\gcd(D)=1$ and $\sigma(D)\ge 3+\min\{1/4,\,2/m\}$, then (C). [acceptance 6, checkpoint 17; it contains acceptance 5, checkpoint 16, the range $\sigma(D)\ge 3+2/m$.] Proof: `record/attack/erdos-124-quarter-mass/moves/001-quarter-mass-completeness.md` and `record/attack/erdos-124-mass-partition/moves/001-high-mass-completeness.md`.
2. If $m=3$, $\gcd(D)=1$ and $\sigma(D)\ge 11/6$, then (C). [acceptance 7, checkpoint 18] Proof: `record/attack/erdos-124-ternary-reserve/moves/001-ternary-reserve.md`.
3. If $m=4$, $\{8,16\}\subseteq D$, $\gcd(D)=1$ and $\sigma(D)\ge 251/140$, then (C). [acceptance 8, checkpoint 19] Proof: `record/attack/erdos-124-binary-block-reserve/moves/001-binary-block-reserve.md`.
4. If $D$ consists of integers at least 4, $\gcd(D)=1$ and $\sigma(D)\ge b(m)=2+\frac{1}{m-1}+\frac{\lfloor\log_2 m\rfloor+1}{m}$, then (C); moreover $b(m)\le 37/12$ for every $m\ge4$ and $b(m)\to2$. [acceptance 11, checkpoint 24] Proof: `record/attack/erdos-124-ergodic-mass-threshold/moves/002-two-supply-ergodic-rung.md`.
5. If $\gcd(D)=1$ and there are an integer $B\ge2$, a nonempty finite set $A$ of positive integers and a nonempty set $C\subseteq D\setminus R$, where $R=\{B^a:a\in A\}\subseteq D$, with $\sigma(R)\ge1/2$, $\gcd(\{B\}\cup C)=1$ and $\sigma(D\setminus(R\cup C))\ge1$, then (C). [acceptance 9, checkpoint 22] The record notes that the seed condition has no solutions with $B\ge4$ and needs base 3 when $B=3$, and that it covers the binary seed $\{4,8,32\}$ (mass $331/651$) without 16. Proof: `record/attack/erdos-124-common-radix-reserve/moves/001-common-radix-reserve.md`; write-up: [`paper/common-radix-reserve.md`](paper/common-radix-reserve.md).
6. If $\gcd(D)=1$ and there are an integer $B\ge2$ and a nonempty finite set $A$ of positive integers with $R=\{B^a:a\in A\}\subseteq D$, $\sigma(R)\ge1/2$, and $V=D\setminus R$ satisfying $\min V\ge4$ and $\sigma(V)>1$, then (C). [acceptance 14, checkpoint 27] The record states that the same proof covers every input with $m=3$, $\gcd(D)=1$ and $\sigma(D)>3/2$. Proof: `record/attack/erdos-124-phase-modular-reserve/moves/001-phase-modular-reserve.md`; write-up: [`paper/phase-modular-reserve.md`](paper/phase-modular-reserve.md).
7. If $\gcd(D)=1$ and there are an integer $B\ge2$ and a nonempty finite set $A$ of positive integers with $R=\{B^a:a\in A\}\subseteq D$, $\sigma(R)\ge1/2$, and $V=D\setminus R$ satisfying $\min V\ge4$ and $\sigma(V)=1$, containing two multiplicatively independent integers, and with $H_V(x)>x$ for every real $x>1$, where $p_d(x)$ is the least nonnegative integer power of $d$ that is at least $x$ and $H_V(x)=\sum_{d\in V}\frac{p_d(x)-1}{d-1}$, then (C). [acceptance 15, checkpoint 28] The record shows by hand that $D=\{3,4,5,6,7,21\}$, of total mass $3/2$, satisfies this criterion and lies outside every witness of item 6; its completeness at cutoff 1 was already known from Burr-Erdős-Graham-Li for the subset $\{3,4,5\}$, and the record does not claim that case as new. Proof: `record/attack/erdos-124-critical-complement/moves/001-critical-complement.md`; write-up: [`paper/critical-complement.md`](paper/critical-complement.md).

### A conditional theorem

8. Let WOC be the assertion: for every nonempty finite set $E$ of distinct integers at least 4 with $\sigma(E)>1$ and every integer $k\ge1$, there exist an integer $r\ge1$, $\theta\in(\mathbb{R}/\mathbb{Z})^r$, an open set $U\subseteq(\mathbb{R}/\mathbb{Z})^r$ meeting $K=\overline{\{n\theta:n\in\mathbb{Z}\}}$, and a set $J$ of positive integers containing intervals of every finite length, such that every $n\in J$ with $n\theta\in U$ is $\sum_{(d,j)\in H}d^j$ for some nonempty finite set $H$ of labels with $d\in E$ and $j\ge k$. If WOC holds, then (C) holds for every $D$ with $\gcd(D)=1$ and $\sigma(D)\ge2+\min\{1/8,\,1/m\}$. [acceptance 10, checkpoint 23] Only the implication was accepted; WOC is open. Proof: `record/attack/erdos-124-one-class-conditional/moves/002-woc-restricted-bridge.md`.

### Arbitrarily long intervals (not completeness)

9. Let $D$ consist of integers at least 4 and let $H=\{h\in D:\sigma(D\setminus\{h\})\ge1\}$. If $H$ is nonempty with $\gcd(H)=1$, then for every cutoff $k$ and deletion $F$ there is an explicitly recursive infinite sequence $Q$ of distinct remaining labels, strictly increasing in value, whose complement has finite subset sums with consecutive gaps at most $g=\lceil\sum_{d\in D}d^k/(d-1)+\sum_{(d,j)\in F}d^j\rceil$, in which every $h\in H$ occurs infinitely often with bounded gaps between its selected exponents, and with $\sum_i\lVert\beta q_i\rVert^2=\infty$ for every nonzero $\beta\in\mathbb{R}/\mathbb{Z}$; moreover, for every $L\ge1$ the finite subset sums of all remaining labels contain $L$ consecutive integers, with a terminating witness procedure and each label used at most once. [acceptance 12, checkpoint 25] Proof: `record/attack/erdos-124-cyclic-spectral-thinning/moves/001-cyclic-spectral-thinning.md`; write-up: [`paper/cyclic-spectral-thinning.md`](paper/cyclic-spectral-thinning.md).
10. If $D$ consists of integers at least 4, $\gcd(D)=1$ and $\sigma(D)>1$, the same conclusion holds with a sequence $Q$ that uses every base infinitely often with bounded selected exponent gaps. [acceptance 13, checkpoint 26] The record stresses that intervals of every finite length are not eventual completeness. Proof: `record/attack/erdos-124-phase-spectral-thinning/moves/001-phase-spectral-thinning.md`; write-up: [`paper/phase-spectral-thinning.md`](paper/phase-spectral-thinning.md).

### Auxiliary lemmas

11. If $\gcd(D)=1$ and $\sigma(D)\ge1$, there is $E\subseteq D$ containing $m$ with $\gcd(E)=1$ and $1\le\sigma(E)<1+1/m$. [acceptance 1, checkpoint 8] Proof: `record/attack/erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md`.
12. For every $D$ admissible in the sense of the claim, every cutoff $k$ and every deletion $F$, list the remaining powers in increasing order, breaking ties by base label, as $a_1,a_2,\dots$, and let $S_m=a_1+\dots+a_m$. Then $S_m-a_{m+1}\to+\infty$. [acceptance 2, checkpoint 9] The proof imports the finiteness theorem of Evertse, Schlickewei and Schmidt (doi:10.2307/3062133). Proof: `record/attack/erdos-124-tail-surplus/moves/001-sunit-tail-surplus.md`.

### Counterexamples to abstract proof routes

These refute general inferences that a proof might have used. They are not counterexamples to the problem.

13. Two labelled copies of $b_{2t}=9^t+\lfloor 9^t/t\rfloor$ and $b_{2t+1}=3b_{2t}+1$, $t\ge1$, satisfy every hypothesis of the abstract strong-surplus seed inference (obligation 10 in the search tree: gcd one and full residue coverage of subset sums in every tail, a counting condition, divergent norm sums, and prefix surplus beyond every sublinear power), yet their subset sums contain at most $\lfloor X/9\rfloor$ positive integers up to $X$. [acceptance 3, checkpoint 10] Proof: `record/attack/erdos-124-strong-surplus-seed/moves/001-paired-perturbation.md`.
14. A sequence of numerical multiplicity two with all of those properties and, in addition, a legal signed representation of 1 in every tail, whose positive subset sums up to $X$ number at most $\lfloor X/9\rfloor$. [acceptance 4, checkpoint 15] Proof: `record/attack/erdos-124-signed-tail-seed/moves/001-sparse-signed-blocks.md`; write-up: [`paper/signed-tail-seed.md`](paper/signed-tail-seed.md).

## Proof in brief

The record's starting point is an interval extension step of Brown type. If the first $r$ remaining occurrences represent every integer in $[L,S_r-L]$ and the next occurrence satisfies $a_{r+1}\le S_r-2L+1$, the represented interval extends to $[L,S_{r+1}-L]$. Lemma 12 shows that the surplus $S_m-a_{m+1}$ tends to infinity, so the difficulty lies in producing a represented interval (a seed) at some late prefix with a fixed loss $L$.

The completeness theorems produce the seed from disjoint supplies of labels. Items 1 and 4 split $D$ into disjoint supplies, two or three of them of reciprocal mass at least one: item 1 uses lemma 11 and a published bounded-gap and Bohr input (Bergelson and Simmons), and item 4 builds a Fourier-Stieltjes mean on the subset sums of a finite gcd-one supply and applies a sumset corollary of Griesmer (arXiv:2507.10512v1). The record notes that this kind of partition needs total mass above two, so refining its constants cannot reach mass one.

Items 2, 3 and 5 to 7 use a digit construction and a reserve. A digit system on fresh labels (balanced ternary in item 2, a block of thirteen binary weights in item 3, aligned exponents of a common radix in items 5 to 7) gives signed unit pairs: disjoint finite sets $P,Q$ of unused labels with $\sum_Q-\sum_P=1$. A separate reserve of mass at least one has positive subset sums with gaps at most a constant $g$ fixed before the pairs are chosen. Then $g-1$ disjoint pairs represent $g$ consecutive integers, and the reserve fills in every larger integer. Item 6 replaces whole correction streams by individual corrections at admissible phases, with one cumulative ledger of removed weight; item 7 handles a complement of mass exactly one under the stated condition on $H_V$, using a result of Gouillon (2006) and the simultaneous Dirichlet theorem as stated in Fishman and Simmons (2017).

Items 9 and 10 select individual powers recursively so that the complement keeps bounded gaps, and use the Fourier-Stieltjes mean and Griesmer's corollary to obtain long intervals. They give thickness, which the record does not turn into completeness.

## What did not work

- The central-prefix route C1, which asks for fixed-loss represented intervals at every late prefix after any deletion: its abstract seed principle fails for $q-1$ copies of every $q^j+1$, $j\ge k$, with $q\ge4$ even, which have the growth and arithmetic properties the principle assumes but subset sums of upper density at most $q^{-k}$ (checkpoint 4; this is not a counterexample to C1 or to the problem), and both proposed arithmetic repairs fail (checkpoint 5).
- A lattice-aware reformulation through real thickenings: the direct use of Astels's thickness condition cannot work at total radius below one (checkpoint 6).
- Generating all admissible base sets from a finite list by adding bases and lowering the cutoff is impossible (checkpoint 7).
- Exact coefficient and exponential-tilt formulas gave no positivity estimate; a fourth-moment argument excludes a Gaussian limit (checkpoint 11).
- Carry and exchange constructions: no growing seed with controlled cost was built, and the Evertse-Schlickewei-Schmidt theorem excludes bounded-support identities in deep tails (checkpoints 12 and 13).
- Two abstract inferences are refuted (items 13 and 14).
- Scalar normalisation: for $d\ge4$ the only integers $M$ with $MX_d\subseteq X_d$, where $X_d$ is the set of finite signed base-$d$ sums with digits in $\{-1,0,1\}$, are $0$ and $\pm d^t$, so no common expanding scalar preserves every stream of a gcd-one family with minimum at least 4 (checkpoint 21, author-checked only).
- Several literature preflights ended at their query limits without a usable operation (for example occurrence allocation and phase-reserve completeness), and one external one-shot attempt on the universal central seed reported only a partial result; the record's triage found that it does not prove its target (`record/admission/external-04-run-01-triage.md`).

## Open questions

- The claim itself, with the 47 residual obligations listed in `record/attack/SEARCH_TREE.md`. Among them: the all-tail half-mass signed-unit assertion (obligation 28), the threshold $T_4=1$ for bases at least 4 (obligation 40), the cases $m=3$ or $\sigma(D)=1$ (obligation 44), and the complements and bridges of items 6 and 7 (obligations 53, 54, 56 and 57).
- The question the record was working on when it paused (node 23, obligation 58): whether every set $V$ of integers at least 4 with $\sigma(V)=1$ and a multiplicatively independent pair satisfies $H_V(x)>x$ for every $x>1$. Checkpoint 29 records candidate restrictions on a first failure, including that $H_V(x)-x\ge\gcd(V)-1$ when $\gcd(V)>1$; these are unreviewed and not accepted.
- The record's checkpoint 28 names the next question: whether the condition on $H_V$ can be characterised or removed on a broader domain, compared against a new mixed-base operation.

## How to check

There is nothing to run: the record contains no computation and no Lean development. To check a result, read in this order: its checkpoint report in `record/progress-reports/` (exact statement and evidence links), the proof in `record/attack/<node>/moves/`, and the independent result review (`record/admission/*-result-review.md` for acceptances 1 to 7, `record/attack/admission/*-result-review.md` for acceptances 8 to 15). Each review states its limits, for example which external theorems it treated as trusted inputs and, for several later reviews, that the reviewer could not recompute file hashes. Start with `record/progress-reports/LATEST.md` for the state at the pause.

## Contents of this folder

- `README.md`: this file.
- `paper/`: the six write-ups (unit drafts) the record produced: `common-radix-reserve.md` (item 5), `phase-modular-reserve.md` (item 6), `critical-complement.md` (item 7), `cyclic-spectral-thinning.md` (item 9), `phase-spectral-thinning.md` (item 10) and `signed-tail-seed.md` (item 14).
- `record/`: progress reports, the search tree, the 23 investigation nodes with their proofs, studies and units, the independent reviews, the preflight studies and the outsourcing task packets. `record/README.md` describes each part.

## References

- Burr, Erdős, Graham and Li, Complete sequences of sets of integer powers, Acta Arith. 77 (1996) 133-138, doi:10.4064/aa-77-2-133-138.
- Bergelson and Simmons, New examples of complete sets, with connections to a Diophantine theorem of Furstenberg, doi:10.4064/aa8221-10-2016, arXiv:1507.02208.
- Evertse, Schlickewei and Schmidt, doi:10.2307/3062133, arXiv:math/0409604.
- Griesmer, Discrete sumsets with one large summand, arXiv:2507.10512.
- Gouillon (2006), Corollary 2.3, and Fishman and Simmons (2017), Section 1, as cited in the proof of item 7.
- Erdős problem 124: <https://www.erdosproblems.com/124>; formal statement: `FormalConjectures/ErdosProblems/124.lean` in <https://github.com/google-deepmind/formal-conjectures>; Lean proof of the cutoff-zero case: <https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos124b.lean>.
