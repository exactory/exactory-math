# Independent review of the scalar statement and finite coverage

## Scope and verdict

This review compares `problem.json`, `DESIGN.md`, `BLUEPRINT.md`, and the declarations in `deterministic/formal-check-1/{Definitions,Finite,Main}.lean` with `attack/hall-n8-n15-branch-coverage/PROOF.md`, particularly Sections 3 through 5. The workspace `AGENTS.md` was read. No Lean command, heavy computation, or Git mutation was performed.

The stated scalar theorem and finite coverage match the intended claim. No blocking mathematical statement defect was found. This is a source-level statement review, not a successful compilation or kernel-audit report. At the reviewed snapshot, `Main.lean:10` contained the known temporary `sorry`; its removal and the final transitive axiom audit remain the implementation task's obligations.

All line references below refer to the reviewed snapshot. Changes made after this review require the corresponding references and conclusions to be checked again.

## Formula correspondence

| Quantity | Formal definition | Source statement | Assessment |
| --- | --- | --- | --- |
| gamma | `Definitions.lean:11` | Source proof, line 15 | Exactly `n! / n^n`, calculated in the rationals. |
| Proper permanent floor | `Definitions.lean:13` | Source proof, lines 24 to 26 and 225 | Exactly `gamma(n-a) * gamma(n-b) / gamma(n-a-b)`. |
| Marginal permanent floor | `Definitions.lean:15` | Source proof, lines 27 to 28 and 225 to 226 | Exactly `(n-2)! * ((n-2)/(n-1)^2)^(n-2)`. |
| Proper curvature | `Definitions.lean:23` | Source proof, lines 169 to 176 | Exactly `7*n*(n-a-b)^2 / (16*(a*(n-a)+b*(n-b)))`. |
| Marginal curvature | `Definitions.lean:21` | Source proof, lines 214 to 218 | Exactly `7*n*(1+(1-gamma(n))^2)/(16*(n-1))`. |
| Finite positivity criterion | `Definitions.lean:35` | Source proof, lines 225 to 235 | With positive curvature, `4*C*(M-gamma)-(n*M)^2 > 0` is equivalent to `M-gamma-n^2*M^2/(4*C) > 0`. |

The source proof also uses `C` for the product of column sums. The Lean name `curvature` refers to the scalar coefficient, so this notational reuse does not introduce an incorrect substitution.

The definitions use rational division, not natural-number division. Natural-number arithmetic occurs inside factorial arguments, exponents, omitted-size differences, and the integer denominator expression. On the admitted domain `0 < a+b < n`, both `a < n` and `b < n`, and `n-a-b >= 1`. Consequently the truncated natural differences agree with their ordinary integer meanings. In the proper branch, `a,b > 0`, both terms of `a*(n-a)+b*(n-b)` are positive, and every gamma argument is positive. In the marginal branch, `11 <= n` makes `n-2` and `n-1` positive. No zero denominator or unintended truncated difference affects an admitted case. Total definitions outside that domain do not enlarge the final theorem's hypotheses.

## Coverage and cardinalities

For each fixed dimension, ordered positive pairs with `a+b<n` number
`sum_{s=2}^{n-1}(s-1) = (n-1)*(n-2)/2`.

| n | Ordered proper pairs | Normalized marginal pairs | Reduced total | All original nonfull pairs |
| --- | ---: | ---: | ---: | ---: |
| 11 | 45 | 1 | 46 | 65 |
| 12 | 55 | 1 | 56 | 77 |
| 13 | 66 | 1 | 67 | 90 |
| 14 | 78 | 1 | 79 | 104 |
| 15 | 91 | 1 | 92 | 119 |
| Total | 335 | 5 | 340 | 455 |

The original domain has `2*(n-1)` marginal pairs in each dimension. Thus the 340 reported cases are normalized constant cases, and the final universal theorem covers 455 original ordered natural triples. The existing wording in `problem.json` and `Finite.lean` makes the normalization explicit and does not claim that 340 is the uncompressed count.

`Proper` at `Definitions.lean:26` imposes positivity on both sizes and the strict sum bound. `Reduced` at line 30 adds exactly `(n-1,0)`. In these dimensions this added pair is valid and disjoint from the proper branch. `Finite.lean:10`, 16, 22, 28, and 34 quantify over the full ordered product `Fin 15 × Fin 15`, with no ordering constraint such as `a <= b`. Thus no proper case relies on an unproved transposition reduction.

The natural-to-finite coverage theorem `reduced_good` at `Finite.lean:57` derives `a<15` and `b<15` from the domain, then separates all five dimensions. In particular, the largest normalized marginal coordinate, 14 at dimension 15, belongs to `Fin 15`. There is no off-by-one omission.

`all_good` at `Finite.lean:80` separates `a=0 or b=0` from the proper case. Both `floor` and `curvature` depend only on n in that branch, so substitution from `(n-1,0)` proves exactly the same `Good` proposition for every marginal size and both orientations. This is algebraic normalization of the defined constants. The analytical reason those constants apply to an actual marginal minimizing cut is a separate argument: the source proof selects a smallest row, or transposes first, at lines 93 to 101 and then applies stationarity in Section 4. Lean's normalization theorem does not formalize that matrix argument.

The full pair `(0,0)` is excluded by `0<a+b` in `all_good`, `scalar_positive`, and `scalar_exclusion`. This matches the approved scalar scope. The source's full-cut argument at lines 88 to 91 depends on Hall domination, total mass, boundary structure, and the strict permanent comparison. None of those conclusions is certified by the scalar theorem. Although the piecewise formulas are also defined at `(0,0)`, their totality does not assert that the marginal interfaces apply to a full cut.

## Real quantifiers and scalar deduction

The declaration at `Main.lean:6` has exactly the natural-size hypotheses in `problem.json` and quantifies over every real `u <= 1`, including negative u and both endpoints of `[0,1]`. It imposes no hidden lower bound on u. The source states the inequality on `[0,1]`; the larger proposed scalar domain is mathematically justified by the same argument. Bernoulli's inequality applies to `x=-u >= -1`, giving `(1-u)^n >= 1-n*u` for natural n. The completed quadratic is strictly positive for every real u whenever `Good` holds.

Explicitly, positivity of C and the finite margin gives

```text
C*u^2 - n*M*u + M-gamma
  = C*(u-n*M/(2*C))^2 + (4*C*(M-gamma)-(n*M)^2)/(4*C)
  > 0.
```

Multiplication of Bernoulli's bound by positive M establishes the desired strict scalar polynomial inequality. The extension to negative u concerns this polynomial theorem only. For example, the source's derivation of the matrix proper deficit interface uses `e+f >= p*u >= 0` at line 178. This review does not extend that matrix derivation to negative u.

The declaration `scalar_exclusion` at `Main.lean:13` uses precisely `P >= M*(1-u)^n`, `delta >= C*u^2`, and `P+delta <= gamma`. No sign assumptions on P or delta are needed: adding the two lower bounds contradicts the strict scalar positivity. The relaxed budget inequality is stronger in scope than the source's equality `P+delta=gamma` at lines 265 to 268 and follows from the same strict contradiction.

## Trust and findings

The finite propositions are evaluated from the direct factorial and rational definitions. `Finite.lean` contains `decide +kernel`, not a list of externally computed successful coefficient values, floating-point margins, imported Python verdicts, or new axioms. `reducedCases` at line 38 is a filter of the actual finite product by `Reduced`, so the cardinality claim refers to the same predicate as the finite criterion proofs. External arithmetic is not a mathematical premise of these declarations.

This source inspection cannot establish that the proof-producing tactics completed or that the final theorem has only standard transitive axioms. Those checks must use the completed files and fresh build/audit evidence.

No severity-high, severity-medium, or severity-low corrective finding was identified in the reviewed mathematical statements. The following informational scope boundaries should remain explicit in the final handoff:

1. `Main.lean:6` certifies an explicit scalar inequality after successful proof completion. It is not a theorem about matrices or a Lean formalization of the full Dittert conjecture.
2. `Finite.lean:80` certifies all defined marginal constant cases by equality of formulas. It does not prove the matrix selection and stationarity reduction.
3. `Main.lean:7` intentionally excludes `(0,0)`. Full minimizing cuts remain a separate analytical obligation for a matrix application.
4. `Main.lean:10` was the disclosed temporary proof hole at review time. This report neither treats it as a new finding nor considers the final theorem verified before its removal and the fresh axiom audit.

The design and blueprint already state these distinctions. No hidden matrix assumption, omitted proper transpose, unsupported dimension extension, or mismatch with the intended scalar claim was found.
