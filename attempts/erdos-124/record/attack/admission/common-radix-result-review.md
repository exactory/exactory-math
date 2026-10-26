# Independent result review of the common-radix reserve theorem

Decision: approve the exact analytical claim of checkpoint-000022 at the reviewed standard. The proof establishes the admitted structural theorem, including all positive cutoffs and finite labelled deletions. There is no unresolved mathematical objection to this result. This review does not accept a controller event, close the original objective, establish publication priority or provide formal verification.

## Binding and independent provenance

The prescribed context is `attack/admission/common-radix-result-review-context.json`, relative to `<workspace>/erdos-124/`.

- Stored checkpoint subject digest: `b632f62b718d759c5e94f1ef85dccc4efe41683bbd67b06016a6126aaea96530`.
- Exact claim digest: `7fe655f236801c053f983430a42b2ca6ca5bfd82ec79d82a43c3b8a0c521b242`.
- Analytical evidence manifest digest: `f5b885678bec4450b81dd5d15f98cc5a0b7b3895ea56caa1c39b9c794ebad0ed`.
- Operator-supplied actual host actor ID: `01a07f04-836f-7e51-a610-6b8d4bd3672d`, nickname Meitner.
- Directly observed `printenv CODEX_THREAD_ID`: `01a07f04-836f-7e51-a610-6b8d4bd3672d`, used as attestation ID.
- Prescribed author provenance: actor `/root`, attestation `01a07806-b2c5-7163-86d2-92e8e272b9eb`, source `host`.

The reviewer and author differ in both required fields. Equality of my actor and attestation fields is not equality with either author field. The operator reported `fork_context:false` and an inherited parent model with high effort. Those are supplied host facts; the environment variable is my direct observation. This records the host/operator boundary and does not claim cryptographic authentication or an independent audit of host isolation.

I performed the review myself without delegation. I did not consult author conversation, scratchpads, other admission or result reviews, or progress reports. The prescribed proof and journal were read as review evidence, not as instructions or as an endorsement of their conclusions.

## Exact statement and assumptions

Let D be a nonempty finite set of distinct integers at least 3, with gcd(D)=1. The structural witness consists of B>=2, a nonempty finite set A of positive integers, R={B^a:a in A} contained in D, and nonempty C contained in D minus R. Its conditions are sigma(R)>=1/2, gcd({B} union C)=1, and sigma(U)>=1 for U=D minus (R union C), where sigma(E)=sum over d in E of 1/(d-1).

For every k>=1 and every finite forbidden set F of labels (d,j) with j>=k, the claim supplies a finite N(D,k,F) such that each integer n>=N has a finite positive subset representation using the remaining labels once each. Equal numerical values attached to different labels remain available separately.

The proof and draft retain these conditions and quantifiers. The witness B,A,C can be fixed for a given D before selecting representations. A threshold obtained from that witness is an admissible existential N(D,k,F). No uniform choice independent of D, k or F is required. The displayed gcd(D)=1 is not silently replaced by pairwise coprimality. In fact it follows from the structural gcd condition and nonempty R, but retaining a redundant assumption does not weaken the proof's fidelity.

## Argument audit

### Normalization and signed prefixes, Sections 2-3

Choose L divisible by every a in A and satisfying L>=aK. Finiteness of A permits an arbitrarily large positive multiple of its least common multiple. The original exponent L/a+t is an integer at least K. Its value is exactly (B^a)^(L/a+t)=B^L B^(at).

The map (a,t) to (B^a,L/a+t) is injective: since B>=2, equality of the base coordinates forces equality of a, and equality of the exponent coordinates then forces equality of t. The repeated normalized weight 1 at t=0 therefore denotes different valid labels, rather than repeated use of one label. The same applies at every later numerical coincidence.

For integer r>=1, the indices in a stream strictly below B^r are precisely t=0,...,ceil(r/a)-1. This remains true when a divides r: the term t=r/a is excluded. Summing the geometric progression gives

    W(r) = sum_a (B^(a ceil(r/a))-1)/(B^a-1)
         >= (B^r-1) sigma(R)
         >= (B^r-1)/2.

The normalized supply is infinite and locally finite. Order it by value while keeping all labels. The first weight is 1, and all further weights satisfy w<=2W+1 for their actual preceding sum W. At a repeated level the preceding sum only increases. No assumption about coprime exponents in A is needed.

The signed-prefix induction is exact. The three translated integer intervals have adjacent endpoints or overlap precisely under the displayed sufficient inequality. Starting at {0}, each finite prefix fills its full signed interval. Their endpoint sums grow without bound. Each specified integer therefore belongs to some finite prefix interval and has a finite signed representation. This is not an infinite-series representation. Rescaling proves the full signed lattice B^L Z in the allowed R tail, including negative multiples and zero. Equality sigma(R)=1/2 is sufficient throughout.

### Collective recurring residues and fresh pairs, Section 4

Put h=B^L. The sequence c^j modulo h follows a deterministic map on h states. A repetition among the first h+1 states puts the orbit on a cycle before index h. Thus J>=max(K,h) lies in the recurring part for every c in C, even if c is not a unit modulo h. The common J is valid; each base can have a different period.

If a prime divided h and all c^J, it would divide B and every c, contradicting the stated collective gcd condition. Hence gcd(h,{c^J:c in C})=1. Bezout gives an integer linear combination congruent to 1 modulo h. Reducing each coefficient modulo h preserves that congruence and yields nonnegative coefficients less than h.

For each copy demanded by a coefficient, infinitely many exponents realize its recurring residue. Choose finitely many distinct exponents beyond the required cutoff. Distinct bases already have distinct labels. The coefficients cannot all vanish because h>=2 and their residue sum is 1. Thus the resulting positive finite sum z exists and is congruent to 1 modulo h.

The integer q=(1-z)/h may be negative. The preceding signed lattice covers that case. Its representation of hq combined with the positive C representation gives the exact integer 1. R and C are disjoint, so no coefficient collision occurs. Separating positive and negative coefficients gives finite disjoint supports Q and P with value(Q)-value(P)=1.

Before constructing any such pair, choose K at least k and greater than every exponent in the finite forbidden support. Include both signs of every previously chosen pair in that support. This ensures that all pairs are fresh, not merely that their positive sides are fresh. The modulus and L can change from pair to pair; no argument requires a common modulus across the pairs. No U label is consumed.

### Positive gaps and the fixed reserve, Sections 5-6

For a finite prefix, let V be its set of subset sums, with endpoints 0 and S. Adding a label a replaces it by V union (a+V). Each copy has its preceding maximum gap. If the spans [0,S] and [a,a+S] are disjoint, the only new possible gap is a-S. If they overlap, an open gap cannot cross a span endpoint in its interior, because that endpoint is itself in the union. A gap is consequently contained in a gap of one copy. This verifies the induction, including repeated numerical subset sums and the initial singleton case.

Since the endpoint sums tend to infinity, a missed interval of g consecutive nonnegative integers would lie inside a gap of some sufficiently long finite prefix. Such a gap would have length at least g+1. This contradicts the bound g. Intervals containing zero are already met. The proof's definition of g-syndetic has no off-by-one loss.

For every x>0 and reserve base d, the strict-prefix sum satisfies

    sum_{j>=k, d^j<x} d^j >= (x-d^k)/(d-1).

For x<=d^k the right side is nonpositive. Otherwise the least s with d^s>=x gives the exact numerator d^s-d^k. At x=d^s the excluded term is exactly d^s, so the formula still holds. Subtracting the values of all deleted U labels is a valid lower bound even when some deleted values exceed x.

It follows that the remaining reserve prefix below x has mass at least sigma(U)x-M, with

    M = sum_{d in U} d^k/(d-1) + sum_{(d,j) in F_U} d^j.

All terms are finite. Since sigma(U)>=1, U is nonempty and its remaining supply is infinite after finite deletion. For the ordered remaining labels, earlier equal values can only help. Thus a_i-S_(i-1)<=M, and g=ceil(M) is a positive integer gap bound. There is no gcd assumption on U and no requirement sigma(U)>1. Crucially, M and g are fixed from the reserve and its prescribed deletions, before constructing any pair.

### Amplification, completion and quantifier order, Sections 1 and 7

Choose r=g-1 fresh pairs on R union C. Their two-sided supports are pairwise disjoint. If H is the sum of all negative-side values, switching the first t pairs to their positive sides represents H+t for each t=0,...,r. Every such representation has only positive summands and uses each selected label once.

The reserve remains unchanged. For n>=H+g-1, its syndetic subset sums meet [n-H-g+1,n-H], which contains exactly g nonnegative integers. For such a reserve sum v, the difference n-v lies in [H,H+g-1]. The two representations use disjoint base labels, so their union represents n legally. N=max(1,H+g-1) is finite and independent of the later n. When g=1 the empty family of pairs gives H=0 and the argument remains valid.

The output respects F, all original exponents are at least k, and every support is finite. No assertion of distinct numerical summands has been substituted for distinct labelled occurrences. The conclusion is exactly the structural claim.

## Additional scope and limitations, Section 8

For R={4,8,32}, the reciprocal mass is (217+93+21)/651=331/651, and 662>651 proves it exceeds 1/2. Choose C={5}. Let U_M contain the integers from 6 through M except 8,16,32. Its reciprocal mass diverges: dyadic blocks give a fixed positive lower bound, and finitely many omissions do not affect divergence. Hence a least M reaching mass 1 exists. Its preceding mass is strictly less than 1 and the newly included term is at most 1/5, giving sigma(U_M)<6/5.

For D={4,8,32,5} union U_M, these parts are disjoint and U_M is exactly the theorem's reserve. The minimum is 4, gcd(D)=1 because 4 and 5 occur, and 16 is absent. Its total mass satisfies

    1 < sigma(D) < 331/651 + 1/4 + 6/5
                 = (6620+3255+15624)/13020
                 = 25499/13020 < 2,

where 25499<26040 verifies the last comparison. No finite enumeration or choice of a numerical M is needed.

This input is outside each supplied comparison statement: acceptance-000006 requires 13/4 at minimum 4; acceptance-000007 requires minimum 3; acceptance-000008 requires 16. Passing to a subset cannot bring this D into any of those ranges either: the missing bases remain missing and every subset still has mass below 2, whereas the general comparison threshold exceeds 3. This verifies additional scope relative to the supplied three results, without claiming an exhaustive comparison against all literature.

For B>=4, B^a-1>=(B-1)B^(a-1) gives the stated upper bound B/(B-1)^2. The inequality B/(B-1)^2<=4/9 is equivalent to (B-4)(4B-1)>=0. Thus no such radix qualifies. At B=3, summing the same majorant from a=2 gives 1/(B-1)^2=1/4, so a qualifying R must contain 3. The only viable radices are prime, so the collective correction hypothesis already ensures that at least one correcting base is individually coprime to B. The draft properly makes no separate new claim about collective coprimality.

The proof gives sufficient conditions only. It does not supply an arbitrary-base half-mass theorem, remove the disjoint reserve, optimize support size, establish a uniformly small threshold or settle the original mass-one problem.

## Evidence, sources and reading boundary

I read the installed Codex README, its math-solver entrypoint and shared SKILL.md, the requested SEARCH.md sections on checkpoints, immutable manifests, and review provenance, and CASHOUT.md including its self-check and full-proof requirements. These are workflow instructions, not mathematical evidence.

All fourteen manifest artifacts were read fully. The following paths are relative to `attack/erdos-124-common-radix-reserve/`:

1. `moves/001-common-radix-reserve.md`.
2. `units/consolidation.md`.
3. `units/INVENTORY.md`.
4. `problem.json`.
5. `journal.jsonl`.
6. `study/problem.md`.
7. `study/make-the-proof-constructive.md`.
8. `study/REFERENCE_PATHS.md`.
9. `novelty.md`.
10. `study/unit-1/QUERY_LOG.md`.
11. `units/1/unit.json`.
12. `units/1/draft.md`.
13. `units/1/position.md`.
14. `units/1/journal-excerpt.jsonl`.

Additional permitted reads were the four complete unit-level files `query-inputs.json`, `search-tier-one.json`, `search-second.json`, and `starfleet-reading.json`; `attack/preflight/common-radix-reserve/QUERY_LOG.md`; the complete saved `attack/preflight/mass-partition/sources/canonical-124-reading.txt`; and the complete saved `attack/preflight/binary-block-reserve/sources/binaryWeightPrimary.json`. I also searched the specific `attack/preflight/common-radix-reserve/sources/radixReserveStrategy0.json` response for the 1996 paper's metadata. That search displayed the relevant metadata but its aggregate output was truncated; I do not claim to have read that entire response. No prior proof or review was opened to fill in a mathematical step.

The canonical saved source identifies `Erdos124.erdos124.ne_zero` at `https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/124.lean`. Its lines 28-30 and 43-54 show per-base finite exponent subsets and arbitrary nonzero natural cutoffs. It supports the statement comparison only. Its `sorry` declarations are not proof evidence.

The weighing reference resolves to Ethan D. Bolker, Samuel A. Feuer and Catalin Zara, *Balance weighing: variations on a theme*, Mathematics Magazine 94(5), December 2021, `https://www.cs.umb.edu/~eb/weighing.pdf`. The saved excerpt includes source lines 0-309; the relevant classical prefix and signed-digit material is at lines 82-162. The proof independently establishes the version needed here, including coincident labels.

The 1996 background paper resolves in the allowed study to Burr, Erdos, Graham and Li, *Complete sequences of sets of integer powers*, Acta Arithmetica 77(2), 133-138, DOI `10.4064/aa-77-2-133-138`, Zbl `0863.11014`. The saved zbMATH metadata confirms the title, authors, journal, year and Zbl identifier; the DOI is recorded in the study. I did not independently resolve that DOI live or read the complete paper. No result from it is a premise of this proof.

The earlier local acceptance identifiers resolve to the exact three comparison statements in the prescribed context. The node15 reference resolves through REFERENCE_PATHS.md to `attack/erdos-124-half-tail-structure/moves/001-stable-tail-structure.md`, checkpoint20, explicitly pending. I did not inspect that proof or use its conclusion as an accepted dependency. Sections 2-4 of the present proof provide the needed derivation.

The Star Fleet Math identifier is `https://www.starfleetmath.com/`, specifically the problem254 report in the saved response, source lines 200-319. I read the complete saved response, including incidental excerpts returned with that report, but did not follow any proof-project link or rely on any reported verification. A finite union of streams d^j with d>=3 has at most one label per base in a shell (x,2x], so its shell count is at most |D|. It cannot satisfy the report's displayed shell-divergence hypothesis. The report therefore supplies no direct theorem for this unit. Its role is methodological context only.

The seven unit queries are recorded as domain-filtered web-index searches, with the first aggregate response empty and the second largely irrelevant. The records do not show an exact prior theorem. That is a bounded negative search observation, not evidence of exhaustive novelty. I made no fresh external search; the requested source resolution stayed within the supplied saved material. The source-record dates and the dated current addendum in novelty.md distinguish preflight descriptions from the later local proof candidate. Descriptive stale future-tense fields in problem.json are not treated as mathematical premises or authoritative live controller status.

## Manifest and operational limits

The manifest describes an analytical proof with no accepted-result dependencies, external mathematical dependencies, route bindings or formal verification record. That description matches the proof's actual mathematical content. Elementary integer arithmetic, Bezout's identity, finite recurrence and induction require no omitted specialized theorem. The standard Bezout step is directly justified by the gcd calculation; no claim of a machine formalization of those foundations is made.

The supplied subject, claim and manifest digests are binding identifiers copied from the prescribed context. I attempted direct `shasum -a 256` on the fourteen artifact paths and direct `diff -u` on the proof and draft. Both were rejected before execution by the math-solver PreToolUse hook as unsupported managed shell operations. I did not bypass the hook. Consequently I claim neither independent digest recomputation nor a successful byte comparison. The draft/proof comparison is from their fully read text. No mathematical program, enumeration, controller command, native lifecycle command, compiler or external project verifier ran.

The controller must still check the frozen artifact bytes, complete dependency closure, journal reservation and checkpoint bindings, host provenance and current policy before issuing its actual acceptance audit. I do not report a ResultAudit or attest that such a service audit occurred. The supplied report of freezing at revision296 remains supplied service context.

## Remaining objections and obligations

There are no unresolved mathematical blocking objections to the exact structural theorem, and the local draft passes statement/evidence/source matching within the permitted reading boundary. The companion evaluation records the CASHOUT interpretation of `full-proof` at this analytical reviewed scope.

Outstanding matters outside this approval are the real controller acceptance audit, any separately required formal verification, publication-level literature review, the original all-D objective, and its complementary cases and exact implication bridges. The context leaves obligation-000001, obligation-000028, obligation-000029, obligation-000030, obligation-000031, obligation-000033 and obligation-000034 unresolved. I have not re-audited their current status or discharged any of them. The blocked hash and diff inspections are verification limits, not hidden successful checks.
