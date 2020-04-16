import unittest
from incode_compiler import compile

class TestDay2(unittest.TestCase):
    def setUp(self):
        self.intcode_1 = [1, 0, 0, 0, 99]
        self.intcode_2 = [2, 3, 0, 3, 99]
        self.intcode_3 = [2, 4, 4, 5, 99, 0]
        self.intcode_4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]


    def test_decode(self):
        self.assertEqual(compile(self.intcode_1), [2, 0, 0, 0, 99])
        self.assertEqual(compile(self.intcode_2), [2, 3, 0, 6, 99])
        self.assertEqual(compile(self.intcode_3), [2, 4, 4, 5, 99, 9801])
        self.assertEqual(compile(self.intcode_4), [30, 1, 1, 4, 2, 5, 6, 0, 99])


if __name__ == '__main__': 
    unittest.main() 