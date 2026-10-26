# Consolidation of the tail-surplus proof

Date: 2026-09-07. Closing move: node-000005, move 1.
This is the native consolidation required before local cash-out.
The immutable candidate proof remains moves/001-sunit-tail-surplus.md.

## Steps inspected for unexplained necessity

- The imported theorem is much more general than this application. Its
  role is only finiteness for one two-variable equation at a fixed nonzero
  difference. The proof states that instance explicitly and checks rank,
  coefficients and nondegeneracy. No quantitative part of ESS is needed.
- Gcd one might appear stronger than the gap argument needs. The proof
  isolates its exact use: choosing one base divisible by a prime and
  another not divisible by it. No pairwise hypothesis is introduced.
- Finite deletion and tie handling could be hidden in an asymptotic
  approximation. They are instead handled by an exact per-stream
  geometric identity and one fixed subtraction constant.
- Separate strict and equality mass arguments are unnecessary. The chosen
  pair-gap lower bound proves both at once; the strict-mass elementary
  estimate is retained only to explain where the previous ceiling lay.

## Standard-framework replacement

The finite-rank incidence theorem replaces any unproved claim that
different-base powers simply move apart. Such a claim needs a theorem:
irrationality of logarithm ratios alone does not provide the asserted
additive gap limit. The proof also excludes zero difference before
taking the finite union over possible integer differences.

The final proof is already computer-free. There is no numerical estimate
or unverified computation to replace.

## Short proof with the roles visible

Fix an admissible input and choose the prime-distinguished pair a,b.
For each nonzero integer c, apply ESS to
Gamma=<(a,1),(1,b)> and the equation X/c-Y/c=1. Its hypotheses give
finitely many positive exponent pairs with difference c. Since the chosen
pair has no zero differences, finitely many pairs have absolute difference
at most any fixed H.

For each late prefix let q be its next value and x_d its next unused
power in stream d. Local finiteness gives q tending to infinity, every
x_d>=q, and the chosen pair's difference therefore tends to infinity.
After the finite deletions lie below q, the exact identity is

    S_m-q=(sigma-1)q+sum_d (x_d-q)/(d-1)-C.

All residual terms are nonnegative, and one of the two chosen terms
bounds the absolute pair difference divided by max(a,b)-1 from below.
This proves the exact admitted surplus limit.

## Independent second route

An effective two-logarithm estimate is a possible different engine;
BEGL96 uses one for the specific pair 3,4. No general second proof has
been executed here, and no second-proof unit is claimed. Both routes
would still need the exact same prefix pull-back.

## Generality and limits

The argument identifies a potentially wider sufficient condition:
one pair with no common positive powers in place of collective gcd one.
The strict-mass elementary argument uses even less. These observations
are not separately studied, admitted or accepted claims and are not
reported as new theorems. The checkpoint remains exactly the original
auxiliary statement for admissible D,k,F.

The proof supplies no seed interval, effective threshold or coverage.
It is an internal corollary of a published finiteness theorem, not an
independently established publication-level contribution.

