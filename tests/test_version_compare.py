"""
    1. Compile test_version_compare.cpp
    2. Execute the version test.
    3. If exit_code == 0, success
    4. else fail.
"""
import unittest
import subprocess
from os.path import join, dirname, exists


class TestVersionCompare(unittest.TestCase):
    def setUp(self):
        pass

    def test_version_compare_compile(self):
        file = join(dirname(__file__), "bin", "test_version.bin")
        src = join(dirname(__file__), "test_version_compare.cpp")
        assert exists(src), "missing source file"
        cmd = ["g++", "-o", file, src]
        print("processing {}".format(cmd))
        assert subprocess.run(cmd).returncode == 0, "Compile command failed."
        assert exists(file), "missing target file"

    def test_version_compare_execute(self):
        file = join(dirname(__file__), "bin", "test_version.bin")
        src = join(dirname(__file__), "test_version_compare.cpp")
        assert exists(src), "missing source file"
        cmd = ["g++", "-o", file, src]
        print("processing {}".format(cmd))
        assert subprocess.run(cmd).returncode == 0, "Compile command failed."
        assert exists(file), "missing target file"
        cmd = [file]
        assert subprocess.run(cmd).returncode == 0, "compile failed."
