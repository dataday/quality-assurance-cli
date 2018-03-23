import subprocess
import shlex


class Process:
    """ Executes commands within a new process """
    def __init__(self):
        pass

    def execute(self, command):
        """Executes command processes and responds with success or error results.
            :param str command: requested command
            :return: str -- result of command execution
            :raises: ProcessException: command processing exception
        """
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        result, error = process.communicate()

        if process.returncode:
            print(result, error)
            raise ProcessException(process.returncode)

        return result


class ProcessException(Exception):
    """ Describes the exception raised during processing """
    def __init__(self, code, message="Command execution failed"):
        """Class initialisation
            :param int code: error return code
            :param mixed message: error message
        """
        super().__init__()

        self.code = code
        self.message = message

    def __str__(self):
        """Override parse response more effectively
            :return: dict -- error
        """
        return repr([self.code, str(self.message)])
