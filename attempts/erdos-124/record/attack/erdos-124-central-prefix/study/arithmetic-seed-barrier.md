# Supplementary study: arithmetic conditions and seed production

Date: 2026-09-06. This supplements the admitted strengthening strategy. It does
not change the C1 claim, grant finite execution, or certify novelty.

## Exact neighbouring question

For a nondecreasing, locally finite sequence of labelled positive integers of
bounded numerical multiplicity, do the following four conditions imply eventual
central-prefix coverage: prefix surplus S_m-a_(m+1) tends to infinity; every tail
has gcd one; every irrational alpha has divergent sum of squared distances
||a_i alpha||^2; and the raw label exponent
liminf log(2) #{i:a_i<=X}/log(X) is greater than one?

This is an abstract proposed seed principle, G, not a restatement of C1.
Together with divergent surplus its conclusion would supply a joint seed and
future extension bound. The pure-power structure is deliberately dropped to
test whether the proposed numerical and arithmetic inputs suffice by themselves.
No assertion that all C1 instances already satisfy every G hypothesis is made.

## Queries

All queries below were run on 2026-09-06.

1. arXiv API: `all:"complete sequences" AND all:"digit"`, five-result cap.
   Zero results. Saved as `sources/arxiv-c1-barrier.atom`.
2. Semantic Scholar API: `complete sequences digit sum powers`, five-result cap.
   HTTP 429. Saved as `sources/semantic-c1-barrier.json`. No immediate retry.
3. Crossref: `complete sequences digit sum powers`, three-result cap.
   Metadata hits: Characteristic digit-sum sequences,
   DOI 10.1007/s12095-017-0256-3; Integer Sequences for the Sum of Powers of
   Trigonometric Values, DOI 10.4236/oalib.1105417; Complete Sequences of
   Fibonacci Powers, DOI 10.1080/00150517.1973.12430811.
   Only metadata was inspected. No theorem from these papers is used.
   Response: `sources/crossref-c1-barrier.json`.
4. zbMATH through web search: `site:zbmath.org "complete sequences" "powers"`.
   The author index returned BEGL96, Zbl 0863.11014, already studied.
5. Problem database through web search:
   `site:erdosproblems.com/124 "sum" "powers"`.
   The existing problem and discussion returned. The cutoff-zero distinction
   and the denominator transcription issue remain as recorded in the original
   study. The live source copies from this session are retained under sources.
6. General web: `"complete sequences" "digit sum"`. No exact relevant hit.
7. General web: `"q^n+1" "complete" "sequence"` and
   `"2^n+1" "subset sums"`. No source establishing this exact G principle or
   the intended counterexample was located. General subset-sum papers and
   r-completeness references returned, but no theorem from them is imported.

## Primary sources inspected and constraints

Bergelson and Simmons, arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016,
Theorem 2.1 and Remarks 2.3 through 2.10, have been read in the saved full text.
They separate growth, irrational nonconcentration, and modular coverage and
require disjoint supplies in their sufficient theorem. The proposed G removes
that resource separation and replaces its growth input with one surplus bound.
It must therefore be tested rather than attributed to their theorem.

BEGL96, DOI 10.4064/aa-77-2-133-138, was read in the earlier studies. Its
bounded-gap and residue arguments do not give central-prefix seed production.
The study does not certify the novelty of an elementary digit-sum example.

## Stop reason

The fixed query list above was completed. The statement-specific first-tier
floor was attempted, including the unavailable Semantic Scholar endpoint.
There is enough primary-source context to test G by an explicit analytical
construction, without a numerical search or an additional literature survey.
