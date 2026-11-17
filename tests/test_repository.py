"""Exercise the repository validator against an isolated copy of this tree."""

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


def copy_tracked(destination):
    """Copy the files Git tracks, never local state such as harness worktrees."""
    listing = run("git", "ls-files", "-z", cwd=SOURCE)
    if listing.returncode != 0:
        raise RuntimeError(listing.stderr)
    for relative in filter(None, listing.stdout.split("\0")):
        source = SOURCE / relative
        if source.is_file():
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


class RepositoryFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="radiant-repo-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "radiant"
        copy_tracked(self.root)

    def check(self):
        return run(sys.executable, str(self.root / "validators/check_repository.py"))


class RepositoryCheckTests(RepositoryFixture):
    """Without Git metadata, the validator scans the files on disk."""

    def test_current_tree_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

    def assert_practice_failure(self, relative, message):
        result = self.check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(relative, result.stderr)
        self.assertIn(message, result.stderr)

    def test_practice_card_missing_section_fails(self):
        relative = "engineering/practices/tdd.md"
        path = self.root / relative
        path.write_text(path.read_text(encoding="utf-8").replace("## Verification", "Verification"), encoding="utf-8")
        self.assert_practice_failure(relative, "missing section: Verification")

    def test_practice_card_not_indexed_fails(self):
        text = (self.root / "engineering/practices/tdd.md").read_text(encoding="utf-8")
        (self.root / "engineering/practices/new-practice.md").write_text(text.replace("`tdd`", "`new-practice`"), encoding="utf-8")
        self.assert_practice_failure("engineering/practices/README.md", "card is not indexed: new-practice")

    def test_indexed_practice_without_card_fails(self):
        (self.root / "engineering/practices/adr.md").unlink()
        self.assert_practice_failure("engineering/practices/README.md", "indexed card is missing: adr")

    def test_repeated_index_row_fails(self):
        path = self.root / "engineering/practices/README.md"
        text = path.read_text(encoding="utf-8")
        row = next(line for line in text.splitlines() if line.startswith("| [`tdd`]"))
        path.write_text(text + row + "\n", encoding="utf-8")
        self.assert_practice_failure("engineering/practices/README.md", "repeated practice id: tdd")

    def test_malformed_index_row_fails(self):
        path = self.root / "engineering/practices/README.md"
        path.write_text(path.read_text(encoding="utf-8").replace("[`tdd`](tdd.md)", "tdd"), encoding="utf-8")
        self.assert_practice_failure("engineering/practices/README.md", "first cell must be one sibling card link")

    def test_practice_template_missing_section_fails(self):
        relative = "templates/practice-card.md"
        path = self.root / relative
        path.write_text(path.read_text(encoding="utf-8").replace("## Source", "Source"), encoding="utf-8")
        self.assert_practice_failure(relative, "missing section: Source")

    def test_contract_template_cites_unknown_practice_fails(self):
        relative = "templates/task-contract.md"
        path = self.root / relative
        path.write_text(path.read_text(encoding="utf-8").replace("`test-strategy`", "`no-such-practice`"), encoding="utf-8")
        self.assert_practice_failure(relative, "unknown practice id: no-such-practice")

    def test_adapter_missing_a_capability_fails(self):
        path = self.root / "adapters/codex/capabilities.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        del data["light"]
        path.write_text(json.dumps(data), encoding="utf-8")
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("adapters/codex/capabilities.json", result.stderr)

    def test_adapter_without_capabilities_file_fails(self):
        (self.root / "adapters/claude-code/capabilities.json").unlink()
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("adapters/claude-code", result.stderr)

    def test_template_units_example_must_validate(self):
        path = self.root / "templates/task-contract.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("role: radiant-dev", "role: radiant-x", 1), encoding="utf-8")
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("templates/task-contract.md", result.stderr)

    def test_routing_example_with_unknown_harness_fails(self):
        path = self.root / "docs/routing.example.json"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace('"claude-code"', '"copilot"', 1), encoding="utf-8")
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("docs/routing.example.json", result.stderr)

    def test_adapter_missing_from_global_block_fails(self):
        adapter = self.root / "adapters/new-harness"
        adapter.mkdir()
        shutil.copy2(self.root / "adapters/codex/capabilities.json", adapter / "capabilities.json")
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("adapters/global.template.md", result.stderr)

    def test_agent_with_unknown_role_or_capability_fails(self):
        path = self.root / "skills/radiant-delegation/agents.json"
        original = path.read_text(encoding="utf-8")
        for field, value in (("role", "missing"), ("capability", "turbo"), ("access", "admin")):
            with self.subTest(field=field):
                data = json.loads(original)
                data["agents"][0][field] = value
                path.write_text(json.dumps(data), encoding="utf-8")
                result = self.check()
                self.assertEqual(result.returncode, 1)
                self.assertIn("agents.json", result.stderr)
                path.write_text(original, encoding="utf-8")

    def test_provides_with_unknown_requirement_fails(self):
        path = self.root / "adapters/codex/provides.json"
        path.write_text(json.dumps({"provides": ["turbo"]}), encoding="utf-8")
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("adapters/codex/provides.json", result.stderr)

    def test_adapter_without_provides_fails(self):
        (self.root / "adapters/claude-code/provides.json").unlink()
        result = self.check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("adapters/claude-code", result.stderr)



class GitRepositoryCheckTests(RepositoryFixture):
    """Inside a Git checkout, the validator lists documents through Git."""

    def setUp(self):
        super().setUp()
        self.assertEqual(run("git", "init", "-q", cwd=self.root).returncode, 0)
        self.assertEqual(run("git", "add", ".", cwd=self.root).returncode, 0)

    def test_current_tree_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_ignored_harness_worktree_is_not_scanned(self):
        # Harness sessions keep full checkouts under .claude/worktrees/, excluded by Git.
        copy_tracked(self.root / ".claude/worktrees/session")
        exclude = self.root / ".git/info/exclude"
        exclude.write_text(exclude.read_text() + ".claude/worktrees/\n", encoding="utf-8")
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unignored_second_constitution_still_fails(self):
        copy = self.root / "drafts/CONSTITUTION.md"
        copy.parent.mkdir()
        shutil.copy2(self.root / "constitution/CONSTITUTION.md", copy)
        result = self.check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("single normative body", result.stderr)

    def test_git_failure_is_reported_instead_of_scanning_disk(self):
        (self.root / ".git/index").write_bytes(b"not an index")
        result = self.check()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("git ls-files", result.stderr)


if __name__ == "__main__":
    unittest.main()
