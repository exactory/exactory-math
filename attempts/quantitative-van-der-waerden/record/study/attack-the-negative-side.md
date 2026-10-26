# Strategy study: attack-the-negative-side

Written 2026-09-04 (step 1 of the strategy's plan). Contract: STUDY.md.

## 1. Queries

The query set of `novelty.md`, re-read for counterexample work: searches for matrices where the
van der Waerden inequality is nearly tight, for the structure of near-minimisers of the permanent
on the Birkhoff polytope, and for computer searches over that polytope.

## 2. Hits worth reading

- **Egorychev 1981, Falikman 1981.** The equality case is `J_n/n` and it is unique. So the only
  matrix where the deficiency term is zero is the centre, and every other matrix has positive
  slack in the plain inequality. That is the one fact in print about the negative side, and it
  says the counterexample space excludes exactly one point.
- **Knopp and Sinkhorn 1982.** The minimum on the face with a zero entry, `m_n`, attained at
  `T_n`. That is the only other exact minimum on a subset of the polytope in print, and
  `||T_n - J_n/n||_F^2 = 1/(n-1)^2` exactly, so `T_n` is a candidate the claim must survive: the
  ratio there is `(m_n/gamma_n - 1)(n-1)^2`, which tends to `1/2`.
- **Cheon and Wanless 2012**, and their 2016 update arXiv:1608.02844. The surveys list the known
  minima of the permanent over faces of the polytope. No search over the whole polytope for a
  matrix minimising a ratio of this shape appears anywhere.

## 3. What was learned, as constraints on the plan

1. **The range already searched with no hit.** This session searched `n = 3` to 8 by multi-start
   Nelder-Mead over the polytope, parametrised by Sinkhorn, 60 starts at four spreads
   (`study/qvdw-constant.py`). The minimum ratio found was 0.250000, 0.333333, 0.418403,
   0.460519, 0.486709, 0.497450. No matrix with ratio below 1/4 was found at any `n`. Every later
   search starts above that range, at `n >= 9`.
2. **The constructions in print, and their resource.** There are two: `J_n/n`, where the ratio
   tends to `n/(2(n-1))` in the limit, and `T_n`, where it tends to `1/2`. Both are above `1/4`,
   and both are explicit, so neither is a counterexample and neither costs anything to check.
3. **The near miss is `(I + C_n)/2`.** At `n = 3, 4, 5` the measured minimiser is the average of
   the identity and the `n`-cycle, with `per = 2^{1-n}` and
   `||(I + C_n)/2 - J_n/n||_F^2 = 2n(1/2 - 1/n)^2 + (n-2)/n`, giving exactly `1/4`, `1/3` and
   `0.418403`. It attains `1/4` at `n = 3`, so the claim is tight there and no constant above
   `1/4` can hold. This is the object every proof has to be tight against.
4. **The family stops being extremal at `n = 6`.** There `(I + C_6)/2` gives `0.5125`, above the
   measured minimum `0.460519`, and at `n = 7` and 8 the measured minimiser has no zero entries
   at all. So the extremal family is not `(I + C_n)/2` for all `n`, and the plan must not assume
   it is.
5. **A counterexample is bounded away from the centre.** The exact local expansion gives ratio
   `n/(2(n-1)) + O(||B - J_n/n||_F)` near `J_n/n`, and `n/(2(n-1)) >= 1/2` for every `n >= 2`, so
   no matrix within an explicit radius of the centre can violate the claim. That is the first
   compression of the counterexample space and it is what step 3 of the plan builds on.

## 4. Stop reason

The queries ran dry: no search over the Birkhoff polytope for a minimiser of a ratio of this
shape exists in print, so everything beyond `T_n` and `J_n/n` is new work.
