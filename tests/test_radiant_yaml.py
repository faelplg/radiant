"""Exercise the strict YAML subset reader used by the validators."""

from pathlib import Path
import sys
import unittest

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / "validators"))

from radiant_yaml import YamlError, load  # noqa: E402


class RadiantYamlTests(unittest.TestCase):
    def test_units_example_round_trip(self):
        data = load("units:\n  - id: TC-0025.1\n    requires: []\n"
                    "    writes: [src/a/, tests/a/]\n    capability: deep\n")
        self.assertEqual(data, {"units": [{"id": "TC-0025.1", "requires": [],
                                           "writes": ["src/a/", "tests/a/"],
                                           "capability": "deep"}]})

    def test_scalars_are_typed(self):
        self.assertEqual(load("a: true\nb: null\nc: 3\nd: '3'\ne: \"x # y\"\n"),
                         {"a": True, "b": None, "c": 3, "d": "3", "e": "x # y"})

    def test_comments_are_ignored(self):
        self.assertEqual(load("# topo\na: b  # fim\n"), {"a": "b"})

    def test_plain_scalar_with_colon_is_refused(self):
        with self.assertRaisesRegex(YamlError, r"^linha 1: .*aspas"):
            load("done_when: passa: ok\n")

    def test_duplicate_key_is_refused(self):
        with self.assertRaisesRegex(YamlError, r"^linha 2: .*repetida"):
            load("a: 1\na: 2\n")

    def test_tab_indentation_is_refused(self):
        with self.assertRaisesRegex(YamlError, r"^linha 2: .*tab"):
            load("a:\n\t- b\n")

    def test_unsupported_features_are_refused(self):
        for text in ("a: &x 1\n", "a: *x\n", "a: !tag 1\n", "a: |\n  b\n",
                     "a: {b: 1}\n", "---\na: 1\n", "a: [[b]]\n"):
            with self.subTest(text=text), self.assertRaises(YamlError):
                load(text)


if __name__ == "__main__":
    unittest.main()
