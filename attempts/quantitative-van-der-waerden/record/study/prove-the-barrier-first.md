# Strategy study: prove-the-barrier-first

Written 2026-09-04 (step 1 of the plan). Contract: STUDY.md.

## 1. Queries

The query set of novelty.md, re-read for the three things step 1 asks: methods that stopped at
a documented value, the property those methods share, and a modified problem shown false.

## 2. Hits worth reading

- Gurvits, arXiv:0711.3496; Laurent and Schrijver, Amer. Math. Monthly 117 (2010). The capacity
  proof peels one variable at a time; each step is a one-variable inequality about one column.
- Wanless, Linear Algebra Appl. 286 (1999): the Holens-Dokovic conjecture, that the normalised
  subpermanent sums q_k are monotone, is false at n = 22 for i = n. Cited by the interpolation
  route as the reason the termwise chain q_{k+1} >= q_k cannot be the proof.
- Egorychev 1981, Falikman 1981: first-order arguments, no deficiency term.
- This record: route-capacity.md, two-column section, and route-interpolation.md, Section 6.
  Both routes stop at the same place and each proves why its own tools stop.

## 3. What was learned, as constraints on the plan

1. **The documented value.** Every route in the record stops at a = 1/(2n): the one-column
   capacity theorem gives exactly that, and the interpolation route proves that every input it
   has (van der Waerden, Friedland, the local theorem, the exponential bound along the ray,
   Newton) leaves the endpoint value free above exp(d^2/(2n)). The truth is c*(n) >= 1/4.
2. **The shared property.** Every stopped method uses information about one column, or about
   one permutation, at a time. In the capacity proof the peeling step sees one column; in the
   interpolation the inputs are values along one segment; the pointwise-in-permutation scheme
   loses because the second-order term E e_2 = E p_2 / (2(n-1)) is a 1/n effect of the
   permutation constraint (route-interpolation.md, 6.2, where every such scheme gives c < 0 for
   n >= 5). The deficiency term at the needed order is a joint two-column quantity.
3. **The modified problem shown false.** The sequential forms of the two-column inequality,
   cap(q_{n-2}) >= g(n-1) e^{d_prime/2} cap(q_{n-1}) and its variants, fail with ratio 0.967 at
   n = 4 and 0.984 at n = 5 (route-capacity.md, two-column section 2). So the two-column gain
   cannot be obtained one column at a time by any argument, not only by the ones tried.
4. **Where the joint tools degenerate.** For the joint capacity C_2 the convexity-plus-Hessian
   argument needs a Hessian floor on a ball; every provable floor goes through the smallest
   column entry, which on the n = 7 region can be 0.02, and for disjoint supports the Hessian is
   genuinely degenerate along a direction. Explicit dual weights are exact in one regime and
   lose first order in another. Second-order expansion fails because the tight direction has
   relative margin 1/(n-1) while entry deviations on the region reach 100 percent.

## 4. Stop reason

The queries ran dry: the property the stopped methods share is stated in the record by two
independent routes, and the false modified problem is a computed fact.
