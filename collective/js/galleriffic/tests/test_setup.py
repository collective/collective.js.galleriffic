import unittest
from collective.js.galleriffic.tests.base import TestCase

class TestSetup(TestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """

    def test_js_registred(self):
        pass

def test_suite():
    """
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
