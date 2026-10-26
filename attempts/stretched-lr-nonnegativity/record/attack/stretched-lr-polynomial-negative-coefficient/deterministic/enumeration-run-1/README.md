# enumeration-run-1: calibration scan of the box (predict-the-value-and-test-it-numerically)

Date: 2026-09-03. Entry: predict-the-value-and-test-it-numerically, actions 1-3.
Step kind: enumeration run (a seeded random sample of the finite residue R of move 1,
each instance decided exactly).

## The prediction (action 1)

Ehrhart theory writes the linear coefficient of P(t) = sum_i h*_i C(t + D - i, D) as

    a_1 = H_D + sum_{i=1}^{D} (-1)^{i-1} h*_i / (i C(D, i)),

with H_D the harmonic number, so a negative coefficient needs h*-mass at even indices
(h*_2: many lattice points at dilation 2, few at dilation 1, the Reeve pattern) or
at high indices (interior points at small dilations) against small h*_1 = c - D - 1
and small odd entries.  Prediction P1: the minimum of a_1 over a stratum is attained
by unimodular simplices, a_1 = H_D, unless the stratum contains non-unimodular
polytopes with few lattice points, which push a_1 below H_D.  Prediction P2 (the
hunt's prior, from `hive_poly.py` of the 2026 negativity hunt): non-integral hives
(vertex denominator >= 2) and hives with c <= D are the negative-leaning region.
Prediction P3: high-dimensional hives (6 and 7 parts, dimension >= 9) are where a
coefficient below the top four can first turn negative.  Assumptions: the sample is
uniform enough within each stratum to show the extremes; nothing is dropped.

## The run (action 2)

`scan.py --mode sample`: for each stratum (n, N) with n in {5, 6, 7} (largest length)
and N = |lam| in {22, 24, 26, 28, 30}, 3000 seeded random canonical triples with
parts <= 10 (seed 20260903, `scan-maxpart10.jsonl`) and 1000 with parts <= 30 (seed
20260904, `scan-maxpart30.jsonl`).  Canonical: mu >= nu lexicographically, no common
column at the largest length.  For every triple: c by lrcalc (classical rule); when
c >= 3, dim H by Normaliz; when dim H >= 3, the Ehrhart quasi-polynomial by Normaliz
(`EhrhartQuasiPolynomial` from the rhombus inequalities of `hivepoly.py`), the
vertex denominators, the leading-factor count M, the minimal coefficient.

Counts: 60,000 triples sampled; 45,000 (parts <= 10): 33,909 with c < 3, 3,811 with
dim H < 3, 7,280 polynomials; 15,000 (parts <= 30): 2,197 polynomials; 9,477
polynomials in all, every one with period 1 (Derksen-Weyman, as expected) and no
negative coefficient.  Dimensions reached: 5 parts up to 6, 6 parts up to 9, 7 parts
up to 12 (one triple, (7,6,5,4,3,2,1; 5,4,3,2,1; 5,4,2,1,1), c = 93).

## What the numbers say (action 3)

- P1 confirmed: in every (n, dim) stratum the minimum a_1 is exactly H_dim (11/6, 25/12,
  137/60, 49/20, 363/140, 761/280, 7129/2520, 7381/2520 for dim 3..10), attained by
  unimodular simplices, except that dimensions 4 and 5 contain empty non-unimodular
  simplices, h* = (1, 0, 1, 0, ...), c = dim + 1, normalized volume 2, with a_1 = 2 and
  67/30 (below H_4 = 25/12 and H_5 = 137/60).  Forty such triples were found, all with
  a small third partition (nu = (2,2,1), (2,2,1,1), (2,2,2,1), (3,3,1,1), ...).
- P2 refuted as a direction: a_1 increases with the vertex denominator (mean a_1 2.27 at
  denominator 1, 2.87 at 2, 3.43 at 3, 3.84 at 4) and no record has a negative h* entry;
  the non-integral hives are the more positive ones.
- P3 refuted in the sample: the high-dimensional hives are fat (h* unimodal with the mass
  in the middle; the dim-12 triple has h* = (1, 80, 2549, 25891, 98855, 155299, ...)) and
  their a_1 is 4 to 5; the ratio of each coefficient to the unimodular-simplex value
  never falls below 0.96, and that minimum is the volume-2 empty simplices' a_1.
- Corrected prediction: within the box, the only structures that lower a coefficient
  below the simplex value are empty (c = D + 1) non-unimodular hive polytopes; a
  negative linear coefficient by that mechanism needs normalized volume > 1 + H_D D(D-1)
  (27 in dimension 4, 47 in dimension 5, 75 in dimension 6; journal move 2 and an earlier version of this line said 148 for dimension 6, which is the threshold 1 + H_6 4 C(6,4) for mass at index 4, not the index-2 one the formula gives), against the volume 2
  observed.  The next runs therefore (i) enumerate the 5-part box exhaustively, since
  every 5-part triple with c >= 3 can be decided (about 1.7 million triples), and (ii)
  at 6 and 7 parts, search for polytopes with few lattice points and large volume
  (small c, large c(2)/c(1) and c(3)), the only negative-leaning shape the data show.

## Independent check

`check.sh` runs `check.py`: for 60 records (every negative one, none; the 15 with the
smallest a_1; the 15 with the smallest coefficient; 30 seeded random) it recounts
c^{t lam}_{t mu, t nu} for t = 0..min(deg + 2, 5) by the classical lattice-word rule
(`lrtableaux.py`, no hive, no polytope, no Normaliz) and compares with the recorded
polynomial: 29 records pinned (deg + 2 points), 31 consistent at 6 points, 0 mismatches
(`result.json`).  lrcalc supplied c at t = 1 in the scan itself.  Trusted base: Normaliz
3.11 (via PyNormaliz) for the polynomials, lrcalc for c, Python integers and Fractions.

## What the run decided

Evidence, not a decision: no coefficient is negative among the 9,477 sampled polynomials;
the minimum of every coefficient over the sample is within 4 percent of the
unimodular-simplex value, and the only sub-simplex structures are volume-2 empty
simplices in dimensions 4 and 5.

## Correction (2026-09-04, from certified-special-case-check-4)

The polytopes this README calls "empty non-unimodular simplices" were named from their Ehrhart
polynomial (that of an empty lattice simplex of normalized volume 2, h* = (1, 0, 1, 0, ...),
c = D + 1). The vertex counts recorded by run 2 show that at 5 parts each of the 304 has 7 vertices, so at 5 parts they are not simplices (runs 3 and 4 recorded no vertex counts); read "polytopes with D + 1 lattice points, normalized
volume 2 and h* = (1, 0, 1, 0, ...)". The census of check 4 also shows that their minimal
coefficient ratio is 24/25 only in dimension 4 (44/45 in dimension 5, 799/812 in dimension 6).
