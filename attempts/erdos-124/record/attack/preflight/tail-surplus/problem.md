# Problem study: all-future prefix surplus

## Queries

See sources/queries.md for every query, source, date and access limitation. Fixed bounded search completed on 2026-09-07.

## Exact proposed statement

For every finite set D of distinct integers at least 3 with gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=1, every integer k>=1, and every finite set F of labelled occurrences (d,j) with d in D and j>=k, list the remaining occurrences by increasing value and then increasing base label as a_1,a_2,... and put S_m=sum_{i=1}^m a_i; then S_m-a_{m+1} tends to positive infinity as m tends to infinity.

The original objective remains the positive-cutoff claim in Erdos124.erdos124.ne_zero, not its solved zero-cutoff neighbour. The finite deletion strengthening concerns only this auxiliary surplus estimate. There is no formalisation of the new auxiliary statement in the inspected canonical file.

## Hits worth reading

- Evertse, Schlickewei and Schmidt, Linear Equations in Variables which Lie in a Multiplicative Group, Annals of Mathematics 155 (2002), DOI 10.2307/3062133, arXiv:math/0409604v1. The introduction's finite-rank nondegenerate-solution theorem was read in full, including hypotheses. Full HTML saved; the long proof was not audited. It supplies a possible qualitative finiteness engine, not a power-prefix or coverage theorem.
- Burr, Erdos, Graham and Li, DOI 10.4064/aa-77-2-133-138, printed pp.133-138. Full local extracted text read. Its final examples use a quantitative two-logarithm estimate for powers of 3 and 4. The arbitrary finite-base conjecture remains unresolved there.
- The current problem page, saved in sources/124.html, is marked OPEN. Its zero-cutoff result is distinct from the positive-cutoff target.
- Other query hits and unsuccessful source access are in sources/queries.md.

## Constraints on the plan

The exact geometric-sum identity from predecessor move 3 gives linear surplus growth when sigma>1 and only a constant lower bound when sigma=1. A useful new proof must control the latter case along every sufficiently late prefix, not merely on a subsequence.

The prospective translation turns bounded additive differences of two pure powers into fixed-coefficient equations in a finitely generated multiplicative group. It must check the group rank, nonzero coefficients, nondegeneracy, distinctness of exponent witnesses, and the zero-difference case. Gcd one is not pairwise coprimality.

Any result must survive finite deletion and prefixes ending within tied numerical values. No computed threshold is requested. Finiteness of the number of solutions alone does not give a largest exponent by an effective procedure.

The accepted reciprocal-core lemma does not prove the surplus claim and is not an inherited premise. The stopped abstract seed repairs remain invalid. Surplus growth supplies no represented seed by itself.

## Stop reason

The fixed query count was reached with a specific primary engine and explicit applicability checks. No exact claim was found, but novelty is not established exhaustively and no standalone publication claim is made.

