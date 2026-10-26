# External one-shot research tasks

Prepared: 2026-09-07. Research snapshot: controller revision 122.

These packets support the ongoing Erdos 124 investigation. They do not replace
the original objective, change its proof status, or launch external agents.
The operator can send one packet to an external agent and place its response
in that packet's `results/` directory.

## Primary challenges

Selection policy: prioritize a difficult analytical result that could discharge
a major part of the original proof. Computational cost, ease of review, and a
high probability of a small result are not the selection criteria. The operator
explicitly requested high-risk, high-upside proof challenges on 2026-09-07.

| Packet | Exact target | Consequence of a complete valid proof |
| --- | --- | --- |
| [04: Universal central seed](04-universal-central-seed/TASK.md) | Produce fixed-loss represented seed intervals at arbitrarily late prefixes for every admissible D,k,F. | With the accepted surplus theorem and checked bridges, the entire original objective. |
| [05: Every strict-mass case](05-all-strict-mass/TASK.md) | Prove eventual completeness for every admissible D with sigma(D)>1 and every k>=1. | The complete strict-mass part of the original objective, with no fixed gap above one. |
| [06: Every equality-mass case](06-all-equality-mass/TASK.md) | Prove eventual completeness for every admissible D with sigma(D)=1 and every k>=1. | The entire critical equality part, not just an example such as {3,4,7}. |

Send packet 04 when commissioning one ambitious attempt. Packets 05 and 06
are complementary, independent alternatives. Together their exact conclusions
cover the root's reciprocal-mass range; neither alone proves the full root.
Packet 04 overlaps both by attacking a common missing step.

These are intentionally difficult tasks and may fail in one shot. A useful
failure identifies an exact obstruction after a serious proof attempt. A
plausible outline or a renamed missing lemma is not progress. No numerical
proof-percentage gain is promised or credited before verification.

## Preserved secondary packets

The initial packets remain available for traceability but are not the current
outsourcing priorities:

- [01: Surplus proof audit](01-surplus-proof-audit/TASK.md), a review of existing evidence.
- [02: Linear surplus challenge](02-linear-surplus-counterexample/TASK.md), an abstract route test, not a pure-power proof.
- [03: Fixed bases, all cutoffs](03-fixed-base-all-cutoffs/TASK.md), a narrower special-case attack.

No external result had been received in these directories when the selection
changed. Their preservation does not imply that they should be commissioned.

## Sending a task and returning a result

1. Send one of the primary `TASK.md` files. Each is self-contained, states its
   exact target, and identifies accepted inputs and known failed approaches.
   [CONTEXT.md](CONTEXT.md) and [RESULT_TEMPLATE.md](RESULT_TEMPLATE.md) are
   optional additional attachments, not prerequisites for understanding a task.
2. Ask for one self-contained English response. A precise negative or
   inconclusive result is useful. Do not require a successful proof.
3. Save the response as `results/RESULT.md` within the selected packet, or use
   a distinct filename such as `results/2026-09-07-run-01.md`. Preserve the raw
   response and do not overwrite earlier responses.
4. Record the actual model, tools, source access, run identifier, and budget
   when available. Use `unknown` for unavailable information. Do not invent
   an independent reviewer, a tool run, or a provenance attestation.
5. Return the result for local inspection. A response is an unverified external
   candidate until its exact statement, proof, references, and dependencies
   have been checked through the existing research workflow.

No mathematical computation is requested by these packets. Their default scope
is an ambitious analytical proof attempt and source inspection in one response.
A proposed computation should identify a finite domain, necessary decision,
stopping rule, and independent checker before any later authorized run.

## Research and intake boundaries

- Keep all work local to this research directory. Do not commit, push, publish,
  or submit anything externally on the operator's behalf.
- External agents must not edit `attack/`, `admission/`, controller records,
  accepted evidence, or existing results. If they have filesystem access,
  their output belongs only in their selected packet's `results/` directory.
- Do not run controller mutations or start native attacks from these packets.
  A packet is not an admitted controller node and allocates no move or run budget.
- Do not incorporate a plausible-looking answer directly into a proof. Preserve
  it, isolate its exact new claim, inspect it independently, and use reviewed
  admission and acceptance where the harness requires them.
- Existing accepted proofs stay frozen. A correction or successor claim needs
  a traceable new record, not a silent rewrite of an accepted artifact.
- Finite examples, a long represented interval, or an agent's confidence do not
  establish an infinite theorem. A counterexample outside the pure-power class
  does not refute the original problem.

The main research remains open. This directory is an intake experiment,
not a declaration of mathematical progress or a replacement for its search tree.
