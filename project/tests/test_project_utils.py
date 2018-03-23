# pylint: disable=missing-docstring
import unittest
from unittest import mock


class TestProjectUtils(unittest.TestCase):
    """ TestProjectUtils """
    def setUp(self):
        patcher = mock.patch("project.utils.project_utils", autospec=True)
        self.addCleanup(patcher.stop)
        self.utils_mock = patcher.start()

    def __mock_response(self, obj, value):
        """Mocks response object during tests"""
        obj.return_value = value
        return obj

    def test_print_directory_contents_is_callable(self):
        method = self.utils_mock.print_directory_contents
        method("path/to/directory")
        method.assert_called_once_with("path/to/directory")

    def test_print_directory_contents_should_print_contents(self):
        fixture = """
        /path/to/file.suffix
        /path/to/directory
        """
        method = self.__mock_response(self.utils_mock.print_directory_contents, fixture)
        self.assertEqual(method("path/to/directory"), fixture)

    def test_print_file_contents_is_callable(self):
        method = self.utils_mock.print_file_contents
        method("path/to/file")
        method.assert_called_once_with("path/to/file")

    def test_print_file_contents_should_print_contents(self):
        fixture = "file contents"
        method = self.__mock_response(self.utils_mock.print_directory_contents, fixture)
        self.assertEqual(method("path/to/file"), fixture)

    def test_create_unittest_command_is_callable(self):
        method = self.utils_mock.create_unittest_command
        method("path/to/target", "path/to/base")
        method.assert_called_once_with("path/to/target", "path/to/base")

    def test_create_unittest_command_with_configuration(self):
        fixture = "python -m nose -v --config /path/to/config /path/to/directory"
        method = self.__mock_response(self.utils_mock.create_unittest_command, fixture)
        self.assertEqual(method("path/to/target", "path/to/base"), fixture)

    def test_create_unittest_command_without_configuration(self):
        fixture = "python -m nose -v"
        method = self.__mock_response(self.utils_mock.create_unittest_command, fixture)
        self.assertEqual(method("path/to/target", "path/to/base"), fixture)

    def test_create_codestyle_command_is_callable(self):
        method = self.utils_mock.create_unittest_command
        method("path/to/target", "path/to/base")
        method.assert_called_once_with("path/to/target", "path/to/base")

    def test_create_ucodestyle_command_with_configuration(self):
        fixture = "python -m pylint --rcfile path/to/base/config path/to/target"
        method = self.__mock_response(self.utils_mock.create_codestyle_command, fixture)
        self.assertEqual(method("path/to/target", "path/to/base"), fixture)

    def test_create_codestyle_command_without_configuration(self):
        fixture = "python -m pylint"
        method = self.__mock_response(self.utils_mock.create_codestyle_command, fixture)
        self.assertEqual(method("path/to/target", "path/to/base"), fixture)
