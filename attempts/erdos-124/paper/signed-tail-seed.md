# Legal signed coverage without central positive coverage

## Statement

There exists a nondecreasing locally finite infinite sequence of positive integers with numerical multiplicity two such that every tail has gcd one, finite positive subset sums meet every residue modulo every positive integer and contain arbitrarily long intervals, every integer is a legal finite signed sum from every tail using each label at most once, the labelled counting ratio (log 2)#{i:a_i<=X}/log X tends to log(4)/log(3)>1, the squared norms sum to infinity for every noninteger real multiplier, and (S_m-a_{m+1})/a_{m+1}^beta tends to infinity for every fixed beta in (0,1) along all prefixes, but for every X>=0 the number of positive numerical finite subset sums at most X is at most floor(X/9), so no fixed-loss central-prefix coverage is possible.

## Construction and argument

The full self-contained proof and seed checks are in
moves/001-sparse-signed-blocks.md, Sections 1-8. All mathematical
claims below refer to those sections.

For j>=2 set b_j=3^j+floor(3^j/j). For t>=4 set m_t=2^t and
k_t=m_t-2t. Use two labelled copies of each level v_j, with v_j=b_j
except at endpoints m_t, where

    v_(m_t)=2 sum_(j=k_t)^(m_t-1)b_j-1.

Section 1 proves disjointness of the closed blocks [k_t,m_t],
the upward endpoint replacements and the bounds

    3^j<=b_j<=v_j<2*3^j<3^(j+1).

The floor and reciprocal inequalities in that section give

    2 sum_(j=2)^(m-1)b_j-b_m >= 3^m/(3m^2), m>=8.

Section 2 checks the first admissible block seed t=4 and restricts
the minimality claim to this block schedule.

Each block contains a legal signed identity of value one using
exactly 4t+1 labels. Independent choices between its negative and
positive parts produce consecutive positive sums. Disjoint blocks
beyond every cutoff give arbitrary long positive intervals and
legal signed representations of every integer in every tail.
Section 3 proves both assertions without unrestricted coefficients.
Section 4 proves every-tail gcd one and full modular coverage,
choosing distinct occurrences for each finite combination.

For any noninteger real alpha, Section 5 gives

    sum_(i in gadget t) ||alpha a_i||^2
      >= ||alpha||^2/(4t+1).

Disjoint supports and divergence of the reciprocal-length sum prove
the norm assertion. Increasing support alone would not suffice.

For unmodified levels m>=8, the pre-level surplus is at least
3^m/(3m^2). At modified levels m_t it is at least
(1/2)3^(k_t). Dividing by v_m^beta proves divergence for every
fixed beta in (0,1). Between the two copies of a level the surplus
increases by that level's value, so Section 6 covers every prefix.

Section 7 counts two labels per geometric level to obtain the
labelled counting ratio log(4)/log(3). To count numerical subset
sums instead, write their coefficients as c_j in {0,1,2}. The integer

    T=sum_j c_j 3^(j-2)

uniquely determines the finite coefficient vector, and its sum is
at least 9T. Thus at most floor(X/9) nonzero coefficient vectors
can give sums at most X. Collisions cannot increase the number of
distinct numerical sums. The support bound follows.

A fixed central loss would make the positive subset sums cofinite:
for a given n>=L choose a sufficiently late prefix whose total is
at least n+L, then apply its central coverage. This contradicts the
support bound, as Section 7 proves.

## Scope and status

The result is a counterexample to the exact auxiliary inference,
not to the original Erdős 124 pure-power assertion. The sequence
is not claimed to come from a finite set of pure-power bases.
All original positive-cutoff quantifiers, the actual pure-power
signed profile and the implication bridges remain open.

The proof is elementary and uses no mathematical program or external
theorem. Independent analytical result review and draft evaluation
are required. This is not a claim of certificate or Lean checking.
The bounded exact-result literature check and its limitations are in
study/unit-novelty.md. Standalone publication novelty and broad
significance are not established.
