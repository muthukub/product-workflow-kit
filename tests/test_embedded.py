"""Exercise kit coexistence with an application's README/config/coding agents."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1]


class EmbeddedKitTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="sdlc-embedded-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for folder in (".codex/agents", ".claude/agents", "templates", "workflow", "examples"):
            shutil.copytree(SOURCE / folder, self.root / folder)
        for name in ("AGENTS.md", "CLAUDE.md", "USER-MANUAL.md", ".codex/config.toml",
                     "scripts/validate-kit.py", "scripts/sync-claude-agents.py",
                     "scripts/validate-requirements.py", "tests/test_requirements.py"):
            destination = self.root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / name, destination)
        self.write("README.md", "# My application\n\nApplication setup belongs here.\n")
        self.write("apps/web/package.json", '{"name":"@app/web","private":true}\n')
        self.write(".codex/agents/coding_helper.toml",
                   'name = "coding_helper"\ndescription = "Application coding"\n'
                   'developer_instructions = "Follow engineering rules."\nmodel = "app-model"\n')
        self.write(".claude/agents/code-reviewer.md",
                   '---\nname: code-reviewer\ndescription: Review app code\n---\n\nApp rules.\n')
        config = self.root / ".codex/config.toml"
        config.write_text('model = "app-model"\n' + config.read_text(encoding="utf-8")
                          .replace("max_concurrent_threads_per_session = 3",
                                   "max_concurrent_threads_per_session = 7"), encoding="utf-8")

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def run_script(self, name, *args):
        return subprocess.run([sys.executable, str(self.root / "scripts" / name), *args],
                              cwd=self.root, capture_output=True, text=True, check=False)

    def snapshot(self):
        return {str(path.relative_to(self.root)): path.read_bytes()
                for path in self.root.rglob("*") if path.is_file()}

    def test_embedded_audit_preserves_application_and_default_mode_stays_strict(self):
        before = self.snapshot()
        result = self.run_script("validate-kit.py", "--embedded")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(before, self.snapshot(), "Embedded audit must not modify app files")
        strict = self.run_script("validate-kit.py")
        self.assertNotEqual(strict.returncode, 0)
        self.assertIn("Expected exactly nine", strict.stdout)
        self.assertIn("missing from agent catalog", strict.stdout)
        self.assertEqual(before, self.snapshot())

    def test_kit_only_sync_updates_managed_drift_and_preserves_coding_agents(self):
        custom = {name: (self.root / name).read_bytes() for name in (
            ".codex/agents/coding_helper.toml", ".claude/agents/code-reviewer.md",
            "README.md", ".codex/config.toml", "apps/web/package.json")}
        self.write(".claude/agents/lean-prd.md", "stale managed profile\n")
        result = self.run_script("sync-claude-agents.py", "--kit-only")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for name, content in custom.items():
            self.assertEqual((self.root / name).read_bytes(), content, name)
        check = self.run_script("sync-claude-agents.py", "--kit-only", "--check")
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)

    def test_embedded_mode_still_rejects_stale_managed_profiles_without_writes(self):
        self.write(".claude/agents/lean-prd.md", "stale managed profile\n")
        before = self.snapshot()
        result = self.run_script("validate-kit.py", "--embedded")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing or stale Claude profile: lean-prd.md", result.stdout)
        self.assertEqual(before, self.snapshot())

    def test_kit_only_missing_canonical_role_fails_before_writing(self):
        (self.root / ".codex/agents/adr.toml").unlink()
        before = self.snapshot()
        result = self.run_script("sync-claude-agents.py", "--kit-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Missing canonical SDLC roles: adr", result.stdout)
        self.assertEqual(before, self.snapshot())


if __name__ == "__main__":
    unittest.main()
