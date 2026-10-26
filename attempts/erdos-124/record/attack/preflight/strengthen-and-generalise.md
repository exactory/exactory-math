# Strategy study: strengthen-and-generalise

Date: 2026-09-06.

## Queries

The problem-study queries supply the initial original and neighbouring statements. Additional strategy-specific tier-one queries were:
- arXiv API: 'ti:complete AND (all:powers OR all:Furstenberg)', saved as sources/arxiv-strengthening.atom; hit arXiv:1507.02208v2.
- Semantic Scholar: '"New examples of complete sets" Furstenberg'; rate limited, no result.
- Crossref: 'complete sequences finite sums strong completeness Brown criterion powers'; saved as sources/crossref-strengthening.json. Hits included DOI 10.2307/2687907, On the Equivalence of Completeness and Semi-Completeness for Integer Sequences. Only the bibliographic record was inspected, and no theorem is imported from it.
- zbMATH Open: 'ti: complete sets Furstenberg'; saved as sources/zbmath-strengthening.json.
- Erdős database: the refreshed problem 124 discussion, specifically the Brown proof and the warnings about cutoff deletion.
- General web: '"complete sequences" "finite" "Brown" powers'; '"central interval" "subset sums" powers'; '"strongly complete" "powers" "Bergelson"'; '"3,4,7" "powers" cutoff'. These located Brown statements, arXiv:1507.02208, and zero-cutoff formalizations; no all-cutoff proof for the small sets was identified.

## Primary sources and constraints

BEGL96, DOI 10.4064/aa-77-2-133-138, pp.134-137, uses a bounded-gap supply plus a separately constructed long interval and a gcd-one residue supply. Its tail-gcd argument proves finite residue coverage, not integer coverage. The cutoff-1 small cases cannot supply a cutoff-uniform induction without a separate argument.

Bergelson-Simmons, arXiv:1507.02208v2 / DOI 10.4064/aa8221-10-2016, Main Theorem 2.1 and Theorem 1.23, replace a single supply by three disjoint supplies satisfying a bounded deficit condition. Their strengthening is already in print. Its proof explicitly requires disjointness when adding finite-sum sets, and separates irrational torus obstructions from rational congruence obstructions. The paper also gives incomplete syndetic finite-sum examples. Mere bounded gaps therefore cannot close an induction.

Brown's zero-cutoff argument begins with a summand of value 1. The proposed investigation will track a central represented interval and its endpoint losses, while retaining every original D and k. Any changed auxiliary statement must have a short deduction back to the objective and must be tested by hand on transparent examples before it is used. Finite experimental execution is not part of this analytical admission.

## Questions for the strategy

1. Which finite-deletion operation is genuinely needed, and what stronger interval statement remains meaningful after it?
2. Can prefix capacity, tail gcd, and residue coverage force a sufficient seed interval, or is an additional global condition necessary?
3. Does strict reciprocal surplus remove a loss that remains at equality?
4. Can a meaningful lemma or special family be separated into a reviewed branch with an exact claim?

## Stop reason

Fixed first-tier and neighbouring-statement study count reached. The known induction starting points, disjointness requirement, and published stronger sufficient conditions have been identified. No new mathematical claim has been proved during the study.
