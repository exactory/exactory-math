# Independent local check of carry-seed move 2

Date: 2026-09-07.
Checker: host-provided agent identifier `/root`; host-provided context-window identifier: `01a07c97-8cc9-71c2-aaa8-861106b4f0bb`.
Target: `attack/erdos-124-carry-seed/moves/02-exchange-size-obstruction.md`.
Role: independent local mathematical checker. This report is not controller acceptance, harness certification, or final verification of the root objective.

## Finding and scope

I found no invalid deduction in the stated bounded-support obstruction, the vanishing-gain lemma, or the use of the inherited support ledger. The mathematical uses of ESS and Graham are supported by the supplied primary sources, in the positive-integer occurrence setting of this move. The warning about the two-copy counterexample is correct. These findings do not prove that all support-compatible seeds fail, establish signed unit identities in every pure-power tail, or settle the root objective.

I read both carry-seed moves in full, the supplied paired-perturbation move in full, and the ESS excerpt in full. I independently read the corresponding ESS HTML introduction, including the field assumption, group-rank definition, nondegeneracy definition, Theorem 0.1, and its discussion of uniformity. After reading the PDF skill, I visually read the four supplied Graham page images, printed pages 275-278, including all definitions and the complete proofs of Lemmas 1 and 4. I did not rely on the producer's statements that these sources had been inspected.

No mathematical program, formal checker, or subagent was used. No manuscript or harness-owned file was changed. Only this report was written. The accepted all-future surplus theorem and controller acceptance records were not supplied for this check; their truth and acceptance status are inherited assumptions, not independently certified here. The paired-perturbation construction was read to check the occurrence warning, not to issue a separate verification verdict on that entire construction.

## 1. Graham amplification and occurrence accounting

On page 277, Definition 5 uses coefficients in `{-1,0,1}` with finite support. Lemma 4 assumes that the same integer belongs to the signed-sum set of every tail. Its proof on pages 277-278 chooses a new signed representation beyond every index used for the preceding progression. Its two sides have distinct indices, and adding either side therefore preserves legality of the positive subset assignments. For positive integer sequences and positive step `h`, this gives progressions of arbitrary finite length; `h=1` gives arbitrarily long integer intervals. A possible initial zero can be omitted when positive integers are required. The conclusion does not specify where those intervals begin relative to the weights reserved for them.

On pages 275-276, the bounded-prefix-deficit condition is Graham's Sigma-sequence condition, and Lemma 1 concludes completeness for the interleaving `(s_1,t_1,s_2,t_2,...)`. The two component sequences occupy separate occurrence positions. Equal numerical values are allowed, but an application inside one original stream requires separate available labels. Thus it would be invalid to invoke this lemma by using the same original occurrences simultaneously in both components. Move 2 correctly identifies this restriction and does not make that deduction.

The statement about Lemma 4 is checked here for the positive integer streams actually under discussion. No extension to arbitrary real sequences is needed. Neither lemma, as used in move 2, proves the required residual inequality for a chosen finite exchange family.

## 2. ESS obstruction, including degenerate identities

The exact quantifiers justified by the proof are

`for every finite D subset of {2,3,...}, and every positive r,H, there exists a positive K(D,r,H), such that every signed sum using at most r allowed labels with all exponents at least K avoids every nonzero integer c with |c| <= H.`

The same cutoff works for all such `c`, signs, base assignments, and supports after `D,r,H` have been fixed. Any larger cutoff also works. There is no asserted cutoff uniform over varying `D`, support bound `r`, or difference bound `H`. Empty `D` is vacuous.

The deletion argument is valid. Removing a nonempty zero-sum subcollection preserves `c` and strictly decreases the number of terms, so the process terminates. Since `c` is nonzero, the final collection cannot be empty. It has no nonempty zero subsum and still uses at most `r` original labels, all with the original lower bound on their exponents. No replacement label or repetition is introduced. This handles original degenerate identities, including cancellations arising from numerical coincidences between different labels.

For fixed remaining length `t`, integer `c`, ordered bases, and signs, every coefficient `epsilon_i/c` is nonzero. Take the field to be `C`, which satisfies the source's algebraically closed, characteristic-zero assumption. The coordinate generators `(1,...,d_i,...,1)` generate a free abelian group of rank exactly `t`: a product of their integer powers equals the identity only when each `d_i` has exponent zero. This remains true when some bases coincide or are multiplicatively dependent as numbers, because the generators act in different coordinates.

The normalized equation has exactly the nondegeneracy required in ESS Theorem 0.1. That theorem bounds the number of nondegenerate solution vectors by `exp((6t)^(3t)(t+1))` for this group. Only finiteness is needed. Since each `d_i>1`, each coordinate uniquely determines its integer exponent. The finite union over `1<=t<=r`, `1<=|c|<=H`, base tuples, and signs therefore contains only finitely many surviving exponent tuples. Choosing a positive `K` above every exponent in that union contradicts any proposed equation entirely beyond `K`. It is harmless that the ambient group also permits negative exponents and tuples not satisfying all occurrence restrictions: restricting a finite solution set remains finite.

This does not show that all original degenerate solutions form a finite set. Such a conclusion is unnecessary and is not asserted. It shows that every original solution has a nonempty surviving subsolution with an exponent below the chosen cutoff.

The ESS source states a bound on the number of solutions, not their heights. It supplies no numerical cutoff through the proof given here. No gcd or reciprocal-sum condition is used. Consequently unit exchanges available at arbitrarily large cutoffs must have unbounded support size. The remark about bounded-size finite-difference gadgets is valid insofar as those gadgets are legal sums with coefficients `+1` or `-1` on at most a fixed number of available labels and have bounded nonzero output. It does not cover arbitrary unrestricted integer coefficients, growing output, or growing support.

The mathematical theorem in the supplied excerpt agrees with the HTML. The HTML's equation cross-references have inconsistent displayed numbers, but its written equation and theorem are unambiguous. I found no unsupported mathematical attribution to ESS. Journal metadata and DOI resolution were not independently checked outside the supplied sources.

## 3. Vanishing normalized gain

The elementary limit proof is correct under all its stated hypotheses: positive integer values, local finiteness, disjoint sides, pairwise disjoint unions, and one fixed upper bound `H_0` on the positive differences.

An empty `P_t` forces a nonempty `Q_t` with total at most `H_0`. Each such pair consumes an occurrence of value at most `H_0`; only finitely many exist. Apart from these finitely many pairs, `P_t` is nonempty. For any fixed `M`, only finitely many `P_t` can contain a value at most `M`, by local finiteness and disjointness. Hence eventually every nonempty `P_t` has total exceeding `M`, so `b_t -> infinity`. This argument does not require the pairs to be enumerated in increasing support order.

It follows that `B_s/s -> infinity`. Since `0 < H_s <= s H_0` and `W_s=2B_s+H_s`, eventually

`0 <= H_s/W_s <= H_0/(2B_s/s) -> 0`.

For unit differences, the switch choices represent precisely the integers from `B_s` through `B_s+s`. Thus `B_s/s` is the claimed baseline per unit of interval span. The ratio limit alone yields no lower bound on the residual maximum gap `K_(V_s)` strong enough to contradict `K_(V_s)<=s+1`. Inferring universal certificate failure from it would be invalid. Move 2 explicitly avoids that inference.

## 4. Inherited ledger and cutoff order

The maximum-gap identity in move 1 is sound. The finite-prefix union with its translate has the stated mesh bound. An attained positive maximum deficit gives an actual permanent gap because every later occurrence is at least its upper endpoint. Positivity, nondecreasing order, and integer values justify this step. For the infinite stream, local finiteness and unbounded subset sums ensure that consecutive subset sums and the next subset sum used in the covering argument exist.

Deleting the finite support `V` gives preceding retained weight `S_(i-1)-W_(i-1)`, hence exactly

`K_V = sup_(i notin V)(a_i-S_(i-1)+W_(i-1))`.

Conditional on the inherited limit `S_(i-1)-a_i -> +infinity`, this supremum is finite and attained among finitely many positive candidates. No effective bound on their indices follows from a bare limit assertion.

Disjoint switch choices have sums `B+FS(h_1,...,h_s)` and reserved weight `W=2B+H`. The stated Brown inequalities yield the full interval `[B,B+H]` of integers. Covering with residual subset sums works exactly when their consecutive gaps are at most `H+1`; the integer endpoint correction is correct. Algebraically this is precisely

`S_(i-1)-a_i + W-W_(i-1) >= 2B-1` for every retained `i`.

After the last reserved occurrence, the inherited surplus limit proves this inequality eventually for each already fixed family. Its threshold may depend on that family, in particular on `B`. It does not prove the inequalities at all the earlier retained indices. Choosing a new family changes both the threshold requirement and the deleted prefix weights. Move 2 preserves this quantifier order.

The growing-gap restrictions refer to this particular full-interval switch certificate. They are not necessary conditions for every conceivable completeness proof or every useful subset of `FS(V)`. A signed identity does not permit dropping its negative side while retaining its value as a positive assignment; the displayed baseline cost is exact. The separate fixed-buffer diameter argument in move 1 also correctly excludes only its stated universal finite-buffer replacement rule.

## 5. Warning about the paired-perturbation example

The supplied construction expressly gives exactly two labelled copies of each strictly increasing level `b_j`. A legal signed sum therefore has net coefficient between `-2` and `2` at each level. The relation `b_(2t+1)-3b_(2t)=1` needs three negative occurrences of `b_(2t)`, so that displayed relation alone is not a legal signed unit exchange. Allowing overlapping positive and negative representations would not repair this: cancel their shared labels, and the same net coefficient bound remains.

The relation is legitimately used in the supplied construction for gcd and nearest-integer-norm arguments, where unrestricted integer coefficients are allowed. Those arguments do not establish occurrence-respecting signed tail representation. The supplied move proves modular coverage, which likewise is not an exact signed unit identity. I found no proof of signed tail coverage or nearly complete subset sums in that supplied move.

The broader wording that neither property was proved anywhere in its entire "evidence package" cannot be independently certified from the supplied move alone. I did not inspect the rest of that package. This is a scope limitation on that historical assertion, not a defect in the mathematical occurrence warning.

## 6. Disposition limits

The findings support move 2 as an analysis of this bounded construction attempt. They do not establish that variable-length exchanges are impossible, that tail signed representability is insufficient for every alternative argument, or that the root is false or proved. In particular, the ESS cutoff depends on the prescribed support bound, and the gain limit does not settle the residual-gap inequalities.

I did not audit the claimed number of permitted strategy applications, method-failure registration, checkpoint acceptance status, or other controller records. Those administrative statements are outside this local check. The unresolved mathematical inputs remain the proposed legal seed family and a uniform proof of its retained-index inequalities for the intended base sets and positive cutoffs.
