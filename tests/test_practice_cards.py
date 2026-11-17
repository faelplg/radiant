"""Check practice card structure and table readers without repository paths."""

from pathlib import Path
import sys
import unittest

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / "validators"))

from practice_cards import (CARD_SECTIONS, baseline_ids, index_ids, practice_ids,
                            validate_card, validate_sections)

VALID = """# Single responsibility

- Id: `solid-srp`
- Serves: [EB-05](../engineering-baseline.md#maintainability)

One reason to change.

## Applies when

Several actors change the module.

## Does not apply when

All parts change together.

## Violation signals

Unrelated changes edit the same module.

## Verification

Review the last changes by actor.

## Source

Robert C. Martin, Clean Architecture (2017).
"""
INDEX = """| Id | Practice | Serves |
| --- | --- | --- |
| [`solid-srp`](solid-srp.md) | Responsibility | [EB-05](../engineering-baseline.md) |
"""
CONTRACT = """# 8. Engineering Check

### Practices

| Practice | Serves | Why | Evidence |
| --- | --- | --- | --- |
| `tdd` | EB-03 | Behavior | Test |
| solid-srp | EB-05 | Actors | Review |

# 9. Constraints

| `unrelated` | ignored |
"""


class PracticeCardTests(unittest.TestCase):
    def test_valid_card_passes(self):
        self.assertEqual(validate_card(VALID, "solid-srp", {"EB-05"}), [])

    def test_baseline_ids_reads_only_headings(self):
        self.assertEqual(baseline_ids("# 7. EB-05 - Maintainability\nEB-09\n```\n## EB-08\n```\n"), {"EB-05"})

    def test_missing_sections_are_named(self):
        for section in CARD_SECTIONS:
            with self.subTest(section=section):
                errors = validate_sections(VALID.replace("## " + section, "Ignored"))
                self.assertTrue(any(section in error for error in errors), errors)

    def test_sections_out_of_order_fail(self):
        text = VALID.replace("## Applies when", "## TEMP").replace("## Source", "## Applies when").replace("## TEMP", "## Source")
        self.assertTrue(validate_sections(text))

    def test_repeated_section_fails(self):
        self.assertTrue(validate_sections(VALID + "\n## Source\nDuplicate\n"))

    def test_unknown_section_fails(self):
        self.assertTrue(validate_sections(VALID + "\n## Other\nExtra\n"))

    def test_empty_body_fails(self):
        self.assertTrue(validate_sections(VALID.replace("Review the last changes by actor.", "  ")))

    def test_fenced_headings_are_ignored(self):
        self.assertEqual(validate_sections(VALID + "\n```markdown\n## Fake\n```\n"), [])
        self.assertTrue(validate_sections(VALID.replace("## Source", "```\n## Source\n```")))

    def test_title_is_required_once(self):
        for text in (VALID.replace("# Single responsibility", "Title"), VALID + "\n# Extra\n"):
            self.assertTrue(validate_card(text, "solid-srp", {"EB-05"}))

    def test_id_equals_stem(self):
        self.assertTrue(validate_card(VALID, "solid-ocp", {"EB-05"}))

    def test_id_pattern(self):
        self.assertTrue(validate_card(VALID.replace("`solid-srp`", "`SOLID_SRP`"), "SOLID_SRP", {"EB-05"}))

    def test_id_is_backticked_and_unique(self):
        for text in (VALID.replace("`solid-srp`", "solid-srp"), VALID + "\n- Id: `solid-srp`\n"):
            self.assertTrue(validate_card(text, "solid-srp", {"EB-05"}))

    def test_serves_requires_baseline_id(self):
        self.assertTrue(validate_card(VALID.replace("EB-05", "nothing"), "solid-srp", {"EB-05"}))

    def test_serves_rejects_unknown_baseline_id(self):
        self.assertTrue(validate_card(VALID.replace("EB-05", "EB-09"), "solid-srp", {"EB-05"}))

    def test_serves_is_unique(self):
        self.assertTrue(validate_card(VALID + "\n- Serves: EB-05\n", "solid-srp", {"EB-05"}))

    def test_practice_ids_reads_both_styles_and_stops_at_heading(self):
        self.assertEqual(practice_ids(CONTRACT), ["tdd", "solid-srp"])

    def test_practice_ids_preserves_invalid_cell(self):
        self.assertEqual(practice_ids(CONTRACT.replace("`tdd`", "INVALID / id")), ["INVALID / id", "solid-srp"])

    def test_practice_ids_without_subsection(self):
        self.assertEqual(practice_ids(CONTRACT.replace("### Practices", "### Other")), [])

    def test_practice_ids_ignores_fenced_table(self):
        self.assertEqual(practice_ids("```\n" + CONTRACT + "```\n"), [])

    def test_index_ignores_serves_and_keeps_repetitions(self):
        row = INDEX.splitlines()[-1]
        self.assertEqual(index_ids(INDEX + row + "\n"), (["solid-srp", "solid-srp"], []))

    def test_index_rejects_malformed_first_cells(self):
        cells = ["solid-srp", "[`solid-srp`](solid-srp.txt)",
                 "[`solid-srp`](https://example.org/solid-srp.md)",
                 "[`solid-srp`](dir/solid-srp.md)", "[`solid-srp`](solid-srp.md#source)",
                 "[`solid-srp`](solid-srp.md) [`tdd`](tdd.md)",
                 "[`wrong`](solid-srp.md)", "[`SOLID_SRP`](SOLID_SRP.md)"]
        for cell in cells:
            with self.subTest(cell=cell):
                ids, errors = index_ids(INDEX.replace("[`solid-srp`](solid-srp.md)", cell))
                self.assertEqual(ids, [])
                self.assertEqual(len(errors), 1)
                self.assertIn("3", errors[0])
                self.assertIn(cell, errors[0])


if __name__ == "__main__":
    unittest.main()
