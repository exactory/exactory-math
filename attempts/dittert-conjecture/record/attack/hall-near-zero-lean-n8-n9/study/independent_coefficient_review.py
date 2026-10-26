"""Compare the actual Lean constants with the inherited Bernstein implementation.

This review check does not import or execute generate_certificate.py. Lean's
literal identity proofs remain the proof of the complete real inequalities.
"""
from fractions import Fraction
import importlib.util
import json
from math import comb
from pathlib import Path
import re
import sys

attack = Path(__file__).resolve().parents[1]
package = attack / "deterministic/formal-check-1"
inherited = attack.parent / "hall-n8-n15-branch-coverage/deterministic/certified-witness-chain-1/independent_coverage.py"
spec = importlib.util.spec_from_file_location("inherited_review_coverage", inherited)
coverage = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = coverage
spec.loader.exec_module(coverage)
metadata = json.loads((package / "candidate-data.json").read_text())
reports = []

for n, denominator in ((8, 400), (9, 500)):
    source = (package / f"Certificate{n}.lean").read_text()
    terms = re.findall(r"\((\d+) / (\d+) : ℝ\) \* x\^(\d+) \* \(1-x\)\^(\d+)", source)
    degree = 2 * n
    assert len(terms) == degree + 1
    actual = []
    for k, (numerator, divisor, left_power, right_power) in enumerate(terms):
        assert (int(left_power), int(right_power)) == (k, degree-k)
        actual.append(Fraction(int(numerator), int(divisor)))
    normalized = coverage.near_poly(n, Fraction(0), Fraction(1, denominator))
    expected = [comb(degree, k) * value for k, value in enumerate(normalized)]
    assert actual == expected
    assert all(value > 0 for value in actual)
    record = next(item for item in metadata if item["dimension"] == n)
    assert [Fraction(value) for value in record["coefficients"]] == actual
    assert record["interval_denominator"] == denominator
    assert record["degree"] == degree
    assert record["positive_coefficients"] == degree + 1
    assert Fraction(record["smallest"]) == min(actual)
    leading = sum(((-1)**(degree-k) * value for k, value in enumerate(actual)), Fraction(0))
    assert leading != 0
    for x in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1)):
        direct_sum = sum((value*x**k*(1-x)**(degree-k) for k, value in enumerate(actual)), Fraction(0))
        assert direct_sum == coverage.near_literal(n, x/denominator)
    reports.append({"dimension": n, "interval_denominator": denominator,
                    "degree_exact": degree, "matched_positive_coefficients": len(actual),
                    "metadata_matches": True, "literal_regression_points": 4})

unit = json.loads((attack / "units/1/unit.json").read_text())
full_journal = [json.loads(line) for line in (attack / "journal.jsonl").read_text().splitlines() if line.strip()]
excerpt = [json.loads(line) for line in (attack / "units/1/journal-excerpt.jsonl").read_text().splitlines() if line.strip()]
assert excerpt == [row for row in full_journal if row["move"] in unit["moves"]]
print(json.dumps({"status": "pass", "cases": reports, "journal_excerpt_matches": True}, indent=2))
