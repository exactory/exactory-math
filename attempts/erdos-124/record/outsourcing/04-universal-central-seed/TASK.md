# Challenge 04: prove the universal central-seed lemma

Packet version: 1. Prepared: 2026-09-07.
Priority: primary. Type: high-risk analytical proof attempt.
Return one self-contained English response. Computation is not the task.

## Objective and potential contribution

The original objective is the following. For every finite set D of distinct
integers d>=3 with gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=1, and every
integer k>=1, all sufficiently large integers are sums of finitely many powers
d^j, d in D, j>=k, with each pair (d,j) used at most once. Different pairs
with the same numerical value are separate available occurrences.

This challenge targets the missing represented-seed lemma in a route to that
full objective. A complete proof, together with the accepted surplus theorem
and verified implications below, could finish the mathematical argument for
the entire original scope. It would still require independent verification
and controller acceptance. Merely restating the lemma achieves nothing.

## Exact claim to prove

Fix any admissible D and k as above, and any finite set F of labelled
occurrences (d,j) with d in D and j>=k. Remove F and sort the remaining
occurrences a_1,a_2,... by value and then base label. Put

    S_m=sum_{i=1}^m a_i,
    T_m={sum_{i in I}a_i : I subset {1,...,m}}.

Prove:

    There exists an integer L>=0 such that for every integer M>=1
    there exists m>=M with S_m>=2L and
    [L,S_m-L] intersect Z subset T_m.

L may depend on D,k,F, but not on M or the selected m. No effective bound on
L or m is required. Every admissible D must be covered, including sigma(D)=1.

The input is a union of exact geometric power streams, not an arbitrary
sequence with similar growth. Exponent zero, new bases, signed coefficients,
unbounded use of a label, and perturbations of the powers are not allowed.

## Accepted input that may be used

The project has an independently reviewed analytical proof that, for exactly
these D,k,F and streams,

    S_m-a_{m+1} -> +infinity.

This is checkpoint-000009, acceptance-000002, source node-000005 move 1.
The proof uses the finite-rank equation theorem of Evertse, Schlickewei and
Schmidt, [arXiv:math/0409604](https://arxiv.org/abs/math/0409604),
[DOI 10.2307/3062133](https://doi.org/10.2307/3062133).
Treat the exact surplus statement as a supplied lemma, not a theorem that
already gives the seed. It has no effective threshold in the equality case.

An elementary identity is also available. Once q_m=a_{m+1} exceeds all deleted
values, let x_d(m) be the first unused remaining power of base d and put

    C=sum_{d in D}d^k/(d-1)+sum_{(d,j) in F}d^j.

Then

    S_m-q_m=(sigma(D)-1)q_m
             +sum_{d in D}(x_d(m)-q_m)/(d-1)-C.

It follows by summing each labelled geometric stream separately. This identity
does not create represented intervals.

## Deduction to the root, to be checked in your response

If the requested lemma holds, first fix its L. The supplied surplus theorem
gives a threshold M beyond which S_r-a_{r+1}>=2L-1 for every r>=M. Choose
the lemma's represented seed at some m>=M. At each following step, the two
integer intervals

    [L,S_r-L],
    [L+a_{r+1},S_r+a_{r+1}-L]

overlap or are adjacent. Each is represented by either omitting or using the
new label, so their union is the next central interval. Induction and
S_r->infinity give all integers at least L. Taking F empty yields the root.
These bridge arguments must be checked; they are not separately accepted
controller evidence at the packet's snapshot.

## Where a conceptual advance is needed

Develop one serious mechanism for exact integer coverage of the central
interval. A possible direction is a loss invariant that remains bounded
under the different maps x->dx and exploits gcd(D)=1 without losing access
to the required individual labels. Another is an exact additive covering
argument whose expansion cannot be trapped by recurring holes. These are
research suggestions, not supplied results or restrictions on your method.

Known failed shortcuts:

- A small represented interval need not survive the next power. Repeatedly
  increasing its endpoint loss does not establish one fixed L.
- Choosing L after observing a late prefix, then appealing to an eventual
  threshold depending on that new L, does not ensure compatible seed and scale.
- Many labelled representations need not yield many distinct numerical sums.
- Real Cantor-set interval coverage or positive measure does not imply exact
  lattice coverage without a separate argument.
- Full modular subset-sum coverage, counting growth, irrational squared-norm
  divergence, and surplus exceeding every fixed sublinear power of the next
  term are jointly insufficient for arbitrary sequences. An accepted abstract
  counterexample already rules out that proposed general inference.

Preserve exact power structure unless you prove that your replacement retains
the property needed for integer coverage. Do not simply assume an abstract
completeness theorem that reproduces the missing input.

Background: BEGL96, *Complete sequences of sets of integer powers*,
[DOI 10.4064/aa-77-2-133-138](https://doi.org/10.4064/aa-77-2-133-138).
Any additional theorem must be identified precisely and its hypotheses checked.

## Required result and failure signal

Attempt the proof, rather than returning a menu of research directions. State
your central new lemma and develop its proof as far as logically justified.

A successful response supplies the exact all-D,k,F seed theorem and the full
deduction above. A conditional theorem must name every remaining assumption.
A partial result must state exactly which root cases it covers. If the method
fails, identify its first unresolved inference and a concrete reason or
counterexample to that inference where possible. Do not label the original
objective false because an auxiliary strengthening fails.

Return the exact claim, full argument, inspected references, actual model/tools
when known, and unresolved obligations. Keep publication novelty separate from
validity. Do not assign a proof percentage to an unverified answer.

This packet is a proposal for external analytical work, not an admitted attack.
Do not launch mathematical programs, other agents, or controller mutations.
If local files are available, write only `results/RESULT.md` in this packet,
or a unique result filename. Preserve existing results and accepted artifacts.
