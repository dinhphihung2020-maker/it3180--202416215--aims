import unittest
from aims.discount import calculate_discount


class TestDiscount(unittest.TestCase):

    def test_discount_20_percent(self):
        self.assertEqual(calculate_discount(100, 20), 80)

    def test_invalid_percent(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)


if __name__ == "__main__":
    unittest.main()