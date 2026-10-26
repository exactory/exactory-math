# Novelty study

Objective `objective-000001`; study written on 2026-10-21. It covers the root statement and the two premises of the
case-split route that this attempt proposes. Write C_2 for the class of finite bipartite graphs with at least one edge
and no 4-cycle that have a bipartition (X, Y) in which every vertex of X has degree at most two. The route splits the
statement into the statement on C_2 (node of the reduce-and-translate strategy) and the statement on the girth-six
graphs outside C_2 (node of the barrier strategy, which asks whether the counterexample's mechanism transfers there).

## The root statement

Searches: the nine common-store records listed in `problem.md`, section 1, one per declared formulation (the exact
statement and its eight neighbours), captured on 2026-10-21 with recorded coverage; plus the tier-one study queries
(Crossref, zbMATH Open, Semantic Scholar) and MathOverflow.

Decisive works, all read in full: Conlon, Kim, Lee and Lee 2018 (Problem 1.5 open), Im, Li and Liu 2024 (Conjecture
4.1 open), Zhao 2025 (the general 1-subdivision question stated open), Kiem, Parczyk and Spiegel (21 September 2026),
and the reported counterexample [161], whose pattern has 4-cycles.

Finding of the common store: `supported_open` (record `problem_openness/assignment-openness-fable-2`, digest
`711410e0a450465dcf1afacdd23990ba5dc4681636f8d000f16b077fb5a75d78`, revision 276), from an independent observed review
on `route-claude-fable` that binds the nine searches and seventeen full readings. No settling work exists in the
captured literature, and no captured work after 2026-09-23 concerns Sidorenko's conjecture for patterns.

## The transfer of the counterexample's mechanism (barrier node)

Question: does any source apply the construction of [161] to a pattern without 4-cycles, or state what its limit
gives there? The natural transfer targets lie outside C_2: the pattern of [161] is the incidence graph of a triple
system, and its girth-six analogues are incidence graphs of linear triple systems whose points lie in at least three
triples, such as the Heawood graph, the incidence graph of the Fano plane.

- [161] itself states, after Equation (3.4), that "every fully active pair tests the parity of its four incidence
  signs" and builds the deficit on pairs lying in two faces (Proposition 2.1: every pair of E lies in exactly two
  faces). It does not discuss other patterns, and it proves the rank-layer limit (Lemma 3.1) only for its complex.
- No captured work after 2026-09-23 treats the construction; the arXiv window 2026-09-23 to 2026-10-21 is captured
  completely (`o3-after-counterexample`, three works, none on graph patterns). The MathOverflow question 515955 has no
  answer and was closed as not suitable for the site.
- Conclusion: the observation that the sign model is identically 1 on patterns without 4-cycles is not stated in any
  source found. It follows in a few lines from Equations (3.2) and (3.4) of [161]; this record claims it as a method
  boundary, not as a deep result. It holds for every girth-six pattern, inside C_2 as well as outside.

## The class with one side of maximum degree at most two (reduction node)

Question: does any source state that the statement restricted to this class is equivalent to Problem 1.5 of Conlon,
Kim, Lee and Lee?

- The ingredients are in print: the reduction to hosts of bounded maximum degree (Kim, Lee and Lee, Lemma 3.3; Conlon,
  Kim, Lee and Lee, Lemmas 3.3 and 3.4) and the removal of a vertex of degree one in the bigraph setting (Coregliano
  and Razborov, Corollary 5.3).
- Conlon, Kim, Lee and Lee pose Problem 1.5 for 1-subdivisions directly; Im, Li and Liu, Chen, Lin and Ma, Zhao and
  Kiem, Parczyk and Spiegel treat subdivisions of particular base graphs or on particular hosts. None states the
  equivalence of Problem 1.5 with the statement on graphs of girth at least six with one side of maximum degree at
  most two.
- Conclusion: the equivalence is not stated in any source found; it is an elementary consequence of the published
  lemmas, and the record presents it as such.

## Gaps

- Semantic Scholar returned HTTP 429 (rate limit) to every query of this study, including four retries with waits
  (`sources/study-queries/manifest.json` of the workspace). It is an unavailable source. The common-store searches
  cover the journal literature through OpenAlex, and the tier-one queries through Crossref and zbMATH Open.
- The full text of Fox and Wei 2017 (closed access) was not read; its content is taken from two works that describe it,
  Kral et al. 2019 (read in full) and Hancock, Kral, Krnc and Volec (arXiv:2011.02562, introduction): a local theorem
  for every graph that is a tree or has even girth. A local theorem cannot settle the statement.
