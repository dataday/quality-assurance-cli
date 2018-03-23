# pylint: disable=invalid-name
# pylint: disable=missing-docstring
import os
from nose.core import TestProgram

os.chdir(os.path.abspath(os.path.dirname(__file__)))

TestProgram()
