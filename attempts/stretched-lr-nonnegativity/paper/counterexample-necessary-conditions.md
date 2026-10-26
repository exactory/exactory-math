# Necessary conditions on a counterexample to the King-Tollu-Toumazet conjecture

Draft of 2026-09-05 (unit 2 of the attack `stretched-lr-negative-coefficient-unbounded`): a
conditional statement assembling known theorems and the box computation into the shape any
counterexample must have.

## Statement

**Proposition.** Suppose the King-Tollu-Toumazet conjecture is false: some partitions lam, mu,
nu with |lam| = |mu| + |nu| and c^{lam}_{mu nu} > 0 have a stretched Littlewood-Richardson
polynomial P(t) = c^{t lam}_{t mu, t nu} with a negative coefficient. Then some counterexample
satisfies all of the following.

- (C1) It is primitive: every essential Horn inequality of its rank holds strictly.
- (C2) c = c^{lam}_{mu nu} >= 3 and dim H(lam, mu, nu) >= 3, H the hive polytope.
- (C3) One of its partitions has at least 5 parts, and it lies outside the box of length at
  most 7 and size at most 30 (for at most 6 parts this rests on a theorem, for 7 parts on the
  computational evidence of the sibling attack).
- (C4) If its partitions have at most 5 parts, its hive polytope is full-dimensional with a
  negative linear coefficient, or has dimension 3, 4 or 5.
- (C6) It lies in the closed cone of a chamber of the Littlewood-Richardson chamber complex of
  its rank on which the polynomial giving one coefficient of P is negative at it; when it is
  interior to that chamber, an open sub-cone of the chamber consists of counterexamples, so
  counterexamples of every multiple of its size and of infinitely many sizes exist.

This is `statement` in `unit.json`, in the conditional-or-special-case form: its hypothesis is
the negation of the conjecture, and its ledger carries the obligation of that assumption (the
attack's move 1 entered the direction false as an assumption).

## Proof

The proof is `units/2/proof.md`; in outline:

- (C1) from the factorisation theorem [KTT09, CJM08]: on a saturated essential Horn inequality
  P is the product of the polynomials of two sub-triples with fewer parts, and a product of
  coefficientwise nonnegative polynomials is nonnegative, so a negative coefficient passes to a
  factor; iterate.
- (C2) from c = 1 => P = 1 [KTW04] and c = 2 => P = t + 1 [Ik16, Sh17], and from the
  reciprocity argument for dim H <= 2 (P is the Ehrhart polynomial of H by [KT99, DW02];
  Ehrhart-Macdonald reciprocity [Ma71] gives 2 a_1 t = P(t) -/+ P°(t) >= 0 and a_0 = 1 in
  dimensions 1 and 2).
- (C3) from Theorem 1 of [Fe26] (all partitions of at most 4 parts) and the sibling attack's
  box result: a theorem for at most 6 parts (every polynomial by two independent programs),
  computational evidence for 7 parts (one solver, two encodings, lrcalc at t = 1, 2; the
  non-primitive triples reduced by (C1)).
- (C4) from Theorem 3 of [Fe26] (every coefficient but the linear one of a full-dimensional
  5-part hive is positive) and (C2).
- (C6) from Rassart's piecewise polynomiality [Ra04]: on each closed chamber Delta of the
  chamber complex the coefficient is a polynomial Q_Delta, so P(t) = Q_Delta(t lam, t mu, t nu)
  and the coefficient of t^k is the degree-k homogeneous part of Q_Delta evaluated at the triple;
  a negative value at an interior point gives a negative open neighbourhood, hence by
  homogeneity a negative open sub-cone, whose integer points are counterexamples; the ray
  through the point gives counterexamples of every multiple of its size.

## What it gives

It fixes the classes in which a counterexample can be sought (the sampled classes of unit 1) and
what a sampling at large sizes tests: by (C6), chambers with a negative open sub-cone contain
counterexamples of every multiple of a size, so random triples of large size hit such a
sub-cone with probability proportional to its solid angle in the chamber. It says nothing about
whether such a chamber exists. The novelty record (`novelty.md`, unit-level queries V1-V2)
finds each ingredient in print and the conjunction with the chamber consequence nowhere.

## References

- [CJM08] S. Cho, E.-K. Jung, D. Moon, Reduction formulae from the factorization theorem of
  Littlewood-Richardson polynomials by King, Tollu and Toumazet, Discrete Math. Theor. Comput.
  Sci. Proc. (2008). doi:10.46298/dmtcs.3592
- [DW02] H. Derksen, J. Weyman, On the Littlewood-Richardson polynomials, J. Algebra 255 (2002)
  247-257. doi:10.1016/S0021-8693(02)00125-4
- [Fe26] A. Ferudun, Positivity of stretched Littlewood-Richardson coefficients for partitions
  of length at most four, arXiv:2607.22301 (2026).
- [Ik16] C. Ikenmeyer, Small Littlewood-Richardson coefficients, J. Algebraic Combin. 44 (2016)
  1-29. arXiv:1209.1521
- [KT99] A. Knutson, T. Tao, The honeycomb model of GL_n(C) tensor products I: proof of the
  saturation conjecture, J. Amer. Math. Soc. 12 (1999) 1055-1090. arXiv:math/9807160
- [KTW04] A. Knutson, T. Tao, C. Woodward, The honeycomb model of GL_n(C) tensor products II:
  puzzles determine facets of the Littlewood-Richardson cone, J. Amer. Math. Soc. 17 (2004)
  19-48. arXiv:math/0107011
- [KTT09] R. C. King, C. Tollu, F. Toumazet, Factorisation of Littlewood-Richardson
  coefficients, J. Combin. Theory Ser. A 116 (2009) 314-333. doi:10.1016/j.jcta.2008.06.005
- [Ma71] I. G. Macdonald, Polynomials associated with finite cell-complexes, J. London Math.
  Soc. (2) 4 (1971) 181-192. doi:10.1112/jlms/s2-4.1.181
- [Ra04] E. Rassart, A polynomiality property for Littlewood-Richardson coefficients, J. Combin.
  Theory Ser. A 107 (2004) 161-179. arXiv:math/0308101
- [Sh17] C. Sherman, Quiver generalization of a conjecture of King, Tollu, and Toumazet, J.
  Algebra (2017). doi:10.1016/j.jalgebra.2017.03.011 ; arXiv:1505.06551
