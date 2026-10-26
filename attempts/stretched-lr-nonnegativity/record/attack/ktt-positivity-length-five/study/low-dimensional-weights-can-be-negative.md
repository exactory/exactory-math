# The weight is already negative in dimension two, so the low-dimensional shortcut is unavailable

Date: 2026-09-05. A computation of seconds on toy cones, recorded as accounting rather than as a
run, settling in writing the question amendment 2 of the sixth review required to be settled
before a move was spent.

## The question

Move 11 reduced obligation O-B, the non-full-dimensional five-part hives, to the same problem in
the intrinsic lattice one dimension lower: a hive of intrinsic dimension `d` has edges whose
transverse cones have dimension `d - 1`. So intrinsic dimension three needs two-dimensional
weights and intrinsic dimension four needs three-dimensional ones, and the record already holds
positivity statements at those codimensions with closed formulas, the minima `1/9` at rank four and
`1/264` at codimension three.

The question was whether those statements are about **every** cone of that dimension or only about
cones whose normals lie in the rank-five normal set. If the former, O-B closes at intrinsic
dimensions two, three and four outright through the nonnegative-class lemma, with no enumeration.

## The answer

They are only about cones with normals in that set, and the general statement is false. Under the
standard form, `tools/bvweight.py` gives:

| cone in dimension two, rays | weight |
|---|---|
| `(1,0)`, `(1,1)` | 3/8 |
| `(1,0)`, `(-1,1)` | 1/8 |
| `(1,0)`, `(-2,1)` | 1/20 |
| `(1,0)`, `(-5,1)` | **-19/104** |
| `(1,0)`, `(-20,1)` | **-2279/1604** |
| `(20,1)`, `(-20,1)` | **-2279/802** |

So the Berline-Vergne weight of a two-dimensional cone is negative as soon as the cone is wide
enough, and negativity does not begin at dimension four as the record's earlier reading of the
rank-five families suggested. Thin cones go the other way: `(1,0)`, `(100,1)` has weight
`343401/40004`, above eight.

It is a consequence of the identity the weights satisfy, not merely consistent with it. For a
lattice polygon the local formula read at codimension two says the vertex weights sum to one. The
thin cone with rays `(1,0)` and `(100,1)` has weight `343401/40004`, above eight. So any lattice
triangle carrying that cone at one vertex has its other two vertex weights summing to below minus
seven, and at least one of them is negative. Negativity in dimension two therefore follows from the
identity together with one computed value.

The same identity checks three of the table's entries at once: the unimodular triangle gives
`1/4 + 3/8 + 3/8 = 1`, and the quadrilateral with vertices `(0,0)`, `(1,0)`, `(2,1)`, `(0,1)` gives
`1/4 + 1/8 + 3/8 + 1/4 = 1`.

Two limits on the table as read. "Negative as soon as the cone is wide enough" is six computed
values and not a monotonicity law. And the weight depends on the lattice as well as on the angle,
so the phrase is a description of these examples rather than a criterion.

## What this settles for O-B

The shortcut is unavailable. Positivity at codimension two and three in this project's record is a
statement about the cones spanned by the twenty-seven rank-five rhombus normals, not about all
cones of those dimensions, and the projected lattices of a non-full-dimensional hive produce
normals that are images of those under a projection rather than elements of the set. So **O-B needs
its own atlas at each intrinsic dimension**, exactly as the full-dimensional case did, and the
saving move 11 hoped for is not there.

What move 11 established still stands: the reductions carry over unchanged, the hardest case needs
four-dimensional weights rather than five-dimensional ones, and `tools/bvweight.py` is built and
validated for them, now to dimension six.
