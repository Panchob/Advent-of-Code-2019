from Instance import Instance

class Node():
    def __init__(self, value):
        self.__value = value
        self.__weight = 0
    
    def __repr__(self):
        return ("{value}, {weight}").format(value = self.__value, weight = self.__weight)


    def weight(self, instance):
        path = self.__value
        weight = 0

        for c in path:
            weight += instance.nbStepTo(c, instance.position())
            instance.toggleFound()

        self.__weight = weight
        return weight




def createGraphFromString(string):
    graph = []
    line = []
    for character in string:
        if character == '\n':
            graph.append(line[:])
            line = []
        else:
            line.append(character)

    return graph


def generateAllNodesToVisit(paths):
    nodes = []
    for p in paths:
        if validatePath(p):
            nodes.append(Node("".join(p)))
    
    return nodes

def validatePath(path):
    visited = []

    if len(path) == 0:
        return False

    for elem in path:
        if elem.isupper():
            if not elem.lower() in visited:
                return False
        visited.append(elem)
    return True

def searchAllPaths(instance):
        nodes = generateAllNodesToVisit(instance.generateAllPossiblePath())
        while nodes:
            node = nodes.pop()
            instance.addSteps(node.weight(instance))
            instance.updateTokens()
            nodes.extend(generateAllNodesToVisit(instance.generateAllPossiblePath()))

if __name__ == "__main__":
        graph = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        instance = Instance(graph)
        instance.updateTokens()
        searchAllPaths(instance)
    

