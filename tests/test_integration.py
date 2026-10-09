"""Exercise the actual bootstrap and pin commands in isolated repositories."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1]


def run(*args, cwd=None):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True)


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="radiant-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "Radiant relocated ç"
        self.project = Path(self.temp.name) / "New product"
        self.project.mkdir()
        self.root.mkdir()
        # Exclude AIKM custody entirely: the consumer must work without it.
        for directory in ("constitution", "docs", "skills", "templates", "adapters", "validators"):
            shutil.copytree(SOURCE / directory, self.root / directory,
                            ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copy2(SOURCE / ".gitignore", self.root / ".gitignore")
        self.assertEqual(run("git", "init", "-q", cwd=self.root).returncode, 0)
        self.assertEqual(run("git", "add", ".", cwd=self.root).returncode, 0)
        commit = run("git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                     "-c", "commit.gpgsign=false", "commit", "-qm", "test: initialize fixture", cwd=self.root)
        self.assertEqual(commit.returncode, 0, commit.stderr)
        self.revision = run("git", "rev-parse", "HEAD", cwd=self.root).stdout.strip()
        self.config = json.loads((SOURCE / "templates/radiant-project.json").read_text())
        self.config["radiant_revision"] = self.revision
        self.write_map()

    def write_map(self):
        (self.project / ".radiant.json").write_text(json.dumps(self.config), encoding="utf-8")

    def gate(self):
        return run(sys.executable, str(self.root / "validators/check_project.py"), str(self.project),
                   cwd=self.project)

    def render(self, *args):
        return run(sys.executable, str(self.root / "adapters/codex/render_bootstrap.py"), *args,
                   cwd=self.project)

    def assert_hold(self):
        result = self.gate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("HOLD:", result.stderr)

    def test_new_project_then_local_state_without_copying_core(self):
        self.assertEqual(self.gate().returncode, 0)
        folder = self.project / "docs/project"
        folder.mkdir(parents=True)
        for field in ("frame", "spec", "plan"):
            target = folder / f"{field.upper()}.md"
            target.write_text(f"# {field}\nProject-specific state.\n", encoding="utf-8")
            self.config[field] = target.relative_to(self.project).as_posix()
        contracts = folder / "contracts"
        contracts.mkdir()
        (contracts / "ACTIVE.md").write_text("Current contract: none.\n", encoding="utf-8")
        self.config["contracts"] = "docs/project/contracts"
        self.config["active_contract"] = "docs/project/contracts/ACTIVE.md"
        self.write_map()
        result = self.gate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.project / "constitution").exists())
        self.assertFalse((self.project / "skills").exists())
        self.assertFalse((self.root / "migration").exists())

    def test_mismatched_and_symbolic_revisions_are_rejected(self):
        for revision in ("0" * 40, "HEAD", "main", "RADIANT_COMMIT"):
            with self.subTest(revision=revision):
                self.config["radiant_revision"] = revision
                self.write_map()
                self.assert_hold()

    def test_dirty_tracked_staged_and_untracked_are_rejected(self):
        target = self.root / "constitution/CONSTITUTION.md"
        original = target.read_bytes()
        target.write_bytes(original + b"\nchanged\n")
        self.assert_hold()
        target.write_bytes(original)
        extra = self.root / "new-rule.md"
        extra.write_text("new rule\n", encoding="utf-8")
        self.assert_hold()
        self.assertEqual(run("git", "add", "new-rule.md", cwd=self.root).returncode, 0)
        self.assert_hold()

    def test_new_radiant_commit_requires_explicit_consumer_adoption(self):
        constitution = self.root / "constitution/CONSTITUTION.md"
        constitution.write_bytes(constitution.read_bytes() + b"\nFixture amendment.\n")
        self.assertEqual(run("git", "add", ".", cwd=self.root).returncode, 0)
        result = run("git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                     "-c", "commit.gpgsign=false", "commit", "-qm", "test: amend fixture", cwd=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_hold()
        self.assertEqual(json.loads((self.project / ".radiant.json").read_text())["radiant_revision"],
                         self.revision)
        self.config["radiant_revision"] = run("git", "rev-parse", "HEAD", cwd=self.root).stdout.strip()
        self.write_map()
        self.assertEqual(self.gate().returncode, 0)

    def test_bad_paths_and_wrong_types_are_rejected(self):
        outside = Path(self.temp.name) / "outside.md"
        outside.write_text("outside\n", encoding="utf-8")
        (self.project / "escape.md").symlink_to(outside)
        for value in ("missing.md", "../outside.md", str(outside), "escape.md", ".", "", 3):
            with self.subTest(value=value):
                self.config["frame"] = value
                self.write_map()
                self.assert_hold()

    def test_maintenance_is_optional_and_may_not_exist_yet(self):
        self.config.pop("maintenance", None)
        self.write_map()
        self.assertEqual(self.gate().returncode, 0)
        for value in (None, "ops/maintenance"):
            with self.subTest(value=value):
                self.config["maintenance"] = value
                self.write_map()
                result = self.gate()
                self.assertEqual(result.returncode, 0, result.stderr)
        (self.project / "ops/maintenance").mkdir(parents=True)
        self.assertEqual(self.gate().returncode, 0)

    def test_maintenance_rejects_escapes_and_files(self):
        outside = Path(self.temp.name) / "outside-dir"
        outside.mkdir()
        (self.project / "escape-dir").symlink_to(outside)
        (self.project / "report.md").write_text("x\n", encoding="utf-8")
        for value in ("../outside-dir", str(outside), "escape-dir", "report.md", "", ".", 3):
            with self.subTest(value=value):
                self.config["maintenance"] = value
                self.write_map()
                self.assert_hold()

    def test_invalid_duplicate_and_missing_map_are_rejected(self):
        mapping = self.project / ".radiant.json"
        for content in ("{", "[]", '{}', '{"radiant_revision":"a","radiant_revision":"b"}'):
            mapping.write_text(content, encoding="utf-8")
            self.assert_hold()
        mapping.unlink()
        self.assert_hold()

    def test_global_output_is_small_portable_and_non_destructive(self):
        result = self.render()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(str(self.root), result.stdout)
        self.assertNotIn(str(SOURCE), result.stdout)
        self.assertLess(len(result.stdout.encode()), 1024)
        self.assertNotIn("Artigo", result.stdout)
        output = self.root / ".local/codex-global.md"
        self.assertEqual(self.render("--output", str(output)).returncode, 0)
        self.assertEqual(output.read_text(encoding="utf-8"), result.stdout)
        self.assertEqual(self.gate().returncode, 0)  # Generated output is ignored.
        output.write_text("existing preferences\n", encoding="utf-8")
        self.assertNotEqual(self.render("--output", str(output)).returncode, 0)
        self.assertEqual(output.read_text(), "existing preferences\n")
        link = self.project / "global-link.md"
        link.symlink_to(output)
        self.assertNotEqual(self.render("--output", str(link)).returncode, 0)
        self.assertEqual(output.read_text(), "existing preferences\n")


if __name__ == "__main__":
    unittest.main()
