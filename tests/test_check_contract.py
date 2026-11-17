"""Exercise the opt-in contract check at its real command boundary."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from test_task_contracts import VALID, PROFILE

SOURCE = Path(__file__).resolve().parents[1]
COMMAND = SOURCE / 'validators/check_contract.py'


def run(*args, stdin=None):
    return subprocess.run([sys.executable, str(COMMAND), *args], input=stdin,
                          text=True, capture_output=True)


class ContractCommandTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='radiant-contract-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def file(self, name, text):
        path = self.root / name
        path.write_text(text, encoding='utf-8')
        return str(path)

    def test_path_and_stdin_success(self):
        for result in (run(self.file('contract.md', VALID)), run('-', stdin=VALID)):
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(json.loads(result.stdout), {'template_version': '0.4', 'practices': ['tdd']})
            self.assertEqual(result.stderr, '')
        result = run('-', stdin=VALID.split('\n', 1)[1].split('# 18.')[0])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIsNone(json.loads(result.stdout)['template_version'])

    def test_all_content_errors_exit_1(self):
        result = run('-', stdin=VALID.replace('`REQUIRED`', 'N/A').replace('`tdd`', 'unknown').replace('- [ ] The command refuses invalid input.', ''))
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        errors = json.loads(result.stdout)['errors']
        for term in ('8. Engineering Check: empty', 'unknown practice id: unknown', '12. Acceptance criteria: empty'):
            self.assertTrue(any(term in error for error in errors), errors)
        self.assertEqual(result.stderr, '')

    def test_profile_is_explicit_and_never_opens_card_links(self):
        text = VALID.replace('`tdd`', '[`local-test`](../never-opened/local-test.md)')
        profile = self.file('profile.md', PROFILE)
        result = run('-', '--profile', profile, stdin=text)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)['practices'], ['local-test'])
        result = run('-', stdin=text)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('local-test', result.stdout)

    def test_invalid_profile_ids_are_reported(self):
        result = run('-', '--profile', self.file('profile.md', PROFILE.replace('local-test', 'tdd')), stdin=VALID)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn('Profile / Project practices: catalog practice id: tdd', result.stdout)

    def test_unreadable_sources_name_contract_or_profile(self):
        for name in ('absent.md', 'directory'):
            path = self.root / name
            if name == 'directory':
                path.mkdir()
            for args in ((str(path),), ('-', '--profile', str(path))):
                result = run(*args, stdin=VALID)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn(str(path), json.loads(result.stdout)['errors'][0])
        path = self.root / 'invalid-utf8.md'
        path.write_bytes(b'\xff')
        for args in ((str(path),), ('-', '--profile', str(path))):
            result = run(*args, stdin=VALID)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn(str(path), json.loads(result.stdout)['errors'][0])

    def test_usage_errors_exit_2(self):
        for args in ((), ('-', '--profile'), ('-', '--project', '.'), ('-', 'extra')):
            result = run(*args)
            self.assertEqual(result.returncode, 2)
            self.assertIn('usage:', result.stderr)

    def test_checkout_template_controls_supported_version(self):
        # Numeric comparison must use this checkout's template, not a hardcoded ceiling.
        import shutil
        root = self.root / 'checkout'
        shutil.copytree(SOURCE / 'validators', root / 'validators', ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copytree(SOURCE / 'engineering', root / 'engineering')
        (root / 'templates').mkdir()
        (root / 'templates/task-contract.md').write_text('**Version:** 0.10\\\n', encoding='utf-8')
        result = subprocess.run([sys.executable, str(root / 'validators/check_contract.py'), '-'],
                                input=VALID.replace('0.4', '0.10'), text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)['template_version'], '0.10')


if __name__ == '__main__':
    unittest.main()
