# Formal attempt log

1. The initial theorem under sorry elaborated and the red axiom gate failed as intended. This was a statement check, not a failed proof attempt.
2. The first Certificate8.lean check failed because its real division definition lacked a noncomputable declaration. No errors were reported for identity8 or positive8. This is an implementation slip, repaired by noncomputable section. Wall time 18.91 seconds; maximum resident set size 1595293696 bytes; peak memory footprint 136668544 bytes, from /usr/bin/time -l. Lean ran -j1 -M2048 at nice 15.

No mathematical lemma has been restated. The exact identity and positive-basis proof are the first mathematical attempts. No native evaluation or custom axiom has been introduced.

3. Certificate8 compiled successfully after the noncomputable repair, including identity8 and positive8. Wall time 15.00 s, maximum RSS 1621475328 bytes, peak memory footprint 166522176 bytes.
4. Certificate9 compiled on its first attempt, including identity9 and positive9. Wall time 11.46 s, maximum RSS 1640792064 bytes, peak memory footprint 167849728 bytes.
5. Main compiled on its first proof attempt. Wall time 7.15 s, maximum RSS 1541062656 bytes.
6. The final harness check passed, with exactly propext, Classical.choice, Quot.sound. Wall time 10.05 s, maximum RSS 1507311616 bytes. The harness's lightweight axiom-print subprocess uses its built-in command without explicit Lean flags; a separate explicit -j1 -M2048 Audit.lean run checks every principal theorem under the required flags. All proof compilations had -j1 -M2048 through the package configuration or command line; stages were sequential and used nice 15.

The only failed implementation attempt was the missing noncomputable declaration. The initial sorry gate was intentional. No six-attempt or two-restatement limit was approached.
