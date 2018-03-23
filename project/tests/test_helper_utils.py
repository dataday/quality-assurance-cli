# pylint: disable=missing-docstring
import unittest
from unittest import mock


class TestHelperUtils(unittest.TestCase):
    """ TestHelperUtils """
    def setUp(self):
        patcher = mock.patch("project.utils.helper_utils", autospec=True)
        self.addCleanup(patcher.stop)
        self.utils_mock = patcher.start()

    def __mock_response(self, obj, value):
        """Mocks response object during tests"""
        obj.return_value = value
        return obj

    def test_is_valid_directory_is_callable(self):
        method = self.utils_mock.is_valid_directory
        method("path/to/directory")
        method.assert_called_once_with("path/to/directory")

    def test_is_valid_directory_returns_true(self):
        method = self.__mock_response(self.utils_mock.is_valid_directory, True)
        self.assertTrue(method("path/to/directory"))

    def test_is_valid_directory_returns_false(self):
        method = self.__mock_response(self.utils_mock.is_valid_directory, False)
        self.assertFalse(method("path/to/directory"))

    def test_is_valid_file_is_callable(self):
        method = self.utils_mock.is_valid_file
        method("path/to/file")
        method.assert_called_once_with("path/to/file")

    def test_is_valid_file_returns_true(self):
        method = self.__mock_response(self.utils_mock.is_valid_file, True)
        self.assertTrue(method("path/to/file"))

    def test_is_valid_file_returns_false(self):
        method = self.__mock_response(self.utils_mock.is_valid_file, False)
        self.assertFalse(method("path/to/file"))

    def test_has_changed_directory_is_callable(self):
        method = self.utils_mock.has_changed_directory
        method("path/to/directory")
        method.assert_called_once_with("path/to/directory")

    def test_has_changed_directory_returns_true(self):
        method = self.__mock_response(self.utils_mock.has_changed_directory, True)
        self.assertTrue(method("path/to/directory"))

    def test_has_changed_directory_returns_false(self):
        method = self.__mock_response(self.utils_mock.has_changed_directory, False)
        self.assertFalse(method("path/to/directory"))

    def test_is_current_directory_is_callable(self):
        method = self.utils_mock.is_current_directory
        method("path/to/directory")
        method.assert_called_once_with("path/to/directory")

    def test_is_current_directory_should_return_true(self):
        method = self.__mock_response(self.utils_mock.is_current_directory, True)
        self.assertTrue(method("path/to/directory"))

    def test_is_current_directory_should_return_false(self):
        method = self.__mock_response(self.utils_mock.is_current_directory, False)
        self.assertFalse(method("path/to/directory"))

    def test_has_win_path_separator_is_callable(self):
        method = self.utils_mock.has_win_path_separator
        method()
        method.assert_called_once_with()

    def test_has_win_path_separator_should_return_true(self):
        method = self.__mock_response(self.utils_mock.has_win_path_separator, True)
        self.assertTrue(method())

    def test_has_win_path_separator_should_return_false(self):
        method = self.__mock_response(self.utils_mock.has_win_path_separator, False)
        self.assertFalse(method())

    def test_get_basename_is_callable(self):
        method = self.utils_mock.get_basename
        method("path/to/file.suffix")
        method.assert_called_once_with("path/to/file.suffix")

    def test_get_basename_should_return_file_name(self):
        method = self.__mock_response(self.utils_mock.get_basename, "file.suffix")
        self.assertEqual(method("path/to/file.suffix"), "file.suffix")

    def test_get_basename_should_return_dotfile_name(self):
        method = self.__mock_response(self.utils_mock.get_basename, ".dotfile")
        self.assertEqual(method("path/to/.dotfile"), ".dotfile")

    def test_get_real_path_is_callable(self):
        method = self.utils_mock.get_real_path
        method("path/to/resource")
        method.assert_called_once_with("path/to/resource")

    def test_get_real_path_should_return_path(self):
        method = self.__mock_response(self.utils_mock.get_real_path, "/real/path/to/resource")
        self.assertEqual(method("path/to/resource"), "/real/path/to/resource")

    def test_get_real_path_should_not_return_path(self):
        method = self.__mock_response(self.utils_mock.get_real_path, None)
        self.assertEqual(method("path/to/resource"), None)

    def test_get_current_directory_is_callable(self):
        method = self.utils_mock.get_current_directory
        method()
        method.assert_called_once_with()

    def test_get_current_directory_should_return_path(self):
        method = self.__mock_response(self.utils_mock.get_current_directory, "path/to/current")
        self.assertEqual(method(), "path/to/current")

    def test_get_current_directory_should_not_return_path(self):
        method = self.__mock_response(self.utils_mock.get_current_directory, None)
        self.assertEqual(method(), None)

    def test_list_directory_contents_is_callable(self):
        method = self.utils_mock.list_directory_contents
        method("path/to/directory")
        method.assert_called_once_with("path/to/directory")

    def test_list_directory_contents_should_return_contents(self):
        fixture = ["/path/to/file.suffix", "/path/to/directory"]
        method = self.__mock_response(self.utils_mock.list_directory_contents, fixture)
        self.assertEqual(method("path/to/directory"), fixture)

    def test_get_file_contents_should_not_return_path(self):
        method = self.__mock_response(self.utils_mock.get_current_directory, None)
        self.assertEqual(method(), None)

    def test_get_file_contents_is_callable(self):
        method = self.utils_mock.get_file_contents
        method("path/to/file")
        method.assert_called_once_with("path/to/file")

    def test_get_file_contents_should_return_contents(self):
        fixture = "file contents"
        method = self.__mock_response(self.utils_mock.get_file_contents, fixture)
        self.assertEqual(method("path/to/file"), fixture)

    def test_concat_path_is_callable(self):
        method = self.utils_mock.concat_path
        method("path/to/base", "path/to/resource")
        method.assert_called_once_with("path/to/base", "path/to/resource")

    def test_concat_path_should_return_path(self):
        fixture = "path/to/base/path/to/resource"
        method = self.__mock_response(self.utils_mock.concat_path, fixture)
        self.assertEqual(method("path/to/base", "path/to/resource"), fixture)
