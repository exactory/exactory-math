"""Exercise the legacy PSD exit gate without generating the large matrix.

The production change caught here is removal or reversal of the negative-slack
failure exit. Execute the actual final statements after the computed slack.
Only the expensive candidate-generation prefix is excluded.
"""
import ast
import contextlib
import io
from pathlib import Path
import unittest

SOURCE = (
    Path(__file__).resolve().parents[3]
    / "dittert-conjecture-n5-to-n15/deterministic"
    / "certified-special-case-check-4/check.py"
)
tree = ast.parse(SOURCE.read_text(), filename=str(SOURCE))
assignments = [
    i for i, node in enumerate(tree.body)
    if isinstance(node, ast.Assign)
    and any(isinstance(t, ast.Name) and t.id == "slack" for t in node.targets)
]
if len(assignments) != 1:
    raise RuntimeError("Expected one final computed-slack assignment")
tail = ast.Module(body=tree.body[assignments[0] + 1:], type_ignores=[])
GATE = compile(tail, str(SOURCE), "exec")


class ExitGateTest(unittest.TestCase):
    def run_gate(self, slack):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(GATE, {"slack": slack, "log": print})
        return output.getvalue()

    def test_negative_slack_rejects(self):
        with self.assertRaises(SystemExit) as caught:
            self.run_gate(-1)
        self.assertNotIn(caught.exception.code, (None, 0))

    def test_zero_slack_accepts(self):
        self.assertIn("EXACT PSD PASS", self.run_gate(0))

    def test_positive_slack_accepts(self):
        self.assertIn("EXACT PSD PASS", self.run_gate(1691794048955))


if __name__ == "__main__":
    unittest.main()
