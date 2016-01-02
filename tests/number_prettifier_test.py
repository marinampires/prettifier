import unittest

from prettifier.number_prettifier import prettifier

class TestNumberPrettifier(unittest.TestCase):

  def test_not_numerics_input(self):
    number = "number"
    with self.assertRaises(ValueError):
        prettifier(number)

  def test_number_with_3_digits(self):
    number = 532
    self.assertEqual(number, prettifier(number))

  def test_number_with_6_digits(self):
    number = 149532
    self.assertEqual(number, prettifier(number))
  
  def test_million_number(self):
    number = 1000000
    self.assertEqual("1M", prettifier(number))

  def test_decimal_million_number(self):
    number = 2500000.34
    self.assertEqual("2.5M", prettifier(number))

  def test_billion_number(self):
    number = 120000000000
    self.assertEqual("120B", prettifier(number))

  def test_decimal_billion_number(self):
    number = 1123456789
    self.assertEqual("1.1B", prettifier(number))

  def test_trillion_number(self):
    number = 1000000000000
    self.assertEqual("1T", prettifier(number))

  def test_decimal_trillion_number(self):
    number = 2501123456789
    self.assertEqual("2.5T", prettifier(number))
