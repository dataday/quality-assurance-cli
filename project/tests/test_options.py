# pylint: disable=missing-docstring
import unittest
from project.lib import Options


class TestOptions(unittest.TestCase):
    """ TestOptions """
    def setUp(self):
        self.options = Options()

    def test_path_default_option_is_set(self):
        self.options.parse()
        self.assertEqual(self.options.known.path, ".")

    def test_unittest_default_option_is_set(self):
        self.options.parse()
        self.assertFalse(self.options.known.unittest)

    def test_codestyle_default_option_is_set(self):
        self.options.parse()
        self.assertFalse(self.options.known.codestyle)

    def test_debug_default_option_is_set(self):
        self.options.parse()
        self.assertFalse(self.options.known.debug)

    def test_set_path_option(self):
        self.options.parse(["-p", "/path/to/directory"])
        self.assertEqual(self.options.known.path, "/path/to/directory")
        self.options.parse(["--path", "/path/to/directory"])
        self.assertEqual(self.options.known.path, "/path/to/directory")

    def test_set_codestyle_option(self):
        self.options.parse(["-s"])
        self.assertTrue(self.options.known.codestyle)
        self.options.parse(["--codestyle"])
        self.assertTrue(self.options.known.codestyle)

    def test_set_unittest_option(self):
        self.options.parse(["-t"])
        self.assertTrue(self.options.known.unittest)
        self.options.parse(["--unittest"])
        self.assertTrue(self.options.known.unittest)

    def test_set_debug_option(self):
        self.options.parse(["-d"])
        self.assertTrue(self.options.known.debug)
        self.options.parse(["--debug"])
        self.assertTrue(self.options.known.debug)



if __name__ == "__main__":
    unittest.main()
