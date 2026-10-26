# A counterexample with legal signed units in every tail

Date: 2026-09-07.
Producer: node-000009, reserved move 1, seed-and-amplify.
Target: obligation-000013, the exact admitted abstract signed-tail inference.
Status: complete analytical proof candidate, awaiting independent result review.
No mathematical program, finite search, certificate or formal build was used.
This is not a counterexample to the original pure-power assertion.

## 1. The extension rule and the preservation estimates

For integers j>=2 put

    b_j = 3^j + floor(3^j/j).

For integers t>=4 put

    m_t = 2^t,              k_t = m_t-2t,
    B_t = {k_t,k_t+1,...,m_t}.

Define a level sequence by

    v_j = b_j,                                      j not equal to any m_t,
    v_(m_t) = 2 sum_(j=k_t)^(m_t-1) b_j - 1.        (1)

The required sequence a has exactly two separately labelled copies of
each v_j, ordered by j, starting at j=2. We first prove the extension
laws, before choosing the finite seed. The finite extension appends
all levels through the next endpoint m_t, with its replacement (1).
No earlier level or occurrence is changed.

The blocks are disjoint. Indeed k_4=8, m_4=16, k_5=22, and for t>=5,

    k_t-m_(t-1) = 2^(t-1)-2t > 0.

The inequality holds at t=5 and persists because doubling
2^(t-1)>2t gives 2^t>4t>=2(t+1).
Thus every interior level of B_t is unmodified. In particular, once
(1) has been appended it is also the exact identity

    2 sum_(j=k_t)^(m_t-1) v_j - v_(m_t) = 1.       (2)

We need the replacements to be upward, not merely positive. Define
the unmodified surplus before level m by

    E_m^b = 2 sum_(j=2)^(m-1) b_j - b_m.

For m>=3, geometric summation and x-1<=floor(x)<=x give

    E_m^b >= -9 + 2 sum_(j=2)^(m-1) 3^j/j
                    -3^m/m -2(m-2).

For 2<=j<m the exact identity

    1/j - 1/m - (m-j)/m^2 = (m-j)^2/(j*m^2) >= 0

shows that

    2 sum_(j=2)^(m-1) 3^j/j
      >= (3^m-9)/m + (2/m^2) sum_(j=2)^(m-1)(m-j)3^j
      >= (3^m-9)/m + 2*3^(m-1)/m^2.

Consequently,

    E_m^b >= (2/3)3^m/m^2 -2m-5-9/m.               (3)

For all integers m>=8,

    3^m >= 12m^3.

The initial inequality is 6561>=6144; the ratio of 3^m/m^3 at
successive integers is 3(m/(m+1))^3, at least 3(8/9)^3>1.
Hence (1/3)3^m/m^2>=4m>=2m+5+9/m for m>=8. Equation (3) implies

    E_m^b >= 3^m/(3m^2),                 m>=8.      (4)

Also 3^j<=b_j<2*3^j for j>=2, so

    2 sum_(j=2)^(k-1) b_j < 2*3^k,       k>=2.     (5)

At m=m_t, k=k_t the change delta_t=v_m-b_m obeys

    delta_t
      = E_m^b - 2 sum_(j=2)^(k-1)b_j -1
      >= 3^m/(3m^2) -2*3^k -1.

For t>=4,

    12*(4/9)^t <= 12*(4/9)^4 = 3072/6561 < 1,

and therefore 2*3^k <= 3^m/(6m^2). It follows that

    delta_t >= 3^m/(6m^2)-1 > 0.                   (6)

The last inequality follows from m>=16 and 3^m>=12m^3.
Thus every replacement is upward. At a modified endpoint, (1) and
b_j<2*3^j also give

    v_m < 4 sum_(j=2)^(m-1)3^j < 2*3^m.

At every level, modified or not,

    3^j <= b_j <= v_j < 2*3^j < 3^(j+1) <= v_(j+1). (7)

This proves strict increase between levels, positivity and exactly
two occurrences of each value. It also proves local finiteness.

Let

    E_m^v = 2 sum_(j=2)^(m-1)v_j-v_m.

At an unmodified level m>=8, (4) and upward replacements imply

    E_m^v >= E_m^b >= 3^m/(3m^2).                  (8)

At a modified level, the exact identity (2) gives instead

    E_(m_t)^v = 2 sum_(j=2)^(k_t-1)v_j+1
              >= 3^(k_t)-8
              >= (1/2)3^(k_t).                   (9)

Here k_t>=8. These are extension laws for all levels, including
modified endpoints. Earlier replacements cannot invalidate (8);
the old prefix is explicitly retained in (9).

Finally, every finite label subset has level coefficients
c_j in {0,1,2}. Its coefficient integer

    T(c) = sum_(j>=2)c_j 3^(j-2)

uniquely determines its finite coefficient vector by base-three
expansion. Equation (7) ensures

    sum_j c_j v_j >= 9 T(c).                      (10)

Appending a new block preserves (10). It does not assume injectivity
of numerical subset sums. Equations (2) and (6)-(10) are the required
preservation and amplification laws: they preserve legal unit
relations, order, multiplicity, a digit-weight support bound and the
stated prefix surplus estimates.

## 2. The first seed in this block template

The block parameter is t, the rule is m_t=2^t and k_t=m_t-2t,
and every block at or after the starting parameter is appended.
One complete block is the smallest nonempty seed carrying (2).

The starting parameter 4 is the smallest positive integer for which
this entire block schedule has starts at least 2 and disjoint closed
level blocks. At t=1 and t=2 the start is 0. Starting at t=3 would
include B_3=[2,8] and B_4=[8,16], which overlap at level 8 and fail
this template's disjoint-block invariant. Starting at t=4 works by
Section 1.

The finite seed consists of the levels 2 through 16, with the single
endpoint replacement for B_4=[8,16]. The inequalities proving that
replacement upward are (4)-(6), and the explicit numerical
start check is 12*(4/9)^4=3072/6561<1. Its legal signed excess is
exactly 1 by (2), and its pre-endpoint surplus is at least 3^8-8>0
by (9). All these are analytical equalities and inequalities, not
outputs of a finite enumeration.

Independent result review must check the extension argument and this
seed, not a sampled list of terms. No claim of global seed minimality
outside this specified block schedule is made.

## 3. Every-tail legal units and long positive intervals

For each t, let Q_t contain both labelled copies at each interior
level k_t through m_t-1, and let P_t contain one of the two copies at
level m_t. These are disjoint finite label sets. Equation (2) states

    sum(Q_t)-sum(P_t)=1.

Their support size is

    r_t = |Q_t|+|P_t| = 4t+1.                      (11)

The supports for different t are pairwise disjoint because the closed
level blocks are disjoint. Since k_t tends to infinity, every tail of
the ordered occurrence sequence contains all supports for sufficiently
large t. It therefore has the required legal signed unit identity.
This uses each occurrence at most once; no coefficient 3 is imposed
on a value with only two copies.

More is true. Choose any r such supports beyond an arbitrary cutoff
and put N equal to the sum of their P_t values. Independently choose
P_t or Q_t in each block. The resulting positive subset sums include

    N,N+1,...,N+r.                                 (12)

Thus every tail has arbitrarily long represented intervals. Combining
finitely many disjoint signed unit identities, reversing their signs
if necessary, also represents any prescribed integer as a finite
legal signed sum in that tail. Neither assertion gives a fixed
central loss L.

## 4. Every-tail gcd and modular conditions

A common divisor of all terms in any tail divides its legal signed
unit, and therefore equals one.

Fix a tail and a positive modulus h. For h=1 there is nothing to prove.
Let R be the residue classes occurring infinitely often in the tail.
After removing finitely many further terms, every remaining term has
its class in R. If R generated a proper subgroup of Z/hZ, there would
be a divisor g>1 of h dividing all representatives of that subgroup.
All sufficiently late terms would be divisible by g, contradicting
the gcd-one property for that later tail.

So R generates Z/hZ. Every class is a finite nonnegative combination
of classes in R: in any integer combination, negative coefficients
can be replaced modulo h by nonnegative coefficients. Every required
class in R has infinitely many available occurrences. Choose the
finite number of distinct occurrences required by the combination.
Their positive subset sum gives the desired residue. This proves
the modular condition separately for every tail and every h.

## 5. Divergence of squared norms despite growing supports

Write ||x|| for distance to the nearest integer. Fix any real alpha
that is not an integer. For each gadget, subadditivity of this norm
and its symmetry give

    ||alpha||
      <= sum_(i in P_t union Q_t) ||alpha a_i||.

Cauchy-Schwarz and (11) imply

    sum_(i in P_t union Q_t) ||alpha a_i||^2
      >= ||alpha||^2/(4t+1).                      (13)

The supports are disjoint and the sum of 1/(4t+1), t>=4, diverges.
For example, 4t+1<=5t. Summing (13) therefore proves

    sum_i ||alpha a_i||^2 = infinity

for every noninteger alpha, in particular for every irrational alpha.
Every tail contains all sufficiently late gadget supports, so the
same conclusion holds after every finite deletion. The reciprocal
support-length sum is essential here: convergence of the individual
norms alone would not justify a conclusion with growing supports.

## 6. Surplus growth at every occurrence prefix

Fix beta with 0<beta<1. At unmodified levels, (7)-(8) give

    E_m^v / v_m^beta
      >= (1/(3*2^beta)) 3^((1-beta)m)/m^2
      -> infinity.                               (14)

At modified levels, (7) and (9) give

    E_(m_t)^v / v_(m_t)^beta
      >= 2^(-beta-1) 3^((1-beta)2^t-2t)
      -> infinity.                               (15)

Both limits follow because a positive exponential dominates any
fixed polynomial, and 2^t/t tends to infinity. In (14), taking
logarithms of the positive main term gives
(1-beta)m log 3-2 log m plus a constant. In (15), the exponent tends
to infinity for each fixed beta. These statements give a threshold
allowed to depend on beta and together prove the limit over every
level, not just a selected subsequence.

Now let S_n be the sum of the first n occurrences of a. Before the
first copy of level m, S_n-a_(n+1)=E_m^v and a_(n+1)=v_m.
After the first copy and before the second, the next term is still
v_m and the surplus is E_m^v+v_m, which is no smaller. These are
all prefix types apart from the irrelevant empty prefix. Thus

    (S_n-a_(n+1))/a_(n+1)^beta -> infinity

along every occurrence prefix, for every fixed beta in (0,1).

## 7. Label growth and the failure of positive central coverage

Let A(X)=#{i:a_i<=X}, counting labelled occurrences. Equation (7)
places v_j between 3^j and 2*3^j, with exactly two occurrences per
level. All levels with 2*3^j<=X are present, and none with 3^j>X
are present. Hence

    A(X) = 2 log X/log 3 + O(1),

so the required liminf is

    (log 2)A(X)/log X -> log 4/log 3 > 1.           (16)

Let FS(a) include zero and all numerical finite positive subset sums.
If a positive subset sum is at most X, (10) places its nonzero
coefficient integer T(c) between 1 and floor(X/9). Each coefficient
vector has one definite numerical sum. Different label subsets may
give the same vector, and different vectors may give the same sum;
both phenomena only decrease the number of distinct numerical sums.
Therefore, for every real X>=0,

    #(FS(a) intersect [1,X]) <= floor(X/9).         (17)

In particular FS(a) has upper asymptotic density at most 1/9 and is
not cofinite. This is compatible with the arbitrarily long intervals
in (12), since those intervals need not occupy most integers.

If the admitted central-prefix conclusion held for some fixed L,m_0,
then each integer n>=L would belong to FS(a): choose a sufficiently
late prefix m>=m_0 with S_m>=n+L and S_m>=2L, possible because a is
an infinite positive-integer sequence, and apply its coverage of
[L,S_m-L]. This would make FS(a) cofinite, contrary to (17).

The sequence therefore satisfies every antecedent of the exact
admitted universal inference and violates its conclusion.

## 8. Optimisation, limits and exact scope

The seed start t=4 is minimal for the stated disjoint-block schedule,
as proved in Section 2. The use of base 3 with two copies is also the
smallest integer-base digit template with q-1 copies per level whose
label exponent (q-1)log 2/log q exceeds one: q=2 gives equality and
fails the strict hypothesis. These are template-level observations,
not an extremal claim over all sequences.

The fixed support deficit in (17) survives every extension and does
not tend to zero. The legal unit supports deliberately grow. A
bounded-support version is not proved, and (13) would no longer give
norm divergence for an arbitrary faster-growing support schedule
with convergent reciprocal-length sum. The all-prefix surplus bounds
are stated for beta<1 only. At gadget endpoints the baseline prefix
is much smaller than the next term; no positive linear-scale surplus
bound is asserted. Extra copies outside the coefficient range
{0,1,2} would invalidate the ternary encoding argument.

The complete proof is elementary and self-contained. Graham's
signed-tail method and the earlier perturbation example motivated
the construction; no external theorem or accepted predecessor result
is needed for the argument above. Independent result review and the
controller's immutable-evidence audit remain necessary for acceptance.

This proves only an infinite counterexample to obligation-000013.
It also shows, for this exhibited sequence, every-tail legal signed
coverage of all integers and arbitrarily long positive intervals.
It establishes no such profile for pure powers from a fixed finite
base set. Consequently it neither proves nor refutes C1 for those
pure powers, the signed pure-power profile, any implication bridge,
or the original all-D all-positive-cutoff objective.
