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

  #def test_decimal_million_number(self):

if __name__ == '__main__':
    unittest.main()
