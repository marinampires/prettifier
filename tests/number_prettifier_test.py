import unittest

from prettifier.number_prettifier import prettifier

class TestNumberPrettifier(unittest.TestCase):

  def test_number_with_3_digits(self):
    number = 532
    number_prettified = prettifier(number)
    self.assertEqual(number, number_prettified)

  def test_number_with_5_digits(self):
    number = 14532
    number_prettified = prettifier(number)
    self.assertEqual(number, number_prettified)

  def test_not_numerics_input(self):
    number = "number"
    with self.assertRaises(ValueError):
        prettifier(number)
  
  def test_million_number(self):
    number = 1000000
    number_prettified = prettifier(number)
    self.assertEqual("1M", number_prettified)

  def test_decimal_million_number(self):
    number = 2500000.34
    number_prettified = prettifier(number)
    self.assertEqual("2.5M", number_prettified)

  def test_billion_number(self):
    number = 1000000000
    number_prettified = prettifier(number)
    self.assertEqual("1B", number_prettified)

  def test_decimal_billion_number(self):
    number = 1123456789
    number_prettified = prettifier(number)
    self.assertEqual("1.1B", number_prettified)

  def test_trillion_number(self):
    number = 1000000000000
    number_prettified = prettifier(number)
    self.assertEqual("1T", number_prettified)

  def test_decimal_trillion_number(self):
    number = 2501123456789
    number_prettified = prettifier(number)
    self.assertEqual("2.5T", number_prettified)

if __name__ == '__main__':
    unittest.main()
