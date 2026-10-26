# Inventory: dittert-conjecture-n5-to-n15

Every journal move and what its output leaves in the record, grouped by
strategy. A move marked as a fired failure signal leaves what that
strategy's Failure signal names. Convert each into a unit under
CASHOUT.md or discard it.

Walk: reduce-to-a-finite-computation -> decompose-and-parallelise -> ladder-the-parameter -> reduce-to-a-finite-computation -> decompose-and-parallelise -> verify-formally-with-lean4.

Costs paid across the attack: axioms, bound_quality, obligations.

## decompose-and-parallelise

- move 7 (pass 1, split-into-components-with-explicit-interfaces, paid obligations): Component table (interface, current value, status). n = 5: route B, lambda = 32 exact, closed (move 5). n = 6: route B, lambda = 128 exact with a verified floating-point step, closed (move 6). n = 7: route B, main block 83, multiplier blocks 2514, pair-orbit computation 7e10 pairs; open, needs orbit canonical forms and a block-2514 SDP; route A r_7 = 0.025. n = 8: route B same block sizes with more copies; open; r_8 = 0.031. n = 9, 10: route B blocks 424 and 22818; out of reach at minimal degree; r = 0.044, 0.065. n = 11, 12: route B blocks 2099 and 198774; out of reach; r = 0.104, 0.172. n = 13: r_13 = 0.298, open. n = 14: r_14 = 0.535, open. n = 15: r_15 = 0.987, open by 1.3 percent of the Kafidov scalar (0.8 percent of the gap without Bernoulli). n = 16: r_16 = 1.87, closed in print. Sharpened route-A interface: every n >= 4 closes if lambda_2(A) >= 1/2 for near-maximisers with a zero (numerically lambda_2 >= 0.71, 0.78, 0.86 at n = 5, 8, 12 whenever per <= 1.05 gamma_n); for n = 15 alone, any rung that reduces the loss by a factor 1.014 closes it, for n = 14 a factor 1.87, for n = 13 a factor 3.4. The final bound is the conjunction of the eleven interfaces; the ledger owes: exact certificates at n = 7, 8 (engineering), and one lemma (spectral gap from a small permanent) for 9 <= n <= 15, which also re-proves 5 <= n <= 8. Obligations paid: the interfaces are statements still owed.
- move 12 (pass 2, make-the-bound-explicit-then-attack-the-lossiest-step, failure signal fired, paid obligations): The final ledger. Closed: n = 5 (exact), n = 6 (verified numerics at one step). Open with a known next step: n = 7, 8 (route B, orbit canonical forms and a block-2514 SDP; estimated as days of engineering, not attempted). Open with an unknown next step: 9 <= n <= 15 (route B out of reach; route A conditional on G(n, c_n)). The hardest component is a known barrier for this record: every route present either stops at it (route A) or cannot reach the dimensions it governs (route B), and no move available to the walk changes that. Failure signal of decompose-and-parallelise: a component is a known barrier the bound cannot move without; the record gains the ceiling, namely the statement G(n, c_n) with the explicit constants of Theorem R and the evidence of run 4. The bound under the hardest component as hypothesis is Theorem R (conditional result, form 1); each closed component is a special case (form 1); the interface table is the reduction (form 3).

## ladder-the-parameter

- move 8 (pass 1, make-the-bound-explicit-then-attack-the-lossiest-step, paid obligations): The ledger. Losses by step at n = 15 (exact and 60-digit computations in study/kafidov-threshold.py): (a) none; (b) at most 0.4 percent of the gap; (c) none beyond (b); (f) 0.5 percent of the gap; (d) the whole remaining loss: the chain proves cap(A) >= (1-t)^n ~ 1 - n^{1.5} sqrt(delta), while in every sampled near-doubly-stochastic matrix cap(A) = exp(-(rho' + sigma')(1 + o(1))), a loss of the factor n^{1.5} sqrt(delta) / delta ~ n^{1.5}/sqrt(delta), between 400 and 17000 in the samples (study/capacity-numerics.py). The lossiest step is (d), the capacity lower bound by uniform dilation, and it is a free choice: any doubly stochastic B with supp B contained in supp A gives cap(A) >= exp(sum_ij b_ij log(a_ij/b_ij)) (a one-line Jensen argument, recorded in study/route-a-capacity-notes.md), of which the dilation is the choice B <= (1-t)^{-1} A. Step (d) therefore selects the rung of step 3: choose B as the nearest doubly stochastic matrix to A in the chi-square sense. The ledger owes the proof that this choice loses only O(rho' + sigma') (obligations).
- move 9 (pass 2, choose-the-auxiliary-weight-or-certificate, paid obligations): Theorem R (study/route-a-reduction-theorem.md, proved with every constant explicit): for n >= 4, if every A in K_n with phi(A) >= 2 - gamma_n and a zero entry has lambda_2(A) >= c_n := 2 sqrt(gamma_n kappa_n)/theta_n, then Dittert's conjecture holds at n. The rung is therefore the spectral-gap statement G(n, c_n), with c_7 = 0.183, c_8 = 0.108, c_9 = 0.065, c_10 = 0.040, c_11 = 0.024, c_12 = 0.015, c_13 = 0.0091, c_14 = 0.0056, c_15 = 0.0035 (c_5 = 0.61, c_6 = 0.32; c_4 = 1.35 makes the theorem vacuous at n = 4). No exact final comparison per n remains: once G(n, c_n) holds, the contradiction m_n - gamma_n <= delta (2 m_n kappa_n/(theta_n c) - 1) < 0 is immediate for every delta in (0, gamma_n]. The remainder handed to the next move is G(n, c_n): a stability statement for the van der Waerden inequality (a near-doubly-stochastic matrix with a zero entry and permanent below gamma_n has second singular value at most 1 - c_n), not in print. Obligation: G(n, c_n).
- move 10 (pass 2, optimise-the-certificate-family-numerically, failure signal fired): Evidence: the smallest gap found is lambda_2 = 0.697, 0.696, 0.726, 0.733 at n = 5, 6, 7, 8, against the required c_n = 0.612, 0.323, 0.183, 0.108 (ratios 1.1, 2.2, 4.0, 6.8); every minimiser sits on the constraint per = 1.05 gamma_n, so on the set G(n, c) concerns (per <= gamma_n) the gap is larger still. No counterexample to the rung; no proof of it either. Failure signal of ladder-the-parameter: the remainder is the whole difficulty. The record gains the rung and the remainder as exact statements: rung = Theorem R (study/route-a-reduction-theorem.md; every n >= 4 with G(n, c_n) closes with no further computation), remainder = G(n, c_n) for 7 <= n <= 15, an explicit-constant stability statement for the van der Waerden inequality that is not in print and that this walk cannot prove within its budget. The value of the ladder did not rise past the current rung in three moves (8, 9, 10).

## reduce-to-a-finite-computation

- move 1 (pass 1, choose-the-auxiliary-weight-or-certificate, paid obligations): Residue R_n, one per n in 5..15, with completeness: a maximiser of phi on K_n exists (compactness); a positive one is J_n/n (Hwang 1986); so the claim for n holds as soon as no A in K_n with a zero entry has phi(A) >= 2 - gamma_n, and it suffices to prove EITHER (A) cap(A) > (gamma_n - delta)/m_n for every fully indecomposable A in K_n with a zero entry, phi(A) >= 2 - gamma_n, per(A) = gamma_n - delta, 0 < delta <= gamma_n, rho + sigma <= delta (rho, sigma the row- and column-product deficits), which is a finite-dimensional inequality in (A) per n whose published scalar-dilation special case proves it for n >= 16 and fails for n <= 15 by the exact ratios in study/kafidov-threshold.py; OR (B) an exact rational identity Q_n - lambda Delta_n (sum x/n)^{2D-2} = sigma_0 + sum_{i<j} x_i x_j sigma_ij with lambda > 0 rational and every sigma an SOS given by a PSD rational Gram matrix, since every term on the right is nonnegative on K_n and Delta_n > 0 off U_n, which also yields the quantitative form with c_1 = lambda/n^n. Obligation owed: for (A), a lower bound on cap(A) in terms of (rho, sigma, n) sharper than (1-t)^n, not in print; for (B), existence of the certificate at degree 2D, unknown for n >= 5. The optimisation handed on: (A) maximise the capacity loss over the constraint set to locate the worst A and the minimal sharpening; (B) the SDP max lambda over the symmetry-adapted template at n = 5.
- move 2 (pass 1, predict-the-value-and-test-it-numerically): Evidence, all numerical. (1) The maximum of phi on the face a_11 = 0 is 2 - m_n at n = 5 and n = 6, attained at the Knopp-Sinkhorn extremal T_n (R = C = 1, per = m_n to 8 digits): the trade-off never pays, the boundary gap equals the full Knopp-Sinkhorn gap m_n - gamma_n (5.3 percent of gamma_5, 1.9 percent of gamma_6), and the prediction of extra slack is refuted; the extremal structure on the face is T_n. Independently checked in exact rational arithmetic at the recorded optimisers (result.json: pass). (2) At n = 5 the degree-6 pairwise template is feasible with lambda* = 40.1156 (kappa = lambda/3125 = 0.01284; the proved n = 4 constant is 1/52 = 0.0192), residual 6e-7, minimum block eigenvalue -1.3e-5; the certificate exists numerically and its exact recovery is the next step; independently checked by direct polynomial evaluation at 200 random points of K_5 (result.json: pass). (3) In 18 random near-doubly-stochastic samples with a zero at n = 5, 8, 15, -log cap(A) / (rho' + sigma') lies in [0.67, 1.18] while the published dilation loses 400 to 17000 times rho' + sigma'; in 1200 doubly stochastic samples with a zero, per(B) <= 1.05 gamma_n forces lambda_2(B) >= 0.71 (n = 5), 0.78 (n = 8), 0.86 (n = 12), and lambda_2 <= 0.3 forces per(B) >= 1.6 gamma_n. Corrected conjecture for route A (study/route-a-capacity-notes.md): for A in K_n with phi(A) >= 2 - gamma_n, cap(A) >= exp(-2 delta / lambda_2(A)) via the entropy dual of the capacity and a chi-square margin correction, and lambda_2(A) >= 1/2; if proved, m_n exp(-4 delta) > gamma_n - delta closes every n >= 4 with one rational inequality per n. The structural data extracted: the singular direction of every Gram block is the projection of z(U_n) onto the trivial isotypic component, so only the trivial blocks are forced singular.
- move 3 (pass 1, optimise-the-certificate-family-numerically, paid bound_quality): Evidence: at n = 5 and lambda = 32 the symmetry-adapted pairwise family contains a certificate whose Gram blocks are positive definite with margin 0.343 off the one forced null vector 1; the recovery target is fixed (rational lambda = 32, common-denominator rounding of the multiplier orbit coordinates, exact projection of the main orbit coordinates onto the 156 coefficient equations and the M 1 = 0 equations, exact positive-semidefiniteness through the rational isotypic projectors of G_5). Cost: bound_quality, since 32/3125 is below the numerical optimum 40.1/3125.
- move 4 (pass 1, optimise-the-certificate-family-numerically): Evidence: at n = 6 the minimal-degree pairwise family contains a certificate with lambda* = 174.8926 (kappa = lambda*/6^6 = 0.003749), residual 8.7e-7, minimum block eigenvalue -1.3e-4. The stability constants on route B so far: kappa_4 = 1/52 (in print), kappa_5 ~ 0.0128 (exact at 32/3125), kappa_6 ~ 0.0037. The family's value stays visibly positive, so no exactness is conjectured; the target for the exact recovery at n = 6 is the rational lambda = 128 (kappa = 128/46656 = 0.00274), for which the margin-maximising solve gives margin 1.25. The block sizes at fixed certificate degree do not grow with n (the same 16 and 22 at n = 5 and 6), confirming the gate table; what grows is the number of monomials to expand (4.5e6 at n = 6, 2.7e5 degree-4 monomials but 7e10 ordered pairs at n = 7 for the main pair-orbit computation, beyond the label-propagation method's memory).
- move 5 (pass 1, certify-the-finite-residue-by-computation): The n = 5 component of the claim is closed: for every A in K_5, phi(U_5) - phi(A) >= (32/3125) ||A - U_5||_F^2, hence phi(A) <= 2 - 5!/5^5 with equality only at U_5. Evidence: deterministic/certified-special-case-check-1 (certificate, README, result.json), produced by deterministic/numerical-optimisation-run-2/recover5.py. The residue of route B is settled for n <= 5 (n = 4 in print, n = 5 here); the first open instance is n = 6, whose numerical certificate exists (lambda* = 174.9, numerical-optimisation-run-3) and whose rational recovery is running. The trusted base of the exact check is Python integer arithmetic and python-flint; no Lean check yet (the formal check is the obligation still owed for the mode certificate as the input defined it).
- move 6 (pass 1, certify-the-finite-residue-by-computation, paid axioms): The n = 6 component of the claim is closed as a full proof by computation with one non-exact step: for every A in K_6, phi(U_6) - phi(A) >= (128/46656) ||A - U_6||_F^2, hence phi(A) <= 2 - 6!/6^6 with equality only at U_6. The first implementation checks the multiplier matrices exactly (flint) and the main matrix by verified floating-point Cholesky; the second implementation checks the identity exactly and all three matrices by verified floating-point Cholesky with Higham's a posteriori bound (a certified-numerics argument in IEEE-754 double precision, not exact arithmetic). Route B's residue is now settled for n <= 6; the first open instance is n = 7, where the main Gram matrix has 270725 monomials (blocks up to 83) and the multiplier matrices 20825 (blocks up to 2514), and the pair-orbit label propagation of this pipeline needs 7e10 pairs, beyond memory: the case count passes this solver's reach at n = 7 unless orbits are computed by canonical forms and the multiplier SDP is solved at block size 2514. Cost paid: axioms, in the sense the harness uses for a machine check outside exact arithmetic (the trusted base grows by LAPACK's floating-point Cholesky and its error analysis).
- move 11 (pass 2, enumerate-small-cases-to-locate-the-threshold, failure signal fired, paid bound_quality): Failure signal of reduce-to-a-finite-computation: the case count passes the solver's reach. The record gains the settled range, n <= 6 (n = 4 in print, n = 5 exact, n = 6 with one verified-floating step), and the first open instance, n = 7, together with what reaching it needs: the gap polynomial and the orbit structure computed in G_n-orbit coordinates from the start (canonical forms of monomials under row and column permutations and transpose, never the monomial list), and an SDP with blocks of size up to 2514 (main blocks at most 83). Estimated as days of engineering with the same mathematics; not attempted within this budget. Bound quality is what the strategy gives up here: the closed range stops below the target.

## verify-formally-with-lean4

- move 13 (pass 2, formalise-while-fresh, failure signal fired, paid obligations): Certificate: the exact stopping point of the published analytic route is kernel-checked (formal-check-1, pass, standard axioms): its final inequality holds at n = 16 and fails at n = 15. Blueprint: the n = 5 theorem and its quantitative form are stated in Lean and elaborate (Main.lean, two sorry warnings), which fixes the target of the formal certificate check. Failure signal of verify-formally-with-lean4: the axiom check of the claim's theorem (dittert_five) reports sorryAx, and the finite check that would discharge it is not encodable within the budget; the record gains the checked statement file, the axiom list of the residue theorem, and the conditional theorem (the claim at n = 5 modulo the certificate check). Obligations: the two sorry theorems.


## Inventory of what stands (declare-the-stall-and-inventory-what-stands, 2026-09-03)

Rule that started the cash-out: `plan` admitted no opening. Four strategies ended on their
own failure signals (ladder-the-parameter at move 10, reduce-to-a-finite-computation at
move 11, decompose-and-parallelise at move 12, verify-formally-with-lean4 at move 13); the
two remaining admitted strategies could not be entered (attack-the-negative-side precedes
ladder-the-parameter and strengthen-and-generalise precedes verify-formally-with-lean4,
both of which had run) and were closed with `fail` for that structural reason. A move 14
under strengthen-and-generalise (the statement moved to Hypothesis G) was prepared and
refused by the walk rule; the problem record was restored to its move-13 state, so the
statement attacked stayed the claim throughout.

### Candidate claims (self-check applied: one sentence, a claim, not in the literature, evidence named)

1. **Special case, n = 5** (form: conditional-or-special-case). For every nonnegative 5 x 5 real
   matrix A with entry sum 5, phi(U_5) - phi(A) >= (32/3125) ||A - U_5||_F^2; hence Dittert's
   conjecture holds at n = 5. Evidence: deterministic/certified-special-case-check-1 (exact
   rational certificate; first implementation exact throughout, second implementation exact
   except a verified floating-point Cholesky). Moves 3, 5. Ledger: bound_quality (32/3125 is
   below the numerical optimum 40.1/3125). On the path to the target.
2. **Special case, n = 6** (form: conditional-or-special-case). For every nonnegative 6 x 6 real
   matrix A with entry sum 6, phi(U_6) - phi(A) >= (128/46656) ||A - U_6||_F^2; hence Dittert's
   conjecture holds at n = 6. Evidence: deterministic/certified-special-case-check-2 (rational
   certificate; the identity and the multiplier matrices exact in the first implementation,
   the 8435 x 8435 main matrix's positive definiteness verified in IEEE-754 double precision
   with Higham's bound in both implementations). Moves 4, 6. Ledger: axioms (the floating-point
   verified step). On the path.
3. **Conditional result for 7 <= n <= 15** (form: conditional-or-special-case). For n >= 4, if
   every A in K_n with phi(A) >= 2 - n!/n^n and a zero entry has spectral gap lambda_2(A) >= c_n
   (Theorem R's explicit constant, 0.183 at n = 7 down to 0.0035 at n = 15), then Dittert's
   conjecture holds at n. Evidence: study/route-a-reduction-theorem.md (proof text, every
   input cited). Moves 8, 9. Ledger: obligations (the hypothesis G(n, c_n)). On the path.
4. **New machinery** (form: new-machinery). The symmetry-reduced exact-certificate pipeline for
   G_n-invariant polynomial inequalities on the matrix simplex: character-theoretic block
   sizes, numerical block diagonalisation by two generic invariant matrices, orbit-coordinate
   coefficient equations, margin-maximising SDP, numerical projection with exact pivot fix,
   exact positive-semidefiniteness through rational isotypic projectors. Evidence:
   deterministic/numerical-optimisation-run-3 (sdp_n.py, recover_n.py, result.json) with the
   n = 5 instance in numerical-optimisation-run-2 and the block table in
   study/gate-symmetry-blocks. Moves 2, 3, 4. Ledger: bound_quality. Off to the side (reusable
   for any G_n-invariant inequality on K_n, e.g. the permanent inequalities of the same family).
5. **Problem paper** (form: survey-or-problem-paper). The exact state: the published analytic
   route's final inequality holds iff n >= 16 (exact, and kernel-checked at 15 and 16); the
   boundary maximum on the face a_11 = 0 is 2 - m_n at n = 5, 6 (numerical, checked exactly at
   the optimisers); the ladder of losses with the capacity step as the whole loss; the
   conjecture G(n, c_n) with its numerical evidence (smallest gap 0.70 against 0.18 required at
   n = 7); the reach of the SOS route (n = 7, 8 as engineering; n >= 9 out of reach at minimal
   degree); the Lean blueprint of the n = 5 theorem. Evidence: deterministic/certified-special-
   case-check-3, formal-check-1, numerical-optimisation-run-1, numerical-optimisation-run-4,
   and this inventory. Moves 2, 10, 11, 12, 13. Ledger: bound_quality, obligations.

Discarded: nothing further survives the claim test; the numerical values of moves 2-4 are
content of units 4 and 5.

### The exact state of the attack (problem-paper content)

Fired: ladder-the-parameter (the remainder G(n, c_n) is the whole difficulty),
reduce-to-a-finite-computation (n = 7 beyond the pipeline's reach: exact expansion of a
degree-8 polynomial in 49 variables and 7e10 pair orbits), decompose-and-parallelise (the
hardest component is a barrier for every route in the record), verify-formally-with-lean4
(the certificate check of n = 5 is not encodable within budget; the residue theorem at n = 16
is kernel-checked). Not entered: attack-the-negative-side, strengthen-and-generalise
(precedence). The ceiling: one lemma, G(n, c_n), an explicit-constant stability statement for
the van der Waerden inequality, would close 7 <= n <= 15 at once and re-prove 5, 6; nothing
in the record moves it. Obligations still owed: G(n, c_n) for 7 <= n <= 15; the Lean checks
of the n = 5 and n = 6 certificates; the exact (non-floating) positive-definiteness check of
the n = 6 main matrix.
