import unittest
from intCode_compiler import compile

class TestDay5(unittest.TestCase):
    def setUp(self):
        self.intcode_1 = [1, 0, 0, 0, 99]
        self.intcode_2 = [2, 3, 0, 3, 99]
        self.intcode_3 = [2, 4, 4, 5, 99, 0]
        self.intcode_4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        self.intcode_5 = [1002, 4, 3, 4, 33]


    def test_compile(self):
        self.assertEqual(compile(self.intcode_1, 1), [2, 0, 0, 0, 99])
        self.assertEqual(compile(self.intcode_2, 1), [2, 3, 0, 6, 99])
        self.assertEqual(compile(self.intcode_3, 1), [2, 4, 4, 5, 99, 9801])
        self.assertEqual(compile(self.intcode_4, 1), [30, 1, 1, 4, 2, 5, 6, 0, 99])
        self.assertEqual(compile(self.intcode_5, 1), [1002, 4, 3, 4, 99])



if __name__ == '__main__': 
    unittest.main() 