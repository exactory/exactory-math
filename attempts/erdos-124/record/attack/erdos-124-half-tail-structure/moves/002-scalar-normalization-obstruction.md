# Move 2: the scalar-shift attempt on the noncommensurate residual

Reservation: move-node-000015-2, revision277.
Status: analytical author verification. No independent result acceptance.
The full half-mass signed-unit assertion and original Erdos124 objective remain open.

## Question and inherited restrictions

Continue plan step3 of attack-the-negative-side under the hypothetical missing
tail unit. Move1 implies that a counterexample contains no3 and no common-radix
half-mass subfamily. In particular all its bases are at least4. It also implies
H={0} and delta(K) tending to infinity, despite bounded gaps at each fixed K.

The candidate repair considered here is a common integer multiplier whose
per-base digit normalization preserves all legal signed supports. Such an
operation could try to move a finite support to higher exponents without
losing label capacity. The study supplement records the bounded source search.
The statements below delimit this particular operation. They are not a claim
that every possible mixed-base construction must have this form.

## 1. Signed digits and divisibility

For an integer d>=3, let X_d be the finite signed base-d sums
sum_{j>=0} e_j d^j, where e_j is in {-1,0,1} and only finitely many are nonzero.

The lowest digit of any element of X_d is determined by its residue modulo d,
because -1,0,1 have distinct residues. If that element is divisible by d,
its lowest digit is zero; dividing by d leaves an element of X_d. Iterating,
if an element of X_d is divisible by d^t, its first t digits are zero and its
quotient by d^t lies in X_d. Repeated lowest-digit recovery also proves uniqueness
of a finite signed representation, after padding with zeros.

These conclusions include negative values and zero. X_d is closed under
negation and multiplication by d^t for every nonnegative t.

## 2. Classification of universal scalar multipliers for one base

Claim: for d>=4 and an integer M,
M X_d is contained in X_d if and only if
M=0 or M=epsilon d^t for some epsilon in {-1,1} and integer t>=0.

The stated scalars preserve X_d directly. Conversely suppose M is nonzero
and M X_d is contained in X_d. Since1 belongs to X_d, M belongs to X_d.
Write its first nonzero signed digit as epsilon at position t, and put
M=epsilon d^t U. The signed digits of U have constant digit1.

The assumed closure implies U X_d is contained in X_d: for any x in X_d,
epsilon d^t Ux lies in X_d, so negation and the divisibility fact in section1
give Ux in X_d.

If U has no other nonzero digit, U=1 and the conclusion follows. Otherwise let
r>=1 be the first position with a nonzero digit sigma in {-1,1}. Then, modulo
d^(r+1),
U=1+sigma d^r.
The integer x=1+sigma d^r belongs to X_d. Since2r>=r+1,
Ux=1+2 sigma d^r modulo d^(r+1).

If Ux belonged to X_d, its lowest digit would be1. After subtracting1 and
dividing by d, the next r-1 digits would be zero, by repeated divisibility.
The digit at position r would therefore have to be congruent to2 sigma
modulo d. For d>=4, neither2 nor-2 is congruent to any of -1,0,1 modulo d.
There is no such signed digit. This contradicts Ux belonging to X_d and
proves the classification.

The restriction d>=4 is essential to this proof. At d=3, the residue2
is also the residue-1 and ordinary balanced ternary allows carrying.

## 3. No common expanding scalar for a gcd-one residual

Let E be any finite gcd-one set of bases at least4. Suppose an integer
M with absolute value greater than1 preserves X_d separately for every d in E.
Section2 gives absolute value M=d^(t_d) for each d, where t_d>=1.
A prime divisor of absolute value M would then divide every d in E,
contradicting gcd(E)=1.

Thus no such common expanding scalar exists. More elementary one-label shifts
are included: a shift j to j+t_d multiplies values by d^(t_d), so a common
expanding factor already has the same prime-divisor obstruction.

This is an obstruction to universal per-base scalar normalization. It does not
rule out a multiplier preserving a selected finite collection of supports,
a construction depending on the target, a signed union using several base
streams, or a nonlinear operation. In particular, the aligned common-radix
construction in move1 mixes the capacities of the bases in R. It does not
claim to preserve X_d separately for each d, so it is not contradicted here.

## 4. Why this supplies no new counterexample condition

The obstruction in section3 holds for every finite gcd-one E with minimum
at least4, including configurations already known to have legal tail units.
For example, any gcd-one family containing4,8,16 and enough disjoint positive
reserve lies in the accepted binary positive theorem and hence has tail units,
but still admits no common expanding scalar preserving each X_d separately.

Accordingly this candidate does not distinguish a missing-unit input from a
successful one. It gives no additional compression of the noncommensurate
residual identified in move1. It also gives no cutoff-independent bound on
delta(K), finite parameter range, genuine counterexample or contradiction of
the residual assumptions. Congruence coverage and fixed-cutoff syndeticity
remain insufficient for exactly the reason already recorded.

At the end of the second planned negative-side application, the proposed
universal scalar repair has failed and no new counterexample restriction has
been obtained. This is the recorded no-compression failure signal for the
selected negative-side route. The exact scalar classification is retained as
a limited method obstruction. It does not erase the positive common-radix
progress of move1, and it is not called a barrier for all proofs.

The full admitted claim stays unchanged. Direction false remains only the
counterexample assumption. The move does not close the attack and does not
supply a cash-out trigger by itself. It pays object and obligations: the proved
statement concerns a restricted operation class, while the arbitrary-base
unit construction remains owed. The native strategy must be marked failed
after this journal move, and any controller retreat must cite that actual
recorded predicate. No failure is attributed to the original conjecture.

## Verification and continuation

The proof is entirely elementary and was checked by hand: the residues
-1,0,1 are distinct for every d>=3; divisibility forces zero low digits;
the first double coefficient appears at position r;2r>=r+1 includes r=1;
and for d=4 both possible double coefficients have residue2, outside the
allowed set. Negation and removal of trailing powers of d account for every
nonzero integer multiplier. The converse scalars preserve finite support.

No mathematical process, finite enumeration or numerical inference was used.
No independent proof or publication novelty is claimed. The common-radix
positive successor is a separately admitted structural task, not a replacement
for this claim. The noncommensurate case should be revisited only with an
operation not covered by this restrictive scalar ansatz, or new evidence
controlling delta(K). A fixed-cutoff search would not by itself address it.
