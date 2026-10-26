# No negative coefficient in a stretched Littlewood-Richardson polynomial with at most seven parts and size at most 30

Draft of 2026-09-04 (unit 2 of the attack `stretched-lr-polynomial-negative-coefficient`): a
computational answer to the FrontierMath open problem "Stretched Littlewood-Richardson
coefficients", with the state of the search and the open questions it leaves.

## Abstract

For partitions lam, mu, nu with |lam| = |mu| + |nu| the stretched Littlewood-Richardson
coefficient c^{t lam}_{t mu, t nu} is a polynomial P(t) in t, conjectured by King, Tollu and
Toumazet to have nonnegative coefficients. The FrontierMath open problem [Ep26] asks for a
counterexample with partitions of length at most 7 and size at most 30. We report that none
exists: the 6,855,302 polynomials computed (every canonical triple of largest length 5 or 6
with dim H >= 3, and every primitive one of largest length 7) have nonnegative coefficients,
and every other triple of the box reduces to these by theorems. For at most 6 parts this is a
theorem proved by computation
(every polynomial computed by two independent programs, unit 1); for 7 parts it is
computational evidence, every polynomial being computed by Normaliz from two different
polytope encodings and matched by lrcalc at t = 1 and 2, with the non-primitive triples
reduced to fewer parts by the King-Tollu-Toumazet factorisation theorem. A census of the
computed polynomials (two implementations) finds that exactly 7,469 of them have a coefficient
below the corresponding coefficient of the unimodular simplex, all of them polytopes with D + 1
lattice points, normalized volume 2 and h*-vector (1, 0, 1, 0, ...) in dimensions 4, 5 and 6,
with minimal ratios 24/25, 44/45 and 799/812; no computed polynomial comes closer to a negative
coefficient. We record what a
counterexample must look like, where the search now stands beyond the box (six families of
transportation polytopes with small margins, all Ehrhart positive), and what would turn the
7-part evidence into a proof.

## 1. The problem and the answer

**Problem [Ep26].** Find integer partitions lam, mu, nu, each of length at most 7 and size at
most 30, such that c^{t lam}_{t mu, t nu}, as a polynomial in t, has at least one negative
coefficient.

**Answer.** There are no such partitions: a theorem for at most 6 parts and computational
evidence for 7 parts. Precisely (`statement` in `unit.json`): no integer
partitions lam, mu, nu of length at most 7 and size at most 30 with |lam| = |mu| + |nu| have
a stretched Littlewood-Richardson polynomial with a negative coefficient. For partitions with
at most 6 parts this is a theorem (unit 1, `units/1/draft.md`); for triples with a partition
of 7 parts it rests on the computation of Section 4 with the certification of Section 5. (When
|lam| differs from |mu| + |nu| the coefficient is 0 for every t and the polynomial is 0.)

## 2. Background

King, Tollu and Toumazet [KTT04, KTT06] conjectured the positivity; polynomiality is due to
Derksen and Weyman [DW02] (also [Ra04, Th22]). By Knutson and Tao [KT99],
c^{lam}_{mu nu} counts the integer points of the hive polytope H = H(lam, mu, nu), a rational
polytope in R^D with D <= (n-1)(n-2)/2 for n parts, cut out by rhombus inequalities with 0/+-1
normals; H(t lam, t mu, t nu) = t H, so P is the Ehrhart polynomial of H. Known cases: c = 1
(P = 1, [KTW04]); c = 2 (P = t + 1, [Ik16, Sh17]); every triple with at most 4 parts, and the
top four coefficients of every full-dimensional hive polytope, with every coefficient but the
linear one for full-dimensional 5-part hives [Fe26]. De Loera and McAllister computed stretched
Littlewood-Richardson polynomials with LattE at small rank and found none negative [DM06];
[Fe26] reports extensive computation without a counterexample and its repository a search of
about 4 x 10^8 triples [KP26], both without recorded ranges. General lattice polytopes are not
Ehrhart positive (Reeve tetrahedra; [CLNT18]; order polytopes from dimension 14, [LT19,
LXZ26]), which is why the conjecture is expected by some, including the problem's author
[Ep26], to be false. On a saturated essential Horn inequality the polynomial factorises,
P = P_1 P_2, into the polynomials of two triples with fewer parts [KTT09, CJM08]. The novelty
record of the attack (`novelty.md`, queries of 2026-09-03 and 2026-09-04 by statement, over
arXiv, Semantic Scholar, zbMATH, Crossref, MathOverflow and the problem's own page) found no
computation over the box and no negative coefficient in print.

## 3. Method

**Reductions.** Section 3 of unit 1: c <= 2 and dim H <= 2 give nonnegative polynomials
(theorems and Ehrhart reciprocity [Ma71, BR15]); mu and nu may be swapped; a column of full
height may be removed from lam and from mu or nu; triples with at most 4 parts are [Fe26].
What remains are the canonical triples (mu >= nu lexicographically, mu and nu contained in lam with 1 <= |mu| <= |lam| - 1, neither with n parts; the set the enumeration generates, which includes the triples with c <= 2) of largest length n = 5, 6, 7 that have c >= 3 and dim H >= 3.

**Enumeration.** For each n every canonical triple with |lam| <= 30 was generated in a fixed
order (`deterministic/enumeration-run-2`, `-3`, `-4`): c by lrcalc; for c >= 3 the dimension
and the Ehrhart quasi-polynomial of H by Normaliz 3.11 [No] from the rhombus inequalities
(`hivepoly.py`). At n = 7 a triple that saturates one of the 2042 essential Horn inequalities
of GL_7 (computed by the criterion of [KTW04], c^{sigma_K}_{sigma_I sigma_J} = 1, and stored in
`horn-essential-7.json`) was not sent to Normaliz: by [KTT09] its polynomial is the product of
the polynomials of two triples with at most 6 parts and size at most 30, both nonnegative by
unit 1. The factorisation identity was verified against Normaliz on 150 saturated 6-part
triples before the run and on 120 sampled skipped 7-part triples during it, and the run's
checker re-verifies the saturation, the factor triples and c = c_1 c_2 on the 93,567 recorded
skipped triples.

**Completeness.** Each run's checker recounts the canonical triples per size with an
independent generator: every size 5..30 for n = 5, every size 6..30 for n = 6, and every size
7..30 for n = 7 (`result.json` of each run, status pass).

**Certification.** n = 5 and 6: every polynomial pinned by lrcalc counts at t = 0..deg P and
exact interpolation (unit 1). n = 7: `deterministic/certified-special-case-check-3` recomputed
every one of the 1,302,871 polynomials from a second encoding, the tableau polytope
(`tableau_polytope.py`: the column-strictness and lattice-word inequalities on the
multiplicity matrix of a Littlewood-Richardson tableau, no hive entry, no code shared with the
hive encoder) with Normaliz, and lrcalc recomputed c^{lam}_{mu nu} and
c^{2 lam}_{2 mu, 2 nu} for every record: 1,302,871 agreements on each count, 0 mismatches.

## 4. Results

| n | canonical triples | c >= 3 | reduced by factorisation | polynomials (dim H >= 3) | dimensions | vertex denominators | negative |
|---|---|---|---|---|---|---|---|
| 5 | 12,091,018 | 2,447,636 | 0 | 1,334,669 | 3..6 | <= 2 | 0 |
| 6 | 31,745,644 | 6,564,885 | 0 | 4,217,762 | 3..10 | <= 4 | 0 |
| 7 | 52,834,374 | 10,516,904 | 9,201,781 | 1,302,871 | 3..13 | <= 7 | 0 |

At 7 parts the 1,315,123 primitive triples with c >= 3 split into 12,252 with dim H <= 2 and
1,302,871 with dim H >= 3, distributed over dimensions 3 to 13 as 37,726; 95,556; 187,745;
273,415; 317,104; 239,177; 115,385; 32,360; 4,195; 206; 2. Every quasi-polynomial in the box
has period 1. Wall times: 627 s, 1,883 s and 9,625 s on 10 to 11 single-threaded Normaliz
workers; the 7-part second-encoding check took 6,667 s on 8 workers.

## 5. What is proved and what is evidence

- At most 6 parts: a theorem. Every polynomial was computed by two programs that share no code
  (Normaliz on the hive inequalities; lrcalc by the classical rule with exact interpolation),
  and every enumeration was recounted independently for every size (unit 1).
- Exactly 7 parts: evidence. Pinning a 7-part polynomial by lattice-word counts needs values up
  to t = 15, astronomically many tableaux for the fat hives (P(10) already exceeds 4 x 10^8 at 6
  parts), and no second Ehrhart solver (LattE, barvinok) was available. The two encodings are
  independent, but both are solved by Normaliz, so a defect of its Ehrhart-series computation
  that affected both identically at t >= 3 would not show; lrcalc guards t = 1 and t = 2 only.
  Either a second solver on the 1,302,871 records or a pinning of them would close this gap, relative to the trusted base, in which the Horn filter of the enumeration code sits (its skip rule is re-verified on a 1-in-100 sample).
- The trusted base of the whole: Normaliz 3.11 through PyNormaliz 2.24 [No], lrcalc 2.1 [Lr],
  Python integers and rationals, the theorems cited in Sections 2 and 3, the encoders and
  checkers recorded in the step directories.

## 6. Where the coefficients come closest to zero

Write H_D = 1 + 1/2 + ... + 1/D for the linear coefficient of the Ehrhart polynomial of the
unimodular D-simplex and s_k for its coefficient of t^k. The first and third facts below are recorded by a census of all 6,855,302 computed polynomials (`deterministic/certified-special-case-check-4`: the ratios a_k / s_k, the normalized volume D! a_D and the h*-vector of every polynomial, computed from the recorded coefficients in two implementations that agree); the second and the fourth come from the READMEs of runs 2, 3 and 4 and of the sample run 1:

- Exactly 7,469 computed polynomials have a coefficient below the simplex value: 3,543 of
  dimension 4 (304, 3,088 and 151 at 5, 6 and 7 parts) with h*-vector (1, 0, 1, 0, 0),
  normalized volume 2 and minimal ratio 24/25 (the linear coefficient 2 against H_4 = 25/12);
  2,730 of dimension 5 (1,098 and 1,632 at 6 and 7 parts) with h*-vector (1, 0, 1, 0, 0, 0),
  volume 2 and minimal ratio 44/45 (at the coefficient of t^2; the linear coefficient is 67/30,
  ratio 134/137); and 1,196 of dimension 6 (7 parts) with h*-vector (1, 0, 1, 0, 0, 0, 0),
  volume 2 and minimal ratio 799/812 (the linear coefficient is 29/12, ratio 145/147). Every
  other computed polynomial has every coefficient at least the simplex value; the minimal ratio
  over all computed polynomials is 24/25. These polytopes have D + 1 lattice points and the Ehrhart polynomial of an empty lattice simplex of volume 2; at 5 parts they are not simplices (each of the 304 has 7 vertices, recorded by run 2); runs 3 and 4 recorded no vertex counts, but run 1's sample (`enumeration-run-1`, field `nverts`) holds 12 six-part and 28 seven-part ones (dimensions 4 and 5, with 7 and 8 vertices, so not simplices), and the rest, including every dimension-6 one, are not known either way. An example is
  (5,4,3,2,1), (4,3,2,1), (2,2,1).
- The minimal linear coefficient in each (n, D) stratum is H_D, except at the polytopes above
  (H_D - 1/(D(D-1)): 2, 67/30, 29/12 in dimensions 4, 5, 6) and in the strata where it lies
  above H_D: dimensions 9 and 10 at 6 parts, 12 and 13 at 7 parts, and 6 at 5 parts (157/60,
  the full-dimensional stratum, where only the linear coefficient is open by [Fe26]).
- No computed polynomial with D + 1 lattice points (h*_1 = 0) has normalized volume above 2;
  every polynomial with a coefficient below the simplex value has exactly D + 1 lattice points and volume 2, so the polynomials with exactly D + 2 lattice points (among those with at most D + 2 lattice points the largest normalized volume is 3 at 5 parts and 10 at 6 and 7 parts) and every polynomial of volume other than 2 have every coefficient at least the simplex value. In the
  h*-expansion a_1 = H_D + sum_{i >= 1} (-1)^{i-1} h*_i / (i binom(D, i)), a negative linear
  coefficient by the few-point mechanism alone, with the h*-mass v - 1 at index 2
  (h* = (1, 0, v - 1, 0, ...), the pattern of the volume-2 examples), needs normalized volume v
  above 1 + H_D D(D-1): v >= 27 in dimension 4, 47 in dimension 5, 75 in dimension 6 (mass at
  a higher even index needs more; 148, the number an earlier version of the record gave for
  dimension 6, is the index-4 threshold 1 + H_6 4 binom(6, 4)).
- The largest vertex denominator among the computed polynomials is 2 at 5 parts, 4 at 6 parts and 7 at 7 parts. In the
  stratified sample of 9,477 polynomials of `deterministic/enumeration-run-1` (move 2 of the
  attack) the mean linear coefficient rises with the denominator (2.27, 2.87, 3.43, 3.84 for
  denominators 1 to 4) and no h*-vector has a negative entry.
- Outside the census: the hive polytopes of dimension at most 2 (their polynomials were never
  computed; their coefficients are nonnegative by reciprocity) and the products of the
  non-primitive 7-part triples.

## 7. Beyond the box

- By Rassart's piecewise polynomiality [Ra04] each coefficient is a polynomial in (lam, mu, nu)
  on the chambers of the Littlewood-Richardson chamber complex, so a negative coefficient on
  an open sub-cone of a chamber would give counterexamples of every size in that sub-cone;
  sampling at sizes far above the box tests chambers the box cannot reach.
- 3 x N transportation polytopes are Littlewood-Richardson polytopes under the strip construction of [Fe26] (stated there for three strips; the k x N case for k >= 4 is not in print, so the 4 x 4, 4 x 5 and 5 x 5 families below are neighbouring polytopes, not established images) (the 3 x 8 example with row margins (3,3,3) and column margins (2,1^7) is, in the
  convention of [Fe26] where nu is the outer partition, the triple lam = (9,6,3),
  mu = (9,9,7,6,5,4,3,2,1), nu = (15,12,9,7,6,5,4,3,2,1), that is c^{nu}_{lam mu} with
  |nu| = 64 = 18 + 46 and an outer partition of 10 parts), so a negative transportation
  polytope would refute the conjecture. The families 3 x 4, 3 x 5, 3 x 6, 4 x 4, 4 x 5 and
  5 x 5 with small margins (5,170 polytopes, dimension up to 16, sibling attack
  `attack/stretched-lr-negative-coefficient-unbounded`, `counterexample-search-run-2`,
  `result.json` status pass) are Ehrhart positive, with the minimal ratio 60/49 at the member
  with margins (2,1,1) and (1,1,1,1), near the Birkhoff-type polytopes, as is the codegree-3
  3 x 8 family of [Fe26] (minimum linear coefficient 2157/280).
- No translation in print reaches the box: the known Ehrhart-negative families have facet
  normals outside the rhombus set (Reeve simplices, [CLNT18]) or dimension at least 14 (order
  polytopes, [LT19, LXZ26]), and the strip construction needs partitions of length 9 and 10
  already for a 3 x 8 table (move 9 of the attack).

## 8. Open questions

1. Size 31 at 5, 6 or 7 parts, and 8 parts: the first instances outside the box.
2. Is 24/25 the infimum, over all hive polytopes of dimension at least 3, of the ratio of an
   Ehrhart coefficient to the corresponding coefficient of the unimodular simplex? (The census
   covers dimension at least 3; a rational polygon with fewer than 3 boundary lattice points
   would have linear coefficient below H_2 = 3/2, and the dimension-2 hive polytopes of the box
   were not examined.)
3. Do hive polytopes with D + 1 lattice points and normalized volume 3 or more exist? The
   computed part of the box has none; a negative linear coefficient by that mechanism alone
   needs volume above 1 + H_D D(D-1).
4. A second Ehrhart solver on the 1,302,871 seven-part records would make the whole box a theorem relative to the trusted base (in which the Horn filter of the enumeration code sits with lrcalc and Normaliz).

## 9. Reproduction

Each enumeration or search directory under `deterministic/` holds its code and `input.json`,
its records (`.jsonl` with logs for runs 1 and 2; `.jsonl.gz` with logs and summaries for runs 3 and 4),
`README.md`, `check.sh` (the independent checker) and the harness's `result.json`; each
`certified-special-case-check-*` directory holds the verification script, its log and summary,
`check.sh`, `README.md` and `result.json`, and reads the records of the run it certifies.
Normaliz must run single-threaded (`OMP_NUM_THREADS=1`) when several workers share a
machine.

## References

- [BR15] M. Beck, S. Robins, Computing the Continuous Discretely, 2nd ed., Springer, 2015.
  doi:10.1007/978-1-4939-2969-6
- [CJM08] S. Cho, E.-K. Jung, D. Moon, Reduction formulae from the factorization theorem of
  Littlewood-Richardson polynomials by King, Tollu and Toumazet, Discrete Math. Theor. Comput.
  Sci. Proc. (2008). doi:10.46298/dmtcs.3592
- [CLNT18] F. Castillo, F. Liu, B. Nill, A. Paffenholz, Smooth polytopes with negative Ehrhart
  coefficients, J. Combin. Theory Ser. A 160 (2018) 316-331. arXiv:1704.05532
- [DM06] J. A. De Loera, T. B. McAllister, On the computation of Clebsch-Gordan coefficients
  and the dilation effect, Experiment. Math. 15 (2006). arXiv:math/0501446
- [DW02] H. Derksen, J. Weyman, On the Littlewood-Richardson polynomials, J. Algebra 255 (2002)
  247-257. doi:10.1016/S0021-8693(02)00125-4
- [Ep26] Epoch AI, FrontierMath open problem "Stretched Littlewood-Richardson coefficients",
  https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients and
  https://epoch.ai/files/open-problems/stretched-lr-coefficients.pdf (read 2026-09-03).
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
- [KTT09] R. C. King, C. Tollu, F. Toumazet, Factorisation of Littlewood-Richardson
  coefficients, J. Combin. Theory Ser. A 116 (2009) 314-333. doi:10.1016/j.jcta.2008.06.005
- [Lr] A. S. Buch, lrcalc, the Littlewood-Richardson calculator, version 2.1,
  https://math.rutgers.edu/~asbuch/lrcalc
- [LT19] F. Liu, A. Tsuchiya, Stanley's non-Ehrhart-positive order polytopes, Adv. Appl. Math.
  108 (2019). arXiv:1806.08403
- [LXZ26] F. Liu, G. Xin, Z. Zhang, Order polytopes of dimension <= 13 are Ehrhart positive,
  Discrete Math. 349 (2026) 114833. arXiv:2412.07164
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
