# Evaluation of units/3/draft.md (second reader, 2026-09-03)

Read against unit.json, study/route-a-reduction-theorem.md (the proof text), the journal
excerpt for moves 8 and 9, deterministic/certified-special-case-check-3 and
numerical-optimisation-run-4 (cited for context), and the novelty record.

1. **Statement.** Theorem R and Hypothesis G(n, c) in the draft are unit.json's statement
   with the same constants (gamma_n, h_n, theta_n, kappa_n, c_n) and the same conclusion.
   Match.
2. **Proof.** The proof text was read in full. Lemma 1(i) (per = per(B) cap(A)) and 1(ii)
   (Jensen) are complete. Lemma 2: the kernel of L is span{(1;-1)} by full indecomposability;
   (u; v) is orthogonal to it because sum u = sum v = 0; B' has unit margins; the sign
   condition (N) is stated as a hypothesis and discharged in the theorem. The identity
   sum alpha + sum beta = (u; v)^T (alpha; beta) uses the first n equations summed; checked.
   Lemma 3(a): the inequality log(1 + x) <= x - x^2/2 + x^3/3 for x > -1 and the use of
   Thm 2.1 with k = 1 (|r_i - 1| <= sqrt(2 delta) <= h_n) are correct; the constant kappa_n
   follows. Lemma 3(b), (c): the congruence L = S L~ S, the eigenvalues 1 +- sigma_k(M), the
   kernel of L~, and the orthogonality of S^{-1}(u; v) to it are verified; the bounds use
   r_i, c_j >= theta_n. The theorem's final inequality m_n sqrt(kappa_n/gamma_n) < 1 was
   recomputed for 4 <= n <= 15 (maximum 0.40 at n = 4). The values of c_n in the table were
   recomputed to four figures and agree.
3. **Citations.** Hwang 1986 (doi:10.1016/0024-3795(86)90212-0), Cheon-Wanless 2012
   (doi:10.1016/j.laa.2010.08.041, Thms 2.1 and 3.2 read in the fetched full text),
   Knopp-Sinkhorn 1982 (doi:10.1080/03081088208817459, used through the two 2026 preprints),
   Sinkhorn-Knopp 1967 (full indecomposability implies a scaling; standard). All resolve.
4. **Ledger.** costs = [obligations]; the draft names the owed statement, G(n, c_n), as the
   hypothesis of the theorem and takes the conditional form. Correct.
5. **Findings.** The draft states the evidence for the hypothesis as numerical and does not
   overclaim. One point to keep visible in any write-up: at n = 4 the theorem is vacuous
   (c_4 > 1), which the draft says. It passes.
