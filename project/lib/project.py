import logging
from project.utils.project_utils import *
from project.lib.process import Process


class Project:
    """ Provides access to command line functionality and utilities """
    def __init__(self, options):
        """Class initialisation with options.
            :param Options options: command line options
        """
        self.options = options
        self.process = Process()
        self.current_path = None
        self.target_path = None
        self.__exec_base = None

        if self.options.known.debug:
            logging.basicConfig(level=logging.INFO)

    def bootstrap(self, exec_base):
        """Bootstraps prior to running
            :param str exec_base: directory path
        """
        self.__exec_base = utils.get_real_path(
            exec_base
        )

    def run_path_option(self):
        """Runs the path option if provided and valid
            :raises ProjectException: raised if the target path is invalid
        """
        option = self.options.known.path

        if option:
            path = utils.get_real_path(option)

            if utils.is_valid_directory(path):

                self.current_path = utils.get_current_directory()

                print_directory_contents(path)

                self.target_path = path

            else:
                raise ProjectException(
                    1,
                    "Error: {}".format(path)
                )

    def run_unittest_option(self):
        """ Runs unit test option if provided and valid """
        option = self.options.known.unittest

        if option and utils.is_valid_directory(self.target_path):

            command = create_unittest_command(
                self.target_path,
                self.__exec_base
            )

            # needed to scope report creation
            changed = utils.has_changed_directory(self.target_path)


            utils.log(QA_LOG_TMPL.format(
                changed,
                self.target_path,
                utils.get_current_directory()
            ))

            self.process.execute(command)

    def run_codestyle_option(self):
        """ Runs code style option if provided and valid """
        option = self.options.known.codestyle

        if option and utils.is_valid_directory(self.target_path):

            command = create_codestyle_command(
                self.target_path,
                self.__exec_base
            )

            try:
                self.process.execute(command)
            except Exception as error:
                utils.log(repr(error))


class ProjectException(Exception):
    """ Describes an exception raised during processing """
    def __init__(self, code, message="Unsupported option"):
        """Class initialisation
            :param int code: error return code
            :param str message: error message
        """
        super().__init__()

        self.code = code
        self.message = message

    def __str__(self):
        """Overrides parse response
            :return: dict -- error
        """
        return repr([self.code, str(self.message)])
