# Ternary-reserve query log

Date: 2026-09-07. This is a bounded pre-admission study, not a proof record.
The exact candidate is eventual labelled pure-power completeness for every finite D with min D=3, gcd(D)=1 and reciprocal mass at least 11/6, at every positive cutoff and after every finite labelled deletion.

## Problem-level queries

- arXiv domain search: "powers of 3" "thick" "sums".
- Semantic Scholar domain search: "powers" "balanced ternary" "complete".
- zbMATH domain search: "powers of 3" "complete sequences".
  These three requests and their returned hits are in sources/ternaryProblem0.txt. The only displayed hit was an unrelated graph-automorphism paper, not a completeness theorem.
- Crossref API domain search: "balanced ternary" powers subset sums thick completeness.
- Erdős database domain search: "124" "ternary" powers.
  Response: sources/ternaryProblem1.txt. The database's cached aggregate pages restate the positive-cutoff problem and distinguish it from the zero-cutoff result. They also report the distinct density problem 125; no density assertion is transferred to thickness.
- Direct API attempts used arXiv all:"balanced ternary" AND all:"sums"; Semantic Scholar "balanced ternary powers complete sequences"; Crossref bibliographic "powers three eleven sixths strong completeness"; zbMATH "balanced ternary complete sequences"; and the exact database page /124. All four API requests were rejected by the web reader as unavailable, and /124 returned 403. Exact URLs and failures are in sources/ternaryProblemApis.txt. No hit-free claim is inferred from these failures.
- General neighbouring-statement searches: "powers of 3" "powers" "thick"; "balanced ternary" "subset sums"; "complete" "11/6" "powers". Response: sources/ternaryDiscovery.txt. OEIS A005836 identifies the ordinary ternary digit set, and the Algebraic Combinatorics formalization page states balanced ternary existence and uniqueness. Other displayed hits concern code golf, electronics, physics or unrelated problems.

## Strategy-level queries

- arXiv domain search: "balanced ternary" "integer" "representation".
- Semantic Scholar domain search: "powers of three" "signed sums".
- zbMATH domain search: "complete sequences" "ternary".
  Response: sources/ternaryStrategy0.txt. arXiv:2608.08910 concerns model quantization, not additive completeness; the zbMATH serial page is bibliographic background only. No exact route was found.
- Crossref API domain search: "balanced ternary" "integer representations".
- Erdős database domain search: "3" "cutoff" "124".
  Response: sources/ternaryStrategy1.txt. Bloom's cached author page distinguishes the positive-cutoff problem from the solved zero-cutoff statement and discusses the separate density problem. Other forum hits are irrelevant.
- Opened and searched https://faabian.github.io/algebraic-combinatorics/targets.html for balancedTernaryRepresentation_exists. Response: sources/ternaryFormalBackground.txt. Read the local section containing Theorem 1.483 and the exact displayed existence declarations. The repository and its build were not audited or executed.

## Primary and accepted material read

- Burr, Erdős, Graham and Li, Complete sequences of sets of integer powers, Acta Arithmetica 77 (1996), 133-138. Local research-root sources/begl1996.txt, previously read in full; the concluding remarks at lines 210-253 were reread. The small-input largest-exception statements concern cutoff one, not every cutoff.
- Bergelson and Simmons, New examples of complete sets, arXiv:1507.02208v2, DOI 10.4064/aa8221-10-2016. Local sources/bergelson-simmons.txt, relevant completeness definitions and Theorem 2.1/Corollary 2.5 read. Its published mechanism is not a two-syndetic-component theorem.
- Fan, Strongly complete sets and a conjecture of Erdos, arXiv:2607.14071v3. The saved response in ../two-component/sources/fan-conclusion.txt and prior mass-partition study cover the complete finite-correction argument and its ordered-block extension. The latter still uses three deficit-bounded components.
- Accepted local checkpoint-000016, acceptance-000005, proof erdos-124-mass-partition/moves/001-high-mass-completeness.md. Read in full. Sections 1, 2 and 5.1 supply the elementary disjoint interval/reserve and labelled gap interfaces.
- Accepted local checkpoint-000017, acceptance-000006, records the current high-mass range. It is the logical predecessor and comparison, not proof of the proposed ternary seed.
- The source-level two-component assessment is ../two-component/DECISION.md. Its initial discovery was not fully archived and supplies no proof evidence.

## Stop reason and limits

The fixed study budget was five tier-one source queries at each level, the documented direct-API attempts, three general neighbouring-statement queries, one relevant background page read and the stated accepted-source rereads. It is now reached. No exact all-positive-cutoff 11/6 statement was found in the inspected material. Access limitations and irrelevant search hits preclude an exhaustive novelty claim. Classical balanced ternary is already known and must be proved locally, not presented as a discovery. No mathematical computation was requested or executed.
