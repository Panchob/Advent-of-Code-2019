import unittest
from day4 import isValidPassword, isValidPasswordWithMatchingRule


class TestDay4(unittest.TestCase):
    def setUp(self):
        self.password1 = [1, 1, 1, 1, 1, 1]
        self.password2 = [2, 2, 3, 4, 5, 0]
        self.password3 = [1, 2, 3, 7, 8, 9]
        self.password4 = [1, 1, 2, 2, 3, 3]
        self.password5 = [1, 2, 3, 4, 4, 4]
        self.password6 = [1, 1, 1, 1, 2, 2]

    def test_isValidPassword(self):
        self.assertTrue(isValidPassword(self.password1))
        self.assertFalse(isValidPassword(self.password2))
        self.assertFalse(isValidPassword(self.password3))

    def test_isValidPasswordWithMatchingRule(self):
        self.assertTrue(isValidPasswordWithMatchingRule(self.password4))
        self.assertFalse(isValidPasswordWithMatchingRule(self.password5))
        self.assertTrue(isValidPasswordWithMatchingRule(self.password6))


if __name__ == '__main__':
    unittest.main()
