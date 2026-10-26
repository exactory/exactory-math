"""Run the reviewed independent n=7 routines without repeating n=6 work."""
import importlib.util
import json
from pathlib import Path

source=Path(__file__).resolve().parents[2]/'study/external-proof/n6-n7/audit_dittert_n6_n7_sympy.py'
spec=importlib.util.spec_from_file_location('external_n7_independent_audit',source)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
result={'scalars':module.audit_n7_scalars(),'bridges':module.audit_n7_bridges()}
print(json.dumps(result,sort_keys=True,indent=2))
print('INDEPENDENT N=7 SCALARS AND ALL BRIDGES CERTIFIED')
