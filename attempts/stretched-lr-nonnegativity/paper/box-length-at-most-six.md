# Positivity of stretched Littlewood-Richardson polynomials for partitions with at most six parts and size at most 30: a certified computation

Draft of 2026-09-04 (unit 1 of the attack `stretched-lr-polynomial-negative-coefficient`).

## Abstract

For partitions lam, mu, nu with |lam| = |mu| + |nu|, the stretched Littlewood-Richardson
coefficient c^{t lam}_{t mu, t nu} is a polynomial P(t) in the stretching parameter t
(Derksen and Weyman). King, Tollu and Toumazet conjectured that every coefficient of P is
nonnegative; the conjecture is known for partitions with at most four parts (Ferudun 2026).
We prove, by an exhaustive computation in which every polynomial is computed by two programs
that share no code and every enumeration is recounted independently, that the conjecture holds
for all triples with at most six parts and |lam| <= 30: 5,552,431 polynomials of hive polytopes
of dimension 3 to 10, none with a negative coefficient. A census of every computed polynomial
(two implementations) records the structure of the near-misses: exactly 4,490 polynomials have
a coefficient below the corresponding coefficient of the unimodular simplex, all of them
polytopes with D + 1 lattice points, normalized volume 2 and h*-vector (1, 0, 1, 0, ...) in
dimensions 4 and 5, with minimal ratios 24/25 and 44/45; every other polynomial has every
coefficient at least the simplex value.

## 1. Statement

**Theorem.** Let lam, mu, nu be integer partitions with at most 6 parts each and
|lam| = |mu| + |nu| <= 30. Then every coefficient of the polynomial
P(t) = c^{t lam}_{t mu, t nu} (t = 1, 2, 3, ...) in the monomial basis 1, t, t^2, ... is
nonnegative.

Here c^{lam}_{mu nu} is the Littlewood-Richardson coefficient, the multiplicity of the Schur
function s_lam in s_mu s_nu, and t lam denotes the partition (t lam_1, t lam_2, ...). The proof
is a computation whose every ingredient is recorded in the step directories named below; the
statement is exactly `statement` in `unit.json`.

## 2. Background

King, Tollu and Toumazet [KTT04, KTT06] observed that t -> c^{t lam}_{t mu, t nu} is a
polynomial and conjectured that its coefficients are nonnegative; polynomiality was proved by
Derksen and Weyman [DW02] (see also Rassart [Ra04] and Thawinrak [Th22]). By Knutson and Tao
[KT99], c^{lam}_{mu nu} is the number of integer points of the hive polytope H(lam, mu, nu),
and since H(t lam, t mu, t nu) = t H(lam, mu, nu), P is the Ehrhart polynomial of the
rational polytope H. The conjecture is known when c = 1 (P = 1, [KTW04]), when c = 2
(P = t + 1, [Ik16, Sh17]), for every triple of partitions with at most four parts, and for
the top four coefficients of every full-dimensional hive polytope [Fe26]. No counterexample is
known; the ktt-positivity repository accompanying [Fe26] reports a search of about
4 x 10^8 triples with no negative coefficient, without recorded ranges [KP26]. The FrontierMath
open problem [Ep26] asks for a counterexample with at most 7 parts and size at most 30; the
present note settles its part with at most 6 parts in the negative, as a theorem. The novelty
record of the attack (`novelty.md`, queries of 2026-09-03 and 2026-09-04 by statement over
arXiv, Semantic Scholar, zbMATH, Crossref, MathOverflow and the problem's own page) found no
certified computation over the box or over its part with at most 6 parts in print.

## 3. Reductions

Let (lam, mu, nu) be as in the theorem, c = c^{lam}_{mu nu}, and n the largest length among
the three partitions. The following facts reduce the theorem to a finite list of canonical
triples (`units/1/proof.md`, facts F1 to F6).

1. If c = 0 then P = 0: by the saturation theorem [KT99], c^{t lam}_{t mu, t nu} > 0 forces
   c > 0, so P vanishes at every positive integer. If c = 1 then P = 1 [KTW04]; if c = 2 then
   P = t + 1 [Ik16, Sh17].
2. If c > 0 then mu and nu are contained in lam, so n = the length of lam. If n <= 4, the
   theorem is Theorem 1 of [Fe26].
3. P is symmetric in mu and nu. If lam and mu (or lam and nu) both have exactly n parts, then
   P(lam, mu, nu) = P(lam - (1^n), mu - (1^n), nu): the identity
   c^{kappa + (1^n)}_{rho + (1^n), sigma} = c^{kappa}_{rho sigma} for partitions with at most
   n parts (multiplication by the determinant representation of GL_n), applied to
   (t lam, t mu, t nu), removes t columns of height n. The new triple has the same P, at most
   6 parts, and size |lam| - n.
4. If dim H(lam, mu, nu) <= 2, every coefficient of P is nonnegative. For a point, P = 1. For
   dim H = 2, P(t) = a_2 t^2 + a_1 t + 1 with a_2 the relative area of H, and Ehrhart-Macdonald
   reciprocity [Ma71, BR15] gives P(-t) = P°(t), the number of interior points of tH, so
   2 a_1 t = P(t) - P°(t) = the number of boundary points of tH >= 0. For dim H = 1,
   P(t) = a_1 t + a_0 and P(-t) = -P°(t) give 2 a_0 = P(t) - P°(t) >= 0 and
   2 a_1 t = P(t) + P°(t) >= 0. (The constant term of P is 1: the Ehrhart quasi-polynomial of a
   rational polytope takes the value 1 at t = 0, and its constant term is constant when the
   quasi-polynomial is a polynomial [BR15].)

Call a triple canonical when mu >= nu in lexicographic order, mu and nu are contained in lam
with 1 <= |mu| <= |lam| - 1, and neither mu nor nu has n parts (this is the set the enumeration
generates; it includes the triples with c <= 2). By induction on |lam|, the theorem follows
from: every canonical triple with c >= 3, n = 5 or n = 6, |lam| <= 30 and dim H >= 3 has a
polynomial with nonnegative coefficients.

## 4. The computation

**Enumeration.** For n = 5 (`deterministic/enumeration-run-2`) and n = 6
(`deterministic/enumeration-run-3`) every canonical triple with largest length exactly n and
|lam| <= 30 was generated in a fixed order; c was computed by lrcalc (the classical
Littlewood-Richardson rule); for c >= 3 the dimension of H and, when dim H >= 3, the Ehrhart
quasi-polynomial of H were computed by Normaliz 3.11 [No] from the rhombus inequalities
(`hivepoly.py`, the hive model of [KT99] in the normalisation of [KTT06]). Every
quasi-polynomial has period 1, as [DW02] requires.

| largest length n | canonical triples | c <= 2 | c >= 3, dim H <= 2 | polynomials (dim H >= 3) | negative coefficient |
|---|---|---|---|---|---|
| 5 | 12,091,018 | 9,643,382 | 1,112,967 | 1,334,669 (dimensions 3: 700,759; 4: 452,281; 5: 168,412; 6: 13,217) | 0 |
| 6 | 31,745,644 | 25,180,759 | 2,347,123 | 4,217,762 (dimensions 3: 1,614,795; 4: 1,224,438; 5: 758,791; 6: 409,393; 7: 175,269; 8: 33,433; 9: 1,636; 10: 7) | 0 |

**Completeness.** For each run, `check.sh` recounts the canonical triples of every size
(5..30, respectively 6..30) with an independent partition generator, containment test and
canonical form that share no code with the scan, and compares with the scan's per-size totals:
0 mismatches (`enumeration-run-2/result.json`, `enumeration-run-3/result.json`, both status
pass).

**Certification of every polynomial by a second program.** A hive of side n has
(n-1)(n-2)/2 interior entries (6 for n = 5, 10 for n = 6), so deg P <= 6, respectively 10, and
P is determined by its values at t = 0, 1, ..., deg P. For every record, lrcalc computed
c^{t lam}_{t mu, t nu} for t = 1, ..., 6 (n = 5; `deterministic/certified-special-case-check-1`)
or t = 1, ..., 10 (n = 6; `deterministic/certified-special-case-check-2`); with P(0) = 1 the
values were interpolated exactly (Newton divided differences over rationals) and compared with
the Normaliz polynomial: 1,334,669 and 4,217,762 agreements, 0 mismatches. lrcalc shares no
code with Normaliz or with the hive encoder. The checkers (`result.json`, status pass) confirm
the summaries against the record counts and recount a sample (310 and 30 records) by a third
implementation, a lattice-word counter with a Lagrange interpolation.

**Result.** No polynomial has a negative coefficient. With the reductions of Section 3 this
proves the theorem.

## 5. Near-misses

The computation records where the coefficients are smallest. Write H_D = 1 + 1/2 + ... + 1/D
for the linear coefficient of the Ehrhart polynomial of the unimodular D-simplex and s_k for
its coefficient of t^k.

- A census of all 5,552,431 computed polynomials
  (`deterministic/certified-special-case-check-4`: the ratios a_k / s_k, the normalized volume
  D! a_D and the h*-vector of every polynomial, computed from the recorded coefficients in two
  implementations that agree) finds exactly 4,490 polynomials with a coefficient below the
  simplex value: 3,392 of dimension 4 (304 at 5 parts, 3,088 at 6 parts) with h*-vector
  (1, 0, 1, 0, 0), normalized volume 2 and minimal ratio 24/25 (the linear coefficient 2 against
  H_4 = 25/12), and 1,098 of dimension 5 (6 parts) with h*-vector (1, 0, 1, 0, 0, 0), volume 2
  and minimal ratio 44/45 (attained by the coefficient of t^2; the linear coefficient is 67/30
  against H_5 = 137/60, ratio 134/137). Every other computed polynomial has every coefficient at
  least the simplex value, and the minimal ratio over all computed polynomials is 24/25. These polytopes have D + 1 lattice points and the Ehrhart polynomial of an empty lattice simplex of volume 2; at 5 parts they are not simplices (each of the 304 has 7 vertices, recorded by run 2); runs 3 and 4 recorded no vertex counts, but run 1's sample (`enumeration-run-1`, field `nverts`) holds 12 of the 6-part ones (dimensions 4 and 5, with 7 and 8 vertices, so not simplices), and the rest are not known either way. An example is (5,4,3,2,1), (4,3,2,1), (2,2,1).
- From the READMEs of runs 2 and 3 (not census outputs): the minimal linear coefficient a_1 in each dimension D is the simplex value H_D for D = 3
  (both strata), for D = 5 at 5 parts (137/60) and for D = 6, 7, 8 at 6 parts (49/20, 363/140,
  761/280); it lies above H_D in dimensions 9 and 10 at 6 parts (3827/1260 and 2843/840) and in
  dimension 6 at 5 parts (157/60, the full-dimensional stratum, where only a_1 is open by
  [Fe26]); in dimension 4 (both strata) and in dimension 5 at 6 parts it is H_D - 1/(D(D-1)),
  2 and 67/30, at the polytopes above.
- No computed polynomial with D + 1 lattice points has normalized volume above 2 (the census
  counts, at 5 parts, 363,029, 124,200 and 31,111 such polynomials of volume 1 in dimensions 3,
  4, 5 and the 304 of volume 2; at 6 parts 1,073,096, 502,775, 205,857, 65,598, 16,832 and 950 of
  volume 1 in dimensions 3 to 8 and 3,088 + 1,098 of volume 2). Every polynomial with a coefficient below the simplex value has exactly D + 1 lattice points and normalized volume 2; hence the polynomials with exactly D + 2 lattice points (among the polynomials with at most D + 2 lattice points the largest normalized volume is 3 at 5 parts and 10 at 6 parts) and every polynomial of volume other than 2 have every coefficient at least the simplex value. The largest vertex denominator among the computed polynomials is 2 at 5 parts and 4 at 6 parts (READMEs of runs 2 and 3). The hive polytopes of dimension at most 2, whose polynomials were
  not computed, are outside the census.

## 6. Trusted base and reproduction

The proof rests on Normaliz 3.11 through PyNormaliz 2.24 [No], lrcalc 2.1 [Lr], Python
integers and rationals, the facts of Section 3 with their references, the encoders recorded in
the step directories (the enumeration's completeness being recounted independently), and the
checker scripts. Every polynomial rests on two programs that share no code; the classification of the canonical triples into c <= 2 (decided by lrcalc alone), c >= 3 with dim H <= 2 (by Normaliz's dimension computation alone) and computed rests on one program each, both in the trusted base. Each enumeration
directory holds its code and `input.json`, its records (`.jsonl` for run 2, `.jsonl.gz` for run 3), its logs (run 2, whose per-size totals are in `result.json`; its `README.md` gives the total and the size-30 value) or its log and summary (run 3), `README.md`, `check.sh` and the harness's `result.json`; each
certified-special-case-check directory holds the verification script (`verify5.py`,
`verify6.py`), its log and summary, `check.sh`, `README.md` and `result.json`, and reads the
records of the run it certifies. Wall times: run 2, 627 s and run 3, 1,883 s on 10 single-threaded Normaliz
workers; check 1, 101.5 s; check 2, 43,814 s on 11 workers (lrcalc enumerates tableaux; the
largest value is P(10) = 473,221,012, at a dimension-10 hive with c = 76).

## References

- [BR15] M. Beck, S. Robins, Computing the Continuous Discretely, 2nd ed., Springer, 2015.
  doi:10.1007/978-1-4939-2969-6
- [DW02] H. Derksen, J. Weyman, On the Littlewood-Richardson polynomials, J. Algebra 255 (2002)
  247-257. doi:10.1016/S0021-8693(02)00125-4
- [Ep26] Epoch AI, FrontierMath open problem "Stretched Littlewood-Richardson coefficients",
  https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients (read 2026-09-03).
- [Fe26] A. Ferudun, Positivity of stretched Littlewood-Richardson coefficients for partitions
  of length at most four, arXiv:2607.22301 (2026).
- [Ik16] C. Ikenmeyer, Small Littlewood-Richardson coefficients, J. Algebraic Combin. 44 (2016)
  1-29. arXiv:1209.1521
- [KP26] A. Ferudun, ktt-positivity, https://github.com/AlperTheKing/ktt-positivity (cloned
  2026-09-03).
- [KT99] A. Knutson, T. Tao, The honeycomb model of GL_n(C) tensor products I: proof of the
  saturation conjecture, J. Amer. Math. Soc. 12 (1999) 1055-1090. arXiv:math/9807160
- [KTW04] A. Knutson, T. Tao, C. Woodward, The honeycomb model of GL_n(C) tensor products II:
  puzzles determine facets of the Littlewood-Richardson cone, J. Amer. Math. Soc. 17 (2004)
  19-48. arXiv:math/0107011
- [KTT04] R. C. King, C. Tollu, F. Toumazet, Stretched Littlewood-Richardson and Kostka
  coefficients, CRM Proc. Lecture Notes 34 (2004) 99-112. doi:10.1090/crmp/034/10
- [KTT06] R. C. King, C. Tollu, F. Toumazet, The hive model and the polynomial nature of
  stretched Littlewood-Richardson coefficients, Sem. Lothar. Combin. 54A (2006), B54Ad.
  zbMATH 5660467; https://www.mat.univie.ac.at/~slc/wpapers/s54Akitoto1.pdf
- [Lr] A. S. Buch, lrcalc, the Littlewood-Richardson calculator, version 2.1,
  https://math.rutgers.edu/~asbuch/lrcalc
- [Ma71] I. G. Macdonald, Polynomials associated with finite cell-complexes, J. London Math.
  Soc. (2) 4 (1971) 181-192. doi:10.1112/jlms/s2-4.1.181
- [No] W. Bruns, B. Ichim, C. Soeger, U. von der Ohe, Normaliz. Algorithms for rational cones and affine monoids, version 3.11,
  https://www.normaliz.uni-osnabrueck.de/ ; PyNormaliz 2.24,
  https://github.com/Normaliz/PyNormaliz
- [Ra04] E. Rassart, A polynomiality property for Littlewood-Richardson coefficients, J. Combin.
  Theory Ser. A 107 (2004) 161-179. arXiv:math/0308101
- [Sh17] C. Sherman, Quiver generalization of a conjecture of King, Tollu, and Toumazet, J.
  Algebra (2017). doi:10.1016/j.jalgebra.2017.03.011 ; arXiv:1505.06551
- [Th22] W. Thawinrak, A short proof for the polynomiality of the stretched Littlewood-Richardson
  coefficients, arXiv:2211.06810 (2022).
