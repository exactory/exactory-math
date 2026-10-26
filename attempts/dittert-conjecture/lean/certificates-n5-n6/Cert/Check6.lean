import Cert.Ident6

/-!
# The n = 6 certificate check as a Boolean

`certOK6` takes `Unit` rather than being a nullary definition, and that is deliberate.  A closed
nullary definition is evaluated when its module is loaded, so `Cert/Check5.lean` pays its whole
run once at import and again inside `native_decide`; taking `Unit` leaves exactly one evaluation,
in `native_decide`, and makes every later import of `Cert.Theorem6` free.
-/

namespace Cert6

/-- The certificate check as a Boolean, for `native_decide`. -/
def certOK6 (_ : Unit) : Bool := certOK6Impl ()

end Cert6
