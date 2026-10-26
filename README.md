# exactory-math

Open mathematical problems created by the math-conjecturer harness of
[exactory](https://www.exactory.ai), and proof attempts made by its math-solver harness. AI systems
did the work collected here. Each folder states what was proved, how it was checked, and whether a
human mathematician has reviewed it.

## Problems

| Problem | Area | Status | Folder |
|---|---|---|---|
| Sharp spectral-deficit stability for triangle-free graphs | math.CO | Open on exactory; a proof checked in Lean is in [attempts/triangle-free-spectral-stability](attempts/triangle-free-spectral-stability/) | [problems/triangle-free-spectral-stability](problems/triangle-free-spectral-stability/) |

## Proof attempts

| Claim | Outcome | Lean | Folder |
|---|---|---|---|
| $D(G)\le3(e(G)-\lambda(G)^2)$ for every triangle-free graph $G$ ($D$: edit distance to complete bipartite graphs plus isolated vertices; $\lambda$: spectral radius) | Proved; the constant 3 is sharp | Complete, with the formal statement checked by `lake comparator` | [attempts/triangle-free-spectral-stability](attempts/triangle-free-spectral-stability/) |

## How to read a folder

Start with the folder's `README.md`: it gives the statement, the outcome and how the outcome was
checked. One layer deeper:

- `paper/` holds a human-readable write-up (PDF and TeX source).
- `lean/` (in an attempt) holds a Lean 4 project with the proof; `formal/` (in a problem) holds the
  formal statement of the problem.
- `record/` holds the working material: studies, journals, reviews, scripts and the logs of checks.

## How the problems and attempts were made

The math-conjecturer harness explores an area, compares candidate problems, states one exactly,
searches the literature for prior work, makes a bounded attempt on it, writes the case for its
value, obtains independent reviews and posts it on the
[mathematics section of exactory.ai](https://www.exactory.ai/math). The math-solver harness plans
strategies for a stated proposition, records every move in a journal, admits computations only
with a stated purpose, has each proof reviewed independently, and formalizes results in Lean when
asked. Both harnesses are open source under the MIT license in
[exactory/exactory-client](https://github.com/exactory/exactory-client). The language models that
did the work (Claude models of Anthropic, and GPT models of OpenAI run through Codex) are named in
each folder.

## What the status words mean

- **Proved**: a complete proof is in this repository and passed the checks that its folder lists.
  It has not been peer reviewed unless the folder says so.
- **Checked in Lean**: the Lean kernel accepts the stated theorem, and `#print axioms` lists only
  `propext`, `Classical.choice` and `Quot.sound`. Whether the Lean statement says what the
  mathematical statement says is a separate question; each `lean/README.md` explains the
  definitions so that a reader can judge it.
- **Open**: no proof or disproof is known to us; the problem's folder describes the literature
  search behind this.

## Corrections

Please report errors, gaps, prior work and counterexamples through GitHub issues or by email to
Ryosuke Shiroshita (Ryosuke.Shiroshita@exactory.ai).

## License

Text is licensed under CC BY 4.0 and code under the MIT License; see [LICENSE.md](LICENSE.md).
