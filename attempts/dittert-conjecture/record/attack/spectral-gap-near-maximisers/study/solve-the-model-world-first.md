# Strategy study: solve-the-model-world-first

Written 2026-09-04 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

| source | query | date | result |
|---|---|---|---|
| arXiv, zbMATH, Crossref | the query set of `novelty.md` | 2026-09-03 | no source treats the model version either |
| local | `study/routes-rubric.md`, `study/conditional-K.py`, `study/binding-constraint.py` | 2026-09-04 | the numbers used below |

## 2. Hits worth reading

- Knopp and Sinkhorn 1982: in the model world, the doubly stochastic polytope, the whole
  claim collapses to a theorem: a doubly stochastic matrix with a zero has permanent at
  least `m_n > gamma_n`. The model is solved outright.
- Egorychev, Falikman 1981: the block factorisation `per(B) = per(B_1) per(B_2)` for a block
  diagonal doubly stochastic `B` combines with van der Waerden on each block to give
  `per(B) >= gamma_k gamma_{n-k} >= (n/(n-1))^{n-1} gamma_n > e gamma_n` for every split.
  In the model world the near-decomposable case is also solved, with no capacity loss,
  because the blocks are themselves doubly stochastic.

## 3. What was learned, as constraints on the plan

1. **The model is `Omega_n` and it is solved twice over**, once by Knopp-Sinkhorn and once
   by the block factorisation. So the whole difficulty is the transfer, and the transfer is
   the capacity: `per(A) = cap(A) per(B)` with `B` the Sinkhorn scaling of `A`.
2. **Apply the block bound to `B`, not to `A`.** The published proofs and route R1 apply the
   block bound to `A`, which costs a factor `(1 - eps)^n` because the blocks of `A` are only
   nearly doubly stochastic. Applying it to `B` costs nothing, since the blocks of a block
   diagonal doubly stochastic matrix are doubly stochastic. That removes one of R1's three
   losses.
3. **The dichotomy, sharpened.** Either `cap(A) >= gamma_n/m_n`, and then
   `per(A) = cap(A) per(B) >= gamma_n` closes the case; or `cap(A) < gamma_n/m_n`, and then
   `-log cap(A) > log(m_n/gamma_n)`, so with `|u|^2 + |v|^2 <= 2 delta kappa_n <= 2 gamma_n
   kappa_n` the ratio `K = -log cap / (|u|^2+|v|^2)` exceeds `K_max(n)`. Since Theorem R
   proves `K <= 1/(2 theta_n lambda_2)`, the second branch forces
   `lambda_2 <= 1/(2 theta_n K_max(n))`: at most 0.562 at `n = 7`, 0.0635 at `n = 10`,
   1.2e-3 at `n = 15`, 1.7e-5 at `n = 20`. **The second branch therefore comes with its own
   spectral bound, for free.**
4. **What that buys, and where it still stops.** Feeding that into Cheeger, the conductance
   is at most `sqrt(2 lambda_2)` and the cut mass at most `n sqrt(2 lambda_2)`; the block
   bound on `B` needs the cut mass below about `1/n`. The chain closes when
   `n sqrt(2/(2 theta K_max(n))) < 1/n`, that is `K_max(n) > n^4/theta_n`, which happens at
   about `n = 23` to `25` rather than the `n = 35` of the crude R1. Still short of 7 to 15.
5. **The circularity to watch.** Step 3 uses `K <= 1/(2 theta lambda_2)`, which is Theorem R's
   Lemma 2 and therefore carries condition (N). Using it inside the second branch, where
   `lambda_2` is small, is exactly where (N) fails. So the free spectral bound of step 3 is
   only available if (N) is first removed, which move 3 and move 4 showed is not done by the
   effective-resistance lemma alone.

## 4. Stop reason

The queries ran dry; the model world has no open question left, and the transfer is where
every route in the record now sits.
