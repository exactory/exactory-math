# counterexample-search-run-1: can Theorem 6.1 of Leung-Schmidt (2016) reach any survivor?

## Question

Theorem 6.3 of the anti-field-descent paper is the special case of Theorem 6.1 in which u/m is a prime power. The general form allows several primes in u/m (the primes that fail condition (101) for the chosen descent prime p and unitary divisor d), at the price of the factor (u/m)^4 in the bound (103). Before implementing the general search (which needs discrete logarithms to construct the integer t), this run tests the route on every survivor of Theorem 6.3: since the maximum in (103) is at least 2 m^2 / u^2, a violation of (103) requires

    p - 1 >= ord_p(t) > 2 (u/m)^2                                                   (*)

for the chosen (p, d) with m as large as (101) allows, i.e. u/m = the product of the prime powers of the primes failing (101). The scan enumerates, for each survivor, every prime p of u and every unitary divisor d coprime to p with phi(d^2) < p phi(u^2) / (2u^2), computes the failing set B(p, d), and records:

- `min_bad`: the smallest |B(p, d)| over all admissible (p, d);
- `empty_bad`: the pairs (p, d) with B(p, d) empty (then Theorem 3.5 of the paper with m = u gives a root of unity X with X eta outside Z[zeta_{v/p}] for every root of unity eta, which is impossible, so no circulant Hadamard matrix of order 4u^2 exists);
- `feasible`: the (p, d) with the smallest u/m satisfying (*), if any;
- `feasible_multi`: the same restricted to |B(p, d)| >= 2, the cases Theorem 6.3 cannot take.

## Result

Over the 8,125 survivors (`survivors_thm63.txt`, from enumeration-run-1):

- min |B(p, d)| = 1 for every survivor; no (p, d) has an empty failing set;
- 274 survivors have some (p, d) satisfying (*), all with |B(p, d)| = 1 (Theorem 6.3's own case, where the inequality (109) failed because of the other terms of the maximum);
- 0 survivors have a (p, d) with |B(p, d)| >= 2 satisfying (*).

So the general form of Theorem 6.1 cannot rule out any survivor, whatever t is chosen: the route is closed on this residue. The 274 cases are recorded in `scan_thm61.jsonl` (field `feasible`); their eliminating parameters would have to come from a different bound, not from a different choice of m.

## Files

- `scan_thm61.py`: the scan (sympy for orders); `scan_thm61.jsonl`: one record per survivor.
- `check_scan.py`, `check.sh`: independent recomputation (own primality test, trial-division factorisation, order routine; standard library only) of `min_bad`, `empty_bad`, `feasible`, `feasible_multi` for every survivor, compared record by record. Exit 0 when every record agrees.
- `survivors_thm63.txt`: the input (copied from enumeration-run-1).

Range searched: all 8,125 survivors, all (p, d) admissible under (100)/(107). No random sampling; seed not applicable.

## Trusted base

Theorem 6.1 and Theorem 3.5 of Leung-Schmidt 2016 (refereed) and Python's integer arithmetic. The status of this run is evidence about the plan, not an elimination: it decides that a certificate family cannot apply, it produces no certificate.
