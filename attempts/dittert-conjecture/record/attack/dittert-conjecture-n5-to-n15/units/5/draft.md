# Dittert's conjecture for 7 <= n <= 15: where the known routes stop, and one lemma that would finish it

## The problem

K_n is the simplex of nonnegative n x n real matrices with entry sum n, phi(A) = prod r_i +
prod c_j - per(A), and Dittert's conjecture (Minc 1983, Conjecture 28) says phi(A) <= 2 - n!/n^n
with equality only at J_n/n. Known: n = 2 (Sinkhorn 1984), n = 3 (Hwang 1987), n = 4
(arXiv:2607.29191, 2026-07-31), n = 16 (arXiv:2607.19439, 2026-07-21), n >= 17 (arXiv:2606.01531,
2026-06-01), and, from this record, n = 5 and n = 6 (units 1, 2). Open: 7 <= n <= 15.

## Route 1: boundary exclusion (the analytic route), and its exact stopping point

Every proof for n >= 16 shows that a maximiser cannot have a zero entry and finishes with
Hwang's positive-support theorem. Kafidov's version is dimension-free except for one rational
inequality, K_n = m_n - gamma_n - n^3 m_n^2/(4(1 - gamma_n)) > 0 with gamma_n = n!/n^n and m_n
the Knopp-Sinkhorn boundary minimum. **Exactly** (`deterministic/certified-special-case-check-3`,
two exact implementations; `deterministic/formal-check-1`, kernel-checked in Lean 4 at n = 15
and 16): K_n > 0 iff n >= 16, and at n = 15 the ratio of the two sides is 0.98712. Removing
the Bernoulli step and sharpening Pinsker recovers under one percent of the gap; the loss is
structural: the chain proves cap(A) >= (1-t)^n for the capacity of A, whereas in every sampled
near-doubly-stochastic matrix cap(A) = exp(-(rho' + sigma')(1 + o(1))) with rho', sigma' the log
row- and column-product deficits (`study/capacity-numerics.py`: the published bound loses a
factor between 400 and 17000). Unit 3 replaces the uniform dilation by the chi-square-nearest
doubly stochastic competitor and proves: **if every near-maximiser with a zero has spectral
gap lambda_2(A) >= c_n, Dittert's conjecture holds at n** (Theorem R), with c_7 = 0.183 down to
c_15 = 0.0035.

**Conjecture G(n, c_n).** Every A in K_n with phi(A) >= 2 - gamma_n and a zero entry has
lambda_2(A) = 1 - sigma_2(D_r^{-1/2} A D_c^{-1/2}) >= c_n.

Evidence (`deterministic/numerical-optimisation-run-4`, independently re-evaluated): minimising
lambda_2 over doubly stochastic matrices with a zero and per <= 1.05 gamma_n gives 0.697, 0.696,
0.726, 0.733 at n = 5, 6, 7, 8 (required: 0.612, 0.323, 0.183, 0.108), every minimiser on the
constraint per = 1.05 gamma_n; 1200 random samples at n = 5, 8, 12 (`study/per-vs-gap-numerics.py`)
show per <= 1.05 gamma_n forcing lambda_2 >= 0.71, 0.78, 0.86 and lambda_2 <= 0.3 forcing
per >= 1.6 gamma_n. The conjecture is a weak, explicit stability statement for the van der
Waerden inequality; no theorem of that kind was found in print.

## Route 2: exact sum-of-squares certificates (the computational route), and its reach

The n = 4 pipeline needs, at n = 5, a Gram matrix over 2925 monomials; with the symmetry group
G_n the blocks are at most 16 (main) and 22 (multipliers) at n = 5 and 6, which is why units 1
and 2 exist (unit 4). The block sizes at fixed certificate degree do not grow with n, but the
degree does: at n = 7 and 8 the main blocks are 83 and the multiplier blocks 2514 (feasible with
orbit canonical forms and a large SDP; not attempted); from n = 9 the blocks are 424 and 22818
and up (`study/gate-symmetry-blocks/blocks-output.txt`). A direct attempt at n = 7 with the
present code exceeded 11 GB in the exact expansion of the degree-8 gap polynomial within 300 s.

## Two more facts about the boundary

The maximum of phi on the face a_11 = 0 is 2 - m_n at n = 5 and n = 6, attained at the
Knopp-Sinkhorn extremal T_n (multi-start optimisation, exact re-evaluation at the optimisers,
`deterministic/numerical-optimisation-run-1`): lowering the row or column products to reduce
the permanent never pays, and the boundary gap equals the full Knopp-Sinkhorn gap m_n - gamma_n.
And the stability constants obtained on the computational route are c_1 = 1/52, 32/3125,
128/46656 at n = 4, 5, 6, all below the numerical optima (0.0192, 0.0128, 0.0037 per unit of
||A - U_n||_F^2).

## Open questions, one sentence each

1. Prove G(n, c_n) for 7 <= n <= 15, or any lower bound on the spectral gap of a near-maximiser
   with a zero that decreases no faster than sqrt(gamma_n).
2. Compute the G_7 and G_8 certificates (orbit canonical forms; a block-2514 SDP).
3. Verify the n = 5 certificate in Lean 4 (its statement is `dittert_five_stability` in
   `deterministic/formal-check-1/Main.lean`; the isotypic reduction or block certificates are
   the two routes).
4. Replace the verified floating-point step of the n = 6 certificate by an exact isotypic
   check (class-based projectors of G_6).
5. Decide whether the face maximum equals 2 - m_n for every n >= 4, which would be a
   boundary form of the conjecture sharper than the conjecture itself.

## The record

The full attack record (13 moves, 4 failure signals, the walk, the ledger of costs) is
`units/INVENTORY.md` and `journal.jsonl` of the workspace `attack/dittert-conjecture-n5-to-n15`.
