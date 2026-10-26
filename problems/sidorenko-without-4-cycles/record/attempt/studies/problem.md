# Problem study: Sidorenko's inequality for bipartite graphs without 4-cycles

Objective: `objective-000001` of this attack root. Common research store: the workspace `..`
(`math-conjectures/sidorenko-after-counterexample`), problem record `statement-girth-six`. Study written on 2026-10-21.

## Statement

Let H be a finite bipartite graph with at least one edge and no cycle of length four (girth at least six). Is
t(H, W) ≥ t(K_2, W)^{e(H)} for every graphon W? The contract asks for a decision with a complete proof. The finite-host
form is equivalent: t(H, G) ≥ p(G)^{e(H)} for every finite simple graph G, counting all homomorphisms, with
p(G) = 2e(G)/v(G)² (Kim, Lee and Lee, arXiv:1310.4383v3, equations (1.1) and (1.2); step graphons in one direction,
cut-distance approximation in the other).

## 1. Queries run

Common-store searches (exact records; every query's coverage, date and depth is in the record):

| Search record | Formulation | Digest |
|---|---|---|
| `search-openness-statement` | the exact statement | `8f546a52a7aaf0463011ebe9dcc7e044073a2046ebfb8112bcd5a745c916d96e` |
| `search-openness-one-subdivision` | the 1-subdivision of every graph (Conlon, Kim, Lee and Lee, Problem 1.5) | `c80796acee29996e963794fc815cf6a10aa7cc1209afd750756343d7904ac697` |
| `search-openness-subdivided-counterexample` | the 1-subdivision of the reported counterexample | `62d8f6f660a499716782a22d245ad518453755857dace80323dee408c9d9505a` |
| `search-openness-large-girth` | a girth threshold beyond which every bipartite graph is Sidorenko | `ce5b8b6a9c2f3128c0c9f11eee456618d1e3ab112abdf1b5eaac732dd98f2be2` |
| `search-openness-linear-incidence` | incidence graphs of linear k-uniform hypergraphs | `e55a09fe96082f618ddd51204e21598b2e6bad78e0ea2cb30c18d4bc857bdac2` |
| `search-openness-heawood` | the Heawood graph | `f9c03908ead9b00015f055935e44db2255ca087c3e257a99ad66feb35711e6bd` |
| `search-openness-forcing` | forcing for girth-six graphs with a cycle | `3080d83ed1b0178e3f585f028898fc733a24c75ea42c44cdff7727851b4460bc` |
| `search-openness-biregular` | biregular graphs of girth at least six | `5fb73773b410548ed3419cc019ce0564cd47de2df008a0cccf154e0e97cb9032` |
| `search-openness-subdivisions-of-sidorenko` | Conjecture 4.1 of Im, Li and Liu | `94add89065289a66f640067c70004ec37c0455f5ba64fad5b7a63ca376438c5c` |

They bind 25 captured responses, all captured on 2026-10-21: eleven openness arXiv API queries (most with complete
coverage, up to 50 results each), seven OpenAlex work searches (top 20 by relevance, or complete when fewer; journal
literature included), an OpenAlex citing-works query for Fox and Wei 2017 (complete), and the six arXiv captures of the
exploration's earlier field searches, bound where they cover a formulation.

Tier-one study queries outside the common searches, saved in the workspace under `sources/study-queries/` with their
manifest (URL, capture time, HTTP status, totals):

- Crossref `query.bibliographic=Sidorenko conjecture girth` and `... subdivision`, 20 rows each (relevance-ranked
  fuzzy matches; the hits are known works or unrelated).
- zbMATH Open `Sidorenko & girth` (5 documents, complete), `Sidorenko & subdivision` (6, complete) and `ti:Sidorenko`
  (51, complete). Every document there is either read in full in this record, disposed of in the common searches, or
  outside the question (linear equations, tournaments, hypergraphs, determinants); the one further title,
  "Markov random fields, homomorphism counting, and Sidorenko's conjecture" (IEEE Trans. Inform. Theory, 2022), proves
  the inequality for classes and settles no formulation (abstract only).
- Semantic Scholar `Sidorenko conjecture girth` and `Sidorenko subdivision`: HTTP 429 (rate limit) on the first
  capture and on four further attempts with 30, 60 and 90 second waits (2026-10-21T22:57:21Z and 23:02:28Z). Semantic
  Scholar is recorded as an unavailable source for this study.
- MathOverflow (tier two) `Sidorenko` (7 questions) and `Sidorenko girth` (none). Question 515955 (2026-10-12), "Is
  Sidorenko's Conjecture false?", asks whether the reported proof is correct and how to refine the conjecture so that
  it stays interesting; it was closed as not suitable for the site, with score -2 and no answer, and its comments point
  to a list question (515849) on the checking of the released papers.

## 2. Hits worth reading (all read in full in the common store)

- The reported counterexample [161] (`reading-openai-sidorenko-2026`): a 35-vertex, 66-edge bipartite pattern, the
  incidence graph of 22 triples on 13 points in which every pair of E lies in exactly two faces, so it has 4-cycles;
  the limit (3.2) of its rank-layer kernels is a sign model whose nonconstant terms are indexed by those pairs.
- Conlon, Kim, Lee and Lee 2018 (`reading-ckll-2018`): 1-subdivisions of cliques, of Sidorenko graphs and of KNRS
  graphs are Sidorenko; Problem 1.5 asks for the 1-subdivision of every graph, "outside the reach of current methods";
  Lemma 3.3 (hosts of bounded maximum degree suffice) and Lemma 3.4 (a large subgraph of large minimum degree).
- Kim, Lee and Lee 2016 (`reading-kll-2016`): the proof of the bounded-degree reduction (Lemma 3.3) by vertex splitting.
- Coregliano and Razborov 2021 (`reading-cr-2021`): biregular hosts suffice; Corollary 5.3, a vertex of degree one
  can be removed; Theorem 8.2, regular graphons suffice in the symmetric setting (proof sketched).
- Im, Li and Liu 2024 (`reading-ill-2024`): even theta replacements, uniform subdivisions of Sidorenko graphs,
  Conjecture 4.1.
- Chen, Lin and Ma 2024 (`reading-clm-2024`): odd subdivisions of KNRS graphs.
- Zhao 2025 and 2026 (`reading-zhao-2025-even`, `reading-zhao-2026-conj`, `reading-zhao-2026-corr`,
  `reading-zhao-2026-lp`): 1-subdivisions on abelian, class-function and product Cayley hosts; regular-KNRS base graphs
  have Sidorenko 1-subdivisions.
- Kiem, Parczyk and Spiegel 2026 (`reading-kps-2026`): the state of the subdivision results on 21 September 2026; the
  forcing conjecture stated open.
- Lovász 2011 (`reading-lovasz-2011`): local Sidorenko for every bipartite graph.
- Conlon and Lee 2017 and 2021, Hatami 2010, Kral et al. 2019, Lee and Schülke 2019, Conlon, Fox and Sudakov 2010,
  Sidorenko 2020 (readings `reading-conlon-lee-2017`, `reading-conlon-lee-2021`, `reading-hatami-2010`,
  `reading-kmpw-2019`, `reading-lee-schuelke-2019`, `reading-cfs-2010`, `reading-sidorenko-2020`): the norming classes
  and their limits; the named smallest open case K_{5,5} minus C_10 has 4-cycles.

## 3. What was learned, as constraints on the plan

1. The statement is open: the independent openness finding of the common store (`problem_openness`,
   `assignment-openness-fable-2`, digest `711410e0a450465dcf1afacdd23990ba5dc4681636f8d000f16b077fb5a75d78`,
   revision 276) is `supported_open` for the statement and its eight neighbours. No argument reaching the statement is
   in print, in either direction.
2. The positive results are class results: subdivisions of KNRS, regular-KNRS or Sidorenko graphs; even theta
   replacements under divisibility; incidence graphs of regular polytopes; restricted Cayley hosts; graphs with a part
   of at most four vertices (Sidorenko 1991, as cited by Im, Li and Liu and by Kim, Lee and Lee). A proof of the
   statement must go beyond all of them; this attempt does not aim at a proof.
3. The only negative result is [161], whose pattern has 4-cycles. Transferring its construction to a girth-six pattern
   is the natural negative route. Its mechanism is visible in Equations (3.2) and (3.4): the limit moments are products
   of parity factors over pairs of points lying in two faces. Whether a girth-six pattern has such pairs at all is the
   first thing to check (node of the barrier strategy).
4. Hosts may be taken of bounded maximum degree (Kim, Lee and Lee; Conlon, Kim, Lee and Lee, Lemma 3.3), and a vertex
   of degree one does not change the property (Coregliano and Razborov, Corollary 5.3, in the bigraph setting; their
   symmetric Theorem 8.2 is sketched). The reduction of a subclass to a known open problem must use the fully proved
   finite lemmas (node of the reduce-and-translate strategy).
5. Every 1-subdivision of a simple graph has girth at least six, so the statement contains Problem 1.5. Whether the
   statement on the graphs with one side of maximum degree at most two is equivalent to Problem 1.5 is an exact
   question the reduction can answer.
6. Local results hold for every bipartite graph (Lovász; Fox and Wei, as described by Hancock, Kral, Krnc and Volec and
   by Kral et al.), so a counterexample, if any, is far from the constant graphon in cut norm; small perturbation
   arguments cannot decide the statement.
7. No computation is planned: no finite residue is known, and the contract's resource policy is a screen.

## 4. Stop reason

The queries ran dry: the second round of openness searches (o9 to o11, x1 to x8) and the tier-one study queries
returned no relevant work beyond those already read in full.
