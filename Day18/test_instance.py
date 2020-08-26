import unittest
from Instance import *
from day18 import *

class TestInstance(unittest.TestCase):
    
    def setUp(self):
        graph = createGraphFromString("#########\n#b.A.@.a#1111111111`11111111111111111q11\n#########\n")
        self.instance1 = Instance(graph)
        
    def testListAvailableElementsFromPosition(self):
        pos = self.instance1.getCurrentPosition()
        self.assertEqual(self.instance1.listAvailableElementsFromPosition(pos), ['a','A'])

    def testGenerateAllPossiblePath(self):
        for p in self.instance1.generateAllPossiblePath():
            print(p)

    def testNbStepTo(self):
        pos = self.instance1.getCurrentPosition()
        self.assertEqual(self.instance1.nbStepTo('a', pos), 2)


        
if __name__ == "__main__":
    unittest.main()
