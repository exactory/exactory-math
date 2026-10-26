import Audit

-- This separate audit checks the public positivity theorem itself, not only its corollary.
#check @HallScalar.scalar_positive
#check @HallScalar.scalar_exclusion
#check @HallScalar.finite_certificate
#print axioms HallScalar.scalar_positive
#print axioms HallScalar.scalar_exclusion
#print axioms HallScalar.finite_certificate
#print axioms hall_scalar_certificate

-- Expose the arithmetic definitions used by the imported theorem.
#print HallScalar.gamma
#print HallScalar.rectangle
#print HallScalar.oneZero
#print HallScalar.floor
#print HallScalar.curvature
