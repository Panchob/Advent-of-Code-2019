import unittest
from Instance import Instance
from day18 import *

class testAStar(unittest.TestCase):
    def setUp(self):
        self.graph1 = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        self.graph2 = createGraphFromString("########################\n#f.D.E.e.C.b.A.@.a.B.c.#\n######################.#\n#d.....................#\n########################\n")
        self.graph3 = createGraphFromString("########################\n#...............b.C.D.f#\n#.######################\n#.....@.a.B.c.d.A.e.F.g#\n########################\n")
        self.graph4 = createGraphFromString("#################\n#i.G..c...e..H.p#\n########.########\n#j.A..b...f..D.o#\n########@########\n#k.E..a...g..B.n#\n########.#########l.F..d...h..C.m#\n#################\n")
        self.graph5 = createGraphFromString("########################\n#@..............ac.GI.b#\n###d#e#f################\n###A#B#C################\n###g#h#i################\n########################\n")
        self.instance1 = Instance(self.graph1)
        self.instance1.updateTokens()
        self.instance2 = Instance(self.graph2)
        self.instance2.updateTokens()
        self.instance3 = Instance(self.graph3)
        self.instance3.updateTokens()
        self.instance4 = Instance(self.graph4)
        self.instance4.updateTokens()
        self.instance5 = Instance(self.graph5)
        self.instance5.updateTokens()

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

    def testSearchAllPaths(self):
        searchAllPaths(self.instance1)
        searchAllPaths(self.instance2)
        #searchAllPaths(self.instance3)
        #searchAllPaths(self.instance4)
        searchAllPaths(self.instance5)


if __name__ == "__main__":
    unittest.main()