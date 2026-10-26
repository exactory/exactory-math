# Unit 1 novelty check

Date: 2026-09-08. Stage 7 after accepted checkpoint-000028 and the native closing cash-out rule.

## Exact statement

For every nonempty finite set D of distinct integers at least 3 with gcd(D)=1 for which there are an integer B>=2 and a nonempty finite set A of positive integers such that R={B^a:a in A} is contained in D, sigma(R)=sum_{d in R}1/(d-1)>=1/2, and V=D minus R has min V>=4, sigma(V)=1, contains multiplicatively independent integers a,b, and satisfies H_V(x)>x for every real x>1, where p_d(x) is the least nonnegative integer power of d at least x and H_V(x)=sum_{d in V}(p_d(x)-1)/(d-1), every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit an integer N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each labelled pair used at most once and coincident numerical values retained separately.

## Bound and reading discipline

Run at most seven source query attempts for this exact unit and its cutoff-one and strict-complement neighbours: one each at arXiv, Semantic Scholar, Crossref, zbMATH Open and the Erdős problem database, followed by at most two statement-based web searches. Stop at that fixed count or after the tier-one floor and two consecutive queries produce no new relevant result. Network failure is recorded, not counted as a negative literature finding. Reading a returned primary source is not a new search. No mathematical program, formal verification or publication is authorized. This required unit-level check is distinct from the completed twelve-attempt proposal preflight and does not reset that cap.

Primary query terms: complete sequences powers common radix reciprocal sum critical complement arbitrary exponent cutoff finite deletion.

## Queries and results

### U1: arXiv

Query: all:"complete sequences" AND all:powers AND all:cutoff

URL: https://export.arxiv.org/api/query?search_query=all%3A%22complete%20sequences%22%20AND%20all%3Apowers%20AND%20all%3Acutoff&start=0&max_results=10

Date: 2026-09-08.

Result: The browser retrieval service refused this API URL as unsafe to open. This is a retrieval failure, not a zero-hit source result.

Raw response: sources/U1.json.

### U2: Semantic Scholar

Query: complete sequences powers common radix reciprocal sum critical complement exponent cutoff

URL: https://api.semanticscholar.org/graph/v1/paper/search?query=complete%20sequences%20powers%20common%20radix%20reciprocal%20sum%20critical%20complement%20exponent%20cutoff&fields=title,year,externalIds&limit=5

Date: 2026-09-08.

Result: The browser retrieval service refused this API URL as unsafe to open. This is a retrieval failure, not a zero-hit source result.

Raw response: sources/U1.json.

### U3: Crossref

Query: complete sequences powers common radix reciprocal sum critical complement arbitrary exponent cutoff finite deletion

URL: https://api.crossref.org/works?query.bibliographic=complete%20sequences%20powers%20common%20radix%20reciprocal%20sum%20critical%20complement%20arbitrary%20exponent%20cutoff%20finite%20deletion&rows=5

Date: 2026-09-08.

Result: The browser retrieval service refused this API URL as unsafe to open. This is a retrieval failure, not a zero-hit source result.

Raw response: sources/U1.json.

### U4: zbMATH Open

Query: ti:"complete sequences" powers cutoff

URL: https://api.zbmath.org/v1/document/_search?search_string=ti%3A%22complete%20sequences%22%20powers%20cutoff

Date: 2026-09-08.

Result: The browser retrieval service refused this API URL as unsafe to open. This is a retrieval failure, not a zero-hit source result.

Raw response: sources/U4.json.

### U5: Erdos Problems

Query: Problem124 powers reciprocal sum at least one every positive cutoff, current statement and results

URL: https://www.erdosproblems.com/124

Date: 2026-09-08.

Result: HTTP403, no current database statement was retrieved. This is not evidence that the problem is open or solved.

Raw response: sources/U4.json.

### U6: General web search

Query: "complete sequences" "powers" "cutoff"

URL: Web search interface; exact string above.

Date: 2026-09-08.

Result: The joint U6/U7 response contains related and unrelated hits, saved in full. Its combined display does not supply a reliable per-query hit partition; no exact hit count is asserted.

Raw response: sources/U6.json.

### U7: General web search

Query: "powers" "reciprocal" "complete" "3/2" Erdős

URL: Web search interface; exact string above.

Date: 2026-09-08.

Result: The joint U6/U7 response contains related and unrelated hits, saved in full. Its combined display does not supply a reliable per-query hit partition; no exact hit count is asserted.

Raw response: sources/U6.json.

## Hits worth reading and exact limits

The primary publisher page for Jacek Marchwicki, Achievement Sets of Reciprocals of Complete Sequences (2023), DOI10.1007/s00025-023-01941-3, was opened. The displayed abstract and Sections1-2 were read, not an independently verified full paper. It concerns achievement sets of reciprocal sequences. Its recalled prefix criterion is background for an elementary induction already proved here, not the exact all-cutoff critical-complement result. Saved response: sources/reading-1.json.

The MathOverflow index returned a question titled Sums of distinct powers of 3, 4 and 7 and attributed it to G. Melfi. Only the index excerpt was inspected at https://mathoverflow.net/questions/tagged/analytic-number-theory?page=5&tab=active. The individual question and answer were not read and no theorem is imported from them. The related primary BEGL1996 paper is already completely available in ../sources/begl1996-extracted.txt and was read earlier. The small-set cutoff-one overlap is explicit in the accepted proof Section9.

The joint response also includes Graham's finite reciprocal-power sums paper, DOI/source https://msp.org/pjm/1964/14-1/pjm-v14-n1-p10-s.pdf, and the survey Paul Erdos and Egyptian Fractions at https://mathweb.ucsd.edu/~ronspubs/13_03_Egyptian.pdf. Only returned excerpts were inspected. They concern reciprocal sums or multiplicative closures rather than this exact finite fixed-base power-tail statement. No full-text reading or applicable theorem is asserted.

The remaining displayed hits, including educational powers pages, unrelated matrix and algebraic-variety papers, general AI-result aggregators and other Erdos problem reports, remain recorded with their URLs and snippets in sources/U6.json. They supply no exact primary theorem for this unit and were not used as mathematical evidence. In particular an aggregator's open/solved label is not an authoritative status check.

## Constraints on this unit

The problem-level study is ../problem.md; its twelve-attempt preflight and source-reading boundaries remain unchanged. CP27/acceptance14 covers a strictly supercritical complement. CP28's result uses quantitative power separation and a sign-controlled actual-period recurrence to treat the stated equality subclass. These substantive missing interfaces are not supplied merely by a classical bounded-gap induction.

BEGL1996, DOI10.4064/aa-77-2-133-138, Section3 already covers the example's cutoff-one conclusion via its subset {3,4,5}. The example at that cutoff is not novel. The new local coverage is the exact all-k, finite-deletion theorem outside every earlier CP27 radix witness, as proved in move1 Section9. The additional strict H_V hypothesis is retained. The finite test and example belong to this same theorem, not independent units or checkpoints.

This bounded check identified no prior exact theorem. Access failures at every tier-one endpoint severely limit the new search. The prior saved primary problem/strategy studies, the exact theorem comparison and the new primary publisher reading support retaining one nontrivial local full-proof unit, but do not establish exhaustive literature novelty, priority or readiness to publish.

## Stop reason

The fixed seven-attempt cap was reached, including one attempt at each tier-one source. No query was retried and no source failure was relabelled as a negative result. Primary reading added no query and no mathematical execution. The selected result remains a local research artifact; no external submission or publication is made.

