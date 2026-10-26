# No Barker sequence of length 4u² for u in the Borwein-Mossinghoff list

| | |
|---|---|
| Claim | For every integer $u$ in the list $L$ of 237,807 integers $u < 5\cdot 10^{49}$ published by Borwein and Mossinghoff (2014), and for every sequence $a_1,\dots,a_n$ of entries $\pm 1$ with $n = 4u^2$, some aperiodic autocorrelation $c_k = \sum_{i=1}^{n-k} a_i a_{i+k}$ with $1 \le k < n$ has $\lvert c_k\rvert \ge 2$. In words: no Barker sequence of length $4u^2$ exists for any $u$ in $L$. |
| Outcome | Open. The record reduces the claim, by exact computation with an independent checker, to an explicit residue $R$ of 8,125 values of $L$. Three further published tests and a feasibility scan for a fourth eliminate none of them. The attack has one journalled move and four open tasks. This is a small record. |
| Formal verification | None. The record read the Lean statement of the Barker conjecture in google-deepmind/formal-conjectures but has no Lean development of its own. |
| Related problem | None in this repository. |
| Made by | exactory math-solver harness, objective `barker-sequences`, attack `barker-lengths-below-10-100-residue`. The studies are dated 2026-09-02; the tool activity log has timestamps on 2026-09-03 (UTC). |

A Barker sequence is a sequence of entries $\pm 1$ whose aperiodic autocorrelations $c_k$, $1 \le k < n$, all satisfy $\lvert c_k\rvert \le 1$. Barker sequences are known for the lengths 2, 3, 4, 5, 7, 11 and 13, and the Barker conjecture says that no Barker sequence has length greater than 13. The record's problem study (`record/study/problem.md`) summarises what is known. A Barker sequence of length $n > 13$ gives a circulant Hadamard matrix of order $n$ (Eliahou-Kervaire 1992), so $n = 4u^2$ with $u$ odd (Turyn 1965), and every prime $p \mid u$ satisfies $p \equiv 1 \pmod 4$ (Eliahou-Kervaire-Saffari 1990). Leung and Schmidt (2016, Theorem 6.4) proved that no Barker sequence has length $n$ with $13 < n \le 4\cdot 10^{33}$.

The list $L$ consists of the values $u < 5\cdot 10^{49}$ that pass Corollary 3, Theorem 5 and Theorem 7 of Borwein-Mossinghoff (arXiv:1306.0045) and for which some of their tests were not run. Leung and Schmidt (2016) report that their Theorem 6.3 eliminates 229,682 of the 237,807 values and that the smallest survivor is $u = 30109\cdot 1128713\cdot 2167849\cdot 268813277$. Their survivor list is "available from the authors upon request" and is not published. The record states that $L$ is complete only up to $n = 4\cdot 10^{33}$, so clearing $L$ would give no new lower bound on $n$.

## Results

Throughout, $\Omega(u)$ is the number of prime factors of $u$ counted with multiplicity.

1. The residue $R$, by exact computation with an independent checker. The record re-implemented Theorem 6.3 of Leung and Schmidt, "The anti-field-descent method", J. Combin. Theory Ser. A 139 (2016) 87-131, with the parameter search of their Remark 6.2, and ran it on all 237,807 values of $L$. It eliminated 229,682 values, each with a certificate $(d, p, q)$ that satisfies the hypotheses of Theorem 6.3 and violates its inequality (109). The 8,125 survivors form $R$. An independent checker, which shares no code with the search, verified all 229,682 certificates with exact rational arithmetic and checked that the eliminated values and the survivors together are exactly $L$ (harness status `pass`). The counts and the smallest survivor agree with the published ones. The journal states the consequence: the claim holds for all of $L$ if and only if it holds for every $u$ in $R$. It also records that every element of $R$ contains the four primes 30109, 1128713, 2167849 and 268813277, that 35 distinct primes occur in $R$, and that $\Omega(u)$ ranges from 4 to 16 on $R$. Trusted base: the refereed Theorem 6.3 and Python's integer arithmetic. Where: `record/deterministic/enumeration-run-1/` (`README.md`, `survivors_thm63.txt`, `result.json`) and `record/journal.jsonl`.

2. Turyn's test and Theorems 3.5 and 3.1 of Leung-Schmidt (2012) on $R$, by exact computation. The log of `record/deterministic/enumeration-run-3/` ends with `values: 8125  eliminated: {'turyn': 0, 'thm35': 0, 'thm31': 0}  survivors: 8125`. So, in the formulation implemented in `search_tests.py`, none of the three tests eliminates a value of $R$. This run has no README, no journal entry and no recorded checker result, and the corresponding task in `record/tasks.json` is still open.

3. A feasibility scan for Theorem 6.1 of Leung-Schmidt (2016), the general form of Theorem 6.3, by exact computation. Over the 8,125 values of $R$, `record/deterministic/counterexample-search-run-1/README.md` reports that no admissible pair $(p, d)$ satisfies the necessary condition $p - 1 > 2(u/m)^2$ with at least two primes in $u/m$; 274 values satisfy it only with one prime in $u/m$, the case that Theorem 6.3 already covers. The README concludes that Theorem 6.1 "cannot rule out any survivor, whatever t is chosen", and labels the run as evidence about the plan, not an elimination. The record holds no result of running this run's checker, and the run is not journalled.

## Proof in brief

Result 1 is a computation whose logic is short. For each eliminated $u$ the certificate names a unitary divisor $d$ of $u$ and primes $p, q$ of $u$ that satisfy the hypotheses of Theorem 6.3 (the bound $\varphi(d^2) < p\,\varphi(u^2)/(2u^2)$ and condition (108) for every prime of $u$ other than $p$ and $q$) while the inequality (109) fails. By the theorem, no circulant Hadamard matrix of order $4u^2$ exists, hence no Barker sequence of length $4u^2$. The checker recomputes every quantity of the theorem from $(u, d, p, q)$ alone, with its own primality test, trial-division factorisation and multiplicative-order routine.

## What did not work

- The general form of Theorem 6.1 on $R$ (result 3): the record calls the route closed on this residue.
- Turyn's test and Leung-Schmidt (2012) Theorems 3.5 and 3.1 on $R$ (result 2): no elimination.
- Lean formalisation was ranked second and not attempted. The record's ranking says a formal check could only confirm the arithmetic of a certificate, because Mathlib does not hold the theorems of Turyn and Leung-Schmidt.

## Open questions

- The claim itself: the 8,125 values of $R$ remain open.
- Tasks 3 to 6 of `record/tasks.json` are open: validate the implementation of Turyn's test and of Theorems 3.5 and 3.1 against Table 100 of Borwein-Mossinghoff for $\Omega(u) \le 8$; run the three tests on the survivors with certificates; write and run an independent checker for them; search Theorem 6.1 in general form on the survivors.
- Two sets of numbers in the record that do not fit together, which the record does not discuss. `record/problem.json` quotes Table 100 of Borwein-Mossinghoff: Turyn's test, run for $\Omega(u) \le 8$, eliminated 1045 values of $L$, and Theorem 3.5, run on all of $L$, eliminated 4. The record's whole-list run (`record/deterministic/enumeration-run-2/`), which tries the tests in the order Turyn, Theorem 3.5, Theorem 3.1, eliminated 228 values by Turyn's test, none by Theorem 3.5 and 10 by Theorem 3.1 in all of $L$. A validation file for the 10,894 values with $\Omega(u) \le 8$ (`validation/L_omega_le8.certs.jsonl`) holds 9 certificates, all from Theorem 3.1; the record does not say which tests that run applied. The task that would validate the implementation against Table 100 is still open. Smaller validation sets agree with published eliminations: every value of `chm_turyn_22` (22 values), `ls12_thm35_22` (22) and `ls12_thm31_135` (135), which the strategy study traces to Mossinghoff's exclusion file and to Leung-Schmidt 2012, and of two sets of 6 and 3 Barker values has a certificate from the test the set is named after, and the 1371 circulant Hadamard values left open after 2014 have none.

## How to check

The scripts need Python 3; the searches also need sympy (the record used Python 3.11.11 and sympy 1.14). The checkers use the standard library only.

1. Download the list $L$ (`BarkerCandidates100.txt.gz`, 7.7 MB) from the Wayback Machine capture that the record used, <https://web.archive.org/web/20210718130442id_/http://wayback.cecm.sfu.ca/~mjm/WieferichBarker/Data/BarkerCandidates100.txt.gz>, and unpack it as `BarkerCandidates100.txt` in `record/deterministic/enumeration-run-1/`.
2. In that folder run `python3.11 search_thm63.py`. It writes `certificates_thm63.jsonl` (about 77 MB, not included here) and `survivors_thm63.txt`; the recorded run took about 8.5 minutes on one core. Then run `./check.sh`. The expected output, from `result.json`, is `certificates read: 229682, valid: 229682, invalid: 0, survivors: 8125`, then a line saying the counts agree with Leung-Schmidt 2016, then `PASS`.
3. For result 2, copy `survivors_thm63.txt` into `record/deterministic/enumeration-run-3/` as `R_survivors_thm63.txt` and run `python3.11 search_tests.py R_survivors_thm63.txt certificates_R.jsonl survivors_R.txt` (usage in the script's docstring). The expected last line is the one quoted in result 2; the recorded run took about 33 minutes. `./check.sh` runs the independent checker.
4. For result 3, copy `survivors_thm63.txt` into `record/deterministic/counterexample-search-run-1/`, run `python3.11 scan_thm61.py survivors_thm63.txt scan_thm61.jsonl` and then `./check.sh`, which recomputes every record of `scan_thm61.jsonl` independently.
5. The whole-list run of `record/deterministic/enumeration-run-2/` uses the same script on `BarkerCandidates100.txt`; its log ends with `values: 237807  eliminated: {'turyn': 228, 'thm35': 0, 'thm31': 10}  survivors: 237569` after about 512 minutes.

## Contents of this folder

- `README.md`: this file.
- `record/`: the attack's problem statement, journal, studies, task list and the four computation runs, with `record/README.md` describing each file. The input list and the papers are linked above, not copied.

## References

- Borwein and Mossinghoff, LMS J. Comput. Math. 17 (2014) 24-32, doi:10.1112/S1461157013000223, arXiv:1306.0045.
- Leung and Schmidt, "The anti-field-descent method", J. Combin. Theory Ser. A 139 (2016) 87-131, doi:10.1016/j.jcta.2015.11.005.
- Leung and Schmidt, Des. Codes Cryptogr. 64 (2012) 143-151, doi:10.1007/s10623-011-9493-1.
- Mossinghoff, Des. Codes Cryptogr. 53 (2009) 149-163, doi:10.1007/s10623-009-9301-3.
- Turyn, Pacific J. Math. 15 (1965) 319-346.
- Eliahou and Kervaire, Enseign. Math. 38 (1992) 345-382; Eliahou, Kervaire and Saffari, J. Combin. Theory Ser. A 55 (1990) 49-59.
- Lean statement of the Barker conjecture: `FormalConjectures/Arxiv/2104.00502/BarkerSequence.lean` in <https://github.com/google-deepmind/formal-conjectures>.
