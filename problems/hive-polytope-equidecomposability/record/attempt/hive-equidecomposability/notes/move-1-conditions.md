# Move 1: necessary conditions on a hypothetical counterexample

Entry: extract-structure-from-a-hypothetical-counterexample (strategy attack-the-negative-side).
Assume a triple (lambda, mu, nu) with at most n parts, c^nu_{lambda mu} > 0, whose hive polytope
H = H(lambda, mu, nu) is not GL_D(Z)-equidecomposable with any lattice polytope, and take it
minimal (smallest n, then smallest |nu|). The following conditions hold.

C1 (rank). n >= 4, proved: for n <= 3 the hive polytope has D <= 1 and is a lattice polytope by
C2 below, and a lattice polytope is equidecomposable with itself (one piece per relatively open
simplex of a triangulation, every map the identity). n >= 5, reported: for n = 4 Buch 2000 states
after Example 2, without a printed proof, that all corners of the hive polytope are integral
(`known` of problem.json); this record uses that remark on Buch's authority and labels every
consequence of it as reported.

C2 (dimension). dim H >= 2. If dim H = 0, H is one integral hive (c > 0 and the saturation
theorem give an integral point; a point is a lattice polytope). If dim H = 1, H is a rational
segment on a rational line L in R^D containing a lattice point (c > 0); in the affine lattice
L n Z^D the segment is [a, b] with a, b rational and its dilates have lattice-point counts
L(t) = floor(tb) - ceil(ta) + 1 = (b - a)t + 1 - {tb} - {-ta}; since L(t) is a polynomial in t
(period collapse, Derksen-Weyman, Rassart), the function t -> {tb} + {-ta} is a polynomial on the
positive integers, and it vanishes at every multiple of the common denominator, so it vanishes
identically: a and b are lattice points and H is a lattice segment, equidecomposable with itself.

C3 (vertices). H has a non-integral vertex: otherwise H is a lattice polytope. By Buch 2000,
Example 2, such hives exist from five parts on, and by the saturation theorem (Knutson-Tao; Buch
2000, Theorem 2) H also has an integral vertex, so H has both integral and non-integral vertices.

C4 (the two types). Either (i) the Ehrhart polynomial L_H(t) = c^{t nu}_{t lambda, t mu} is not the
Ehrhart polynomial of any lattice polytope of dimension dim H, or (ii) it is, say L_H = L_Q for a
lattice polytope Q, and H is not finitely unimodularly equidecomposable with Q nor with any other
lattice polytope with that polynomial. In case (i), H is also a counterexample to the Ehrhart form
N1 and the invariant that certifies it is a function of the polynomial alone: in dimension 2,
Scott's inequality and b >= 3 decide realizability, so a two-dimensional counterexample of type
(i) has b <= 2 or violates Scott; in dimension at least 3 only necessary conditions are known
(nonnegativity of h*, the interior bound, Hibi's lower bound, Stanley's inequality, Hibi 1990,
the universal inequalities when h*_3 = 0, the f*-vector inequalities), so a type-(i) counterexample
of dimension at least 3 either violates one of them or lies outside what the known conditions
detect. In case (ii) the certificate must be an invariant of finite unimodular equidecomposability
finer than the Ehrhart polynomial; in dimension 2 the only one in print is the Turner-Wu edge
weighting on minimal triangulations of a fixed denominator, and in dimension at least 3 none is
known (Haase-McAllister, Problem 4.5), so a type-(ii) counterexample of dimension at least 3 is
one that no method in print can certify.

C5 (size at five parts; computed, not proved). Every five-part hive polytope with |nu| <= 14 is a
lattice polytope, and exactly five triples of size 15 have a non-integral vertex, all with
denominator 2 and dim H in {3, 4} (exploratory scan `studies/scripts/instance_check.py`; no native
credit). So a minimal counterexample with n = 5 has |nu| >= 15, and the five size-15 triples are
the first candidates to test.

C6 (what the computed ranges exclude; exploratory). No type-(i) counterexample of five, six or
seven parts and size at most 30 violates the five tested h*-inequalities (probe
hstar-inequalities-1, 6,855,302 polynomials), and no two-dimensional hive polytope of at most five
parts and size at most 22 is of type (i) (probe dim2-hives-1, Scott and b >= 3). These are
exploratory censuses, not admitted evidence; they bound where a type-(i) counterexample could be
found by the known tests.

C7 (primitivity under the operations that carry decompositions). If H is minimal, then H is not
an integral translate of a hive polytope of a smaller triple (adding a common integer to every
part of two of the partitions translates H by an integral vector; move 3 proves this), and if the
Horn-product lemma of move 3 holds, no essential Horn inequality of (lambda, mu, nu) is tight under
the multiplicity-one subset condition (a product of polytopes each equidecomposable with a lattice
polytope is equidecomposable with the product of the lattice polytopes).

What the conditions leave. They leave no finite range and no contradiction: the residual class is
the union of the type-(i) class outside the computed ranges and the type-(ii) class in every
dimension at least 2, both infinite. The smallest objects passing C1 to C5 are the five size-15
five-part triples; the first of them is the seed of the constructive strategy (moves 3 and 4),
which decides whether it is a near miss rather than a counterexample.
