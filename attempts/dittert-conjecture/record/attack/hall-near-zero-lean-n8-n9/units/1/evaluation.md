# Independent Stage 8 evaluation

Date: 2026-09-05. Verdict: PASS for the local formalisation unit. No blocking or corrective finding remains.

I did not write the draft or its formal proof. I read the installed Codex runtime instructions, math-solver Stage 8 and CASHOUT.md, then reviewed the actual evidence package and reran its mathematical verification. The complete technical report, commands, measured resources, source hashes, and axiom outputs are in `../../independent-review.md`.

## Statement and evidence

The statement in draft paragraph 1 matches `unit.json`: every real u in the closed interval [0,1/400] satisfies p_8(u)>0, and every real u in [0,1/500] satisfies p_9(u)>0, for the exact literal definitions and only Lean's three listed standard axioms. There is no coefficient hypothesis or omitted endpoint. This is a mathematical claim with an attached formal certificate, not merely a report of research activity.

| Draft claim | Evidence checked | Assessment |
| --- | --- | --- |
| Literal two-polynomial conjunction | `../../DEFINITIONS.md`, package `Definitions.lean` and `Main.lean:4` | Exact constants, intervals, quantifiers, and conclusion match. |
| Degrees 16 and 18, with 17 and 19 positive homogeneous coefficients | Package `Certificate8.lean`, `Certificate9.lean`, `candidate-data.json`; reviewer `../../study/independent_coefficient_review.py` | All 36 exact constants and exponent pairs match the inherited independent Bernstein implementation; leading coefficients are nonzero. |
| Literal identities are proved, not presumed | `identity8`, `identity9`, their full source, and fresh direct axiom audits | Both identities quantify over every real x and unfold the actual formula. |
| Strict positivity and exact rescaling | `positive8`, `positive9`, `Main.lean`, and `../../PROOF.md` | Nonnegative summands, a positive first term for x<1, a positive last term at x=1, and exact rescaling cover both closed intervals. |
| Generator contributes no proof premise | Full source imports and all five axiom lists | Confirmed. No generated table is assumed correct by the theorem. |
| Initial proof-hole gate and noncomputable repair | `../../INITIAL_RED_GATE.md`, `../../ATTEMPTS.md`, retained successful build logs | These are identified historical development records, not premises of the final result. The final source and fresh audits have no proof hole. |
| Standard axioms for all principal declarations | Package `Audit.lean`, `axioms.log`, reviewer direct audit, and standalone replay | Exactly propext, Classical.choice, Quot.sound for all five declarations. |
| Limited relationship to Hall coverage | Inherited `hall-n8-n15-branch-coverage/PROOF.md` Section 6 and `independent_coverage.py` | Polynomial and cleared-denominator formula match. Broader matrix and support arguments remain outside scope. |

Short source filenames in the draft refer to `../../deterministic/formal-check-1/`. In particular, both references to `axioms.log` resolve to `../../deterministic/formal-check-1/axioms.log`. The problem, strategy, and unit studies were read; the unit's journal excerpt agrees exactly with journal move 2, and the unit digest agrees with `check-unit.json`.

## Reproduction

The fresh harness invocation passed in 21.14 seconds with maximum RSS 1507786752 bytes. A separate `nice -n 15 lake env lean -j1 -M2048 Audit.lean` invocation passed in 7.77 seconds with maximum RSS 1506852864 bytes. The independent coefficient comparison passed in 0.10 seconds with maximum RSS 14630912 bytes. The actual standalone `replay.sh` also passed in 31.84 seconds with maximum RSS 1506197504 bytes and printed every principal axiom list. All checks were sequential, with cached dependencies. These are incremental verification timings, not clean-install or total-development costs.

The inspected proof files use the pinned Lean v4.33.1 and Mathlib commit `0df444a360eaa60ab8c11dca51a86af692955474`. No native evaluation or custom axiom occurs in the audited closure. No publication, commit, or immutable-checkpoint update was performed by the reviewer.

## Reference resolution and position

All external draft references resolve to the identifiers recorded in the studies or known list:

1. DOI 10.1017/S0960129511000090 resolves to Bertot, Guilhot, and Mahboubi's *A formal study of Bernstein coefficients and polynomials*. The publisher record supports the earlier Bernstein-formalization description.
2. DOI 10.1007/s10817-012-9256-3 resolves to Munoz and Narkawicz's *Formalization of Bernstein Polynomials and Applications to Global Optimization*. The publisher abstract supports its characterization as earlier formal verification of Bernstein methods.
3. arXiv:2607.29191v2 resolves to Li, Xiong, and Yang's dimension-four Dittert certificate paper. The versioned abstract states that the exact certificate is formally verified in Lean.

Resolved primary URLs and the lookup limitation for direct DOI opening are recorded in `../../independent-review.md`. No external citation is substituted for the local proof. The novelty studies openly record rate limits, and the draft makes no priority or new mathematical Dittert-theorem claim.

The position note correctly classifies this as a formalisation supplement on the path to a broader verification target. The underlying inequalities and Bernstein method are already known. PASS here means that the bounded formal artifact is correct and the draft faithfully represents its evidence; it does not assert journal-level novelty or readiness to publish a full Dittert proof.

## Reviewed snapshot

The reviewed draft SHA256 is `eaecaff042468cb92138b1f7b467820c25044ca2f29697473dbce937229f5567`. The reviewed unit SHA256 is `34a09e29ea8c40d1af6785a22278facd20f53d595fe746c19c6ad9e9fe2a7155`. Exact formal-source hashes are retained in the independent report. A substantive change to the statement, formula, proof source, or draft claims requires corresponding review; prose packaging does not enlarge the theorem's verified scope.
