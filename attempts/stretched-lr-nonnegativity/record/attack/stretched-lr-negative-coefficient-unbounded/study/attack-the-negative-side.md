# Strategy study: attack-the-negative-side (unbounded conjecture)

Date: 2026-09-04. How the negative side of King-Tollu-Toumazet positivity was attacked
before: the range searched with no hit, the constructions in print and their resource, the
near misses and the conditions each passes. Contract: `STUDY.md`. Sources under the sibling
workspace's `study/sources/`.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| N1 | zbMATH Open | `Littlewood-Richardson polynomial negative coefficient` | 2026-09-04 | 4 records, only Ferudun 2026 on topic (`sources/zbmath-neg.json`) |
| N2 | Semantic Scholar | `paper/search?query=counterexample King Tollu Toumazet positivity stretched` | 2026-09-04 | empty response (`sources/s2-neg.json`) |
| N3 | Crossref | `query.bibliographic=stretched Littlewood-Richardson coefficients negative coefficient counterexample` | 2026-09-04 | KTT 2004, Gutschwager 2011, King 2022 (Newell-Littlewood), Thawinrak 2025, a shifted-LR paper; no counterexample (`sources/crossref-neg.json`) |
| N4 | arXiv API | (all queries since 2026-09-03 refused, HTTP 503) | 2026-09-04 | not available; arXiv items reached via abs pages and zbMATH earlier |
| N5 | the ktt-positivity repository | `engine/hive_poly.py` header (the hunt's waves and triage), `proof/r5/GENERALIZATION_REPORT.md` (the ~4 x 10^8-triple search), `proof/ORDER_TRANSFER_3ROW_VERDICT.md` (the transfer route) | 2026-09-03 | the record of the 2026 hunt |
| N6 | the sibling box attack | journal moves 1-6, `deterministic/enumeration-run-1..4`, `certified-special-case-check-1` | 2026-09-03/04 | the range searched with no hit and the near misses |

## 2. Hits worth reading

- Ferudun 2026 and repository: extensive computation with no counterexample; a project search of
  about 4 x 10^8 triples (ranges unrecorded); the hunt's waves 1-2 sampled with tableau/hive
  enumerators (minutes per stretched count at 6 parts); wave 3 planned the non-integral
  stratum (c <= dim H) as the region not yet entered; the transportation transfer route
  (3 x 8 family, dimension 14, codegree 3) is valid but the family is Ehrhart positive with
  minimum linear coefficient 2157/280; the Liu-Tsuchiya order polytope (255 points) is not
  realisable there (every codegree-3 member has >= 1050 points).
- The box attack (this project): every triple with length <= 7 and size <= 30 decided
  (6,855,302 polynomials, none negative; the 5-part part pinned by two implementations);
  the near misses are the empty non-unimodular simplices of normalized volume 2 (h* =
  (1, 0, 1, 0, ...), coefficient ratio 24/25) in dimensions 4, 5, 6; everywhere else the
  minimal linear coefficient is the unimodular-simplex value H_D; the linear coefficient grows
  with the vertex denominator; high-dimensional hives are fat (unimodal h*).
- KTT 2006: the polynomial carries the factor (t+1)...(t+M) with M the last dilation whose
  interior is empty; Conjecture 6.2 evaluates P(-m) as a signed negatively stretched LR
  coefficient for simple triples.
- Rassart 2004: the coefficients are piecewise polynomial on the chamber complex, a_k
  homogeneous of degree k; hence a_1 is piecewise linear and a chamber with a negative a_1
  contains integer points of every size.
- Cho-Jung-Moon 2008 / KTT 2009: the factorisation theorem, so a counterexample is primitive or
  has a primitive counterexample factor with fewer parts.

## 3. What was learned, as constraints on the plan

1. Range searched with no hit: length <= 4 (all, by theorem); the box length <= 7,
   size <= 30 (all); an unrecorded set of ~4 x 10^8 triples (Ferudun's hunt), most likely small
   sizes at 5 parts and samples at 6 parts. Every later search starts above the box.
2. Constructions in print: none produce a negative coefficient. The record of "sub-simplex"
   structures stops at normalized volume 2; a negative linear coefficient by the empty-simplex
   mechanism needs volume above 1 + H_D D(D-1) (27 in dimension 4).
3. Near misses and the conditions they pass: the volume-2 empty simplices pass primitivity,
   c = D + 1, non-unimodularity, and fail only by volume; the fat high-dimensional hives pass
   nothing (their a_1 is 4 to 5).
4. Conditions any counterexample must satisfy (for step 3): primitive; length >= 5; outside the
   box; c >= 3; dim H >= 3; at 5 parts either full-dimensional with a_1 < 0 or of dimension 3..5;
   by piecewise linearity, it lies in a chamber of the LR chamber complex on which a_1 (or a
   higher coefficient's polynomial) is negative on an open sub-cone, so integer points of every
   size in that sub-cone are counterexamples and random sampling at sizes well above the box
   tests chambers the box cannot reach.
5. Routes not to duplicate: enumeration inside the box; the 3 x 8 transportation family; the
   a_1 descent as first written (it walks into low-dimensional simplices, where a_1 is smallest
   but positive, `tools/descent.py`).

## 4. Stop reason

One query per tier-one source that answered (zbMATH, Crossref; Semantic Scholar's search endpoint
returned nothing; arXiv refused), plus the repository and the sibling record; the last two sources
(Crossref, the repository) added nothing beyond the sibling's study.
