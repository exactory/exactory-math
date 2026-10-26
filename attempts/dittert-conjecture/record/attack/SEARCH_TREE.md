# Mathematical search tree

Generated from .search/tree.json; do not edit.

Objective: objective-000001

For every integer n with 5 <= n <= 15 and every n by n real matrix A whose entries are all nonnegative and whose entries sum to n, with r_i(A) the row sums and c_j(A) the column sums, prod_i r_i(A) + prod_j c_j(A) - per(A) <= 2 - n!/n^n, and equality holds if and only if every entry of A equals 1/n.

Quantifiers: For every integer n with 5 <= n <= 15; for every n by n real matrix A with all entries nonnegative and total entry sum n.
Assumptions: []
Proof policy: lean-kernel
Recorded proof status: open
Execution status: running
Freshness: unchecked by this generated view.

## Residual obligations

- obligation-000001: For every integer n with 5 <= n <= 15 and every n by n real matrix A whose entries are all nonnegative and whose entries sum to n, with r_i(A) the row sums and c_j(A) the column sums, prod_i r_i(A) + prod_j c_j(A) - per(A) <= 2 - n!/n^n, and equality holds if and only if every entry of A equals 1/n.
- obligation-000002: For every integer n with 5 <= n <= 6 and every n by n real matrix A whose entries are all nonnegative and whose entries sum to n, prod_i r_i(A) + prod_j c_j(A) - per(A) <= 2 - n!/n^n, and equality holds if and only if every entry of A equals 1/n.
- obligation-000003: For every integer n with n = 7 and every n by n real matrix A whose entries are all nonnegative and whose entries sum to n, prod_i r_i(A) + prod_j c_j(A) - per(A) <= 2 - n!/n^n, and equality holds if and only if every entry of A equals 1/n.
- obligation-000004: For every integer n with 8 <= n <= 10 and every n by n real matrix A whose entries are all nonnegative and whose entries sum to n, prod_i r_i(A) + prod_j c_j(A) - per(A) <= 2 - n!/n^n, and equality holds if and only if every entry of A equals 1/n.
- obligation-000005: For every integer n with 11 <= n <= 15 and every n by n real matrix A whose entries are all nonnegative and whose entries sum to n, prod_i r_i(A) + prod_j c_j(A) - per(A) <= 2 - n!/n^n, and equality holds if and only if every entry of A equals 1/n.
- obligation-000010: For every integer n >= 3 and every n by n real matrix A with nonnegative entries and total entry sum n that attains the maximum of Phi over that set and has at least one zero entry: no s rows and n - s columns of A with 1 <= s <= n - 1 form a zero block, and A has two zero entries in distinct rows and distinct columns.
- obligation-000011: For every integer n with 8 <= n <= 10 and every n by n doubly stochastic real matrix B having zero entries at two positions in distinct rows and distinct columns, per(B) >= kappa(n) (1 + 1/(2 n^2)), where kappa(n) = (n-2)! ((n-2)/(n-1)^2)^(n-2).
- obligation-000012: The n = 7 finite certificates of attack/hall-n7-branch-coverage/COVERAGE_PROOF.md hold: the six ordinary and six mixed margins M(L, c, lambda) are positive; W(t) = (2/3)(1-g)^2 (1-t)^6 - g (7 - 21 t + 35 t^2)^2 with g = 720/117649 is positive for every real t in [0, 3/20]; and for each pair (a,b) in {(1,5),(2,4),(3,3)} and every point (e,f) of the closed square [0,3/20]^2, G(e,f) > 0 or (N(e,f) > 0 and F(e,f) > 0), with G, N, F the polynomials defined there.
- obligation-000013: The n = 8, 9, 10 finite certificates of attack/hall-n8-n15-branch-coverage/PROOF.md hold, with gamma(n) = n!/n^n, kappa(n) = (n-2)! ((n-2)/(n-1)^2)^(n-2), L_n = kappa(n) (1 + 1/(2n^2)), nu(n,a,b) = gamma(n-a) gamma(n-b) / gamma(n-a-b), the curvature C = 7 n (n-a-b)^2 / (16 (a(n-a) + b(n-b))) for a, b >= 1 and C = (7n/(16(n-1))) (1 + (1 - gamma(n))^2) for the marginal cut, and the floor M = max(nu(n,a,b), L_n) for a, b >= 1 and M = L_n for the marginal cut: (i) for every ordered proper cut (a,b) with a, b >= 1, a + b <= n - 1, 8 <= n <= 10, and for the marginal cut (a,b) = (9,0) of n = 10, with u-bar the least positive multiple of 10^-6 satisfying u-bar^2 >= gamma(n)/C and beta = ((1-u-bar)^n - 1 + n u-bar)/u-bar^2: 0 < u-bar < 1, beta > 0, M > gamma(n) and M - gamma(n) - n^2 M^2 / (4 (C + beta M)) > 0; (ii) with E(u) = 1 - (2 - gamma(n)) u, H(u) = (1 - gamma(n)) u, T(u) = E(u) - H(u)/(n-1), f(u) = (1-u)(1 + u/(n-1))^(n-1) and p_n(u) = (2 - gamma(n) + L_n (1-u)^n - f(u)) E(u)^n - (E(u) + H(u)) T(u)^(n-1) (the near-zero polynomials of attack/hall-near-zero-lean-n8-n9/DEFINITIONS.md, checkpoint CP-d68bc3f612310f32): p_8(u) > 0 for every real u in [0, 1/400] and p_9(u) > 0 for every real u in [0, 1/500]; (iii) with Q = (2 - gamma(n)) E^(n-1) - T^(n-1), m = n - 1 - z, W = (n - 1 + u) Q - m E^(n-1), M_z = max(L_8, gamma(8-z) gamma(7)/gamma(7-z)) for n = 8 and M_z = L_9 for n = 9, S = (2 - gamma(n) + M_z (1-u)^n) E^n - (E + H) T^(n-1), and G_{n,z}(u) = z^z Q^(n-1) S - (1-u) E^(n+(n-1)m) W^z: G_{8,z}(u) > 0 for every real u in [1/400, 1/20] and z = 1..6, and G_{9,7}(u) > 0 for every real u in [1/500, 3/100]; (iv) with h(u) = H(u)/E(u), g(h) = (1+h)(1 - h/(n-1))^(n-1) and q(u) = 2 - gamma(n) - (1 - h(u)/(n-1))^(n-1), at (n, s, v) = (8, 1/400, 1/20) and (9, 1/500, 3/100): E(v) > 0, 0 <= h(v) < n - 1, 2 - f(v) - g(h(v)) > gamma(n), E(s) > 0 and q(s) > 1.
- obligation-000014: For every integer n with 11 <= n <= 15, all integers a, b >= 0 with 0 < a + b < n, and every real u <= 1: C(n,a,b) u^2 + M(n,a,b) (1-u)^n - gamma(n) > 0, where gamma(n) = n!/n^n, M(n,a,b) = gamma(n-a) gamma(n-b) / gamma(n-a-b) if a, b >= 1 and M(n,a,b) = kappa(n) = (n-2)! ((n-2)/(n-1)^2)^(n-2) if a = 0 or b = 0, and C(n,a,b) = 7 n (n-a-b)^2 / (16 (a(n-a) + b(n-b))) if a, b >= 1 and C(n,a,b) = (7n/(16(n-1))) (1 + (1 - gamma(n))^2) if a = 0 or b = 0 (the constants of attack/hall-scalar-lean-n11-n15/deterministic/formal-check-1/Definitions.lean, checkpoint CP-eb3a961dbe4535ad).
- obligation-000015: If the Dittert inequality with its equality case holds for every integer n in [5,6], in [7,7], in [8,10] and in [11,15], then it holds for every integer n with 5 <= n <= 15.
- obligation-000016: The reduction to boundary maximizers, the Hall domination theorem, the Gurvits permanent floors, the complementary-minor entropy lemma and the n = 7 finite certificates together imply the Dittert inequality with its equality case for n = 7.
- obligation-000017: The reduction to boundary maximizers, the Hall domination theorem, the Gurvits permanent floors, the maximizer zero pattern, the two-zero permanent floor and the n = 8, 9, 10 finite certificates together imply the Dittert inequality with its equality case for every integer n with 8 <= n <= 10.
- obligation-000018: The reduction to boundary maximizers, the Hall domination theorem, the Gurvits permanent floors and the n = 11..15 certificates together imply the Dittert inequality with its equality case for every integer n with 11 <= n <= 15.

route-000001: 0 of 11 cases accepted; remaining [[5, 15]].

route-000002: 0 of 1 cases accepted; remaining [[7, 7]].

route-000003: 0 of 3 cases accepted; remaining [[8, 10]].

route-000004: 0 of 5 cases accepted; remaining [[11, 15]].

## Investigations

- node-000001 (dittert-lean-5-15): admitted; obligation obligation-000001; account account-000001.
- node-000002 (scalar-cert-11-15): admitted; obligation obligation-000014; account account-000002.
- node-000003 (hall-domination): finished; obligation obligation-000007; account account-000003.
- node-000004 (reduction-to-boundary): finished; obligation obligation-000006; account account-000004.
- node-000005 (gurvits-floors): finished; obligation obligation-000008; account account-000005.
- node-000006 (scalar-cert-8-10): admitted; obligation obligation-000013; account account-000006.
- node-000007 (core-entropy): active; obligation obligation-000009; account account-000007.
- node-000008 (bridge-assembly): admitted; obligation obligation-000015; account account-000008.
- node-000009 (bridge-11-15): admitted; obligation obligation-000018; account account-000009.
- node-000010 (scalar-cert-7): admitted; obligation obligation-000012; account account-000010.
- node-000011 (bridge-7): admitted; obligation obligation-000016; account account-000011.
