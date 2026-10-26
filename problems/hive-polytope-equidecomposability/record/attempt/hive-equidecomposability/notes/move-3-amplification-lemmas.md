# Move 3: amplification lemmas for equidecomposability of hive polytopes

Entry: seed-and-amplify, action 1 (strategy make-the-proof-constructive). Conventions as in
the seed proof: the hive array of side n has vertices (x, y), x, y >= 0, x + y <= n; the border
labels are h(0, 0) = 0, h(0, y) = lambda_1 + ... + lambda_y (left edge), h(x, 0) = nu_1 + ... +
nu_x (bottom edge), h(x, n - x) = |lambda| + mu_1 + ... + mu_x (right edge); the interior
vertices are those with x, y >= 1 and x + y <= n - 1, D = binom(n-1, 2) of them; H_n(lambda,
mu, nu) in R^D is the set of interior labellings satisfying every rhombus inequality. Say that
a rational polytope P in R^d "has property E" when it is GL_d(Z)-equidecomposable with a
lattice polytope in the sense of the root claim.

## Lemma A (affine relabelling)

Let g be an affine function on the plane of the array, g(x, y) = ax + by + c. For every unit
rhombus with obtuse vertices p_1, p_2 and acute vertices p_3, p_4 one has p_1 + p_2 = p_3 + p_4
as vectors (a rhombus is a parallelogram and the obtuse vertices are opposite), hence
g(p_1) + g(p_2) = g(p_3) + g(p_4). So a labelling h satisfies a rhombus inequality if and only
if h + g does. Proof: immediate from the equality of the g-sums.

## Lemma T (integral translation along two sides)

Let (lambda, mu, nu) be admissible with at most n parts and let k be a nonnegative integer.
Write mu + k = (mu_1 + k, ..., mu_n + k) and nu + k = (nu_1 + k, ..., nu_n + k) (n parts, zero
parts included; both are partitions with at most n parts). Then (lambda, mu + k, nu + k) is
admissible (|lambda| + |mu| + nk = |nu| + nk) and

    H_n(lambda, mu + k, nu + k) = H_n(lambda, mu, nu) + k v,   v = (x)_{(x, y) interior} in Z^D.

Proof. With g(x, y) = kx: the left edge (x = 0) is unchanged; the bottom edge changes by
sum_{i <= x} k = kx = g(x, 0); the right edge changes by |lambda| + sum_{i <= x}(mu_i + k) -
(|lambda| + sum_{i <= x} mu_i) = kx = g(x, n - x). So the border of (lambda, mu + k, nu + k) is
the border of (lambda, mu, nu) plus g, and by Lemma A the map h -> h + g restricted to the
interior coordinates, which is the translation by k v, is a bijection between the two
polytopes. The same argument with g(x, y) = k(x + y) gives H_n(lambda + k, mu, nu + k) =
H_n(lambda, mu, nu) + k v' with v' = (x + y)_{interior} in Z^D. The general admissible form
is (lambda + a, mu + b, nu + (a + b)) with a, b >= 0 (adding a to every part of lambda, b to
every part of mu and a + b to every part of nu; adding a common integer to lambda and mu alone
breaks |lambda| + |mu| = |nu|), which is the composition of the two cases with
g(x, y) = a(x + y) + bx. Consequently property E is invariant under these operations (compose
each U_i with the translation, which is affine unimodular), and
c^{nu + (a+b)}_{lambda + a, mu + b} = c^nu_{lambda mu}.

## Lemma Z (zero parts)

Let (lambda, mu, nu) be admissible with at most n parts, n >= 2, and regard the three
partitions as partitions with at most n + 1 parts (a zero part appended). Let pi be the
projection from the interior coordinates of the side-(n+1) array to those of the side-n array
(forgetting the coordinates of the vertices with x + y = n). Then pi maps H_{n+1}(lambda, mu, nu)
bijectively onto H_n(lambda, mu, nu), and its inverse is h -> (h, s) with the constant integral
vector s given by s_{(x, n-x)} = |lambda| + mu_1 + ... + mu_x (1 <= x <= n - 1). In particular
H_{n+1}(lambda, mu, nu) is the affine unimodular image of H_n(lambda, mu, nu) x {0} and property
E holds for (n + 1, lambda, mu, nu) if and only if it holds for (n, lambda, mu, nu).

Proof. In the side-(n+1) array write R_x = h(x, n + 1 - x) for the right-edge labels
(0 <= x <= n + 1), S_x = h(x, n - x) (0 <= x <= n) and T_x = h(x, n - 1 - x) (0 <= x <= n - 1).
The border gives R_x = |lambda| + mu_1 + ... + mu_x, hence R_x - R_{x+1} = -mu_{x+1} for
0 <= x <= n (with mu_{n+1} = 0); S_0 = h(0, n) = lambda_1 + ... + lambda_n = |lambda| and
S_n = h(n, 0) = nu_1 + ... + nu_n = |nu| = |lambda| + |mu|.

(1) The row S is forced. The rhombus inequality of type (B) at (x, n - x), for 0 <= x <= n - 1
(it needs y = n - x >= 1 and x + y = n <= (n + 1) - 1), reads S_x + R_{x+1} >= R_x + S_{x+1},
that is S_x - S_{x+1} >= -mu_{x+1}. Summing over x = 0, ..., n - 1 gives S_0 - S_n >= -|mu|,
and the left side equals |lambda| - (|lambda| + |mu|) = -|mu|. So every one of the n
inequalities is an equality, S_x - S_{x+1} = -mu_{x+1}, and S_x = S_0 + mu_1 + ... + mu_x = R_x
for 0 <= x <= n. Hence pi is injective on H_{n+1}, with the stated constant values.

(2) The restriction of a side-(n+1) hive to the side-n sub-array (the vertices with x + y <= n)
is a side-n hive: its border is the left edge and the bottom edge of the big array restricted
to y <= n and x <= n, which carry lambda_1 + ... + lambda_y and nu_1 + ... + nu_x, and the row
S, which by (1) carries |lambda| + mu_1 + ... + mu_x, the side-n right-edge labels; and every
rhombus inequality of the side-n array is a rhombus inequality of the side-(n+1) array. So pi
maps H_{n+1} into H_n.

(3) pi is surjective: given a side-n hive h, extend it by S_x = R_x. Every rhombus inequality of
the side-(n+1) array either involves only vertices with x + y <= n, in which case it is a
side-n inequality satisfied by h (with the right-edge values S_x), or it involves a vertex of
the row R or of the row S together with a vertex of sum n + 1 or n; the unit rhombi with a
vertex of sum n + 1 are: type (A) at (x, y) with x + y = n - 1, which reads S_{x+1} + S_x >=
T_x + R_{x+1}, equivalent (as S_{x+1} = R_{x+1}) to S_x >= T_x; type (B) at (x, y) with
x + y = n, which reads S_x + R_{x+1} >= R_x + S_{x+1}, an equality by the choice of S; type (C)
at (x, y) with x + y = n and x >= 1, which reads S_x + R_x >= R_{x+1} + R_{x-1}, equivalent to
mu_x >= mu_{x+1}, true for a partition (R_x - R_{x-1} = mu_x). The rhombi with a vertex of sum n
and none of sum n + 1 are side-n rhombi (type (B) at (x, n - 1 - x) with y >= 1, which reads
T_x + S_{x+1} >= S_x + T_{x+1}, and type (C) at (x, n - 1 - x) with x >= 1, which reads
T_x + S_x >= S_{x+1} + S_{x-1}), satisfied by h. It remains to prove S_x >= T_x for
0 <= x <= n - 1 from the side-n inequalities. For x = 0, T_0 = h(0, n - 1) = |lambda| -
lambda_n <= |lambda| = S_0. For x >= 1, the side-n inequality of type (B) at (x - 1, n - x)
(y = n - x >= 1 and (x - 1) + (n - x) = n - 1) reads T_{x-1} + S_x >= S_{x-1} + T_x, that is
T_x - T_{x-1} <= S_x - S_{x-1} = mu_x; summing from 1 to x gives T_x <= T_0 + mu_1 + ... +
mu_x = |lambda| - lambda_n + mu_1 + ... + mu_x <= S_x. So the extension is a side-(n+1) hive,
and pi is a bijection with inverse h -> (h, s), an affine map with integral translation part.

(4) Property E transfers: if H_n = disjoint union of T_i with U_i(T_i) disjoint and union Q, then
H_{n+1} = disjoint union of T_i x {s} and the maps (x, t) -> (U_i(x), t) (block diagonal, in
GL(Z)) carry them onto Q x {s}, a lattice polytope; conversely pi carries a decomposition of
H_{n+1} to one of H_n after the affine unimodular identification of the n-dimensional... (the
identification of H_{n+1} with H_n x {s} is the affine unimodular map (h, s) -> h on the affine
subspace {t = s}, extended by the identity in the complementary coordinates). This proves the
lemma.

Consequence (reduction). The root statement for the pair (n, lambda, mu, nu) holds if and only
if it holds for (n_0, lambda, mu, nu) with n_0 = max(l(lambda), l(mu), l(nu)) (induct on n with
Lemma Z); in particular the complementary obligation's zero-padded instances of the seed triple
follow from the seed obligation, and for n <= 3 (D <= 1) property E holds for every admissible
triple because the hive polytope is a point or a segment, which by the dimension argument of
move 1 is a lattice segment.

## Lemma P (products)

If P in R^a and P' in R^b have property E, with lattice targets Q and Q', then P x P' in
R^{a+b} has property E with target Q x Q'. Proof: let P = disjoint union of T_i with maps U_i,
P' = disjoint union of T'_j with maps U'_j. Then P x P' is the disjoint union of the relatively
open rational polytopes T_i x T'_j, each of which is a finite disjoint union of relatively open
rational simplices (triangulate the closed product of simplices without new vertices and take
relative interiors of the faces of the triangulation that lie in the relatively open product;
the product of relatively open simplices is the union of the relatively open cells of such a
triangulation that meet it, and those cells are exactly the ones contained in it). The maps
U_i x U'_j are affine unimodular (block diagonal), their images are pairwise disjoint (if
(U_i x U'_j)(T_i x T'_j) met (U_k x U'_l)(T_k x T'_l) then U_i(T_i) would meet U_k(T_k) and
U'_j(T'_j) would meet U'_l(T'_l)), and the union of the images is Q x Q', a convex polytope with
integral vertices.

## The Horn-product obligation (stated, not proved)

Conjecture (polytope-level Horn factorization). Let (lambda, mu, nu) be admissible with at
most n parts, let 1 <= r < n and let I, J, K be r-subsets of [n] with
c^{tau(K)}_{tau(I) tau(J)} = 1 (tau as in Cho-Jung-Moon 2008, Definition 1.2; Ghodsi 2026,
Theorem 12) and sum_{k in K} nu_k = sum_{i in I} lambda_i + sum_{j in J} mu_j. Then
H_n(lambda, mu, nu) is GL_D(Z)-equidecomposable with H_r(lambda_I, mu_J, nu_K) x
H_{n-r}(lambda_{I^c}, mu_{J^c}, nu_{K^c}) (embedded in R^D by an injective affine unimodular
map). What is known: the factorization theorem of King-Tollu-Toumazet 2009 (JCTA 116, Theorem
1.4; restated as Theorem 1.3 of Cho-Jung-Moon 2008 and Theorem 12 of Ghodsi 2026) gives
c^nu_{lambda mu} = c^{nu_K}_{lambda_I mu_J} c^{nu_{K^c}}_{lambda_{I^c} mu_{J^c}} and the
equality of the stretched polynomials, hence Ehrhart equivalence of H_n(lambda, mu, nu) with
the product; by Turner-Wu, Ehrhart equivalence does not imply finite equidecomposability in
general, so the conjecture is strictly more than the theorem. If it holds, then by Lemma P
property E for every admissible triple follows from property E for the primitive triples (no
essential Horn inequality tight under the subset condition), which still form an infinite
family containing non-lattice hive polytopes of dimension 3 at five parts (Ferudun 2026,
Section 2: lambda = (4,3,3,1), mu = (4,2,1,1), nu = (6,5,4,2,2), dim H = 3, all 142 essential
Horn inequalities strict; that example is a lattice simplex in the exploratory check
`zero_parts.py`, so it is not itself a counterexample candidate). This obligation is left open
by the move; it is the amplification lemma whose absence keeps the seed branch at the level of
special cases.
