# Barrier: the leading-order mechanism of the reported counterexample gives no deficit on girth-six patterns

Node `sign-model-barrier` (strategy prove-the-barrier-first, entry axiomatise-the-method-and-build-a-near-miss). This
file is the evidence for the node's obstruction milestone. It excludes one refutation strategy for the premise outside
C_2 of the case-split route, the transfer of the construction of [161] at leading order; it neither proves nor refutes
that premise, and it changes no obligation or route status. A draft was written during the exploration, outside this
attack root (`attempt/drafts/sign-model-obstruction.md`); this version was checked against [161] and completed in the
node's move 1. It answers the non-blocking objections of the admission review (`assignment-admission-barrier-fable-2`):
the full text of [161] is part of the checkpoint evidence; the sign model M_H is defined for arbitrary face sizes
(Section 2); the conditional assumption is named RL(H) (Section 3); and the passage from the construction's density to
its limit, with the normalization E V_q = (E W_q)², is written out (Corollary O′).

[161] denotes "A counterexample to Sidorenko's conjecture" (OpenAI, dated September 23, 2026; openai/math, commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a, `preprints/A-counterexample-to-Sidorenkos-conjecture-September-23-2026/
paper.pdf`). Its extracted text is `studies/sources/openai-161-counterexample.txt` of this attack root; bracketed
numbers below are line numbers of that file. The passages used are transcribed in the appendix of
`study/prove-the-barrier-first.md`. [161] is a reported result; its Lemma 3.1 is proved in its Sections 4 to 7, which
this record has not checked. Nothing below depends on the correctness of [161] beyond the identities quoted.

## 1. The mechanism of [161]

[161] works with the incidence graph H_0 = (I ⊔ J, C) of 22 triples (faces) on 13 points, where E is the set of point
pairs contained in a face and every pair of E lies in exactly two faces (Proposition 2.1 [353]); each such pair spans a
4-cycle of H_0. The kernel K_ξ of [431-443] is the normalized indicator of a rank layer of symmetric matrices over F_q.

Lemma 3.1 [444-455] (the rank-layer limit, proved in [161] only for H_0): for independent uniform symmetric matrices
X_i (i ∈ I), Y_j (j ∈ J), every B ⊆ C and every choice of signs ξ_ij on B,

  E ∏_{(i,j)∈B} K_{ξ_ij}(X_i − Y_j) → E_η ∏_{j∈J} ∏_{e={i,k}⊂j, (i,j),(k,j)∈B} (1 + c_0 η_e ξ_ij ξ_kj)   (3.2)

as q → ∞, with independent uniform signs η_e (e ∈ E), c_0 ∈ {1, −1}, uniformly in B and the signs, and the same with
Y_j − X_i. By (3.4) [456-471] the right side equals the product, over the pairs e ∈ E all four of whose incidences lie
in B, of 1 + (product of their four signs): "every fully active pair tests the parity of its four incidence signs,
contributing 0 or 2".

The construction (Sections 3.2 to 3.5) chooses finite type sets with distributions, a finite coordinate set K and, for
each type pair, a law of an activation set S ⊆ K with signs; the kernel W_q of (3.6) [494-510] has E W_q = 1 for every
q. The proof of Lemma 3.2 [553-559] computes the limit of t_{I,J}(W_q): conditional on the types and on an
independent activation sample at each incidence, the matrix integral factors over the coordinates κ ∈ K, and at each
coordinate Lemma 3.1 applies to the active set B_κ = {incidences whose activation set contains κ} with their signs at
κ. The deficit of [161] then comes from the parity factors of (3.4) through its coefficient expansion and the choices
of Sections 3.3 to 3.5. Proposition 3.5 [834-843] symmetrizes: for V((x, y), (x', y')) = W(x, y') W(x', y),
t(H, V) = t_{I,J}(W) t_{I,J}(W^⊤), an identity that uses only that H is bipartite with parts I and J. Lemma 3.6
passes from a kernel with a strict deficit to a finite simple host.

## 2. The sign model of a general pattern

Let H be a finite bipartite graph with parts I and J and edge set C ⊆ I × J. For B ⊆ C, signs ξ: B → {1, −1} and
c_0 ∈ {1, −1}, define

  M_H(B, ξ) = E_η ∏_{j∈J} ∏_{{i,k}⊆N_B(j), i≠k} (1 + c_0 η_{{i,k}} ξ_ij ξ_kj),

where N_B(j) = {i ∈ I : (i, j) ∈ B} and (η_P) are independent uniform signs indexed by the unordered pairs P of
distinct points. There is one factor for each face j and each pair of points of j that are both active at j, exactly
as on the right side of (3.2). For H = H_0 this is the right side of (3.2).

**Lemma O.** (a) If H has no cycle of length four, then M_H(B, ξ) = 1 for every B ⊆ C, every ξ and every c_0.
(b) If H has a cycle of length four, there are B and ξ with M_H(B, ξ) = 0, and others with M_H(B, ξ) = 2.

*Proof.* (a) A pair P = {i, k} of distinct points occurs in the product once for each face j with i, k ∈ N_B(j) ⊆ N(j).
Two distinct such faces j, j' would make i – j – k – j' – i a cycle of length four. So each η_P occurs in at most one
factor. The factors therefore depend on distinct independent variables, and

  M_H(B, ξ) = ∏_P E(1 + c_0 a_P η_P) = ∏_P (1 + c_0 a_P E η_P) = 1,

where P runs over the pairs that occur, a_P = ξ_ij ξ_kj for the unique face j of P, and E η_P = 0.

(b) Let i – j – k – l – i be a cycle of length four with i, k ∈ I and j, l ∈ J. Take B = {(i, j), (k, j), (i, l),
(k, l)}. Then N_B(j) = N_B(l) = {i, k} and N_B(j') = ∅ for every other face j'. With a = ξ_ij ξ_kj, b = ξ_il ξ_kl
and η = η_{{i,k}},

  M_H(B, ξ) = E(1 + c_0 η a)(1 + c_0 η b) = 1 + c_0 (a + b) E η + c_0² ab E η² = 1 + ab,

which is 0 when the four signs have product −1 and 2 when it is +1. This is Equation (3.4) of [161] for one pair. ∎

The argument of part (a) and the averaged form (3.4) say the same thing. In (3.4) the only nonconstant factors belong
to pairs lying in two faces; part (a) reaches the conclusion directly, because a pair that occurs in a single factor
averages that factor to 1, and in a pattern without 4-cycles every pair occurs in at most one factor. Longer cycles do
not change this: on a cycle of length six or more, each face of the cycle contains two consecutive points of the
cycle, and no pair of points lies in two faces, since that would be a 4-cycle. So the even cycles of length at least
six, present in every girth-six pattern that is not a forest, create no dependence among the factors and no
nonconstant term.

## 3. The consequence for the construction of [161]

**Assumption RL(H) (the rank-layer limit for the pattern H).** There is an integer D_0 such that for every fixed even
D ≥ D_0, as q tends to infinity through odd primes, for independent uniform symmetric D-by-D matrices X_i (i ∈ I) and
Y_j (j ∈ J) over F_q, every B ⊆ C and every choice of signs ξ on B,

  E ∏_{(i,j)∈B} K_{ξ_ij}(X_i − Y_j) = M_H(B, ξ) + o(1),

uniformly over B and ξ, with c_0 = χ((−1)^{D/2}) in M_H, and the same with Y_j − X_i in place of X_i − Y_j. For
H = H_0 this is Lemma 3.1 of [161]. For any other pattern it is an assumption, not a theorem; the statement below is
conditional on it.

**Corollary O′.** Let H be a finite bipartite graph with parts I and J, at least one edge and no cycle of length four,
and assume RL(H). Fix any finite data of the construction of [161, Sections 3.2 to 3.5] for H: finite type sets A and B
with distributions π and ν, a finite coordinate set K, and for every type pair (a, b) a law of an activation set
S ⊆ K with signs (ξ^κ)_{κ∈S} (this covers the dilution and the choices of Sections 3.3 to 3.5). Let W_q be the kernel
(3.6) on X = A × S_D^K and Y = B × S_D^K, and V_q((x, y), (x', y')) = W_q(x, y') W_q(x', y). Then

  lim_{q→∞} t_{I,J}(W_q) = 1,   lim_{q→∞} t_{I,J}(W_q^⊤) = 1,   lim_{q→∞} t(H, V_q) = 1 = (E V_q)^{e(H)}.

*Proof.* Write a vertex of X as (a, x) with x = (x^κ)_{κ∈K}, and similarly for Y. By (3.5) and (3.6),

  t_{I,J}(W_q) = E_{a,b} E_{x,y} ∏_{(i,j)∈C} E_{(S_ij, ξ_ij) | a_i, b_j} ∏_{κ∈S_ij} K_{ξ_ij^κ}(x_i^κ − y_j^κ),

where the types a_i (i ∈ I) and b_j (j ∈ J) are independent with laws π and ν, the matrices are independent uniform,
and for each incidence (i, j) an activation set S_ij with signs is drawn from the law of the type pair (a_i, b_j),
independently over the incidences, as in the proof of [161, Lemma 3.2]. All the probability spaces are finite, so the
expectations may be exchanged, and regrouping the factors by coordinate gives

  t_{I,J}(W_q) = E_{a,b} E_{S,ξ} ∏_{κ∈K} E[ ∏_{(i,j)∈B_κ} K_{ξ_ij^κ}(X_i^κ − Y_j^κ) ],

where B_κ = {(i, j) ∈ C : κ ∈ S_ij}: conditional on the types and activations, the coordinates are independent, and at
each coordinate the matrices X_i^κ, Y_j^κ are independent and uniform. By RL(H), each inner expectation equals
M_H(B_κ, ξ^{(κ)}) + o(1), uniformly. The values M_H(B, ξ) lie in [0, 2^N], where N is the number of pairs of points, and
the outer average is over finitely many configurations of types, activation sets and signs, so the finite product and
the finite average converge:

  lim_{q→∞} t_{I,J}(W_q) = E_{a,b} E_{S,ξ} ∏_{κ∈K} M_H(B_κ, ξ^{(κ)}) = 1,

because every product equals 1 by Lemma O(a); the moment condition (3.7) of [161] is not needed. In t_{I,J}(W_q^⊤)
the vertices of I are sampled from Y and those of J from X, so the same computation runs with the differences
Y_i^κ − X_j^κ, and the second part of RL(H) gives the limit 1.

For the last limit, give each vertex v of H a pair (x_v, y_v) ∈ X × Y. For an edge (i, j) of H,
V_q((x_i, y_i), (x_j, y_j)) = W_q(x_i, y_j) W_q(x_j, y_i). The first factors over all edges use only x_i (i ∈ I) and
y_j (j ∈ J), and the second factors only y_i (i ∈ I) and x_j (j ∈ J); the two groups of variables are independent, so

  t(H, V_q) = E ∏_{(i,j)∈C} W_q(x_i, y_j) · E ∏_{(i,j)∈C} W_q^⊤(y_i, x_j) = t_{I,J}(W_q) t_{I,J}(W_q^⊤),

which is the identity of [161, Proposition 3.5] and uses only that H is bipartite with parts I and J. The kernel V_q is
symmetric, and E V_q = E W_q(x, y') · E W_q(x', y) = 1, since E W_q = 1 for every q ([161], after (3.6)). Hence
t(H, V_q) → 1 = (E V_q)^{e(H)}. ∎

## 4. The barrier, in the form of the entry axiomatise-the-method-and-build-a-near-miss

1. The method's properties. The construction of [161] uses: kernels of the form (3.6); the leading-order limit of their
   densities given, coordinate by coordinate, by the pairwise sign model (3.2); and the parity factors (3.4) of pairs
   lying in two faces as the only source of a nonconstant limiting term.
2. The optimum over the admissible family. For every girth-six pattern H and every finite data, the limit of
   t(H, V_q) equals (E V_q)^{e(H)}: the optimum of the family equals the Sidorenko value, so the family gives no
   deficit at leading order (Corollary O′).
3. The barrier. No choice of finite data in the admissible family produces, at leading order, a counterexample on a
   pattern of girth at least six; in particular none on the girth-six patterns outside C_2 that the premise of the
   route concerns, such as incidence graphs of linear triple systems whose points lie in at least three triples (the
   Heawood graph among them).
4. The property the girth-six patterns lack. A pair of points lying in two faces, that is, a 4-cycle: it is the only
   configuration that makes a sign variable occur twice.
5. Tightness. On every pattern with a 4-cycle the sign model takes the values 0 and 2 (Lemma O(b)), which is the
   property that the choices of [161, Sections 3.3 to 3.5] exploit on H_0.

## 5. Scope and limits

- Leading order only. The barrier concerns the limit q → ∞. It says nothing about the error term at a fixed q, whose
  sign [161] does not control: a deficit that vanishes as q → ∞ is not excluded, and [161]'s method does not produce
  one.
- Conditional on the rank-layer limit. Lemma 3.1 is proved in [161] only for H_0, whose faces are triples. For any other
  pattern the formula with M_H is Assumption RL(H), and Corollary O′ is stated under it. If the true limit for some
  pattern contains terms beyond the pairwise sign model (for instance for faces with more than three active
  incidences), this argument does not cover them.
- Other kernels, other limit regimes and other constructions are not addressed; a construction with parity on larger
  configurations is outside the admissible class.
- The barrier holds for every girth-six pattern, inside C_2 as well as outside; it is recorded on the premise outside
  C_2 because that is the premise the transfer targets, and the premise on C_2 is reduced to Problem 1.5 of Conlon,
  Kim, Lee and Lee by the other node.
