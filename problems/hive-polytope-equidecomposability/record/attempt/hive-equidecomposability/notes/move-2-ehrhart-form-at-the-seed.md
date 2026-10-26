# Move 2: the Ehrhart form N1 tested at the seed instance

Entry: test-strengthenings-by-counterexample (strategy attack-the-negative-side). The
neighbouring statements that would be refuted by a counterexample of type (i) of move 1 are
N1 (some lattice polytope has Ehrhart polynomial c^{t nu}_{t lambda, t mu}) and its
consequence N4 (nonnegative numerator); small instances are computable by hand. This move
tests N1 at the first non-lattice five-part instance of the exploratory scan, by hand.

## 1. The seed instance identified

Pair (n, lambda, mu, nu) = (5, (4,3,2,1), (3,2), (5,4,3,2,1)). Conventions: the hive array
of side 5 has vertices (x, y), x, y >= 0, x + y <= 5; the border labels are h(0, 0) = 0,
h(0, y) = lambda_1 + ... + lambda_y on the left edge, h(x, 0) = nu_1 + ... + nu_x on the
bottom edge and h(x, 5 - x) = |lambda| + mu_1 + ... + mu_x on the right edge:

    h(0,1) = 4, h(0,2) = 7, h(0,3) = 9, h(0,4) = 10, h(0,5) = 10,
    h(1,0) = 5, h(2,0) = 9, h(3,0) = 12, h(4,0) = 14, h(5,0) = 15,
    h(1,4) = 13, h(2,3) = 15, h(3,2) = 15, h(4,1) = 15.

(The other assignment of the two small partitions to the left and right edges gives a hive
polytope that is the image of this one under a coordinate permutation composed with an
integral translation; its derivation from its own rhombus inequalities is Section 8 of
`../proofs/smallest-instance.md`. So the choice of convention does not affect anything below.)

The six interior vertices in the order (1,1), (1,2), (1,3), (2,1), (2,2), (3,1) carry the
coordinates x_1, ..., x_6. The rhombus inequalities in the three orientations are

    (A) h(x+1,y) + h(x,y+1) >= h(x,y) + h(x+1,y+1)      (x, y >= 0, x + y <= 3),
    (B) h(x,y) + h(x+1,y)   >= h(x,y+1) + h(x+1,y-1)    (y >= 1, x + y <= 4),
    (C) h(x,y) + h(x,y+1)   >= h(x+1,y) + h(x-1,y+1)    (x >= 1, x + y <= 4).

Forced coordinates. (B) at (3,1): x_6 + h(4,1) >= h(3,2) + h(4,0), i.e. x_6 >= 14; (C) at
(4,0): h(4,0) + h(4,1) >= h(5,0) + x_6, i.e. x_6 <= 14. So x_6 = 14. (C) at (3,1):
x_6 + h(3,2) >= h(4,1) + x_5, i.e. x_5 <= 14; (B) at (2,2): x_5 + h(3,2) >= h(2,3) + x_6, i.e.
x_5 >= 14. So x_5 = 14. (C) at (3,0): h(3,0) + x_6 >= h(4,0) + x_4, i.e. x_4 <= 12; (B) at
(2,1): x_4 + x_6 >= x_5 + h(3,0), i.e. x_4 >= 12. So x_4 = 12.

The remaining inequalities, after substituting the border and the forced values (the rhombi
giving each are listed; (A) at (2,0), (2,1), (3,0) reduce to the constants 1 >= 0 and (C) at
(2,2) to x_3 <= 14, implied by (B) at (0,4)):

    x_1 <= 9          (A)(0,0), (C)(2,0)
    x_1 >= 8          (B)(0,1), (A)(1,0), (C)(1,0)
    x_3 <= 13         (B)(0,4)
    x_3 >= 12         (A)(0,3), (B)(1,3), (C)(1,3)
    x_2 <= 12         (C)(2,1)
    x_2 - x_1 >= 2    (B)(0,2), (A)(1,1)
    x_2 - x_1 <= 3    (A)(0,1), (B)(1,1)
    x_3 - x_2 >= 1    (B)(0,3), (A)(1,2)
    x_3 - x_2 <= 2    (A)(0,2), (B)(1,2)
    x_1 + x_2 >= 19   (C)(1,1)
    x_2 + x_3 >= 23   (C)(1,2)

With x = x_1 - 8, y = x_2 - 11, z = x_3 - 12 these read x <= 1, x >= 0, z <= 1, z >= 0,
y <= 1, x - 1 <= y <= x, z - 1 <= y <= z, y >= -x, y >= -z, where x >= 0, z >= 0 and y <= 1
follow from the others. Hence, inside the affine 3-plane {x_4 = 12, x_5 = 14, x_6 = 14}
whose lattice points form a copy of Z^3,

    H - (8, 11, 12, 12, 14, 14) = P := {x <= 1, z <= 1, y <= x, y <= z, y >= x-1, y >= z-1, y >= -x, y >= -z}.

P n {y >= 0} = {0 <= y <= min(x, z), x, z <= 1} is the pyramid with apex p = (1, 1, 1) over
the unit square S = [0,1] x {0} x [0,1]; P n {y <= 0} = {max(x-1, z-1, -x, -z) <= y <= 0}
is the pyramid with apex w = (1/2, -1/2, 1/2) over S. So P = conv(S u {p, w}) has the six
vertices (0,0,0), (1,0,0), (0,0,1), (1,0,1), p, w, dim P = 3, and w is half-integral: the
hive polytope is not a lattice polytope (this is the instance's non-integral vertex of
condition C3).

## 2. The Ehrhart polynomial of the seed, by hand

For t >= 1 the lattice points of tP are counted level by level in y. Upper pyramid: at
height y = k (0 <= k <= t) the section is the square [k, t]^2 in (x, z)... more precisely
{(x, z) : k <= x <= t, k <= z <= t}, with (t - k + 1)^2 lattice points; total
sum_{m=1}^{t+1} m^2 = (t+1)(t+2)(2t+3)/6. Lower pyramid, levels y = -j with
1 <= j <= t/2: the section is {j <= x <= t - j, j <= z <= t - j}, with (t - 2j + 1)^2
points. So L_P(1) = 5 + 0 = 5, L_P(2) = 14 + 1 = 15, L_P(3) = 30 + 4 = 34. Since L_P is a
polynomial of degree 3 with L_P(0) = 1 (Ehrhart; the period collapse of hive polytopes is a
theorem, and in this instance it is also visible directly: the count is (t+1)(t+2)(2t+3)/6 +
sum_{1 <= j <= t/2} (t-2j+1)^2 = 1 + 2t + (3/2)t^2 + (1/2)t^3 for t even and for t odd
alike, as one checks from the two closed forms), the four values determine it:

    L_H(t) = c^{t nu}_{t lambda, t mu} = 1 + 2t + (3/2) t^2 + (1/2) t^3,

with h*-vector (1, 1, 1, 0) (from L(1) = 5 = 4 + h*_1, L(2) = 15 = 10 + 4 h*_1 + h*_2,
L(3) = 34 = 20 + 10 h*_1 + 4 h*_2 + h*_3).

## 3. N1 holds at the seed: a lattice polytope with the same Ehrhart polynomial

Let Q' = conv{0, e_1, e_2, e_3, (1,1,1)} in R^3. It is the union of the unimodular simplex
Delta = conv{0, e_1, e_2, e_3} and the tetrahedron T' = conv{e_1, e_2, e_3, (1,1,1)} along the
triangle conv{e_1, e_2, e_3} (the segment from 0 to (1,1,1) crosses that triangle at its
centroid, so the union is convex). The lattice points of tT' are the integer points
(x, y, z) = a e_1 + b e_2 + c e_3 + d (1,1,1) with a, b, c, d >= 0 and a + b + c + d = t,
that is, with s = x + y + z: d = (s - t)/2 >= 0 and x, y, z >= d. Counting:

    t = 1: Delta gives 4, T' beyond the triangle gives (1,1,1) only: L_{Q'}(1) = 5;
    t = 2: 2 Delta gives 10; s = 3: (1,1,1); s = 4: (2,1,1), (1,2,1), (1,1,2); s = 6: (2,2,2);
           L_{Q'}(2) = 10 + 1 + 3 + 1 = 15;
    t = 3: 3 Delta gives 20; s = 4: three points (2,1,1) and permutations; s = 5: six points
           (x, y, z >= 1 summing to 5); s = 6: (2,2,2); s = 7: (3,2,2) and permutations, three
           points; s = 9: (3,3,3); L_{Q'}(3) = 20 + 3 + 6 + 1 + 3 + 1 = 34.

(The points of tT' with s = t lie on the shared triangle and are counted in t Delta.) Hence
L_{Q'} and L_H agree at t = 0, 1, 2, 3 and both are cubic: L_{Q'} = L_H. So the Ehrhart form
N1 holds for the seed instance, with Q' a lattice 3-polytope with five lattice points and
h*-vector (1, 1, 1, 0); the necessary inequalities of move 1 (nonnegativity, the interior
bound h*_3 <= h*_1, Hibi's lower bound, Stanley's inequality, Hibi 1990, the universal
inequality for h*_3 = 0) are all satisfied, as they must be. The seed is therefore not a
counterexample of type (i); whether it is one of type (ii) is decided by the constructive
strategy (move 4).

## 4. Outcome of the test

No counterexample to N1 appears in the range tested by hand (the seed), and N1 is as hard as
the target in general (a lattice-realizable polynomial does not give the geometric
decomposition, by Turner-Wu's examples in dimension 2), so the entry's failure signal fires:
the strengthening is a target, not a test. The record gains the identification of the seed
polytope (used by move 4) and the hand-proved N1 instance.
