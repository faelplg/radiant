"""Exercise contract rules on minimal text, independent of the shared form."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'validators'))
from task_contracts import validate_contract

VALID = """**Template version:** `0.4`
# 8. Engineering Check
| Baseline | Status | Application | Evidence |
| --- | --- | --- | --- |
| EB-03 Tests | `REQUIRED` | Behavior | Tests |
### Practices
| Practice | Serves |
| --- | --- |
| `tdd` | EB-03 |
# 12. Acceptance criteria
- [ ] The command refuses invalid input.
# 18. Owner decisions
None.
"""
PROFILE = """## Project practices
| Id | Card |
| --- | --- |
| local-test | never-opened.md |
"""
BASELINE = {'EB-01', 'EB-03'}
CATALOG = {'tdd', 'test-strategy'}
GENERIC = (
    'all applicable checks in section 11 pass',
    'there was no change outside the Allowed scope',
    'relevant limitations are recorded',
    'the final evidence was read, not just presumed from the exit code',
)


class ContractRuleTests(unittest.TestCase):
    def check(self, text=VALID, profile=None, latest='0.4'):
        return validate_contract(text, BASELINE, CATALOG, latest, profile)

    def refuses(self, text, message, **kwargs):
        errors = self.check(text, **kwargs)[1]
        self.assertTrue(any(message in error for error in errors), errors)

    def test_valid_and_level_two_sections(self):
        self.assertEqual(self.check(), ({'template_version': '0.4', 'practices': ['tdd']}, []))
        self.assertEqual(self.check(VALID.replace('\n# ', '\n## '))[1], [])

    def test_missing_sections(self):
        for section in ('8. Engineering Check', '12. Acceptance criteria', '18. Owner decisions'):
            with self.subTest(section=section):
                self.refuses(VALID.replace('# ' + section, '# Other'), 'missing section: ' + section)

    def test_repeated_sections_and_practices(self):
        for section in ('8. Engineering Check', '12. Acceptance criteria', '18. Owner decisions'):
            self.refuses(VALID + '\n## ' + section + '\nNone.\n', 'repeated heading: ' + section)
        self.refuses(VALID.replace('# 12.', '### Practices\n# 12.'), 'repeated heading: 8. Engineering Check / Practices')

    def test_baseline_rows(self):
        for status in ('REQUIRED', 'APPLICABLE', '`REQUIRED`', '`APPLICABLE`'):
            self.assertEqual(self.check(VALID.replace('`REQUIRED`', status))[1], [])
        for ident in ('EB-99', 'bad', '../tdd'):
            self.refuses(VALID.replace('EB-03 Tests', ident), '8. Engineering Check: unknown baseline id: ' + ident)
        for status in ('REQUIRED / N/A', '', 'required'):
            self.refuses(VALID.replace('`REQUIRED`', status), '8. Engineering Check: EB-03: invalid status')
        row = '| EB-03 Tests | `REQUIRED` | Behavior | Tests |\n'
        self.refuses(VALID.replace(row, row * 2), 'repeated baseline id: EB-03')

    def test_empty_engineering_and_subsection_boundary(self):
        for text in (VALID.replace('`REQUIRED`', '`N/A`'), VALID.replace('| EB-03 Tests | `REQUIRED` | Behavior | Tests |', ''),
                     VALID.replace('| EB-03 Tests', '### Other\n| EB-03 Tests')):
            self.refuses(text, '8. Engineering Check: empty')
        self.assertEqual(self.check(VALID.replace('### Practices', '### N/A justification\nNo explanation required.\n### Practices'))[1], [])

    def test_practices_optional_but_not_empty(self):
        start, tail = VALID.split('### Practices')
        acceptance = '# 12.' + tail.split('# 12.', 1)[1]
        self.assertEqual(self.check(start + acceptance)[0]['practices'], [])
        self.assertEqual(self.check(start + acceptance)[1], [])
        self.refuses(VALID.replace('| `tdd` | EB-03 |', ''), '8. Engineering Check / Practices: empty')

    def test_practice_cells(self):
        for cell in ('tdd', '`tdd`', '[`tdd`](../cards/tdd.md)', '[`tdd`](tdd.md)', '[`tdd`](../cards:local/tdd.md)'):
            self.assertEqual(self.check(VALID.replace('`tdd`', cell))[1], [])
        for cell in ('', '../tdd', '`bad id`', '[tdd](tdd.md)', '[`tdd`](wrong.md)',
                     '[`tdd`](https://host/tdd.md)', '[`tdd`](/tdd.md)', '[`tdd`](//host/tdd.md)',
                     '[`tdd`](tdd.md?q)', '[`tdd`](tdd.md#source)', '[`tdd`](file:tdd.md)'):
            with self.subTest(cell=cell):
                self.refuses(VALID.replace('`tdd`', cell), 'invalid practice cell: ' + repr(cell))

    def test_unknown_repeated_and_ordered_practices(self):
        self.refuses(VALID.replace('`tdd`', '`unknown`'), '8. Engineering Check / Practices: unknown practice id: unknown')
        self.refuses(VALID.replace('| `tdd` | EB-03 |', '| `tdd` | EB-03 |\n| tdd | EB-03 |'), 'repeated practice id: tdd')
        text = VALID.replace('| `tdd` | EB-03 |', '| test-strategy | EB-03 |\n| tdd | EB-03 |')
        self.assertEqual(self.check(text)[0]['practices'], ['test-strategy', 'tdd'])

    def test_profile_ids(self):
        text = VALID.replace('`tdd`', 'local-test')
        for profile in (PROFILE, PROFILE.replace('local-test', '`local-test`')):
            self.assertEqual(self.check(text, profile=profile)[1], [])
        self.refuses(text, 'unknown practice id: local-test', profile='## Commands\nNothing.\n')
        self.assertEqual(self.check(profile='## Commands\nNothing.\n')[1], [])
        for ident, message in (('../local', 'invalid practice id'), ('BAD', 'invalid practice id'), ('tdd', 'catalog practice id')):
            self.refuses(VALID, 'Profile / Project practices: ' + message + ': ' + ident,
                         profile=PROFILE.replace('local-test', ident))
        self.refuses(VALID, 'Profile / Project practices: repeated practice id: local-test',
                     profile=PROFILE + '| local-test | other.md |\n')
        self.refuses(text, 'unknown practice id: local-test', profile=PROFILE.replace('## Project practices', '## Other'))
        bounded = PROFILE + '## Other\n| Id | Card |\n| --- | --- |\n| tdd | ignored |\n'
        self.assertEqual(self.check(text, profile=bounded)[1], [])

    def test_acceptance_checklists_and_normalization(self):
        for marker in ('[ ]', '[x]', '[X]'):
            self.assertEqual(self.check(VALID.replace('[ ]', marker))[1], [])
        for item in ('', 'ordinary prose', '- [ ] `[observable criterion]`;', '- [x] [another placeholder].',
                     '\n'.join('- [ ] ' + item + ';' for item in GENERIC)):
            self.refuses(VALID.replace('- [ ] The command refuses invalid input.', item), '12. Acceptance criteria: empty')
        self.assertEqual(self.check(VALID.replace('# 18.', '### Notes\nText.\n# 18.'))[1], [])
        self.refuses(VALID.replace('- [ ] The command refuses invalid input.', '### Notes\n# Other\n- [ ] Outside.'), '12. Acceptance criteria: empty')

    def test_owner_decisions_and_exemption(self):
        for version in ('0.0', '0.3'):
            self.assertEqual(self.check(VALID.replace('0.4', version).split('# 18.')[0])[1], [])
        absent = VALID.split('\n', 1)[1].split('# 18.')[0]
        self.assertEqual(self.check(absent), ({'template_version': None, 'practices': ['tdd']}, []))
        for body in ('', '   ', '**`[YYYY-MM-DD]`:** Decide.'):
            self.refuses(VALID.replace('None.', body), '18. Owner decisions', latest='0.4')
        self.refuses(VALID.split('# 18.')[0], 'template version 0.4')
        self.assertEqual(self.check(VALID.replace('None.', 'Owner approved the boundary.'))[1], [])

    def test_numeric_versions_and_value_as_written(self):
        for version in ('bad', '0', '0.4.0', 'v0.4', ''):
            self.refuses(VALID.replace('`0.4`', '`' + version + '`'), 'Template version: malformed')
        self.refuses(VALID.replace('0.4', '0.10'), 'Template version: unsupported')
        self.refuses(VALID.replace('0.4', '1.0'), 'Template version: unsupported')
        self.assertEqual(self.check(VALID.replace('0.4', '0.10'), latest='0.10')[1], [])
        self.refuses(VALID.replace('0.4', '0.10').split('# 18.')[0], '18. Owner decisions', latest='0.10')
        self.assertEqual(self.check(VALID.replace('`0.4`', '00.04'))[0]['template_version'], '00.04')

    def test_fences_ignore_headings_rows_items_and_metadata(self):
        for fence in ('```', '~~~~', '   ```'):
            hidden = fence + '\n' + VALID + fence.strip() + '\n'
            self.assertEqual(self.check(VALID + hidden)[1], [])
            self.refuses(hidden, 'missing section: 8. Engineering Check')
            self.refuses(VALID.replace('- [ ] The command refuses invalid input.', fence + '\n- [ ] Hidden.\n' + fence), '12. Acceptance criteria: empty')
            self.refuses(VALID.replace('| EB-03 Tests | `REQUIRED` | Behavior | Tests |', fence + '\n| EB-03 Tests | REQUIRED | Behavior | Tests |\n' + fence), '8. Engineering Check: empty')
        self.assertEqual(self.check(VALID + '```\n# 8. Engineering Check\n')[1], [])
        self.refuses(VALID.replace('None.', '```\nNone.\n```'), '18. Owner decisions')
        self.assertEqual(self.check(profile='```\n' + PROFILE + '```\n')[1], [])

    def test_all_errors_are_returned(self):
        errors = self.check('')[1]
        self.assertTrue(any('8. Engineering Check' in error for error in errors))
        self.assertTrue(any('12. Acceptance criteria' in error for error in errors))


if __name__ == '__main__':
    unittest.main()
