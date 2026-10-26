# Exact-claim study

Date: 2026-09-05. Fixed floor: one query per four tier-one sources, plus two general-web queries. Stored responses are problem-arxiv.json, problem-semantic.json, problem-crossref.json, problem-zbmath.json.

- arXiv: all:Dittert AND (all:Bernstein OR all:polynomial), HTTP 200, one hit 2607.29191v2, dimension four SOS formalization. Abstract read.
- Semantic Scholar: Dittert near zero polynomial Bernstein 8 9, HTTP 429. Coverage blocked, no retry.
- Crossref: Dittert near zero polynomial Bernstein 8 9, HTTP 200. Five records concern wavelets or near-zero combinatorial theorems, not this claim.
- zbMATH: Dittert Bernstein polynomial, HTTP 404 no results.
- General web: "Dittert" "near" "Bernstein" "Lean"; "Dittert" "polynomial" "8" "9" "formalization". No exact polynomial formalization located. Unrelated results discarded. The known SamuelSchlesinger scaffold is a neighboring matrix statement, not this claim.

Primary evidence read: inherited PROOF.md section 6 and independent_coverage.py definitions near_poly, near_literal, and Bernstein arithmetic. The actual polynomial matches DEFINITIONS.md term by term. The study scratch/lean-novelty-2026-09-05.md records public Lu and Nascimento provenance, dimension-four Lean prior art, and the unmerged formal-conjectures matrix statement. No external canonical statement exists in the searched record for this particular local polynomial lemma. Its canonical formula is the explicit local checker, not the full matrix conjecture. Neighboring n7/support/matrix theorems are deliberately excluded.

Constraint: this is formal verification of a known mathematical certificate, with no priority or new Dittert theorem claim. The exact polynomial-to-Bernstein identity and both endpoints must be kernel checked. Stop reason: fixed six-query count reached; rate-limited coverage remains explicit.
