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


class RepositoryCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="radiant-repo-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "radiant"
        shutil.copytree(SOURCE, self.root,
                        ignore=shutil.ignore_patterns(".git", ".local", "__pycache__"))

    def check(self):
        return run(sys.executable, str(self.root / "validators/check_repository.py"))

    def test_current_tree_passes(self):
        result = self.check()
        self.assertEqual(result.returncode, 0, result.stderr)

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

    def test_agent_with_unknown_role_or_capability_fails(self):
        path = self.root / "skills/radiant-delegation/agents.json"
        original = path.read_text(encoding="utf-8")
        for field, value in (("role", "inexistente"), ("capability", "turbo")):
            with self.subTest(field=field):
                data = json.loads(original)
                data["agents"][0][field] = value
                path.write_text(json.dumps(data), encoding="utf-8")
                result = self.check()
                self.assertEqual(result.returncode, 1)
                self.assertIn("agents.json", result.stderr)
                path.write_text(original, encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
