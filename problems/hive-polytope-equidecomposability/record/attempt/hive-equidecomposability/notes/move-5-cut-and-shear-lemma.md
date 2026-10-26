# Move 5: the general cut-and-shear lemma and the limits of the seed class

Entry: seed-and-amplify, action 5 (strategy make-the-proof-constructive): optimise the seed
and test the limits of the seed class. The seed proof (proofs/smallest-instance.md) used one
cut along a lattice hyperplane through the half-integral vertex and one shear fixing that
hyperplane. This note proves that mechanism in general (Lemma CS) and records, as
exploratory candidates, its application to the other four size-15 five-part hive polytopes
with a non-integral vertex found by the record's scan.

## 1. Lemma CS (cut and shear)

Let P be a rational polytope in R^k with vertex set V. Let l : Z^k -> Z be a primitive
integral linear form (its coefficients have gcd 1), let c be an integer, and write
Pi = {l = c}. Suppose:

(i) exactly one vertex a of P satisfies l(a) > c, and l(a) = c + 1, and a is a lattice point;
(ii) the vertices with l < c are lattice points b_1, ..., b_m (m >= 1) with l(b_i) = c - 1;
(iii) every other vertex lies on Pi, and among them exactly one, w, is not a lattice point,
and 2w is a lattice point;
(iv) with d := a + b_1 - 2w (a lattice vector by (iii)), every midpoint
m_i := (a + b_i - d)/2 = w + (b_i - b_1)/2 (1 <= i <= m) lies in K := P n Pi.

Then, with U(x) := x + (l(x) - c) d, the set Q := (P n {l >= c}) u U(P n {l < c}) is the
lattice polytope conv(K_Z u {a, b_1 - d, ..., b_m - d}), where K_Z is the set of lattice
vertices of K, the two pieces are disjoint, and P has property E (it is GL_k(Z)-
equidecomposable with Q). The lemma also holds with the roles of the two sides exchanged.

Proof. (1) U is affine unimodular and fixes Pi pointwise. Its linear part is I + d l^T (with
l also denoting the row vector of coefficients), an integral matrix of determinant
1 + l(d) = 1 + l(a) + l(b_1) - 2 l(w) = 1 + (c + 1) + (c - 1) - 2c = 1, so it lies in GL_k(Z);
the translation part -c d is integral; U(x) = x for l(x) = c; and l(U(x)) = l(x) + (l(x) - c)
l(d) = l(x), so U preserves l.

(2) The two pieces of P are pyramids over K. Let P_+ = P n {l >= c} and P_- = P n {l <= c}.
Claim: P_+ = conv(K u {a}) and P_- = conv(K u {b_1, ..., b_m}). The inclusions from right to
left are clear. Conversely let p in P_+. Write p as a convex combination of vertices,
p = alpha a + (1 - alpha) q with q a convex combination of the vertices other than a, so
l(q) <= c. If alpha = 1 then p = a. If l(q) = c then q in P n Pi = K and p in conv(K u {a}). If
l(q) < c, the segment [q, a] meets Pi at a point q' = (1 - s) q + s a with
s = (c - l(q))/(l(a) - l(q)) in (0, 1), and q' in P n Pi = K; since l(p) >= c the point p lies
on the subsegment [q', a], so p in conv(K u {a}). The argument for P_- is the same with the
b_i in place of a (p = sum beta_i b_i + (1 - sum beta_i) q with l(q) >= c; if l(q) > c the
segment from q to the point r = (sum beta_i b_i)/(sum beta_i) meets Pi inside P, hence in K,
and p lies between that crossing point and r, where r in conv{b_i}).

(3) Q = P_+ u U(P_- \ K) is convex, and equals conv(K u {a} u {b_i - d}). Put b_i' = U(b_i)
= b_i + (c - 1 - c) d = b_i - d, so U(P_-) = conv(K u {b_i'}) by (2) and (1). Let
p = alpha a + sum_i beta_i b_i' + gamma q with q in K and alpha + sum beta_i + gamma = 1 (a
point of the convex hull). Set beta = sum beta_i. If alpha >= beta, write p = sum_i beta_i
(a + b_i') + (alpha - beta) a + gamma q = sum_i 2 beta_i m_i + (alpha - beta) a + gamma q,
where m_i = (a + b_i')/2 lies in K by (iv); so p in conv(K u {a}) = P_+. If beta >= alpha,
write alpha a = sum_i alpha_i a with alpha_i = alpha beta_i / beta, and p = sum_i 2 alpha_i
m_i + sum_i (beta_i - alpha_i) b_i' + gamma q, a convex combination of points of
K u {b_i'}; so p in U(P_-). Hence conv(K u {a} u {b_i'}) is contained in P_+ u U(P_-), and the
reverse inclusion is clear; the union with U(P_- \ K) instead of U(P_-) is the same set
because U fixes K. The pieces P_+ and U(P_- \ K) are disjoint because U preserves l: the
first lies in {l >= c} and the second in {l < c}.

(4) Q is a lattice polytope. Its vertices are among K's vertices, a and the b_i'. The point w
is not a vertex of Q: w = (a + b_1')/2 is the midpoint of two other points of Q. Every other
vertex of K is a lattice point by (iii), and a, b_i' are lattice points. So all vertices of Q
are lattice points.

(5) The decomposition. Triangulate P by a triangulation with rational vertices refining Pi
(triangulate K first, then cone its simplices from a and from each b_i, which triangulates
the two pyramids compatibly with K; the pyramid over K with several apexes b_i is
triangulated by first triangulating conv(K u {b_i}) with the vertices of K and the b_i, which
can be done with the cut K as a subcomplex). The relatively open faces of all dimensions,
each counted once, partition P; assign the identity to the faces in P_+ (including those in
K) and U to the faces in P_- \ K. The images are disjoint by (3) and cover Q. This proves the
lemma.

Remarks. (a) The seed is the case k = 3, l = x - z, c = 0, a = (1,0,0), m = 1, b_1 = (0,0,1),
w = (1/2,-1/2,1/2), d = (0,1,0). (b) The lemma straightens one half-integral vertex; if K has
two, one of them survives as a vertex of Q, and a second application of the lemma to Q may
remove it (this happens for one of the candidates below). (c) The hypothesis l(a) = c + 1 and
l(b_i) = c - 1 (lattice distance one on each side) is what makes d integral and the midpoints
lie on Pi; the lemma says nothing when a vertex lies at lattice distance 2 or more, or when
the non-lattice vertex has denominator 3 or more.

## 2. The seed class: the other four size-15 candidates (exploratory, no credit)

The record's exploratory scan found five five-part triples of size 15 whose hive polytope
has a non-integral vertex (studies/scripts/instance_check.out.txt); the first is the seed.
The script ../checks/cut_shear_apply.py (output cut_shear_apply.out.txt) computes, for each
of the five, the vertices in the free coordinates of the affine hull (the equations fix
coordinates or have unimodular form), searches the configurations of Lemma CS, applies the
shear and reports the vertices of the union. Everything in this section is the output of
that computation, read as candidate data; none of it is proved here, and in particular the
identification of each polytope from its rhombus inequalities (the step that the seed proof
does by hand) is not done for these four. In hivepoly's notation the triples are
(lam; mu, nu) with lam = (5,4,3,2,1) the large partition (the statement's nu).

Candidate 2: mu = (2,2,1), nu = (4,3,2,1). Free coordinates (x_2, x_4, x_5, x_6)
(x_1 = 7, x_3 = 9 fixed), dim 4, seven vertices, two of them half-integral:
w_1 = (17/2, 21/2, 12, 27/2) and w_2 = (17/2, 11, 23/2, 27/2). Step 1: l = x_6 - x_2 - 5,
a = (8, 11, 12, 14) (l = 1), b_1 = (9, 11, 12, 13) (l = -1), all other vertices on l = 0,
w = w_1, d = a + b_1 - 2w_1 = (0, 1, 0, 0); the union has the single non-lattice vertex w_2.
Step 2 on the union: a = (8, 10, 11, 13), b_1 = (8, 11, 12, 13), l = x_6 - x_4 - x_5 + 10
(l(a) = 1 ... as computed: normal (0, -1, -1, 1)), d = (-1, -1, 0, -1); the union is the
lattice polytope with vertices (8,10,11,13), (8,11,12,14), (9,10,12,13), (9,11,12,14),
(9,12,12,14). Two cuts and two shears.

Candidate 3: mu = (3,2,1), nu = (4,2,2,1). Free coordinates (x_1, x_2, x_4, x_6)
(x_3 = 10, x_5 = 12 fixed), dim 4, seven vertices, one half-integral
w = (15/2, 9, 21/2, 27/2). No configuration with m = 1 exists; with m = 2: a = (7, 9, 11, 13),
b_1 = (8, 9, 11, 14), b_2 = (8, 10, 12, 14), l = -x_1 - x_6 + 21 (normal (-1, 0, 0, -1)),
d = (0, 0, 1, 0); both midpoints lie in K and the union is a lattice polytope. One cut, one
shear with two far vertices.

Candidate 4: mu = (3,2,1), nu = (3,3,2,1). Free coordinates (x_1, x_2, x_4, x_6)
(x_5 = x_2 + 3, x_3 = 9), dim 4, seven vertices, one half-integral w = (15/2, 9, 21/2, 27/2).
Configuration with m = 1: a = (8, 9, 11, 13), b_1 = (7, 9, 11, 14), l = x_1 - x_6 + 6,
d = (0, 0, 1, 0); the union is a lattice polytope. One cut, one shear.

Candidate 5: mu = (3,2,1,1), nu = (3,2,2,1). Free coordinates (x_1, x_4, x_5, x_6)
(x_2 = x_5 - 3, x_3 = x_5 - 2), dim 4, six vertices, one half-integral
w = (15/2, 21/2, 12, 27/2). Configuration with m = 1: a = (8, 11, 12, 13),
b_1 = (7, 11, 12, 14), l = x_1 - x_6 + 6, d = (0, 1, 0, 0); the union is a lattice polytope.
One cut, one shear.

Reading of the evidence. Within the exploratory scan, every non-lattice five-part hive
polytope of size 15 is reached by Lemma CS in at most two steps, with every cutting form of
the shape x_i - x_j + const (the difference of two interior labels at lattice distance one
across the half-integral vertex) and every shear vector a unit vector. This is the seed
class as far as the record sees it: hive polytopes whose non-integral vertices are
half-integral and are straightened one at a time by unit shears along a lattice hyperplane
through them. The limits of the class that the record cannot see: hive polytopes with
vertices of denominator 3 or more (they exist in the census, denominators up to 6 at size
at most 30), where Lemma CS does not apply as stated; and configurations where no lattice
hyperplane through the non-integral vertex isolates lattice vertices at distance one. The
first open instance beyond the seed class, in the sense of the attack, is therefore the
first hive polytope (by size, at five parts) with a vertex of denominator 3; the record does
not know which triple that is.

## 3. What the move produced

Proved: Lemma CS, by hand, in Section 1. Candidates (exploratory, no credit): the four
applications of Section 2, which would, once each polytope is identified from its rhombus
inequalities by hand, give four more instances of the root statement at five parts.
Obligation unchanged: the Horn-product lemma of move 3; the amplification by Lemma CS is not
an operation on triples but on polytopes with a half-integral vertex, so it does not reduce
the root statement to finitely many cases.
