from argparse import ArgumentParser


class Options:
    """ Parses command line arguments """
    def __init__(self):
        """Class initialisation
            .. document private functions
            .. automethod:: __init_parser
        """
        self.known = None
        self.unknown = None
        self.script_name = "project"
        self.__init_parser()

    def __init_parser(self):
        """ Initiates parser: https://docs.python.org/3/library/argparse.html """
        options = "[--path path/to/directory --unittest --codestyle --debug]"
        usage = "{} {}".format(self.script_name, options)

        self.parser = ArgumentParser(
            description="Quality Assurance CLI",
            usage=usage
        )

        # capture target path
        self.parser.add_argument(
            "-p",
            "--path",
            default=".",
            type=str,
            dest="path",
            help="Project directory, defaults to: '.'"
        )

        # capture unit test flag
        self.parser.add_argument(
            "-t",
            "--unittest",
            action="store_true",
            dest="unittest",
            help="Add unit test validation"
        )

        # capture code style flag
        self.parser.add_argument(
            "-s",
            "--codestyle",
            action="store_true",
            dest="codestyle",
            help="Add code style validation"
        )

        # capture debug flag
        self.parser.add_argument(
            "-d",
            "--debug",
            action="store_true",
            dest="debug",
            help="Enable debug"
        )

    def parse(self, args=None):
        """Parses known command line arguments, unknown arguments
            are ignored as warnings
            :param None or list args: command line arguments
        """
        self.known, self.unknown = self.parser.parse_known_args(args)[:]
        if self.unknown:
            print("WARNING: Unknown argument - {}".format(repr(self.unknown)))
