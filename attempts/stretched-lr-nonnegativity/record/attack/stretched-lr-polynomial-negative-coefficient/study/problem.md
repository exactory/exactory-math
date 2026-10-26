# Problem-level study: a negative coefficient in a stretched Littlewood-Richardson polynomial

Date: 2026-09-03. Contract: `STUDY.md` of the math-solver skill. Every fetched
document is saved under `study/sources/`.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| Q1 | arXiv API | `all:"stretched Littlewood-Richardson"`, 25 results by date | 2026-09-03 | 5 hits: 2607.22301, 2211.06810, 1505.06551, 1505.01542, 0904.4778 (`sources/arxiv-q1-stretched-LR.xml`) |
| Q2 | arXiv API | `all:"Littlewood-Richardson" AND all:polynomial AND all:negative AND all:coefficients` | 2026-09-03 | 5 hits, only 2607.22301 on topic (`sources/arxiv-q2-LR-negative.xml`) |
| Q3 | arXiv API | `all:"King" AND all:"Tollu" AND all:"Toumazet"` | 2026-09-03 | 9 hits (`sources/arxiv-q3-KTT.xml`): adds 1603.05626, 1209.1521, math/0603173, math/0308101, 2401.01582, 2005.09012 |
| Q4-Q7 | arXiv API | recent `Littlewood-Richardson AND stretched`, `hive AND polytope AND Ehrhart`, `Ehrhart AND positivity AND negative`, and an `id_list` for math/0501446, 2206.02276, 1711.09962 | 2026-09-03 | refused: HTTP 503 "Rate exceeded" after the first three queries; the abstracts of math/0501446, 2604.08394, 2101.00984 were read from arxiv.org/abs pages instead |
| Q8 | Semantic Scholar | `paper/search?query=stretched Littlewood-Richardson coefficients polynomial positivity` | 2026-09-03 | empty response (`sources/s2-q1.json`) |
| Q9 | Semantic Scholar | citations of DOI 10.1090/crmp/034/10 (King-Tollu-Toumazet 2004), 100 rows | 2026-09-03 | 60 citing papers, listed in `sources/s2-cit-ktt2004.json`; none announces a counterexample; newest are 2607.22301, 2604.27107, 2601.04182 |
| Q10 | Semantic Scholar | citations of ARXIV:2607.22301 | 2026-09-03 | none (`sources/s2-cit-2607.22301.json`) |
| Q11 | Crossref | `query.bibliographic=stretched Littlewood-Richardson Kostka coefficients King Tollu Toumazet`, 6 rows | 2026-09-03 | KTT 2004 (10.1090/crmp/034/10), KTT 2009 factorisation (10.1016/j.jcta.2008.06.005), Gutschwager 2011 (10.1016/j.jcta.2011.02.005), Sherman 2017 (10.1016/j.jalgebra.2017.03.011), stretched Newell-Littlewood (10.5802/alco.186) (`sources/crossref-q1.json`) |
| Q12 | zbMATH Open | `ti:stretched Littlewood-Richardson` | 2026-09-03 | 5 records: KTT 2004 (2124855), KTT 2006 (5660467), Ferudun 2026 (903113622), Thawinrak (8063758), Gutschwager 2011 (5909626) (`sources/zbmath-q1.json`) |
| Q13 | MathOverflow API | `stretched Littlewood-Richardson`; `King Tollu Toumazet` | 2026-09-03 | one question on factorisation of LR coefficients (mathoverflow.net/questions/461887), nothing on negative coefficients (`sources/mo-q1.json`, `mo-q2.json`) |
| Q14 | general web search | `King Tollu Toumazet conjecture counterexample stretched Littlewood-Richardson negative coefficient` | 2026-09-03 | only the arXiv papers above; no counterexample reported |
| Q15 | problem's own page | https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients and its background PDF `/files/open-problems/stretched-lr-coefficients.pdf` | 2026-09-03 | the canonical statement of the claim (`sources/epoch-stretched-lr-coefficients.pdf`) |
| Q16 | GitHub | github.com/AlperTheKing/ktt-positivity, the replay bundle of 2607.22301 | 2026-09-03 | cloned to `sources/ktt-positivity/`; read README, `proof/GENERAL_KTT_PROOF_STATUS.md`, `proof/ORDER_TRANSFER_3ROW_VERDICT.md`, `proof/r5/GENERALIZATION_REPORT.md`, `proof/r5/R5_AUDIT_VERDICT.md`, `engine/CALIBRATION.md`, `engine/BUILD_A.md` |
| Q17 | GitHub code search | `LittlewoodRichardson`, `Littlewood-Richardson`, `SchurPolynomial`, `SemistandardYoungTableau` in leanprover-community/mathlib4 | 2026-09-03 | only `SemistandardYoungTableau` and `YoungDiagram` exist; no LR coefficient, no Schur polynomial |

Formal statement: none. The claim has no entry in google-deepmind/formal-conjectures
(it is an Epoch AI problem, not an Erdos problem), and Mathlib has no definition of
the objects (Q17).

## 2. Hits worth reading

- arXiv:2607.22301 (Ferudun, 2026-07-24), "Positivity of stretched Littlewood-Richardson coefficients for partitions of length at most four". Full text read (`sources/2607.22301/ktt_positivity.tex`). Proves KTT positivity for length <= 4 by the Berline-Vergne local formula on hive polytopes after a period-one dilation; proves the top four coefficients of every full-dimensional hive positive; proves full-dimensional 5-part hives positive except possibly the linear coefficient; reduces the general conjecture to an effectivity statement (HTE); records that termwise cone positivity fails at codimension 4; records a valid 3 x 8 transportation-polytope transfer into LR that produces no negative because the family is Ehrhart positive (minimum linear coefficient 2157/280); states "extensive computation has produced no counterexample"; cites the Epoch FrontierMath open problem.
- github.com/AlperTheKing/ktt-positivity (cloned). Full text of the status files read. `GENERALIZATION_REPORT.md`: "No counterexample known; a ~405,000,000-triple project search found none" (ranges not recorded). `R5_AUDIT_VERDICT.md`: the half-integral hive (2,2,1; 4,3,2,1; 5,4,3,2,1) has L(0..6) = 1,5,16,40,85,161,280 and polynomial (1, 2, 17/12, 1/2, 1/12); the largest vertex denominator at 5 parts is bounded by max |det| = 7. `ORDER_TRANSFER_3ROW_VERDICT.md`: the Liu-Tsuchiya negative order polytope O(P_{7,7}) (255 lattice points, dimension 14, codegree 3) cannot be realised as a 3 x 8 transportation polytope (every codegree-3 member has >= 1050 points) and the whole family is positive. `engine/`: two independent LR counters (a C++ hive enumerator, a Python lattice-word counter) and an exact Newton interpolation with two held-out dilations, calibrated on all triples with |nu| <= 8.
- Epoch AI background PDF (read in full, 3 pages). The canonical statement, the box (length <= 7, size <= 30), the output format, "the problem author expects this to be false", special cases covered (Chen-Robbins-Yuen polytope; stretched Kostka numbers), the degree bound d <= C(l+1, 2), the note "hard going past l(lam) >= 6 or so", "reasonable to do a search on partitions with l(lam) <= 20", and the references (Castillo et al. 2018; Ferroni-Higashitani 2024; Derksen-Weyman 2002; Ikenmeyer 2016; KTT 2006; Knutson-Tao 1999; Panova 2023; Rassart 2004; Thawinrak 2022).
- arXiv:2211.06810 (Thawinrak), abstract: short proof of polynomiality via Steinberg's formula and the chamber complex.
- arXiv:1505.06551 (Sherman) and arXiv:1209.1521 (Ikenmeyer), abstracts: c = 2 implies P = t + 1.
- arXiv:0904.4778 (Gutschwager), abstract: adding an LR tableau's shape and content weakly increases the count (no operation that could amplify a negative coefficient).
- arXiv:math/0501446 (De Loera-McAllister), abstract via arxiv.org/abs: lattice-point algorithm (LattE) for tensor product multiplicities, six tables of computed examples, experimental support for saturation-type conjectures; positivity restated as their Conjecture 4.7 per the ktt-positivity report.
- arXiv:2604.08394 (Jochemko-Menon, 2026), abstract via arxiv.org/abs: marked order polytopes of skew shapes and skew Gelfand-Tsetlin polytopes are Ehrhart positive; stretched Kostka numbers are therefore not a source of a negative coefficient.
- arXiv:2101.00984 (King, 2021), abstract via arxiv.org/abs: stretched Newell-Littlewood coefficients are quasi-polynomials of period <= 2 with positivity conjectured; a neighbour, open.
- Semantic Scholar citation list of KTT 2004 (60 papers): read as titles; the two 2026 Schubert papers (2601.04182 saturation fails for Schubert coefficients; 2604.27107 stretched Schubert coefficients eventually quasi-polynomial) concern a different object.

## 3. What was learned, as constraints on the plan

1. The claim is open as of 2026-09-03: no counterexample is in print or on the problem's page; the problem's author expects one to exist. The attack is a search, not a proof.
2. Settled ranges (no counterexample can be there): every triple with length <= 4; every triple with c <= 2; for full-dimensional 5-part hives every coefficient but the linear one. So the search starts at 5 parts and, at 5 parts, targets either the linear coefficient of a full-dimensional (dimension 6) hive or a lower-dimensional hive of dimension >= 3; at 6 and 7 parts every coefficient below the top four is open.
3. A route in print that this attack must not duplicate: the 3 x 8 transportation-polytope transfer (dead, family positive). Reeve-type reasoning (few lattice points, large volume, lattice-sparse boundary) is the only Ehrhart-theoretic guidance; Horn-facet factorisation means a counterexample is primitive or has a primitive counterexample factor.
4. Tools in print: the hive model with Barvinok-type counting (LattE in 2006), exact Newton interpolation from D+1 dilations with two held-out checks (Ferudun 2026), two independent LR counters cross-calibrated. This workspace reproduces the route with Normaliz (`tools/hivepoly.py`, validated on the published values: the half-integral example, the (12,8,4)^2 -> (18,14,10,6) example with P = 1 + 7t + 18t^2 + 24t^3, and 300 random triples against lrcalc).
5. The prior search's range is not recorded (about 4 x 10^8 triples). Its size suggests that random or low-size sampling at 5 parts is already covered; the attack must go where that search likely did not: larger sizes near 30, 6 and 7 parts, and hives selected by an Ehrhart-theoretic criterion rather than at random.
6. A counterexample's certificate is small (a triple and its polynomial) and independently checkable; the unit form is a single counterexample if one is found, computational evidence otherwise.

## 4. Stop reason

The tier-one floor was reached (arXiv, Semantic Scholar, Crossref, zbMATH, the problem's own page and its replay repository), plus tier two (MathOverflow, web search). The last two sources with new results (the repository, the Epoch PDF) returned nothing beyond what 2607.22301 already contained; the arXiv rate limit blocked four follow-up queries, whose targets were reached through arxiv.org/abs pages.
