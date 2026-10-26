# Unit 1: bounded exact-statement novelty check

Date: 2026-09-08. This cash-out study adds no mathematical move, run or checkpoint.
It supplements the preserved problem-level study in study/problem.md and its
QUERY_LOG.md. The original novelty.md remains the unchanged CP27 snapshot.

## Statement searched

For every nonempty finite set D of distinct integers at least 3 with gcd(D)=1 for which there exist an integer B>=2 and a nonempty finite set A of positive integers such that R={B^a:a in A} is contained in D, sigma(R)=sum_{d in R}1/(d-1)>=1/2, V=D minus R has min V>=4 and sigma(V)>1, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k admit an integer N(D,k,F) such that every integer n>=N is a sum of finitely many remaining occurrences d^j, each pair (d,j) used at most once and coincident numerical values from different pairs retained separately.

## Queries and returned evidence

The following twelve query attempts used the statement's pure-power completeness,
reciprocal-mass and common-radix language. Responses, including errors and unrelated
hits, are saved in study/sources/unit-1-search-responses.json.

1. arXiv: `(all:"powers" AND all:"complete") AND (all:"subset sums" OR all:"Erdos")`. Returned 8 of 13 records. Their titles and abstracts concerned generic subset-sum algorithms, graphs, statistics or computing hardware, not this theorem.
2. Semantic Scholar API: `"powers" AND "complete" AND ("Erdos" OR "subset sums")`. The service returned a rate-limit error. This is unavailable evidence, not a no-hit result. No rapid retry was made.
3. Crossref-domain web index: `common radix powers reciprocal sum complete sequences 1/(a-1)`. No relevant Crossref result was returned.
4. zbMATH-domain web index: `powers complete sequences reciprocal sums Erdos`. Returned the BEGL1996 title, Zbl 0863.11014, through author and collaboration records; unrelated author records were also returned.
5. Erdős Problems domain: `124 powers sums reciprocal 1 a minus 1`. Returned problem124 and its discussion, including the finite-base positive-cutoff problem and the known zero-cutoff distinction.
6. arXiv: `cat:math.NT AND (all:"complete sequences" OR all:"sums of powers") AND (all:"bases" OR all:"Erdos" OR all:"reciprocal")`. Returned 8 of 15 records on other number-theoretic power sums, prime powers, finite fields, digit expansions or polynomial diagonalization. None of the returned abstracts states this criterion.
7. Crossref API, query.bibliographic: `complete sequences integer powers reciprocal common radix`, rows=5. Returned DOI10.4064/aa-77-2-133-138 first. Other hits were DOI10.2307/2689879 and DOI10.1080/0025570x.1976.11976532 (the same 1976 title, Integer Representations and Complete Sequences), DOI10.4236/oalib.1105417 (trigonometric power sums), and DOI10.35834/2005/1702071 (common moments). Only metadata was retrieved for these neighboring records.
8. General web: `"complete sequences" "powers" "common radix"`. No exact theorem was returned. The combined response included an unrelated self-reported exponential-floor sequence study; it is not used as proof or a source of novelty certification.
9. General web: `"powers" "complete" "3/2" "Erdos"`. Returned mostly unrelated graph, polynomial-power and number-theory results. No exact minimum-three all-cutoff result at strict mass above three halves was identified.
10. Semantic Scholar domain fallback: `"complete sequences of sets of integer powers"`. The combined indexed response did not return an exact Semantic Scholar page. This fallback does not repair the unavailable citation-graph search.
11. zbMATH Open API: `ti:complete sequences powers`. Returned three records: BEGL1996 (document918701, Zbl0863.11014), Complete sequences of weighted r-generalized Fibonacci powers (document7350747, Zbl1471.11074), and a license-redacted 1973 record (document3430777, DOI10.1080/00150517.1973.12430811). The first carries a review, with MSC11B83 and11B13. The Fibonacci record carries an abstract/summary about a different recurrence family. The redacted record cannot establish a theorem comparison.
12. arXiv: `all:"complete sequences" AND all:"powers"`. Returned five unrelated records about GUI agents, operator eigenfunctions, generative models, language-model decoding and astronomy. The title/abstract returns did not identify the proposed theorem; their relevance limits the strength of this negative result.

The arXiv responses were not clean mathematical phrase matches, and the first two
arXiv queries were truncated by their requested result cap. No absence claim over their
unreturned records is made. A page-open attempt for each of
https://www.erdosproblems.com/124 and https://zbmath.org/0863.11014 returned an internal
error. The former's indexed content and the latter's successful API record remain
distinct evidence. No error was recorded as a successful full-text read.

## Primary sources and exact comparison

Burr, Erdős, Graham and Li, Complete sequences of sets of integer powers,
Acta Arithmetica77(2),133--138(1996), DOI10.4064/aa-77-2-133-138:
https://doi.org/10.4064/aa-77-2-133-138.
The already saved full six-page primary extraction,
study/sources/begl1996-extracted.txt, was reread in full during this check.
Its Theorem1 starts with an infinite positive-upper-density collection and
selects a finite collection depending on the cutoff. Its other stated results
cover interval-base families and specific small configurations. Those hypotheses
do not prove the present arbitrary fixed finite-D common-radix criterion.
The proof's disjoint gap-reserve and interval construction is acknowledged as
prior method, not claimed as newly invented.

The canonical file is
https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/124.lean,
saved as study/sources/canonical-124.lean. The full105-line file was reread.
Erdos124.erdos124.ne_zero asks for every positive cutoff and every admissible finite
base set with collective gcd one and reciprocal mass at least one. Its pointwise
sum retains independent base choices. The unit preserves those cutoff and label
semantics, strengthens the conclusion by finite deletion, and restricts the
base-set hypothesis to the exact common-radix criterion. The solved zero-cutoff
statement, a particular cutoff-one example, and Melfi's infinite-base construction
are not substitutes for this theorem or the original objective. The known web
denominator typo is not adopted.

The local CP22 common-radix proof and CP26 phase-selection proof are acknowledged
method predecessors. CP22 dedicates an entire nonempty correction-base set and
requires a disjoint mass-one reserve. CP26 gives thickness of the full supply, not
eventual completeness. The present proof rederives its needed elementary lemmas.
It adds one correction occurrence per signed unit while preserving a single gap
constant and cumulative removal ledger. The two explicit comparisons in its
Section7 show inputs outside the older allocation criterion, not external
publication priority.

## Decision and stop

The twelve-query bounded check is complete. No exact prior proof was identified
in the inspected results. The primary comparison does not reduce the structural
claim to a few-line application of BEGL1996 or the earlier local theorems.
This supports retaining one local theorem unit, with its minimum-three
consequence and examples in the same unit. It does not establish exhaustive
novelty, a bibliographic record, peer-reviewed correctness or publication priority.
No standalone paper is being published.

The first-tier floor was attempted for all five prescribed sources. The actual
Semantic Scholar failure, fallback limitation, ranked result caps and weak
arXiv relevance are retained. The study stops at twelve query attempts; no
additional mathematical conclusion is drawn from search behavior.
