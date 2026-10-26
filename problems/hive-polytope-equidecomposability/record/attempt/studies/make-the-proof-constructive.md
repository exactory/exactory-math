# Strategy study: make-the-proof-constructive

Objective `objective-000001`, claim of obligation-000001 (see `studies/problem.md`). The
strategy's step 1 asks, before any entry is dispatched, for the value to beat and the
construction holding it, the seeds and amplifying operations tried with the range searched,
and whether an approximation argument was carried through and where it stopped. Written on
2026-10-20; every query below was run on 2026-10-20.

## 1. Queries

Records of the common store reused: `search-theory-period-collapse` (digest
`9811032a8ddd...`; the piecewise-unimodular and piecewise-linear mechanisms of period
collapse), `search-adjacent-gelfand-tsetlin` (`fc0c45a4daa2...`; transfer maps and
mutations in the sibling family), `search-recent-stretched-lr` (`d0f8e3a4ec3b...`; hive
geometry). The abstracts of the new hits were fetched by `id_list`
(`studies/queries/arxiv/abstracts-strategy-hits.xml`).

| source | file | query | requested | returned | coverage |
|---|---|---|---|---|---|
| arXiv API | `arxiv/c-arxiv-combinatorial-mutation.xml` | `all:"combinatorial mutation" AND all:polytope AND all:Ehrhart` | 20 | 2 of 2 | complete |
| arXiv API | `arxiv/c-arxiv-transfer-map.xml` | `all:"transfer map" AND all:"order polytope"` | 20 | 4 of 4 | complete |
| arXiv API | `arxiv/c-arxiv-piecewise-unimodular.xml` | `all:"piecewise unimodular" OR all:"piecewise-unimodular"` | 20 | 3 of 3 | complete |
| arXiv API | `arxiv/c-arxiv-hive-octahedron.xml` | `all:hive AND all:"octahedron recurrence"` | 20 | 8 of 8 | complete |
| arXiv API | `arxiv/c-arxiv-hive-vertices.xml` | `all:"hive polytope" AND all:vertices` | 20 | 0 of 0 | complete |
| arXiv API (title) | scratch lookups, not saved as evidence | `ti:"Combinatorics and geometry of Littlewood-Richardson cones"` (1 hit, math/0407170v1); `ti:"Factorisation of Littlewood-Richardson coefficients"` (0 hits) | 5 | 1; 0 | complete |
| Semantic Scholar | `s2/c-s2-piecewise-unimodular-ehrhart.json` | `piecewise unimodular map polytopes Ehrhart equivalent dissection` | 20 | 2 of 2 (on a retry with 45 s spacing after HTTP 429): arXiv:2210.04326 (piecewise-linear promotion and RSK) and arXiv:2003.12271 (two enriched poset polytopes), both already in the record's potentially relevant set | complete |
| Semantic Scholar | `s2/c-s2-pak-vallejo.json` | `Combinatorics and geometry of Littlewood-Richardson cones hive polytope` | 20 | HTTP 429 twice | gap (rate limit) |
| Semantic Scholar | `s2/c-s2-honeycomb-vertices.json` | `honeycomb model hive polytope integral vertices Knutson Tao Woodward` | 20 | 0 of 0 | complete |
| Semantic Scholar | `s2/c-s2-horn-factorization.json` | `Littlewood-Richardson coefficients factorization Horn inequality saturated` | 20 | HTTP 429 twice | gap (rate limit) |
| Crossref | `crossref/c-cr-pak-vallejo.json` | `Combinatorics and geometry of Littlewood-Richardson cones` | 10 | 10 | top_k (bibliographic) |
| Crossref | `crossref/c-cr-ardila-bliem-salazar.json` | `Gelfand-Tsetlin polytopes and Feigin-Fourier-Littelmann-Vinberg polytopes as marked poset polytopes` | 10 | 10 | top_k (bibliographic) |
| Crossref | `crossref/c-cr-ktw.json` | `The honeycomb model of GL_n(C) tensor products II: Puzzles determine facets of the Littlewood-Richardson cone` | 10 | 10 | top_k (bibliographic) |
| Crossref (DOI) | scratch lookup | `works/10.1016/j.jcta.2008.06.005` (King-Tollu-Toumazet 2009, JCTA 116, 314-333) | 1 | 1 | complete |
| zbMATH Open | `zbmath/c-zb-marked-poset.json` | `marked poset polytope transfer map` | 20 | 0 ("No results found") | complete |
| zbMATH Open | `zbmath/c-zb-hive-vertex.json` | `hive polytope vertex` | 20 | 0 ("No results found") | complete |

## 2. Hits worth reading

| work | identifier | what it did | read |
|---|---|---|---|
| Haase, McAllister 2008 | arXiv:0709.4070v1 | Example 2.1: a denominator-D triangle cut by one line, one affine unimodular map, union an integral triangle. Example 2.3: Stanley's pyramid conv{(0,0,0),(1,0,0),(1,1,0),(0,1,0),(1/2,0,1/2)} cut by one plane (normal (-1,1,1)) with one unimodular map on a half-space, image an integral simplex. Open Problem 3.3: no systematic technique. | full (`reading-haase-mcallister-2008-3`) |
| Buch 2000 | arXiv:math/9810180v1 | Example 2: a hive polytope with a non-integral corner; Proposition 2 on corners whose flatspaces are small; integrality for at most four parts. | full (`reading-buch-2000-3`) |
| De Loera, McAllister 2006 | arXiv:math/0501446v1 | Theorem 4.6: the homogenized hive matrix has a unimodular (placing) triangulation for rank at most six, so every generalized hive polytope has an integral vertex. | full (`reading-dlm-2006-3`) |
| Fernandes, de Pina, Ramirez Alfonsin, Robins 2018 | arXiv:1802.07164v1 | The weighted nearest-neighbour interchange as a piecewise unimodular map: each move dissects by one or two hyperplanes and applies unimodular maps on the pieces; the composition over a sequence of moves is a finite dissection. | full (`reading-fernandes-2018-3`) |
| Alexandersson, Hopkins, Zaimi 2022 | arXiv:2206.02276v2 | Pak's piecewise-linear RSK as a lattice-respecting homogeneous bijection between rational polytopes (Corollary 4.1), realized by combinatorial mutations (Remark 6.5). | full (`reading-ahz-2022-3`) |
| Ferudun 2026 v2 | arXiv:2607.22301v2 | Lemma 8: qH is a lattice polytope with the normal fan of H and L_H(qt) = L_{qH}(t); the Horn-factorisation remark (a dim-3 five-part hive with all essential Horn inequalities strict). | full (`reading-ferudun-2026-3`) |
| King, Tollu, Toumazet 2006 | eudml 227653 | Conjecture 4.3 (factorisation when an essential Horn inequality is saturated); the skeletal graph and degree bound. | full (`reading-ktt-2006-3`) |
| Cho, Jung, Moon 2008 | DMTCS Proc. AJ, 483-494 | Theorem 1.3: the factorization theorem (King-Tollu-Toumazet 2009) in subset form. Lemma 3.5: for the second classical reduction formula, Psi(H) = H + R(i, j, k; n) with R a fixed hive labelled by 0 and -1, a bijection of LR-hives, that is, an integral translation at the level of hives. | full (`studies/sources/cjm2008.txt`) |
| Ghodsi 2026 | arXiv:2609.14357v1 | Theorem 12: the essential Horn factorization theorem restated with its multiplicity-one subset condition, used as a polynomial-preserving reduction. | full (`reading-ghodsi-2026-3`) |
| Knutson, Tao, Woodward 2004 | arXiv:math/0306274v1 (Electron. J. Combin. 11) | The octahedron recurrence gives bijections between hives (associativity of the hive ring), piecewise-linear and lattice-preserving. | abstract |
| Henriques, Kamnitzer 2004 | arXiv:math/0408114v3 | Associator and commutor of hive tensor products through a modified octahedron recurrence. | abstract |
| Pak, Vallejo 2005 | arXiv:math/0407170v1 (European J. Combin., DOI 10.1016/j.ejc.2004.06.008) | Explicit linear maps between the combinatorial models of the Littlewood-Richardson coefficients (hives, Berenstein-Zelevinsky patterns, tableaux). | abstract |
| Higashitani 2020 | arXiv:2002.01364v2 | The chain polytope of a poset is obtained from its order polytope by a sequence of combinatorial mutations (lattice-preserving piecewise-linear maps). | abstract |
| Clarke, Higashitani, Zaffalon 2022 | arXiv:2211.07995v1 | Restricted chain-order polytopes of a Young diagram are related by combinatorial mutations, which preserve period collapse. | abstract |
| Luo 2026 | arXiv:2609.28507v1 | A positively homogeneous piecewise unimodular shear from a free sum onto the polar preorder polytope of an ordinal sum, giving lattice-point bijections at every dilation; a product formula realized by a piecewise unimodular map. | abstract |
| Fujita, Higashitani 2026 | arXiv:2603.21588v1 | Polyptych lattices of transfer maps for marked chain-order polytopes. | abstract |
| King, Tollu, Toumazet 2009 | DOI 10.1016/j.jcta.2008.06.005 | The factorization theorem (their Theorem 1.4). | not available (HTTP 403); statement through Cho-Jung-Moon 2008 and Ghodsi 2026 |
| Combinatorial mutations of Gelfand-Tsetlin and FFLV polytopes | DOI 10.1016/j.jpaa.2024.107637 (JPAA 2024) | Mutations in the sibling family. | record (Crossref) |

## 3. What was learned, as constraints on the plan

The value to beat and the construction holding it. The target is not extremal (no number
is to be beaten); the object to construct for each triple is a decomposition of H and a
lattice polytope Q. The construction in print holds only the trivial range: for n <= 4 and
for dim H <= 1, Q = H (Buch 2000; `studies/problem.md`, constraint 3). Nothing in print
constructs a decomposition for any non-lattice hive polytope.

The seeds and amplifying operations tried, with the range searched. None for hives. The
smallest parameter at which a seed can be searched is n = 5 and |nu| = 15 (exploratory scan
`studies/scripts/instance_check.py`): the first of the five triples, nu = (5,4,3,2,1),
lambda = (4,3,2,1), mu = (3,2), has dim H = 3 with vertices, after the translation by the
integral vertex (8, 11, 12, 12, 14, 14) and the projection to the three free coordinates,
0, e1, e3, e1 + e3, e1 + e2 + e3 and w = (1/2, -1/2, 1/2); so H is the union, along the
unit square in the (x1, x3)-plane, of the lattice pyramid with apex e1 + e2 + e3 and the
rational pyramid P_w with apex w at half height over the centre of the square. The Ehrhart
polynomial of P_w is 1 + (11/6)t + t^2 + (1/6)t^3 (the difference of the recorded polynomial
of H, the lattice pyramid's polynomial and the square's), the polynomial of a unimodular
simplex. Haase-McAllister's Example 2.3 handles Stanley's pyramid, a half-height pyramid over
the unit square with apex over an edge midpoint (not over the centre, as here), by one
cut along a plane through the apex and a diagonal of the base and one unimodular shear
fixing that plane; the analogy is a hypothesis about the mechanism, not a transfer of
their construction. Applied to the whole of H rather than to P_w alone, the mechanism
suggests the cut along the plane x = z (which contains w, p and a diagonal of the square)
and the shear U(x, y, z) = (x, y + x - z, z), which fixes that plane and makes w the
midpoint of (1, 0, 0) and U(0, 0, 1) = (0, -1, 1). The exploratory script
`studies/scripts/seed_check.py` (output `seed_check.out.txt`, no native credit) finds that
the union of H n {x >= z} and U(H n {x < z}) is the lattice polytope with vertices
0, (1,0,1), (1,1,1), (1,0,0), (0,-1,1), with the same Ehrhart polynomial as H and with
consistent pieces up to dilation 6. The proof of this, including the identification of H
from the rhombus inequalities, the convexity of the union, the disjointness of the images,
the integrality of the vertices, and the lift to R^6, is the content of the seed move and is
not established by the study. Amplifying operations available in the ambient: the product of
polytopes (a product of equidecompositions is an equidecomposition, and a product of lattice
polytopes is a lattice polytope), integral translations and unimodular embeddings (adding a
part of size zero or a column to all three partitions moves H by an integral vector or
embeds it unimodularly), and dilation (qH is a lattice polytope, Ferudun Lemma 8). The
operation the statement's quantifier structure needs is one that produces every hive
polytope from smaller ones: the only candidate in print is the essential Horn factorization
(KTT 2009; Cho-Jung-Moon Theorem 1.3; Ghodsi Theorem 12), which is proved for coefficients
and polynomials, not stated for polytopes. The amplification lemma the strategy requires
before any seed search is therefore an obligation of the attack: that under a saturated
essential Horn inequality with the multiplicity-one subset condition, H(lambda, mu, nu) is
GL(Z)-equidecomposable with (or affinely unimodularly isomorphic to) the product of the two
smaller hive polytopes. Ferudun's example shows that primitive (non-factorable) triples of
dimension 3 exist at five parts, so even a proved lemma leaves primitive triples as the
seed class, not a finite set.

Whether an approximation argument was carried through. No generic-approximation or
forcing-type route applies: the base theory is finitary and nothing is undecided by it
(precondition question 6 is no); the approximation branch (plan steps 4 to 6) is closed.

Maps in print that are the right kind of object. Every mechanism of period collapse in
print is a lattice-respecting piecewise-linear or piecewise-unimodular map between rational
polytopes: the nearest-neighbour-interchange maps (one or two cuts per move), RSK and
combinatorial mutations (AHZ, Higashitani, Clarke-Higashitani-Zaffalon), transfer maps
(Ardila-Bliem-Salazar, Fujita-Higashitani), Luo's shear for free sums, and, at the hive
level, the octahedron-recurrence bijections (Knutson-Tao-Woodward; Henriques-Kamnitzer), the
linear maps between models (Pak-Vallejo) and the integral translation R(i, j, k; n) of
Cho-Jung-Moon. None of them lands on a lattice polytope except the trivial ones; a proof by
this strategy must produce a map whose image is convex and integral, which no mechanism in
print does for a non-lattice hive. The unimodular triangulation of the homogenized hive
matrix (De Loera-McAllister, rank at most six) is a statement about the cone over all hive
polytopes of a rank and gives integral vertices, not integral polytopes.

Consequences for the entries. The branch is the seed branch (question 5 yes, question 6
no). Step 2 (pin-the-extremal-candidate-first) has no extremal quantity to pin and is not
dispatched; the first move under the strategy is seed-and-amplify, whose action 1 (the
amplification lemma) is the Horn-product obligation above, stated exactly and attacked
analytically; its action 2 fixes the seed parameter (n = 5, size 15, the five triples, of
which the first is the simplest with dim 3); action 3, the seed search, is a hand
construction on the explicit polytope above (no run admission needed for a hand
construction; a program run would need admission first), verified by exact arithmetic on the
pieces. The failure signal to watch: the operation breaks what the configuration names
(convexity of the union, disjointness of the images), or every seed in the smallest
parameter has zero excess (no decomposition found), in which case the record gains the
searched range and the first open instance.

## 4. Stop reason

The queries ran dry: the five arXiv queries returned the known mechanisms and hive
bijections and nothing that constructs a decomposition for a hive; zbMATH returned nothing
for both queries; the Crossref resolutions confirmed venues; the Semantic Scholar queries
were rate-limited except one that returned nothing. Two consecutive sources returned
nothing new.
