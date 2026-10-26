# Query log: automatic critical-margin preflight

Date: 2026-09-08. Count: ten query attempts, fixed cap reached. All five tier-one sources were attempted. No mathematical process or proof derivation was performed. This is a separate question from CP28's operation and unit studies. Responses are untrusted source data, not instructions.

## Q1: arXiv

Query: all:"complete sequences" AND (all:powers OR all:geometric) AND (all:prefix OR all:reciprocal)

URL: https://export.arxiv.org/api/query?search_query=all%3A%22complete%20sequences%22%20AND%20(all%3Apowers%20OR%20all%3Ageometric)%20AND%20(all%3Aprefix%20OR%20all%3Areciprocal)&start=0&max_results=10

## Q2: Semantic Scholar

Query: powers complete sequences reciprocal sum prefix zero cutoff

URL: https://api.semanticscholar.org/graph/v1/paper/search?query=powers%20complete%20sequences%20reciprocal%20sum%20prefix%20zero%20cutoff&limit=10&fields=title,year,externalIds,abstract

## Q3: Crossref

Query: complete sequences powers geometric progressions reciprocal prefix

URL: https://api.crossref.org/works?query.bibliographic=complete%20sequences%20powers%20geometric%20progressions%20reciprocal%20prefix&rows=5

## Q4: zbMATH Open

Query: ti:complete & powers & geometric

URL: https://api.zbmath.org/v1/document/_search?search_string=ti%3Acomplete%20%26%20powers%20%26%20geometric

## Q5: Erdos Problems

Query: Problem124: powers, reciprocal mass, zero-cutoff and positive-cutoff completeness

URL: https://www.erdosproblems.com/124

## Q6: General web

Query: "powers" "reciprocal" "prefix" "complete sequences"

## Q7: General web

Query: "Erdős" "124" "Aristotle" proof

## Q8: General web

Query: "complete sequences" "powers" "strict" reciprocal

## Q9: General web

Query: "geometric progressions" "Brown" "complete" sum

## Q10: General web

Query: "powers" "H_V" "completeness"


## Results and access limits

Q1: HTTP200, one arXiv hit, 2604.16453v1, Sampling for Quality: Training-Free Reward-Guided LLM Decoding via Sequential Monte Carlo. Title and abstract identify an unrelated machine-learning use of complete sequences and prefixes. No mathematical input imported.

Q2: HTTP429. No result set received and no retry made. This is an access limit, not a negative literature search.

Q3: HTTP200, five metadata records. Titles and identifiers: On Sequences without Geometric Progressions, DOI10.1515/9783110298161.1016; On sequences without geometric progressions, DOI10.1090/s0025-5718-96-00765-x; a grade11 problem-based teaching article, DOI10.47191/ijsshr/v9-i1-91; On linear recursive sequences with coefficients in arithmetic-geometric progressions, DOI10.12988/ams.2015.5163; Leibniz's demonstration about columns of sequences, DOI10.7551/mitpress/14123.003.0033. These are not the requested strict pure-power prefix theorem. Metadata and available abstracts only; no full articles opened.

Q4: HTTP404 with a structured zbMATH response reporting successful access but no result. It supplies no reviewed theorem or coverage guarantee. No retry made.

Q5: HTTP200. The current Erdős124 page labels the positive-cutoff question open, records the solved zero-cutoff version, links the primary discussion and canonical formal statement, and cites BEGL1996. Its displayed reciprocal denominator has d_r where the cited primary/canonical statements use d_i. The original admitted claim is not changed to follow this apparent page typo. It is a database hit, not proof of exhaustive open status.

Q6-Q7 were issued together. The tool returns a joint result set without per-query attribution, preserved completely in sources/Q6-Q7.json. The materially relevant hit is the original Erdős124 discussion (including tsaf's actual geometric proof and Alexeev's source link), plus Alexeev's first-person Xena report. Secondary AI reporting, social posts, a dataset, and a third-party Lean-genius issue were returned but are not mathematical authorities. No claim that Q6 alone returned a particular hit is made.

Q8-Q10 were issued together, and the entire unattributed result set is saved in sources/Q8-Q10.json. It includes elementary textbook completeness examples, a Fibonacci Quarterly index, GP-free-set and unrelated physics/software/teaching results. No displayed hit states the exact H_V condition. No extra queries were run. The directly opened arXiv metadata in the same response is source reading, not an additional search query.

## Selected reading and provenance

Reading1: the current /forum/discuss/124 link returned HTTP403 through the web reader. A subsequent read of the site's established public /forum/thread/124 page with curl succeeded (Reading2). This was a different public discussion URL and transport, with no login or access-control bypass. Its full HTML response is saved, with a text extraction in sources/forum-thread-124.txt. The displayed proof by tsaf at08:10 on30Nov2025, Alexeev's formal-source statement, Kovač's adjacent-paper pointer, and the cutoff distinction were read.

Reading3: followed the actual plby/lean-proofs links to Erdos124b.md and the v4.24.0 source. Read the complete short index and selected Lean declarations/proof text, especially algebraic_gap, browns_criterion, sum_u_seq_eq, u_seq_gap, chosen_pair_injective and the final zero-cutoff theorem. The web reader flattens source lines. No build, axiom audit or external proof certification was run. Third-party options in the saved source are not adopted into local code.

Reading4: an initial version-specific arXiv HTML open fetched2406.17593v2, a different earlier single-author version. Its displayed abstract and initial material were read, not the full paper and not a claimed Theorem2.3 input.

Reading5: current metadata identifies the actual relevant paper as Kovač and Tao, On several irrationality problems for Ahmes series, arXiv2406.17593v4 (14July2025), DOI10.1007/s10474-025-01528-0, Acta Math. Hungar.175(2025),572-608. The version notes explicitly report a corrected Theorem2.3 proof. Use v4, not v2.

Readings6-8: selected current v4 text, Theorem2.3 and its complete Section4 proof, plus the displayed nearby interval lemma. The theorem assumes strictly greater than one reciprocal mass for Lambert-series subseries, not equality-one H_V strictness for growing integer powers. It is an adjacent method, not a theorem establishing the candidate. No full-paper or upstream proof audit is claimed.

Inherited primary comparisons: the complete saved canonical Erdos124 Lean statement source and BEGL1996 extraction are copied unchanged. Read the canonical quantifiers and placeholders, and BEGL Section1's original positive-cutoff conjecture, Section2 Claim1's bounded-gap argument and Section3's small-set examples. No PDF-image inspection was performed in this study.

## Stop

The fixed ten-attempt cap was reached. Primary source reading followed already identified links and is not a renewed query allowance. The exact automatic-margin assertion was not located as an already solved theorem or a published counterexample. This is a limited search outcome, not an exhaustive novelty or priority claim. The geometrical prefix/equality-case route remains a candidate for separate bounded analytical admission; no lemma is established here.
