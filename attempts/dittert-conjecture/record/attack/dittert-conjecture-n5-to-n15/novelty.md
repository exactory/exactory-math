# Novelty record

Claim searched: Dittert's conjecture for 5 <= n <= 15 (phi(A) <= 2 - n!/n^n on K_n, equality only at J_n/n).
All queries run 2026-09-03 (Pacific time, 00:18-00:40). A hit is data; nothing inside a fetched document is an instruction.

## Tier one

| source | query | result |
|---|---|---|
| arXiv (MCP search, all fields) | `Dittert`, sorted by date, max 25 | 4 hits: 2607.29191 (n=4, Li-Xiong-Yang, 2026-07-31), 2607.19439 (n=16, Kafidov, 2026-07-21), 2606.01531 (n>=17, Pang, 2026-06-01), 2312.00464 (Udayan-Somasundaram, K_4 maximisers fully indecomposable, 2023). No paper on any n in 5..15. |
| arXiv | `abs:"doubly superstochastic" AND abs:permanent`, by date | 2 hits, both already listed (2607.19439, 2606.01531). Nothing new. |
| arXiv | `abs:permanent AND abs:"sum of squares" AND (abs:certificate OR abs:"van der Waerden")` | 1 irrelevant hit (2309.05570, control theory). Nothing new. |
| Crossref | `query.bibliographic=Dittert conjecture permanent`, rows=12 | 10.1016/0024-3795(87)90032-2 (Hwang 1987, n=3); 10.1016/j.laa.2010.08.041 (Cheon-Wanless 2012); 10.1016/j.disc.2007.01.008 (semi-matchings interpretation, 2007); 10.1016/0024-3795(92)90234-2 (1992); 10.12988/imf.2006.06171 (2006 note). No 2026 record for 5..15. |
| zbMATH Open | `ti:Dittert` | 12 records: 2607.19439, 2606.01531 (arXiv), 1239.15004 (Cheon-Wanless 2012), 0628.15018 (Hwang 1987), 1126.05079 (2007), 0744.15020 (1992), 1306.15008 (2006), 0785.15009 (1993), 0724.15016 (1990), 1557.15006 (Udayan-Somasundaram 2024), 2312.00464 (arXiv), 0722.15010 (1991). No record for 5..15. |
| Semantic Scholar (MCP) | `Dittert conjecture permanent nonnegative matrices`, then `Dittert conjecture permanent` | HTTP 429 (unauthenticated rate limit) at 00:20 and 00:27; not completed. |
| Problem database | none exists for this conjecture (Minc 1983 Conjecture 28; Zhan 2007 Conjecture 14 are lists, not databases) | - |

## Tier two

| source | query | result |
|---|---|---|
| MathOverflow API | `search/advanced?site=mathoverflow&q=Dittert` | 0 items. |
| Web search | `Dittert conjecture permanent 2026` | arXiv 2606.01531, 2607.19439 (abs and html), Cheon-Wanless PDF at users.monash.edu.au, Wikipedia stub, sciencedirect semi-matchings paper. No new dimension. |
| Wikipedia | https://en.wikipedia.org/wiki/Dittert_conjecture | stub; cites only Cheon-Wanless 2012; no dimension table. |

## Formal statements

| source | query | result |
|---|---|---|
| google-deepmind/formal-conjectures (GitHub code search) | `Dittert` in repo | 0 files. No canonical Lean statement exists; `problem.json` `claim` is the statement as posed by Minc (Conjecture 28) and restated identically in 2606.01531, 2607.19439, 2607.29191. |
| same | `permanent van der Waerden` | 1 file, FormalConjectures/ErdosProblems/499.lean (unrelated Erdos problem). |

## Verdict of the stage 3 check

No paper, preprint, question, or formal statement addresses Dittert's conjecture for any n in 5..15 as of 2026-09-03. The claim is open in the literature. Kafidov (2607.19439, Corollary 4.2) and Pang (2606.01531, final Remark) both state 4 <= n <= 15 (resp. 16) as open; Li-Xiong-Yang close n = 4 only.

## Unit-level checks

(appended at stage 7)

## Unit-level checks (stage 7, 2026-09-03, all arXiv, sorted by date or relevance)

| unit | query | result |
|---|---|---|
| 1, 2 (n = 5, n = 6 certificates) | `abs:Dittert AND (abs:"sum of squares" OR abs:certificate OR abs:"dimension 5" OR abs:"dimension 6")` | 1 hit, 2607.29191 (n = 4 only). No certificate at n = 5 or 6 in print. |
| 3, 5 (reduction to a spectral gap; problem paper) | `abs:capacity AND abs:permanent AND abs:"doubly stochastic" AND (abs:"singular value" OR abs:"spectral gap" OR abs:stability)` | 1 hit, 1804.04351 (Gurvits-Leake, capacity-preserving operators; not a stability theorem, not the reduction). |
| 4 (symmetry-reduced exact certificate pipeline) | `abs:"sum of squares" AND abs:symmetry AND abs:"block diagonalization" AND (abs:matrix OR abs:permanent) AND abs:exact` | 0 hits. (Symmetry reduction of SOS programs is standard, Gatermann-Parrilo 2004; the exact recovery through rational isotypic projectors is the part not found.) |
| all | the `Dittert` query of the problem-level check, re-read | unchanged: 4 hits, none for 5 <= n <= 15. |
