import unittest
from day18 import *

class testAStar(unittest.TestCase):
    def setUp(self):
        self.graph1 = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        self.position1 = getCurrentPosition(self.graph1)
        self.keysAndDoors1 = listAvailableElementsFromPosition(self.graph1, self.position1, 0)
        self.paths1 = generateAllPossiblePath(self.keysAndDoors1)
        
    def testCreateGraphFromString(self):
        self.assertEqual(len(self.graph1), 3)
        self.assertEqual(len(self.graph1[0]), 9)
    
    def testGetCurrentPosition(self):
        self.assertEqual(self.position1, (1,5))
    
    def testListAvailableElementsFromPosition(self):
        self.assertEqual(len(self.keysAndDoors1), 2)

    def testGenerateAllPossiblePath(self):
        pass
        # self.assertEqual(self.paths1)
    
    def testValidatePath(self):
        pass
        #self.assertEqual(validatePath(self.paths1), False)
        
    def testGenerateAllNodesToVisit(self):
        nodes = generateAllNodesToVisit(self.paths1)
        weightOfNode(self.graph1, nodes[0], getCurrentPosition(self.graph1))
        print(nodes)






if __name__ == "__main__":
    unittest.main()