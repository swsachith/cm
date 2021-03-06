"""
A convenient method to execute shell commands and return their output. Note: that this method requires that the
command be completely execute before the output is returned. FOr many activities in cloudmesh this is sufficient.
"""
import errno
import glob
import os
import subprocess
import sys
import zipfile

from typing import Union
from pipes import quote
from sys import platform

from cm4.common.console import Console
from cm4.common.util import path_expand
from distutils.spawn import find_executable
import textwrap
from sys import platform


class SystemPath(object):

    @staticmethod
    def add(path):
        if platform == "darwin":
            script = """
            echo \"export PATH={path}:$PATH\" >> ~/.bash_profile
            source ~/.bash_profile
            """.format(path=path)
        elif platform == "linux":
            script = """
            echo \"export PATH={path}:$PATH\" >> ~/.bashrc
            source ~/.bashrc
            """.format(path=path)
        elif platform == "windows":
            script = None
            # TODO: BUG: Implement
        installer = Script(script)


class Script(object):

    def __init__(self, script):
        if script is not None:
            self.run(script)

    def run(self, script):
        lines = textwrap.dedent(script).strip().split("\n")
        print("===============")
        print(lines)
        print("===============")
        for line in lines:
            r = subprocess.check_output(line, shell=True)
            print(r)
