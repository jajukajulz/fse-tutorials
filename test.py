# usage - python test.py
# demonstrates use of inbuilt Python unittest library

import unittest

# recall that ideally a function should have a single purpose 
# i.e. SRP - single responsibility purpose
def add(num_a, num_b):
    return num_a + num_b

def do_nothing(n):
    return None


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers_fail(self):
        self.assertEqual(add(1, 2), 4)

    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

    def test_do_nothing_return_none(self):
        self.assertIsNone(do_nothing(), None)

if __name__ == '__main__':
    unittest.main()