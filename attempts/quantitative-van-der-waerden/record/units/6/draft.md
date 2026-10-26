# Where the quantitative van der Waerden route stops

**Form.** Barrier. **Venue.** On the path, as the statement of where it stops.

## 1. For the claim: the one-column ceiling and the two-column residue

Every argument in the record that sees one column, or one permutation, at a time stops at the
constant 1/(2n):

- Unit 1 is an equality at sparse uniform columns for every completion of the matrix, so no bound
  of the form gamma_{n-1} F(column) gives a constant above about 0.6/n
  (route-capacity.md, section 5).
- Every input of the one-variable interpolation f(t) = per(J_n/n + tE) is a lower bound at points
  of one segment, and in the Bernstein form the endpoint value is a free coordinate, so no
  combination of van der Waerden, Friedland, the local theorem, the exponential bound along the
  ray, and Newton inequalities gives more than exp(||E||^2/(2n)) at t = 1
  (route-interpolation.md, 6.1).
- Every pointwise-in-permutation scheme gives a negative constant for n >= 5, because the
  second-order deficiency is a 1/n effect of the permutation constraint (route-interpolation.md,
  6.2).
- The sequential two-column forms are false: cap(q_{n-2}) >= g(n-1) e^{d/2} cap(q_{n-1}) fails
  with ratio 0.967 at n = 4 (route-capacity.md, Two-column theorem, section 2). So the two-column
  gain is a joint quantity and cannot be obtained one column at a time by any argument.
- The Holens-Dokovic monotonicity of the subpermanent sums, which would make the termwise chain
  a proof, is false at n = 22 (Wanless, Linear Algebra Appl. 286 (1999)).

The residue for the constant 1/n, and hence for n = 7 in unit 5, is one inequality:

    (I2)  C_2(v, v') K(v + v') >= g(n) g(n-1) exp( (d + d')/2 )

for probability vectors v, v' (the two columns) with v + v' <= 1, where C_2 is the capacity of
the two-column polynomial, d = ||v - 1/n||^2, d' = ||v' - 1/n||^2, and K, g are as in units 1
and 2. It holds numerically at n = 4 to 7 with ratio 1 only at v = v' = 1/n; it is proved for
disjoint supports and locally at the centre; its only tight direction is v' = 2/n - v; and it
was reduced to an elementary inequality (star)
plus an a priori oscillation bound (T) on the optimiser of C_2, with 59 percent numerical room on
the n = 7 region (route-capacity.md, Drop lemma via the two-scalar reduction). Every provable
lower bound on the Hessian of the capacity goes through the smallest column entry, which can be
0.02 on that region, and is degenerate for disjoint supports; that is what blocks (T).

## 2. For the application: the near-decomposable branch

The Dittert deduction of unit 5 is a fixed-point inequality with two solution branches. The
small-cost branch is excluded at every n >= 8. The large-cost branch, K >= K_2(n) and
lambda_2(B) <= 1 - sqrt(2 n K_2(n)), is not: on it the scaling of the counterexample is
near-decomposable, and excluding it needs a lower bound on the permanent of a near-decomposable
doubly stochastic matrix that is far above gamma_n. Unit 2 gives only exp(||E||^2/(2n)), which at
||E||^2 = 1 (the block-diagonal value) is 1 + 1/(2n) and consistent with the branch. This is the
barrier of attack/spectral-gap-near-maximisers, unit 5, unchanged in substance and now stated
with the exact threshold.

## 3. What would remove either barrier

For the claim: a proof of (I2), or of any two-column bound with constant above 0.36 per column at
n = 7. For the application: any statement per(B) >= (1 + c) gamma_n for doubly stochastic B with
lambda_2(B) <= 0.13 and c above K_2(n), which at n = 8 means c > 0.05; numerically the truth on
that set is far larger (the block-diagonal value is about 2.5 gamma_n).

## 4. Ledger

Bound quality: the constant stays at 1/(2n). Obligations: (I2) and the near-decomposable bound.
