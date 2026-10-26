module

import TriangleFreeEdit
import TriangleFreeSharpness

/-! Kernel axiom audit: run `lake env lean Audit.lean` after `lake build`. Each command should
print only `propext`, `Classical.choice` and `Quot.sound`. -/

#print axioms TriangleFreeEdit.editDistance_le_three_deficit
#print axioms TriangleFreeSharpness.cycle5_equality
#print axioms TriangleFreeSharpness.triangleFree_constant_sharp
