# The quantitative van der Waerden inequality at n = 3, sharp

**Form.** Conditional or special-case result. **Venue.** On the path, at the dimension where the
claim is tight.

## 1. Statement

For every doubly stochastic 3 by 3 real matrix B,

    per(B) >= (2/9) ( 1 + ||B - J_3/3||_F^2 / 4 ),

with equality exactly at J_3/3 and at the six row and column permutations of (I + C_3)/2, where
C_3 is the 3-cycle. No constant larger than 1/4 holds at n = 3.

## 2. Proof

Write the rows of B as probability vectors b, and e_2(b), e_3(b) for their elementary symmetric
functions. The identity, valid on the doubly stochastic matrices,

    per(B)/gamma_3 - 1 - ||B - J_3/3||_F^2 / 4 = sum over the three rows of ( 1 - 4 e_2(b) + 9 e_3(b) ),

is a polynomial identity in the four free entries once the six margin equations are substituted;
it is checked in exact rational arithmetic in study/route-interpolation-06-exact.py. For a
probability vector b, 1 - 4 e_2 + 9 e_3 = e_1^3 - 4 e_1 e_2 + 9 e_3 is the degree-one Schur
expression sum_x x (x - y)(x - z) over the coordinates, which is nonnegative for nonnegative x, y,
z, with equality exactly when x = y = z or when two coordinates are equal and the third is 0.
Summing over rows gives the inequality. The equality cases are the matrices all of whose rows
are (1/3, 1/3, 1/3) or (1/2, 1/2, 0) up to order, subject to the column sums: J_3/3 and the
permutations of (I + C_3)/2. Sharpness: at (I + C_3)/2 the ratio is exactly 1/4 (unit 4). QED

## 3. Checks

The identity: exact rational arithmetic on a symbolic doubly stochastic 3 by 3 matrix
(study/route-interpolation-06-exact.py). The sharp constant: unit 4, c*(3) = 0.250000, attained
at (I + C_3)/2, with per = 1/4 and ||(I + C_3)/2 - J_3/3||^2 = 1/2.

A Lean 4 encoding of the statement on the nine entries, with Schur proved by a case split on the
order of the variables and the inequality closed by nlinarith, is in
deterministic/formal-check-1/QvdW3b.lean; its build was starved by the machine load at the time
of writing and is recorded there as run or not run.

## 4. References

- Schur inequality of degree one, classical.
- Marcus and Newman, On the minimum of the permanent of a doubly stochastic matrix, Duke Math.
  J. 26 (1959) 61-72, for the plain n = 3 case.

## 5. Ledger

Object: the unit is about one dimension, not about the claim.
