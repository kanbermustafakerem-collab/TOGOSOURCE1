import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from mymodule.core import greet, add_numbers

class TestCoreFunctions(unittest.TestCase):

    def test_greet_with_name(self):
        self.assertEqual(greet("cmd"), "Hello cmd, welcome to the project!")

    def test_greet_empty(self):
        self.assertEqual(greet(""), "Hello World!")

    def test_add_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)
        self.assertEqual(add_numbers(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()