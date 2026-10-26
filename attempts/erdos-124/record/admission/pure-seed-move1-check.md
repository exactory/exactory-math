# Independent analytical review of pure-power seed move 1

Date: 2026-09-07.

Reviewed artifact: `<workspace>/erdos-124/attack/erdos-124-pure-power-seed/moves/01-exact-coefficients.md`, read in full. The artifact identifies its source as `node-000007`, reserved move 1; those are producer references, not reviewer identifiers.

Actual host reviewer identifier: unknown. Actual host review-session or invocation identifier: unknown. No authenticated reviewer receipt was supplied, and this review does not invent one or certify host-level separation from the producer.

## Scope and disposition

I independently checked the deductions in Sections 2-4 from the definitions in the supplied artifact and checked the surrounding narrative for scope preservation. I read the installed Exactory Codex README before its math-solver instructions. No other research artifact or cited paper was inspected. No mathematical computation commands, experiments, attack initialization, controller mutations, or agent spawning were performed. This document is the only requested research write.

No mathematical error was found in Sections 2-4 under their stated power-stream assumptions. The fourth-moment obstruction and its uniform-integrability justification are valid. The exact translations and recurrence are also valid, but they do not establish seed coverage. The disposition is a sound bounded analytical review of a failed attempt with a residual hypothesis, not proof acceptance, root closure, or a novelty judgment.

## Section 2: exact coefficients and tilted probabilities

The finite product correctly counts selections of labelled occurrences. Repeated numerical values do not merge the corresponding factors: choosing different labels gives distinct selections and contributes the appropriate multiplicity to the same coefficient. Consequently, coefficient positivity is exactly equivalent to representability by a subset of the prefix. Complementation gives the stated symmetry about `S_m/2`.

The displayed quantifiers retain one fixed integer `L` for each admissible input, followed by arbitrarily large successful prefix indices. The condition `S_m >= 2L` prevents an empty central interval from making positivity vacuous. Neither coefficient notation nor complementation allows `L` to vary with the chosen prefix.

For a selection with sum `n`, multiplication of its independent Bernoulli probabilities gives

    exp(-t n) / product_i (1 + exp(-t a_i)).

Summing over such selections proves the probability identity. Every factor is strictly positive for finite real `t`, so the identity preserves support, including endpoints. The Fourier formula follows from finite expansion and integer-frequency orthogonality. No limiting interchange or local-limit assumption is needed.

The artifact uses the inherited term "admissible" without reproducing its entire definition. I can verify the coefficient equivalence for every stream defined here and preservation of the displayed quantifier pattern, but cannot audit the external admissibility definition against a controller contract that was outside the prescribed reading scope. In accordance with the supplied review mandate, the full producer target includes all admissible `D,k,F`, with fixed-`L` unbounded-prefix coverage.

## Section 3: finite-base Gaussian obstruction

The geometric bound is correct. For any base present in a prefix, its retained powers form a subset of the powers at or below its largest retained power `b`. Their squared sum is at most `b^2/(1-d^{-2})`. This remains true with an exponent cutoff, finite deletions, multiplicative relations between bases, or a prefix ending inside a numerical tie. Summing over labels and retaining the largest occurrence gives

    T_m^2 <= V_m <= C_D T_m^2.

Here `m >= 1` and `D` is nonempty, so `V_m > 0`. Fixed finite deletion preserves the infinite locally finite stream assumed in the artifact.

The normalization is exact: `E[X_m(0)] = S_m/2`, `Var(X_m(0)) = V_m/4`, and `Y_m` has mean zero and variance one. Independence of the symmetric signs removes every fourth-power term with an odd index multiplicity. Thus

    E[Y_m^4] = 3 - 2 (sum_i a_i^4)/V_m^2.

The largest occurrence supplies `sum_i a_i^4 >= T_m^4`, and the upper bound for `V_m` supplies the claimed uniform gap

    E[Y_m^4] <= 3 - 2/C_D^2 < 3.

The direction of each inequality is correct. The gap depends only on the fixed finite base set, not on prefix length or the locations of the fixed deletions.

The passage from distributional convergence to fourth moments is justified, rather than assumed. Writing `w_i = a_i/sqrt(V_m)` gives `sum_i w_i^2 = 1`, so the elementary bound on `cosh` implies

    E[exp(s Y_m)] = product_i cosh(s w_i) <= exp(s^2/2).

Applying the exponential Markov inequality separately to the two tails, with parameters `x` and `-x`, gives the stated bound `P(|Y_m| > x) <= 2 exp(-x^2/2)` for every positive `x`.

For a nonnegative random variable `Z`, tail integration gives

    E[Z^4 1_{Z>R}]
      = R^4 P(Z>R) + integral_R^infinity 4 x^3 P(Z>x) dx.

Applying this identity to `Z = |Y_m|` yields exactly the artifact's constants `2` and `8`. The endpoint term tends to zero, and the integral tends to zero because a polynomial times the displayed Gaussian exponential is integrable. Both estimates are uniform in `m`. This proves uniform integrability of the family `|Y_m|^4`; equivalently, the threshold on these fourth powers is `R^4`.

For completeness, if a subsequence converged in distribution to a standard normal `G`, then the bounded continuous functions `min(y^4,K)` would have convergent expectations. Uniform integrability controls the discarded tails uniformly along that subsequence, and integrability of `G^4` controls the limiting tail. Letting `K` increase therefore gives `E[Y_m^4] -> E[G^4] = 3` along the subsequence. This contradicts the fixed positive gap. The contradiction excludes every subsequence of prefixes tending to infinity, not merely convergence of the entire prefix sequence.

The scope restrictions in the artifact are appropriate. The proof concerns independent uniform choices at `t = 0` and normalization by the actual standard deviation, for a fixed nonempty finite `D`. It does not establish a gap uniform over base sets of unbounded cardinality, and it does not establish an obstruction for general tilted distributions. It excludes a standard normal distributional limit, without excluding non-Gaussian coefficient estimates or restricted Gaussian-shaped estimates that do not imply such convergence. It uses neither a gcd condition nor a reciprocal-mass condition. It provides no counterexample to seed coverage.

## Section 4: power recursion and the missing seed

The infinite products are well-defined as formal power series because the positive exponents tend to infinity. Substituting `z^d` shifts `j` to `j+1`, so the single-base functional equation is exact. The corresponding multivariate equation is exact as well.

Substitution of the same variable for every coordinate adds coordinate exponents. It is not extraction of coefficients having equal coordinate indices. After this substitution, the right-hand side still evaluates the multivariate series at the different arguments `z^d`. Therefore the displayed equation does not itself produce a recurrence for the univariate specialization under one common dilation. This observation should be read as a limitation of this identity, not a theorem excluding every possible scalar recurrence or other treatment of the factor structure.

The finite-prefix recurrence follows by separating selections according to whether they use the new occurrence. For a nonempty certified old interval `[L,S_m-L]`, the new translated interval is `[L+a_{m+1},S_m-L+a_{m+1}]`. The two integer intervals are adjacent or overlap exactly when

    L + a_{m+1} <= S_m - L + 1,

which rearranges to the stated condition `S_m-a_{m+1} >= 2L-1`. When this holds, their union contains `[L,S_{m+1}-L]`. The condition is necessary and sufficient for these two certified intervals to meet or be adjacent; it is not asserted to be necessary for coverage by the full support, which might contain additional sums.

The referenced "accepted surplus theorem" was not supplied for review. Its hypotheses, acceptance status, and application to every admissible input cannot be independently certified here. Conditional on its supplying the stated eventual inequality for fixed `L`, the recurrence propagates an already represented interval. It does not supply an initial interval at or beyond the propagation threshold. Thus this external reference does not close the missing seed within the argument reviewed.

The warning about deletion is correct: coefficients of a product can be positive even when coefficients of a remaining factor product vanish. No coefficientwise positivity conclusion follows by division. The undeleted functional identities are explicitly labelled as such, and the supplied argument makes no invalid deletion inference.

## Full objective and residual hypothesis

The opening status, Section 2's quantifiers, the limitations following Section 3, and Section 5 consistently leave the full seed theorem open. Neither the reformulation nor the obstruction is presented as its proof. No coefficient lower bound or represented central interval is obtained.

The proposed strict-surplus hypothesis remains prospective. The artifact does not prove that a macroscopic band exists, that a band has the fixed-endpoint form required by the seed target, or that it can start permanent coverage. Its statement that a separate exact scope, study, admission, and proof are needed is appropriate. Equality remains an explicit unresolved obligation, so restricting a possible successor to strict surplus does not silently replace the full admitted target.

No novelty assessment was made, from memory or otherwise. The cited literature and inherited studies were not checked. This review records the correctness and limits of the supplied elementary argument only; it does not supply a controller acceptance receipt or authorize any new research work.
