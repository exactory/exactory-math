# Move 1: a minimum-preserving reciprocal core

Node: node-000004. Entry: seed-and-amplify.
Reserved at controller revision 76.
Status: complete analytical proof candidate, pending independent result review.
No mathematical process or sample enumeration was used.

## Claim

For every nonempty finite set D of distinct integers at least 3, with
m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=1, there exists
E subset D containing m such that gcd(E)=1 and
1<=sigma(E)<1+1/m.

All reciprocal sums in this note are exact rational sums.

## 1. The augmentation lemma

Suppose B is a subset of D containing m, gcd(B)=1, and sigma(B)<1.
Adjoin the elements of D outside B in increasing order and stop at the first
set E whose reciprocal mass is at least one. A stopping set exists because
D is finite and sigma(D)>=1.

Write E=E_previous union {d} at that first crossing. Then
sigma(E_previous)<1. Also d is not m, since m was already in B, so d>=m+1.
Consequently

1<=sigma(E)=sigma(E_previous)+1/(d-1)<1+1/m.

Every intermediate set contains m and is a subset of D. Since a superset
of a gcd-one set has gcd one, gcd(E)=1. The last inequality is strict even
when d=m+1 because the preceding mass is strictly below one.

It therefore suffices to construct B with the stated seed properties.
This lemma proves preservation and the final bound before the seed is chosen.

## 2. Constructing a small gcd-one seed

Start with B_0={m}, whose gcd is g_0=m. While the current gcd g is greater
than one, choose the least d in D for which g does not divide d, and adjoin d.

Such a d exists: if g divided every element of D, then g would divide
gcd(D)=1, contradicting g>1. Moreover d is not already in the current B,
because g divides each of its elements. Thus each step adds a new element
strictly greater than m.

The new gcd is h=gcd(g,d), a positive proper divisor of g. In particular
h<g. The gcd therefore decreases as a positive integer and eventually
reaches one. This construction never assumes pairwise coprimality of bases.

Let q denote the number of additions and let B be the resulting set.
At least one addition is necessary because m>=3. After the first addition,
the gcd g_1 is a proper divisor of m, and hence g_1<=floor(m/2):
writing m=a g_1, the integer a is at least two.

Starting at g_1, a strictly decreasing positive-integer sequence has at most
g_1-1 further decreases before reaching one. Thus

q<=1+(g_1-1)=g_1<=floor(m/2),
|B|=q+1<=floor(m/2)+1<=m-1.

The last inequality holds for every integer m>=3. For m=3 both sides are
two; for m>=4 it follows from m/2+1<=m-1.

This argument constructs the seed using only gcd descent. The prime-witness
argument proposed in the study is unnecessary; no stronger unproved seed
claim is imported in its place.

## 3. The seed has reciprocal mass strictly below one

Every b in B satisfies b>=m, so 1/(b-1)<=1/(m-1). At least one element
of B is strictly greater than m, because at least one addition occurred.
Its inequality is strict. Therefore

sigma(B)<|B|/(m-1)<=1.

The seed contains m, has gcd one, and has mass below one, exactly as the
augmentation lemma requires.

Notice that sections 2 and 3 use only m>=3 and gcd(D)=1. They do not assume
that the seed already has mass at least one or contains a coprime pair.

## 4. Completing and optionally shortening the core

Apply section 1 to this B. The resulting E is a subset of D, contains m,
has gcd one, and lies in the required half-open reciprocal window.
This proves the claim for every admissible input D.

If a smaller inclusion-minimal output is desired, repeatedly delete an
element other than m whenever the deletion preserves gcd one and mass at
least one. Each deletion strictly decreases mass, so it also preserves
the strict upper bound. Finiteness makes this optional pruning terminate.
This does not claim minimum cardinality among all feasible outputs.

## 5. Quantifiers, cost, and contribution audit

The construction applies to every finite D in the claim, without a bound
on its cardinality or largest element. It keeps the original m and proves
both mass endpoints with the required strictness. No input hypothesis,
quantifier, or conclusion was weakened, and no unproved lemma remains in
this analytical argument.

The move decides direction=true and mode=construction while leaving the
claim, attacked statement, and stage unchanged. As a closing argument with
all seed and augmentation obligations discharged, it pays no remaining
cost in the ledger of CASHOUT.md. It does not borrow a hypothesis or an
external theorem.

For the original research objective, the only immediate contribution is
the choice of E in a proposed reduction. In particular, its mass is below
1+1/m<=4/3. This proves no eventual pure-power representation, no initial
represented interval, and no infinite extension bound. The restricted
coverage assertion and its implication bridge remain separate controller
obligations. Labelled powers and positive cutoffs occur only in those
later assertions, not in this finite-set lemma.

## 6. Entry and failure audit

The augmentation lemma was proved first. The seed was then constructed
for arbitrary D by finite symbolic gcd descent, with positive slack
1-sigma(B), and was extended to the requested object. No numerical seed
search or deterministic run was necessary. Step 2 of the strategy, which
would seek an extremal optimum, was inapplicable to this feasibility claim.
The forcing branch was likewise inapplicable.

The gain at each augmentation is positive, and the first-crossing argument
controls the final increment without assuming a uniform lower gain over
all inputs. The process is finite for each D because the total mass of D
is already at least one. The operation preserves the required gcd and
minimum. The seed-and-amplify failure conditions do not fire.

The optional pruning explains the limited sense in which the seed/output
can be shortened. Optimal reciprocal excess or cardinality is not claimed.
The elementary nature of the argument is not evidence of a standalone
publication-level advance.
