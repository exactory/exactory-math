# A counterexample to the abstract strong-surplus inference

Status: complete analytical proof candidate, pending independent result review.
Producer: node-000006, reserved native move 1, seed-and-amplify.
Target: the exact admitted abstract inference, obligation-000010.
This is not a counterexample to the pure-power objective or to C1 for pure powers.

## 1. Definition and extension lemma

For integers t>=1 define

    u_t = floor(9^t/t),
    b_(2t) = 9^t + u_t,
    b_(2t+1) = 3 b_(2t) + 1.

The sequence a has exactly two separately labelled copies of each b_j,
in increasing j, starting with j=2. Write S_m=sum_(i=1)^m a_i.
The finite extension operation appends the next pair of levels, with two
copies of each. We first prove its preservation and amplification laws,
before selecting or checking the seed.

For every t>=1,

    9^t <= b_(2t) <= 2*9^t,
    b_(2t) < b_(2t+1) <= 6*9^t+1 < 9^(t+1) <= b_(2t+2).

Thus every extension preserves strict order between levels and exactly
two occurrences of each value. In particular a is nondecreasing,
positive, infinite and locally finite. For every j>=2 we also have

    3^j <= b_j <= 3*3^j.                              (1)

Let e_j=b_j-3^j, so e_j>=0. A finite subset of labels has coefficients
c_j in {0,1,2}. The integer

    T = sum_(j>=2) c_j 3^(j-2)

uniquely identifies this finite coefficient vector by base-three
expansion. Its numerical sum is

    sum_j c_j b_j = 9T + sum_j c_j e_j >= 9T.        (2)

Appending levels preserves this encoding and inequality. Different
label subsets can have the same vector, and different vectors might
have the same sum. Neither injectivity is assumed for numerical sums.

Define the local increments and complete-level surplus by

    Delta_j = 3b_j-b_(j+1),
    E_n = 2 sum_(j=2)^n b_j-b_(n+1),  n>=2.

Direct telescoping gives

    E_n = sum_(j=2)^n Delta_j-b_2.                  (3)

The extension increments are exactly

    Delta_(2t) = -1,
    Delta_(2t+1) = 9 floor(9^t/t)+3
                   -floor(9^(t+1)/(t+1)).          (4)

The inequalities x-1<=floor(x)<=x imply

    Delta_(2t+1) >= 9^(t+1)/(t(t+1))-6.             (5)

The positive sequence 9^(t+1)/(t(t+1)) increases, since the ratio of
its successive terms is 9t/(t+2)>1 for t>=1. Its first value is 81/2.
In particular every odd increment is positive. A complete-pair
extension satisfies

    E_(2t+3)-E_(2t+1)
      = Delta_(2t+2)+Delta_(2t+3)
      >= 9^(t+2)/((t+1)(t+2))-7 > 0.              (6)

Each intervening even endpoint is just one less than its preceding
odd endpoint. Equations (1)-(6) are the amplification and preservation
lemma. They also show why a slowly varying positive perturbation can
produce surplus growth while preserving a sparse numerical support.
The extension changes the number of labels by four; it preserves the
affine relation b_(2t+1)-3b_(2t)=1 and all the invariant formulas above.
The infinite arithmetic consequences of that relation are checked in
Section 4, rather than presumed from a finite seed.

## 2. Smallest seed in this template

The first complete pair has t=1:

    b_2=18, b_3=55, b_4=121.

After just level 2, E_2=36-55=-19. After the first complete pair,

    E_3=2(18+55)-121=25>0.

These are direct integer equalities, not a finite search or software
experiment. One pair is the smallest nonempty complete-pair seed in
the specified template, and it already has positive excess. Equations
(4) and (6) preserve a positive excess at all subsequent endpoints,
including the intervening even endpoints. No smaller untested seed
range is invoked. Independent result review must check these equalities
and the extension proof, not merely a list of sampled terms.

## 3. Surplus growth at every prefix

Use (3), retain the last positive odd increment, discard the other
positive odd increments, count the t even increments, and use b_2=18.
For t>=2,

    E_(2t) >= 9^t/((t-1)t)-t-24.                   (7)

For t>=1,

    E_(2t+1) >= 9^(t+1)/(t(t+1))-t-24.             (8)

Also b_(2t+1)<=7*9^t and b_(2t+2)<=2*9^(t+1).
For each fixed beta in (0,1), equations (7)-(8) imply

    E_n / b_(n+1)^beta -> +infinity.               (9)

For completeness, the lower bounds in (7)-(8) are positive for all
sufficiently large t, so an upper bound for the denominator can be used.
The positive main term is a constant multiple of
9^((1-beta)t)/t^2, which tends to infinity: its logarithm is
(1-beta)t log 9-2 log t plus a bounded term, and log t/t tends to zero.
The subtracted O(t)/9^(beta t) tends to zero. This proves (9) on both
parities, with a threshold allowed to depend on beta.

There are two prefix types. After the two copies of levels 2 through n,
the surplus S_m-a_(m+1) is E_n and the next value is b_(n+1).
After just the first copy at the following level, the surplus is
E_n+b_(n+1), with the same next value b_(n+1). Hence (9) gives

    (S_m-a_(m+1))/a_(m+1)^beta -> +infinity

as m tends to infinity along all prefixes, for every fixed beta in
(0,1). No favourable-endpoint restriction or uniformity in beta is used.

## 4. Every-tail arithmetic conditions and irrational norms

Every tail contains an entire adjacent pair b_(2t),b_(2t+1).
Their gcd is one, because b_(2t+1)-3b_(2t)=1. The gcd of all terms in
the tail is therefore one. Removing one of the two copies at an early
cut has no effect on the existence of later complete pairs.

Fix any tail and any positive modulus h. For h=1 the residue claim is
immediate. For general h let R be the residue classes occurring
infinitely often in the tail. There are finitely many classes, so after
discarding finitely many further terms all residues belong to R. If R
generated a proper subgroup of Z/hZ, there would be a divisor g>1 of h
dividing every representative in that subgroup. All sufficiently late
terms would then be divisible by g, contradicting the every-tail gcd
property just proved. Thus R generates Z/hZ. A subgroup generated by
R is also the monoid of nonnegative combinations of R, since the
negative of any class r can be replaced by (h-1)r. Every desired
residue is a finite nonnegative combination of classes in R. Choose
that many distinct later occurrences of each class, possible because
each occurs infinitely often. Their finite subset sum realizes the
desired residue. This works separately for every tail and modulus.

Now fix a real alpha. Suppose sum_i ||alpha a_i||^2 were finite.
Nonnegativity implies ||alpha b_(2t)||->0 and
||alpha b_(2t+1)||->0 as t tends to infinity. The elementary triangle
inequality for distance to the nearest integer gives

    ||alpha||
      = ||alpha(b_(2t+1)-3b_(2t))||
      <= ||alpha b_(2t+1)||+3||alpha b_(2t)|| -> 0.

Consequently alpha is an integer. In particular the sum diverges for
every irrational alpha, as required. In fact it diverges for every
noninteger alpha. This argument also works after any finite deletion.

## 5. Label abundance and numerical support deficit

Let A(X)=#{i:a_i<=X}, counting labels. Equation (1) gives

    A(X)=2 log X/log 3+O(1),  X->infinity.

Indeed levels with 3^(j+1)<=X are present, while levels with 3^j>X
are absent, and there are two labels per level. Therefore

    liminf_(X->infinity) (log 2)A(X)/log X
      = 2 log 2/log 3 = log 4/log 3 > 1.            (10)

Let FS(a) denote the set of numerical finite subset sums, including zero.
For any positive sum at most X, (2) assigns a nonzero coefficient
integer T<=floor(X/9). There are at most floor(X/9) such coefficient
vectors. Each vector has exactly one numerical sum. Multiple vectors
can only reduce the number of distinct numerical sums. Thus

    # (FS(a) intersect [1,X]) <= floor(X/9).        (11)

For positive integer X, at least X-floor(X/9) integers of [1,X] are
missing. In particular FS(a) is not cofinite.

If the admitted central-prefix conclusion held, fix its L and m_0.
For each integer n>=L choose m>=m_0 sufficiently large that S_m>=n+L
and S_m>=2L. This is possible because all terms are positive.
The asserted prefix interval would contain n, so n would belong to
FS(a). This would make FS(a) cofinite, contradicting (11).
The exact admitted inference is therefore false.

## 6. Seed optimisation, limitations and scope

Within the base-q digit template with exactly q-1 labelled copies at
each level and b_j comparable to q^j, the labelled counting exponent is
(q-1)log 2/log q. Base q=2 gives exactly one and fails the strict
hypothesis. The selected base q=3 is the smallest integer base in this
template whose exponent exceeds one; it uses two copies and the first
complete-pair seed. No global optimality across all possible sequences
is claimed. The support argument relies on the coefficient range
{0,...,q-1}; adding arbitrary extra copies would destroy its unique
base-digit encoding and is outside the verified construction.

All hypotheses of obligation-000010 have been checked: infinite
nondecreasing positive terms, local finiteness, numerical multiplicity
two, every-tail gcd one and all modular residues, strict labelled
counting growth, every irrational norm divergence, and the all-prefix
surplus limit for every fixed beta. The violation is quantified by (11).
No mathematical computation, external theorem, or accepted predecessor
result is needed for this proof. The literature and predecessor
checkpoint motivate the question only.

The candidate is not a union of labelled pure powers from one finite
base set. Its positive perturbations cannot be discarded when checking
the original hypotheses. Accordingly this proof rejects only the
proposed generic strong-surplus route. It neither refutes nor proves
C1, its pure-power quantitative profile, its bridges, or the root.

