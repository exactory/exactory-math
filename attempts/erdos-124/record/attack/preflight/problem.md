# Problem study: positive-cutoff pure-power completeness

Date: 2026-09-06. This is an initial admission study, not a claim of new mathematics.

## Queries and sources

1. Erdős database: refreshed https://www.erdosproblems.com/124, /forum/thread/124, and /forum/thread/124/proof-claims. The browser fetch returned 403, but direct HTTPS downloads succeeded. Saved sources/124-page.html, sources/124-thread.html, and sources/124-proof-claims.html in the research workspace. The live discussion says OPEN and Proof claims (0). The latest visible comment is dated 2026-05-13.
2. Formal statement: refreshed https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/124.lean, saved as sources/124.lean. The positive-cutoff declaration is Erdos124.erdos124.ne_zero, tagged research open and containing sorry. This is a formal statement, not a checked proof.
3. arXiv tool query: '"complete sequences" AND powers', six results requested. It returned four unrelated records. A refined API query, 'ti:complete AND (all:powers OR all:Furstenberg)', returned arXiv:1507.02208v2 among unrelated records. The API response is sources/arxiv-strengthening.atom.
4. Semantic Scholar: '"Complete sequences of sets of integer powers"', five results requested. Rate limited. A later distinct query, '"New examples of complete sets" Furstenberg', was also rate limited. No results were inferred.
5. Crossref: bibliographic query 'Complete sequences sets integer powers', five results. Exact hit: DOI 10.4064/aa-77-2-133-138. Response: sources/crossref-problem.json.
6. zbMATH Open: 'ti: complete sequences powers'. Exact hit: document 918701, BEGL96, with an author summary. Other hits were generalized Fibonacci powers and an unavailable licensed record. Response: sources/zbmath-problem.json.
7. General web queries: '"Complete sequences of sets of integer powers" Burr Graham Li pdf'; '"complete sequences" "integer powers" strict inequality cutoff'; '"complete sequences" "powers" Melfi 2004'; 'site:arxiv.org "complete" "sets" "integer powers" Burr'; 'site:zbmath.org "complete sequences" "powers"'; 'site:mathoverflow.net "complete" "powers" "Burr"'; '"New examples of complete sets" Furstenberg'. These located the primary Bergelson-Simmons paper and its publisher record, DOI 10.4064/aa8221-10-2016.

## Primary documents inspected

- Burr, Erdős, Graham, Li, Complete sequences of sets of integer powers, Acta Arithmetica 77 (1996), 133-138, DOI 10.4064/aa-77-2-133-138. Downloaded from https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7722.pdf. Inspected the conjecture, Theorem 1 and its proof architecture, residue Claim 4, and all concluding theorem statements on p.137. Rendered and visually inspected p.137. Saved PDF and extracted text.
- Bergelson and Simmons, New examples of complete sets, with connections to a Diophantine theorem of Furstenberg, arXiv:1507.02208v2; published DOI 10.4064/aa8221-10-2016. Downloaded from https://arxiv.org/pdf/1507.02208. Inspected Theorem 1.23 and its multiplicity footnote, Main Theorem 2.1, Lemma 2.11, Remarks 2.7-2.10, and the proof of Theorem 1.23. These selected sections, not the entire paper, were read.
- Aristotle/Alexeev zero-cutoff proof source: https://raw.githubusercontent.com/plby/lean-proofs/refs/heads/main/src/v4.24.0/ErdosProblems/Erdos124b.lean. Saved as sources/aristotle-zero.lean; inspected theorem and lemma inventory. The existing proof is attributed; no Lean build was run in this workspace.

## Statement audit

The user's D is a finite set, so distinctness is automatic. Natural k != 0 is k >= 1. Pointwise sums of sumsOfDistinctPowers exactly implement one finite exponent subset per base. Zero belongs to each summand set, so optional coefficients c_i introduce no additional freedom. Different bases may supply the same numerical power as separate occurrences. The reciprocal denominator is d_i - 1, as in BEGL96 and the current formal file, not the website's d_r - 1 typo. No computational observation about finitely many n can refute eventual completeness.

## Known constraints

The zero-cutoff theorem is known. Removing the initial powers cannot be justified by completeness alone. BEGL96 states the small-set largest-exception results at cutoff 1: {3,4,7}: 581; {3,5,7,13}: 111; {3,6,7,13,21}: 16; {3,4,5}: 78. Its text does not establish these same fixed sets for every cutoff. Its Theorem 3 allows the base set to grow with the cutoff, so its quantifiers do not settle a fixed finite D for all k.

Bergelson-Simmons Theorem 1.23 already gives strong completeness for base sets partitioned into three reciprocal-mass blocks each of mass at least 1 and a separate gcd-one block (subject to its set/multiplicity convention). Families satisfying that result are not new. The method uses three disjoint bounded-gap subset-sum supplies and a fourth supply for torus and residue coverage. A single bounded-gap supply is insufficient for that published argument. Its finite-set notation must not erase collisions in the user's labelled sequence.

The full positive-cutoff conjecture remains open in the inspected sources. The equality case is delicate because growing prefix surplus requires separation of powers; the strict case has a linear surplus bound. Neither surplus nor complete residues provides an initial interval of sufficient length by itself.

## Study stopping rule

Fixed initial study count reached: all five tier-one sources were queried, the exact original and neighbouring strong-completeness statements were checked, and two relevant primary papers were inspected. Semantic Scholar was unavailable due to rate limits. Further strategy studies will be scoped to the next mathematical question rather than repeating this survey.
