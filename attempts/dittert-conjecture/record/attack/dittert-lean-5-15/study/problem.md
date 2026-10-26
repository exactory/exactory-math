# Problem study: Dittert's conjecture for 5 <= n <= 15 as a kernel-checked Lean theorem

Claim under study: for every integer n with 5 <= n <= 15 and every n by n real matrix A with
nonnegative entries and total entry sum n, prod_i r_i(A) + prod_j c_j(A) - per(A) <= 2 - n!/n^n,
with equality if and only if every entry equals 1/n. Requested outcome: a proof whose formal
check in Lean 4 uses only propext, Classical.choice and Quot.sound.

## 1. Queries (source, string, date)

Tier one, run on 2026-09-06 by `scratch/study-2026-09-06/study_queries.py`; raw responses are
saved next to it (`arxiv-*.xml`, `crossref-*.json`, `zbmath-*.json`, `s2-*.json`).

| source | query string | result |
|---|---|---|
| arXiv API | all:"Dittert conjecture permanent" | 10 hits; see 2 |
| arXiv API | all:"van der Waerden permanent formalization Lean" | 10 hits, none about permanents in Lean |
| arXiv API | all:"Gurvits capacity stable polynomial formalization proof assistant" | 10 hits, none a formalization |
| arXiv API | all:"max-flow min-cut theorem formalization Lean Isabelle Coq" | 10 hits, none a Lean formalization |
| arXiv API | all:"Dittert conjecture Lean formalization" | 10 hits, none about Dittert |
| Crossref | the same five bibliographic queries | 5 rows each; see 2 |
| zbMATH Open | "Dittert conjecture permanent" | 7 records; the other four strings returned HTTP 404 (no record) |
| Semantic Scholar | "Dittert conjecture permanent", "van der Waerden permanent formalization Lean" | answered after backoff; the other three strings were rate limited (HTTP 429) and are recorded as not answered |
| GitHub code search (gh api search/code) | `"van der Waerden" permanent language:Lean`; `Gurvits capacity language:Lean`; `Dittert language:Lean`; `"max-flow min-cut" language:Lean` | 0, 0, 2, 0 hits; see 2 |
| google-deepmind/formal-conjectures tree | paths matching dittert, permanent, waerden | no file: no canonical formal statement exists |
| web search | "Lean 4 Mathlib formalization Gurvits capacity theorem van der Waerden permanent conjecture real stable polynomials"; "Dittert conjecture Lean formalization formal proof permanent 2026"; "Mathlib max-flow min-cut theorem formalization Lean 4 Ford-Fulkerson" | see 2 |
| local Mathlib checkout, rev 0df444a360eaa60ab8c11dca51a86af692955474 | grep for permanent, doublyStochastic, Birkhoff, Hall, GaussLucas, farkas, maxflow, Hurwitz, LinearProgram | see 3 |

Tier two: the local records of the eight finished attacks under `attack/` (STATUS.md,
FORMALIZATION_SCOPE.md, PROOF.md of dittert-branch-complete-audit, COVERAGE_PROOF.md of
hall-n7-branch-coverage, PROOF.md of hall-n8-n15-branch-coverage) were read in full.

## 2. Hits worth reading

- arXiv:2606.01531 (Pang), Proof of Dittert's conjecture for n >= 17. Abstract read. Settles the infinite range; not needed for 5 <= n <= 15.
- arXiv:2607.19439 (Kafidov), dimension 16. Abstract read earlier; its inequality fails at n = 15 (ratio 0.987, local attack 1).
- arXiv:2607.29191 (Li, Xiong, Yang), n = 4 by an exact constrained SOS certificate, with a Lean 4 formalization (v4.30.0-rc1) whose finite checks use `native_decide`. HTML full text read for the Lean section.
- github.com/arthurborgesdev/dittert-conjecture-n5 (2026-08-06): n = 5 by a symmetry-reduced SOS certificate and a Lean 4 formalization; README states the large finite checks use `native_decide`. README read.
- github.com/DCPRevere/maths-pub, combinatorics/permanents/cheon-hwang (2026-08-12, Apache-2.0, Lean v4.32.2): a Lean development for the Cheon-Hwang conjecture whose axiom freeze reports 4599 audited declarations, no sorry, no native_decide, standard axioms only. It contains `GurvitsUnconditional.gurvitsBound` (Gurvits's capacity theorem with no hypothesis), `egorychev_falikman` (van der Waerden), H-stability closure lemmas, and `DeficiencyHall`. Sources cloned to `scratch/study-2026-09-06/maths-pub`; a detailed read is recorded in `scratch/study-2026-09-06/maths-pub-report.md`.
- DOI 10.1016/j.laa.2010.08.041 (Cheon, Wanless), Some results towards the Dittert conjecture on permanents: Theorem 3.2 (maximizers are fully indecomposable) and Theorem 3.7 (no maximizer whose entire zero set is one rectangle) are the two structural inputs of the n = 8, 9, 10 route. Full text was read by the earlier audit (audit-n8-n9.md).
- DOI 10.1016/0024-3795(87)90032-2 (Hwang 1987): n = 3 and the support-stationarity condition. Abstract only.
- github.com/pedromnasc/dittert-conjecture-proof at 894066bbaa715138c98bf3cb7c6fdb4f39a37701 and github.com/lueluelue2006/dittert-n7-extension at 56397b70299278b338a286b90361180833dbf983: the assembled computer-assisted proof this formalization follows; full local reconstructions in attack/dittert-branch-complete-audit and its children.

## 3. What was learned, as constraints on the plan

1. No canonical formal statement exists; the theorem is stated here over `Matrix (Fin n) (Fin n) ℝ` with `Matrix.permanent` and read against the claim quantifier by quantifier.
2. Mathlib (rev 0df444a3) defines `Matrix.permanent` (multilinearity in rows and columns, transposition, permutation), `doublyStochastic`, Birkhoff's theorem, Hall's marriage theorem for finite sets, Gauss-Lucas, the maximum modulus principle, `IsCompact.exists_isMaxOn`. It lacks max-flow/min-cut, linear-programming duality in a usable finite form, H-stable polynomials and Gurvits's theorem. The dominated-doubly-stochastic theorem (Hall domination) must be built.
3. Gurvits's theorem and van der Waerden exist kernel-checked under Apache-2.0 (DCPRevere); the plan ports them instead of re-proving. Whether the per-variable degree-refined extraction needed for the rectangle floors is proved there is settled by the maths-pub report.
4. Both prior Dittert formalizations (n = 4, n = 5) rest on `native_decide`; the contract forbids it, and the local n = 5, 6 SOS certificates (Gram matrices 2925 and 8436) are not kernel-feasible as stored. The route for n = 5, 6 is open and is declared as an obligation without a route.
5. The mathematical route for 7 <= n <= 15 is fixed by the local computer-assisted proof: compactness, stationarity, the Hall cut parameter, a dominated doubly stochastic matrix, Gurvits floors, and dimensional scalar certificates. The n = 8, 9, 10 route also needs Cheon-Wanless 3.2 and 3.7 and the Pula-Song-Wanless two-zero floor, which are literature theorems to be formalized.
6. Kernel-checked scalar pieces already exist locally and are ported as sources: the n = 11..15 scalar certificates (hall-scalar-lean-n11-n15) and the n = 8, 9 near-zero polynomials (hall-near-zero-lean-n8-n9).

## 4. Stop reason

The fixed count was reached: one query per tier-one source for the claim and for its main
neighbours (van der Waerden, Gurvits capacity, max-flow), plus the code searches. Three
Semantic Scholar strings remain unanswered because of rate limiting and are recorded as such.
