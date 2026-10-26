# Bounded query log

Date: 2026-09-07 UTC. This is pre-admission planning, not a mathematical move.
The proposed statement is high-mass positive-cutoff completeness, not a
claim that the complete original conjecture has been solved.

## Problem-level tier-one floor

1. arXiv MCP: `all:"complete" AND all:"powers" AND (all:"reciprocal" OR all:"Burr")`.
   Eight abstracts returned. None is a completeness result for pure powers.
   The returned titles include reciprocal quadrinomials, reciprocal power
   congruences, Artin reciprocity, Sturm-Liouville formal powers, person
   re-identification, nonreciprocal matter, operator product states and
   graphon power series. Their raw identifiers and abstracts are saved in
   sources/massProblemArxiv.txt. No theorem is imported from these hits.
2. Semantic Scholar MCP: `"complete sequences" "powers"`, limit eight.
   One relevant hit is BEGL96, DOI 10.4064/AA-77-2-133-138, CorpusId 13967275.
   A Fibonacci-powers title is only a neighbouring discovery hit; its
   varying-index sequence is not identified with the mixed-base objective.
   Other algebra and Lucas-sequence hits are not used.
3. Crossref API: bibliographic query
   `Complete sequences sets integer powers reciprocal`, rows five.
   Resolves BEGL96 as DOI 10.4064/aa-77-2-133-138.
4. zbMATH API: `ti:complete & ti:powers`.
   The response includes the BEGL96 record and summary. The broad result
   exceeded the output limit; sources/massProblemZbmath.txt is explicitly
   a truncated response, not an exhaustive search result.
5. Problem database: direct opens of
   https://www.erdosproblems.com/124 and its discussion thread both returned
   HTTP 403. The strategy-level indexed searches below provide a fallback.
   No content or current status is inferred from the failed direct opens.

## Strategy-level tier-one floor

1. arXiv MCP:
   `ti:"Strongly complete sets" OR (ti:"Examples" AND ti:"complete sets")`.
   Returns Fan 2607.14071v3 and Bergelson-Simmons 1507.02208v2.
   Both abstracts were read. The theorem sections described below were read.
2. Semantic Scholar MCP: `"Examples of complete sets"`, limit five.
   The service returned a rate-limit error. No immediate retry was made.
3. Crossref API: bibliographic query
   `Examples of complete sets Bergelson Simmons`, rows five.
   Resolves the published article, DOI 10.4064/aa8221-10-2016,
   Acta Arithmetica 177 (2017), 101-131.
4. zbMATH API: `ti:Examples of complete sets & au:Simmons`.
   Returns the Bergelson-Simmons record and review.
5. Indexed problem-database queries:
   `site:erdosproblems.com/124 powers complete reciprocal Bergelson Simmons Fan`
   and `site:erdosproblems.com/forum/thread/124 completeness powers partition`.
   Relevant old thread material distinguishes finite from infinite base sets
   and identifies the critical reciprocal-equality issue. The returned
   statement snippet contains an index typo; the pinned original objective
   and the canonical formal statement use the sum indexed by each base.

## Additional bounded route discovery and canonical statement

Three saved four-query web batches examined signed-tail identities,
syndetic difference sets, pure-power completeness and partition criteria.
Their exact queries/results are in sources/discovery-01.txt through
sources/discovery-03.txt. They are discovery, not proof evidence.

The current canonical file was opened and its 94 lines read:
https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/124.lean.
The original target is erdos124.ne_zero, with every nonzero natural k,
every finite base set, collective gcd one, reciprocal sum at least one,
and eventual membership in the sum of the per-base power sets.
The zero-cutoff theorem and the k=1 theorem for {3,4,7} do not replace it.
The source still contains sorry placeholders, and no Lean check was run.

Fan v3 sections 1 and 2 were read using the web reader, including Lemma 2.2,
Corollaries 2.3 and 2.5, their proofs, and the finite-residue proposition.
The saved reader response and targeted searches are under sources/.
A requested curl download of the raw HTML was refused by the managed-shell
hook. That command was not repeated or wrapped; no raw HTML snapshot is
claimed. This does not affect the already available reader response.

## Stop rule and scope of the search

The fixed ten tier-one source calls were completed, with the errors and
truncation recorded above, plus the bounded route-discovery batches and
canonical-source read. Stop at this count. No exhaustive novelty result is
claimed. The study may identify a useful corollary of existing methods;
publication-level novelty is not a condition for an internal root lemma.

