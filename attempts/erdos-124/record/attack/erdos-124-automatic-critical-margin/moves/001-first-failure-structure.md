# Move 1: first-failure structure and the common-divisor exclusion

Node: node-000023. Strategy: attack-the-negative-side, plan step3.
Entry: extract-structure-from-a-hypothetical-counterexample.
Reservation: revision446, move-node-000023-1.
Status: analytical partial-result candidates, not independently accepted.
No mathematical process, enumeration, solver or formal build was run.

## 1. Exact target and temporary assumption

The admitted claim is unchanged: for every nonempty finite set V of distinct
integers at least4, with sigma(V)=sum_d 1/(d-1)=1 and a multiplicatively
independent pair, H(x)>x for all real x>1. Here p_d(x) is the first
nonnegative integer power of d at least x and

    H(x)=sum_{d in V}(p_d(x)-1)/(d-1).

Assume temporarily that this claim fails. The negative direction below is
this assumption, not a proved counterexample. Each summand in H is an
integer geometric sum. Write v=|V| and g=gcd(V).

## 2. A failure is an exact tight integer power

For every real x>1 put q=min_d p_d(x). Independence ensures that the
p_d(x) are not all equal: equality for the independent pair would equate
positive powers of its two bases. Exact mass one gives

    H(x)=q-1+sum_d (p_d(x)-q)/(d-1)>q-1.

Both H(x) and q are integers. Consequently H(x)>=q. If H(x)<=x, then

    q<=H(x)<=x<=q.

Thus every failing real scale is already an integer q, is a positive power
of a base in V, and satisfies H(q)=q. In particular, unlike the inherited
integer-witness reduction alone, there is no failure at a noninteger scale
or at an integer which is not a power in the supply. At that scale,

    sum_d (p_d(q)-q)/(d-1)=1.                         (1)

All terms are nonnegative. Hence for each d

    q<=p_d(q)<=q+d-1,
    p_d(q)=d ceil(q/d).                              (2)

The second equality follows because p_d(q) is a multiple of d and the
closed interval [q,q+d-1] contains exactly one such multiple. It states
that this next multiple must itself be a power of d. These are necessary
alignment conditions, not a sufficient characterization of failure unless
the exact sum (1) is also retained. No bounded all-V domain is inferred.

## 3. Common divisors exclude every failing scale

Suppose g>1. Set L=product_{d in V}(d-1), a positive integer coprime to g.
The exact mass identity says L=sum_d L/(d-1). Modulo g each d-1 equals
-1, so L/(d-1) is congruent to -L. Therefore

    v=-1 modulo g.

For x>1 the geometric sum (p_d(x)-1)/(d-1) is congruent to1 modulo g:
its initial term is1 and all later terms are divisible by g. Thus

    H(x)=-1 modulo g.

The integer q=min_d p_d(x) is divisible by g. Section2 gives H(x)>=q;
the congruence improves this to

    H(x)>=q+g-1>=x+g-1.                             (3)

This proves the following precise partial-result candidate: under the
admitted hypotheses, if gcd(V)>1 then H(x)-x>=gcd(V)-1 for every real
x>1. In particular, every counterexample to the admitted claim has
gcd(V)=1. No divisibility property of V is inserted into the full claim.
This is a genuine exclusion of an entire family, not the old per-base
normalization condition from node15. That failed operation stays failed.

## 4. Additional restrictions on the first failure

Let s=min V. In fact v>s. If v<=s, distinctness bounds sigma(V) by
sum_{i=0}^{s-1}1/(s+i-1), which is at most

    1/(s-1)+1/s+(s-2)/(s+1)<1.

For s>=4 the last strict inequality is equivalent to
s^2-4s+1>0. This contradicts sigma(V)=1. Therefore H(x)=v>x on
1<x<=s, and a first failing scale q must exceed s.

If a failure exists, take the smallest one. Section2 makes it an integer
power q>s. Let r be the largest numerical power d^j with d in V, j>=1,
and d^j<q. Such r exists because s<q. Let c>=1 count the distinct labels
of value r; coincident values keep their multiplicity. Between r and q
the geometric prefix changes only when these c occurrences are included.
The exact jump is

    H(q)=H(r)+c r.

Minimality gives H(r)>r, hence H(r)>=r+1. Consequently

    q>2r.                                          (4)

The first failure is thus at a power following a multiplicative gap
greater than two. This is a further necessary restriction. It neither
asserts that such power gaps never occur nor settles their weighted prefix.

## 5. A nonempty critical family and its exact CP28 contribution

The family excluded in Section3 is nonempty. A hand identity is

    1/3+1/5+1/7+1/9+1/11+1/15+1/35+1/45+1/231=1.

With denominator3465 its nine numerators are
1155,693,495,385,315,231,99,77,15, whose sum is3465.
Thus

    V={4,6,8,10,12,16,36,46,232}

has exact mass one, minimum4 and gcd2. The bases4 and6 are
multiplicatively independent, since a positive power of6 has a factor3
and a power of4 does not. Formula(3) gives H_V(x)>=x+1 for every x>1.
This finite arithmetic example was checked by hand, not by a program.

Conditional on acceptance of the new lemma, accepted CP28 applies to
every original D having its other structural hypotheses and such a
common-divisor critical complement. For the displayed V take R={3}
and D=R union V. The radix supply has mass one half, gcd(D)=1, and all
positive cutoffs and finite labelled deletions follow from CP28.
This statement is a deduction to be preserved and reviewed in the
separate special-case branch, not an acceptance of that branch here.

The example is outside CP27's strict-complement structural criterion:
any witnessing radix set must contain3 so that the complement has
minimum at least4. Its integer radix must then be3, and no other base
in this D is a positive power of3. Its complement consequently has
mass exactly one, not strictly greater. This comparison does not claim
that no other theorem can settle the particular example.

## 6. Entry result, costs and next hypothesis

The entry produced new restrictions: every failure is a tight integer
power with the alignment (2); a first one obeys (4); all common-divisor
inputs are excluded by the quantitative bound (3). This is more than
the inherited CP28 finite test. No actual no-compression failure has
been observed in this application, and no process or impractical finite
residue has been handed off. A positive object cannot satisfy H(q)=q;
the necessary subconditions alone are not presented as a complete test.

The full admitted claim remains open on gcd(V)=1. The working target
has become a necessary-condition list under a temporary counterexample
assumption. The move pays object and obligations, not implication:
proving the remaining class empty would return to the exact original
claim, while a true counterexample would still require every original
assumption. The restriction itself does not provide either conclusion.

Before further mathematics, journal this application and follow the
required strategy reassessment. Preserve a stable checkpoint of the
partial argument, explicitly without full-claim proof credit. Develop
the common-divisor result and its CP28 application in a separately
studied and reviewed special-case attack, keeping this all-V attack
open. The potential next full-scope question is whether the tight-power
alignment and first-gap condition on the remaining gcd-one sets force
another arithmetic restriction or admit an exact counterexample.
That is a hypothesis, not an executed second move or a new reservation.
