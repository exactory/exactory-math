import Cert.Ident5

/-!
# The n = 5 certificate check as a Boolean

`certOK5` takes `Unit` rather than being a nullary definition.  A closed nullary definition is
evaluated when its module is loaded, so the check would run once at import and again inside
`native_decide`; taking `Unit` leaves exactly one evaluation, in `native_decide`, and makes
every later import of `Cert.Theorem5` free, including the one `#print axioms` needs.
-/

namespace Cert5

/-- The certificate check as a Boolean, for `native_decide`. -/
def certOK5 (_ : Unit) : Bool := certOK5Impl ()

end Cert5
