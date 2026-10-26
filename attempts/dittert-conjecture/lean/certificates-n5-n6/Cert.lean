import Cert.Core
import Cert.Sym
import Cert.Data5
import Cert.N5
import Cert.Ident5
import Cert.Check5
import Cert.Data6
import Cert.N6
import Cert.Ident6
import Cert.Check6

/-!
# The Dittert certificate checks

The root of the `Cert` library, which is precompiled (`precompileModules` in `lakefile.toml`).
That is what makes `native_decide` run the checks as compiled code: without it Lean interprets
every imported definition, which measured three times slower on the `n = 5` check.

`Theorem5.lean` and `Theorem6.lean` sit outside this library on purpose, so that building it
does not run either check.
-/
