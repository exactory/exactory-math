# Task 03: the fixed bases 3, 4, and 5 at every positive cutoff

Packet version: 1. Prepared: 2026-09-07.
Type: analytical special-case attack. Return one self-contained English response.

Priority: secondary. Current primary packets 04-06 target all admissible bases
or a complete reciprocal-mass regime, rather than this single base set.

## Exact target

Prove or disprove the following statement:

For every integer k>=1 there exists an integer N(k) such that, for every
integer n>=N(k), there are finite subsets S_3,S_4,S_5 of {k,k+1,...} with

    n = sum_{j in S_3} 3^j + sum_{j in S_4} 4^j + sum_{j in S_5} 5^j.

Each pair (d,j) may be used at most once. Exponent zero, unrestricted
multiplicities, negative coefficients, and powers of other bases are forbidden.
The bases must remain exactly {3,4,5} as k grows.

This is a special case of the original objective for all finite distinct
D subset {3,4,...} with gcd(D)=1 and sum_{d in D}1/(d-1)>=1. Proving this
task would not prove the full all-D statement. The current work has no
accepted proof of this all-cutoff special case; do not assume it is novel
without checking the exact statement in the literature.

## Prior information and scope checks

The reciprocal mass is 1/2+1/3+1/4=13/12>1.
BEGL96 reports completeness at k=1 for {3,4,5}, with largest missing integer
78, on p.137. This does not give all k. Its theorem providing a finite set
of bases that may depend on k also does not keep {3,4,5} fixed.

Reference: S. A. Burr, P. Erdos, R. L. Graham, and W. Wen-Ching Li,
*Complete sequences of sets of integer powers*, Acta Arithmetica 77 (1996),
133-138, [DOI 10.4064/aa-77-2-133-138](https://doi.org/10.4064/aa-77-2-133-138).
Check source quantifiers before treating a literature hit as a solution.
If an exact known theorem settles the task, provide the theorem and complete
application rather than presenting it as a new discovery.

## A conditional seed route to examine

For a fixed k, sort all labelled powers of 3,4,5 with exponents at least k
as a_1,a_2,...; put S_m=sum_{i<=m}a_i and q_m=a_{m+1}. Let x_d(m) be
the first power of base d not used by the first m terms. Then the proposed
elementary identity and bound are

    C(k)=3^k/2+4^k/3+5^k/4,
    S_m=sum_{d in {3,4,5}} x_d(m)/(d-1)-C(k),
    S_m-q_m >= q_m/12-C(k).

Recheck these formulae. A sufficient seed would be integers L>=0 and m>=1
satisfying all of

    S_m>=2L,
    [L,S_m-L] intersect Z subset FS(a_1,...,a_m),
    q_m >= 12(C(k)+2L-1).

Indeed, monotonicity of q_r would give S_r-a_{r+1}>=2L-1 for every r>=m.
The represented intervals [L,S_r-L] and
[L+a_{r+1},S_r+a_{r+1}-L] would overlap or be adjacent. Their union gives
the next central interval, and positivity makes their upper endpoints
unbounded. This is a conditional route to completeness, not a proof of
seed existence. It has not separately received controller acceptance.

The unresolved task on this route is to construct compatible L=L(k) and
m=m(k) for every k. Choosing L from a large finite prefix and only then
appealing to a threshold depending on L is circular unless all three
conditions are verified together. Alternative analytical approaches are welcome.

## Non-solutions and useful partial outcomes

- Checking k=1, or any finite list of cutoffs, does not prove this task.
- Proving that an infinite stream has gcd one, meets every residue class,
  has many labelled subset sums, or has positive surplus does not by itself
  prove that its numerical subset sums are cofinite.
- A real interval in a normalized Cantor-set sum does not imply exact
  integer representation without an additional lattice argument.
- Completeness before deleting finitely many terms does not automatically
  imply completeness afterward for arbitrary sequences.
- A seed construction for a precisely described infinite set of k, an exact
  recurrence transferring a seed from k to k+1, or a rigorously proved new
  intermediate lemma is useful. State its narrower scope and remaining gap.
- A fixed k together with a proof of infinitely many nonrepresentable n
  would refute the target. One missing n cannot refute eventual completeness.

## Required response and limits

Return a verdict, exact claim established, self-contained argument, inspected
references, actual model/tools when known, remaining obligations, and one
specific next hypothesis if unresolved. Keep novelty separate from validity.
An honest partial or inconclusive result is acceptable.

Use a single analytical response. Do not run subset-sum enumeration, extend
a tested prefix, start other agents, or mutate controller records. If a finite
diagnostic is genuinely needed, describe its exact domain, necessary decision,
stopping rule, and verification plan for later review. Return the result for
storage in this packet's `results/RESULT.md` or a unique filename there;
preserve all previous files.
