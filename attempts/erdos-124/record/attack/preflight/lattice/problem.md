# Problem study for a lattice-aware pure-power successor

Date: 2026-09-06. Proposed scope: exactly the original positive-cutoff Erdős 124
claim, over every admissible finite D and every positive k. This is a new
method after checkpoint-000005, not a new objective or a budget renewal.

## Queries

1. arXiv API: `all:"integer powers" AND all:"complete"`, five-result cap.
   Thirty total hits, of which the first five were inspected at metadata and
   abstract level: 2507.13402v2, 0910.0244v3, 1905.03374v2, 1505.05362v1,
   and 2311.10330v1. None establishes this completeness claim. The first is
   marked withdrawn by its author. Response: `sources/arxiv-fractal-problem.atom`.
2. Semantic Scholar: `integer powers complete sequences Cantor seed`, three
   results requested. HTTP 429; no immediate retry. The saved response is
   `sources/semantic-fractal-problem.json`.
3. Crossref: `Complete sequences of sets of integer powers`, three-result cap.
   BEGL96, DOI 10.4064/aa-77-2-133-138, is the relevant existing source.
   Other metadata hits are DOI 10.1007/springerreference_57603 and
   DOI 10.2307/2689879. No theorem from the latter two is imported.
   Response: `sources/crossref-fractal-problem.json`.
4. zbMATH through web: `site:zbmath.org "Complete sequences of sets of integer
   powers"`. The author index and a collaboration index identify BEGL96,
   Zbl 0863.11014. No additional theorem is supplied by these index entries.
5. Problem database: `site:erdosproblems.com/124 "Cantor"`. The discussion
   records a connection to Newhouse's gap lemma in Tao's 2025-12-01 comment.
   This connection was already suggested and must not be called a new discovery.
   The source copy is `sources/124-thread.html`, at its Newhouse paragraph.

## Canonical statement and already known results

The saved current formal source `sources/124.lean` was reread. The declaration
`Erdos124.erdos124.ne_zero` quantifies over k!=0 in Nat, finite D, d>=3,
sum (d-1)^(-1)>=1, gcd(D)=1, and eventual membership in the Minkowski sum of
the distinct-power sets. It is marked research open and contains sorry.
The zero-cutoff result is a different declaration. Empty summands are allowed,
and equal values from distinct base-exponent pairs are separate choices.
The proposed claim preserves each of these quantifiers and conventions.

BEGL96, DOI 10.4064/aa-77-2-133-138, and Bergelson-Simmons,
arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016, were read in the preceding
studies. Their saved PDFs and extracts remain the primary evidence. The former
gives bounded gaps and explicitly recorded cutoff-1 examples; the latter gives
a sufficient strong-completeness theorem using multiple disjoint supplies.
Neither has been asserted to prove all admissible D and all k.

The original root record separates conditional interval extension from seed
existence. C1 move 1 proves finite-preamble lifting. C1 moves 2 and 3, preserved
by checkpoint-000005, exclude initialization from divergent surplus and the
specified abstract arithmetic inputs alone. The translated-power example is
not an original-problem counterexample. These local arguments have independent
reviews where recorded, but no controller proof acceptance.

## Constraints on this successor

The new task must retain the pure-power digit sets and their integer lattice.
A continuous interval, an entropy count of labelled choices, or complete
residue coverage is not an integer-coverage theorem. Any translated statement
must have a proved pullback, with truncation error and repeated labels explicit.
Any narrower family or auxiliary lemma requires its exact branch scope rather
than replacing this full claim. The method study supplies the relevant Cantor
theorem and its additional size hypotheses.

## Stop reason

The fixed first-tier query list was completed. No solution to the exact
positive-cutoff problem was located. This is a bounded literature check, not
a certification of novelty or openness.
