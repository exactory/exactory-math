# Mathematical search tree

Generated from .search/tree.json; do not edit.

Objective: objective-000001

Let $n\ge 2$ and let $\lambda,\mu,\nu$ be partitions with at most $n$ parts, $|\lambda|+|\mu|=|\nu|$ and Littlewood-Richardson coefficient $c^{\nu}_{\lambda\mu}>0$. Let $H=H(\lambda,\mu,\nu)\subset\mathbb{R}^{D}$, $D=\binom{n-1}{2}$, be the hive polytope of Knutson and Tao: the set of real labellings of the $D$ interior vertices of the triangular hive array of side $n$ whose border labels are $0$ at the apex and the partial sums of $\lambda$, $\mu$ and $\nu$ along the three sides, and which satisfy every rhombus inequality (the sum of the labels at the two obtuse vertices of each unit rhombus is at least the sum at the two acute vertices). $H$ is a rational polytope whose lattice points are the integral hives, so that $\#(tH\cap\mathbb{Z}^{D})=c^{t\nu}_{t\lambda,t\mu}$ for every integer $t\ge 1$.

Statement. For every such triple, $H(\lambda,\mu,\nu)$ is $\mathrm{GL}_{D}(\mathbb{Z})$-equidecomposable with a lattice polytope: there exist finitely many relatively open rational simplices $T_{1},\dots,T_{r}$ with $H=\bigsqcup_{i=1}^{r}T_{i}$ (disjoint union, every face of the decomposition counted once as the relative interior of a simplex of some dimension between $0$ and $\dim H$) and affine unimodular maps $U_{i}(x)=A_{i}x+b_{i}$ with $A_{i}\in\mathrm{GL}_{D}(\mathbb{Z})$ and $b_{i}\in\mathbb{Z}^{D}$, such that the images $U_{1}(T_{1}),\dots,U_{r}(T_{r})$ are pairwise disjoint and $Q=\bigsqcup_{i=1}^{r}U_{i}(T_{i})$ is a lattice polytope, that is, a convex polytope all of whose vertices lie in $\mathbb{Z}^{D}$. In particular $\#(tH\cap\mathbb{Z}^{D})=\#(tQ\cap\mathbb{Z}^{D})$ for every $t\ge 1$, so the stretched Littlewood-Richardson polynomial $c^{t\nu}_{t\lambda,t\mu}$ is the Ehrhart polynomial of the lattice polytope $Q$.

Quantifiers: Universal over every integer n >= 2 and every triple of partitions (lambda, mu, nu) with at most n parts, |lambda|+|mu|=|nu| and c^nu_{lambda mu} > 0; existential, for each such triple, over a finite decomposition of H(lambda, mu, nu) into relatively open rational simplices, affine unimodular maps on the pieces, and a lattice polytope Q equal to the disjoint union of the images.
Assumptions: []
Proof policy: reviewed
Recorded proof status: open
Execution status: paused
Freshness: unchecked by this generated view.

## Residual obligations

- obligation-000001: Let $n\ge 2$ and let $\lambda,\mu,\nu$ be partitions with at most $n$ parts, $|\lambda|+|\mu|=|\nu|$ and Littlewood-Richardson coefficient $c^{\nu}_{\lambda\mu}>0$. Let $H=H(\lambda,\mu,\nu)\subset\mathbb{R}^{D}$, $D=\binom{n-1}{2}$, be the hive polytope of Knutson and Tao: the set of real labellings of the $D$ interior vertices of the triangular hive array of side $n$ whose border labels are $0$ at the apex and the partial sums of $\lambda$, $\mu$ and $\nu$ along the three sides, and which satisfy every rhombus inequality (the sum of the labels at the two obtuse vertices of each unit rhombus is at least the sum at the two acute vertices). $H$ is a rational polytope whose lattice points are the integral hives, so that $\#(tH\cap\mathbb{Z}^{D})=c^{t\nu}_{t\lambda,t\mu}$ for every integer $t\ge 1$.

Statement. For every such triple, $H(\lambda,\mu,\nu)$ is $\mathrm{GL}_{D}(\mathbb{Z})$-equidecomposable with a lattice polytope: there exist finitely many relatively open rational simplices $T_{1},\dots,T_{r}$ with $H=\bigsqcup_{i=1}^{r}T_{i}$ (disjoint union, every face of the decomposition counted once as the relative interior of a simplex of some dimension between $0$ and $\dim H$) and affine unimodular maps $U_{i}(x)=A_{i}x+b_{i}$ with $A_{i}\in\mathrm{GL}_{D}(\mathbb{Z})$ and $b_{i}\in\mathbb{Z}^{D}$, such that the images $U_{1}(T_{1}),\dots,U_{r}(T_{r})$ are pairwise disjoint and $Q=\bigsqcup_{i=1}^{r}U_{i}(T_{i})$ is a lattice polytope, that is, a convex polytope all of whose vertices lie in $\mathbb{Z}^{D}$. In particular $\#(tH\cap\mathbb{Z}^{D})=\#(tQ\cap\mathbb{Z}^{D})$ for every $t\ge 1$, so the stretched Littlewood-Richardson polynomial $c^{t\nu}_{t\lambda,t\mu}$ is the Ehrhart polynomial of the lattice polytope $Q$.
- obligation-000003: For every integer n >= 2 and every triple of partitions (lambda, mu, nu) with at most n parts, |lambda| + |mu| = |nu| and c^nu_{lambda mu} > 0, such that the pair (n, lambda, mu, nu) is not n = 5 and the triple nu = (5,4,3,2,1), lambda = (4,3,2,1), mu = (3,2) (the same triple with n >= 6, that is, with zero parts appended and the hive array of side n, is included here), the hive polytope H(lambda, mu, nu) in R^D, D = binom(n-1, 2), is GL_D(Z)-equidecomposable with a lattice polytope in the sense of the root claim.
- obligation-000004: If the root statement holds for the pair n = 5 and the triple nu = (5,4,3,2,1), lambda = (4,3,2,1), mu = (3,2) and for every other admissible pair (n, lambda, mu, nu), then it holds for every admissible pair: the two premises partition the set of admissible pairs (n, lambda, mu, nu) over which the root claim quantifies.

## Investigations

- node-000001 (hive-equidecomposability): active; obligation obligation-000001; account account-000001.

## Strategy reassessment

Recorded context: f4493c51254e3985fc66ed20163d9d9f0a85570839975591fb32e62701364a34
Reassessment required by recorded evidence: yes
Policy recorded as enabled: yes
Local plan freshness is checked by search strategy-context and at execution.

### assessment-000001

Predecessor: None
Context: [snapshot](.search/blobs/fa69bc3b28d2cc85e348122c742e296319e9e868f3bd7afb47a3cd2bed3a1fe6.json)
Assessment: [record](.search/blobs/31d6fa32a2176c87b90a88d34cdeba746f73248d78b16dcc37561f001ac9b770.json)
Independent review: [record](.search/blobs/ccb7be21e3201c17f5ebdadacfa5499f7e292c9e1f66a6ec7c779997d46e7e4d.json)
What changed: Move 2 (test-strengthenings-by-counterexample under attack-the-negative-side) fired its failure signal. Classified as the record stands, with nothing yet independently verified: (a) a candidate identification of the seed hive polytope for the pair (5, (4,3,2,1), (3,2), (5,4,3,2,1)) as the union of two pyramids over a unit square with apexes (1,1,1) and (1/2,-1/2,1/2), derived by hand from the thirty rhombus inequalities in a move note that this packet does not deliver, so for this assessment it is an unverified candidate foothold; (b) a candidate verification by hand that its Ehrhart polynomial 1 + 2t + (3/2)t^2 + (1/2)t^3 is that of the lattice polytope conv{0, e1, e2, e3, (1,1,1)}, likewise unverified here, so the Ehrhart form N1 at the seed is a candidate instance and not an established fact; (c) no counterexample to N1 or N4 within hand reach. Two inferences in the record are withdrawn by this assessment: the journal wording that N1 is 'as hard as the target' (N1 is a weaker consequence; a verified instance of it decides nothing about the root at that instance, which is all the failure signal records), and the negative-side study's remark that computed monomial positivity excludes a disproof 'through negative monomial coefficients' (monomial positivity is neither N4 nor a necessary condition for lattice realizability; the remark is void and nothing depends on it). The plan of attack-the-negative-side has no further step in this record (no hive construction record for step 2, no guessing principle for step 5); retiring it means stopping this search, not that the negative approach is exhausted. The direction stays undecided. Openness remains unresolved and nothing here claims supported openness or priority. The seed candidate is the input the constructive seed branch needs; every proof it produces is to be bound to a checkpoint, where its text is delivered for independent review, before any acceptance is requested.
Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000004"]

- node-000001 / attack-the-negative-side: retire. Its plan reached its last step in this record: the condition list of move 1 leaves an infinite structured class and no contradiction (its proved parts are dimension at least 2 and a non-integral vertex; rank at least 5 rests on a reported remark of Buch; the exploratory censuses carry no credit), and the strengthening test of move 2 found no counterexample to the weaker consequence N1 within hand reach and ended with its failure signal. No entry of the strategy has a next action the record supports. This is a stop of this search, not a proof that no counterexample exists.
  Next action: None under this strategy; its outputs (the condition list and the seed candidate) are handed to make-the-proof-constructive.
  Evidence: ["journal:move-node-000001-2"]
- node-000001 / make-the-proof-constructive: continue. The seed branch has a concrete candidate to prove or refute: the seed polytope candidate P = conv(S u {(1,1,1), (1/2,-1/2,1/2)}) with S the unit square, the cut along x = z and the shear (x, y, z) -> (x, y + x - z, z), whose union is claimed to be the lattice polytope conv{0, (1,0,1), (1,1,1), (1,0,0), (0,-1,1)}. None of this is verified by the delivered evidence; the identification of the hive from its inequalities, the boundary-compatible refinement into relatively open simplices, the GL_6(Z) extension and the zero-part embedding are pending obligations, to be written as proofs and bound to checkpoints (seed obligation obligation-000002) for independent review before any acceptance is requested. The amplification lemmas the entry seed-and-amplify requires first (affine relabelling; integral translations under (lambda + a, mu + b, nu + (a + b)); appending zero parts with an explicit integral affine inverse and block-diagonal extensions of the piece maps; products) are drafted, unverified, and will be journalled with their proofs; the polytope-level Horn-product lemma is an open obligation, the published factorization theorem giving only the equality of stretched polynomials. The strategy's verdict is unknown (whether the objects are reachable from a seed by an amplifying operation), which the walk may rest on once.
  Next action: Move 3: seed-and-amplify action 1, the amplification lemmas (journal the proofs of the relabelling, translation, zero-part and product lemmas; state the Horn-product obligation exactly), carrying the mode move to construction. Move 4: actions 2 to 4, the seed construction for obligation-000002, written as a complete proof and bound to a proof checkpoint whose packet delivers the text for independent result review; acceptance only on approval. Move 5: action 5, test the limits of the seed class on the other four size-15 five-part candidates of the exploratory scan.
  Evidence: ["journal:move-node-000001-2"]

Continuing order: [{"node_id": "node-000001", "strategy": "make-the-proof-constructive"}]
Considered failures: []

- Hypothesis: The seed pair (5, (4,3,2,1), (3,2), (5,4,3,2,1)) satisfies the root statement: its hive polytope is, up to an integral translation inside its affine 3-plane, P = conv(S u {(1,1,1), (1/2,-1/2,1/2)}); with l = x - z and U(x, y, z) = (x, y + x - z, z), the pieces P n {l >= 0} and P n {l < 0} with the maps (identity, U) give the lattice polytope conv{0, (1,0,1), (1,1,1), (1,0,0), (0,-1,1)}, the pieces refine into relatively open rational simplices compatibly with the cut, and the construction lifts to R^6 by a block-diagonal map in GL_6(Z).
  Success criterion: A complete hand proof bound to a proof checkpoint of obligation-000002 and accepted after an independent result review that inspects the delivered proof text.
  Failure signal: The identification of the hive from its inequalities fails, the union of the two pieces is not convex or has a non-integral vertex, the images overlap, the refinement into simplices is not boundary-compatible, or the lift to R^6 is not unimodular.
- Hypothesis: Property E (finite GL(Z)-equidecomposability with a lattice polytope) of hive polytopes is invariant under (lambda, mu, nu) -> (lambda + a, mu + b, nu + (a + b)) for integers a, b >= 0, under appending a zero part to all three partitions, and under products of polytopes.
  Success criterion: Hand proofs journalled in move 3, each checked against the rhombus inequalities of the side-n and side-(n+1) arrays, with the explicit integral affine inverse of the zero-part projection and the block-diagonal extension of the piece maps.
  Failure signal: A rhombus inequality of the larger array is not implied by those of the smaller one together with the border, or the product of decompositions fails to be a decomposition.

### assessment-000002

Predecessor: assessment-000001
Context: [snapshot](.search/blobs/cf3910a4b80bb59b540669de11100ee94967885796f69d2ec1b2fc5b7a298cbf.json)
Assessment: [record](.search/blobs/6efd16e7646f9f8986714e6447e66580b0856c0fac8c985e50a966635ba98402.json)
Independent review: [record](.search/blobs/1ccbc36ae8abbba0a51aee22c1a1a945f0677829b2862bfa5c7450ecdac980ae.json)
What changed: Format note for the observed review record (the controller validates it mechanically): every finding is a single string, and in particular findings.openness.coverage must be one sentence of text, not an object or a list; findings.openness.evidence is a list of digests. A record with a non-string finding is refused by the controller and the review is lost. Reviewer's question, per the reassessment contract: whether each disposition follows from what changed, whether any failed method is repeated without its obstruction being addressed, and whether the next hypotheses can advance the residual claim. Approval of this record approves those dispositions and hypotheses as a plan; it accepts no proof and closes no obligation, and nothing below is submitted for acceptance (the seed proof will be submitted separately as a proof checkpoint of obligation-000002 with its own result review). This is a bounded planning reassessment after a recorded problem change; approval concerns only the retirement of one recorded search and the continuation of the constructive investigation with explicitly testable hypotheses. It asserts no mathematical result as established: every lemma, identification and construction named below is an unverified candidate until it is bound to a checkpoint whose packet delivers its proof text for independent review, and no acceptance is requested here. Openness remains unresolved and no claim of supported openness or priority is made. What changed: Move 3 (seed-and-amplify, action 1, under make-the-proof-constructive) was journalled with a problem change: the mode moved from undecided to construction, as the branch's first move requires. Its content, recorded in the journal line and in the node note notes/move-3-amplification-lemmas.md (not delivered by this packet, so classified as candidate lemmas pending their own review): hand proofs of four amplification lemmas, namely (A) adding an affine function of the array position to every label preserves every rhombus inequality; (T) the integral translations H_n(lambda + a, mu + b, nu + (a + b)) = H_n(lambda, mu, nu) + a(x + y) + b(x) for integers a, b >= 0; (Z) appending a zero part to all three partitions gives a hive polytope that is the affine unimodular image of the previous one times a point, with the explicit integral affine inverse h -> (h, s) and block-diagonal extensions of the piece maps, so the root statement for a pair (n, lambda, mu, nu) is equivalent to the statement at the largest length; (P) products of polytopes with the property have the property; and the exact statement of the polytope-level Horn-product lemma as an open obligation (the published factorization theorem gives only the equality of stretched polynomials). The move paid the obligations cost (the Horn-product statement is added as a statement still to be proved) and fired no failure signal. Nothing in this move is independently verified; the lemmas are candidates until a checkpoint carries them. Openness remains unresolved; no claim of supported openness or priority is made. The next move is the seed construction (actions 2 to 4), to be bound to a proof checkpoint of obligation-000002 whose packet delivers the proof text.

=== DELIVERED TEXTS FOR INSPECTION (verbatim copies of the node files; candidates, not accepted) ===

--- notes/move-2-ehrhart-form-at-the-seed.md ---

# Move 2: the Ehrhart form N1 tested at the seed instance

Entry: test-strengthenings-by-counterexample (strategy attack-the-negative-side). The
neighbouring statements that would be refuted by a counterexample of type (i) of move 1 are
N1 (some lattice polytope has Ehrhart polynomial c^{t nu}_{t lambda, t mu}) and its
consequence N4 (nonnegative numerator); small instances are computable by hand. This move
tests N1 at the first non-lattice five-part instance of the exploratory scan, by hand.

## 1. The seed instance identified

Pair (n, lambda, mu, nu) = (5, (4,3,2,1), (3,2), (5,4,3,2,1)). Conventions: the hive array
of side 5 has vertices (x, y), x, y >= 0, x + y <= 5; the border labels are h(0, 0) = 0,
h(0, y) = lambda_1 + ... + lambda_y on the left edge, h(x, 0) = nu_1 + ... + nu_x on the
bottom edge and h(x, 5 - x) = |lambda| + mu_1 + ... + mu_x on the right edge:

    h(0,1) = 4, h(0,2) = 7, h(0,3) = 9, h(0,4) = 10, h(0,5) = 10,
    h(1,0) = 5, h(2,0) = 9, h(3,0) = 12, h(4,0) = 14, h(5,0) = 15,
    h(1,4) = 13, h(2,3) = 15, h(3,2) = 15, h(4,1) = 15.

(The other assignment of the two small partitions to the left and right edges gives a hive
polytope that is the image of this one under a coordinate permutation composed with an
integral translation; its derivation from its own rhombus inequalities is Section 8 of
`../proofs/smallest-instance.md`. So the choice of convention does not affect anything below.)

The six interior vertices in the order (1,1), (1,2), (1,3), (2,1), (2,2), (3,1) carry the
coordinates x_1, ..., x_6. The rhombus inequalities in the three orientations are

    (A) h(x+1,y) + h(x,y+1) >= h(x,y) + h(x+1,y+1)      (x, y >= 0, x + y <= 3),
    (B) h(x,y) + h(x+1,y)   >= h(x,y+1) + h(x+1,y-1)    (y >= 1, x + y <= 4),
    (C) h(x,y) + h(x,y+1)   >= h(x+1,y) + h(x-1,y+1)    (x >= 1, x + y <= 4).

Forced coordinates. (B) at (3,1): x_6 + h(4,1) >= h(3,2) + h(4,0), i.e. x_6 >= 14; (C) at
(4,0): h(4,0) + h(4,1) >= h(5,0) + x_6, i.e. x_6 <= 14. So x_6 = 14. (C) at (3,1):
x_6 + h(3,2) >= h(4,1) + x_5, i.e. x_5 <= 14; (B) at (2,2): x_5 + h(3,2) >= h(2,3) + x_6, i.e.
x_5 >= 14. So x_5 = 14. (C) at (3,0): h(3,0) + x_6 >= h(4,0) + x_4, i.e. x_4 <= 12; (B) at
(2,1): x_4 + x_6 >= x_5 + h(3,0), i.e. x_4 >= 12. So x_4 = 12.

The remaining inequalities, after substituting the border and the forced values (the rhombi
giving each are listed; (A) at (2,0), (2,1), (3,0) reduce to the constants 1 >= 0 and (C) at
(2,2) to x_3 <= 14, implied by (B) at (0,4)):

    x_1 <= 9          (A)(0,0), (C)(2,0)
    x_1 >= 8          (B)(0,1), (A)(1,0), (C)(1,0)
    x_3 <= 13         (B)(0,4)
    x_3 >= 12         (A)(0,3), (B)(1,3), (C)(1,3)
    x_2 <= 12         (C)(2,1)
    x_2 - x_1 >= 2    (B)(0,2), (A)(1,1)
    x_2 - x_1 <= 3    (A)(0,1), (B)(1,1)
    x_3 - x_2 >= 1    (B)(0,3), (A)(1,2)
    x_3 - x_2 <= 2    (A)(0,2), (B)(1,2)
    x_1 + x_2 >= 19   (C)(1,1)
    x_2 + x_3 >= 23   (C)(1,2)

With x = x_1 - 8, y = x_2 - 11, z = x_3 - 12 these read x <= 1, x >= 0, z <= 1, z >= 0,
y <= 1, x - 1 <= y <= x, z - 1 <= y <= z, y >= -x, y >= -z, where x >= 0, z >= 0 and y <= 1
follow from the others. Hence, inside the affine 3-plane {x_4 = 12, x_5 = 14, x_6 = 14}
whose lattice points form a copy of Z^3,

    H - (8, 11, 12, 12, 14, 14) = P := {x <= 1, z <= 1, y <= x, y <= z, y >= x-1, y >= z-1, y >= -x, y >= -z}.

P n {y >= 0} = {0 <= y <= min(x, z), x, z <= 1} is the pyramid with apex p = (1, 1, 1) over
the unit square S = [0,1] x {0} x [0,1]; P n {y <= 0} = {max(x-1, z-1, -x, -z) <= y <= 0}
is the pyramid with apex w = (1/2, -1/2, 1/2) over S. So P = conv(S u {p, w}) has the six
vertices (0,0,0), (1,0,0), (0,0,1), (1,0,1), p, w, dim P = 3, and w is half-integral: the
hive polytope is not a lattice polytope (this is the instance's non-integral vertex of
condition C3).

## 2. The Ehrhart polynomial of the seed, by hand

For t >= 1 the lattice points of tP are counted level by level in y. Upper pyramid: at
height y = k (0 <= k <= t) the section is the square [k, t]^2 in (x, z)... more precisely
{(x, z) : k <= x <= t, k <= z <= t}, with (t - k + 1)^2 lattice points; total
sum_{m=1}^{t+1} m^2 = (t+1)(t+2)(2t+3)/6. Lower pyramid, levels y = -j with
1 <= j <= t/2: the section is {j <= x <= t - j, j <= z <= t - j}, with (t - 2j + 1)^2
points. So L_P(1) = 5 + 0 = 5, L_P(2) = 14 + 1 = 15, L_P(3) = 30 + 4 = 34. Since L_P is a
polynomial of degree 3 with L_P(0) = 1 (Ehrhart; the period collapse of hive polytopes is a
theorem, and in this instance it is also visible directly: the count is (t+1)(t+2)(2t+3)/6 +
sum_{1 <= j <= t/2} (t-2j+1)^2 = 1 + 2t + (3/2)t^2 + (1/2)t^3 for t even and for t odd
alike, as one checks from the two closed forms), the four values determine it:

    L_H(t) = c^{t nu}_{t lambda, t mu} = 1 + 2t + (3/2) t^2 + (1/2) t^3,

with h*-vector (1, 1, 1, 0) (from L(1) = 5 = 4 + h*_1, L(2) = 15 = 10 + 4 h*_1 + h*_2,
L(3) = 34 = 20 + 10 h*_1 + 4 h*_2 + h*_3).

## 3. N1 holds at the seed: a lattice polytope with the same Ehrhart polynomial

Let Q' = conv{0, e_1, e_2, e_3, (1,1,1)} in R^3. It is the union of the unimodular simplex
Delta = conv{0, e_1, e_2, e_3} and the tetrahedron T' = conv{e_1, e_2, e_3, (1,1,1)} along the
triangle conv{e_1, e_2, e_3} (the segment from 0 to (1,1,1) crosses that triangle at its
centroid, so the union is convex). The lattice points of tT' are the integer points
(x, y, z) = a e_1 + b e_2 + c e_3 + d (1,1,1) with a, b, c, d >= 0 and a + b + c + d = t,
that is, with s = x + y + z: d = (s - t)/2 >= 0 and x, y, z >= d. Counting:

    t = 1: Delta gives 4, T' beyond the triangle gives (1,1,1) only: L_{Q'}(1) = 5;
    t = 2: 2 Delta gives 10; s = 3: (1,1,1); s = 4: (2,1,1), (1,2,1), (1,1,2); s = 6: (2,2,2);
           L_{Q'}(2) = 10 + 1 + 3 + 1 = 15;
    t = 3: 3 Delta gives 20; s = 4: three points (2,1,1) and permutations; s = 5: six points
           (x, y, z >= 1 summing to 5); s = 6: (2,2,2); s = 7: (3,2,2) and permutations, three
           points; s = 9: (3,3,3); L_{Q'}(3) = 20 + 3 + 6 + 1 + 3 + 1 = 34.

(The points of tT' with s = t lie on the shared triangle and are counted in t Delta.) Hence
L_{Q'} and L_H agree at t = 0, 1, 2, 3 and both are cubic: L_{Q'} = L_H. So the Ehrhart form
N1 holds for the seed instance, with Q' a lattice 3-polytope with five lattice points and
h*-vector (1, 1, 1, 0); the necessary inequalities of move 1 (nonnegativity, the interior
bound h*_3 <= h*_1, Hibi's lower bound, Stanley's inequality, Hibi 1990, the universal
inequality for h*_3 = 0) are all satisfied, as they must be. The seed is therefore not a
counterexample of type (i); whether it is one of type (ii) is decided by the constructive
strategy (move 4).

## 4. Outcome of the test

No counterexample to N1 appears in the range tested by hand (the seed), and N1 is as hard as
the target in general (a lattice-realizable polynomial does not give the geometric
decomposition, by Turner-Wu's examples in dimension 2), so the entry's failure signal fires:
the strengthening is a target, not a test. The record gains the identification of the seed
polytope (used by move 4) and the hand-proved N1 instance.


--- notes/move-3-amplification-lemmas.md ---

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


--- proofs/smallest-instance.md (draft for the move 4 checkpoint) ---

# The seed instance: the hive polytope of (5, (4,3,2,1), (3,2), (5,4,3,2,1)) is equidecomposable with a lattice polytope

Claim (obligation-000002). For n = 5 and the triple nu = (5,4,3,2,1), lambda = (4,3,2,1),
mu = (3,2) (so |lambda| + |mu| = 10 + 5 = 15 = |nu| and c^nu_{lambda mu} = 5), the hive
polytope H = H(lambda, mu, nu) in R^6 is GL_6(Z)-equidecomposable with a lattice polytope: H
is a disjoint union of finitely many relatively open rational simplices T_i, and there are
affine unimodular maps U_i with pairwise disjoint images whose union is a convex polytope
with integral vertices.

## 0. Conventions

The hive array of side 5 has vertices (x, y) with x, y >= 0 and x + y <= 5. The border labels
are h(0, 0) = 0, h(0, y) = lambda_1 + ... + lambda_y on the left edge, h(x, 0) = nu_1 + ... +
nu_x on the bottom edge, and h(x, 5 - x) = |lambda| + mu_1 + ... + mu_x on the right edge:

    h(0,1) = 4, h(0,2) = 7, h(0,3) = 9, h(0,4) = 10, h(0,5) = 10,
    h(1,0) = 5, h(2,0) = 9, h(3,0) = 12, h(4,0) = 14, h(5,0) = 15,
    h(1,4) = 13, h(2,3) = 15, h(3,2) = 15, h(4,1) = 15.

The six interior vertices are ordered (1,1), (1,2), (1,3), (2,1), (2,2), (3,1), with
coordinates x_1 = h(1,1), x_2 = h(1,2), x_3 = h(1,3), x_4 = h(2,1), x_5 = h(2,2),
x_6 = h(3,1). The rhombus inequalities ("the sum of the labels at the two obtuse vertices of
each unit rhombus is at least the sum at the two acute vertices") are, in the three
orientations,

    (A) h(x+1,y) + h(x,y+1) >= h(x,y) + h(x+1,y+1)      (x, y >= 0, x + y <= 3),
    (B) h(x,y) + h(x+1,y)   >= h(x,y+1) + h(x+1,y-1)    (y >= 1, x + y <= 4),
    (C) h(x,y) + h(x,y+1)   >= h(x+1,y) + h(x-1,y+1)    (x >= 1, x + y <= 4).

On the convention. The root statement places the partial sums of lambda, mu and nu on the
three sides without fixing which of the two small partitions is read first; the orientation
of the array is immaterial (a symmetry of the triangle permutes the interior coordinates,
which is a unimodular map). So there are two hive polytopes to consider: the one above, with
lambda = (4,3,2,1) on the left edge and mu = (3,2) on the right edge, and the one with the
two small partitions exchanged. Sections 1 to 7 prove the claim for the first; Section 8
derives the second from its own thirty rhombus inequalities and shows that it is the image of
the first under an explicit coordinate permutation composed with an integral translation, so
the claim holds for both readings.

## 1. The three forced coordinates

(B) at (3,1) reads x_6 + h(4,1) >= h(3,2) + h(4,0), that is x_6 >= 14; (C) at (4,0) reads
h(4,0) + h(4,1) >= h(5,0) + x_6, that is x_6 <= 14. So x_6 = 14. (C) at (3,1) reads
x_6 + h(3,2) >= h(4,1) + x_5, that is x_5 <= 14; (B) at (2,2) reads x_5 + h(3,2) >=
h(2,3) + x_6, that is x_5 >= 14. So x_5 = 14. (C) at (3,0) reads h(3,0) + x_6 >= h(4,0) + x_4,
that is x_4 <= 12; (B) at (2,1) reads x_4 + x_6 >= x_5 + h(3,0), that is x_4 >= 12. So
x_4 = 12. Hence H lies in the affine 3-plane A = {x_4 = 12, x_5 = 14, x_6 = 14}, and
Z^6 n A = {(x_1, x_2, x_3, 12, 14, 14)} is a copy of Z^3 with coordinates (x_1, x_2, x_3).

## 2. The eight facets

The complete list of rhombus inequalities of the side-5 array is the 30 inequalities below
(every (A) with x + y <= 3, every (B) with y >= 1 and x + y <= 4, every (C) with x >= 1 and
x + y <= 4), written with the border labels substituted; the six used in Step 1 are included.
After substituting x_4 = 12, x_5 = 14, x_6 = 14 they become:

    (A)(0,0): 9 - x_1 >= 0            (A)(0,1): x_1 - x_2 + 3 >= 0      (B)(0,1): x_1 - 8 >= 0
    (A)(0,2): x_2 - x_3 + 2 >= 0      (B)(0,2): x_2 - x_1 - 2 >= 0      (A)(0,3): x_3 - 12 >= 0
    (B)(0,3): x_3 - x_2 - 1 >= 0      (B)(0,4): 13 - x_3 >= 0           (A)(1,0): x_1 - 8 >= 0
    (C)(1,0): x_1 - 8 >= 0            (A)(1,1): x_2 - x_1 - 2 >= 0      (B)(1,1): x_1 - x_2 + 3 >= 0
    (C)(1,1): x_1 + x_2 - 19 >= 0     (A)(1,2): x_3 - x_2 - 1 >= 0      (B)(1,2): x_2 - x_3 + 2 >= 0
    (C)(1,2): x_2 + x_3 - 23 >= 0     (B)(1,3): x_3 - 12 >= 0           (C)(1,3): x_3 - 12 >= 0
    (A)(2,0): 1 >= 0                  (C)(2,0): 9 - x_1 >= 0            (A)(2,1): 1 >= 0
    (B)(2,1): 0 >= 0 (used: x_4)      (C)(2,1): 12 - x_2 >= 0           (B)(2,2): 0 >= 0 (used: x_5)
    (C)(2,2): 14 - x_3 >= 0           (A)(3,0): 1 >= 0                  (C)(3,0): 0 >= 0 (used: x_4)
    (B)(3,1): 0 >= 0 (used: x_6)      (C)(3,1): 0 >= 0 (used: x_5)      (C)(4,0): 0 >= 0 (used: x_6)

(For instance (C)(1,1) is h(1,1) + h(1,2) >= h(2,1) + h(0,2), that is x_1 + x_2 >= 12 + 7;
(A)(1,2) is h(2,2) + h(1,3) >= h(1,2) + h(2,3), that is 14 + x_3 >= x_2 + 15.) The
inequality (C)(2,2), x_3 <= 14, is implied by (B)(0,4). Write x = x_1 - 8, y = x_2 - 11,
z = x_3 - 12 (an integral translation of the Z^3 of Step 1). The list becomes

    x <= 1,  x >= 0,  z <= 1,  z >= 0,  y <= 1,  y >= x - 1,  y <= x,  y <= z,  y >= z - 1,
    y >= -x,  y >= -z,

where x >= 0 follows from y >= -x and y <= x, z >= 0 from y >= -z and y <= z, and y <= 1 from
y <= x <= 1. Therefore

    H - (8, 11, 12, 12, 14, 14) = P := {(x, y, z) in R^3 : x <= 1, z <= 1, y <= x, y <= z,
                                         y >= x - 1, y >= z - 1, y >= -x, y >= -z}

inside A (with (x, y, z) the coordinates (x_1, x_2, x_3) of A shifted). The set P is the union
of two pyramids over the unit square S = [0,1] x {0} x [0,1]: P n {y >= 0} = {0 <= y <=
min(x, z), x <= 1, z <= 1} = conv(S u {p}) with p = (1, 1, 1) (a point with y >= 0 satisfies
the eight inequalities exactly when 0 <= y <= min(x, z) and x, z <= 1, and that set is the
pyramid: its sections at height y are the squares [y, 1]^2), and P n {y <= 0} =
{max(x - 1, z - 1, -x, -z) <= y <= 0} = conv(S u {w}) with w = (1/2, -1/2, 1/2) (its sections
at height y = -s, 0 <= s <= 1/2, are the squares [s, 1 - s]^2, which shrink linearly to the
point (1/2, 1/2) at s = 1/2). The union of the two pyramids is convex because the segment from
p to w meets S at (2/3, 0, 2/3), in the relative interior of S. So P is a convex polytope
with vertices (0,0,0), (1,0,0), (0,0,1), (1,0,1), p and w, five of them integral and one
half-integral; dim P = 3; H is not a lattice polytope; and #(P n Z^3) = 5 =
c^nu_{lambda mu} (the five integral vertices: at y = 0 the lattice points of S are its
corners, at y = 1 only p, and no lattice point has y < 0 since y >= -1/2).

## 3. The cut and the shear

Let l(x, y, z) = x - z, a primitive integral linear form, and Pi = {l = 0}. Set

    P_+ = P n {l >= 0},   P_- = P n {l <= 0},   K = P n Pi,

and let U : R^3 -> R^3, U(x, y, z) = (x, y + x - z, z). U is linear with matrix
[[1, 0, 0], [1, 1, -1], [0, 0, 1]] of determinant 1 and integral inverse
U^{-1}(x, y, z) = (x, y - x + z, z), so U is in GL_3(Z); it fixes Pi pointwise and preserves
x and z, hence preserves l.

On P_- (where x <= z) the inequalities y <= z, y >= x - 1 and y >= -z follow from y <= x,
y >= z - 1 and y >= -x respectively, and x <= 1 follows from x <= z <= 1; so

    P_- = {x <= z <= 1,  -x <= y <= x,  y >= z - 1}.

With (x', y', z') = U(x, y, z), that is x' = x, z' = z, y = y' - x' + z', this becomes

    U(P_-) = {x' <= z' <= 1,  y' >= -z',  y' >= x' - 1,  y' <= 2x' - z'}.

(The inequality -x <= y gives y' - x' + z' >= -x', that is y' >= -z'; y <= x gives
y' <= 2x' - z'; y >= z - 1 gives y' >= x' - 1.) Similarly, on P_+ (where x >= z) the binding
inequalities are z <= x <= 1, -z <= y <= z and y >= x - 1:

    P_+ = {z <= x <= 1,  -z <= y <= z,  y >= x - 1}.

Define

    Q = {(x, y, z) in R^3 : x <= 1,  z <= 1,  y >= -z,  y >= x - 1,  y <= z,  y <= 2x - z}.

On {x >= z}, 2x - z >= z, so y <= 2x - z is implied by y <= z, and Q n {l >= 0} = P_+. On
{x < z}, 2x - z < z, so y <= z is implied by y <= 2x - z, and Q n {l < 0} = U(P_-) n {l < 0}
= U(P_- \ K) (U preserves l). Hence

    Q = P_+ u U(P_- \ K)   and   P = P_+ u (P_- \ K),   both disjoint unions.

## 4. Q is a lattice polytope

Q is bounded: y <= z and y >= -z give z >= 0; y <= 2x - z and y >= x - 1 give x >= z - 1 >=
-1; with x <= 1 and z <= 1 this gives -1 <= x <= 1, 0 <= z <= 1 and -1 <= y <= 1. Its
vertices are the points of Q where three of the six bounding planes meet with linearly
independent normals; checking the twenty triples: (0, 0, 0) (y = -z, y = z, y = 2x - z);
(1, 0, 0) (x = 1, y = -z, y = z); (1, 0, 1) (x = 1, z = 1, y = x - 1); (1, 1, 1) (x = 1,
z = 1, y = z, also y = 2x - z); (0, -1, 1) (z = 1, y = -z, y = x - 1, also y = 2x - z); the
remaining triples meet outside Q or in these points (for instance y = z, y = 2x - z and
y = x - 1 force z = x and x - 1 = x). So Q = conv{(0,0,0), (1,0,0), (1,0,1), (1,1,1),
(0,-1,1)} has five vertices, all in Z^3: Q is a lattice polytope. (The point w =
(1/2, -1/2, 1/2) is the midpoint of (1, 0, 0) and U(0, 0, 1) = (0, -1, 1), which is why it is
no longer a vertex.)

## 5. The decomposition into relatively open rational simplices

Triangulate P by a triangulation with rational vertices that refines the cut by Pi: for
instance, triangulate the quadrilateral K = conv{(0,0,0), (1,0,1), p, w} (all four points lie
on Pi; K is a convex quadrilateral in that plane) into the two triangles conv{0, (1,0,1), p}
and conv{0, (1,0,1), w}, then cone each of the two triangles from the apex (1, 0, 0) and
from the apex (0, 0, 1): this gives four closed tetrahedra with rational vertices,
conv{0, (1,0,1), p, a}, conv{0, (1,0,1), w, a} for a = (1,0,0) and for a = (0,0,1), whose
union is P (P_+ is the pyramid conv(K u {(1,0,0)}) and P_- the pyramid conv(K u {(0,0,1)}),
since P_+ = {z <= x <= 1, ...} is the convex hull of K and (1,0,0): every vertex of P with
x >= z is a vertex of K or (1,0,0), and similarly for P_-) and which meet along common faces
(the two tetrahedra over the same triangle of K meet exactly in that triangle, and the two
tetrahedra over the same apex meet in the triangle conv{0, (1,0,1), a}). The relatively open
faces of all dimensions (0 to 3) of these four tetrahedra, each counted once, partition P
into relatively open rational simplices T_1, ..., T_r. Put U_i = identity when T_i lies in
P_+ (every face of the two tetrahedra with apex (1,0,0), including the faces in K) and
U_i = U when T_i lies in P_- \ K (the faces of the two tetrahedra with apex (0,0,1) that are
not contained in Pi). The images are pairwise disjoint: U preserves l, so the images of the
second kind lie in {l < 0} and those of the first kind in {l >= 0}, and within each kind the
pieces are disjoint because U is injective and the T_i are disjoint. Their union is
P_+ u U(P_- \ K) = Q.

## 6. Back in R^6

Compose with the integral translation by c = (8, 11, 12, 12, 14, 14) and extend U to R^6 by
the identity on the coordinates x_4, x_5, x_6: the map V(x_1, ..., x_6) = (x_1, x_2 + x_1 -
x_3, x_3, x_4, x_5, x_6) has an integral matrix of determinant 1, so V is in GL_6(Z), and it
preserves the affine 3-plane A. The pieces T_i + c (T_i placed in A through (x, y, z) ->
(x + 8, y + 11, z + 12, 12, 14, 14)) are relatively open rational simplices with disjoint
union H; the maps are x -> x (for the first kind) and x -> V(x - c) + c (for the second kind),
affine unimodular; and the union of the images is Q + c = conv{(8,11,12,12,14,14),
(9,11,12,12,14,14), (9,11,13,12,14,14), (9,12,13,12,14,14), (8,10,13,12,14,14)}, a convex
polytope with integral vertices. This proves the claim.

## 7. Consequence

Since every map is affine unimodular and the construction is compatible with dilation (U is
linear and the pieces of tP are the dilates of the pieces of P, as the defining inequalities
of P_+, P_- and Q are homogeneous), #(tH n Z^6) = #(t(Q + c) n Z^6) for every t >= 1: the
stretched polynomial c^{t nu}_{t lambda, t mu} = 1 + 2t + (3/2)t^2 + (1/2)t^3 (note of move
2, section 2) is the Ehrhart polynomial of a lattice 3-polytope with h*-vector (1, 1, 1, 0).

Exploratory check (no native credit): `../checks/seed_check.py` recomputes with Normaliz the
Ehrhart polynomials of P and Q (both 1 + 2t + (3/2)t^2 + (1/2)t^3) and verifies for
t = 1, ..., 6 that every lattice point of tQ with x >= z lies in tP and every lattice point of
tQ with x < z is the U-image of a lattice point of tP with x < z.

## 8. The other reading of the convention

Now put mu = (3,2) on the left edge and lambda = (4,3,2,1) on the right edge (nu stays on the
bottom edge). The border labels are

    h(0,1) = 3, h(0,2) = 5, h(0,3) = 5, h(0,4) = 5, h(0,5) = 5,
    h(1,0) = 5, h(2,0) = 9, h(3,0) = 12, h(4,0) = 14, h(5,0) = 15,
    h(1,4) = 9, h(2,3) = 12, h(3,2) = 14, h(4,1) = 15,

(the right edge carries |mu| + lambda_1 + ... + lambda_x = 5 + (4, 7, 9, 10, 10)), and the
thirty rhombus inequalities, with the same coordinates x_1, ..., x_6 for the interior
vertices (1,1), (1,2), (1,3), (2,1), (2,2), (3,1), are

    (A)(0,0): 8 - x_1 >= 0            (A)(0,1): x_1 - x_2 + 2 >= 0      (B)(0,1): x_1 - 7 >= 0
    (A)(0,2): x_2 - x_3 >= 0          (B)(0,2): x_2 - x_1 >= 0          (A)(0,3): x_3 - 9 >= 0
    (B)(0,3): x_3 - x_2 >= 0          (B)(0,4): 9 - x_3 >= 0            (A)(1,0): x_1 - x_4 + 4 >= 0
    (C)(1,0): x_1 - 7 >= 0            (A)(1,1): x_2 - x_1 + x_4 - x_5 >= 0
    (B)(1,1): x_1 - x_2 + x_4 - 9 >= 0                                  (C)(1,1): x_1 + x_2 - x_4 - 5 >= 0
    (A)(1,2): x_3 - x_2 + x_5 - 12 >= 0                                 (B)(1,2): x_2 - x_3 - x_4 + x_5 >= 0
    (C)(1,2): x_2 + x_3 - x_5 - 5 >= 0                                  (B)(1,3): x_3 - x_5 + 3 >= 0
    (C)(1,3): x_3 - 8 >= 0            (A)(2,0): x_4 - x_6 + 3 >= 0      (C)(2,0): x_4 - x_1 - 3 >= 0
    (A)(2,1): x_5 + x_6 - x_4 - 14 >= 0                                 (B)(2,1): x_4 - x_5 + x_6 - 12 >= 0
    (C)(2,1): x_4 + x_5 - x_2 - x_6 >= 0                                (B)(2,2): x_5 - x_6 + 2 >= 0
    (C)(2,2): x_5 - x_3 - 2 >= 0      (A)(3,0): x_6 - 13 >= 0           (C)(3,0): x_6 - x_4 - 2 >= 0
    (B)(3,1): x_6 - 13 >= 0           (C)(3,1): x_6 - x_5 - 1 >= 0      (C)(4,0): 14 - x_6 >= 0

Forced coordinates. (A)(0,2) and (B)(0,3) give x_2 = x_3; (A)(0,3) and (B)(0,4) give x_3 = 9;
so x_2 = x_3 = 9. (C)(2,2) gives x_5 >= 11, (B)(1,3) gives x_5 <= 12 and (A)(1,2) gives
x_5 >= 12; so x_5 = 12. The remaining inequalities, after substituting x_2 = x_3 = 9 and
x_5 = 12 ((C)(1,2) becomes 1 >= 0 and (C)(1,3) becomes 1 >= 0), are

    7 <= x_1 <= 8                     (B)(0,1), (C)(1,0), (A)(0,1); (A)(0,0)
    x_1 + 3 <= x_4 <= x_1 + 4         (A)(1,1), (C)(2,0); (A)(1,0), (C)(1,1)
    x_1 + x_4 >= 18                   (B)(1,1)
    x_4 <= 12                         (B)(1,2)
    x_4 + 2 <= x_6 <= x_4 + 3         (A)(2,1), (C)(3,0); (A)(2,0), (C)(2,1)
    x_4 + x_6 >= 24                   (B)(2,1)
    13 <= x_6 <= 14                   (A)(3,0), (B)(3,1), (C)(3,1); (B)(2,2), (C)(4,0)

With x = x_1 - 7, y = x_4 - 11, z = x_6 - 13 these read x <= 1, x >= 0, y <= x, y >= x - 1,
y >= -x, y <= 1, y <= z, y >= z - 1, y >= -z, z <= 1, z >= 0: the same system as in Section
2, so this hive polytope is P + (7, 9, 9, 11, 12, 13) in the coordinates (x_1, x_4, x_6),
inside the affine 3-plane {x_2 = 9, x_3 = 9, x_5 = 12}. The map

    Phi(v_1, v_2, v_3, v_4, v_5, v_6) = (v_1 - 1, v_4 - 3, v_5 - 5, v_2, v_6 - 2, v_3 + 1)

is a permutation of the coordinates followed by an integral translation, hence affine
unimodular, and it carries the point (8 + x, 11 + y, 12 + z, 12, 14, 14) of the first
polytope to the point (7 + x, 9, 9, 11 + y, 12, 13 + z) of the second. So the second hive
polytope is Phi(H), and composing the pieces and maps of Sections 5 and 6 with Phi (pieces
Phi(T_i + c), maps Phi o U_i o Phi^{-1}) proves the claim for the other reading of the
convention as well.

Remaining obligations: ["obligation-000001", "obligation-000002", "obligation-000003", "obligation-000004"]

- node-000001 / attack-the-negative-side: retire. Unchanged from assessment-000001: its plan reached its last step in this record (no hive construction record for step 2, no guessing principle for step 5), and move 2 ended with its failure signal; retiring it stops this search without claiming that the negative approach is exhausted. Move 3 adds nothing that reopens it: the amplification lemmas, if they hold, only transfer the property between triples and produce no counterexample candidate.
  Next action: None under this strategy.
  Evidence: ["journal:move-node-000001-2", "journal:move-node-000001-3"]
- node-000001 / make-the-proof-constructive: continue. Continuation is proposed on the strength of concrete, falsifiable candidates, none of them verified: The strategy has started (move 3) and its seed branch has both the candidate lemmas of action 1 and the candidate seed construction identified in move 2. The mode is now construction, so the walk is committed to producing the explicit object; the next move is the one that writes the seed construction out as a complete proof (identification of the hive from its thirty rhombus inequalities, the cut, the shear, the inequality description of the union, its five integral vertices, the boundary-compatible refinement into relatively open rational simplices, the disjointness of the images, the GL_6(Z) lift, and the other reading of the border convention) and binds it to a proof checkpoint of obligation-000002 for independent review; acceptance only on approval. The exploratory check checks/cut_shear_apply.py (no credit) suggests that the same cut-and-shear mechanism, with one or two steps, also handles the other four size-15 five-part candidates of the exploratory scan, which gives action 5 (test the limits of the seed class) a concrete content: a general cut-and-shear lemma to prove and apply. The strategy's verdict is unknown (whether the objects are reachable from a seed by an amplifying operation), which the walk rests on once.
  Next action: Move 4: seed-and-amplify actions 2 to 4, the complete proof proofs/smallest-instance.md for obligation-000002, journalled and bound to a proof checkpoint with its independent result review. Move 5: action 5, the general cut-and-shear lemma (a lattice hyperplane through a half-integral vertex and all other vertices except one lattice vertex at lattice distance 1 on each side, or several on one side; the shear fixing the hyperplane that sends the far vertex to the reflection of the near one through the half-integral vertex), proved by hand, and its application to the other four size-15 candidates as evidence of the seed class, with the first candidate it does not reach named if any.
  Evidence: ["journal:move-node-000001-2", "journal:move-node-000001-3"]

Continuing order: [{"node_id": "node-000001", "strategy": "make-the-proof-constructive"}]
Considered failures: []

- Hypothesis: The seed pair (5, (4,3,2,1), (3,2), (5,4,3,2,1)) satisfies the root statement by the cut along x = z and the shear (x, y, z) -> (x, y + x - z, z) of the identified polytope P = conv(S u {(1,1,1), (1/2,-1/2,1/2)}), the union being the lattice polytope conv{0, (1,0,1), (1,1,1), (1,0,0), (0,-1,1)}, with a boundary-compatible refinement into relatively open rational simplices and a block-diagonal lift to GL_6(Z).
  Success criterion: The complete proof is bound to a proof checkpoint of obligation-000002 and accepted after an independent result review that inspects the delivered text.
  Failure signal: The identification from the inequalities fails, the union is not convex or has a non-integral vertex, the images overlap, the refinement is not boundary-compatible, or the lift is not unimodular.
- Hypothesis: General cut-and-shear lemma: if a rational polytope P has a lattice hyperplane {l = c} (l primitive integral, c an integer) containing every vertex except one lattice vertex a with l(a) = c + 1 and lattice vertices b_1, ..., b_m with l(b_i) = c - 1, if K = P n {l = c} has exactly one non-lattice vertex w, half-integral, and if every midpoint (a + b_i + 2w - a - b_1)/2 lies in K, then with d = a + b_1 - 2w and U(x) = x + (l(x) - c) d the union of P n {l >= c} and U(P n {l < c}) is the lattice polytope conv(K u {a} u {b_i - d}), so P has the property; applied to the four other size-15 five-part candidates (one of them in two steps), the lemma yields explicit lattice targets.
  Success criterion: The lemma proved by hand in the move 5 note, with the convexity, disjointness and integrality arguments; the applications recorded with their explicit data as candidates (no credit for the exploratory computation).
  Failure signal: The union fails to be convex for some admissible configuration (a midpoint outside K), or a non-lattice vertex of K other than w survives, or one of the four candidates does not fit the lemma even after two steps.
