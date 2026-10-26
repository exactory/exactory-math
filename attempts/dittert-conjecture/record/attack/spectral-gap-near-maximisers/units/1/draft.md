# An effective-resistance bound on the Sinkhorn potentials of a near-maximiser

**Form.** New machinery. **Venue.** On the path to Dittert's conjecture: the lemma attacks the
binding half of the spectral threshold that Theorem R needs.

## 1. The statement

Let `A` be a non-negative `n x n` matrix whose bipartite support graph is connected. Write
`r_i = sum_j a_ij` and `c_j = sum_i a_ij` for the margins, `u = 1 - r` and `v = 1 - c` for their
deviations from one, and

    L = [[diag(r), A], [A^T, diag(c)]]

for the weighted bipartite Laplacian, an edge of weight `a_ij` joining row `i` to column `j`.
Let `(alpha; beta) = L^+ (u; v)` be the potentials and `Phi = (u; v)^T L^+ (u; v)` their energy.
Write `R_eff(i, j)` for the effective resistance between row `i` and column `j` in that network.

**Lemma.** For every entry with `a_ij > 0`,

    |alpha_i + beta_j| <= sqrt( R_eff(i, j) * Phi ) <= sqrt( Phi / a_ij ).          (*)

*Proof.* Let `chi_ij` be the incidence vector of the pair `(i, j)`, so that
`alpha_i + beta_j = chi_ij^T L^+ (u; v)`. Cauchy-Schwarz in the semi-definite inner product
`<x, y>_{L^+} = x^T L^+ y` gives
`|chi_ij^T L^+ (u; v)| <= sqrt(chi_ij^T L^+ chi_ij) sqrt((u; v)^T L^+ (u; v))`, and
`chi_ij^T L^+ chi_ij = R_eff(i, j)` by definition. For the second inequality, Rayleigh
monotonicity: the single edge `ij` already carries conductance `a_ij`, so deleting every other
edge can only raise the resistance, giving `R_eff(i, j) <= 1 / a_ij`. QED

## 2. What it gives Theorem R

Theorem R closes Dittert's conjecture at `n` once every `A in K_n` with a zero entry and
`phi(A) >= 2 - gamma_n` has spectral gap `lambda_2(A) >= c_n`. Its Lemma 2 needs a non-negativity
condition (N) on the corrected competitor, and its Lemma 3(c) supplies it through

    |alpha|_inf + |beta|_inf <= sqrt(2) |(u; v)|_2 / (theta_n lambda_2),

which carries `1 / lambda_2`. Since the margins have size `sqrt(delta)`, that bound converts into
a condition on `lambda_2` that scales as `sqrt(delta)` and is the binding half of `c_n`, by a
factor `1 / sqrt(gamma_n kappa_n)` equal to 12.1 at `n = 7` and 6555 at `n = 20` (unit 5).

The bound (*) carries no `1 / lambda_2`. It gives condition (N) with no spectral hypothesis at
every entry with `a_ij >= Phi`, and where a spectral hypothesis is still wanted the bar becomes
`lambda_2 >= 2 delta kappa_n / (theta_n a_min)`, linear in `delta` where the old one was
`sqrt(delta)`. At the heuristic `a_min ~ 1/n` that bar is 0.105 at `n = 7`, 7.6e-3 at `n = 10`,
1.3e-3 at `n = 12` and 9.0e-5 at `n = 15`, against the old 0.183, 0.0395, 0.0149 and 3.5e-3: a
gain of 1.7 times at `n = 7` rising to 38 times at `n = 15`.

## 3. Numerical check

`study/reff-bound-check.py` builds 24 near-doubly-stochastic matrices with a zero, at `n = 5, 7,
10, 12`, three entry spreads and two margin sizes, and checks both inequalities of (*) against the
attained maximum of `|alpha_i + beta_j|` over the support. All 24 held. Over the same 24 cases
the resistance bound was up to 60 times smaller than Lemma 3(c)'s.

## 4. What the lemma does not give, and why that is stated here

Extending condition (N) from the entries with `a_ij >= Phi` to every entry needs two further
statements, and both are false on the natural relaxation (`study/removing-condition-N.md`,
move 4).

1. *An entrywise lower bound on a near-maximiser.* Minimising the smallest positive entry over
   doubly stochastic matrices with a zero and `per <= 1.05 gamma_n` reaches 2.9e-2 at `n = 5`,
   **3.6e-28** at `n = 6`, **9.3e-29** at `n = 7` and 5.6e-4 at `n = 8`. The Knopp-Sinkhorn
   extremal has smallest entry `(n-2)/(n-1)^2 ~ 1/n`, so no bound of that order survives the
   relaxation.
2. *A margin repair after truncating the entries below `Phi`.* Truncation moves the margins by at
   most `sum (a_ij + sqrt(a_ij Phi)) <= n^1.5 sqrt(Phi) + n^2 Phi`, and `Phi >= 2 delta` always,
   so the error exceeds the original margin size `sqrt(delta)` by a factor of at least
   `n^1.5 sqrt(2)`. The repair enlarges what it repairs.

A caveat on both refutations: the constraint set of the real problem is conjecturally empty
(unit 4), so each test above is a test of a relaxation, and a relaxation that is non-empty is one
in which the structure being sought can be absent. What the two results establish is that no
argument for the entrywise bound can use only the relaxed hypothesis.

## 5. References

- Cheon and Wanless, *An update on Minc's survey of open problems involving permanents*, Linear
  Algebra and its Applications 436 (2012) 1197-1218, Theorems 2.1, 3.2 and 3.7.
- Theorem R and its Lemmas 2 and 3 are in the sibling attack,
  `attack/dittert-conjecture-n5-to-n15/study/route-a-reduction-theorem.md`.

## 6. Ledger

Bound quality: the new condition is weaker in `delta` but is now entrywise, so it does not
dominate Lemma 3(c) uniformly. Obligations: the two statements of section 4 stand refuted on the
relaxation and unresolved on the true constraint set.
