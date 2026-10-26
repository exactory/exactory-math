# Task 02: does positive linear surplus force completeness?

Packet version: 1. Prepared: 2026-09-07.
Type: analytical challenge with an unverified candidate. Return one English response.

Priority: secondary. This abstract route test is not one of the current primary
high-upside pure-power proof challenges; see packets 04-06.

## Exact proposition to test

Let a_1,a_2,... be a nondecreasing infinite sequence of positive integers,
locally finite (finitely many terms below every fixed bound), with bounded
numerical multiplicity. Define

    S_m = sum_{i=1}^m a_i,
    A(X) = #{i : a_i<=X},
    FS(a) = {sum_{i in I} a_i : I is a finite set of positive indices}.

The empty sum is allowed. Each labelled index can be used at most once.
Let ||x|| denote distance to the nearest integer; logarithms are natural.
Assume all of the following:

1. For every M>=1, gcd{a_i:i>=M}=1.
2. For every M>=1 and h>=1, every residue class modulo h contains a finite
   subset sum using only indices i>=M.
3. liminf_{X->infinity} (log 2)A(X)/log X > 1.
4. For every irrational real alpha, sum_{i>=1} ||alpha a_i||^2 = infinity.
5. liminf_{m->infinity} (S_m-a_{m+1})/a_{m+1} > 0.

Must FS(a) contain every sufficiently large positive integer?

The preferred target is a fully analytical counterexample satisfying every
hypothesis and omitting infinitely many integers. A proof of the proposition
is also acceptable, but it must resolve the candidate below. Failure of this
candidate is not a proof of the proposition.

## Why this question matters

The original project concerns streams of all powers d^j, j>=k>=1, from every
finite set D of distinct integers d>=3 with gcd(D)=1 and
sum_{d in D}1/(d-1)>=1, retaining distinct labels. Its claim is eventual
completeness for every D and k.

For actual streams with strict reciprocal mass, a geometric-sum identity gives
positive linear relative surplus. An earlier abstract counterexample already
shows that even surplus exceeding every fixed sublinear power of the next term,
together with hypotheses 1-4, is insufficient. It does not settle hypothesis 5.

This task tests a genuinely stronger substitute for pure-power structure.
An abstract counterexample would reject that substitute, not the original
pure-power conjecture. Conversely, a positive abstract theorem would still
need its hypotheses verified on the relevant power streams and would not
automatically cover reciprocal equality.

## Specific candidate to investigate

Define integers h_n by

    h_0=h_1=h_2=1,
    h_(n+3)=h_(n+2)+2h_n,       n>=0,

and take

    a_i=h_(i+3),               i>=1.

The proposed stream begins 5,7,13,23,37,63,..., with no duplicated labels
beyond the terms the recurrence actually produces. This candidate has not
been admitted or accepted as a proof in the current research. All claimed
properties must be independently derived or rejected.

Suggested checks, not established lemmas:

- Analyze x^3-x^2-2. A positive dominant root between the golden ratio and
  2 would suggest both counting growth above the required threshold and
  positive linear surplus. Verify the asymptotic coefficient and all indices.
- Check whether every characteristic root has modulus greater than one.
  If ||alpha h_n|| tends to zero, nearest-integer errors might eventually
  satisfy the same exact recurrence. Decide rigorously whether this forces
  those errors to vanish, and what tail gcd then implies about alpha.
- Check gcd one for every tail, not just for the first displayed terms.
  For modular coverage, justify why sufficiently late recurrent residue
  classes generate the entire finite cyclic group and why their multiplicities
  suffice for subset sums without reusing any index.
- Investigate whether a_(i+2)>a_(i+1)+a_i for all i>=1. The sequence
  h_(n+2)-h_(n+1)-h_n may help, but its initial signs and recurrence require
  proof.
- If that inequality holds, test whether the integers

      (a_(2r-1)+a_(2r-3)+...+a_1)-1,     r>=1,

  form an infinite family missing from FS(a). Prove both exclusion of larger
  summands and any forced-largest-summand induction. A finite list is not enough.

Relevant primary lead: S. A. Burr and P. Erdos, *Completeness properties of
perturbed sequences*, Theorem 3.5, pp.452-453,
[original paper](https://users.renyi.hu/~p_erdos/1981-02.pdf),
[DOI 10.1016/0022-314X(81)90036-6](https://doi.org/10.1016/0022-314X(81)90036-6).
Verify the theorem's exact inequalities and index conventions from the paper.
Its use may establish validity without establishing any publication novelty.
A self-contained proof of the missing-integers claim is preferable if short.

## Success, failure, and deliverable

Success requires a single explicit infinite sequence, proofs of every hypothesis,
and proof of infinitely many omissions. If the candidate fails, identify the
first failed hypothesis or inference. You may give an analytical repair, but
label any altered sequence and check its hypotheses afresh. An incomplete
construction or proof is a partial result, not a counterexample.

Return the exact result, full argument, references actually checked, actual
model/tools when known, unresolved steps, and the consequence for this abstract
route only. Use `inconclusive` when appropriate.

This is one analytical response, not an unbounded experiment. Do not launch
mathematical searches, other agents, or controller mutations. If computation
seems necessary, propose its finite domain and decision value instead. If local
files are available, write only to this packet's `results/RESULT.md` or a unique
result filename, and preserve all previous outputs.
