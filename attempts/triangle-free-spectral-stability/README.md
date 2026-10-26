# Sharp spectral-deficit stability for triangle-free graphs: a proof

| | |
|---|---|
| Claim | For every finite simple triangle-free graph $G$, $D(G)\le 3\bigl(e(G)-\lambda(G)^2\bigr)$. |
| Outcome | Proved, with the best possible constant: the five-cycle attains equality. |
| Verification | Lean 4 with Mathlib (theorem and sharpness). `lake comparator --paranoid` accepts the proof against the problem's formal statement in Lean's kernel and five further proof checkers. Independent AI review inside the harness. Numerical check of every step on 2,918 graphs. No human mathematician has reviewed the proof yet. |
| Problem | [Sharp spectral-deficit stability for triangle-free graphs](../../problems/triangle-free-spectral-stability/), posted on [exactory.ai](https://www.exactory.ai/math/5aa390a0-bf63-4326-9b97-b50c46334fd8) on 22 October 2026 |
| Made by | exactory math-solver harness (objective `trianglefree-spectral-edit-three`), 24 and 25 October 2026 |

Here $e(G)$ is the number of edges, $\lambda(G)$ is the spectral radius of the adjacency matrix
($0$ for the graph with no vertices), and

$$D(G)=\min_{A,B\subseteq V(G),\ A\cap B=\varnothing}\bigl|E(G)\mathbin{\triangle}E(K_{A,B})\bigr| ,$$

where $K_{A,B}$ has all edges between $A$ and $B$ and no other edges on $V(G)$, and empty parts
are allowed. So $D(G)$ is the least number of edge insertions and deletions that turn $G$ into a
complete bipartite graph together with isolated vertices. Nosal's inequality
$\lambda(G)^2\le e(G)$ makes the spectral deficit $\xi(G)=e(G)-\lambda(G)^2$ nonnegative.

## Results

**Theorem.** For every finite simple triangle-free graph $G$, $D(G)\le 3\,\xi(G)$. When $G$ has an
edge, the target can be taken as $K_{N(v),N(u)}$ for a suitable edge $uv$.

**Sharpness.** The five-cycle has $e(C_5)=5$, $\lambda(C_5)=2$, $\xi(C_5)=1$ and $D(C_5)=3$, so no
coefficient below $3$ works.

**Consequence.** $\xi(G)=0$ forces $D(G)=0$, so $G$ is a complete bipartite graph with isolated
vertices; this is the equality case of Nosal's inequality.

For bipartite graphs the inequality $D(H)\le 3\,\xi(H)$ is Lemma 4.3 of Li, Liu and Ning,
[arXiv:2609.20225v2](https://arxiv.org/abs/2609.20225v2). The theorem removes the bipartiteness
assumption. The paper is [paper/main.pdf](paper/main.pdf).

## Proof in brief

For an edge $uv$ of a triangle-free graph, $N(u)\cap N(v)=\varnothing$, so $K_{N(v),N(u)}$ is an
admissible target. Its cost is $D_{uv}=m+d(u)d(v)-2(A^3)_{uv}$. Li, Liu and Ning average $D_{uv}$
uniformly over the edges; that average can exceed $3\xi$ for triangle-free graphs. Instead, take a
unit eigenvector $x$ for $\lambda$, choose a vertex $u$ with probability $x_u^2$, and then a
uniformly random neighbour $v$. The expected cost is

$$\sum_u x_u^2\,\overline{D}_u,\qquad \overline{D}_u=2m-Z_u-\frac{2(A^4)_{uu}}{d(u)},$$

where $Z_u$ is the number of edges with both ends outside $N(u)\cup\{u\}$. Two Cauchy–Schwarz
bounds give $\lambda^2=\|Ax\|^2\le\sum_u x_u^2(Ad)_u$ and
$\lambda^2\le\sum_u x_u^2(A^2d)_u/d(u)$, and a counting lemma, which uses triangle-freeness, gives
$(A^2d)_u\le(A^4)_{uu}+d(u)Z_u$. Together with $(Ad)_u=m-Z_u$ they yield
$\sum_u x_u^2\overline{D}_u\le 3m-3\lambda^2$. Some edge therefore has $D_{uv}\le3\xi$.

## What did not work

- **The uniform average over edges** (the device of the bipartite lemma) fails for triangle-free
  graphs. The smallest examples have six vertices; the largest excess there is about $0.0133$, on
  the blow-up $C_5[1,1,2,1,1]$ (one vertex of the five-cycle doubled).
- **Weights proportional to $x_ux_v$** fail on the double star $S(8,7)$: the weighted average of
  $D_{uv}$ is about $15.985$, above $3\xi=24-6\sqrt2\approx15.515$.
- **The earlier route.** The bounded attempt made while the problem was created proved
  $D(G)\le15\,\xi(G)$ by cutting along the signs of a least-eigenvalue eigenvector and applying the
  bipartite lemma, and $\limsup D(G)/\xi(G)\le3$ as $\xi(G)/e(G)\to0$. It did not reach the
  coefficient $3$ uniformly (see the problem's "Where it stands").

## How to check

The Lean project is in [lean/](lean/). With [elan](https://github.com/leanprover/elan) installed:

```sh
cd lean
lake exe cache get          # Mathlib build files
lake build                  # TriangleFreeEdit and TriangleFreeSharpness
lake env lean Audit.lean    # axioms of the three main theorems
lake comparator             # Linux with bubblewrap: judges the proof against Challenge.lean
```

Each `#print axioms` line should list only `propext`, `Classical.choice` and `Quot.sound`, and
`lake comparator` should end with `Your solution is okay!`. [lean/README.md](lean/README.md) says
what the definitions mean and what we ran.

The numerical checks are in [record/scripts/](record/scripts/); see
[record/README.md](record/README.md).

## Contents of this folder

| Path | What it is |
|---|---|
| [paper/](paper/) | The paper: theorem, proof, sharpness, remarks and the Lean statement (`main.pdf`, source `main.tex`) |
| [lean/](lean/) | Lean 4 project: the proof, the five-cycle sharpness, the axiom audit and the comparator configuration |
| [record/](record/) | Scripts of the numerical checks and logs of the checks run for this release |

The full research record of the attempt (search tree, journal, strategy studies and reviews) is
not included yet.
