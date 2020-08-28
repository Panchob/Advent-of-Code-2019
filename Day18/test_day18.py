import unittest
from Instance import Instance
from day18 import *

class testAStar(unittest.TestCase):
    def setUp(self):
        self.graph1 = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        self.graph2 = createGraphFromString("########################\n#f.D.E.e.C.b.A.@.a.B.c.#\n######################.#\n#d.....................#\n########################\n")
        self.instance1 = Instance(self.graph1)
        self.instance1.updateTokens()
        self.instance2 = Instance(self.graph2)
        self.instance2.updateTokens()
        
    def testCreateGraphFromString(self):
        self.assertEqual(len(self.graph1), 3)
        self.assertEqual(len(self.graph1[0]), 9)
        self.assertEqual(len(self.graph2), 5)
    

    def testValidatePath(self):
        pass
        #self.assertEqual(validatePath(self.paths1), False)
        
    def testGenerateAllNodesToVisit(self):
       self.assertEqual(len(generateAllNodesToVisit(self.instance1.generateAllPossiblePath())), 1)
       self.assertEqual(len(generateAllNodesToVisit(self.instance2.generateAllPossiblePath())), 1)

    def testNodeWeight(self):
        node = Node("aA")
        node.setInstance(self.instance1)
        node.weight()
        print(node)

    def testSearchAllPaths(self):
        searchAllPaths(self.instance1)
        searchAllPaths(self.instance2)


if __name__ == "__main__":
    unittest.main()