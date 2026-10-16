"""Exercise the strict YAML subset reader used by the validators."""

from pathlib import Path
import sys
import unittest

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / "validators"))

from radiant_yaml import YamlError, load  # noqa: E402

try:
    import yaml
except ImportError:
    yaml = None


def typed(value):
    """Compare values with their types, since True == 1 in Python."""
    if isinstance(value, dict):
        return {key: typed(item) for key, item in value.items()}
    if isinstance(value, list):
        return [typed(item) for item in value]
    return (type(value).__name__, value)


def extract_template_block():
    text = (SOURCE / "templates/task-contract.md").read_text(encoding="utf-8")
    return text.split("```yaml radiant-units\n", 1)[1].split("\n```", 1)[0] + "\n"


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
        self.assertEqual(load('# topo\na: "b"  # fim\nc: [d]  # x\n'), {"a": "b", "c": ["d"]})

    def test_comment_after_plain_scalar_is_refused(self):
        for text in ("a: corrige o bug #12\n", "- b # fim\n"):
            with self.subTest(text=text), self.assertRaisesRegex(YamlError, r"^linha 1: .*aspas"):
                load(text)

    def test_apostrophe_inside_plain_scalar_is_literal(self):
        self.assertEqual(load("a: it's done\nb: d'água\n"), {"a": "it's done", "b": "d'água"})

    def test_doubled_single_quote_before_hash_is_kept(self):
        self.assertEqual(load("objective: 'it''s issue #12'\n"), {"objective": "it's issue #12"})

    def test_escaped_double_quote_inside_flow_list_is_kept(self):
        self.assertEqual(load('writes: ["src/a\\"b/", tests/]\n'), {"writes": ['src/a"b/', "tests/"]})
        self.assertEqual(load("writes: ['it''s, ok', b]\n"), {"writes": ["it's, ok", "b"]})

    def test_implicitly_typed_plain_scalars_are_refused(self):
        for value in ("True", "TRUE", "Null", "1.5", ".5", "0x10", "0b11", "007", "+1", ".inf",
                      ".NaN", "1_000", "1:30", "2026-10-16", "yes", "no", "on", "Off", "3 testes"):
            for text in (f"k: {value}\n", f"k: [{value}]\n"):
                with self.subTest(text=text), self.assertRaisesRegex(YamlError, "aspas"):
                    load(text)

    def test_typed_keys_are_refused(self):
        for text in ("true: 1\n", "null: 1\n", "yes: 1\n", "on: 1\n"):
            with self.subTest(text=text), self.assertRaises(YamlError):
                load(text)

    def test_indicator_led_or_control_plain_scalars_are_refused(self):
        for text in ("k: @x\n", "k: `x`\n", "k: `make test` passa\n", "k: %x\n", "k: - a\n", "k: -\n",
                     "k: ?\n", "k: ? x\n", "k: ]\n", "k: }\n", "k: =\n", "k: <<\n", "k: a\tb\n",
                     "k: b\x07\n", "- - a\n", "- -\n", "- ? x\n", "k: [- a]\n", "k: [a]b]\n",
                     "k: [@x]\n"):
            with self.subTest(text=text), self.assertRaises(YamlError):
                load(text)

    @unittest.skipUnless(yaml, "PyYAML ausente")
    def test_accepted_documents_match_a_full_parser(self):
        documents = [
            "units:\n  - id: TC-0025.1\n    requires: []\n    writes: [src/a/, tests/a/]\n",
            "a: true\nb: null\nc: 3\nd: '3'\ne: \"x # y\"\nf: -4\n",
            '# topo\na: "b"  # fim\nc: [d]  # x\n',
            "a: it's done\nb: d'água\nc: src/sync/\nd: TC-0025.1\ne: _x\nf: .gitignore\n",
            "a:\n- b\n- c: d\n  e: [f, 'g h']\n",
            "a: 'it''s'\nb: \"l1\\nl2\"\n",
            "objective: 'it''s issue #12'\n",
            'writes: ["src/a\\"b/", tests/]\nc: [\'it\'\'s, ok\', b]\n',
        ]
        documents.append(extract_template_block())
        for text in documents:
            with self.subTest(text=text):
                self.assertEqual(typed(load(text)), typed(yaml.safe_load(text)))

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
