# Exploratory checks (no native credit)

Scripts run outside the controller, in the common workspace's Python environment
(`<venv>/bin/python`,
PyNormaliz), as aids to the hand arguments of the moves. Each script has a `.out.txt` file
with the output of its run on 2026-10-20. Nothing here is admitted evidence; the proofs in
`../proofs/` and the notes in `../notes/` stand on their own.

- `seed_check.py`: the equidecomposition of the seed polytope (move 4): Ehrhart
  polynomials of P and Q by Normaliz, and the piece consistency up to dilation 6.
- `zero_parts.py`: Lemma Z of move 3 on three admissible triples at sides 5, 6, 7: the
  dimension, the vertices, the Ehrhart polynomial and the forced interior labels.
- `five_instances.py`: the vertex data of the five size-15 five-part hive polytopes with a
  non-integral vertex (move 5).
