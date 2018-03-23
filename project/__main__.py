# pylint: disable=invalid-name
# pylint: disable=missing-docstring
import os
import sys
from .lib import Project
from .lib import Options


def main(args=None):
    """Main entry point"""

    if args is None:
        args = sys.argv

    options = Options()
    options.parse(args[1:])

    # init project
    project = Project(options)

    # assign exec base
    exec_base = os.environ.get("QA_EXEC_BASE", ".")

    # bootstrap project
    project.bootstrap(exec_base)

    # run path option
    project.run_path_option()

    # run code style option
    project.run_codestyle_option()

    # run unit test option
    project.run_unittest_option()

if __name__ == "__main__":
    main(sys.argv)
