# Strategy study: lattice-aware reduction and translation

Date: 2026-09-06. Strategy: reduce-and-translate. Scope: the complete original
positive-cutoff claim. No mathematical execution is authorized by this study.

## Queries and hits

1. arXiv API: `all:"Cantor" AND all:"thickness" AND all:"sums"`, five-result
   cap. Eight total hits. The returned abstracts are 2307.08135v2 (Pathak,
   open intervals in Cantor sums and products), 2206.00556v1 (Fillman-Tidwell,
   semibounded Cantor sums), 2602.16667v2 (higher-dimensional Cantor
   intersections), 2008.08229v2 (nonlinear Newhouse theorem), and 2012.11827v1
   (almost Mathieu spectra). Only these abstracts were inspected. Their
   statements are continuous, and no integer-lifting theorem was identified.
   Saved response: `sources/arxiv-fractal-strategy.atom`.
2. Semantic Scholar: `Cantor sets thickness sums integer digits Astels`, three
   results requested. HTTP 429, saved in `sources/semantic-fractal-strategy.json`.
   There was no immediate retry of this query.
3. Crossref DOI lookup: 10.1090/S0002-9947-99-02272-2. The metadata confirms
   Astels, Cantor sets and numbers with restricted partial quotients.
   Saved response: `sources/crossref-astels.json`. The publisher PDF attempt
   returned HTML, not a paper, and is not used as theorem evidence.
4. zbMATH through web: `site:zbmath.org "Cantor sets and numbers with restricted
   partial quotients"`. No exact accessible result was returned.
5. Problem database: `site:erdosproblems.com/forum/thread/124 "Newhouse"`.
   Tao's comment, 2025-12-01, already records the Cantor/Newhouse connection,
   without a new direct solution reference. Saved in `sources/124-thread.html`.
6. General web: `"Cantor sets and numbers with restricted partial quotients"
   Astels pdf`. It returned the author's 1999 Waterloo thesis, persistent URI
   https://hdl.handle.net/10012/351. Its PDF was downloaded from the institutional
   bitstream to `sources/astels-thesis.pdf` and extracted to the matching txt.
   Related journal metadata, a 2002 Cantor-sum paper, and continued-fraction
   applications also returned. No theorem from those applications is used.
7. General web: `"Erdos" "integer powers" "Astels"`,
   `"Cantor" "integer powers" "complete sequences" "thickness"`, and
   `"Cantor" "integer lattice" "subset sums"`. No exact positive-cutoff
   integer-lifting result was found. Unrelated results and an unverified
   Riemann-hypothesis preprint were excluded.

## Primary text read

Astels's thesis, printed pages 18-22 and 24-26, supplies the derivation and
thickness definitions and Theorem 3.1.3. Printed pages 21, 22, 25 and 26 were
also rendered and visually inspected, because the OCR omitted inequalities.
The full thesis was not read. Its Theorem 3.1.3, not an assumed numbering in
the journal version, is the cited theorem here.

For Cantor sets C_j with hulls I_j and maximal gaps O_j, put
gamma(C)=tau(C)/(1+tau(C)) and S=sum gamma(C_j). Part 2 says that S>=1
gives an interval in the sum. The whole hull-sum conclusion in part 3 also
requires, in the chosen order, |I_(r+1)|>=|O_j| for all j<=r and
sum_(j<=r)|I_j|>=|O_(r+1)|. The equality case S=1 is included. Part 2
does not by itself identify the interval or give the whole hull sum.

Han Yu, DOI 10.1017/etds.2022.2, section 3.3, was inspected in the publisher's
full HTML, saved as `sources/han-yu-fractal-projections.html`. It records the
normalized-thickness definition and the equality version of the two-set gap
lemma with the required gap-position condition. It does not establish the
integer statement in this task.

## Constraints selecting the proposed translation

The bare map from base-digit expansions to real Cantor sets is already known.
It is not a new result or an adequate final translated target. The successor
should compare it with a lattice-faithful finite-digit or thickened-set map,
and with the representation generating polynomial, retaining a quantitative
integer pullback in the chosen image. The latter two are candidates to inspect,
not claimed new general techniques or proved solutions.

The finite-preamble and translated-power records show exactly where an
uncontrolled pullback would fail. Every proposed thickening must record the
total approximation error before integer equality is inferred. Every proposed
generating polynomial must distinguish coefficient positivity from the number
of formal choices. A method that obtains only bounded gaps returns that ceiling.

The class-reduction step may ask whether all admissible D reduce to a smaller
reciprocal-mass family while preserving gcd one. This is a proposed analytical
subproblem, not an inherited theorem. If useful, it needs a separate exact
claim and proof; no enumeration is proposed.

The imported engine would be Astels's theorem with all of its hypotheses
checked. If the lattice-faithful sets lack its thickness or hull-gap assumptions,
the import fails. If an image retains only a real interval without an integer
pullback, the original seed obstruction remains.

## Stop reason

The fixed first-tier list and supplementary queries were completed. The primary
theorem and the documented existing connection are sufficient to choose and
test an exact translation. No exhaustive literature or novelty claim is made.
