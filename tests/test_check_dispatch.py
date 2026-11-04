"""Exercise the dispatch validator command that operators call with this checkout's rules."""

import json
import os
import shutil
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / "validators"))

import radiant_yaml  # noqa: E402
from dispatch_formats import extract_units_block  # noqa: E402

COMMAND = SOURCE / "validators/check_dispatch.py"
TEMPLATE = SOURCE / "templates/task-contract.md"
ROUTING = SOURCE / "docs/routing.example.json"


def run(*args, stdin=None, env=None):
    return subprocess.run([sys.executable, str(COMMAND), *args], input=stdin,
                          capture_output=True, text=True, env=env)


class UnitsCommandTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="radiant-dispatch-")
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)

    def contract(self, text):
        path = self.dir / "TC-0025-example.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_template_units_print_the_same_value_as_the_canonical_reader(self):
        # Protects operators that consume the parsed units instead of parsing YAML themselves.
        result = run("units", str(TEMPLATE))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        expected = radiant_yaml.load(extract_units_block(TEMPLATE.read_text(encoding="utf-8")))
        self.assertEqual(json.loads(result.stdout), expected)

    def test_contract_read_from_stdin(self):
        # Operators read the contract from a Git commit, so it never exists as a file.
        result = run("units", "-", stdin=TEMPLATE.read_text(encoding="utf-8"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(len(json.loads(result.stdout)["units"]), 2)

    def test_invalid_unit_lists_errors_and_exits_1(self):
        # A wrong role must never reach a launch.
        text = TEMPLATE.read_text(encoding="utf-8").replace("role: radiant-dev", "role: nobody", 1)
        result = run("units", str(self.contract(text)))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        errors = json.loads(result.stdout)["errors"]
        self.assertTrue(any("'nobody'" in error for error in errors), errors)

    def test_restricted_yaml_error_keeps_the_line(self):
        # The subset is the canonical one; a full YAML parser would accept this anchor.
        text = TEMPLATE.read_text(encoding="utf-8").replace("depends_on: []", "depends_on: &a []", 1)
        result = run("units", str(self.contract(text)))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("line", json.loads(result.stdout)["errors"][0])

    def test_contract_without_block_exits_1(self):
        # Without units the contract is a single package; there is nothing to dispatch.
        result = run("units", str(self.contract("# Contract\n\nNo units.\n")))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("radiant-units", json.loads(result.stdout)["errors"][0])

    def test_missing_contract_exits_1(self):
        result = run("units", str(self.dir / "absent.md"))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertTrue(json.loads(result.stdout)["errors"])

    def test_usage_error_exits_2(self):
        self.assertEqual(run("units").returncode, 2)
        self.assertEqual(run("unknown", "x").returncode, 2)


class RoutingCommandTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="radiant-routing-")
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)

    def env(self, **values):
        env = {key: value for key, value in os.environ.items() if key != "XDG_CONFIG_HOME"}
        env.update(values)
        return env

    def test_example_rules_pass_and_print_the_rules(self):
        result = run("routing", str(ROUTING))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout), json.loads(ROUTING.read_text(encoding="utf-8")))

    def test_default_path_follows_xdg_config_home(self):
        # The instance belongs to the user, at the path that docs/routing.md defines.
        (self.dir / "radiant").mkdir()
        (self.dir / "radiant/routing.json").write_text(ROUTING.read_text(encoding="utf-8"),
                                                       encoding="utf-8")
        result = run("routing", env=self.env(XDG_CONFIG_HOME=str(self.dir)))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_default_path_without_xdg_uses_home_config(self):
        home = self.dir / "home"
        (home / ".config/radiant").mkdir(parents=True)
        (home / ".config/radiant/routing.json").write_text(ROUTING.read_text(encoding="utf-8"),
                                                           encoding="utf-8")
        result = run("routing", env=self.env(HOME=str(home)))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_harness_without_adapter_fails(self):
        # Routing to a harness without adapter would launch a session without the Radiant bootstrap.
        data = json.loads(ROUTING.read_text(encoding="utf-8"))
        data["default"] = [{"harness": "unknown-harness"}]
        path = self.dir / "routing.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        result = run("routing", str(path))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        errors = json.loads(result.stdout)["errors"]
        self.assertTrue(any("without an adapter" in error for error in errors), errors)

    def test_directory_without_adapter_files_is_not_an_adapter(self):
        # An empty directory is invisible to Git, so the pin gate would not catch it.
        root = self.dir / "radiant"
        for directory in ("adapters", "skills", "validators"):
            shutil.copytree(SOURCE / directory, root / directory,
                            ignore=shutil.ignore_patterns("__pycache__"))
        (root / "adapters/ghost").mkdir()
        data = json.loads(ROUTING.read_text(encoding="utf-8"))
        data["default"] = [{"harness": "ghost"}]
        path = self.dir / "routing.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        result = subprocess.run([sys.executable, str(root / "validators/check_dispatch.py"), "routing",
                                 str(path)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertTrue(any("'ghost'" in error for error in json.loads(result.stdout)["errors"]))

    def test_invalid_json_and_missing_file_exit_1(self):
        path = self.dir / "routing.json"
        path.write_text("{", encoding="utf-8")
        self.assertEqual(run("routing", str(path)).returncode, 1)
        self.assertEqual(run("routing", str(self.dir / "absent.json")).returncode, 1)


if __name__ == "__main__":
    unittest.main()
