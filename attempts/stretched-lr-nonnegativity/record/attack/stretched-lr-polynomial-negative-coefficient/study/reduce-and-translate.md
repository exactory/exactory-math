# Strategy study: reduce-and-translate

Date: 2026-09-03. How a negative Ehrhart coefficient has been carried from one polytope
family into another, and which images of hive polytopes are in print. Contract:
`STUDY.md`. Sources saved under `study/sources/`.

## 1. Queries

| # | source | query | date | result |
|---|---|---|---|---|
| T1 | arXiv API | `all:Ehrhart AND all:negative AND all:coefficients` | 2026-09-03 | refused, HTTP 503 rate limit (`sources/arxiv-rt1-ehrhart-negative.xml`); the arXiv ids below come from the zbMATH records |
| T2 | Semantic Scholar | `paper/search?query=Ehrhart positivity negative coefficients polytopes examples` | 2026-09-03 | empty response (`sources/s2-rt1.json`) |
| T3 | zbMATH Open | `Ehrhart positivity negative coefficients` | 2026-09-03 | 12 records (`sources/zbmath-rt1.json`); documents 7040477, 8137114, 7079186, 902723871, 7064989 fetched (`sources/zbmath-<id>.json`) |
| T4 | Crossref | `query.bibliographic=Ehrhart polynomials with negative coefficients Hibi Higashitani Tsuchiya Yoshida` | 2026-09-03 | doi:10.1007/s00373-018-1990-9 and four papers on roots and small volumes (`sources/crossref-rt1.json`) |
| T5 | the problem's replay repository | `proof/ORDER_TRANSFER_3ROW_VERDICT.md`, `proof/GENERAL_KTT_PROOF_STATUS.md` (routes 2 and 4) | 2026-09-03 | the one worked transfer into LR polynomials and the recorded obstructions to flow and matroid transfers |

## 2. Hits worth reading

- Hibi, Higashitani, Tsuchiya, Yoshida, "Ehrhart polynomials with negative coefficients", Graphs Combin. 35 (2019) 363-371, doi:10.1007/s00373-018-1990-9, arXiv:1312.7049 and 1506.00467 (zbMATH record only; abstract not served): which coefficients of a lattice polytope's Ehrhart polynomial can be negative.
- Liu and Tsuchiya, "Stanley's non-Ehrhart-positive order polytopes", Adv. Appl. Math. 108 (2019), arXiv:1806.08403 (zbMATH 7079186; abstract from the problem-level study): order polytopes of dimension <= 11 are Ehrhart positive and a non-positive one exists in every dimension >= 14; the dimension-14 example O(P_{7,7}) has 255 lattice points and codegree 3.
- Liu, Xin, Zhang, "Order polytopes of dimension <= 13 are Ehrhart positive", Discrete Math. 349 (2026) 114833, arXiv:2412.07164 (zbMATH 8137114, review read): closes dimensions 12 and 13, so the first negative order polytopes are 14-dimensional.
- Castillo et al., "Smooth polytopes with negative Ehrhart coefficients", JCTA 160 (2018), arXiv:1704.05532 (abstract, problem-level study): smooth lattice polytopes in every dimension >= 3 with every possibly-negative coefficient negative; Berline-Vergne valuations as the positivity tool.
- Liu, "On positivity of Ehrhart polynomials", Assoc. Women Math. Ser. 16 (2019) 189-237, arXiv:1711.09962 (zbMATH 7064989, review read): survey of positive families, negative examples, and conjectures.
- Konoike, "On the magic positivity of Ehrhart polynomials of dilated polytopes", arXiv:2504.21395 (zbMATH 902723871, summary read): every polynomial with positive coefficients becomes magic positive after enough dilation; not a source of negatives.
- Ferudun 2026 and the repository (full text, problem-level study): the only transfer into LR polynomials in print realises a 3 x N transportation polytope as the LR polytope of a skew shape made of three disjoint horizontal strips, compatibly with dilation; it dies because every codegree-3 3 x 8 transportation polytope has >= 1050 lattice points (the target order polytope has 255) and the whole family is Ehrhart positive (minimum linear coefficient 2157/280). Recorded obstructions to other transfers: hive tangent cones have determinant 2, so hive polytopes are not network-flow polytopes and Lidskii positivity does not transfer; a hive face carries a U_{2,4} tight-normal restriction, so the tight-row systems are not regular matroids.

## 3. What was learned, as constraints on the plan

1. The image families with known negative coefficients (Reeve simplices, order polytopes from dimension 14, the smooth examples) all have many more facets or larger dimension than any hive polytope in the box (dimension <= 12 observed, 3 to 11 typical), and the one valid transfer (transportation polytopes as LR polytopes) needs partitions far outside the box (the 3 x 8 example has 9 and 10 parts). Inside the box, therefore, a translation cannot produce what the exhaustive enumeration of the box does not already contain; the strategy's use is outside the box (larger lengths), as a route to a counterexample to the unbounded conjecture.
2. A translation must keep dilation compatibility (the image's Ehrhart polynomial must equal P for every t), which the strip construction achieves by fixing the content globally; the recorded obstructions rule out flow and matroid images.
3. Route not to duplicate: the 3 x 8 transportation transfer and its family.

## 4. Stop reason

The tier-one floor was attempted for each source (arXiv refused, Semantic Scholar empty, zbMATH and Crossref answered); the last two productive sources (zbMATH and the repository) agree on the state: negative Ehrhart coefficients need dimension or facet counts beyond the box's hive polytopes, and the only transfer in print is dead.
