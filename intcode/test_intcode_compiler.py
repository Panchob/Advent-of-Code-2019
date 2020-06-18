import unittest
from intCode_compiler import Intcode

class TestIncode(unittest.TestCase):
    def setUp(self):
        self.intcode_1 = Intcode([1, 0, 0, 0, 99])
        self.intcode_2 = Intcode([2, 3, 0, 3, 99])
        self.intcode_3 = Intcode([2, 4, 4, 5, 99, 0])
        self.intcode_4 = Intcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
        self.intcode_5 = Intcode([1002, 4, 3, 4, 33])
        self.intcode_6 = Intcode([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])
        self.intcode_7 = Intcode([1002, 4, 3, 4, 33])
        self.intcode_8 = Intcode([1002, 4, 3, 4, 33])
        self.intcode_9 = Intcode([1102, 34915192, 34915192, 7, 4, 7, 99, 0])


    def test_run(self):
        self.intcode_1.run(0)
        self.assertEqual(self.intcode_1.code, [2, 0, 0, 0, 99])
        self.intcode_2.run(0)
        self.assertEqual(self.intcode_2.code, [2, 3, 0, 6, 99])
        self.intcode_3.run(0)
        self.assertEqual(self.intcode_3.code, [2, 4, 4, 5, 99, 9801])
        self.intcode_4.run(0)
        self.assertEqual(self.intcode_4.code, [30, 1, 1, 4, 2, 5, 6, 0, 99])
        self.intcode_5.run(0)
        self.assertEqual(self.intcode_5.code, [1002, 4, 3, 4, 99])
        self.assertEqual(self.intcode_9.run(0), 1219070632396864)
    



if __name__ == '__main__': 
    unittest.main() 