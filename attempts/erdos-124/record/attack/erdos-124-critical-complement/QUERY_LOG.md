# Critical-complement preflight query log

Date: 2026-09-08. Planning authority: independent strategy assessment7, submitted at revision411. Maximum:12 query attempts, reached. No mathematical process or proof move ran.

## Queries

| Attempt | Source | Exact query or API terms | Result and use |
| --- | --- | --- | --- |
| 1 | General discovery | "Linear forms in two logarithms and Schneider" "II" Mignotte Waldschmidt | Author bibliography and primary journal records located. |
| 2 | arXiv domain | "linear forms" "two logarithms" powers | Yamada1906.00419 and application papers; returned abstracts do not directly supply the needed real positive power estimate. |
| 3 | Erdos database domain | "complete sequences" "integer powers" "124" | No relevant hit identifiable in the returned combined response. This is not an API success or proof of no literature. |
| 4 | Semantic Scholar API | Linear forms in two logarithms Schneider II | Response code429, not a no-hit result. |
| 5 | Crossref API | Linear forms in two logarithms and Schneiders method II | Five records, including exact MW1989 DOI10.4064/aa-53-3-251-287. |
| 6 | zbMATH Open API | ti: "Linear forms in two logarithms" | Eleven records; MW1989 id4045848, Zbl0642.10034, carries a review. Laurent and Gouillon-related primary leads were retained. |
| 7 | arXiv domain | "powers" "complete sequences" "reciprocal" "critical" | No relevant exact critical-complement result identified in the combined response. |
| 8 | Semantic Scholar API | complete sequences powers critical reciprocal mass | Distinct later request again returned429; no further request was made. |
| 9 | Crossref API | complete sequences sets integer powers critical mass | Five records; BEGL1996 DOI10.4064/aa-77-2-133-138 and unrelated or older completeness records. No exact criterion theorem identified. |
| 10 | zbMATH Open API | ti: "complete sequences" & "powers" | BEGL1996 id918701 with author review, weighted Fibonacci paper and a license-unavailable item. No exact criterion theorem identified. |
| 11 | Erdos database domain | "124" "powers" "3/2" | No relevant hit identifiable in the combined response. |
| 12 | General discovery | Dirichlet simultaneous approximation theorem infinitely many q pigeonhole proof pdf | Classical theorem statements and primary Fishman-Simmons2017 article found; its Section1 theorem and corollary were read. |

Attempts2--6 constitute the quantitative-operation source pass;7--11 constitute the critical-completeness source pass. These are bounded broad statement/object searches, not exhaustive exact-formula or priority searches. The newly formulated explicit H_V-margin criterion was not found in those inspected results; it is not asserted novel on this basis alone. It requires its own exact claim review, and any produced unit requires its unit-level novelty check.

All actual responses are saved under sources/ as criticalStudyBatch1/2, criticalAPI4/5/6/8/9/10 and criticalPrimaryOpen1--4. Primary title and DOI navigation and text reads are retrievals of hits, not further search queries. No unseen paper was classified as fully read.

## Primary reading boundaries

1. BEGL1996, the full existing immutable extracted text, digest bee3747819fd4f0eb806190666cca0cb2dd57ada40d972d8b0848e8a8ed8b93d, was reread. Page137 identifies the two-logarithm approach and its fixed-cutoff examples. It does not prove the new all-cutoff criterion.
2. MW1989, DOI10.4064/aa-53-3-251-287: Crossref exact metadata, zbMATH review, author bibliography entry and IMPAN publisher record were inspected. The publisher's download click failed, and EuDML returned403. The full primary theorem was not obtained from this paper. The review is a discovery aid, not a proof premise.
3. Nicolas Gouillon, Explicit lower bounds for linear forms in two logarithms, Journal de theorie des nombres de Bordeaux18(1)(2006),125--146, DOI10.5802/jtnb.537. The canonical Numdam PDF https://www.numdam.org/article/JTNB_2006__18_1_125_0.pdf was accessible through the document reader. Full introductory definitions and Section2 through Corollary2.3, including Corollary2.2 and its setup, were read in the extracted text. Corollary2.4 and subsequent proof excerpts were displayed for context but are not selected inputs. The full23-page proof was not independently checked. Exact relevant response is criticalGouillonReading2.json.
4. Lior Fishman and David Simmons, Unconventional height functions in simultaneous Diophantine approximation, Monatshefte fuer Mathematik182(2017),577--618, DOI10.1007/s00605-016-0983-0. Publisher HTML Section1, displayed lines85--104, states the classical simultaneous Dirichlet theorem and its irrational-vector corollary. The max-norm convention at87 was read. The nonstandard-height results are not imported.
5. Classical lecture notes in the discovery response were not chosen as proof premises. Their displayed extraction includes apparent typographical errors, so no proof is copied from that snippet.

## Access and image limitations

The first Gouillon PDF URL failed, and the canonical /article/ URL succeeded. Document-reader screenshot requests for PDF indices2,3,4 returned only text references in this session, with no inspectable image payload. A direct curl download with an output path was rejected by the managed-shell hook before execution; it was not retried through a wrapper, and the following renderer commands in that script never ran. No local PDF, raster image, visual formula check, or full PDF text extraction is claimed. The exact selected mathematical statements are available in the text extraction and must be restated with their explicit hypotheses. Saved source responses preserve what was actually returned.

## Stop and constraint

The fixed12-attempt cap was reached. Two Semantic Scholar requests failed due to throttling; empty combined domain results were not classified as exhaustive negative evidence. The searches supplied a published quantitative logarithm estimate and a classical simultaneous approximation input. They did not establish the unshifted integer margin, its nonvacuity on a new critical input, or the preservation law after a correction. Those are research obligations for separately reviewed claims.
