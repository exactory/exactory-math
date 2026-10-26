# C1 move 2: an obstruction to abstract seed production

Status: analytical argument for independent review, not controller-accepted
evidence. The admitted C1 claim and the full original objective remain open.
No mathematical computation process was run.

## Tested statement and study

The neighbouring principle G is stated in `problem.json.shape.neighbours` and
studied in `study/arithmetic-seed-barrier.md`. It asks whether divergent prefix
surplus, gcd one in every tail, irrational nonconcentration, and a raw label
exponent greater than one force eventual central-prefix coverage for locally
finite positive-integer sequences of bounded multiplicity. Pure-power structure
is omitted. This is a diagnostic of proposed seed-production inputs, not a
replacement target for C1 or a claimed implication from C1 to G.

## Construction

Fix an even integer q>=4 and k>=1. For each j>=k take exactly q-1 separately
labelled copies of b_j=q^j+1. Order them by value, and denote the resulting
sequence by a_1,a_2,..., its prefix totals by S_r, and its finite subset-sum set
by FS. This sequence is locally finite, tends to infinity, and has uniformly
bounded multiplicity q-1. The case q=4, k=1 already refutes G.

### 1. Divergent surplus at every sufficiently late prefix

At the end of the block with exponent m>=k, let t=m-k+1. Then

    S_( (q-1)t ) = (q-1) sum_(j=k)^m (q^j+1)
                = q^(m+1)-q^k+(q-1)t.

The next occurrence is q^(m+1)+1. Thus the surplus there equals

    (q-1)t-q^k-1,

which tends to infinity. After s additional copies from the next block, where
0<=s<q-1, the next value stays q^(m+1)+1 and the surplus increases by
s(q^(m+1)+1). Completing that block gives the next endpoint formula.
Consequently S_r-a_(r+1) tends to infinity along all prefixes, including those
ending within a block. Any finite deletion only subtracts a fixed total from
the eventual corresponding prefix totals, so the same divergence survives it.

### 2. Tail gcd and modular coverage

For every j,

    gcd(q^j+1,q^(j+1)+1)
      = gcd(q^j+1,q-1)
      = gcd(2,q-1)
      = 1.

Every tail contains two such adjacent exponent values, so every tail has gcd
one. In fact every tail's finite subset sums meet every class modulo every
positive integer h. To check the general implication used here, let R be the
set of residues occurring infinitely often in a given tail modulo h. Remove
the finitely many occurrences of residues outside R. If gcd(h,R)>1, this gcd
would divide all remaining terms, contrary to the tail gcd condition. Thus R
generates Z/hZ. Every element of this finite group is a finite nonnegative
combination of R: inverses can be replaced by repeated addition. Infinitely
many occurrences of each r in R realize that combination with distinct labels.
This proves the assertion for every tail, without any uniform bound on the
number or size of the terms chosen.

### 3. Irrational nonconcentration

For every irrational real alpha,

    sum_(j>=k) ||b_j alpha||^2 = infinity,

where ||x|| is the distance from x to the nearest integer. Otherwise the terms
would tend to zero. The identity q b_j-b_(j+1)=q-1 and the triangle inequality
on R/Z would give

    ||(q-1)alpha|| <= q ||b_j alpha|| + ||b_(j+1)alpha|| -> 0.

This contradicts the irrationality of alpha. Repeating each term q-1 times
and deleting finitely many occurrences preserve this divergence.

### 4. The raw label exponent is greater than one

Let A(X) count labelled occurrences at most X. Then

    A(X) = (q-1) log(X)/log(q) + O(1),

and hence

    lim_(X->infinity) log(2) A(X)/log(X) = (q-1)log(2)/log(q) > 1.

The last inequality follows from 2^(q-1)>q for integer q>=4. In the smallest
example q=4 its value is exactly 3/2. This count concerns choices of labels,
not distinct numerical subset sums.

### 5. Despite these conditions, the subset-sum density is small

Selecting c_j copies at exponent j, with 0<=c_j<=q-1, gives

    sum_(j>=k) c_j(q^j+1) = q^k t+s_q(t),
    t = sum_(j>=k) c_j q^(j-k),

where s_q(t) is the ordinary base-q digit sum. Conversely every nonnegative
integer t has a unique finite base-q digit expansion with these coefficients,
and every coefficient choice can be realized using the available labels.
Therefore, as a set of numerical values,

    FS = {q^k t+s_q(t): t>=0}.

The displayed map need not be injective, which is immaterial for the bound.
A positive value at most X comes from an integer 1<=t<=X/q^k. Consequently

    |FS intersect [1,X]| <= floor(X/q^k),
    upper_density(FS) <= q^(-k) < 1.

There are infinitely many missing positive integers. Eventual central-prefix
coverage would imply cofiniteness: for a fixed L and any n>=L choose a long
prefix with S_r>=n+L. The density bound therefore rules it out. In particular,
the divergent surplus cannot be combined with a suitable central seed at any
starting prefix. Such a seed would propagate by the previously proved append
lemma and would contradict this density bound.

## Hand check and scope of the obstruction

For q=4,k=1 the first blocks are three copies of 5, then three of 17, then
three of 65. The first two block totals are 15 and 66. The corresponding next
values are 17 and 65, so the endpoint surpluses are -2 and 1, as the formula
predicts. The first block has subset sums {0,5,10,15}. These checks illustrate
the construction; the infinite conclusion follows from the proof above, not
from a finite search.

The example refutes G. It does not refute C1 or C2 for admissible pure powers.
Its terms are translated powers, and its repeated labels are not distinct
base-exponent pairs from an admissible D. A proof for the original problem
must use additional structure beyond these four abstract conditions. This
does not show that a particular extra condition, such as distinct numerical
values or a stronger support count, is sufficient.

The entry's failure signal fires in the stated sense that this neighbouring
counterexample uses features outside the original pure-power hypotheses.
The useful output is the exact boundary of the discarded abstract principle.
There is no counterexample to the admitted C1 target, no novelty claim, no
publication, and no controller proof credit.
