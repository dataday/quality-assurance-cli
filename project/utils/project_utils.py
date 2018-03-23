# pylint: disable=missing-docstring
import sys
import project.utils.helper_utils as utils


QA_LOG_TMPL = "QA-> {}:\nQA-> {}\nQA-> {}"
QA_CODESTYLE_CONFIG_PATH = "data/styles/google.rc"
QA_UNITTEST_CONFIG_PATH = "data/config/.noserc"
QA_COVERAGE_CONFIG_PATH = "data/config/.coveragerc"

def print_directory_contents(path):
    """Prints directory contents.
        :param str path: directory path
        :return: str -- file and directory list
    """
    contents = utils.list_directory_contents(path)
    utils.log(
        QA_LOG_TMPL.format("Directory Contents", path, "\nQA-> ".join(contents))
    )


def print_file_contents(path):
    """Prints file contents.
        :param str path: file path
        :return: str -- contents of the file
    """
    file_path = utils.get_real_path(path)
    contents = utils.get_file_contents(file_path)

    utils.log(
        QA_LOG_TMPL.format("File Contents", file_path, contents)
    )


def create_unittest_command(path, exec_base):
    """Gets unit test command, with or without the configuration option
        :param: str path: target directory path
        :param: str exec_base: execution base path
        :return: str -- formatted command
    """
    command = '"{}" -m nose -v'.format(sys.executable)
    config_path = utils.concat_path(
        utils.get_real_path(exec_base),
        QA_UNITTEST_CONFIG_PATH
    )

    utils.log(
        QA_LOG_TMPL.format("Test Path", path, config_path)
    )

    # add configuration
    if utils.is_valid_file(config_path):
        print_file_contents(config_path)

        result = "{} {} {}".format(
            command,
            "--config",
            # configuration path (unix)
            utils.replace_path_separator(config_path)
        )

        utils.log(
            QA_LOG_TMPL.format("Test CMD", utils.get_current_directory(), result)
        )

        return result

    # omit configuration
    return "{}".format(
        command
    )


def create_codestyle_command(path, exec_base):
    """Gets code style command, with or without configuration option
        :param: str path: target directory path
        :param: str exec_base: execution base path
        :return: str -- formatted command
    """
    command = '"{}" -m  pylint'.format(sys.executable)
    config_path = utils.concat_path(
        utils.get_real_path(exec_base),
        QA_CODESTYLE_CONFIG_PATH
    )

    utils.log(
        QA_LOG_TMPL.format("Style Path", path, config_path)
    )

    # add configuration
    if utils.is_valid_file(config_path):
        print_file_contents(config_path)

        result = "{} {} {} {}".format(
            command,
            "--rcfile",
            # configuration path (unix)
            utils.replace_path_separator(config_path),
            # target path (unix)
            utils.replace_path_separator(path)
        )

        utils.log(
            QA_LOG_TMPL.format("Style CMD", utils.get_current_directory(), result)
        )

        return result

    # omit configuration
    return "{}".format(
        command
    )
