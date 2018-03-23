# pylint: disable=missing-docstring
import unittest
from unittest import mock
from project.lib import ProjectException


class TestProject(unittest.TestCase):
    """ TestProject """
    def setUp(self):
        self.patcher = mock.patch("project.lib.project")
        self.project_mock = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_should_execute_successfully(self):
        self.project_mock.process.execute.return_value = "value\n"
        self.assertEqual(self.project_mock.process.execute("echo value"), "value\n")

    def test_should_raise_exception_with_invalid_reference(self):
        method = self.project_mock.process.execute
        method.side_effect = ProjectException(1, "error")
        self.assertRaises(ProjectException, method, "/path/to/invalid/resource")

    def test_should_raise_exception_with_default_message(self):
        method = self.project_mock.process.execute
        method.side_effect = ProjectException(1)
        self.assertRaisesRegex(
            ProjectException,
            repr([1, "Unsupported option"]),
            method,
            "/path/to/exception"
        )

if __name__ == "__main__":
    unittest.main()
