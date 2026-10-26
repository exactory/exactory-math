# The seed instance: the hive polytope of (5, (4,3,2,1), (3,2), (5,4,3,2,1)) is equidecomposable with a lattice polytope

Claim (obligation-000002). For n = 5 and the triple nu = (5,4,3,2,1), lambda = (4,3,2,1),
mu = (3,2) (so |lambda| + |mu| = 10 + 5 = 15 = |nu| and c^nu_{lambda mu} = 5), the hive
polytope H = H(lambda, mu, nu) in R^6 is GL_6(Z)-equidecomposable with a lattice polytope: H
is a disjoint union of finitely many relatively open rational simplices T_i, and there are
affine unimodular maps U_i with pairwise disjoint images whose union is a convex polytope
with integral vertices.

## 0. Conventions

The hive array of side 5 has vertices (x, y) with x, y >= 0 and x + y <= 5. The border labels
are h(0, 0) = 0, h(0, y) = lambda_1 + ... + lambda_y on the left edge, h(x, 0) = nu_1 + ... +
nu_x on the bottom edge, and h(x, 5 - x) = |lambda| + mu_1 + ... + mu_x on the right edge:

    h(0,1) = 4, h(0,2) = 7, h(0,3) = 9, h(0,4) = 10, h(0,5) = 10,
    h(1,0) = 5, h(2,0) = 9, h(3,0) = 12, h(4,0) = 14, h(5,0) = 15,
    h(1,4) = 13, h(2,3) = 15, h(3,2) = 15, h(4,1) = 15.

The six interior vertices are ordered (1,1), (1,2), (1,3), (2,1), (2,2), (3,1), with
coordinates x_1 = h(1,1), x_2 = h(1,2), x_3 = h(1,3), x_4 = h(2,1), x_5 = h(2,2),
x_6 = h(3,1). The rhombus inequalities ("the sum of the labels at the two obtuse vertices of
each unit rhombus is at least the sum at the two acute vertices") are, in the three
orientations,

    (A) h(x+1,y) + h(x,y+1) >= h(x,y) + h(x+1,y+1)      (x, y >= 0, x + y <= 3),
    (B) h(x,y) + h(x+1,y)   >= h(x,y+1) + h(x+1,y-1)    (y >= 1, x + y <= 4),
    (C) h(x,y) + h(x,y+1)   >= h(x+1,y) + h(x-1,y+1)    (x >= 1, x + y <= 4).

On the convention. The root statement places the partial sums of lambda, mu and nu on the
three sides without fixing which of the two small partitions is read first; the orientation
of the array is immaterial (a symmetry of the triangle permutes the interior coordinates,
which is a unimodular map). So there are two hive polytopes to consider: the one above, with
lambda = (4,3,2,1) on the left edge and mu = (3,2) on the right edge, and the one with the
two small partitions exchanged. Sections 1 to 7 prove the claim for the first; Section 8
derives the second from its own thirty rhombus inequalities and shows that it is the image of
the first under an explicit coordinate permutation composed with an integral translation, so
the claim holds for both readings.

## 1. The three forced coordinates

(B) at (3,1) reads x_6 + h(4,1) >= h(3,2) + h(4,0), that is x_6 >= 14; (C) at (4,0) reads
h(4,0) + h(4,1) >= h(5,0) + x_6, that is x_6 <= 14. So x_6 = 14. (C) at (3,1) reads
x_6 + h(3,2) >= h(4,1) + x_5, that is x_5 <= 14; (B) at (2,2) reads x_5 + h(3,2) >=
h(2,3) + x_6, that is x_5 >= 14. So x_5 = 14. (C) at (3,0) reads h(3,0) + x_6 >= h(4,0) + x_4,
that is x_4 <= 12; (B) at (2,1) reads x_4 + x_6 >= x_5 + h(3,0), that is x_4 >= 12. So
x_4 = 12. Hence H lies in the affine 3-plane A = {x_4 = 12, x_5 = 14, x_6 = 14}, and
Z^6 n A = {(x_1, x_2, x_3, 12, 14, 14)} is a copy of Z^3 with coordinates (x_1, x_2, x_3).

## 2. The eight facets

The complete list of rhombus inequalities of the side-5 array is the 30 inequalities below
(every (A) with x + y <= 3, every (B) with y >= 1 and x + y <= 4, every (C) with x >= 1 and
x + y <= 4), written with the border labels substituted; the six used in Step 1 are included.
After substituting x_4 = 12, x_5 = 14, x_6 = 14 they become:

    (A)(0,0): 9 - x_1 >= 0            (A)(0,1): x_1 - x_2 + 3 >= 0      (B)(0,1): x_1 - 8 >= 0
    (A)(0,2): x_2 - x_3 + 2 >= 0      (B)(0,2): x_2 - x_1 - 2 >= 0      (A)(0,3): x_3 - 12 >= 0
    (B)(0,3): x_3 - x_2 - 1 >= 0      (B)(0,4): 13 - x_3 >= 0           (A)(1,0): x_1 - 8 >= 0
    (C)(1,0): x_1 - 8 >= 0            (A)(1,1): x_2 - x_1 - 2 >= 0      (B)(1,1): x_1 - x_2 + 3 >= 0
    (C)(1,1): x_1 + x_2 - 19 >= 0     (A)(1,2): x_3 - x_2 - 1 >= 0      (B)(1,2): x_2 - x_3 + 2 >= 0
    (C)(1,2): x_2 + x_3 - 23 >= 0     (B)(1,3): x_3 - 12 >= 0           (C)(1,3): x_3 - 12 >= 0
    (A)(2,0): 1 >= 0                  (C)(2,0): 9 - x_1 >= 0            (A)(2,1): 1 >= 0
    (B)(2,1): 0 >= 0 (used: x_4)      (C)(2,1): 12 - x_2 >= 0           (B)(2,2): 0 >= 0 (used: x_5)
    (C)(2,2): 14 - x_3 >= 0           (A)(3,0): 1 >= 0                  (C)(3,0): 0 >= 0 (used: x_4)
    (B)(3,1): 0 >= 0 (used: x_6)      (C)(3,1): 0 >= 0 (used: x_5)      (C)(4,0): 0 >= 0 (used: x_6)

(For instance (C)(1,1) is h(1,1) + h(1,2) >= h(2,1) + h(0,2), that is x_1 + x_2 >= 12 + 7;
(A)(1,2) is h(2,2) + h(1,3) >= h(1,2) + h(2,3), that is 14 + x_3 >= x_2 + 15.) The
inequality (C)(2,2), x_3 <= 14, is implied by (B)(0,4). Write x = x_1 - 8, y = x_2 - 11,
z = x_3 - 12 (an integral translation of the Z^3 of Step 1). The list becomes

    x <= 1,  x >= 0,  z <= 1,  z >= 0,  y <= 1,  y >= x - 1,  y <= x,  y <= z,  y >= z - 1,
    y >= -x,  y >= -z,

where x >= 0 follows from y >= -x and y <= x, z >= 0 from y >= -z and y <= z, and y <= 1 from
y <= x <= 1. Therefore

    H - (8, 11, 12, 12, 14, 14) = P := {(x, y, z) in R^3 : x <= 1, z <= 1, y <= x, y <= z,
                                         y >= x - 1, y >= z - 1, y >= -x, y >= -z}

inside A (with (x, y, z) the coordinates (x_1, x_2, x_3) of A shifted). The set P is the union
of two pyramids over the unit square S = [0,1] x {0} x [0,1]: P n {y >= 0} = {0 <= y <=
min(x, z), x <= 1, z <= 1} = conv(S u {p}) with p = (1, 1, 1) (a point with y >= 0 satisfies
the eight inequalities exactly when 0 <= y <= min(x, z) and x, z <= 1, and that set is the
pyramid: its sections at height y are the squares [y, 1]^2), and P n {y <= 0} =
{max(x - 1, z - 1, -x, -z) <= y <= 0} = conv(S u {w}) with w = (1/2, -1/2, 1/2) (its sections
at height y = -s, 0 <= s <= 1/2, are the squares [s, 1 - s]^2, which shrink linearly to the
point (1/2, 1/2) at s = 1/2). The union of the two pyramids is convex because the segment from
p to w meets S at (2/3, 0, 2/3), in the relative interior of S. So P is a convex polytope
with vertices (0,0,0), (1,0,0), (0,0,1), (1,0,1), p and w, five of them integral and one
half-integral; dim P = 3; H is not a lattice polytope; and #(P n Z^3) = 5 =
c^nu_{lambda mu} (the five integral vertices: at y = 0 the lattice points of S are its
corners, at y = 1 only p, and no lattice point has y < 0 since y >= -1/2).

## 3. The cut and the shear

Let l(x, y, z) = x - z, a primitive integral linear form, and Pi = {l = 0}. Set

    P_+ = P n {l >= 0},   P_- = P n {l <= 0},   K = P n Pi,

and let U : R^3 -> R^3, U(x, y, z) = (x, y + x - z, z). U is linear with matrix
[[1, 0, 0], [1, 1, -1], [0, 0, 1]] of determinant 1 and integral inverse
U^{-1}(x, y, z) = (x, y - x + z, z), so U is in GL_3(Z); it fixes Pi pointwise and preserves
x and z, hence preserves l.

On P_- (where x <= z) the inequalities y <= z, y >= x - 1 and y >= -z follow from y <= x,
y >= z - 1 and y >= -x respectively, and x <= 1 follows from x <= z <= 1; so

    P_- = {x <= z <= 1,  -x <= y <= x,  y >= z - 1}.

With (x', y', z') = U(x, y, z), that is x' = x, z' = z, y = y' - x' + z', this becomes

    U(P_-) = {x' <= z' <= 1,  y' >= -z',  y' >= x' - 1,  y' <= 2x' - z'}.

(The inequality -x <= y gives y' - x' + z' >= -x', that is y' >= -z'; y <= x gives
y' <= 2x' - z'; y >= z - 1 gives y' >= x' - 1.) Similarly, on P_+ (where x >= z) the binding
inequalities are z <= x <= 1, -z <= y <= z and y >= x - 1:

    P_+ = {z <= x <= 1,  -z <= y <= z,  y >= x - 1}.

Define

    Q = {(x, y, z) in R^3 : x <= 1,  z <= 1,  y >= -z,  y >= x - 1,  y <= z,  y <= 2x - z}.

On {x >= z}, 2x - z >= z, so y <= 2x - z is implied by y <= z, and Q n {l >= 0} = P_+. On
{x < z}, 2x - z < z, so y <= z is implied by y <= 2x - z, and Q n {l < 0} = U(P_-) n {l < 0}
= U(P_- \ K) (U preserves l). Hence

    Q = P_+ u U(P_- \ K)   and   P = P_+ u (P_- \ K),   both disjoint unions.

## 4. Q is a lattice polytope

Q is bounded: y <= z and y >= -z give z >= 0; y <= 2x - z and y >= x - 1 give x >= z - 1 >=
-1; with x <= 1 and z <= 1 this gives -1 <= x <= 1, 0 <= z <= 1 and -1 <= y <= 1. Its
vertices are the points of Q where three of the six bounding planes meet with linearly
independent normals; checking the twenty triples: (0, 0, 0) (y = -z, y = z, y = 2x - z);
(1, 0, 0) (x = 1, y = -z, y = z); (1, 0, 1) (x = 1, z = 1, y = x - 1); (1, 1, 1) (x = 1,
z = 1, y = z, also y = 2x - z); (0, -1, 1) (z = 1, y = -z, y = x - 1, also y = 2x - z); the
remaining triples meet outside Q or in these points (for instance y = z, y = 2x - z and
y = x - 1 force z = x and x - 1 = x). So Q = conv{(0,0,0), (1,0,0), (1,0,1), (1,1,1),
(0,-1,1)} has five vertices, all in Z^3: Q is a lattice polytope. (The point w =
(1/2, -1/2, 1/2) is the midpoint of (1, 0, 0) and U(0, 0, 1) = (0, -1, 1), which is why it is
no longer a vertex.)

## 5. The decomposition into relatively open rational simplices

Triangulate P by a triangulation with rational vertices that refines the cut by Pi: for
instance, triangulate the quadrilateral K = conv{(0,0,0), (1,0,1), p, w} (all four points lie
on Pi; K is a convex quadrilateral in that plane) into the two triangles conv{0, (1,0,1), p}
and conv{0, (1,0,1), w}, then cone each of the two triangles from the apex (1, 0, 0) and
from the apex (0, 0, 1): this gives four closed tetrahedra with rational vertices,
conv{0, (1,0,1), p, a}, conv{0, (1,0,1), w, a} for a = (1,0,0) and for a = (0,0,1), whose
union is P (P_+ is the pyramid conv(K u {(1,0,0)}) and P_- the pyramid conv(K u {(0,0,1)}),
since P_+ = {z <= x <= 1, ...} is the convex hull of K and (1,0,0): every vertex of P with
x >= z is a vertex of K or (1,0,0), and similarly for P_-) and which meet along common faces
(the two tetrahedra over the same triangle of K meet exactly in that triangle, and the two
tetrahedra over the same apex meet in the triangle conv{0, (1,0,1), a}). The relatively open
faces of all dimensions (0 to 3) of these four tetrahedra, each counted once, partition P
into relatively open rational simplices T_1, ..., T_r. Put U_i = identity when T_i lies in
P_+ (every face of the two tetrahedra with apex (1,0,0), including the faces in K) and
U_i = U when T_i lies in P_- \ K (the faces of the two tetrahedra with apex (0,0,1) that are
not contained in Pi). The images are pairwise disjoint: U preserves l, so the images of the
second kind lie in {l < 0} and those of the first kind in {l >= 0}, and within each kind the
pieces are disjoint because U is injective and the T_i are disjoint. Their union is
P_+ u U(P_- \ K) = Q.

## 6. Back in R^6

Compose with the integral translation by c = (8, 11, 12, 12, 14, 14) and extend U to R^6 by
the identity on the coordinates x_4, x_5, x_6: the map V(x_1, ..., x_6) = (x_1, x_2 + x_1 -
x_3, x_3, x_4, x_5, x_6) has an integral matrix of determinant 1, so V is in GL_6(Z), and it
preserves the affine 3-plane A. The pieces T_i + c (T_i placed in A through (x, y, z) ->
(x + 8, y + 11, z + 12, 12, 14, 14)) are relatively open rational simplices with disjoint
union H; the maps are x -> x (for the first kind) and x -> V(x - c) + c (for the second kind),
affine unimodular; and the union of the images is Q + c = conv{(8,11,12,12,14,14),
(9,11,12,12,14,14), (9,11,13,12,14,14), (9,12,13,12,14,14), (8,10,13,12,14,14)}, a convex
polytope with integral vertices. This proves the claim.

## 7. Consequence

Since every map is affine unimodular and the construction is compatible with dilation (U is
linear and the pieces of tP are the dilates of the pieces of P, as the defining inequalities
of P_+, P_- and Q are homogeneous), #(tH n Z^6) = #(t(Q + c) n Z^6) for every t >= 1: the
stretched polynomial c^{t nu}_{t lambda, t mu} = 1 + 2t + (3/2)t^2 + (1/2)t^3 (note of move
2, section 2) is the Ehrhart polynomial of a lattice 3-polytope with h*-vector (1, 1, 1, 0).

Exploratory check (no native credit): `../checks/seed_check.py` recomputes with Normaliz the
Ehrhart polynomials of P and Q (both 1 + 2t + (3/2)t^2 + (1/2)t^3) and verifies for
t = 1, ..., 6 that every lattice point of tQ with x >= z lies in tP and every lattice point of
tQ with x < z is the U-image of a lattice point of tP with x < z.

## 8. The other reading of the convention

Now put mu = (3,2) on the left edge and lambda = (4,3,2,1) on the right edge (nu stays on the
bottom edge). The border labels are

    h(0,1) = 3, h(0,2) = 5, h(0,3) = 5, h(0,4) = 5, h(0,5) = 5,
    h(1,0) = 5, h(2,0) = 9, h(3,0) = 12, h(4,0) = 14, h(5,0) = 15,
    h(1,4) = 9, h(2,3) = 12, h(3,2) = 14, h(4,1) = 15,

(the right edge carries |mu| + lambda_1 + ... + lambda_x = 5 + (4, 7, 9, 10, 10)), and the
thirty rhombus inequalities, with the same coordinates x_1, ..., x_6 for the interior
vertices (1,1), (1,2), (1,3), (2,1), (2,2), (3,1), are

    (A)(0,0): 8 - x_1 >= 0            (A)(0,1): x_1 - x_2 + 2 >= 0      (B)(0,1): x_1 - 7 >= 0
    (A)(0,2): x_2 - x_3 >= 0          (B)(0,2): x_2 - x_1 >= 0          (A)(0,3): x_3 - 9 >= 0
    (B)(0,3): x_3 - x_2 >= 0          (B)(0,4): 9 - x_3 >= 0            (A)(1,0): x_1 - x_4 + 4 >= 0
    (C)(1,0): x_1 - 7 >= 0            (A)(1,1): x_2 - x_1 + x_4 - x_5 >= 0
    (B)(1,1): x_1 - x_2 + x_4 - 9 >= 0                                  (C)(1,1): x_1 + x_2 - x_4 - 5 >= 0
    (A)(1,2): x_3 - x_2 + x_5 - 12 >= 0                                 (B)(1,2): x_2 - x_3 - x_4 + x_5 >= 0
    (C)(1,2): x_2 + x_3 - x_5 - 5 >= 0                                  (B)(1,3): x_3 - x_5 + 3 >= 0
    (C)(1,3): x_3 - 8 >= 0            (A)(2,0): x_4 - x_6 + 3 >= 0      (C)(2,0): x_4 - x_1 - 3 >= 0
    (A)(2,1): x_5 + x_6 - x_4 - 14 >= 0                                 (B)(2,1): x_4 - x_5 + x_6 - 12 >= 0
    (C)(2,1): x_4 + x_5 - x_2 - x_6 >= 0                                (B)(2,2): x_5 - x_6 + 2 >= 0
    (C)(2,2): x_5 - x_3 - 2 >= 0      (A)(3,0): x_6 - 13 >= 0           (C)(3,0): x_6 - x_4 - 2 >= 0
    (B)(3,1): x_6 - 13 >= 0           (C)(3,1): x_6 - x_5 - 1 >= 0      (C)(4,0): 14 - x_6 >= 0

Forced coordinates. (A)(0,2) and (B)(0,3) give x_2 = x_3; (A)(0,3) and (B)(0,4) give x_3 = 9;
so x_2 = x_3 = 9. (C)(2,2) gives x_5 >= 11, (B)(1,3) gives x_5 <= 12 and (A)(1,2) gives
x_5 >= 12; so x_5 = 12. The remaining inequalities, after substituting x_2 = x_3 = 9 and
x_5 = 12 ((C)(1,2) becomes 1 >= 0 and (C)(1,3) becomes 1 >= 0), are

    7 <= x_1 <= 8                     (B)(0,1), (C)(1,0), (A)(0,1); (A)(0,0)
    x_1 + 3 <= x_4 <= x_1 + 4         (A)(1,1), (C)(2,0); (A)(1,0), (C)(1,1)
    x_1 + x_4 >= 18                   (B)(1,1)
    x_4 <= 12                         (B)(1,2)
    x_4 + 2 <= x_6 <= x_4 + 3         (A)(2,1), (C)(3,0); (A)(2,0), (C)(2,1)
    x_4 + x_6 >= 24                   (B)(2,1)
    13 <= x_6 <= 14                   (A)(3,0), (B)(3,1), (C)(3,1); (B)(2,2), (C)(4,0)

With x = x_1 - 7, y = x_4 - 11, z = x_6 - 13 these read x <= 1, x >= 0, y <= x, y >= x - 1,
y >= -x, y <= 1, y <= z, y >= z - 1, y >= -z, z <= 1, z >= 0: the same system as in Section
2, so this hive polytope is P + (7, 9, 9, 11, 12, 13) in the coordinates (x_1, x_4, x_6),
inside the affine 3-plane {x_2 = 9, x_3 = 9, x_5 = 12}. The map

    Phi(v_1, v_2, v_3, v_4, v_5, v_6) = (v_1 - 1, v_4 - 3, v_5 - 5, v_2, v_6 - 2, v_3 + 1)

is a permutation of the coordinates followed by an integral translation, hence affine
unimodular, and it carries the point (8 + x, 11 + y, 12 + z, 12, 14, 14) of the first
polytope to the point (7 + x, 9, 9, 11 + y, 12, 13 + z) of the second. So the second hive
polytope is Phi(H), and composing the pieces and maps of Sections 5 and 6 with Phi (pieces
Phi(T_i + c), maps Phi o U_i o Phi^{-1}) proves the claim for the other reading of the
convention as well.
