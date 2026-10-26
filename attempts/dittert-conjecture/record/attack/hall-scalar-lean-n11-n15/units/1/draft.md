# A Lean certificate for scalar Hall exclusion in dimensions 11 through 15

This note presents a partial formalization of an existing Dittert proof layer. The mathematical scalar argument is attributed to Pedro Paulo Marques do Nascimento's public working proof, pinned to commit 894066bbaa715138c98bf3cb7c6fdb4f39a37701 at https://github.com/pedromnasc/dittert-conjecture-proof. It is not a new mathematical solution or a complete matrix-level Lean proof. Prior Dittert Lean work includes Li, Xiong and Yang, arXiv:2607.29191v2.

## Exact statement

For positive integers k, put \(\gamma_k=k!/k^k\). Let \(11\le n\le15\) and let natural a,b satisfy \(0<a+b<n\). In the proper case \(a,b>0\), set
\[
M=\frac{\gamma_{n-a}\gamma_{n-b}}{\gamma_{n-a-b}},\qquad
C=\frac{7n(n-a-b)^2}{16\{a(n-a)+b(n-b)\}}.
\]
In either marginal orientation, meaning a=0 or b=0, set
\[
M=(n-2)!\left(\frac{n-2}{(n-1)^2}\right)^{n-2},\qquad
C=\frac{7n}{16(n-1)}\left(1+(1-\gamma_n)^2\right).
\]
Then, for every real \(u\le1\),
\[
Cu^2+M(1-u)^n-\gamma_n>0.
\]
Consequently no real P and delta simultaneously satisfy
\[
P\ge M(1-u)^n,\qquad \delta\ge Cu^2,\qquad P+\delta\le\gamma_n.
\]
The exact rational formulas are in deterministic/formal-check-1/Definitions.lean. HallScalar.scalar_positive is the first theorem; HallScalar.scalar_exclusion and hall_scalar_certificate state the consequence. No sign assumptions on P or delta are needed.

## Finite arithmetic and complete scalar coverage

For each dimension, kernel reduction proves
\[
M>0,\quad C>0,\quad D=4C(M-\gamma_n)-(nM)^2>0.
\]
The finite propositions quantify over every ordered pair in Fin15 satisfying the reduced predicate. That predicate contains all proper pairs and one normalized marginal pair (n-1,0). There is no quotient by transposition for the proper cases.

The dimension counts are 46, 56, 67, 79, and 92, totaling 340. Both the counts and their sum are Lean theorems in Finite.lean. The natural-size theorem all_good proves that every original nonfull pair is represented: proper coordinates are less than15, and both marginal orientations give constants identical to those at (n-1,0). The independent combinatorial review counts335 proper cases and120 uncompressed marginal cases, hence455 original nonfull pairs. That last cardinality is a transparent external count; the universal coverage itself is formalized.

## Real proof

Transport the positive rational constants and discriminant into the real field. The identity
\[
4C(Cu^2-nMu+M-\gamma_n)
=(2Cu-nM)^2+D
\]
is verified by the ring tactic. Its right side is positive for every real u, and C>0. Bernoulli's inequality, applied to -u with u<=1, gives \((1-u)^n\ge1-nu\). Multiplication by positive M proves the claimed strict inequality. Adding the two purported lower bounds contradicts the budget inequality. This is the human-readable form of Main.lean; it is the same analytic scalar route as the source, not an independent second proof.

## Verification and reproduction

Both harness formal checks report pass. A fresh independent reader reran them sequentially and separately printed the axiom closures of scalar_positive, scalar_exclusion, finite_certificate and hall_scalar_certificate. Each list is precisely propext, Classical.choice and Quot.sound. Source hashes were unchanged by those runs. See study/final-review.md and the two result.json files.

The package pins Lean v4.33.1 and Mathlib commit0df444a360eaa60ab8c11dca51a86af692955474. The manifest pins upstream revisions. Replay instructions are in deterministic/formal-check-1/README.md. The second package snapshots the same finite Lean source and audits its finite theorem separately; it is not an independent implementation. Kernel checking, the formal statement's fidelity and trust in the installed environment are distinct considerations. No alternate-kernel checker or clean rebuild of all Mathlib dependencies was run.

The temporary initial skeleton was deliberately rejected by the axiom gate because it used sorryAx. Its result is preserved at study/initial-red-result.json, not used as positive evidence. All its proof obligations are discharged by the final code.

## Contribution and limitations

The contribution is the concrete formal artifact: direct exact formulas, exhaustive scalar coverage, the finite criterion, and its connection to a real inequality. It is suitable to assess as a limited reproducible verification note, not as a claimed new mathematical theorem or a first formalization of Dittert.

The matrix reduction is not formalized. In particular, no theorem here constructs a dominated doubly stochastic matrix, proves a permanent floor for it, derives deficit bounds from stationarity, selects a minimum row in the marginal case, or excludes the full cut (0,0). Those are separate analytic inputs in the existing mathematical proof. The scope says nothing about a full Lean result in n5,6, n7 through10, or dimensions above15. The stronger scalar domain u<=1 does not extend the matrix-derived interfaces to negative u.

The stage-3 novelty report and later bounded searches identify earlier mathematics and formalization work but do not prove priority. Correctness of this artifact and the eventual scientific value of a manuscript remain different judgments.
