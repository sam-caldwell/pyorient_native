"""
    This file contains a test to load pyorient_native
    created by Sam Caldwell <mail@samcaldwell.net>
"""
import unittest


class TestPyorientNativeLoad(unittest.TestCase):
    def setUp(self):
        pass

    def test_module_load(self):
        try:
            import pyorient_native
            assert True
        except Exception as e:
            assert False, "failed to load pyorient_native,  {}".format(e)
