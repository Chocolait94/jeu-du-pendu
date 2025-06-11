import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest

from modules import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_non_multiple_of_three_or_five(self):
        self.assertEqual(fizzbuzz.fizzbuzz(2), "2")

    def test_multiple_of_three(self):
        self.assertEqual(fizzbuzz.fizzbuzz(6), "Fizz")

    def test_multiple_of_five(self):
        self.assertEqual(fizzbuzz.fizzbuzz(10), "Buzz")

    def test_multiple_of_three_and_five(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
