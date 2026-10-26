# Independent analytical result review: reciprocal-core lemma

Mathematical verdict: APPROVE. Overall result-review verdict: APPROVE. All four required metadata hashes were independently recomputed and match the prescribed digests. No blocking defect remains. The public acceptance spec is recorded in `admission/core-accept.json`; no controller acceptance command was executed.

## Reviewer and independence

Reviewer source: `host`.
Actual host agent name: `/root`.
Actual thread/session ID, read from `CODEX_THREAD_ID`: `01a07a2e-180f-7731-a0f5-5ba666a51bd9`.

The prescribed proposal records author actor ID `codex-root-01a07806` and author attestation ID `session-01a07806-b2c5-7163-86d2-92fd0ef5cf33`. Both differ from this reviewer's identity. This reviewer did not author the proof and assessed it in fresh context. Identity strings document the host provenance supplied here; they are not cryptographic authentication of intellectual independence.

## Materials and binding status

I read the Exactory Codex README and the SEARCH.md sections `Checkpoints and accepted results` and `Immutable evidence manifests`, together with the relevant canonical-JSON and provenance rules. I read these prescribed research materials in full:

- `attack/checkpoints/core-001-checkpoint.json`.
- `attack/checkpoints/core-001-manifest.json`.
- `attack/erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md`.
- `attack/erdos-124-reciprocal-core/units/consolidation.md`.
- `admission/core-proposal.json`, used only to identify the exact admitted claim, proof policy, and author provenance.

The target is stored checkpoint `checkpoint-000008`, associated in the review request with obligation `obligation-000004`. The expected digests supplied by the request are:

| Object | Expected SHA256 | Independently recomputed |
| --- | --- | --- |
| Complete stored checkpoint, including `id` | `fb793a11c2358e67bf00818cc8668d96e2c282a4e3effd6fe156ebdaaa7a1765` | Yes, exact match |
| Entire admitted claim object | `2f973f00bcb43be598ac9390a6aa290b94b2104ebe8327fc4d9d135773228eec` | Yes, exact match |
| Canonical manifest | `3e7c431c41912315994774e1ac3338ce3f47919d6677ff4394db38a9a9c40882` | Yes, exact match |
| Raw proof bytes | `f2e3fd8517cda7ce584a9f4d297bf9038fbc59f423c2058c9c4d03d0253acbdd` | Yes, exact match |

On direct inspection, the checkpoint and proposal state the same claim, quantifiers, empty assumption IDs, named scope, and `reviewed` policy. The manifest declares analytical evidence, that claim digest, proof outcome, empty acceptance dependencies and route bindings, one proof artifact with the supplied raw digest, no manifest or external dependencies, and null verification. The checkpoint's evidence list contains the supplied manifest digest. The independent hash confirmations above establish the requested artifact bindings in addition to these metadata comparisons.

The initial attempts were rejected by the Exactory PreToolUse hook with: "Unsupported managed shell operation; use a direct supported command or controller search run". On the user's follow-up, all four prescribed direct commands below succeeded with exit code 0 from `<workspace>/erdos-124`. The outputs exactly match the table. No hook was changed or bypassed, and no mathematical run was invoked. This resolves the initial operational blocker.

```sh
shasum -a 256 attack/erdos-124-reciprocal-core/moves/001-minimum-preserving-core.md
python3 -c 'import hashlib,json,pathlib; p=pathlib.Path("attack/checkpoints/core-001-manifest.json"); print(hashlib.sha256(json.dumps(json.loads(p.read_text()),sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest())'
python3 -c 'import hashlib,json,pathlib; p=pathlib.Path("attack/checkpoints/core-001-checkpoint.json"); print(hashlib.sha256(json.dumps(json.loads(p.read_text()),sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest())'
python3 -c 'import hashlib,json,pathlib; p=pathlib.Path("admission/core-proposal.json"); print(hashlib.sha256(json.dumps(json.loads(p.read_text())["proposal"]["claim"],sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest())'
```

JSON hashes use sorted keys, compact separators, preserved Unicode, and UTF-8 encoding. The checkpoint hash includes its stored `id` and immutable `pending` status. The claim hash covers the entire admitted claim object, including quantifiers, assumptions, proof policy, and scope. The raw proof hash confirms that the proof reviewed above is the prescribed artifact.

## Exact statement and quantifiers

For every nonempty finite set D of distinct integers at least 3, set m=min D and sigma(A)=sum over a in A of 1/(a-1). Assuming gcd(D)=1 and sigma(D)>=1, there exists E subset D with m in E, gcd(E)=1, and 1<=sigma(E)<1+1/m.

The proof treats an arbitrary such D. No bound on its size, maximum, prime factors, or pairwise gcds is imposed. The selected E may depend on D. Since m belongs to E and E is a subset of D, min E=m automatically. The empty assumption-ID list does not erase the explicit hypotheses within the statement. The proof uses exactly those hypotheses.

## Gcd descent and seed size

Starting with B={m}, let g=gcd(B). When g>1, some d in D is not divisible by g: otherwise g would be a common divisor of D, contradicting gcd(D)=1. That d is outside B because g divides every current member of B. In particular d>m. Adjoining it replaces g by gcd(g,d), a positive proper divisor of g. Thus descent is strict, and it cannot stop above one. Termination follows from descent in the positive integers; it is also consistent with the finite supply of distinct members of D.

Let q be the number of additions. Since m>=3, q>=1. After the first addition, g1 is a proper divisor of m, so m=a*g1 for an integer a>=2, giving g1<=floor(m/2). From g1 to 1 there can be at most g1-1 further strict integer decreases. Thus q<=1+(g1-1)=g1<=floor(m/2). This bound counts additions correctly even if the first addition already reaches gcd one.

It follows that |B|=q+1<=floor(m/2)+1<=m-1. At m=3 the final inequality is equality; for m>=4, floor(m/2)+1<=m/2+1<=m-1. This argument requires no coprime pair or factorization theorem.

## Strict seed mass and small minima

Every seed member contributes at most 1/(m-1). At least one member is greater than m, so at least one of those inequalities is strict. Hence sigma(B)<|B|/(m-1)<=1. The strictness does not rely on rounding or a numerical approximation.

For m=3, the first proper divisor gcd must be 1, so q=1 and B has two members. Its mass is at most 1/2+1/3=5/6<1. For m=4, g1 is 1 or 2 and q<=2. If q=1, the seed mass is at most 1/3+1/4<1. If q=2, its two distinct members above 4 are at least 5 and 6 after ordering, and its mass is at most 1/3+1/4+1/5=47/60<1. These are symbolic case checks, not enumeration or program output. The general strict termwise argument already covers both minima, including the potentially tight cardinality bound.

The m>=3 assumption is substantive. The consolidation's excluded-boundary example D={2,3} is correct: the only gcd-one subset containing 2 is D itself, with mass 3/2, equal to the prohibited upper endpoint 1+1/2. This does not restrict the admitted domain any further.

## First crossing and completion

Begin with the constructed gcd-one seed of mass below one, and adjoin unused members of D. Positive reciprocal weights and finiteness imply that the full resulting sequence reaches mass sigma(D)>=1. Therefore a first crossing exists, even when sigma(D)=1 exactly. In particular the seed cannot already be all of D under the mass hypothesis.

If d is the last added member, the previous mass is strictly below one. Since m was already present and all elements are distinct integers, d>=m+1. Therefore the final mass is at least one and strictly below 1+1/(d-1)<=1+1/m. Equality d=m+1 causes no problem: the strict inequality comes from the previous mass. Adjoining elements preserves gcd one, containment in D, and the presence of m. This proves every requested property of E.

The optional pruning is harmless. It deletes only members other than m when both gcd one and mass at least one survive. Mass decreases, so the strict upper endpoint survives, and finiteness guarantees termination. Its inclusion-minimality claim is also justified: if a proper feasible subset remained, deleting any one element outside that subset would preserve gcd one and mass at least one. No minimum-cardinality assertion follows or is needed.

## Dependencies, policy, and scope

The proof is complete using elementary facts about finite sets, positive rational sums, divisibility, and gcd. No missing theorem, unproved seed assertion, numerical search, eventual-coverage assertion, or external mathematical dependency is needed. The consolidation is explanatory and is not necessary to complete the proof artifact. The manifest's empty dependencies and route bindings are appropriate for this direct auxiliary proof.

The applicable standard is analytical reviewed proof. No mathematical program, finite search, compiler, certificate checker, or Lean kernel was run. The successful metadata commands confirm artifact identity only; they provide no computational or formal certification of the mathematics.

This proves only the finite-set core lemma. It proves no eventual power representation, no initial represented interval, and no extension bound. Neither the restricted-coverage obligation nor the implication bridge is discharged. The original all-D, all-positive-cutoff objective remains outside this result review. A local review document is not a controller acceptance, and the checkpoint's immutable `pending` field should not be edited.

## Publication assessment and disposition

This short elementary lemma should remain an internal proof note, or appear as an auxiliary lemma in a larger work once that work warrants publication. The prescribed materials do not establish a standalone publication-level contribution or bibliographic novelty. That assessment is separate from the mathematical validity of the auxiliary proof.

There is no blocking mathematical or metadata objection. I approve the exact proof result for obligation `obligation-000004`, bound to the full stored checkpoint and exact claim digests above, with empty dependency IDs and route bindings and analytical reviewed policy. `admission/core-accept.json` contains the requested public acceptance spec. Controller acceptance, provenance validation, journal-receipt checks, and the controller's full immutable-inventory audit remain the responsibility of the accepting service; this review does not claim to have executed them. Only the review and acceptance-spec files were written, using `apply_patch`.
