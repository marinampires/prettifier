#!/usr/bin/env python
import unittest
from tests.number_prettifier_test import TestNumberPrettifier

testLoad = unittest.TestLoader()
testSuite = testLoad.loadTestsFromTestCase(TestNumberPrettifier)
newSuite = unittest.TestSuite(testSuite)

if __name__ == '__main__':
    unittest.main()
