# Independent mathematical result review: Erdos124 ternary reserve

Decision: approve the exact analytical result at checkpoint-000018 under the reviewed proof policy. No unresolved mathematical defect was found. This is a result review of the supplied proof, not a proposal review, controller acceptance, proof of the full original objective, or publication assessment.

## Subject, provenance, and authentication boundary

The prescribed context was read completely from `admission/ternary-result-context.json`. The binding values below are supplied by that context:

- Full stored checkpoint, including `id`: `47dca12bc7966f05b1d183f2da943bf8bf28dbcc9f95f35d23c18ebeeff5072b`.
- Exact Claim: `2440a6e23b1dd9ad1e709d5242f82fe9d60d1f6b240ec6da045af16551585ca6`.
- Evidence manifest: `5228299a26499d6d0c5e382ffc4c716571975c1d44f2114d1eb8ea2a15fc85bd`.
- Target obligation: `obligation-000022`; producer: `node-000012`, journal move 1.

Actual reviewer provenance is `source: host`, `actor_id: <user>`, `attestation_id: 01a07e01-52fd-7521-89a3-21ef207cdff4`. The actor and attestation were obtained from separate, single-variable `printenv USER` and `printenv CODEX_THREAD_ID` host checks using non-login `/bin/sh`. Both differ from the supplied author fields, `/root` and `01a07806-b2c5-7163-86d2-92e8e272b9eb`. These are observed host environment values, not invented reviewer names. Environment values and the supplied author record are not cryptographic authentication of intellectual independence.

The supplied hash bindings were not independently authenticated or recomputed. I inspected the actual files at the prescribed artifact root and compared the statements and manifest structure directly. I did not independently authenticate an immutable store, journal reservation receipt, current controller state, or transitive freshness audit. The approval concerns the mathematical content inspected under the supplied bindings. The service must still authenticate those bindings and perform its required acceptance audit; this review neither supplies nor bypasses that audit.

No parent transcript, current admission review, or other current result review was consulted. No mathematical program, Exactory CLI command, objective lifecycle operation, or native mutation was run. The only writes are these two prescribed review outputs. No successor claim was pursued.

## Material read

I first read the installed Codex README, then the math-solver entrypoint and complete shared SKILL.md. I read SEARCH.md's review and provenance, checkpoints and accepted results, and immutable evidence manifest sections, including the exact raw ResultReview schema. I also read CASHOUT.md and the consolidation and inventory entry instructions to assess those artifacts.

All ten manifest artifacts were read completely under `<workspace>/erdos-124/attack/`:

1. `erdos-124-ternary-reserve/moves/001-ternary-reserve.md`.
2. `erdos-124-ternary-reserve/units/consolidation.md`.
3. `erdos-124-ternary-reserve/units/INVENTORY.md`.
4. `erdos-124-ternary-reserve/problem.json`.
5. `erdos-124-ternary-reserve/journal.jsonl`.
6. `erdos-124-ternary-reserve/study/problem.md`.
7. `erdos-124-ternary-reserve/study/make-the-proof-constructive.md`.
8. `erdos-124-ternary-reserve/study/QUERY_LOG.md`.
9. `erdos-124-ternary-reserve/study/REFERENCE_PATHS.md`.
10. `erdos-124-ternary-reserve/novelty.md`.

The source-location sidecar resolves preflight references against `attack/preflight/ternary-reserve/`, shared sources against the research-root `sources/`, and two-component references against `attack/preflight/two-component/`. No external source context was needed for a mathematical inference: the proof supplies its own lemmas. I did not independently reproduce the historical literature search or authenticate its reported hits, access failures, or earlier acceptances. Those contextual reports supply no proof premise here.

## Exact statement and assumptions

The reviewed statement is:

> For every nonempty finite set D of distinct integers at least 3 with min D=3, gcd(D)=1 and sigma(D)=sum_{d in D}1/(d-1)>=11/6, every integer k>=1 and every finite set F of labelled occurrences (d,j) with d in D and j>=k, all sufficiently large integers are sums of finitely many remaining occurrences d^j, each pair (d,j) used at most once; coincident numerical values from different pairs remain separately available.

The checkpoint Claim and target Claim agree, including their empty assumption lists, named scope, quantifiers, and reviewed policy. The native claim and quadruple statement preserve the same mathematical statement. The proof establishes `for every D,k,F, there exists N(D,k,F), for every n>=N, there exists a finite remaining support`. It does not interchange the existential threshold with the input quantifiers or restrict the deletion or exponent range.

Only ordinary integer arithmetic, finite sets, and induction are needed. The use of coprimality for modular cancellation is elementary and justified by the stated hypotheses. There is no extra completeness assumption, additional axiom, unproved asymptotic estimate, or computational premise.

## Mathematical checks

### Balanced ternary and arbitrary tails

For each positive integer q, the selected digit epsilon is the unique member of {-1,0,1} with the same residue modulo 3. Then q'=(q-epsilon)/3 is a nonnegative integer and q'<q, including q=1. Strong induction therefore terminates and yields a finite expansion with one digit at each position. Uniqueness of the expansion is unnecessary.

For every K>=1 and b>=4 coprime to 3, repetition among powers modulo 3^K gives b^u=b^v modulo 3^K with u<v. Since b^u is a unit modulo 3^K, cancellation yields b^(v-u)=1 modulo 3^K. Positive multiples J of this period are unbounded, so J>=K can always be imposed. Thus q=(b^J-1)/3^K is a positive integer for arbitrarily high K. Multiplying its balanced expansion by 3^K gives the displayed unit identity with all ternary exponents at least K and the b exponent J at least K.

The sign separation is correct: positive ternary digits go into P; negative ternary digits and (b,J) go into Q. Consequently value(Q)-value(P)=1, and both sides are positive subset sums with coefficient one for each label. Distinct digit positions and opposite signs prevent ternary label overlap; b is a different base. Positivity of q forces at least one positive digit, so P is nonempty, while Q contains (b,J). No signed coefficient remains in a legal representation.

Choosing K above every exponent in a finite forbidden set avoids that set completely. During iteration the forbidden set includes both alternatives from every preceding pair, as required, and the relevant original deletion. Each stage excludes finitely many labels, and only finitely many stages are needed. Therefore the construction preserves the full arbitrary-deletion quantifier and makes all gadget supports mutually disjoint.

### Intervals, the fixed reserve, and the exact gap boundary

For r disjoint unit pairs, the baseline A=sum value(P_i) and the choices switching the first t pairs to Q_i give every A+t for 0<=t<=r. This proves an interval of r+1 consecutive sums. The empty case r=0 supplies [0,0]. It does not assert eventual completeness from thickness alone.

If the reserve meets every g consecutive nonnegative integers, then for n>=A+g-1 the interval [n-A-g+1,n-A] has exactly g nonnegative integers. Its reserve sum r leaves n-r in [A,A+g-1]. The two representations combine because the seed and reserve have disjoint labels. The lower bound is inclusive and has no off-by-one loss.

The stated boundary is correct as a universal implication from this gap information. For g>=2, a reserve with values g,2g,4g,... has subset sums exactly g times the nonnegative integers. A disjoint seed of g-2 unit labels has subset sums [0,g-2], including the empty seed when g=2. Their union misses residue g-1 modulo g. Thus g-1 consecutive seed sums need not suffice. This checks the proof's boundary example and does not assert optimality for any particular power supply.

### The reserve's mesh and mass equality

The finite-prefix mesh induction is valid. The subset-sum set at step i is U union (a_i+U). Each copy has gaps at most g within its span. Disjoint spans introduce only the gap a_i-S_(i-1); overlapping spans introduce no larger gap because a span endpoint is itself a subset sum. Positive integer values make prefix endpoints unbounded. An interval of g consecutive nonnegative integers missing the infinite subset-sum set would then force a finite-prefix gap of at least g+1. The endpoint and singleton cases are included.

For each base d, the strict-prefix inequality holds both below its first allowed power and at an exact power: taking the least r>=k with d^r>=x gives prefix sum (d^r-d^k)/(d-1). Subtracting the value of every deleted label is a valid lower bound even when some deleted values are not below x. All strictly smaller remaining values precede a label of value x; earlier equal values only increase the prefix sum. Keeping labels separately therefore handles numerical ties correctly.

It follows that a_i-S_(i-1)<=(1-sigma(B))*a_i+C_B<=C_B whenever sigma(B)>=1. With g=ceil(C_B), the mesh lemma applies at equality sigma(B)=1 as well. No gcd condition on B is needed. The finite positive constant C_B depends only on B,k,F_B.

### The inclusive threshold and quantifier order

Since 3 is in D and gcd(D)=1, some b in D is not divisible by 3. It is at least 4. Removing 3 and b leaves

`sigma(B) >= 11/6 - 1/2 - 1/3 = 1`.

In particular B is nonempty and its reserve is infinite and locally finite. The estimate does not require a strict mass inequality. The reserve uses precisely the other bases and remains untouched by every unit pair, even if values from different bases coincide. Its g is fixed before any seed is constructed, so there is no circular dependence between seed size and reserve gap.

The g-1 fresh pairs produce the needed interval, and N=max{1,A+g-1} works. All choices of b, reserve, g, pairs, and A depend only on D,k,F and precede the choice of n. Every resulting representation uses finitely many remaining labels once each. This completes the exact claimed quantifiers.

## Consolidation, inventory, ledger, and scope

The extracted corollary in the consolidation is sound: if D contains 3 and b coprime to 3 and sigma(D minus {3,b})>=1, the same proof works for every positive cutoff and finite labelled deletion. Such b is automatically distinct from 3, and the pair already has gcd one. This check verifies the corollary already in the supplied artifact; it creates no successor result, acceptance, or renewed resource basis.

The consolidation identifies and supplies the potentially missing digit, congruence, sign, and reserve arguments. Its account of the proof's structure is accurate. It explicitly claims no independent second proof of the exact threshold, and none is needed for this reviewed analytical result.

The journal records one closing move, no deterministic steps, no fired failure signal, and an empty cost ledger. Mathematically that ledger is appropriate relative to the admitted node claim: no hypothesis is added, no quantifier is weakened, and all auxiliary lemmas are discharged. The construction involves terminating finite choices; potentially enormous witnesses do not constitute loss of constructivity or effectivity for a statement requiring only an input-dependent threshold. No efficiency or uniform bound on N is proved or claimed. The node's narrower scope relative to the root remains explicit.

The inventory preserves the internal proof while selecting zero publication units. Its elementary interfaces, main theorem, and extracted corollary can consistently remain one internal proof record without claims of publication novelty. The bounded search records expressly acknowledge inaccessible sources and do not establish priority. The choice of zero publication units is not a mathematical rejection or a root closure, and no publication draft or formal-verification artifact is required for this analytical review.

There are minor historical-status remnants: `problem.json`'s `shape.known_bounds` says the route has not yet been executed, although its proof-shape field and journal record the completed candidate; the inventory lists checkpoint creation among pending requirements, while this review context already supplies a checkpoint. These are nonblocking status descriptions, not proof steps. I have not edited them or treated them as lifecycle authority. Similarly, the inventory's assertion that all plan tasks are done is not independently certified here because task and controller receipt records are outside this manifest.

The proof does not establish the full threshold-one objective, the entire minimum-three range below 11/6, or a new larger-minimum range. Its structural corollary may apply to some lower-mass inputs, which does not settle that entire range. Failure of the reserve estimate below mass one proves no impossibility theorem. The root and complementary obligations, and any required implication bridge, remain outside this approval. Previous accepted results are historical comparisons only and were not used as mathematical dependencies.

## Dependency and policy conclusion

Every nontrivial mathematical ingredient of the target proof is supplied and checked in Sections 1-6. Standard foundational arithmetic does not conceal a cited completeness theorem. The manifest's empty proof-dependency, external-dependency, acceptance-dependency, and route-binding lists are substantively consistent with this self-contained proof. Its analytical kind, proof outcome, and null verification field fit the reviewed policy; no certificate or Lean-kernel claim is made.

The accompanying JSON is exactly the raw ResultReview object: the full stored checkpoint digest, exact Claim digest, observed reviewer provenance, `decision: approve`, and the five required findings. This approval remains distinct from authenticated controller acceptance and does not change any objective state.
