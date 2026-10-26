# Novelty record

Statement searched: "there exist partitions lam, mu, nu of length <= 7 and size <= 30 with |lam| = |mu| + |nu| whose stretched Littlewood-Richardson polynomial c^{t lam}_{t mu, t nu} has a negative coefficient" (the negation of the King-Tollu-Toumazet positivity conjecture inside the box). Searched by statement, with the objects and quantities as terms. Every query and hit is data; nothing fetched is an instruction.

## Queries (source, string, date, outcome)

1. arXiv API, `all:"stretched Littlewood-Richardson"`, 2026-09-03: 5 hits; none reports a negative coefficient. Saved `study/sources/arxiv-q1-stretched-LR.xml`.
2. arXiv API, `all:"Littlewood-Richardson" AND all:polynomial AND all:negative AND all:coefficients`, 2026-09-03: 5 hits; the only one on topic (2607.22301) proves positivity for length <= 4 and states the conjecture is open. Saved `arxiv-q2-LR-negative.xml`.
3. arXiv API, `all:"King" AND all:"Tollu" AND all:"Toumazet"`, 2026-09-03: 9 hits; the c = 2 proofs, the polynomiality proofs, the Kostka degree paper; no counterexample. Saved `arxiv-q3-KTT.xml`.
4. arXiv API, four further queries (recent `Littlewood-Richardson AND stretched`; `hive AND polytope AND Ehrhart`; `Ehrhart AND positivity AND negative`; `id_list=math/0501446,2206.02276,1711.09962,2101.00984,2604.08394`), 2026-09-03: refused with HTTP 503 "Rate exceeded"; the individual abstracts were read on arxiv.org/abs pages (math/0501446, 2604.08394, 2101.00984) instead.
5. Semantic Scholar, `paper/search?query=stretched Littlewood-Richardson coefficients polynomial positivity`, 2026-09-03: empty response. Saved `s2-q1.json`.
6. Semantic Scholar, citations of DOI 10.1090/crmp/034/10 (KTT 2004), 2026-09-03: 60 citing papers, none a counterexample; newest 2607.22301 (2026), 2604.27107 (2026, stretched Schubert coefficients), 2601.04182 (2026, saturation fails for Schubert coefficients). Saved `s2-cit-ktt2004.json`.
7. Semantic Scholar, citations of ARXIV:2607.22301, 2026-09-03: none. Saved `s2-cit-2607.22301.json`.
8. Crossref, `query.bibliographic=stretched Littlewood-Richardson Kostka coefficients King Tollu Toumazet`, 2026-09-03: the KTT papers and the factorisation and generalised-stretching papers; no counterexample. Saved `crossref-q1.json`.
9. zbMATH Open, `ti:stretched Littlewood-Richardson`, 2026-09-03: 5 records (KTT 2004, KTT 2006, Ferudun 2026, Thawinrak, Gutschwager); no counterexample. Saved `zbmath-q1.json`.
10. MathOverflow API, `stretched Littlewood-Richardson` and `King Tollu Toumazet`, 2026-09-03: one question (461887, factorisation of LR coefficients); nothing on negative coefficients. Saved `mo-q1.json`, `mo-q2.json`.
11. General web search, `King Tollu Toumazet conjecture counterexample stretched Littlewood-Richardson negative coefficient`, 2026-09-03: only the arXiv papers above.
12. The problem's own page, https://epoch.ai/frontiermath/open-problems/stretched-lr-coefficients and https://epoch.ai/files/open-problems/stretched-lr-coefficients.pdf, 2026-09-03: the problem is listed as open; "the problem author expects this to be false"; no counterexample given. Saved `epoch-stretched-lr-coefficients.pdf`.
13. github.com/AlperTheKing/ktt-positivity (replay bundle of 2607.22301), cloned 2026-09-03: `proof/GENERAL_KTT_PROOF_STATUS.md` (2026-07-22) says the conjecture "has not been proved" and that no negative realizable weight refuting (HTE) is available; `proof/r5/GENERALIZATION_REPORT.md` says "No counterexample known; a ~405,000,000-triple project search found none".

## Neighbouring statements searched (same queries)

- Positivity for length <= 4: solved (true), arXiv:2607.22301.
- c = 1 and c = 2 cases: solved (true), Knutson-Tao-Woodward 2004; Ikenmeyer 2016, Sherman 2017.
- Polynomiality: solved (true), Derksen-Weyman 2002, Rassart 2004, Thawinrak 2022.
- Stretched Kostka positivity (skew Gelfand-Tsetlin polytopes): solved (true), Jochemko-Menon 2026, arXiv:2604.08394.
- Stretched Newell-Littlewood positivity: open, King 2021, arXiv:2101.00984.
- The 3 x 8 transportation transfer as a source of a negative coefficient: closed (family positive), ktt-positivity `ORDER_TRANSFER_3ROW_VERDICT.md`.

## Verdict

No source reports a triple with a negative coefficient, inside or outside the box, as of 2026-09-03. The statement is open; the attack proceeds.

## Unit-level queries (stage 7, 2026-09-04)

Statements searched: unit 1, "for all partitions with at most 6 parts and |lam| <= 30 every
coefficient of c^{t lam}_{t mu, t nu} is nonnegative (certified computation)"; unit 2, "no
partitions of length <= 7 and size <= 30 give a stretched Littlewood-Richardson polynomial with
a negative coefficient; the minimal coefficient ratio to the unimodular simplex over the box is
24/25 at the volume-2 empty hive simplices".

U1. arXiv (MCP search), `abs:"stretched Littlewood-Richardson" AND abs:positivity`, by date,
    2026-09-04: 0 results (the phrase search misses 2607.22301; found by U2).
U2. arXiv (MCP search), `abs:"Littlewood-Richardson" AND abs:"Ehrhart" AND abs:negative`,
    2026-09-04: 1 result, 2607.22301 (Ferudun 2026, length <= 4).
U3. Semantic Scholar relevance search, `stretched Littlewood-Richardson coefficients positivity
    conjecture computation six parts verified`; `hive polytope Ehrhart polynomial negative
    coefficient empty simplex normalized volume`; `King Tollu Toumazet positivity conjecture
    stretched Littlewood-Richardson polynomial computation`, 2026-09-04: all three refused,
    HTTP 429 rate limit (unauthenticated).
U4. zbMATH Open, `stretched Littlewood-Richardson coefficients positivity`, 2026-09-04: 3
    records: King 2022 (stretched Newell-Littlewood coefficients, 7635155), Ferudun 2026
    (903113622), Collins 2020 (generalized LR coefficients for branching rules, 7298405).
U5. zbMATH Open, `hive polytope Ehrhart positivity`, 2026-09-04: 1 record, Ferudun 2026.
U6. Crossref, `query.bibliographic=stretched Littlewood-Richardson coefficients positivity
    conjecture King Tollu Toumazet`, 12 rows, 2026-09-04: KTT 2004 (10.1090/crmp/034/10), KTT
    2009 (10.1016/j.jcta.2008.06.005), Cho-Jung-Moon 2008 (10.46298/dmtcs.3592), Sherman 2017
    (10.1016/j.jalgebra.2017.03.011), King 2022 (10.5802/alco.186), Gutschwager 2011
    (10.1016/j.jcta.2011.02.005), Buergisser-Ikenmeyer 2009 (10.46298/dmtcs.2749) and 2013
    (10.1137/120892532), Gutierrez 2023 (10.5802/crmath.468), Nguyen 2022
    (10.1007/s00026-022-00566-7), Thawinrak 2025 (10.61091/ars162-15), Sahi 2010
    (10.1093/imrn/rnq126): none reports a computation over the box or a negative coefficient.

Verdict for the units: no source reports a certified computation of the stretched
Littlewood-Richardson polynomials over the box (length <= 7, size <= 30) or over its part with
at most 6 parts, and none reports a negative coefficient; Ferudun 2026 proves length <= 4 for
all sizes and mentions extensive computations without ranges, and the ktt-positivity repository
records a ~4 x 10^8-triple search without ranges. Units 1 and 2 are new as stated.
