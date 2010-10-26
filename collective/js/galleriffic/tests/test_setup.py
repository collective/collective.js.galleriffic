import unittest
from collective.js.galleriffic.tests.base import TestCase

class TestSetup(TestCase):
    """The name of the class should be meaningful. This may be a class that
    tests the installation of a particular product.
    """

    def test_js_registred(self):
        resources = self.portal.portal_javascripts.getResourcesDict().keys()
        resource = ('++resource++jquery.galleriffic.js',
                    '++resource++jquery.opacityrollover.js',
                    '++resource++jquery.history.js')
        for r in resource:
            self.failUnless(r in resources)

def test_suite():
    """
    """
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
