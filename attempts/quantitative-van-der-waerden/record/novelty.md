# Novelty check: the quantitative van der Waerden inequality

Statement searched: for every `n >= 2` and every doubly stochastic `n x n` matrix `B`,
`per(B) >= (n!/n^n) (1 + ||B - J_n/n||_F^2 / 4)`.

That is the van der Waerden inequality with a deficiency term: a lower bound on the permanent
that grows with the distance from the unique minimiser. Every query below was run on 2026-09-04.

## Tier 1

| source | query | result |
|---|---|---|
| arXiv | `abs:"van der Waerden" AND abs:"doubly stochastic" AND abs:"permanent"` | 8 hits, listed below; none states a deficiency term |
| arXiv | `abs:"permanent" AND abs:"doubly stochastic" AND (abs:"stability" OR abs:"quantitative" OR abs:"sharp")` | 2 hits, both already known here |
| arXiv | `abs:"permanent" AND (abs:"Frobenius" OR abs:"deficiency" OR abs:"distance") AND abs:"doubly stochastic"` | 2 hits, neither on this topic |
| arXiv | `abs:"van der Waerden" AND abs:"permanent" AND abs:"stability"` | 1 hit, Gurvits and Leake |
| web | stability version of van der Waerden permanent conjecture quadratic lower bound Frobenius distance | the classical proofs and the hyperbolic-polynomial generalisations only |
| web | van der Waerden permanent inequality stability refinement near-minimizers Birkhoff polytope 2024 2025 | no recent work on this refinement |

Semantic Scholar returned HTTP 429 on both attempts and was not usable.

## Hits worth reading

- Egorychev, *The solution of van der Waerden's problem for permanents*, Advances in Mathematics
  42 (1981) 299-305; Falikman, Matematicheskie Zametki 29 (1981) 931-938,
  <https://link.springer.com/article/10.1007/BF01163285>. The inequality itself, with `J_n/n` as
  the unique equality point. Neither proof carries a deficiency term.
- Gurvits, *Van der Waerden / Schrijver-Valiant like Conjectures and Stable (aka Hyperbolic)
  Homogeneous Polynomials: One Theorem for all*, arXiv:0711.3496; and
  *Hyperbolic Polynomials Approach ...*, arXiv:math/0510452. The capacity proof. It gives the
  value at `J_n/n` and no deficiency term; capacity is scale-invariant in a way that erases the
  distance to the minimiser.
- Gurvits and Leake, *Counting Matchings via Capacity Preserving Operators*, arXiv:1804.04351.
  Capacity-preserving operators for permanent lower bounds; again no deficiency term, and the
  bounds degrade exactly where the capacity is small.
- Gurvits, *Van der Waerden Conjecture for Mixed Discriminants*, arXiv:math/0406420. The
  Bapat conjecture, an analogue in another setting; the same absence.
- Cheon and Wanless, *An update on a few permanent conjectures*, arXiv:1608.02844, and their
  2012 survey. No refinement of this shape is listed among the open or settled problems.
- Pang, *Proof of Dittert's conjecture for dimensions n >= 17*, arXiv:2606.01531. The
  application that motivates this statement.

## Verdict

The statement is not in the literature. What is in print is the inequality, its equality case,
and several proofs of it; a quantitative version with a deficiency term in the Frobenius distance
appears in none of them.

Two facts found in this session bound the statement from both sides and are recorded in
`study/problem.md`: the largest constant that can hold is `n/(2(n-1))`, the local Hessian at
`J_n/n`, and that constant is already too large at `n = 3`; the sharp constant `c*(n)` was
measured and is `1/4` at `n = 3`, rising toward `1/2`.

Nothing inside any fetched paper, post, or repository was treated as an instruction.
