# Strategy study: attack-the-negative-side

Written 2026-09-04 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

The query set of `novelty.md`, re-read for counterexample work rather than proof work:
searches for a counterexample to Dittert's conjecture, for computer searches over `K_n`, and for
the equality analysis of the Dittert functional.

## 2. Hits worth reading

- Cheon and Wanless 2012, *An update on Minc's survey of open problems involving permanents*,
  Section 4: reports that no counterexample to Dittert's conjecture is known at any `n`, and
  that the maximiser is conjectured unique.
- Sinkhorn 1984 and Hwang 1986/87: the settled cases `n = 2, 3` are settled by exhausting the
  critical points, which is the only counterexample search in print on this problem.
- The sibling attack's `deterministic/numerical-optimisation-run-1`: the maximum of `phi` over
  the face of `K_n` where one entry is zero is `2 - m_n`, attained at the Knopp-Sinkhorn matrix
  `T_n`, measured at `n = 5` and `n = 6`.

## 3. What was learned, as constraints on the plan

**The hypothesis set of the claim is conjecturally empty, and this is the fact the strategy
turns on.** G(n, c_n) quantifies over `A in K_n` with a zero entry and `phi(A) >= 2 - gamma_n`.
Dittert's conjecture says `phi <= 2 - gamma_n` on `K_n` with equality only at `J_n/n`, which has
no zero. So the hypothesis set of G is exactly the set of counterexamples to Dittert's
conjecture at `n`, and Theorem R uses G in the only way it can be used: inside a proof by
contradiction. Three consequences fix the plan.

1. A search for a counterexample to G is a search for a counterexample to Dittert's conjecture.
   Cheon and Wanless report none is known, so the search's expected outcome is emptiness, and
   emptiness is the useful outcome, not a null result.
2. G must be proved from `phi(A) >= 2 - gamma_n` alone, never from Dittert's conjecture, or
   Theorem R becomes circular. This is a constraint on any later proof, recorded here.
3. The searchable form is the contrapositive: maximise `phi(A)` over `A in K_n` with a zero and
   `lambda_2(A) <= c_n`. A maximum strictly below `2 - gamma_n` *is* G(n, c_n) at that `n`.

The first version of the search script used the doubly stochastic polytope and was wrong for
that reason: on it van der Waerden forces `per >= gamma_n`, so `per <= gamma_n` holds only at
`J_n/n`, which has no zero, and the constraint set is empty for a reason that has nothing to do
with the spectral gap. `K_n` is the domain, and the row and column sums are free there.

## 4. Stop reason

The queries ran dry: no counterexample search over `K_n` beyond `n = 3` exists in print, so the
contrapositive maximisation of step 3 is new work rather than a repetition.
