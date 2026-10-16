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

    def test_unknown_requirement_fails(self):
        errors = validate_provides({"provides": ["turbo"]}, {"browser"})
        self.assertTrue(any("'turbo'" in error for error in errors), errors)

    def test_repeated_requirement_fails(self):
        errors = validate_provides({"provides": ["browser", "browser"]}, {"browser"})
        self.assertTrue(any("repetido" in error for error in errors), errors)

    def test_wrong_shape_fails(self):
        errors = validate_provides({"outros": []}, {"browser"})
        self.assertTrue(any("provides" in error for error in errors), errors)


VALID = {"units": [
    {"id": "TC-0025.1", "role": "radiant-dev", "requires": [],
     "objective": "Buscar fontes externas por rev para o cache.",
     "writes": ["src/sources/", "tests/sources/"], "depends_on": [],
     "done_when": "Os testes de tests/sources passam e o cache recusa digest divergente."},
    {"id": "TC-0025.2", "role": "radiant-dev", "capability": "deep",
     "capability_reason": "A recusa de digest exige julgamento de segurança.",
     "requires": [], "objective": "Integrar a verificação de digest ao sync.",
     "writes": ["src/sync/"], "depends_on": ["TC-0025.1"],
     "done_when": "bun run check passa e o sync recusa conteúdo sem digest correspondente."},
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
        self.assertError(variant(depends_on=[], writes=["src/sources"]), "sobrep")

    def test_overlap_check_uses_segments(self):
        data = copy.deepcopy(VALID)
        data["units"][0]["writes"] = ["src/sync/"]
        data["units"][1].update(depends_on=[], writes=["src/sync2/"])
        self.assertEqual(self.errors(data), [])

    def test_dependency_cycle_fails(self):
        data = copy.deepcopy(VALID)
        data["units"][0]["depends_on"] = ["TC-0025.2"]
        self.assertError(data, "ciclo")

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
        self.assertError(variant(id="TC-0026.2", depends_on=["TC-0025.1"]), "prefixo")

    def test_escaping_write_path_fails(self):
        for path in ("../x", "/x"):
            with self.subTest(path=path):
                self.assertError(variant(writes=[path]), path)

    def test_two_blocks_are_refused(self):
        block = "```yaml radiant-units\nunits: []\n```\n"
        with self.assertRaisesRegex(ValueError, "mais de um bloco"):
            extract_units_block(block + block)

    def test_block_body_is_extracted(self):
        self.assertEqual(extract_units_block("x\n```yaml radiant-units\nunits: []\n```\n"), "units: []\n")
        self.assertIsNone(extract_units_block("```yaml\na: 1\n```\n"))


ROUTING = {
    "schema": 1,
    "rules": [
        {"id": "ui-browser", "when": "Unidades de interface que precisam abrir e inspecionar páginas",
         "use": [{"harness": "claude-code"}, {"harness": "codex"}],
         "why": "Preferência do owner para inspeção visual"},
        {"id": "independent-critique", "when": "Crítica de um Build feito por modelo de outro fornecedor",
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
        self.assertError(data, "repetido")

    def test_unknown_schema_fails(self):
        data = copy.deepcopy(ROUTING)
        data["schema"] = 2
        self.assertError(data, "schema")


if __name__ == "__main__":
    unittest.main()
