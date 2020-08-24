from Instance import Instance

class Node():
    def __init__(self, value):
        self.__value = value
        self.__weight = 0
    
    def __repr__(self):
        return ("{value}, {weight}").format(value = self.value, weight = self.weight)
    
    def setWeight(self, weight):
        self.__weight = weight


    def weightOfNode(instance):
        path = self.__value
        lastPosition = instance.getPosition()
        weight = 0

        for c in path:
            isFound = False
            weight += nbStepToNext(goal=c, instance)

        node.setWeight(w)

def nbStepTo(goal, instance, direction=None, steps=0):
    position = instance.getPosition()
    current = instance.getValue()
    res = 0

    if current != '#':
        if current == goal:
            isFound = True
            w += steps
            lastPosition = position
        
        if isFound:
            return 0

        x, y = position
        for d in getDirectionsWithoutBacktracking(direction):
           res += nbStepTo(graph, (x + d[0], y + d[1]), goal, d, steps + 1)
    
    return res


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
    for elem in path:
        if elem.isupper():
            if not elem.lower() in visited:
                return False
        visited.append(elem)
    return True


if __name__ == "__main__":
    pass
    

