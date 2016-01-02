import unittest
from tests.prettifier_test import TestPrettify

testLoad = unittest.TestLoader()
testSuite = testLoad.loadTestsFromTestCase(TestPrettify)
newSuite = unittest.TestSuite(testSuite)

if __name__ == '__main__':
    unittest.main()
