# pylint: disable=missing-docstring
import unittest
from unittest import mock
from project.lib import ProcessException


class TestProcess(unittest.TestCase):
    """ TestProcess """
    def setUp(self):
        self.patcher = mock.patch("project.lib.process")
        self.process_mock = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_should_execute_successfully(self):
        self.process_mock.execute.return_value = "value\n"
        self.assertEqual(self.process_mock.execute("echo value"), "value\n")

    def test_should_raise_exception_with_invalid_reference(self):
        method = self.process_mock.execute
        method.side_effect = ProcessException(1, "error")
        self.assertRaises(ProcessException, method, "/path/to/invalid/resource")

    def test_should_raise_exception_with_default_message(self):
        method = self.process_mock.execute
        method.side_effect = ProcessException(1)
        self.assertRaisesRegex(
            ProcessException,
            repr([1, "Unsupported option"]),
            method,
            "/path/to/exception"
        )

    # docs.python.org/3.5/library/unittest.html#unittest.TestCase.assertRaisesRegex
    def test_should_raise_exception_from_return_code(self):
        method = self.process_mock.execute
        method.side_effect = ProcessException(1)
        self.assertRaisesRegex(ProcessException, "1", method, "sh -c 'return 1'")


if __name__ == "__main__":
    unittest.main()
