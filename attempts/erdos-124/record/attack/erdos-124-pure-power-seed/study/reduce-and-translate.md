# Strategy study: preserve the integer coefficients

Date: 2026-09-07. Strategy: reduce-and-translate.
Target: fixed-loss central seeds at arbitrarily late pure-power prefixes.

## Queries and hits

The first-tier strategy sweep queried arXiv for complete sequences and Fourier,
Semantic Scholar for complete sequences, Cassels and Fourier, Crossref for
Cassels and distinct-summand representations, zbMATH for Cassels's representation
paper, and the problem database through a site-restricted Fourier query.
Exact requests, failures and response paths are in sources/queries.md.

The arXiv query returned an unrelated Fourier Image Transformer paper
(arXiv:2104.02555v3), excluded after its abstract. Semantic Scholar again
returned 429 after a later separate request; no further API retries are planned.
The fallback site-restricted search surfaced Erdos's 1962 discussion of Cassels,
DOI 10.4064/aa-7-4-345-354, but that paper was not read in full and is not an
imported theorem. Crossref resolved that neighbouring title, not Cassels's
exact paper. zbMATH document 3345481 supplies the latter's metadata and review.

The primary sources actually inspected are the existing Bergelson-Simmons
Section 2 and Fan 2026 Sections 1-2. The exact identities and statements
selected for inspection are described in problem.md. The problem database
still distinguishes the solved zero-cutoff assertion from the positive-cutoff
question. No Fourier solution of the exact latter target was found.

## What the sources constrain

1. Cassels's route studies coefficients of a distinct-summand generating
   function using the circle method. Its known sufficient density condition
   is absent for a fixed finite collection of exponentially spaced streams.
   A direct citation of that theorem would stop at an unmet hypothesis.
2. The Bergelson-Simmons and Fan arguments retain exact integer sums through
   disjoint supports and Bohr-set coverage. Their required component supplies
   are not furnished by total reciprocal mass at least one. A finite-support
   refinement does not eliminate all the remaining component hypotheses.
3. A real-image or dimension argument is insufficient unless it controls the
   original integer lattice at the required scale. The earlier real-image
   attack already recorded that failure, so simply repeating it is excluded.
4. A finite polynomial product, and equivalently its exact Fourier coefficient
   or an exponentially tilted Bernoulli sum, retains the labelled lattice.
   These are prospective representations of the same problem, not a supplied
   positivity theorem. Support, coefficient multiplicity, and probability mass
   must be distinguished. Zero Fourier modes or a large total number of
   labelled subsets do not suffice.

## Selected plan and its proof obligations

At the strategy's first mathematical move, compare exact finite polynomial
coefficients, a tilted lattice probability distribution, and the earlier
real-image formulation. Prefer the exact-coefficient image if it supplies a
usable route; reject a surrogate that loses the integer conclusion.

State the full image claim with fixed loss and unbounded prefix quantifiers,
prove its pull-back, and attempt a rigorous coefficient lower bound using the
actual powers. Test the applicability of any local-limit approximation before
using it. Preserve the exact problem if Gaussian or uniform Fourier heuristics
fail; do not turn their failure into a counterexample to the power conjecture.
Later plan steps may attach a coefficient or probability object, isolate a
precise still-missing estimate, and import an applicable engine only after all
of its hypotheses have been checked. Follow the native entry failure signals;
the admission does not authorize a predetermined list of unjournalled lemmas.

The prospective output is an analytical proof or a precise new residual
obligation, with a checked relation to the seed. No endpoint loss depending on
the prefix, unbounded-prefix computation, or renewal is admitted. The account
is inherited unchanged. A tautological coefficient restatement alone is not
qualifying root progress.

## Stop reason

The fixed five-source strategy sweep and focused fallback searches are complete.
Relevant primary sections and the exact missing hypotheses were inspected.
The next step is a reviewed analytical attack, not more generic literature
search or an attempt to infer a theorem from the source abstracts.
