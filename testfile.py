import unittest
from test import generate_odd_numbers

class TestGenerateOddNumbers(unittest.TestCase):
    def test_generate_odd_numbers(self):
        expected_odd_numbers = list(range(1, 101, 2))
        self.assertEqual(generate_odd_numbers(), expected_odd_numbers)

if __name__ == '__main__':
    unittest.main()