# Strategy study: decompose-and-parallelise

Written 2026-09-04 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

The query set of `novelty.md` and of the sibling attack, plus the local computations
`r1-threshold.py`, `binding-constraint.py`, `conditional-K.py`, `entrywise-lower-bound.py`,
`reff-bound-check.py`, all run 2026-09-03 and 2026-09-04.

## 2. Hits worth reading

The three 2026 Dittert preprints, each of which is a single chain with one numeric interface
(the final rational comparison), and Theorem R, which is the same chain with the spectral
gap as its interface. No source splits the problem into independent components.

## 3. What was learned, as constraints on the plan

1. **The chain has exactly three interfaces**, and each is a scalar: the margin bound
   `|u|^2 + |v|^2 <= 2 delta kappa_n` (Cheon-Wanless Thm 2.1, tight to within 0.4 percent at
   `n = 15`); the scaling cost `-log cap(A) <= K (|u|^2 + |v|^2)` (open, `K_max(n)` is the
   bar); and the Knopp-Sinkhorn floor `-log cap(A) >= log(m_n/gamma_n)` (a theorem).
2. **The second interface is the only open one**, and moves 3 to 7 established what it needs:
   not a better competitor (the Sinkhorn scaling is already the optimum), not a nonnegativity
   fix alone (the effective-resistance lemma does not remove (N) on its own), and not a
   universal constant (`K` is unbounded on decomposable matrices).
3. **The two components that remain independent** are the two branches of the dichotomy of
   move 6: the branch `cap(A) >= gamma_n/m_n`, which is closed, and the branch where `A` is
   quantitatively near-decomposable, which is open and is the only place a permanent lower
   bound has to come from.
4. **The ledger by dimension** is inherited from the sibling attack: `n = 5, 6` closed there
   by exact certificates, `n >= 16` in print, and `7 <= n <= 15` open here; nothing in this
   attack changes that ledger, it only sharpens what the open part needs.

## 4. Stop reason

The queries ran dry and the component structure is settled by the moves already journalled.
