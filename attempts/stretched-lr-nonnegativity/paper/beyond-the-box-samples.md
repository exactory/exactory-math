# The negative side of the King-Tollu-Toumazet conjecture beyond the box: sampled classes, the recurring near-misses, and a few-point hive polytope of volume three

Draft of 2026-09-05 (unit 1 of the attack `stretched-lr-negative-coefficient-unbounded`): a
computational note on where the search for a counterexample stands outside the box of length
at most 7 and size at most 30, with the state of the attack and the open questions.

## Abstract

King, Tollu and Toumazet conjectured that the stretched Littlewood-Richardson coefficient
c^{t lam}_{t mu, t nu}, a polynomial in t, has nonnegative coefficients. The sibling note settles
the box of length at most 7 and size at most 30 in the negative (no counterexample). Here the
classes a counterexample must lie in (unit 2 of this attack) are sampled beyond the box with
fixed seeds and independent checkers: 400,000 primitive 5-part hives of sizes up to 200, 40,000
primitive 6-part hives of dimension 8 to 10 and sizes up to 80, 1,799 primitive 8-part hives of
dimension up to 12, 12,000 primitive hives with at most D + 2 lattice points, and 5,170
transportation polytopes of six small families. None has a negative coefficient. The
polynomials whose coefficients fall below the unimodular-simplex values are exactly the
polytopes with D + 1 lattice points, h*-vector (1, 0, 1, 0, ...) and normalized volume 2 that
the box already contains, now also in dimension 7, and one polytope with D + 1 lattice points
and normalized volume 3 at 8 parts, the first of its kind in the record, with h*-vector
(1, 0, 2, 0, 0, 0, 0) and every coefficient still positive.

## 1. Statement

The statement of `unit.json` (unit 1): in the sampled classes listed in Section 3 no stretched
Littlewood-Richardson polynomial or transportation-polytope Ehrhart polynomial has a negative
coefficient; the polynomials with a coefficient below the corresponding coefficient of the
unimodular simplex are exactly the polytopes with D + 1 lattice points and h*-vector
(1, 0, 1, 0, ...) of normalized volume 2 (minimal ratios 24/25, 44/45, 799/812, 927/938 in
dimensions 4 to 7) and one polytope of normalized volume 3 with h*-vector (1, 0, 2, 0, 0, 0, 0)
at 8 parts (lam = (4,4,3,3,2,2,1,1), mu = (3,3,2,2,1,1), nu = (3,2,2,1), minimal ratio 393/406).
The unit is computational evidence (form counterexample-or-computational-evidence): the
polynomials of runs 3 and 4 outside their checkers' samples rest on one solver and lrcalc at
t = 1, and a sample proves nothing about the unsampled part of a class.

## 2. Background

The conjecture [KTT04, KTT06], polynomiality [DW02, Ra04], the hive model [KT99], the known
cases (c <= 2, [KTW04, Ik16, Sh17]; length <= 4 and the top four coefficients of full-dimensional
hives, [Fe26]), the factorisation on saturated Horn inequalities [KTT09, CJM08], and the box
result of the sibling attack are as in the sibling note (`../stretched-lr-polynomial-negative-
coefficient/units/2/draft.md`). Unit 2 of this attack proves that a counterexample, if one
exists, can be taken primitive with c >= 3, dim H >= 3, at least 5 parts, outside the box, at
5 parts full-dimensional with a negative linear coefficient or of dimension 3 to 5, and inside a
chamber of the Littlewood-Richardson chamber complex whose coefficient polynomial is negative on
an open sub-cone, so that counterexamples of every multiple of its size exist there. This
defines the classes sampled here: S1 (5 parts, all dimensions and full-dimensional), S2 (6 parts,
dimension 8 to 10), S3 (8 parts), E (few lattice points, where the h*-expansion of the linear
coefficient a_1 = H_D + sum_i (-1)^{i-1} h*_i / (i binom(D, i)) can turn negative), and the
transportation families, whose 3 x N members are Littlewood-Richardson polytopes by the strip
construction of [Fe26]. The novelty record of the attack (`novelty.md`, stage 3 and unit-level
queries of 2026-09-04 and 2026-09-05) found no search of these classes and no negative
coefficient in print.

## 3. The samples

All runs: `sample_search.py` (lrcalc for c, `horn.py` for primitivity with the essential Horn
triples of the rank, Normaliz 3.11 [No] for the dimension and the Ehrhart quasi-polynomial from
the hive inequalities), or `transport.py` for the transportation polytopes; fixed seeds; every
quasi-polynomial has period 1. Each run's `result.json` has status pass.

| run | class | sampled | records | negatives | minimal coefficient ratio |
|---|---|---|---|---|---|
| 1 | S1 | primitive 5-part hives, sizes 31..200: dimension >= 3 (seed 20260904) and full-dimensional (seed 20260905) | 300,000 + 100,000 | 0 | 1 and 157/147 |
| 2 | S4 | transportation polytopes 3 x 4 (total <= 16), 3 x 5 (<= 14), 3 x 6 (<= 12), 4 x 4 (<= 14), 4 x 5 (<= 11), 5 x 5 (<= 8) | 5,170 | 0 | 60/49 |
| 3 | S2 | primitive 6-part hives, dimension 8..10, sizes 31..80 (seed 20260906) | 40,000 | 0 | 1 |
| 4 | S3 | primitive 8-part hives, dimension 3..12, sizes 20..40 (seed 20260913; stopped after 2,000, 1,799 readable) | 1,799 | 0 | 393/406 |
| 5 | E | primitive hives with at most D + 2 lattice points: 5 parts sizes 31..120, 6 parts 31..80, 7 parts 31..60 (seeds 20260907-9) | 6,000 | 0 | 1 |
| 6 | E, small nu | the same with the third partition of size at most 8 (seeds 20260910-2) | 6,000 | 0 | 24/25 |

Checkers (`check.sh` in each directory): run 1, every polynomial recomputed from the
tableau-polytope encoding (`tableau_polytope.py`, the lattice-word inequalities, no hive
inequality) by Normaliz, lrcalc at t = 1 and 2, and lrcalc pinning at t = 0..6 for the 336,404
records with P(6) <= 2,000,000 (all agree); runs 5 and 6, the same with pinning at t = 0..D_n
for 5,907 and 5,968 records (all agree); runs 3 and 4, lrcalc at t = 1 on every record and the
second encoding on 1,500 sampled records; run 2, 78 pairs recounted from the definition of a
contingency table; a third implementation (the lattice-word counter `lrtableaux.py`) on 30
records of each hive run; counts and filters re-verified.

## 4. What the samples show

- No negative coefficient among the 453,799 hive polynomials and the 5,170 transportation
  polynomials.
- The per-stratum minima of the linear coefficient beyond the box equal the box's: 157/60 in the
  full-dimensional 5-part stratum (run 1, the value of the box's 13,217 full-dimensional hives);
  761/280 = H_8, 3827/1260 and 2843/840 in dimensions 8, 9 and 10 at 6 parts (run 3, the box's
  three values).
- The polynomials with a coefficient below the unimodular-simplex value: none in runs 1, 3 and 5
  (every sampled polytope with D + 1 lattice points there is unimodular); in run 6, exactly 112
  of 6,000, all with D + 1 lattice points and normalized volume 2 (13 of dimension 4 at 5 parts;
  13 of dimension 4 and 31 of dimension 5 at 6 parts; 23, 17 and 15 of dimensions 4, 5, 6 at 7
  parts), with the box's ratios 24/25, 44/45, 799/812; in run 4, six: three of dimension 6 and two
  of dimension 7 with volume 2 (ratios 799/812 and 927/938, the h*-pattern (1, 0, 1, 0, ...) one
  dimension higher than the box shows), and one of dimension 6 with normalized volume 3:
  lam = (4,4,3,3,2,2,1,1), mu = (3,3,2,2,1,1), nu = (3,2,2,1), c = 7,
  P(t) = (240 + 572 t + 524 t^2 + 255 t^3 + 75 t^4 + 13 t^5 + t^6)/240, P(1) = 7, P(2) = 30,
  h* = (1, 0, 2, 0, 0, 0, 0), linear coefficient 143/60 = H_6 - 2/30, minimal ratio 393/406 at
  the coefficient of t^2. The box (length <= 7) and the samples at 5, 6, 7 parts contain no
  few-point polytope of volume above 2; this one shows the bound is a property of length <= 7,
  not of hive polytopes. By the h*-expansion, a negative linear coefficient in dimension 6 with
  the mass at index 2 needs h*_2 > H_6 30 = 73.5; this polytope has h*_2 = 2.
- The largest normalized volume among polytopes with at most D + 2 lattice points is 3 at 5 parts, 4 and 10 at 6 parts (runs 5 and 6), 3 and 10 at 7 parts, 6 at 8 parts; none of them has a coefficient below the simplex
  value except the volume-2 and volume-3 polytopes with exactly D + 1 points listed above.
- The transportation families are Ehrhart positive with minimal ratio 60/49 at the member with
  margins (2,1,1) and (1,1,1,1); the tool reproduces the 3 x 8 example of [Fe26] (1050 lattice
  points, linear coefficient 2157/280), the Ehrhart polynomial of the Birkhoff polytope B_3 and
  the volume of B_5 (Beck and Pixton [BP03] computed the Ehrhart polynomials of B_n for n <= 8).

## 5. The state of the attack (problem-paper content)

- The walk: attack-the-negative-side (moves 1 to 3: the necessary conditions of unit 2, the
  transportation families, the six search runs), then reduce-and-translate (move 4), then
  prove-the-barrier-first (ended at its study). Every strategy ended in its failure signal.
- The near miss that passes every necessary condition and is not a counterexample: the
  few-point polytopes above (ratio 24/25 at best, 393/406 for the volume-3 one).
- The translation ceiling (move 4): the one map in print from another family into hives is the
  strip construction for 3 x N transportation polytopes [Fe26]; it is one-way (a negative
  transportation polytope would refute the conjecture, positivity of all of them proves nothing
  about other hives), and Ehrhart positivity of transportation polytopes is itself open in print
  (the destination has Lidskii-type formulas [MM19] and partial Berline-Vergne positivity for
  Tesler polytopes [LL22], no sign theorem); the extension of the construction to k x N tables
  with k >= 4 is not in print.
- The barrier in print (prove-the-barrier-first): proofs by termwise nonnegativity of one fixed
  local formula (McMullen, Berline-Vergne) on the faces of hive polytopes stop at codimension 4,
  where a cell of weight -349/28800 is negative [Fe26]; the same class of argument fails on
  matroid polytopes, which are not Ehrhart positive [Fe21] although conjectured to be [CL18].
  What is not in print is whether some other local formula is termwise nonnegative on hive
  faces, which is the (HTE) statement of [Fe26].
- Open: sizes above 200 at 5 parts and above 80 at 6 parts; dimensions above 12 and sizes above
  40 at 8 parts; 9 parts and more; whether 24/25 is the infimum of the coefficient ratio over
  hive polytopes of dimension at least 3; few-point hive polytopes of volume above 3 (the volume-3
  one was found at 8 parts at size 20, inside the box's size range but beyond its length);
  the (HTE) statement.

## 6. Reproduction

Each directory under `deterministic/` holds the sampling code and its copies of the tools,
`input.json` or `run_all.sh`, the gzipped records, summaries and logs, `README.md`, `check.sh`
and `result.json`. Normaliz runs single-threaded (`OMP_NUM_THREADS=1`). The eight-part run's
record file was rewritten from its readable lines after the run was stopped (its README says
how); the checker reads the rewritten file.

## References

- [BP03] M. Beck, D. Pixton, The Ehrhart polynomial of the Birkhoff polytope, arXiv:math/0202267 (2002).
- [CJM08] S. Cho, E.-K. Jung, D. Moon, Reduction formulae from the factorization theorem of
  Littlewood-Richardson polynomials by King, Tollu and Toumazet, Discrete Math. Theor. Comput.
  Sci. Proc. (2008). doi:10.46298/dmtcs.3592
- [CL18] F. Castillo, F. Liu, Berline-Vergne valuation and generalized permutohedra, arXiv:1509.07884.
- [DW02] H. Derksen, J. Weyman, On the Littlewood-Richardson polynomials, J. Algebra 255 (2002)
  247-257. doi:10.1016/S0021-8693(02)00125-4
- [Fe21] L. Ferroni, Matroids are not Ehrhart positive, arXiv:2105.04465
- [Fe26] A. Ferudun, Positivity of stretched Littlewood-Richardson coefficients for partitions
  of length at most four, arXiv:2607.22301 (2026).
- [Ik16] C. Ikenmeyer, Small Littlewood-Richardson coefficients, J. Algebraic Combin. 44 (2016)
  1-29. arXiv:1209.1521
- [KT99] A. Knutson, T. Tao, The honeycomb model of GL_n(C) tensor products I: proof of the
  saturation conjecture, J. Amer. Math. Soc. 12 (1999) 1055-1090. arXiv:math/9807160
- [KTW04] A. Knutson, T. Tao, C. Woodward, The honeycomb model of GL_n(C) tensor products II:
  puzzles determine facets of the Littlewood-Richardson cone, J. Amer. Math. Soc. 17 (2004)
  19-48. arXiv:math/0107011
- [KTT04] R. C. King, C. Tollu, F. Toumazet, Stretched Littlewood-Richardson and Kostka
  coefficients, CRM Proc. Lecture Notes 34 (2004) 99-112. doi:10.1090/crmp/034/10
- [KTT06] R. C. King, C. Tollu, F. Toumazet, The hive model and the polynomial nature of
  stretched Littlewood-Richardson coefficients, Sem. Lothar. Combin. 54A (2006), B54Ad.
  https://www.mat.univie.ac.at/~slc/wpapers/s54Akitoto1.pdf
- [KTT09] R. C. King, C. Tollu, F. Toumazet, Factorisation of Littlewood-Richardson
  coefficients, J. Combin. Theory Ser. A 116 (2009) 314-333. doi:10.1016/j.jcta.2008.06.005
- [LL22] Y. Lee, F. Liu, Ehrhart positivity of Tesler polytopes and Berline-Vergne's valuation,
  Discrete Comput. Geom. (2022). arXiv:1911.06291 ; doi:10.1007/s00454-022-00453-1
- [MM19] K. Meszaros, A. H. Morales, Volumes and Ehrhart polynomials of flow polytopes, Math. Z.
  (2019). arXiv:1710.00701 ; doi:10.1007/s00209-019-02283-z
- [No] W. Bruns, B. Ichim, C. Soeger, U. von der Ohe, Normaliz. Algorithms for rational cones
  and affine monoids, version 3.11, https://www.normaliz.uni-osnabrueck.de/ ; PyNormaliz 2.24,
  https://github.com/Normaliz/PyNormaliz
- [Ra04] E. Rassart, A polynomiality property for Littlewood-Richardson coefficients, J. Combin.
  Theory Ser. A 107 (2004) 161-179. arXiv:math/0308101
- [Sh17] C. Sherman, Quiver generalization of a conjecture of King, Tollu, and Toumazet, J.
  Algebra (2017). doi:10.1016/j.jalgebra.2017.03.011 ; arXiv:1505.06551
