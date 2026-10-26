# Write-stage report

This report records the original pre-author-identity snapshot. The later
identity-only update is documented in author-identity-review.md; the
mathematical text and bibliography are unchanged.

The technical note is `draft/main.tex`; the compiled output is `output/pdf/main.pdf`, eight letter-size pages. The author field is blank. The title remains "Scalar Hall Exclusion in Dimensions 11 through 15: A Partial Lean Formalization". A separate appendix adds the exact near-zero polynomial certificates for dimensions 8 and 9, without asserting full scalar coverage in either dimension.

## Evidence intake

Read in full: `evidence/claims.json`, the completed Lean definitions, finite proof, real proof, audit, tests, package configuration and manifest, `evidence/finite-result.json`, `evidence/final-review.md`, `evidence/resource-measurements.json`, `evidence/FinalScalarAxiomAudit.lean`, and the complete literature log. All achieved and quantitative manuscript claims come from that intake. No Lean process was launched during drafting.

The note gives the exact piecewise rational formulas, natural-size domain, full real domain `u <= 1`, finite criterion, completed-square proof, Bernoulli comparison, and relaxed-budget corollary. Table 1 distinguishes the 340 formally counted normalized cases from the 455 reviewed uncompressed cases. Table 2 contains two actual recorded incremental runs with cache, shared-load, and non-comparability caveats.

Additional evidence intake for the appendix: all literal definitions, both coefficient lists and identity/positivity proofs, the final theorem, audit, successful result, axiom log, README, definition and proof documents, and complete independent review under `evidence/near-zero/`. The fifteen-entry claim ledger supports the expanded scope. The appendix gives the exact gamma, kappa, L, E, H, T, F, and p formulas; the closed intervals [0,1/400] and [0,1/500]; the 17- and 19-coefficient homogeneous identities; and the endpoint and rescaling argument. The generator is explicitly outside the trusted proof. Review means separate assistant-agent statement and execution review, not external human peer review.

The current artifact does not formalize the matrix reduction, full cut, permanent floors, deficit/stationarity inputs, equality characterization, dimensions 5 and 6, or full scalar coverage in dimensions 7 through 10. The appendix does not include the remaining support intervals or tails in dimensions 8 and 9. The finite-only package is explicitly identified as shared-source verification, not an independently implemented proof algorithm. No numerical margins, empty-cache benchmarks, total development costs, or unsupported extension claims were added.

## How the mandatory searches changed the manuscript

1. Direct prior work: Section 1 attributes the Hall source to Nascimento and acknowledges Li/Xiong/Yang's prior Dittert Lean work. It excludes mathematical-discovery and first-formalization claims.
2. Original methods: Sections 1 and 3 attribute Lean/Mathlib and identify existing exact arithmetic, Bernoulli, and polynomial identity infrastructure. No new automation method is claimed.
3. Theoretical background: Sections 1 and 6 cite Cheon/Wanless and Pang and explicitly separate the matrix interfaces from the verified scalar theorem.
4. Adjacent work: Section 6 compares the evidence boundary with prior rational certificate replay and gives a short Bernstein paragraph. The appendix uses literal homogeneous expansions, but no generic Bernstein checker, subdivision theorem, or de Casteljau implementation is claimed. These certificates are separate from the main scalar theorem.
5. Recent work: Section 5 states the actual dependency closure and evaluation route instead of using exact arithmetic as a proxy for kernel verification. The note makes no unsupported performance comparison with a current tool.

## Citation and build checks

All eight registered references are used: `moura2021lean`, `community2020lean`, `cheon2012some`, `li2026proof`, `pang2026proof`, `siddique2026machine`, `bertot2011formal`, and `munoz2012formalization`. Nascimento and Lu have explicit pinned repository links in footnotes. `references.bib` was not manually edited.

`exactory-check lookup` reported eight verified entries, zero blocking entries, and zero warnings. Its report is `.exactory/citation-check.json`.

Build command: `nice -n 15 sh draft/build.sh`, from the manuscript workspace root. The script runs pdflatex, BibTeX, two further pdflatex passes, pdfinfo, and PNG rendering; each job uses niceness 15. Final logs are `tmp/pdfs/pdflatex-pass1.log`, `tmp/pdfs/bibtex.log`, `tmp/pdfs/pdflatex-pass2.log`, `tmp/pdfs/pdflatex-pass3.log`, and `output/pdf/main.log`. Final LaTeX pass: no undefined references, overfull boxes, underfull boxes, or compilation errors.

One BibTeX metadata warning remains: `empty publisher in moura2021lean`. The entry is registry-generated and its DOI is verified. The bibliography identifies the volume, pages, year, authors, title, and DOI. No publisher was fabricated and no warning was suppressed. The warning and source-field limitation are reported for the main agent's review.

## Visual check and handoff

All eight final rendered pages were inspected at `tmp/pdfs/main-1.png` through `main-8.png`. Equations, tables, source footnotes, reference links, and page numbers are legible and unclipped. The final rendering has no visible layout defect. The main agent will perform its own all-page inspection and commission a separate assistant-agent manuscript evidence review. This is not external human peer review.

The write-stage output is a local verification note, not publication approval. No upload, deposit, external write, Git commit, or new dependency installation occurred.
