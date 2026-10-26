# Formal strategy study

Date: 2026-09-05. Fixed ceiling: four tier-one queries. Full fetched responses retained as strategy-*.json.

- arXiv: all:Bernstein AND (all:formal OR all:Lean), HTTP 200.
- Semantic Scholar: Bernstein polynomial formal verification rational certificate, HTTP 429; no retry.
- Crossref: A formal study of Bernstein coefficients and polynomials, HTTP 200, exact DOI 10.1017/S0960129511000090. Metadata read.
- zbMATH: Bernstein polynomial formal verification, HTTP 200; records include the known Bernstein verification literature. Metadata inspected; unavailable licensed summaries are not claimed read.

Primary implementation read: pinned Mathlib/RingTheory/Polynomial/Bernstein.lean definition and sum identities. Prior studies identify Bertot, Guilhot and Mahboubi, DOI 10.1017/S0960129511000090, and Munoz and Narkawicz, DOI 10.1007/s10817-012-9256-3. Prior finite scalar Lean machinery is available at CP-6602f547de0eb72c. Real numbers, natural powers, factorials, rational arithmetic, and positive powers exist in the pinned library. A short elementary positive-basis lemma can avoid importing the entire Bernstein analysis library.

Constraints: exact formula first under sorry, initial red axiom gate, then finite identities and positivity proofs. No native_decide, axiom, altered interval, supplied-positive-list substitute, installs or full Mathlib rebuild. At most six attempts and two mathematically sufficient restatements per lemma. The available single Lean slot was released to this agent by the coordinator. Commands use nice 15, -j1, -M2048 and sequential module builds. Stop reason: fixed count reached.
