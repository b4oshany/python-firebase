import unittest
import re
import os
import sys

google_appengine = re.search('/[^:]*/google_appengine', os.environ["PATH"])
if google_appengine:
    google_appengine = google_appengine.group()
else:
    raise Exception('No google_appengine path was found')

sys.path.insert(1, google_appengine)
sys.path.insert(1, '{}/lib/yaml/lib'.format(google_appengine))


from .jsonutil_test import JSONTestCase
from .firebase_test import FirebaseTestCase
from .gae_test import FireAppEngineTestCase


def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(JSONTestCase))
    suite.addTest(unittest.makeSuite(FirebaseTestCase))
    suite.addTest(unittest.makeSuite(FireAppEngineTestCase))
    return suite
