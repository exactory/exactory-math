# Problem study: Hall domination (obligation `hall`)

Claim: for every integer n >= 1, every n by n real matrix A with nonnegative entries, and every
real lambda > 0 such that for all row subsets I and column subsets J with |I| + |J| > n the sum of
A over I x J is at least lambda (|I| + |J| - n), there exists a doubly stochastic n by n matrix B
with lambda B_ij <= A_ij for all i, j. Formal reading: `Dittert.HallDomination` in the blueprint.

## Queries (source, string, date)

- The root study's tier-one queries (attack/dittert-lean-5-15/study/problem.md, 2026-09-06):
  arXiv, Crossref, zbMATH, Semantic Scholar and GitHub code search for max-flow/min-cut
  formalizations. Hits: mechanized max-flow/min-cut exists in Isabelle/HOL (countable networks,
  refinement of Ford-Fulkerson) and Mizar; nothing in Lean or Mathlib. GitHub code search
  `"max-flow min-cut" language:Lean`: 0 hits.
- Local Mathlib (rev 0df444a3), 2026-09-06: `Mathlib/Combinatorics/Hall/Basic.lean` (finite
  Hall's marriage theorem), `Mathlib/Analysis/Convex/DoublyStochasticMatrix.lean`,
  `Mathlib/Analysis/Convex/Birkhoff.lean`, `IsCompact.exists_isMaxOn`; no flow networks.
- DCPRevere/maths-pub report (scratch/study-2026-09-06/maths-pub-report.md, section 6):
  deficiency Hall and Koenig for finite sets (`DeficiencyHall.lean`), the doubly stochastic Hall
  condition `card_le_card_met` and the tight-cut lemma `zero_off_of_card_le`
  (`FriedlandEquality/Surplus.lean`); no real-capacity max-flow, no dominated-matrix theorem.
- The mathematical source: attack/dittert-branch-complete-audit/BRANCH_TRANSPORT.md section 5
  (the explicit max-flow construction) and audit-n8-n9.md section 1 (Li's theorem via
  Cheon-Wanless Lemma 2.2).

## What was learned, as constraints on the plan

1. No formal source exists; the theorem is built here. The proof is the augmenting-path argument
   on a maximizing flow: the set F of matrices 0 <= F <= A with row sums <= lambda and column
   sums <= lambda is compact and nonempty (F = 0), so a maximizer of the total sum exists; define
   the residual reachability inductively (a row is reachable when its row sum is below lambda, or
   through a positive entry from a reachable column; a column is reachable through an unsaturated
   entry F_ij < A_ij from a reachable row); a reachable column with column sum below lambda gives an
   augmenting alternating walk, along which the flow can be increased by a small positive amount
   (walks need not be simple: the net change on each edge is a multiple of the step and the step
   is chosen below every relevant slack divided by the walk length), contradicting maximality;
   hence every reachable column is saturated, every unreachable row is saturated, entries from
   reachable rows to unreachable columns are saturated and entries from unreachable rows to
   reachable columns are zero, so the total flow equals lambda (n - |I|) + lambda |J| + s_A(I, J^c)
   with I the reachable rows and J the reachable columns, which the cut condition bounds below by
   n lambda; the total is also at most n lambda, so every row and column is saturated and B = F /
   lambda is doubly stochastic with lambda B <= A.
2. Mathlib supplies compactness of closed bounded subsets of a finite-dimensional space,
   `doublyStochastic` membership lemmas, and finite sums; the inductive reachability predicate and
   the augmentation are new.
3. The tight-cut consequence (B[I^c, J^c] = 0 for a minimizing cut) is not part of this
   obligation; the bridges derive it from double stochasticity and domination in three lines.

## Stop reason

The queries ran dry: two consecutive sources returned nothing new about a formal max-flow
theorem in Lean.
