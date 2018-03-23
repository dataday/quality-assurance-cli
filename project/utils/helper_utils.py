# pylint: disable=missing-docstring
import os
import glob
import logging


def has_changed_directory(path):
    """Changes to the requested directory.
        :param str path: directory path
    """
    if not path == get_current_directory():
        os.chdir(path)
        return True
    return False


def has_win_path_separator():
    """Determines if windows file separators are used
        :return: bool -- true if windows separator, otherwise false
    """
    return True if os.sep == "\\" else False


def replace_path_separator(path):
    """Updates file path to unix separators.
        :param str path: directory path
        :return: str -- directory path (updated separator on windows)
    """
    if has_win_path_separator():
        return str(path).replace("\\", "/").replace("\\\\", "/")
    return path


def is_valid_directory(path):
    """Determines if path is a valid directory.
        :param str path: directory path
        :return: bool
    """
    return os.path.isdir(path)


def is_valid_file(path):
    """Determines if path is a valid file.
        :param str path: file path
        :return: bool
    """
    return os.stat(path)


def is_current_directory(path):
    """Determines if the the target directory path has been changed to.
        :param str path: target directory path
        :return: bool
    """
    return True if path == get_current_directory() else False


def get_basename(path):
    """Gets file base name from path.
        :param str path: file path
        :return: str -- file name
    """
    return os.path.basename(path)


def get_current_directory():
    """Gets the current working directory.
        :return: str -- path to current directory
    """
    return os.getcwd()


def get_real_path(path):
    """Gets a system directories / files real path
        :param str path: directory path
        :return: bool
    """
    return os.path.realpath(path)


def get_file_contents(path):
    """Reads file contents.
        :param str path: file path
        :return: str -- file contents
    """

    file = open(path)
    contents = file.read()
    file.close()

    return contents


def list_directory_contents(path):
    """Gets directory contents with absolute paths.
        :param str path: directory path
        :return: dict -- list of paths
    """
    return glob.glob("{}/*".format(path))


def concat_path(base, path):
    """Concatenates paths.
        :param str base: base directory path
        :param str path: path
        :return: str -- concatenated path
    """
    return "{}/{}".format(
        base,
        path
    )


def log(message):
    """Logs messages.
        :param str message: a message
    """
    logger = logging.getLogger(__name__)
    logger.info(message)
