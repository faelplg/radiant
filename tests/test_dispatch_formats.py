"""Exercise the formats that describe dispatch: requirements, provides, units and routing."""

import copy
from pathlib import Path
import sys
import unittest

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / "validators"))

from dispatch_formats import (extract_units_block, validate_provides, validate_routing,  # noqa: E402
                              validate_units)


class ProvidesTests(unittest.TestCase):
    def test_known_requirement_passes(self):
        self.assertEqual(validate_provides({"provides": ["browser"]}, {"browser"}), [])

    def test_non_string_term_is_reported_not_raised(self):
        self.assertNotEqual(validate_provides({"provides": [["browser"]]}, {"browser"}), [])

    def test_unknown_requirement_fails(self):
        errors = validate_provides({"provides": ["turbo"]}, {"browser"})
        self.assertTrue(any("'turbo'" in error for error in errors), errors)

    def test_repeated_requirement_fails(self):
        errors = validate_provides({"provides": ["browser", "browser"]}, {"browser"})
        self.assertTrue(any("repeated" in error for error in errors), errors)

    def test_wrong_shape_fails(self):
        errors = validate_provides({"outros": []}, {"browser"})
        self.assertTrue(any("provides" in error for error in errors), errors)


VALID = {"units": [
    {"id": "TC-0025.1", "role": "radiant-dev", "requires": [],
     "objective": "Fetch external sources by rev for the cache.",
     "writes": ["src/sources/", "tests/sources/"], "depends_on": [],
     "done_when": "The tests in tests/sources pass and the cache refuses a mismatched digest."},
    {"id": "TC-0025.2", "role": "radiant-dev", "capability": "deep",
     "capability_reason": "Refusing a digest requires security judgment.",
     "requires": [], "objective": "Wire digest verification into sync.",
     "writes": ["src/sync/"], "depends_on": ["TC-0025.1"],
     "done_when": "bun run check passes and sync refuses content without a matching digest."},
]}
AGENTS = {"radiant-dev": "standard", "radiant-verifier": "deep"}


def variant(**changes):
    """Copy VALID and apply changes to the second unit."""
    data = copy.deepcopy(VALID)
    data["units"][1].update(changes)
    return data


class UnitsTests(unittest.TestCase):
    def errors(self, data):
        return validate_units(data, AGENTS, {"browser"})

    def assertError(self, data, fragment):
        errors = self.errors(data)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_units_pass(self):
        self.assertEqual(self.errors(VALID), [])

    def test_overlap_between_independent_units_fails(self):
        self.assertError(variant(depends_on=[], writes=["src/sources"]), "overlap")

    def test_overlap_check_uses_segments(self):
        data = copy.deepcopy(VALID)
        data["units"][0]["writes"] = ["src/sync/"]
        data["units"][1].update(depends_on=[], writes=["src/sync2/"])
        self.assertEqual(self.errors(data), [])

    def test_dependency_cycle_fails(self):
        data = copy.deepcopy(VALID)
        data["units"][0]["depends_on"] = ["TC-0025.2"]
        self.assertError(data, "cycle")

    def test_capability_requires_reason(self):
        data = variant()
        del data["units"][1]["capability_reason"]
        self.assertError(data, "capability_reason")

    def test_unknown_role_requirement_and_key_fail(self):
        for changes, fragment in (({"role": "radiant-x"}, "radiant-x"),
                                  ({"requires": ["turbo"]}, "turbo"),
                                  ({"harness": "codex"}, "harness")):
            with self.subTest(fragment=fragment):
                self.assertError(variant(**changes), fragment)

    def test_ids_must_share_prefix(self):
        self.assertError(variant(id="TC-0026.2", depends_on=["TC-0025.1"]), "prefix")

    def test_escaping_write_path_fails(self):
        for path in ("../x", "/x"):
            with self.subTest(path=path):
                self.assertError(variant(writes=[path]), path)

    def test_non_string_values_are_reported_not_raised(self):
        for changes in ({"role": ["x"]}, {"requires": [["a"]]}, {"capability": ["deep"]},
                        {"depends_on": [["TC-0025.1"]]}, {"writes": [["src/x/"]]}):
            with self.subTest(changes=changes):
                self.assertNotEqual(self.errors(variant(**changes)), [])

    def test_unnormalized_write_paths_fail(self):
        for path in ("./src/sync", "src//sync", ".", "./", "src/./x"):
            with self.subTest(path=path):
                self.assertError(variant(depends_on=[], writes=[path]), repr(path))

    def test_two_blocks_are_refused(self):
        block = "```yaml radiant-units\nunits: []\n```\n"
        with self.assertRaisesRegex(ValueError, "more than one radiant-units block"):
            extract_units_block(block + block)

    def test_block_body_is_extracted(self):
        self.assertEqual(extract_units_block("x\n```yaml radiant-units\nunits: []\n```\n"), "units: []\n")
        self.assertIsNone(extract_units_block("```yaml\na: 1\n```\n"))


ROUTING = {
    "schema": 1,
    "rules": [
        {"id": "ui-browser", "when": "Interface units that need to open and inspect pages",
         "use": [{"harness": "claude-code"}, {"harness": "codex"}],
         "why": "Owner preference for visual inspection"},
        {"id": "independent-critique", "when": "Critique of a Build made by another vendor's model",
         "use": [{"harness": "codex", "capability": "deep"}], "approval": "human"},
    ],
    "default": [{"harness": "claude-code"}],
}
ADAPTERS = {"claude-code", "codex"}


class RoutingTests(unittest.TestCase):
    def assertError(self, data, fragment):
        errors = validate_routing(data, ADAPTERS)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_example_passes(self):
        self.assertEqual(validate_routing(ROUTING, ADAPTERS), [])

    def test_unknown_harness_fails(self):
        data = copy.deepcopy(ROUTING)
        data["rules"][0]["use"][0]["harness"] = "copilot"
        self.assertError(data, "'copilot'")

    def test_unknown_approval_fails(self):
        data = copy.deepcopy(ROUTING)
        data["rules"][1]["approval"] = "auto"
        self.assertError(data, "approval")

    def test_repeated_rule_id_fails(self):
        data = copy.deepcopy(ROUTING)
        data["rules"][1]["id"] = "ui-browser"
        self.assertError(data, "repeated")

    def test_non_string_values_are_reported_not_raised(self):
        for path, value in ((("rules", 0, "use", 0, "harness"), ["codex"]),
                            (("rules", 0, "use", 0, "capability"), ["deep"]),
                            (("rules", 0, "id"), ["x"])):
            with self.subTest(path=path):
                data = copy.deepcopy(ROUTING)
                target = data
                for step in path[:-1]:
                    target = target[step]
                target[path[-1]] = value
                self.assertNotEqual(validate_routing(data, ADAPTERS), [])

    def test_unknown_schema_fails(self):
        data = copy.deepcopy(ROUTING)
        data["schema"] = 2
        self.assertError(data, "schema")


if __name__ == "__main__":
    unittest.main()
