"""Meaningful regression checks for EARS table and canonical-reference auditing."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate-requirements.py"
SPEC = importlib.util.spec_from_file_location("requirements_audit", SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class RequirementAuditTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="ears-audit-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.row = ["PRD-001-R01", "event-driven",
                    "When a completed report is requested, the application shall provide its download.",
                    "User request; proposed scope", "Compare the downloaded data with a completed-report fixture",
                    "None - not risk-driven"]

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def prd(self, rows=None, body=None, status="draft", changes="None - no retired rows"):
        if body is None:
            rows = rows if rows is not None else [self.row]
            body = "| " + " | ".join(checker.HEADERS) + " |\n"
            body += "| " + " | ".join(["---"] * 6) + " |\n"
            body += "\n".join("| " + " | ".join(row) + " |" for row in rows)
        return self.write("prds/PRD-001.md", f"# Report requirements\n\n| Field | Value |\n| --- | --- |\n"
                          f"| ID | PRD-001 |\n| Status | {status} |\n\n"
                          f"## Behavioral requirements\n\n{body}\n\n## Requirement changes\n\n{changes}\n")

    def story(self, req_id="PRD-001-R01", target="../prds/PRD-001.md#behavioral-requirements",
              declared=None, criterion=None, status="draft"):
        link = f"[{req_id}]({target})"
        refs = link if declared is None else declared
        criterion = link if criterion is None else criterion
        return self.write("stories/US-001.md", f"# Export story\n\n| Field | Value |\n| --- | --- |\n"
                          f"| ID | US-001 |\n| Status | {status} |\n| Parents | PRD-001 |\n\n"
                          "## Acceptance criteria\n\n| Criterion | Requirement | Given | When | Then |\n"
                          "| --- | --- | --- | --- | --- |\n"
                          f"| AC-01 | {criterion} | completed fixture | request export | data matches |\n\n"
                          f"## Requirement references\n\n{refs}\n")

    def errors(self):
        return "\n".join(checker.audit(self.root)["errors"])

    def test_valid_scenario_links_and_audit_is_read_only(self):
        self.prd()
        self.story()
        before = {p: p.read_bytes() for p in self.root.rglob("*.md")}
        result = checker.audit(self.root)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["requirements"], 1)
        self.assertEqual(result["references"], 2)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*.md")})

    def test_wrong_parent_id_is_rejected(self):
        self.prd(rows=[["PRD-002-R01"] + self.row[1:]])
        self.assertIn("wrong-parent", self.errors())

    def test_duplicate_ids_and_duplicate_statements_are_rejected(self):
        self.prd(rows=[self.row, self.row])
        self.assertIn("duplicate requirement ID", self.errors())
        self.assertIn("exact duplicate statement", self.errors())

    def test_pattern_must_match_statement_shape(self):
        self.prd(rows=[[self.row[0], "state-driven"] + self.row[2:]])
        self.assertIn("does not match", self.errors())

    def test_required_fields_and_placeholders_are_rejected(self):
        row = list(self.row)
        row[4] = ""
        self.prd(rows=[row])
        self.assertIn("six nonempty fields", self.errors())
        row[4] = "<verification method>"
        self.prd(rows=[row])
        self.assertIn("placeholder", self.errors())

    def test_missing_delimiter_is_not_silently_treated_as_valid(self):
        body = "| " + " | ".join(checker.HEADERS) + " |\n"
        body += "| " + " | ".join(self.row) + " |\n"
        self.prd(body=body)
        self.assertIn("missing canonical table", self.errors())

    def test_retired_id_cannot_be_reused_or_referenced(self):
        changes = ("| Requirement ID | Change / rationale | Replacement ID |\n"
                   "| --- | --- | --- |\n| PRD-001-R01 | removed in revision 2 | None - removed |")
        self.prd(changes=changes)
        self.assertIn("retired requirement ID reused", self.errors())
        self.prd(body="None - discovery work only", changes=changes)
        self.story()
        self.assertIn("missing, retired or wrong-destination", self.errors())

    def test_wrong_destination_and_anchor_are_rejected(self):
        self.prd()
        self.story(target="../prds/PRD-002.md#behavioral-requirements")
        self.assertIn("wrong-destination", self.errors())
        self.story(target="../prds/PRD-001.md#scope")
        self.assertIn("#behavioral-requirements", self.errors())

    def test_external_or_outside_product_reference_is_rejected(self):
        self.prd()
        for target in ("https://example.com/PRD-001.md#behavioral-requirements",
                       "../../outside.md#behavioral-requirements"):
            with self.subTest(target=target):
                self.story(target=target)
                self.assertIn("inside the product root", self.errors())

    def test_criterion_refs_must_be_declared_and_linked(self):
        self.prd()
        self.story(declared="None - learning-only work")
        self.assertIn("not declared", self.errors())
        self.story(criterion="PRD-001-R01")
        self.assertIn("Requirement needs links", self.errors())

    def test_discovery_only_work_uses_justified_none(self):
        self.prd(body="None - this initiative investigates a demand hypothesis")
        self.story(declared="None - customer learning only", criterion="None - customer learning only")
        self.assertEqual(checker.audit(self.root)["errors"], [])
        self.prd(body="None - <reason>")
        self.assertIn("missing canonical table", self.errors())

    def test_legacy_prds_are_skipped_but_not_reported_as_ears_success(self):
        self.write("prds/PRD-001.md", "# Legacy\n\n| ID | PRD-001 |\n\n## Scope\n\nLegacy prose.\n")
        result = checker.audit(self.root)
        self.assertEqual(result["adopted"], 0)
        self.assertTrue(result["skipped"])
        self.assertIn("no EARS requirements checked", "\n".join(result["errors"]))

    def test_historical_references_are_not_active_work(self):
        self.prd()
        self.story(req_id="PRD-001-R99", status="superseded")
        self.assertEqual(checker.audit(self.root)["errors"], [])

    def test_all_six_supported_pattern_shapes(self):
        examples = {
            "ubiquitous": "The application shall retain the report identifier.",
            "event-driven": "When an export is requested, the application shall provide a download.",
            "state-driven": "While a report is pending, the application shall display its pending state.",
            "unwanted-behavior": "If input is malformed, then the application shall reject the request.",
            "optional-feature": "Where exports are enabled, the application shall display an export action.",
            "complex": "While a report is pending, when export is requested, the application shall reject it.",
        }
        for pattern, statement in examples.items():
            with self.subTest(pattern=pattern):
                self.prd(rows=[[self.row[0], pattern, statement] + self.row[3:]])
                self.assertEqual(checker.audit(self.root)["errors"], [])

    def test_missing_reference_section_for_adopted_parent_is_rejected(self):
        self.prd()
        self.write("epics/EPIC-001.md", "# Export outcome\n\n| ID | EPIC-001 |\n| Parents | PRD-001 |\n")
        self.assertIn("needs Requirement references", self.errors())


if __name__ == "__main__":
    unittest.main()
