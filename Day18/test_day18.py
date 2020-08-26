import unittest
from Instance import Instance
from day18 import *

class testAStar(unittest.TestCase):
    def setUp(self):
        self.graph1 = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        self.instance1 = Instance(self.graph1)
        self.instance1.updateTokens()
        
    def testCreateGraphFromString(self):
        self.assertEqual(len(self.graph1), 3)
        self.assertEqual(len(self.graph1[0]), 9)
    

    def testValidatePath(self):
        pass
        #self.assertEqual(validatePath(self.paths1), False)
        
    def testGenerateAllNodesToVisit(self):
        nodes = generateAllNodesToVisit(self.instance1.generateAllPossiblePath())
        print(nodes)

    def testNodeWeight(self):
        node = Node("aA")
        node.weight(self.instance1)
        print(node)

    def testGetAllKeys(self):
        nodes = generateAllNodesToVisit(self.instance1.generateAllPossiblePath())
        while nodes:
            node = nodes.pop()
            self.instance1.addSteps(node.weight(self.instance1))
            self.instance1.updateTokens()
            nodes.extend(generateAllNodesToVisit(self.instance1.generateAllPossiblePath()))



if __name__ == "__main__":
    unittest.main()