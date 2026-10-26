# Problem study and novelty boundary

Date: 2026-09-05. Fixed study floor: four source-restricted queries at each of problem and strategy level, plus the pinned source already present locally.

## Queries and hits

Problem queries (web search restricted by source terms):
- arXiv: `permanent Dittert seven Hall entropy boundary maximizer`. Relevant hit: Zhekai Pang, arXiv:2606.01531, abstract read; covers n>=17 and not this n=7 coverage question.
- Semantic Scholar: `Dittert conjecture seven Hall entropy`. No relevant exact-statement hit.
- Crossref: `Dittert conjecture permanent`. No relevant exact-statement hit returned.
- zbMATH: `Dittert conjecture permanent 7`. Author/serial profiles, no n=7 verification record.

Strategy queries with domains restriction:
- arXiv: `Dittert "Hall" "Bernstein" seven`.
- Semantic Scholar: `Dittert permanent boundary maximizers`.
- Crossref search: `Dittert permanent Hall`.
- zbMATH: `Dittert permanent boundary`.
These searches returned unrelated material, not an independently reviewed n=7 proof. Search failures are not evidence that no such proof exists. No own problem database or formalized canonical statement was identified.

Primary source read: Nascimento's reconstruction, commit 894066bbaa715138c98bf3cb7c6fdb4f39a37701, n6-n7/dittert_n6_n7_reconstruction.tex, sections 1-5 and the n=7 relevant stable-capacity subsections of section 6. Pinned locally at ../dittert-completion-tree/study/external-proof/n6-n7. Complete relevant polynomial arithmetic, n=7 builders, scalar checks, and tree traversals were read in both verify_dittert_n6_n7.py and audit_dittert_n6_n7_sympy.py. n=6-only routines are outside this study. Attribution: https://github.com/pedromnasc/dittert-conjecture-proof/tree/894066bbaa715138c98bf3cb7c6fdb4f39a37701 and https://github.com/lueluelue2006/dittert-n7-extension/tree/56397b70299278b338a286b90361180833dbf983.

## Constraints learned

The theorem and certificate families are already attributed in public unreviewed material. This task is the user's stricter independent verification of that candidate, not a new theorem claim and not a literature priority claim. The existing reviewer verdict is not a premise. Existing certificates and source files remain unchanged. New work must expose full set coverage and simultaneous branch predicates, and reject an omitted leaf or support class.

The source gives a finite residue on fixed compact boxes. Its mathematical coverage uses global maximality and support-preserving stationarity, not a selected fixed point. Hall positivity must be proved before division, and the scalar sign cases include zero deviations. For the bivariate alternative, N>0 is needed before squaring; F>0 by itself does not suffice. A finite certificate can be independently rechecked by direct polynomial restriction on each recorded leaf, avoiding dependence on the generating subdivision recursion.

Stop reason: fixed eight-query count reached. Pinned primary files contain the exact object under verification; broader literature claims are not needed for the assigned audit.

