from Instance import Instance
import copy

class Node():
    def __init__(self, value):
        self.__value = value
        self.__weight = 0
        self.__instance = None
    
    def __repr__(self):
        return ("{value}, {weight}").format(value = self.__value, weight = self.__weight)
    
    def setInstance(self, instance):
        self.__instance = instance
    
    def instance(self):
        return self.__instance


    def weight(self):
        path = self.__value
        weight = 0

        for c in path:
            weight += self.__instance.nbStepTo(c, self.__instance.position())
            self.__instance.toggleFound()

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
        truncatedPath = truncatePath(p)
        if truncatedPath and validatePath(truncatedPath):
            nodes.append(Node("".join(truncatedPath)))

    return nodes


def truncatePath(path):
        visited = []
        for elem in path:
            visited.append(elem)
            if len(visited) > 1 and elem.isupper() and len(visited) < len(path):
                return visited
        return None


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


def searchAllPaths(currentInstance):
        nodes = generateAllNodesToVisit(currentInstance.generateAllPossiblePath())
        total = []

        for n in nodes:
            newInstance = copy.copy(currentInstance)
            n.setInstance(newInstance)

        while nodes:

            # Add weight
            for j in nodes:
                instance = j.instance()
                instance.addSteps(j.weight())
                instance.updateTokens()

                # generate new path
                newNodes = generateAllNodesToVisit(instance.generateAllPossiblePath())
                nodes.remove(j)
                
                if  newNodes:
                    for n in newNodes:
                        instance2 = copy.copy(instance)
                        n.setInstance(instance2)
                        nodes.append(n)
                else:
                    total.append(instance.nbSteps())
    
        print(total)
        #return(min(total))


if __name__ == "__main__":
        graph = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        instance = Instance(graph)
        instance.updateTokens()
        searchAllPaths(instance)
    

