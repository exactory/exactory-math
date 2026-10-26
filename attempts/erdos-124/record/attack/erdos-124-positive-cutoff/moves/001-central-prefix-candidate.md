# Move 1: a finite-deletion-stable central-prefix target

Date: 2026-09-06. Source: node-000001, move 1, pass 1.
Strategy: strengthen-and-generalise, step 2, strengthen-the-target.
Status: a candidate strengthening and an elementary implication, not a proof
of the candidate or of Erdős 124. Independent mathematical review is pending.

## Inputs and study constraints

The admitted problem and strategy studies identify the loss of Brown's initial
unit interval after low powers are deleted. BEGL96 and Bergelson-Simmons already
separate bounded gaps from interval production. This move does not claim that
bounded gaps or residue coverage produce an interval.

An additional web query on 2026-09-06 used
`"complete sequences" "central" "subset sums"` and
`"powers" "subset sums" "interval" "Erdős" "124"`.
No directly applicable central-prefix theorem was identified in the returned
results. This limited supplementary search is not a novelty certification.
The admitted tier-one strategy study remains the source for this opening move.

## Required operations

Let D and k satisfy the complete original claim. Delete any finite set F of
labelled occurrences (d,j), j >= k. Order the remaining occurrences by value,
breaking ties by increasing base label, as a_1,a_2,... . Set S_m=sum_{i<=m}a_i
and T_m={sum_{i in I}a_i : I is a subset of {1,...,m}}.

1. Further finite deletion replaces F by its union with another finite set.
   D, its gcd, and its reciprocal sum remain unchanged. The zero-cutoff target
   of representing every nonnegative integer does not survive this operation.
2. Raising k removes finitely many additional labelled occurrences and is
   therefore covered by the same operation. The constants below may change.
3. Appending the next unused occurrence gives exactly
   T_{m+1}=T_m union (T_m+a_{m+1}). There is no reuse of an occurrence.
4. Complementing a subset of the prefix gives T_m=S_m-T_m. A central interval
   is preserved by this symmetry.

Deleting a base can destroy the hypotheses and is not an operation proposed
for this argument. Common dilation changes the lattice and is also not used.

## Candidate C1

For every admissible D, every k >= 1, and every finite F as above, there exist
integers L >= 0 and m_0 >= 1 such that

    [L,S_m-L] intersect Z is contained in T_m for every m >= m_0.

The threshold L is independent of m, but may depend on D, k, and F. This is a
candidate only. Finite-deletion stability follows from its quantification over
F; it is not a claim that deletion preserves an arbitrary complete sequence.

## Deduction to the complete objective

Take F empty. The sequence has infinitely many positive terms, so S_m tends
to infinity. For any integer n >= L, choose m >= m_0 with S_m >= n+L. Candidate
C1 then places n in T_m. The selected indices give a finite set of distinct
labelled occurrences. Thus C1 implies the full all-D, all-positive-k claim,
with N(D,k)=L. Equal numerical values retain distinct labels throughout.

No converse is asserted. A counterexample to C1 would not by itself refute the
original claim.

## Exact extension condition

If [L,S_m-L] is nonempty and contained in T_m, its translate by a=a_{m+1}
is contained in T_{m+1}. The two integer intervals join without a gap when

    L+a <= S_m-L+1, equivalently a <= S_m-2L+1.

Under this inequality their union is [L,S_{m+1}-L]. If the inequality fails,
the two intervals alone do not prove central coverage. Other represented
values could still fill the gap, so failure of this sufficient condition is
not a counterexample to C1.

This is the elementary interval operation already underlying Brown-type
arguments, not a new completeness theorem. Its role is to expose the two
separate obligations: obtain a seed interval and justify the extension at
every subsequent scale.

## Costs, verification, and next question

The candidate pays object, implication, and obligations. It changes the local
target, proves only a deduction toward the original, and leaves both C1 and
its seed/extension mechanism unproved. Direction and mode remain undecided.

Verification here consists of the displayed exact subset-union identity and
integer endpoint inequality. No program or finite search was run. This record
is not controller-accepted mathematical evidence.

Next: preserve C1 as a hypothesis checkpoint, then develop its exact scope in
a separately reviewed branch. Test transparent examples and determine whether
the extension condition or the seed is the substantive obstruction. Preserve
the complete original root throughout.
