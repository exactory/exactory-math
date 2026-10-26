# A one-column deficiency term in the capacity proof of van der Waerden

**Form.** New machinery. **Venue.** On the path to the quantitative van der Waerden inequality.

## 1. Statement

Let B be a doubly stochastic n by n real matrix, n >= 2, gamma_m = m!/m^m, and for a column
index j let v = (b_1j, ..., b_nj), a probability vector. Then

    per(B) >= gamma_{n-1} * K(v),        K(v) = prod_{s=1}^{n} (1 - v_s)^(1 - v_s),   0^0 = 1.

The same holds for every row. Equality holds whenever v is uniform on its support: for the
Knopp-Sinkhorn face minimisers T_n, for the sparse-column matrices of Gurvits (arXiv:0711.3496,
equation (19)), and at (I + C_3)/2.

## 2. Proof

Write p_B(x) = prod_i sum_j b_ij x_j, homogeneous of degree n, with per(B) as its coefficient of
x_1 ... x_n. Take j = n. Peel x_n once: q(x) = (d/dx_n) p_B(x, 0) = sum_r v_r prod_{s != r} l_s(x),
with l_s(x) = sum_{j <= n-1} b_sj x_j, a polynomial of degree n-1 in n-1 variables with
non-negative coefficients whose coefficient of x_1 ... x_{n-1} is per(B).

**Lemma A.** For every x > 0, q(x) >= K(v) x_1 ... x_{n-1}; hence cap(q) >= K(v), where
cap(q) = inf_{x > 0} q(x) / (x_1 ... x_{n-1}).

If some v_s = 1 then row s is supported on column n alone, the remaining (n-1) by (n-1) block is
doubly stochastic, and AM-GM row by row gives q(x) >= prod_j x_j with K(v) = 1. Otherwise write
a_s = l_s(x) > 0, so q(x) = (prod_s a_s) sum_r v_r / a_r. Weighted AM-GM with weights v gives
sum_r v_r / a_r >= prod_r a_r^(-v_r), hence q(x) >= prod_s a_s^(1 - v_s). For each s the weights
b_sj / (1 - v_s), j <= n-1, sum to 1, so a_s / (1 - v_s) >= prod_j x_j^(b_sj/(1-v_s)) and
a_s^(1-v_s) >= (1 - v_s)^(1 - v_s) prod_j x_j^(b_sj). Multiplying over s and using the column
sums sum_s b_sj = 1 for j <= n-1 gives prod_s a_s^(1-v_s) >= K(v) prod_j x_j. QED

**Lemma B.** per(B) >= gamma_{n-1} cap(q). This is Gurvits theorem applied to q: p_B is H-stable
because every row of B is non-zero, q is H-stable as a derivative of an H-stable polynomial
evaluated at x_n = 0 (Gurvits, Fact 4.9(2); Laurent and Schrijver, Theorem 1), q is non-zero
because per(B) > 0 (Birkhoff), and Gurvits Corollary 2.5 for q in Hom_+(n-1, n-1) gives the
mixed derivative at 0, which is per(B), at least (n-1)!/(n-1)^(n-1) cap(q).

The theorem follows. For rows apply it to the transpose. QED

## 3. What it contains

- **Knopp-Sinkhorn.** If b_sj = 0 for some s then Jensen on the other n-1 coordinates gives
  K(v) >= (1 - 1/(n-1))^(n-2) = g(n-1) and per(B) >= gamma_{n-1} g(n-1) = m_n.
- **Gurvits degree bound.** Jensen over the support of v gives K(v) >= g(#supp v), which is
  Theorem 4.10 of arXiv:0711.3496 after one peeling; the theorem is strictly stronger for every
  column that is not uniform on its support.

## 4. Checks

study/verify-capacity-claim.py reimplements the statement from this text alone and evaluates
it, for every column, on about 500 doubly stochastic matrices per n at n = 2 to 7: the vertices,
block-diagonal families and their segments to the centre, T_n, (I + C_n)/2, random matrices at
four entry spreads, and sparse supports. The minimum ratio per(B) / (gamma_{n-1} K(v)) is exactly
1.0000000000 at every n (equality cases were hit); no case fell below 1. The Fable route file
route-capacity.md checks Lemma A pointwise and the identities symbolically at n = 3, 4.

## 5. References

- Gurvits, Van der Waerden / Schrijver-Valiant like conjectures and stable (aka hyperbolic)
  homogeneous polynomials: one theorem for all, Electron. J. Combin. 15 (2008) R66,
  arXiv:0711.3496.
- Laurent and Schrijver, On Leonid Gurvits proof for permanents, Amer. Math. Monthly 117 (2010)
  903-911.
- Knopp and Sinkhorn, Minimum permanents of doubly stochastic matrices with at least one zero
  entry, Linear and Multilinear Algebra 11 (1982) 351-355.

## 6. Ledger

Bound quality: the theorem sees one column, and one column cannot give a constant above about
0.6/n in the claim (route-capacity.md, section 5).
