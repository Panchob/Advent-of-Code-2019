import unittest
from day3 import *

class TestDay3(unittest.TestCase):
    def setUp(self):
        self.wire1_1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
        self.wire2_1 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
        
        self.wire1_2 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
        self.wire2_2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]


    def test_minDistance(self):
        wire1 = positions(self.wire1_1)
        wire2 = positions(self.wire2_1)
        self.assertEqual(minDistance(wire1, wire2), 159)

        wire1 = positions(self.wire1_2)
        wire2 = positions(self.wire2_2)
        self.assertEqual(minDistance(wire1, wire2), 135)

    def test_minSteps(self):
        wire1 = positions(self.wire1_1)
        wire2 = positions(self.wire2_1)
        self.assertEqual(minSteps(wire1, wire2), 610)

        wire1 = positions(self.wire1_2)
        wire2 = positions(self.wire2_2)
        self.assertEqual(minSteps(wire1, wire2), 410)


if __name__ == '__main__': 
    unittest.main() 