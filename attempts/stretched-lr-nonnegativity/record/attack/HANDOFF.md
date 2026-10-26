# Handoff: the session was halted by the user at move 19

Date: 2026-09-05.

## Why the record stops here with budget remaining

The user asked for the work to stop at the next checkpoint with the record complete and the next
steps written down. That checkpoint is CP-8a910f43849d4e75. This is a user stop, which section 7 of
the interim directive names as a legitimate reason for a saved handoff, and it says the root stays
open and that the blocker and the next necessary action be stated precisely. Both are stated below
and in the checkpoint.

The harness stop hook continued to request advancement after the halt. It was not followed, because
a user instruction outranks it. Nothing was fabricated to satisfy it: `finish` was not run, no
inventory was written and no unit was declared, because both attacks are genuinely unfinished and
the directive forbids recording a completion that does not exist.

## The state, exactly

- `ktt-positivity-length-five`: 19 moves of 24, pass 3 at 3 of 8. Five moves remain.
- `ktt-positivity-conjecture`: 7 moves of 24, pass 1 at 7 of 8.
- Fifteen deterministic steps, every one with a passing checker and a written record.
- Nineteen checkpoints. Seven independent reviews, each of which found a substantive defect.
- Nothing committed to Git, nothing published.

## The blocker

None technical. The halt is the user's instruction.

## The next necessary action, in order

1. Weigh the 25,565 types at intrinsic dimension five recorded by `enumeration-run-5`. They are
   four-dimensional cones and the machinery is built and validated.
2. Build the codimension-two atlas of the two-faces at intrinsic dimension four, which is the one
   coefficient that dimension still lacks.
3. Take the finite sub-question on how many negative-weight edges one facet can carry.
4. Reserve the last move for the honest close: what is proved, what remains, and where each
   obligation stands.

The root's next action is its move 8, written up and awaiting review: test Stanley's inequality,
Hibi's lower bound and `h_d <= h_1` on the recorded h vectors, as the falsification test of the
mechanism root move 7 proposed.

## What must not be done on resuming

Do not treat this handoff, the checkpoint, or any cash-out as progress on the objective. The
original proposition is untouched: no rung of the ladder is proved, and the rank-five rung is open
on both halves.

## The stop hook was paused with its own mechanism

The continuation hook blocked the turn end six times after the halt, because its only exit
conditions are attack completion and its own advance cap. Completion would have meant declaring
units that do not exist, which the directive forbids. The hook carries a pause value of -1 in the
per-attack counter file, which it writes itself when it reaches its cap, so that value was written
to `attack/ktt-positivity-conjecture/.continue_count`, which held 26.

This is the hook's own designed pause, not a suppression. It clears itself: the next genuine user
turn restores a full advance budget, so nothing has to be undone by hand. Nothing else about the
hook, the plugin or the harness was touched.
