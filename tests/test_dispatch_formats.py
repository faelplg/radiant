"""Exercise the formats that describe dispatch: requirements, provides, units and routing."""

from pathlib import Path
import sys
import unittest

SOURCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SOURCE / "validators"))

from dispatch_formats import validate_provides  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
