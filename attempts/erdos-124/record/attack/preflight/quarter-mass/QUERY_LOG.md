# Quarter-mass preflight query log

Date: 2026-09-07 UTC.
This is a source and proposal study, not a mathematical proof.
Fixed limit: one query in each first-tier source for the problem and
the selected construction strategy, with up to five arXiv results,
up to five citation-graph results, and the saved primary readings.

## Problem floor

1. arXiv: ("complete sets" OR "complete sequences") AND ("integer powers" OR "reciprocal" OR "three-component").
The five returned abstracts concerned efficient reciprocal matrices,
Hamilton-Jacobi separation, photonic gates, R26 flow, and quasilattices.
They do not address the claimed completeness threshold. The result
bound was reached, with ten other results not fetched.
2. Semantic Scholar: "complete sequences" "integer powers" reciprocal.
The response was rate limited. No retry or successful lookup is claimed.
3. Crossref-targeted indexed query:
site:api.crossref.org "Complete sequences of sets of integer powers".
No relevant registry record returned.
4. zbMATH-targeted indexed query:
site:zbmath.org "New examples of complete sets".
No relevant record returned in this batch.
5. Problem database indexed query:
site:erdosproblems.com/124 "reciprocal".
A secondary saved problem-list mirror returned the familiar zero-cutoff
result, positive-cutoff problem and BEGL96 reference. Several unrelated
Erdos problem pages were also returned. They are not theorem inputs.
Additional exact-threshold discovery:
"complete sequences of sets of integer powers" "13/4".
No exact claimed threshold appeared in the returned hits.

The complete raw responses are sources/problem-0.json through
sources/problem-2.json. The wide search's irrelevant results are
reported, not converted into evidence of absence.

## Strategy floor

1. arXiv: ti:"Strongly Complete" OR ti:"New examples of complete sets" OR (ti:"bin covering" AND abs:"small").
Five of six abstracts returned. Relevant: Bergelson-Simmons,
1507.02208v2; Fan, 2607.14071v3. The bin-covering migration paper
1904.06543v1 concerns competitive online algorithms, not the proposed
gcd-preserving reciprocal allocation. Coalgebra and MV-algebra papers
are irrelevant. No theorem is imported from those three.
2. Semantic Scholar: "New examples of complete sets" partition.
Rate limited, with no retry.
3. Crossref exact DOI lookup:
https://api.crossref.org/works/10.4064/aa8221-10-2016.
The web reader returned an internal error, not a successful new record.
The existing checked DOI and source bytes remain inherited evidence.
4. zbMATH indexed query:
site:zbmath.org "Bergelson" "Simmons" "complete".
Returned the author profile identifying Zbl 1435.11021 and the 2017 paper.
5. Problem database indexed query:
site:erdosproblems.com "124" "3.25".
No exact matching threshold returned.
Additional strategy discovery:
"reciprocal" "gcd" "complete sets" powers partition.
Returned unrelated coding, algebra and medical material, not a new
construction theorem. No such material constrains the mathematics.

Raw responses: sources/strategy-0.json through sources/strategy-2.json.
All returned abstracts and available response text were read.
The fixed query count was reached. No more broad searches are planned.

## Primary and accepted evidence inspected

Bergelson-Simmons, DOI 10.4064/aa8221-10-2016, arXiv1507.02208v2:
the full locally saved paper was read in the predecessor work. Its
Theorem1.23, multiset footnote, Section2.7, and Section2.1 completeness
mechanism were checked there. The source remains sources/bergelson-simmons.txt
under the research root, pinned by acceptance-000005's manifest.

Fan, arXiv2607.14071v3: the complete Section2 finite-correction argument
and Corollaries2.3/2.5 were read for the accepted predecessor. The
introduction and method/optimal-constant discussion were reread in this
preflight. The numerical-set criterion requires the explicitly proved
occurrence extension in the accepted predecessor; repeated values
cannot be silently deduplicated.

Local accepted core proof: attack/erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md,
read in full again. It gives a gcd-descent seed below mass one and
augmentation below 1+1/m, not the new conjectured 9/8 bound.

Local accepted high-mass proof: attack/erdos-124-mass-partition/moves/001-high-mass-completeness.md,
read completely during its proof and review, with Sections1-3 reread
in this preflight. Acceptance-000005 at checkpoint-000016 pins the
whole occurrence-preserving criterion and all-cutoff application.
No new numerical proof or enumeration has run.

The original formal statement was checked in the predecessor's
canonical-124-reading.txt. The present claim preserves its finite
base set, distinct bases, collective gcd, all positive cutoffs, and
label conventions, strengthens deletion robustness, and restricts
the reciprocal-mass range. It does not settle the root.

