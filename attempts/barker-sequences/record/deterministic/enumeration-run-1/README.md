# enumeration-run-1: Leung-Schmidt (2016) Theorem 6.3 over the Borwein-Mossinghoff list

## What the run decided

For each of the 237,807 values u in `BarkerCandidates100.txt` (the list of Borwein-Mossinghoff 2014, Wayback capture 2021-07-18 of http://wayback.cecm.sfu.ca/~mjm/WieferichBarker/Data/BarkerCandidates100.txt.gz), the search `search_thm63.py` looks for a triple (d, p, q) that satisfies the hypotheses of Theorem 6.3 of Leung-Schmidt, "The anti-field-descent method", J. Combin. Theory Ser. A 139 (2016) 87-131, and violates its inequality (109). A violation proves that no circulant Hadamard matrix of order 4u^2 exists, hence no Barker sequence of length 4u^2.

Result: 229,682 values eliminated, each with a certificate in `certificates_thm63.jsonl`; 8,125 values not eliminated, listed in `survivors_thm63.txt` (input format, sorted). The published counts (Leung-Schmidt 2016, Section 6: "Theorem 6.3 rules out 229,682 of these 237,807 cases", smallest survivor u = 30109 * 1128713 * 2167849 * 268813277) are reproduced exactly. The survivor list itself is not published in the paper ("available from the authors upon request"); this run reconstructs it.

Parameter range: the whole list, Omega(u) from 4 to 17, 148 distinct primes, all below 4.7 * 10^11. First value at which the answer changes: the smallest surviving value is 19804304830012264298738041 (Omega = 4); every value below it is eliminated.

## Files

- `search_thm63.py`: the search (encoder). For each prime p of u and each unitary divisor d of u coprime to p with phi(d^2) < p phi(u^2) / (2u^2), it computes the set of primes r != p failing (108); when at most one prime fails, it tries every admissible q and evaluates (109) with exact rationals. It stops at the first violation. Orders come from sympy 1.14 (`n_order`).
- `certificates_thm63.jsonl`: one JSON object per eliminated u: `u`, `factorisation`, `d`, `p`, `a`, `q`, `b`, `ord_p_q`, the maximum in (109) as `max_num/max_den`, and the right-hand side as `rhs_num/rhs_den`.
- `survivors_thm63.txt`: the 8,125 values not eliminated.
- `check_thm63.py` and `check.sh`: the independent checker. It shares no code with the search: own deterministic Miller-Rabin test, own trial-division factorisation of s - 1, own order routine, and it recomputes every quantity of Theorem 6.3 from (u, d, p, q) alone, with exact rationals. It also checks that the eliminated values are distinct members of the list, that eliminated plus survivors is exactly the list, and that the totals and the smallest survivor agree with the published ones. Standard library only.
- `BarkerCandidates100.txt`: the input.
- `test_top19*`: a smoke test on the 19 values with n <= 10^50 of Table 1 of Leung-Schmidt 2016; all 19 are eliminated, in agreement with the paper (the certificates found first may differ from the paper's choices of d and q).
- `run.log`: the run's log (8 m 33 s of user time on one core, Python 3.11.11, macOS).

## Trusted base

The theorem (Leung-Schmidt 2016, Theorem 6.3, refereed) and Python's big-integer arithmetic. The checker is the independent implementation; sympy is used only by the search.

## Reproduction

```
python3.11 search_thm63.py            # writes certificates_thm63.jsonl and survivors_thm63.txt
./check.sh                            # exit 0 when every certificate is valid and the counts agree
```
