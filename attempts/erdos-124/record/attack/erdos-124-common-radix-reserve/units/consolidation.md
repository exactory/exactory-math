# Consolidation of the common-radix reserve proof

Date: September 8, 2026.
Trigger: the admitted node closed at journal move1. This harness entry is
outside the move budget and adds no research move.

## Marked steps and replacements

The argument has no computational input. Four transitions need explicit
justification: preservation of original exponent labels after normalization,
conversion of congruence information into an exact signed unit, assignment of
disjoint support roles, and a positive reserve gap fixed before seed construction.

The proof in moves/001-common-radix-reserve.md makes each transition explicit.
Its Sections2-3 replace any finite alphabet enumeration by the standard
signed-prefix interval induction and a geometric strict-prefix sum. Section4
uses only eventual periodicity in a finite residue set and Bezout's identity;
the recurring residues permit nonnegative coefficients on distinct late labels.
Sections5-6 prove the reserve gap directly by positive subset-sum induction.
Section1 states and proves the amplification law before the concrete seed,
including its support-preservation condition and smallest positive increment.

No constant is lost in these replacements. The signed threshold remains1/2,
the reserve threshold remains1, and both equality boundaries are retained.
The finite-deletion loss belongs solely to the reserve's fixed constant M;
later seed supports lie on different base labels and do not change M.

## Rewritten proof and role of each step

Fix the exact quantified D,k,F and any witnessing B,A,C. Put
R={B^a:a in A} and U=D minus (R union C).

1. Section6 fixes g=ceil(sum_{d in U}d^k/(d-1)+sum_{F_U}d^j).
   Section5 proves that the unchanged reserve meets every interval of g
   nonnegative integers.
2. For any finite forbidden seed support, choose K beyond all its exponents.
   Section3 aligns exponents at a common L and represents every multiple
   of B^L by a signed sum on R labels of exponent at least K.
3. Section4 produces z congruent to1 modulo B^L on distinct late C labels.
   Add an R representation of1-z. Positive and negative supports give a
   fresh legal unit pair without any U label.
4. Section1 repeats this g-1 times while excluding both supports of all
   previous pairs. The resulting positive sums fill [H,H+g-1].
5. For every n>=H+g-1, the reserve supplies v in
   [n-H-g+1,n-H]. Then n-v lies in the seed interval. Disjoint labels make
   their union a legal positive representation. Set N=max(1,H+g-1).

The complete lemmas and their endpoint checks are in the cited proof,
Sections1-7. This rewrite is an exposition of that proof, not new evidence
or a second independent proof.

## Second route check

A direct positive-prefix induction still requires an initial seed interval.
A modular-only argument gives no exact integer equality. Neither removes
the main aligned signed-lattice step under the stated hypotheses. No genuinely
independent second proof is claimed.

## General statement and limits

The abstract interface actually proved in Sections1 and5 is that a supply
with fresh legal signed-unit pairs after every finite deletion, together
with a disjoint g-syndetic positive subset-sum supply, is eventually complete.
The common-radix condition is a sufficient way to supply the first part.

This is not an arbitrary-base half-mass theorem and does not settle the
original reciprocal-mass-one objective. Section8 proves an additional binary
range containing4,8,32 without16, while explaining why B>=4 is vacuous.
The individual lemmas are not split into separate novelty claims.
Independent result review and controller acceptance remain required.
