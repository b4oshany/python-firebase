import unittest

import sys
sys.path.insert(1, '/home/ubuntu/google_appengine')
sys.path.insert(1, '/home/ubuntu/google_appengine/lib/yaml/lib')


from .jsonutil_test import JSONTestCase
from .firebase_test import FirebaseTestCase
from .gae_test import FireAppEngineTestCase


def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(JSONTestCase))
    suite.addTest(unittest.makeSuite(FirebaseTestCase))
    # suite.addTest(unittest.makeSuite(FireAppEngineTestCase))
    return suite
