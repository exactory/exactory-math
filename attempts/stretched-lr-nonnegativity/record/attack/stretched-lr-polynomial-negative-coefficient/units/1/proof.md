# Unit 1: positivity of stretched Littlewood-Richardson polynomials for at most six parts and size at most 30

## Statement

For all integer partitions lam, mu, nu with at most 6 parts each and |lam| = |mu| + |nu| <= 30,
every coefficient of the stretched Littlewood-Richardson polynomial
P(t) = c^{t lam}_{t mu, t nu} (a polynomial in t) is nonnegative.

## Proof by computation

Throughout, c = c^{lam}_{mu nu}, n = the largest length among the three partitions, and H =
H(lam, mu, nu) is the Knutson-Tao hive polytope: the rational polytope of real hives of side n
with boundary labels the partial sums of lam, mu, nu, cut out by the rhombus inequalities
(`hivepoly.py` in every step directory).

**Facts used, with their references (all in `problem.json`, `known`).**

- (F1) c = number of integer points of H, and H(t lam, t mu, t nu) = t H (the rhombus
  inequalities are homogeneous and the boundary labels scale with t), so P(t) is the Ehrhart
  quasi-polynomial of H evaluated at t (Knutson and Tao 1999).
- (F2) P is a polynomial in t (Derksen and Weyman 2002; Rassart 2004), of degree at most
  dim H <= (n-1)(n-2)/2, the number of interior hive entries, with P(0) = 1 (the constant term
  of the Ehrhart quasi-polynomial of a rational polytope is 1 at t = 0, and it is constant when
  the quasi-polynomial is a polynomial).
- (F3) If every one of lam, mu, nu has at most 4 parts, every coefficient of P is nonnegative
  (Ferudun 2026, arXiv:2607.22301, Theorem 1).
- (F4) c = 0 gives P = 0 (saturation, Knutson and Tao 1999: c^{t lam}_{t mu, t nu} > 0 forces
  c > 0, so P vanishes at every positive integer and is the zero polynomial); c = 1 gives P = 1
  (Knutson, Tao, Woodward 2004); c = 2 gives P = t + 1 (Ikenmeyer 2016; Sherman 2017).
- (F5) Symmetry and column removal: c^{t lam}_{t mu, t nu} = c^{t lam}_{t nu, t mu}; and when
  lam and mu both have exactly n parts, with n the largest length, P(lam, mu, nu) =
  P(lam - (1^n), mu - (1^n), nu), because c^{kappa + (1^n)}_{rho + (1^n), sigma} =
  c^{kappa}_{rho sigma} for partitions with at most n parts (multiplication by the determinant
  in GL_n), applied to (t lam, t mu, t nu) with t columns removed.
- (F6) If dim H <= 2, every coefficient of P is nonnegative: P = 1 for a point; for dim H = 1
  or 2, Ehrhart-Macdonald reciprocity P(-t) = (-1)^{dim H} P°(t) (P°(t) the number of interior
  points of tH, valid for rational polytopes) gives, for dim H = 2, P(t) - P(-t) = 2 a_1 t =
  the number of boundary points of tH >= 0, so a_1 >= 0, while a_2 = vol H > 0 and a_0 = 1;
  for dim H = 1, P(t) + P(-t) = 2 a_0 = P(t) - P°(t) >= 0 and P(t) - P(-t) = 2 a_1 t =
  P(t) + P°(t) >= 0.
- (F7) The King-Tollu-Toumazet factorisation theorem is not needed for this unit (it is used
  only at 7 parts, in unit 2).

**The computation.** Two exhaustive enumerations, one per value of n:

- `deterministic/enumeration-run-2` (n = 5): every canonical triple (mu >= nu in
  lexicographic order, mu and nu contained in lam, 1 <= |mu| <= |lam| - 1, neither mu nor nu
  with 5 parts) with largest length exactly 5 and |lam| <= 30: 12,091,018 triples; c by lrcalc;
  for c >= 3 the dimension of H by Normaliz; for dim H >= 3 the Ehrhart quasi-polynomial of H
  by Normaliz from the rhombus inequalities: 1,334,669 polynomials, every one of period 1,
  none with a negative coefficient (records `scan-n5-*.jsonl`; per-size totals in `result.json`, status pass; `README.md` gives the total and the size-30 value).
- `deterministic/enumeration-run-3` (n = 6): the same for largest length exactly 6 and
  |lam| <= 30: 31,745,644 canonical triples; 4,217,762 polynomials, period 1, none negative
  (`result.json` status pass).

**Completeness of the enumerations.** For each run, `check.sh` recounts the number of canonical
triples of every size (5..30, respectively 6..30) by an independent generator, containment
test and canonical form that share no code with the scan, and compares with the scan's
per-size totals: 0 mismatches (`enumeration-run-2/result.json`, `enumeration-run-3/result.json`).

**Certification of every polynomial by a second program.**

- `deterministic/certified-special-case-check-1`: for every one of the 1,334,669 records of
  run 2, lrcalc (the classical Littlewood-Richardson rule, no code shared with Normaliz or with
  the hive encoder) computed c^{t lam}_{t mu, t nu} for t = 1..6; with P(0) = 1 (F2) and
  deg P <= 6 (six interior entries at side 5), the seven values determine P; exact Newton
  interpolation reproduced the Normaliz polynomial in every case: 0 mismatches. The checker
  (`result.json` status pass) confirms the summary and recounts 310 records by a third
  implementation (the lattice-word counter `lrtableaux.py` with a Lagrange interpolation).
- `deterministic/certified-special-case-check-2`: the same for the 4,217,762 records of run 3,
  with t = 1..10 (ten interior entries at side 6): 0 mismatches; the checker recounts 30
  records by the third implementation (`result.json` status pass).

**The argument.** Let (lam, mu, nu) be as in the statement; induct on |lam|. If c = 0, or
c <= 2, P is 0, 1, or t + 1 by (F4). Otherwise mu and nu are contained in lam (c > 0), so
n = the length of lam. If n <= 4, apply (F3). If n is 5 or 6: swap mu and nu if needed so that
mu >= nu lexicographically (F5, first part); if mu or nu has n parts, remove one column from
lam and from that partition (F5, second part): the new triple has the same P, at most 6 parts
and size |lam| - n < |lam|, so P has nonnegative coefficients by the induction hypothesis.
Otherwise the triple is canonical with largest length n and c >= 3, so it is one of the triples
of run 2 (n = 5) or run 3 (n = 6), by the completeness recount. If dim H <= 2, apply (F6). If
dim H >= 3, P is the recorded polynomial: Normaliz computed it from H (F1, F2), lrcalc
reproduced it independently, and its coefficients are nonnegative (no record is negative).
This covers every case.

**Trusted base.** Normaliz 3.11 (through PyNormaliz), lrcalc, Python integers and Fractions,
the facts (F1)-(F6) with their references, the encoders (`hivepoly.py` for Normaliz's input;
the enumeration code, whose completeness is recounted independently), and the checker scripts
recorded in the step directories. Every polynomial rests on two programs that share no code
(Normaliz on the hive inequalities; lrcalc by the classical rule with exact interpolation).

## Reproduction

Each enumeration directory holds its code and `input.json`, its records (`.jsonl` for run 2, `.jsonl.gz` for run 3), its logs (run 2, whose per-size totals are in `result.json`; its `README.md` gives the total and the size-30 value) or its log and summary (run 3), `README.md`, `check.sh`, and the harness's
`result.json`; each certified-special-case-check directory holds the verification script
(`verify5.py`, `verify6.py`), its log and summary, `check.sh`, `README.md` and `result.json`,
and reads the records of the run it certifies. Runs 2 and 3 take 10.5 minutes and 31
minutes on 10 single-threaded Normaliz workers; check 1 takes 2 minutes and check 2 about 12
hours on 11 workers (lrcalc enumerates tableaux; the largest value is P(10) = 473,221,012).
