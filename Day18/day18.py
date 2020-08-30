from Instance import Instance
import copy

class Node():
    def __init__(self, value):
        self.__path = value
        self.__weight = 0
        self.__instance = None
    
    def __repr__(self):
        return ("{value}, {weight}").format(value = self.__path, weight = self.__weight)
    
    def setInstance(self, instance):
        self.__instance = instance
    
    def instance(self):
        return self.__instance
    
    def listKeys(self):
        keys = []
        for elem in self.__path:
            if elem.islower():
                keys.append(elem)
        return keys

    def weight(self):
        path = self.__path
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


def generateAllNodesToVisit(paths, keys=[]):
    nodes = []

    for p in paths:
        truncatedPaths = truncatePath(p, keys)
        
        if len(p) == 1:
            nodes.append(Node("".join(p)))

        for tp in truncatedPaths:
            if tp not in nodes:
                nodes.append(Node("".join(tp)))

    return nodes


def truncatePath(path, keys):
        paths = []
        visited = []
        for elem in path:
            visited.append(elem)

            if len(visited) > 1 and elem.isupper() and validatePath(visited, keys):

                paths.append(visited[:])
                break
            elif elem.isupper():
                break

        return paths


def validatePath(path, keys):
    visited = []

    if len(path) == 0:
        return False

    for elem in path:
        visited.append(elem)
        if elem.isupper():
            if not elem.lower() in keys and not elem.lower() in visited:
                return False
            
    return True


def searchAllPaths(currentInstance):
        nodes = generateAllNodesToVisit(currentInstance.generateAllPossiblePath(), currentInstance.keys())
        total = []

        for n in nodes:
            newInstance = copy.copy(currentInstance)
            newInstance.keyFound(n.listKeys())
            n.setInstance(newInstance)

        while nodes:

            # Add weight
            j = nodes.pop()
            instance = j.instance()
            instance.addSteps(j.weight())
            instance.updateTokens()

            # generate new path
            newNodes = generateAllNodesToVisit(instance.generateAllPossiblePath(), instance.keys())
            
            if  newNodes:
                for n in newNodes:
                    instance2 = copy.deepcopy(instance)
                    instance2.keyFound(n.listKeys())
                    n.setInstance(instance2)
                    nodes.append(n)
            else:
                total.append(instance.nbSteps())
    
        print(min(total))
    

if __name__ == "__main__":
        graph = createGraphFromString("#########\n#b.A.@.a#\n#########\n")
        instance = Instance(graph)
        instance.updateTokens()
        searchAllPaths(instance)
    

