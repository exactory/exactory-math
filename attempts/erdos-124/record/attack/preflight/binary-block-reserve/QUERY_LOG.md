# Binary-block-reserve query log

Date: 2026-09-07. This is a bounded pre-admission study, not a mathematical move.
The exact candidate is eventual labelled power completeness for all finite D with minimum four, bases eight and sixteen present, collective gcd one, and reciprocal mass at least 251/140, at every positive cutoff and after every finite labelled deletion.

## Problem-level tier-one queries

- arXiv domain: "powers" "4" "8" "16" "complete".
- Semantic Scholar domain: "integer powers" "signed" "complete sequences".
- zbMATH domain: "complete sequences" "powers" "signed".
  Responses are in sources/binaryProblem0.json. The displayed arXiv hits concern Waring-type fixed exponents (2404.08193), particle physics (1505.05264 and 2403.08021) and communications hardware (2406.07934). Their returned snippets, not full papers, were inspected and are unrelated to the exact claim.
- Crossref API domain: "complete sequences" "powers" "4" "16".
- Erdos database domain: "124" "4" "8" "16".
  Responses are in sources/binaryProblem1.json. Cached aggregate pages and a user page refer to problems124 and125 and the zero-cutoff/positive-cutoff distinction. A solved statement on an aggregate or user page is not transferred to this all-positive-cutoff claim.

Direct API attempts used arXiv all:"signed powers" AND all:"complete"; Semantic Scholar "signed power sequences 4 8 16"; Crossref "labelled power sequences balanced binary strongly complete"; zbMATH "signed power complete sequences"; and the exact database page /124. All four API requests were unavailable to the web reader, and /124 returned403. Exact URLs and failures are saved in sources/binaryDirectApis.json. These failures do not establish absence of literature.

## Strategy-level tier-one queries

- arXiv domain: "balanced" "weights" "complete" "powers".
- Semantic Scholar domain: "signed digit" "complete" "weights".
- zbMATH domain: "balanced" "weight sequence".
  The combined response is empty, saved in sources/binaryStrategy0.json.
- Crossref API domain: "balanced" "complete" "weights".
- Erdos database domain: "124" "signed" powers.
  Sources/binaryStrategy1.json returns cached author discussions, including the need to distinguish problem124's converse and other unrelated proof discussions. No exact binary-block construction was identified.

## Discovery and neighbouring formulations

Sources/ternarySuccessorDiscovery0.json records four general queries: "powers of 3" "powers" "thick" subset; "complete sequences" "3" "cutoff"; "strongly complete" "powers" "two"; and "balanced ternary" "complete" "powers" sums. These were successor discovery after the ternary candidate, not new evidence for its already frozen result.

Sources/binarySuccessorDiscovery1.json records four queries: "complete sequences" "4" "8" "16"; "powers" "signed" "251/140"; "powers of two" "balanced" "complete sequences"; and "strongly complete" "repeated" powers. Most hits concern elementary pattern exercises or logical completeness. No relevant exact theorem was identified from their snippets.

Sources/binaryNeighbours.json records three more focused neighbouring queries: "powers of four" "powers of eight" sums; "signed" "4, 8, 16" powers complete; and "complete" "251/140" powers. The mathematical hits concern elementary geometric sums or Waring-type sums, not finite labelled base sets at arbitrary cutoff. None is used as a proof premise.

## Primary material actually read

Ethan D. Bolker, Samuel A. Feuer and Catalin Zara, Balance weighing: variations on a theme, Mathematics Magazine94(5), December2021. Author-hosted text: https://www.cs.umb.edu/~eb/weighing.pdf. The saved response is sources/binaryWeightPrimary.json. Read the title, introduction, Theorem1, and the complete sections containing Theorem2, its corollaries, the complement lemma and Theorem3, through page4 (source lines0-163). The remaining pages were not read for this study. These sections supply the classical relation between signed weights and bounded multiplicities, not the proposed pure-power tail result. No source algorithm was executed.

The complete accepted ternary proof was read at erdos-124-ternary-reserve/moves/001-ternary-reserve.md. Sections1,2,4 and5 give the disjoint interval/reserve, tail-unit iteration, labelled mesh and geometric reserve interfaces. Its checkpoint-000018, acceptance-000007 and manifest are the logical predecessor. The new digit block is not inherited as a theorem.

Read the complete saved canonical formal-conjectures124.lean response at ../mass-partition/sources/canonical-124-reading.txt. The canonical open declaration is erdos124.ne_zero, not erdos124.zero or the solved cutoff-one example. The original outer finite-base sum allows coincident values from different bases separately. This candidate strengthens the input assumptions and adds finite-deletion robustness; it preserves the positive-cutoff and eventual-quantifier meanings. No Lean build or declaration audit ran.

## Stop reason

The chosen fixed count is reached: five tier-one domain queries at each level, one direct API attempt per source, the eleven recorded general discovery/neighbour queries, the relevant primary sections and the stated canonical and accepted-proof reads. No exact result was found in this inspected material. Access limitations, noisy numeric searches and incomplete source coverage rule out any exhaustive novelty or priority claim. No mathematical process was launched.
