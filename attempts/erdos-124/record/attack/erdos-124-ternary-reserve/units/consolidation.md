# Consolidation of the ternary-reserve candidate

The native closing move is move 1. The exact admitted claim remains in
problem.json and moves/001-ternary-reserve.md. This consolidation is a
harness entry, not a new mathematical move or accepted result.

## Marked steps and replacements

The possible unexplained steps were the use of balanced ternary, the
existence of a sufficiently high power congruence, the passage from
signed digits to legal positive choices, and the reserve's bounded-gap
property. All were replaced by explicit elementary arguments in the
proof artifact. No computational input or published deep completeness
theorem is used. The gap lemma retains labels when values coincide.
No marked step still requires an external theorem or a new hypothesis.

## Rewritten argument and the role of each step

Fix the independent reserve before choosing any seed. Its reciprocal
mass at least one bounds its ordered deficit, so its finite subset sums
meet every g consecutive nonnegative integers for an input-dependent g.
This follows from the geometric prefix inequality and the elementary
finite-prefix mesh induction in Sections 4 and 5 of the proof.

For bases three and b coprime to three, choose a sufficiently high
power b^J congruent to one modulo 3^K. Expand (b^J-1)/3^K in balanced
ternary. Separating signs gives two finite legal positive alternatives
with difference one and exponents at least K. Choose each new K beyond
all forbidden exponents and both supports of every earlier pair.

The first g-1 pairs supply [A,A+g-1], as their g choices of how many
pairs to switch increase the baseline A by zero through g-1. The seed
and reserve have disjoint base labels. For n>=A+g-1 choose a reserve
sum in [n-A-g+1,n-A], and represent its difference from n on the seed.
These are exactly Sections 1-3 and 6, not omitted new lemmas.

The claim's mass bound ensures that the reserve exists: gcd(D)=1 and
3 in D give some b>=4 coprime to three, and removing three and b loses
at most 1/2+1/3. Hence total reciprocal mass at least 11/6 leaves at
least one. This calculation includes the boundary.

## Independent second route

The older accepted three-group criterion reaches only the larger
minimum-three threshold 13/4. It is not a second proof of this exact
11/6 result. A direct coefficient-count argument or ordinary ternary
digits would still need the missing interval argument. No independent
second route to the exact claim was found or is claimed. The argument
above is already elementary and computation-free.

## General statement actually proved

For any finite set D of integer bases at least three containing 3 and
some b coprime to three, if sigma(D minus {3,b})>=1, then every
positive-cutoff labelled power supply on D remains eventually complete
after every finite labelled deletion. The proof is Sections 1-6 with
the reserve inequality as a direct hypothesis. This extracted statement
is a local corollary and prospective successor input, not a replacement
for the admitted claim or a separately accepted controller obligation.

More abstractly, the proof combines tail-disjoint unit alternatives
with a separate bounded-gap supply. Without that separate supply it
does not imply completeness. This is the exact additional input absent
from the earlier refuted abstract signed-unit implication.

## Status and limitations

The local mathematical ledger is empty: the claim and quantifiers are
unchanged, all introduced lemmas are proved, and no effectivity or
constructivity is lost. The result still needs independent result
review and controller acceptance. No formalization, publication claim,
optimality claim, or full-root completion is asserted.
