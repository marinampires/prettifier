import unittest

from prettifier.number_prettifier import prettifier

class TestNumberPrettifier(unittest.TestCase):

  def test_validate_number_with_3_digits(self):
    number = 532
    number_prettified = prettifier(number)
    self.assertEqual(number, number_prettified)

  def test_validate_number_with_5_digits(self):
    number = 14532
    number_prettified = prettifier(number)
    self.assertEqual(number, number_prettified)

  def test_validate_not_numerics_input(self):
    number = "number"
    with self.assertRaises(ValueError):
        prettifier(number)
  
  #def validate_million_number(self):

  #def validate_decimal_number_not_integer(self):

if __name__ == '__main__':
    unittest.main()
