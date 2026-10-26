# Unit 2: necessary conditions on a counterexample to the King-Tollu-Toumazet conjecture

## Statement

Suppose the conjecture is false: some partitions lam, mu, nu with |lam| = |mu| + |nu| and
c = c^{lam}_{mu nu} > 0 have a stretched Littlewood-Richardson polynomial
P(t) = c^{t lam}_{t mu, t nu} with a negative coefficient. Then some counterexample satisfies:

- (C1) it is primitive: every essential Horn inequality of its rank is strict;
- (C2) c >= 3 and dim H(lam, mu, nu) >= 3;
- (C3) one of its partitions has at least 5 parts, and it lies outside the box of length at most
  7 and size at most 30 (for at most 6 parts by a theorem, for 7 parts by the box attack's
  evidence);
- (C4) if its partitions have at most 5 parts, its hive polytope is full-dimensional with a
  negative linear coefficient, or has dimension 3, 4 or 5;
- (C6) it lies in the closed cone of a chamber of the Littlewood-Richardson chamber complex of
  its rank on which the polynomial giving one coefficient of P is negative at it; when it is
  interior to that chamber, an open sub-cone of the chamber consists of counterexamples, so
  counterexamples of every multiple of its size and of infinitely many sizes exist.

(C5 of the journal, the h*-expansion of the linear coefficient, is a heuristic, not a condition,
and is not part of the statement.)

## Proof

Let (lam, mu, nu) be a counterexample with a negative coefficient.

(C1) By the factorisation theorem of King, Tollu and Toumazet (J. Combin. Theory Ser. A 116
(2009), doi:10.1016/j.jcta.2008.06.005; Cho, Jung and Moon, DMTCS 2008, doi:10.46298/dmtcs.3592,
Theorem 1.3), if an essential Horn inequality (I, J, K) holds with equality for (lam, mu, nu),
then P = P_1 P_2 where P_1, P_2 are the stretched polynomials of the two sub-triples indexed by
(I, J, K) and their complements. A product of two polynomials with nonnegative coefficients has
nonnegative coefficients, so at least one factor has a negative coefficient: a counterexample
with fewer parts. Repeating, a primitive counterexample exists.

(C2) c = 1 gives P = 1 (Knutson, Tao, Woodward 2004, arXiv:math/0107011) and c = 2 gives
P = t + 1 (Ikenmeyer 2016, arXiv:1209.1521; Sherman 2017, doi:10.1016/j.jalgebra.2017.03.011),
so c >= 3. P is the Ehrhart polynomial of the hive polytope H (Knutson and Tao 1999,
arXiv:math/9807160; Derksen and Weyman 2002, doi:10.1016/S0021-8693(02)00125-4), and for
dim H <= 2 its coefficients are nonnegative (a point; for dimension 1 or 2, Ehrhart-Macdonald
reciprocity for rational polytopes, Macdonald 1971, doi:10.1112/jlms/s2-4.1.181, gives
2 a_1 t = P(t) -/+ P°(t) >= 0 and a_0 = 1, as in the box attack's unit 1), so dim H >= 3.

(C3) Every triple with all partitions of at most 4 parts has nonnegative coefficients (Ferudun
2026, arXiv:2607.22301, Theorem 1). Within the box (length <= 7, size <= 30) no triple has a
negative coefficient: for at most 6 parts this is the theorem of the sibling attack
(`../stretched-lr-polynomial-negative-coefficient/units/1`), for 7 parts the computational
evidence of its unit 2 (every primitive 7-part polynomial computed by Normaliz from two
encodings and matched by lrcalc at t = 1, 2; every non-primitive one a product by (C1)). So the
counterexample has a partition of at least 5 parts and lies outside the box, with the 7-part
part of that exclusion resting on the evidence.

(C4) For partitions with at most 5 parts, a full-dimensional hive polytope has every coefficient
but the linear one positive (Ferudun 2026, Theorem 3), so a negative coefficient of a
full-dimensional 5-part hive is the linear one; otherwise dim H <= 5, and dim H >= 3 by (C2).

(C6) By Rassart (J. Combin. Theory Ser. A 107 (2004), arXiv:math/0308101), for each rank the
Littlewood-Richardson coefficient is a piecewise polynomial function of (lam, mu, nu): there is
a chamber complex (a fan of closed cones) such that on each closed chamber Delta the coefficient
is given by a polynomial Q_Delta. Since t(lam, mu, nu) stays in Delta for t >= 1,
P(t) = Q_Delta(t lam, t mu, t nu) = sum_k t^k Q_{Delta,k}(lam, mu, nu) with Q_{Delta,k} the
degree-k homogeneous part of Q_Delta; so the coefficient a_k of P equals Q_{Delta,k} at the
counterexample, and a negative a_k means Q_{Delta,k} < 0 there, for a chamber Delta whose closed
cone contains the point. If the point is interior to Delta, Q_{Delta,k} is negative on an open
neighbourhood of it inside Delta, and by homogeneity on the open sub-cone it spans; every
integer point of that sub-cone is a counterexample (its a_k is the same polynomial's value),
and the sub-cone contains the ray through the point, hence counterexamples of every multiple of
the original size, and (being open in the span of the chamber) integer points of infinitely many
sizes.

## What the statement gives and what it owes

It reduces the negation of the conjecture to the structured classes searched in unit 1
(primitive hives of at least 5 parts outside the box, at 5 parts full-dimensional or of
dimension 3..5, and the chambers reached by sampling at large sizes). It owes nothing beyond
the cited theorems except the 7-part part of (C3), which rests on the box attack's evidence
rather than a two-program proof; without it (C3) reads "outside the box of length at most 6".
