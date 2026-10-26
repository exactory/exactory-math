# Move 1: a quarter-mass surplus for labelled pure powers

Node: node-000011. Strategy: make-the-proof-constructive.
Entry: seed-and-amplify. Reservation: controller revision 209.
Status: analytical proof candidate, pending independent result review.
No mathematical program, enumeration, or formal checker was run.

## Claim

For every nonempty finite set D of distinct integers at least 3, with m=min D, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=3+min{1/4,2/m}, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

Write sigma(A)=sum_{d in A}1/(d-1). All fractions below are exact.
A base partition is a partition of base labels. Equal numerical powers
of different bases remain different occurrences.

## 1. Accepted amplification and the exact input to improve

We use two already accepted local proofs, with their immutable evidence:

- [Core] acceptance-000001, checkpoint-000008,
  ../erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md.
- [Mass] acceptance-000005, checkpoint-000016,
  ../erdos-124-mass-partition/moves/001-high-mass-completeness.md.

The relative paths above start in this attack directory, not this
moves directory. From this file they have an additional ../ prefix.

Sections1-3 and5-6 of [Mass] establish this explicit intermediate
criterion, independently of the numerical threshold in its Section4:

If D is partitioned into nonempty C,B_1,B_2 with gcd(C)=1 and
sigma(C),sigma(B_1),sigma(B_2)>=1, then every positive cutoff and every
finite labelled deletion of the resulting power supply leave a complete
labelled subset-sum sequence.

Here is the input audit. For A equal to one of the groups and fixed k,F,
Section5 of [Mass] bounds the ordered deficit by

    K_A = sum_{d in A} d^k/(d-1)
          + sum_{(d,j) in F, d in A} d^j.

Thus its subset sums have bounded gaps, including after any further
finite deletion. The proof uses all terms of value strictly below
the current value, so tied values are not deduplicated.
For the correction group, gcd(C)=1 implies divergence of

    sum_{(d,j) in the remaining C supply} ||beta*d^j||

for every nonzero beta in R/Z. The nearest-integer recurrence and
collective-gcd proof are in [Mass, Section5.2]; no pairwise coprimality
or multiplicative independence is required.

The occurrence-preserving criterion in [Mass, Section3] extracts a
finite correction support E from C, makes the subset sums on
B_1 union B_2 union E thick, and then selects an interval as long as
the gap bound of C minus E. These supports are disjoint by label.
The amplification lemma in [Mass, Section1] then covers every
sufficiently large integer. The gap bound is computed after removing
E, so the correction is not counted twice.

This supplies the amplification before the new seed allocation.
Its published additive input is Bergelson-Simmons,
arXiv1507.02208v2, DOI10.4064/aa8221-10-2016, Lemma2.12, citing the
Bergelson-Furstenberg-Weiss sumset theorem. Fan2607.14071v3,
Lemma2.2, supplies the finite-correction method. The labelled
extension is proved in [Mass], not assumed from a numerical-set theorem.

The only new work below is the quantitative finite partition.

## 2. A sharper reciprocal core

We prove the following finite lemma.

For every finite D of distinct integers at least three, with
m=min D, gcd(D)=1 and sigma(D)>=1, there is C subset D containing m,
with gcd(C)=1 and

    1 <= sigma(C) < 9/8.

For m>=8, [Core] already gives a minimum-preserving C with
sigma(C)<1+1/m<=9/8. We therefore treat 3<=m<=7.

Use exactly the gcd-descent seed construction of [Core]. Start with
{m}; while the current gcd g is greater than one, add the least d in D
not divisible by g. The gcd strictly decreases. The completed seed B
contains m, has gcd one, has sigma(B)<1, and has at most
q<=floor(m/2) elements other than m, as proved in [Core, Sections2-3].

Adjoin D minus B in increasing order until the reciprocal mass first
reaches one. This stops because sigma(D)>=1. Call the stopping set C,
and call the last added base d_*.
If d_*>=9, then

    sigma(C) < 1+1/(d_*-1) <= 9/8.

It remains to handle d_*<=8. This also requires checking whether
the original gcd seed contains a base larger than eight.

### 2.1 A large gcd-seed element prevents an early crossing

Suppose B contains a base greater than eight. Immediately before
the first such base was selected, the current gcd g was greater
than one and divided every element of

    S = D intersect {m,m+1,...,8}.

Indeed, otherwise the least eligible base would have been at most
eight. Since m belongs to S, gcd(S)>1 and gcd(S) divides m.
The possible small bases therefore lie in the following sets.
The upper bound in the last column also includes all possible
large seed elements, at most floor(m/2) of weight at most1/8 each.

| m | A set containing S | Upper bound for sigma(S union B) |
|---|---|---|
| 3 | {3,6} | 1/2+1/5+1/8 = 33/40 < 1 |
| 4 | {4,6,8} | 1/3+1/5+1/7+2/8 = 389/420 < 1 |
| 5 | {5} | 1/4+2/8 = 1/2 < 1 |
| 6 | {6,8} | 1/5+1/7+3/8 = 201/280 < 1 |
| 7 | {7} | 1/6+3/8 = 13/24 < 1 |

For m=6, the nontrivial common divisor is 2,3 or6; every resulting
possibility is contained in {6,8}. The other rows follow directly
from the nontrivial divisors of their listed m.
The bound does not charge small seed elements twice: their mass
is included in sigma(S), and only elements outside S need the
additional bound. Using the total q for that additional bound is
a harmless overestimate.

If d_*<=8, every adjoined element is in S, so C is a subset of
S union B. The table would give sigma(C)<1, a contradiction.
Thus an early crossing cannot occur when the seed has a large element.

### 2.2 A small seed when m is at least four

Now B is contained in {m,...,8}. At an early crossing, so is C.
If m>=4, then

    sigma(C) <= 1/3+1/4+1/5+1/6+1/7
             = 153/140
             < 9/8.

This deals simultaneously with m=4,5,6,7. Nothing about the order
of the seed and its later augmentation is needed in this case.

### 2.3 The minimum-three cases

For m=3, the gcd seed is {3,b}, where b is the least base in D
not divisible by three. Since the seed is contained in {3,...,8},
the only possibilities are b=4,5,7,8.

If b=4, augmentation starts with mass1/2+1/3=5/6.
An early first crossing has one of these forms:

- If5 is present, the crossing mass is13/12.
- If5 is absent and6 is present, it is31/30.
- If5 and6 are absent and7 is present, it is1.
- If5,6,7 are absent, adjoining8 gives41/42<1, so there is no early crossing.

Every listed crossing mass is less than9/8.

If b=5, base4 is absent. The seed mass is3/4.
Adjoining6, when present, gives19/20<1.
If6 and7 are both present, the first crossing is at7, with mass67/60.
If6 is present but7 is absent, a crossing by8 has mass153/140.
If6 is absent but7 is present, a crossing by8 has mass89/84.
If neither6 nor7 is present, the mass after8 is25/28<1.
All three possible crossing masses are less than9/8. The case
with6 and7 present stops before8 and must not be charged for8.

If b=7, bases4 and5 are absent. Every possible early set is a subset
of {3,6,7,8}, whose mass is

    1/2+1/5+1/6+1/7 = 106/105 < 9/8.

If b=8, bases4,5,7 are absent. Every early set is a subset of
{3,6,8}, whose mass is59/70<1, so no early crossing occurs.

These alternatives exhaust the least eligible seed base.
Together with Sections2.1-2.2 and the case d_*>=9, they prove
sigma(C)<9/8. The augmentation retains m and gcd one, completing
the sharper reciprocal-core lemma for every m>=3.

## 3. A second bin with the same strict upper bound

Let R be any finite set of distinct integers at least four with
sigma(R)>=1. Add its bases in increasing order until the mass first
reaches one, obtaining B_1.

If its last base is at least nine, the previous mass is below one
and the last weight is at most1/8, so sigma(B_1)<9/8.
If its last base is at most eight, B_1 is contained in {4,...,8},
whose total mass is153/140<9/8.

Thus

    1 <= sigma(B_1) < 9/8.

No gcd condition is asserted or needed for this bin.

## 4. The improved high-mass theorem

First suppose sigma(D)>=13/4, and fix arbitrary k>=1 and finite F.
Use Section2 to construct C. Its complement R=D minus C has mass

    sigma(R) = sigma(D)-sigma(C) > 13/4-9/8 = 17/8.

Because C contains m, every element of R is at least m+1>=4.
Apply Section3 to R to obtain B_1, and let
B_2=D minus (C union B_1). Then

    sigma(B_2)
      = sigma(D)-sigma(C)-sigma(B_1)
      > 13/4-9/8-9/8
      = 1.

Consequently C,B_1,B_2 form three nonempty disjoint base groups,
each with mass at least one, with gcd(C)=1.
The criterion audited in Section1 applies to these groups for
the arbitrary k,F chosen. This proves labelled strong completeness
at the inclusive threshold13/4.

Now suppose only the exact admitted inequality

    sigma(D) >= 3+min{1/4,2/m}.

When3<=m<=7, the right side is13/4, so the preceding proof applies.
When m>=8, it is3+2/m, and the already accepted theorem [Mass]
applies directly to the same D,k,F. At m=8 the two values agree.
This proves the complete admitted claim, while preserving every
input covered by the previous high-mass result.

## 5. Construction, boundary, and dependency audit

The finite allocation uses deterministic symbolic rules: least-base
gcd descent and increasing first crossing. No empirical subset
enumeration supports any inequality above. The finite cases are
exhausted by explicit order and divisibility arguments.

For the resulting three supplies, the terminating finite interval
certificate search in [Mass, Section6] is unchanged. It dovetails
finite correction prefixes and finite prefixes of the two other
supplies, tests the required interval at the correction remainder's
proved gap bound, and terminates by the accepted thickness argument.
The returned seed and disjoint bounded-gap reserve give a terminating
representation search for every sufficiently large n. We do not run
this procedure or claim a useful numerical complexity bound.

The amplification's sufficient seed length is its reserve gap
constant, as proved in [Mass, Section1]. The present refinement
optimizes the mass cost of obtaining that seed's three supplies;
it does not assert that13/4 or9/8 is sharp. The proof still requires
three groups of mass at least one. It establishes no allocation,
integer seed, or completeness theorem for every input down to
the original threshold one.

All k,F and finite D remain universally quantified. Distinct bases,
collective gcd one, and separate occurrence availability are retained.
No additional assumption ID, pairwise-coprimality condition,
multiplicative-independence condition, or uniform N is introduced.

The mathematical dependencies are acceptance-000001 and
acceptance-000005, the latter already depending on the former.
The exact intermediate criterion in [Mass] is essential: its
old threshold theorem alone would not prove the new small-minimum
range. This use of its proof is explicit and is subject to result review.

Direction becomes true and mode becomes construction. The claim,
stage, and root contract remain unchanged. The new allocation
obligations are discharged in this proof, so the closing ledger is
empty. The entry's gain and preservation failure signals do not fire.
The extremal-optimum and forcing branches do not apply.
Only one seed-and-amplify application is used.

This is an analytical proof candidate, not a formal certificate,
independent acceptance, publication-priority claim, or root proof.
The target is obligation-000019. Complementary obligation-000020,
bridge obligation-000021, and the full original objective remain open.

